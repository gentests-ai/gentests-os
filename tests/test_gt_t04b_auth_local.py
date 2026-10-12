import base64
import copy
import json
import tempfile
import unittest
from pathlib import Path
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ed25519, rsa, padding
from scripts.gt_t04b_auth_local import OfflineGateway,sign_with_existing_key,verify_rs256_jwt

NOW=1791750000
S='a'*40

def compact(v):
    return base64.urlsafe_b64encode(v).decode().rstrip('=')

class AuthContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        # Ephemeral synthetic in-memory test keys only. Never written to files.
        self.ed=ed25519.Ed25519PrivateKey.generate()
        self.edpem=self.ed.private_bytes(serialization.Encoding.PEM,serialization.PrivateFormat.PKCS8,serialization.NoEncryption())
        pub=self.ed.public_key().public_bytes(serialization.Encoding.PEM,serialization.PublicFormat.SubjectPublicKeyInfo)
        self.rsa=rsa.generate_private_key(public_exponent=65537,key_size=2048)
        self.rsa_pub=self.rsa.public_key().public_bytes(serialization.Encoding.PEM,serialization.PublicFormat.SubjectPublicKeyInfo)
        self.g=OfflineGateway(Path(self.tmp.name)/'test.sqlite',public_key_pem=pub,issuer_id='director-test',key_id='synthetic-k1',repo_id=123,actor_id=456,
          auth_workflow_ref='owner/repo/.github/workflows/authorize.yml@refs/heads/main',auth_workflow_sha='b'*40,
          invoke_workflow_ref='owner/repo/.github/workflows/invoke.yml@refs/heads/main',invoke_workflow_sha='c'*40,gateway_sha='d'*40,oidc_public_key_pem=self.rsa_pub)
        self.d=dict(contract_version=1,decision_id='test-1',operation_type='authorize',issuer_key_id='synthetic-k1',issuer_human_id='director-test',
          repository_id=123,issue=47,mission='GT-AI-DISPATCH-001',stage='T04b',generation=1,corpus_sha=S,approved_workflow_sha='c'*40,
          approved_gateway_sha='d'*40,approved_resource='synthetic-worker',scope='synthetic-only',synthetic_only=True,not_before=NOW-20,
          expires_at=NOW+60,nonce='n1',max_calls=1,max_tokens=256,max_units=100,no_paid_fallback=True,max_incremental_cost_brl=0,revocation_epoch=0)

    def jwt(self,route='authorize',**changes):
        payload=dict(iss='https://token.actions.githubusercontent.com',aud='gt-t04b-'+route,iat=NOW-2,nbf=NOW-2,exp=NOW+30,repository_id='123',
         actor_id='456',workflow_ref=self.g.auth_ref if route=='authorize' else self.g.invoke_ref,
         workflow_sha=self.g.auth_sha if route=='authorize' else self.g.invoke_sha,
         ref='refs/heads/main',event_name='workflow_dispatch',run_id='101',run_attempt='1',sub='repo:owner/repo:ref:refs/heads/main')
        payload.update(changes)
        h=compact(json.dumps({'alg':'RS256','typ':'JWT'}).encode()); p=compact(json.dumps(payload).encode()); data=(h+'.'+p).encode()
        sig=compact(self.rsa.sign(data,padding.PKCS1v15(),hashes.SHA256()))
        return h+'.'+p+'.'+sig

    def claims(self,route='authorize',**changes):
        return verify_rs256_jwt(self.jwt(route,**changes),self.rsa_pub,'gt-t04b-'+route,NOW)

    def signature(self,d=None):
        return sign_with_existing_key(d or self.d,self.edpem)

    def authorize(self):
        return self.g.authorize(self.d,self.signature(),self.jwt(),NOW)

    def test_authorize_and_one_invoke(self):
        self.assertEqual(self.authorize()['state'],'recorded')
        event={k:self.d[k] for k in ('mission','stage','generation','corpus_sha','scope','repository_id')}
        self.assertEqual(self.g.invoke('test-1',event,self.jwt('invoke'),NOW)['state'],'reserved_offline')
        self.assertEqual(self.g.invoke('test-1',event,self.jwt('invoke'),NOW)['state'],'blocked')

    def test_signature_modified_content(self):
        d=copy.deepcopy(self.d); d['max_tokens']+=1
        self.assertEqual(self.g.authorize(d,self.signature(),self.jwt(),NOW)['state'],'blocked')

    def test_invalid_signature(self):
        self.assertEqual(self.g.authorize(self.d,compact(b'fake'),self.jwt(),NOW)['state'],'blocked')

    def test_automatic_event_forbidden(self):
        self.assertEqual(self.g.authorize(self.d,self.signature(),self.jwt(event_name='push'),NOW)['state'],'blocked')

    def test_branch_or_workflow_changed(self):
        for kwargs in ({'ref':'refs/heads/feature'}, {'workflow_sha':'e'*40}, {'workflow_ref':self.g.invoke_ref}):
            with self.subTest(kwargs=kwargs):
                self.assertEqual(self.g.authorize(self.d,self.signature(),self.jwt(**kwargs),NOW)['state'],'blocked')

    def test_executor_cannot_authorize(self):
        self.assertEqual(self.g.authorize(self.d,self.signature(),self.jwt('invoke'),NOW)['state'],'blocked')

    def test_non_director(self):
        self.assertEqual(self.g.authorize(self.d,self.signature(),self.jwt(actor_id='999'),NOW)['state'],'blocked')

    def test_replay_signed_decision(self):
        self.assertEqual(self.authorize()['state'],'recorded')
        self.assertEqual(self.authorize()['reason'],'replay')

    def test_missing_and_revoked(self):
        event={k:self.d[k] for k in ('mission','stage','generation','corpus_sha','scope','repository_id')}
        self.assertEqual(self.g.invoke('test-1',event,self.jwt('invoke'),NOW)['state'],'blocked')
        self.authorize()
        rev={**self.d,'operation_type':'revoke','nonce':'n2','revocation_epoch':1}
        self.assertEqual(self.g.authorize(rev,self.signature(rev),self.jwt(),NOW)['state'],'recorded')
        self.assertEqual(self.g.invoke('test-1',event,self.jwt('invoke'),NOW)['state'],'blocked')

    def test_stale_revoke(self):
        self.authorize()
        rev={**self.d,'operation_type':'revoke','nonce':'n2','revocation_epoch':0}
        self.assertEqual(self.g.authorize(rev,self.signature(rev),self.jwt(),NOW)['reason'],'stale_revoke')

    def test_wrong_audience_or_tampered_jwt(self):
        self.assertIsNone(verify_rs256_jwt(self.jwt('invoke'),self.rsa_pub,'gt-t04b-authorize',NOW))
        tok=self.jwt(); parts=tok.split('.'); parts[1]=compact(b'{"forged":true}')
        self.assertIsNone(verify_rs256_jwt('.'.join(parts),self.rsa_pub,'gt-t04b-authorize',NOW))

    def test_expired_claim_and_decision(self):
        self.assertIsNone(verify_rs256_jwt(self.jwt(exp=NOW-1),self.rsa_pub,'gt-t04b-authorize',NOW))
        d={**self.d,'expires_at':NOW}
        self.assertEqual(self.g.authorize(d,self.signature(d),self.jwt(),NOW)['state'],'blocked')

    def test_scope_tamper(self):
        self.authorize()
        event={k:self.d[k] for k in ('mission','stage','generation','corpus_sha','scope','repository_id')}
        event['scope']='write'
        self.assertEqual(self.g.invoke('test-1',event,self.jwt('invoke'),NOW)['reason'],'scope')

    def test_bool_integer_rejected(self):
        d={**self.d,'generation':True}
        self.assertEqual(self.g.authorize(d,self.signature(d),self.jwt(),NOW)['state'],'blocked')

    def test_kill_switch(self):
        with self.g.db() as db: db.execute('UPDATE control SET killed=1 WHERE id=1')
        self.assertEqual(self.authorize()['reason'],'kill_switch')

if __name__ == '__main__': unittest.main()
