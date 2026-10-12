"""GOV-08 mock: deterministic offline authority, SQLite quota and kill switch. No network."""
import hashlib, json, sqlite3
from datetime import datetime

FIELDS=('repo','issue','mission','stage','generation','corpus_sha')
def identity(e): return {k:e[k] for k in FIELDS}
def fingerprint(e): return hashlib.sha256(json.dumps(identity(e),sort_keys=True,separators=(',',':')).encode()).hexdigest()

class FakeAuthority:
    """Decisions provided by the test harness; NOT a signature or human authentication."""
    def __init__(self,decisions): self.decisions=decisions
    def verify(self,e,now):
        ref=e.get('auth_ref')
        if type(ref) is not str or not ref: return 'missing_auth_ref'
        d=self.decisions.get(ref)
        if not isinstance(d,dict) or d.get('status')!='authorized': return 'not_authorized'
        if d.get('revoked') is not False: return 'revoked'
        if type(d.get('version')) is not int or d['version']!=1 or type(e.get('decision_version')) is not int or e['decision_version']!=1: return 'decision_version_mismatch'
        if d.get('scope')!='simulate:synthetic' or e.get('scope')!='simulate:synthetic' or e.get('operation')!='dry_run': return 'scope_denied'
        if e.get('synthetic') is not True or e.get('stage')!='simulate': return 'stage_denied'
        try:
            if (type(e['repo']) is not str or not e['repo'] or type(e['mission']) is not str or not e['mission']
                or type(e['issue']) is not int or e['issue']<1 or type(e['generation']) is not int or e['generation']<1
                or type(e['corpus_sha']) is not str or len(e['corpus_sha'])!=40
                or any(c not in '0123456789abcdef' for c in e['corpus_sha'])): return 'invalid_identity'
            decision_identity=d.get('identity')
            event_identity=identity(e)
            if (type(decision_identity) is not dict or set(decision_identity)!=set(FIELDS)
                or any(type(decision_identity[k]) is not type(event_identity[k]) or decision_identity[k]!=event_identity[k] for k in FIELDS)):
                return 'identity_mismatch'
            limit=datetime.fromisoformat(d['expires_at'].replace('Z','+00:00'))
            if now.tzinfo is None or limit.tzinfo is None or now>=limit: return 'expired'
        except (KeyError,TypeError,ValueError,AttributeError): return 'invalid_decision'
        return None

class LocalGate:
    """SQLite transaction mock, NOT distributed lease/fencing or real financial hard stop."""
    def __init__(self,path,authority): self.path,self.authority=str(path),authority
    def connect(self):
        db=sqlite3.connect(self.path,timeout=5)
        db.execute('PRAGMA busy_timeout=5000')
        db.execute('CREATE TABLE IF NOT EXISTS control (id INTEGER PRIMARY KEY CHECK(id=1),killed INTEGER,used INTEGER,cap INTEGER)')
        db.execute('CREATE TABLE IF NOT EXISTS jobs(k TEXT PRIMARY KEY,state TEXT,fence INTEGER,auth_ref TEXT)')
        db.execute('INSERT OR IGNORE INTO control VALUES(1,0,0,2)')
        db.commit()
        return db
    def set_killed(self,killed):
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            db.execute('UPDATE control SET killed=? WHERE id=1',(1 if killed else 0,))
    def reserve(self,e,now):
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            reason=self.authority.verify(e,now)
            if reason: return {'state':'blocked','reason':reason}
            c=db.execute('SELECT killed,used,cap FROM control WHERE id=1').fetchone()
            if not c or any(type(v) is not int for v in c) or c[0] not in (0,1) or c[1]<0 or c[2]<0 or c[1]>c[2]:
                return {'state':'blocked','reason':'counter_corrupt'}
            if c[0]: return {'state':'blocked','reason':'kill_switch'}
            k=fingerprint(e)
            if db.execute('SELECT state FROM jobs WHERE k=?',(k,)).fetchone():
                return {'state':'blocked','reason':'replay_requires_reconciliation'}
            if c[1]>=c[2]: return {'state':'blocked','reason':'quota_exhausted'}
            db.execute('UPDATE control SET used=used+1 WHERE id=1')
            db.execute('INSERT INTO jobs VALUES(?,?,?,?)',(k,'reserved',1,e['auth_ref']))
            return {'state':'reserved','key':k,'fence':1}
    def effect(self,e,fence,now,failure=None):
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            k=fingerprint(e)
            row=db.execute('SELECT state,fence,auth_ref FROM jobs WHERE k=?',(k,)).fetchone()
            if type(fence) is not int or row!=('reserved',fence,e.get('auth_ref')):
                return {'state':'blocked','reason':'stale_fence_or_state'}
            c=db.execute('SELECT killed,used,cap FROM control WHERE id=1').fetchone()
            reason=self.authority.verify(e,now)
            if (not c or any(type(v) is not int for v in c)
                or c[0] not in (0,1) or c[1]<0 or c[2]<0 or c[1]>c[2]
                or c[0]!=0):
                reason='control_denied'
            if reason or failure is not None:
                db.execute("UPDATE jobs SET state='uncertain' WHERE k=?",(k,))
                return {'state':'blocked','reason':reason or 'synthetic_provider_failure','retry':False}
            db.execute("UPDATE jobs SET state='done' WHERE k=?",(k,))
            return {'state':'done','synthetic':True}

def allowed(principal,operation):
    return principal=='future-actions-reader' and operation=='contents:read'
