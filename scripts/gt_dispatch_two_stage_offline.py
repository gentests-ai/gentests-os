"""ENG-20: deterministic, offline ORQ -> ENG handoff, no LLM or external effects.

Extension of the existing synthetic dispatch/checkpoint concept in gt_dispatch_sim.py.
This executable intentionally does not pretend to create independent ChatGPT agents.
"""
import argparse
import hashlib
import json
import sqlite3
from contextlib import contextmanager
from pathlib import Path

CONTRACTS = ('AGT-ORQ', 'AGT-ENG')
ALLOWED_TYPES = frozenset({'synthetic_diagnostic'})
FIELDS = frozenset({'demand_id', 'run_id', 'type', 'objective', 'synthetic', 'scope'})


def encoded(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(',', ':'))


def fingerprint(value):
    return hashlib.sha256(encoded(value).encode('ascii')).hexdigest()


def check_request(req):
    if type(req) is not dict or set(req) != FIELDS:
        return 'invalid_fields'
    if any(type(req[k]) is not str or not req[k] or not req[k].isascii() for k in ('demand_id','run_id','type','objective','scope')):
        return 'invalid_types'
    if req['synthetic'] is not True or req['scope'] != 'simulate:synthetic' or req['type'] not in ALLOWED_TYPES:
        return 'scope_denied'
    if any(len(req[k]) > 128 for k in ('demand_id','run_id','type','objective')):
        return 'field_too_long'
    return None


@contextmanager
def connect(path):
    db = sqlite3.connect(str(path), timeout=5)
    try:
        db.execute('PRAGMA busy_timeout=5000')
        with db:
            yield db
    finally:
        db.close()


def initialize(db):
    db.execute('''CREATE TABLE IF NOT EXISTS requests (
         run_id TEXT PRIMARY KEY, demand_id TEXT NOT NULL, input_hash TEXT NOT NULL,
         state TEXT NOT NULL, current_stage INTEGER NOT NULL,
         error TEXT)''')
    db.execute('''CREATE TABLE IF NOT EXISTS stages (
         run_id TEXT NOT NULL, ordinal INTEGER NOT NULL, contract TEXT NOT NULL,
         status TEXT NOT NULL, input_hash TEXT NOT NULL, output_json TEXT,
         output_hash TEXT, PRIMARY KEY(run_id, ordinal))''')


def orq_handler(req):
    """Deterministically triage synthetic type using Orchestrator contract."""
    return {'stage': 'triaged', 'owner': 'AGT-ENG', 'demand_id': req['demand_id'],
            'objective': req['objective'], 'source_contract': 'AGT-ORQ'}


def eng_handler(handoff):
    """Consume ORQ result; return synthetic engineering result (not actual work)."""
    if handoff['owner'] != 'AGT-ENG' or handoff['stage'] != 'triaged':
        raise ValueError('invalid_handoff')
    return {'stage': 'analyzed_synthetic', 'demand_id': handoff['demand_id'],
            'source_contract': 'AGT-ENG', 'received_from': handoff['source_contract'],
            'result': 'synthetic_diagnostic_ready', 'objective_hash': fingerprint(handoff['objective'])}


def execute(db_path, req, *, fail_at=None):
    """One caller runs both roles, persisting handoff between stages.

    If a stage fails after reservation, it becomes uncertain; never auto-retries.
    """
    reason = check_request(req)
    if reason:
        return {'state':'blocked', 'reason':reason, 'retry':False}
    if fail_at not in (None, 'AGT-ORQ', 'AGT-ENG'):
        return {'state':'blocked', 'reason':'invalid_failure_hook', 'retry':False}
    request_hash = fingerprint(req)
    with connect(db_path) as db:
        initialize(db)
        db.execute('BEGIN IMMEDIATE')
        prior = db.execute('SELECT input_hash,state FROM requests WHERE run_id=?', (req['run_id'],)).fetchone()
        if prior:
            return {'state':'blocked', 'reason':'duplicate_run' if prior[0]==request_hash else 'run_id_collision',
                    'retry':False, 'run_id':req['run_id']}
        # Only supported pipeline has two steps; fixed (no dynamic model selection).
        db.execute('INSERT INTO requests VALUES(?,?,?,?,?,?)',
                   (req['run_id'],req['demand_id'],request_hash,'running',0,None))
    previous = req
    for index, contract in enumerate(CONTRACTS, 1):
        inp_hash = fingerprint(previous)
        with connect(db_path) as db:
            db.execute('BEGIN IMMEDIATE')
            row = db.execute('SELECT state,current_stage FROM requests WHERE run_id=?',(req['run_id'],)).fetchone()
            if row != ('running',index-1):
                return {'state':'blocked','reason':'invalid_transition','retry':False}
            db.execute('INSERT INTO stages(run_id,ordinal,contract,status,input_hash) VALUES(?,?,?,?,?)',
                       (req['run_id'],index,contract,'reserved',inp_hash))
        try:
            if fail_at == contract:
                raise RuntimeError('synthetic_injected_failure')
            output = orq_handler(previous) if contract == 'AGT-ORQ' else eng_handler(previous)
            if type(output) is not dict or output.get('source_contract') != contract:
                raise ValueError('contract_mismatch')
            with connect(db_path) as db:
                db.execute('BEGIN IMMEDIATE')
                changed = db.execute('''UPDATE stages SET status='done',output_json=?,output_hash=?
                                        WHERE run_id=? AND ordinal=? AND contract=? AND status='reserved' ''',
                                     (encoded(output),fingerprint(output),req['run_id'],index,contract)).rowcount
                if changed != 1:
                    raise RuntimeError('stage_lease_lost')
                db.execute('UPDATE requests SET current_stage=?,state=? WHERE run_id=?',
                           (index,'done' if index == len(CONTRACTS) else 'running',req['run_id']))
            previous = output   # Automatic handoff; no chat, copy or manual intervention.
        except Exception as exc:
            with connect(db_path) as db:
                db.execute('BEGIN IMMEDIATE')
                db.execute("UPDATE stages SET status='uncertain' WHERE run_id=? AND ordinal=? AND status='reserved'",
                           (req['run_id'],index))
                db.execute("UPDATE requests SET state='uncertain',error=? WHERE run_id=? AND state='running'",
                           (type(exc).__name__,req['run_id']))
            return {'state':'uncertain','run_id':req['run_id'],'failed_stage':contract,
                    'reason':type(exc).__name__, 'retry':False}
    return {'state':'done','run_id':req['run_id'],'demand_id':req['demand_id'],
            'stages':list(CONTRACTS),'result':previous,'retry':False}


def evidence(db_path, run_id):
    with connect(db_path) as db:
        initialize(db)
        req = db.execute('SELECT demand_id,input_hash,state,current_stage,error FROM requests WHERE run_id=?',(run_id,)).fetchone()
        stages = db.execute('''SELECT ordinal,contract,status,input_hash,output_hash,output_json
                               FROM stages WHERE run_id=? ORDER BY ordinal''',(run_id,)).fetchall()
    return {'run_id':run_id,'request': None if req is None else {
            'demand_id':req[0],'input_hash':req[1],'state':req[2],
            'current_stage':req[3],'error':req[4]},
            'stages':[{'ordinal':r[0],'contract':r[1],'status':r[2],
                       'input_hash':r[3],'output_hash':r[4],
                       'output':json.loads(r[5]) if r[5] else None} for r in stages]}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--db',type=Path,required=True)
    p.add_argument('--fixture',type=Path,required=True)
    p.add_argument('--fail-at',choices=CONTRACTS)
    args=p.parse_args()
    try:
        request=json.loads(args.fixture.read_text(encoding='utf-8'))
        result=execute(args.db,request,fail_at=args.fail_at)
        print(encoded({'execution':result,'evidence':evidence(args.db,request.get('run_id',''))}))
        return 0 if result['state']=='done' else 2
    except (OSError,ValueError,KeyError,sqlite3.Error) as exc:
        print(encoded({'state':'blocked','reason':type(exc).__name__}))
        return 2

if __name__=='__main__':
    raise SystemExit(main())
