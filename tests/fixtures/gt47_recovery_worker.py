"""Separate-process recovery fixture. Never uses a network transport or secrets."""
import argparse
import json
import os
from pathlib import Path
import sqlite3
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.gt47_t06_groq_runner import enqueue, inspect_queue, run_once
from scripts.gt47_t06_groq_handoff import MODEL

class SQLiteStore:
    def __init__(self, path):
        self.path = str(path)
        with sqlite3.connect(self.path) as db:
            db.execute('CREATE TABLE IF NOT EXISTS state (key TEXT PRIMARY KEY, value TEXT, version INTEGER)')
            db.execute('CREATE TABLE IF NOT EXISTS calls (agent TEXT)')
    def get(self, path):
        with sqlite3.connect(self.path) as db:
            value = db.execute('SELECT value,version FROM state WHERE key=?',(path,)).fetchone()
        return (json.loads(value[0]),value[1]) if value else (None,None)
    def put(self, path, value, version):
        with sqlite3.connect(self.path,timeout=10) as db:
            db.execute('BEGIN IMMEDIATE')
            current=db.execute('SELECT version FROM state WHERE key=?',(path,)).fetchone()
            if (current[0] if current else None) != version:
                return False
            db.execute('INSERT OR REPLACE INTO state VALUES(?,?,?)',
                       (path,json.dumps(value),(version or 0)+1))
        return True
    def read(self):
        value, version=self.get('gt47-budget.json')
        return ({'schema':1,'claims':{}} if value is None else value),version
    def cas(self, version, value):
        return self.put('gt47-budget.json',value,version)

def fake_transport(store, *, marker=None):
    def call(payload):
        agent='AGT-QA' if payload['messages'][0]['content'].startswith('QA:') else 'AGT-ENG'
        with sqlite3.connect(store.path) as db:
            db.execute('INSERT INTO calls VALUES(?)',(agent,))
        if marker:
            Path(marker).write_text('reserved-and-submitted')
            while True:
                time.sleep(1)  # Parent sends a real SIGTERM; no model or network.
        return {'model':MODEL,'usage':{'prompt_tokens':400,'completion_tokens':100,'total_tokens':500},
                'choices':[{'finish_reason':'stop','message':{'content':json.dumps({
                    'summary':'Scoped offline fixture.', 'findings':[],
                    'recommendation':'ready_for_finalization'})}}]}
    return call

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--db',required=True)
    parser.add_argument('--action',choices=('seed','tick','inspect','interrupt','cli-inspect','cli-enqueue'),required=True)
    parser.add_argument('--now',type=int,required=True)
    parser.add_argument('--marker')
    parser.add_argument('--task',default='Different task rejected by the single-slot queue.')
    args=parser.parse_args()
    store=SQLiteStore(args.db)
    if args.action.startswith('cli-'):
        from scripts import gt47_t06_groq_runner as runner
        # Exercise PRODUCTION argparse/exit handling, replacing only transport
        # storage with an actual durable local store. No GitHub/Groq access.
        runner.GitHubStore=lambda token: store
        store.initialize=lambda commit: None
        runner.time.time=lambda: args.now
        os.environ.update(GT47_GROQ_ENABLED='true',GROQ_FREE_PLAN_CONFIRMED='true',
                          GH_TOKEN='offline-fixture',GROQ_API_KEY='offline-fixture')
        sys.argv=['gt47-runner','--inspect']
        if args.action=='cli-enqueue':
            task_file=Path(args.db).parent/'cli-task.txt'
            task_file.write_text(args.task,encoding='utf-8')
            sys.argv=['gt47-runner','--commit','a'*40,'--enqueue',str(task_file)]
        runner.main()
        return 0
    if args.action=='seed':
        result=enqueue(store,commit='a'*40,task='Verify offline recovery.')
    elif args.action=='inspect':
        result=inspect_queue(store,now=args.now)
    else:
        result=run_once(store,now=args.now,api_key='offline-fixture',enabled=True,
                        free_plan_confirmed=True,transport=fake_transport(store,
                        marker=args.marker if args.action=='interrupt' else None))
    print(json.dumps(result),flush=True)
    return 2 if result.get('status')=='manual_reconciliation_required' else 0

if __name__=='__main__':
    raise SystemExit(main())
