"""GT-AI-DISPATCH-001 T04b offline reference; NEVER a deployed gateway.

Requires cryptography for Ed25519 and RS256. All JWT keys and decisions in tests
are ephemeral synthetic fixtures. No network, IAM, secrets, or cloud APIs.
"""
import base64
import hashlib
import json
import re
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ed25519, padding

DOMAIN = b'GT-T04B-AUTH-v1\x00'
ALLOWED_OFFLINE_SCOPES = frozenset({'synthetic-only'})
EVENT_FIELDS = ('mission', 'stage', 'generation', 'corpus_sha', 'scope', 'repository_id')
DECIMAL_ID = re.compile(r'(?:0|[1-9][0-9]*)\Z', re.ASCII)
FIELDS = {'contract_version', 'decision_id', 'operation_type', 'issuer_key_id',
          'issuer_human_id', 'repository_id', 'issue', 'mission', 'stage',
          'generation', 'corpus_sha', 'approved_workflow_sha', 'approved_gateway_sha',
          'approved_resource', 'scope', 'synthetic_only', 'not_before', 'expires_at',
          'nonce', 'max_calls', 'max_tokens', 'max_units', 'no_paid_fallback',
          'max_incremental_cost_brl', 'revocation_epoch'}


def canonical(obj):
    """Restricted JSON canonicalization (ASCII schema only); NOT RFC8785 generic."""
    return json.dumps(obj, sort_keys=True, ensure_ascii=True, separators=(',', ':'),
                      allow_nan=False).encode('ascii')


def signed_bytes(obj):
    return DOMAIN + canonical(obj)


def sign_with_existing_key(decision, private_key_pem):
    """No generation or persistence. Private key supplied by caller (not by GitHub)."""
    key = serialization.load_pem_private_key(private_key_pem, password=None)
    if not isinstance(key, ed25519.Ed25519PrivateKey):
        raise ValueError('Ed25519 required')
    return base64.urlsafe_b64encode(key.sign(signed_bytes(decision))).decode().rstrip('=')


def b64url_decode(value):
    if type(value) is not str or not value or any(c not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_' for c in value):
        raise ValueError('invalid base64url')
    return base64.urlsafe_b64decode(value + '=' * (-len(value) % 4))


def unix_time(value):
    if type(value) is not int:
        raise ValueError('timestamp must be int')
    return value


def validated_decision(d, now):
    if type(d) is not dict or set(d) != FIELDS:
        return False
    if any(type(d[k]) is not int for k in ('contract_version','repository_id','issue','generation','not_before','expires_at','max_calls','max_tokens','max_units','max_incremental_cost_brl','revocation_epoch')):
        return False
    if d['contract_version'] != 1 or d['max_calls'] != 1 or d['max_incremental_cost_brl'] != 0 or d['revocation_epoch'] < 0 or d['repository_id'] <= 0 or d['issue'] <= 0 or d['generation'] <= 0 or d['max_tokens'] <= 0 or d['max_units'] <= 0:
        return False
    if (d['synthetic_only'] is not True or d['no_paid_fallback'] is not True
            or d['operation_type'] not in ('authorize','revoke')
            or type(d['scope']) is not str
            or d['scope'] not in ALLOWED_OFFLINE_SCOPES):
        return False
    for field in FIELDS - {'contract_version','repository_id','issue','generation','not_before','expires_at','max_calls','max_tokens','max_units','max_incremental_cost_brl','revocation_epoch','synthetic_only','no_paid_fallback'}:
        if type(d[field]) is not str or not d[field] or any(ord(c) > 127 for c in d[field]):
            return False
    if len(d['corpus_sha']) != 40 or any(c not in '0123456789abcdef' for c in d['corpus_sha']):
        return False
    if len(d['approved_workflow_sha']) != 40 or len(d['approved_gateway_sha']) != 40:
        return False
    if d['not_before'] > now or now >= d['expires_at'] or d['expires_at'] <= d['not_before']:
        return False
    return True


def verify_decision(d, signature, pem, now):
    if not validated_decision(d, now):
        return False
    try:
        key = serialization.load_pem_public_key(pem)
        if not isinstance(key, ed25519.Ed25519PublicKey):
            return False
        key.verify(b64url_decode(signature), signed_bytes(d))
        return True
    except (ValueError, TypeError, InvalidSignature):
        return False


class OfflineGateway:
    """SQLite-backed policy reference, never listens on a port."""
    def __init__(self, sqlite_file, *, public_key_pem, issuer_id, key_id,
                 repo_id, actor_id, auth_workflow_ref, auth_workflow_sha,
                 invoke_workflow_ref, invoke_workflow_sha, gateway_sha, oidc_public_key_pem):
        self.sqlite_file = str(sqlite_file)
        self.public_key_pem = public_key_pem
        self.issuer_id, self.key_id = issuer_id, key_id
        self.repo_id, self.actor_id = repo_id, actor_id
        self.auth_ref, self.auth_sha = auth_workflow_ref, auth_workflow_sha
        self.invoke_ref, self.invoke_sha = invoke_workflow_ref, invoke_workflow_sha
        # Repository identity is pinned from the approved workflow reference.
        self.expected_sub = 'repo:' + invoke_workflow_ref.split('/.github/workflows/', 1)[0] + ':ref:refs/heads/main'
        self.gateway_sha = gateway_sha
        self.oidc_public_key_pem = oidc_public_key_pem
        with self.db() as db:
            db.execute('CREATE TABLE IF NOT EXISTS decisions (id TEXT PRIMARY KEY, payload TEXT NOT NULL, revocation_epoch INTEGER NOT NULL, revoked INTEGER NOT NULL DEFAULT 0, invoked INTEGER NOT NULL DEFAULT 0)')
            db.execute('CREATE TABLE IF NOT EXISTS nonces (nonce TEXT PRIMARY KEY)')
            db.execute('CREATE TABLE IF NOT EXISTS runs (runkey TEXT PRIMARY KEY)')
            db.execute('CREATE TABLE IF NOT EXISTS control (id INTEGER PRIMARY KEY CHECK(id=1), killed INTEGER NOT NULL)')
            db.execute('INSERT OR IGNORE INTO control VALUES(1,0)')

    @contextmanager
    def db(self):
        db = sqlite3.connect(self.sqlite_file, timeout=10)
        try:
            db.execute('PRAGMA busy_timeout=10000')
            with db:
                yield db
        finally:
            db.close()

    def _claims(self, claims, *, route, now):
        """Claims MUST be from verified JWT, not untrusted decoded JSON."""
        if type(claims) is not dict or claims.get('_jwt_verified') is not True:
            return False
        ref, sha, audience = ((self.auth_ref, self.auth_sha, 'gt-t04b-authorize') if route == 'authorize' else
                              (self.invoke_ref, self.invoke_sha, 'gt-t04b-invoke'))
        return (claims.get('aud') == audience and claims.get('repository_id') == str(self.repo_id)
                and claims.get('workflow_ref') == ref and claims.get('workflow_sha') == sha
                and claims.get('ref') == 'refs/heads/main' and claims.get('event_name') == 'workflow_dispatch'
                and type(claims.get('actor_id')) is str
                and (route != 'authorize' or claims.get('actor_id') == str(self.actor_id))
                and claims.get('sub') == self.expected_sub
                and all(type(claims.get(k)) is str and claims[k] for k in ('run_id','run_attempt'))
                and all(DECIMAL_ID.fullmatch(claims[k]) for k in ('run_id','run_attempt'))
                and type(claims.get('exp')) is int and claims['exp'] > now)

    def authorize(self, decision, signature, jwt, now):
        claims = verify_rs256_jwt(jwt, self.oidc_public_key_pem, 'gt-t04b-authorize', now)
        if not self._claims(claims, route='authorize', now=now):
            return {'state':'blocked','reason':'oidc'}
        if not verify_decision(decision,signature,self.public_key_pem,now):
            return {'state':'blocked','reason':'signature_or_schema'}
        if (decision['issuer_human_id'] != self.issuer_id or decision['issuer_key_id'] != self.key_id
            or decision['repository_id'] != self.repo_id or decision['approved_workflow_sha'] != self.invoke_sha
            or decision['approved_gateway_sha'] != self.gateway_sha):
            return {'state':'blocked','reason':'binding'}
        with self.db() as db:
            db.execute('BEGIN IMMEDIATE')
            if db.execute('SELECT killed FROM control WHERE id=1').fetchone() != (0,):
                return {'state':'blocked','reason':'kill_switch'}
            if db.execute('SELECT 1 FROM nonces WHERE nonce=?',(decision['nonce'],)).fetchone():
                return {'state':'blocked','reason':'replay'}
            if decision['operation_type'] == 'authorize':
                if db.execute('SELECT 1 FROM decisions WHERE id=?',(decision['decision_id'],)).fetchone():
                    return {'state':'blocked','reason':'duplicate'}
                db.execute('INSERT INTO decisions(id,payload,revocation_epoch) VALUES(?,?,?)',
                           (decision['decision_id'],canonical(decision).decode('ascii'),decision['revocation_epoch']))
            else:
                old = db.execute('SELECT revocation_epoch,revoked FROM decisions WHERE id=?',(decision['decision_id'],)).fetchone()
                if not old or decision['revocation_epoch'] <= old[0] or old[1]:
                    return {'state':'blocked','reason':'stale_revoke'}
                db.execute('UPDATE decisions SET revoked=1,revocation_epoch=? WHERE id=?',
                           (decision['revocation_epoch'],decision['decision_id']))
            db.execute('INSERT INTO nonces VALUES(?)',(decision['nonce'],))
            return {'state':'recorded','operation':decision['operation_type']}

    def invoke(self, decision_id, event, jwt, now):
        claims = verify_rs256_jwt(jwt, self.oidc_public_key_pem, 'gt-t04b-invoke', now)
        if not self._claims(claims, route='invoke', now=now):
            return {'state':'blocked','reason':'oidc','retry':False}
        if type(event) is not dict or type(decision_id) is not str:
            return {'state':'blocked','reason':'invalid_event','retry':False}
        with self.db() as db:
            db.execute('BEGIN IMMEDIATE')
            if db.execute('SELECT killed FROM control WHERE id=1').fetchone() != (0,):
                return {'state':'blocked','reason':'kill_switch','retry':False}
            record = db.execute('SELECT payload,revoked,invoked FROM decisions WHERE id=?',(decision_id,)).fetchone()
            if not record or record[1] or record[2]:
                return {'state':'blocked','reason':'missing_revoked_or_replay','retry':False}
            decision = json.loads(record[0])
            if not validated_decision(decision,now):
                return {'state':'blocked','reason':'expired','retry':False}
            expected = {k:decision[k] for k in ('mission','stage','generation','corpus_sha','scope','repository_id')}
            if (set(event) != set(expected)
                    or any(type(event[k]) is not type(expected[k]) or event[k] != expected[k]
                           for k in expected)
                    or decision['scope'] not in ALLOWED_OFFLINE_SCOPES):
                return {'state':'blocked','reason':'scope','retry':False}
            # An OIDC-signed synthetic token is explicitly bound to this decision;
            # a valid token for decision A cannot reserve decision B.
            context = {'decision_id': decision_id, 'issue': str(decision['issue']),
                       'approved_resource': decision['approved_resource'],
                       'mission': decision['mission'], 'stage': decision['stage'],
                       'generation': str(decision['generation']),
                       'corpus_sha': decision['corpus_sha']}
            if any(type(claims.get(k)) is not str or claims[k] != v for k,v in context.items()):
                return {'state':'blocked','reason':'jwt_context','retry':False}
            runkey = canonical([claims['run_id'],claims['run_attempt']]).decode('ascii')
            if db.execute('SELECT 1 FROM runs WHERE runkey=?',(runkey,)).fetchone():
                return {'state':'blocked','reason':'replay_run','retry':False}
            db.execute('INSERT INTO runs VALUES(?)',(runkey,))
            db.execute('UPDATE decisions SET invoked=1 WHERE id=? AND invoked=0',(decision_id,))
            return {'state':'reserved_offline','retry':False,'no_inference':True}


def verify_rs256_jwt(token, pem, audience, now):
    """Offline verifier of RS256 signature/claims against preapproved public key.

    Production must fetch/cache/rotate the GitHub JWKS securely, validate issuer,
    audience and OIDC claim policy, and never trust a token-provided key URL.
    """
    try:
        header_raw, payload_raw, sig_raw = token.split('.')
        header = json.loads(b64url_decode(header_raw))
        payload = json.loads(b64url_decode(payload_raw))
        if header != {'alg':'RS256','typ':'JWT'}:
            return None
        key = serialization.load_pem_public_key(pem)
        key.verify(b64url_decode(sig_raw), (header_raw+'.'+payload_raw).encode(),
                   padding.PKCS1v15(), hashes.SHA256())
        if payload.get('iss') != 'https://token.actions.githubusercontent.com' or payload.get('aud') != audience:
            return None
        if not all(type(payload.get(k)) is int for k in ('iat','nbf','exp')):
            return None
        if payload['iat'] > now or payload['nbf'] > now or payload['exp'] <= now:
            return None
        return {**payload,'_jwt_verified':True}
    except (ValueError,TypeError,KeyError,InvalidSignature,AttributeError):
        return None
