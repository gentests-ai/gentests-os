"""Offline GOV-08 negative contract tests. Python stdlib/SQLite only."""
import copy, sqlite3, tempfile, unittest
from datetime import datetime,timezone
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from scripts.gt_t05_security_mock import FakeAuthority,LocalGate,allowed,identity
NOW=datetime(2026,10,11,20,tzinfo=timezone.utc)
BASE=dict(repo='synthetic/example',issue=123,mission='SYNTH-001',stage='simulate',generation=1,corpus_sha='f'*40,scope='simulate:synthetic',operation='dry_run',synthetic=True,auth_ref='TEST-DEC-001',decision_version=1)
class SecurityMockTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.e=copy.deepcopy(BASE)
        self.d={'TEST-DEC-001':dict(status='authorized',revoked=False,version=1,scope='simulate:synthetic',expires_at='2026-10-12T00:00:00Z',identity=identity(self.e))}
        self.g=LocalGate(Path(self.tmp.name)/'test.sqlite',FakeAuthority(self.d))
    def test_success_and_replay(self):
        r=self.g.reserve(self.e,NOW);self.assertEqual(r['state'],'reserved')
        self.assertEqual(self.g.effect(self.e,r['fence'],NOW)['state'],'done')
        self.assertEqual(self.g.reserve(self.e,NOW)['reason'],'replay_requires_reconciliation')
    def test_fake_approval(self):
        self.e['approved']=True;self.e['comment']='director approved';self.e['auth_ref']='fake'
        self.assertEqual(self.g.reserve(self.e,NOW)['reason'],'not_authorized')
        del self.e['auth_ref']
        self.assertEqual(self.g.reserve(self.e,NOW)['reason'],'missing_auth_ref')
    def test_identity_scope_version_sha(self):
        for field,value in [('repo','other'),('issue',124),('mission','other'),('stage','merge'),('generation',2),('corpus_sha','e'*40),('decision_version',2),('scope','admin')]:
            with self.subTest(field=field):
                e=copy.deepcopy(self.e);e[field]=value
                self.assertEqual(self.g.reserve(e,NOW)['state'],'blocked')
    def test_revocation_and_expiry(self):
        self.d['TEST-DEC-001']['revoked']=True
        self.assertEqual(self.g.reserve(self.e,NOW)['reason'],'revoked')
        self.d['TEST-DEC-001']['revoked']=False;self.d['TEST-DEC-001']['expires_at']='2026-10-11T20:00:00Z'
        self.assertEqual(self.g.reserve(self.e,NOW)['reason'],'expired')
    def test_revocation_between_reserve_and_effect(self):
        r=self.g.reserve(self.e,NOW);self.d['TEST-DEC-001']['revoked']=True
        self.assertEqual(self.g.effect(self.e,r['fence'],NOW)['reason'],'revoked')
        self.assertEqual(self.g.effect(self.e,r['fence'],NOW)['reason'],'stale_fence_or_state')
    def test_kill_switch_after_reserve(self):
        r=self.g.reserve(self.e,NOW);self.g.set_killed(True)
        self.assertEqual(self.g.effect(self.e,r['fence'],NOW)['reason'],'control_denied')
    def test_quota_and_corruption(self):
        with self.g.connect() as db: db.execute('UPDATE control SET cap=1')
        self.assertEqual(self.g.reserve(self.e,NOW)['state'],'reserved')
        e=copy.deepcopy(self.e);e['generation']=2;self.d['TEST-DEC-001']['identity']=identity(e)
        self.assertEqual(self.g.reserve(e,NOW)['reason'],'quota_exhausted')
        with self.g.connect() as db:db.execute('UPDATE control SET used=-1')
        self.assertEqual(self.g.reserve(e,NOW)['reason'],'counter_corrupt')
    def test_synthetic_provider_timeout_no_retry(self):
        r=self.g.reserve(self.e,NOW)
        self.assertIs(self.g.effect(self.e,r['fence'],NOW,failure='timeout')['retry'],False)
        self.assertEqual(self.g.effect(self.e,r['fence'],NOW)['state'],'blocked')
    def test_fence_and_allowlist(self):
        r=self.g.reserve(self.e,NOW)
        self.assertEqual(self.g.effect(self.e,r['fence']+1,NOW)['reason'],'stale_fence_or_state')
        self.assertTrue(allowed('future-actions-reader','contents:read'))
        for op in ('contents:write','merge','publish','permissions:write','shell','workflow_dispatch'):
            self.assertFalse(allowed('future-actions-reader',op))
    def test_concurrent_reserve(self):
        with ThreadPoolExecutor(max_workers=2) as pool:
            results=list(pool.map(lambda _:self.g.reserve(self.e,NOW),range(2)))
        self.assertEqual(sorted(x['state'] for x in results),['blocked','reserved'])

    def test_qa05_a01_exact_types_in_decision(self):
        for field in ('version',):
            with self.subTest(field=field):
                self.d['TEST-DEC-001'][field]=True
                self.assertEqual(self.g.reserve(self.e,NOW)['reason'],'decision_version_mismatch')
                self.d['TEST-DEC-001'][field]=1
        for field in ('generation','issue'):
            with self.subTest(field=field):
                original=self.d['TEST-DEC-001']['identity'][field]
                self.d['TEST-DEC-001']['identity'][field]=True
                self.assertEqual(self.g.reserve(self.e,NOW)['reason'],'identity_mismatch')
                self.d['TEST-DEC-001']['identity'][field]=original

    def test_qa05_a02_corrupt_counters_after_reserve(self):
        for field,sql_value in (('used',1.5),('cap',1.5),('used','bogus'),('cap','bogus'),
                                ('used',None),('cap',None),('killed',None),('killed',1.5),
                                ('used',-1),('cap',-1),('used',9)):
            with self.subTest(field=field,value=repr(sql_value)):
                with tempfile.TemporaryDirectory() as t:
                    gate=LocalGate(Path(t)/'db.sqlite',FakeAuthority(self.d))
                    reserved=gate.reserve(self.e,NOW)
                    self.assertEqual(reserved['state'],'reserved')
                    with gate.connect() as db:
                        db.execute('UPDATE control SET '+field+'=? WHERE id=1',(sql_value,))
                    result=gate.effect(self.e,reserved['fence'],NOW)
                    self.assertEqual(result['state'],'blocked')
                    self.assertEqual(result['reason'],'control_denied')
                    self.assertIs(result['retry'],False)
                    with gate.connect() as db:
                        state=db.execute('SELECT state FROM jobs WHERE k=?',(reserved['key'],)).fetchone()
                    self.assertEqual(state,('uncertain',))

if __name__=='__main__':unittest.main()
