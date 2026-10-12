"""Recovery through fresh OS processes and a real killed worker, no inference.

Elapsed times are injected. These checks are not GitHub runner/scheduler evidence.
"""
import json
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import time
import unittest

from scripts.gt47_t06_groq_budget import BudgetWaiting, ReconciliationRequired
from scripts.gt47_t06_groq_runner import inspect_queue, run_once
from test_gt47_t06_groq_handoff import MemoryStore, enqueue, response, SHA, NOW
from scripts.gt47_t06_recovery_rehearsal import test_branch, synthetic_provider
from scripts.gt47_t06_groq_runner import GitHubStore

ROOT=Path(__file__).resolve().parents[1]
WORKER=ROOT/'tests/fixtures/gt47_recovery_worker.py'

class ProcessRecoveryTests(unittest.TestCase):
    def setUp(self):
        directory=tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root=Path(directory.name)
        self.db=self.root/'durable.sqlite'
    def command(self,action,now):
        return [sys.executable,str(WORKER),'--db',str(self.db),'--action',action,'--now',str(now)]
    def tick(self,action,now,expected=0):
        result=subprocess.run(self.command(action,now),cwd=ROOT,capture_output=True,text=True,timeout=10)
        self.assertEqual(result.returncode,expected,result.stderr)
        return json.loads(result.stdout)
    def calls(self):
        with sqlite3.connect(self.db) as db:
            return [r[0] for r in db.execute('SELECT agent FROM calls')]

    def test_ct01_late_fresh_worker_preserves_task(self):
        self.tick('seed',NOW)
        self.assertEqual(self.tick('inspect',NOW+601)['status'],'ready')
        self.assertEqual(self.calls(),[])
        self.assertEqual(self.tick('tick',NOW+601)['status'],'qa_pending')
        self.assertEqual(self.tick('tick',NOW+901)['status'],'completed')
        self.assertEqual(self.calls(),['AGT-ENG','AGT-QA'])

    def test_ct02_absent_pending_worker_cannot_lose_durable_queue(self):
        self.tick('seed',NOW)
        # No worker is started for the intervening ticks. This models lost
        # opportunities, not a proof of GitHub's pending-run replacement.
        for offset in (300,600,900):
            self.assertEqual(self.tick('inspect',NOW+offset)['status'],'ready')
        self.tick('tick',NOW+1200)
        self.assertEqual(self.calls(),['AGT-ENG'])

    def test_ct03_real_process_termination_requires_reconciliation(self):
        self.tick('seed',NOW)
        marker=self.root/'submitted'
        child=subprocess.Popen(self.command('interrupt',NOW)+['--marker',str(marker)],
                               cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        try:
            deadline=time.monotonic()+5
            while not marker.exists() and time.monotonic()<deadline:
                time.sleep(.02)
            self.assertTrue(marker.exists(),'worker did not reach reserved submission')
            child.terminate()
            child.communicate(timeout=5)
            self.assertNotEqual(child.returncode,0)
        finally:
            if child.poll() is None:
                child.kill()
                child.communicate()
        preflight=self.tick('inspect',NOW+600,expected=2)
        self.assertEqual(preflight['status'],'manual_reconciliation_required')
        self.assertEqual(preflight['reason'],'reserved_without_matching_result')
        self.tick('tick',NOW+600,expected=2)
        self.tick('tick',NOW+900,expected=2)
        self.assertEqual(self.calls(),['AGT-ENG'])

    def test_ct04_qa_fresh_process_obeys_cooldown(self):
        self.tick('seed',NOW)
        self.tick('tick',NOW)
        result=self.tick('tick',NOW+299)
        self.assertEqual(result['status'],'waiting')
        self.assertEqual(result['retry_at'],NOW+300)
        self.assertEqual(self.calls(),['AGT-ENG'])
        self.assertEqual(self.tick('tick',NOW+300)['status'],'completed')
        self.assertEqual(self.calls(),['AGT-ENG','AGT-QA'])

    def test_ct05_empty_preflight_never_submits(self):
        self.assertEqual(self.tick('inspect',NOW)['status'],'idle')
        self.assertEqual(self.calls(),[])
        with sqlite3.connect(self.db) as db:
            self.assertEqual(db.execute('SELECT count(*) FROM state').fetchone()[0],0)

    def test_ct06_ledger_survives_process_changes_and_replay(self):
        self.tick('seed',NOW)
        self.tick('tick',NOW)
        self.tick('tick',NOW+300)
        self.assertEqual(self.tick('tick',NOW+86400)['status'],'idle')
        with sqlite3.connect(self.db) as db:
            state=json.loads(db.execute('SELECT value FROM state WHERE key=?',('gt47-budget.json',)).fetchone()[0])
        self.assertEqual(len(state['claims']),2)
        self.assertEqual(sum(c['tokens'] for c in state['claims'].values()),8000)
        self.assertEqual(self.calls(),['AGT-ENG','AGT-QA'])

class DiagnosticTests(unittest.TestCase):
    def test_corrupt_queue_reports_manual_not_idle(self):
        for value in ([],['malformed'],{'status':'engineering_pending','diagnostic':'malformed'}):
            store=MemoryStore()
            store.put('gt47-current.json',value,None)
            self.assertEqual(inspect_queue(store,now=NOW)['status'],'manual_reconciliation_required')
    def test_wait_and_uncertainty_have_different_machine_states(self):
        self.assertEqual(BudgetWaiting('quota').status,'waiting')
        self.assertEqual(ReconciliationRequired('timeout').status,'manual_reconciliation_required')
    def test_preflight_is_read_only(self):
        store=MemoryStore()
        store.put=lambda *args: self.fail('preflight attempted a write')
        store.cas=lambda *args: self.fail('preflight attempted a reservation')
        self.assertEqual(inspect_queue(store,now=NOW),{'status':'idle'})
    def test_provider_error_has_persisted_diagnosis_no_second_call(self):
        store=MemoryStore()
        enqueue(store,commit=SHA,task='Review the regression.')
        calls=[]
        def fail(payload):
            calls.append(payload)
            raise TimeoutError('not printed')
        args=dict(api_key='offline-test',enabled=True,free_plan_confirmed=True,transport=fail)
        result=run_once(store,now=NOW,**args)
        self.assertEqual(result['status'],'manual_reconciliation_required')
        self.assertEqual(store.get('gt47-current.json')[0]['diagnostic'],result)
        self.assertEqual(inspect_queue(store,now=NOW+300)['status'],'manual_reconciliation_required')
        run_once(store,now=NOW+300,**args)
        self.assertEqual(len(calls),1)

class RehearsalSafetyTests(unittest.TestCase):
    def test_trial_cannot_target_production_branch(self):
        self.assertEqual(test_branch('qa-trial-001'),'gt47-recovery-qa-trial-001')
        for trial in ('../gt47-advisory-state','',None,'UPPERCASE','a'*41):
            with self.assertRaises(ValueError):
                test_branch(trial)
        with self.assertRaises(ValueError):
            GitHubStore('offline-test',branch='main')

    def test_rehearsal_no_optin_exits_before_github(self):
        result=subprocess.run([sys.executable,'-m','scripts.gt47_t06_recovery_rehearsal',
            '--trial','qa-trial-001','--commit',SHA,'--phase','seed'],cwd=ROOT,
            capture_output=True,text=True,timeout=10)
        self.assertEqual(result.returncode,2)
        self.assertIn('explicit isolated-state-write opt-in',result.stderr)

    def test_test_branch_used_for_every_state_read_and_write(self):
        store=GitHubStore('offline-test',branch=test_branch('qa-trial-001'))
        seen=[]
        def request(method,path,body=None):
            seen.append((method,path,body))
            return (404,None) if method=='GET' else (201,{})
        store.request=request
        store.initialize(SHA)
        store.get('gt47-current.json')
        store.put('gt47-current.json',{},None)
        self.assertTrue(all('gt47-advisory-state' not in json.dumps(v) for v in seen))
        self.assertIn('?ref=gt47-recovery-qa-trial-001',seen[2][1])
        self.assertEqual(seen[-1][2]['branch'],'gt47-recovery-qa-trial-001')

    def test_synthetic_provider_journals_without_inference(self):
        store=MemoryStore()
        provider=synthetic_provider(store)
        payload={'messages':[{'content':'QA: synthetic fixture'}]}
        result=provider(payload)
        self.assertEqual(result['model'],'openai/gpt-oss-120b')
        self.assertEqual(store.get('gt47-test-submissions.json')[0][0]['agent'],'AGT-QA')
        self.assertTrue(store.get('gt47-test-submissions.json')[0][0]['synthetic'])
