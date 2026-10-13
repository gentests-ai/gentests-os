"""Explicit new rounds preserve unresolved attempts and global quota claims."""
import copy
from pathlib import Path
import unittest
from scripts.gt47_t06_groq_runner import start_new_round, EnqueueRejected, enqueue
from scripts.gt47_t06_groq_budget import ReconciliationRequired
from scripts.gt47_t06_groq_handoff import prepare
from tests.test_gt47_t06_groq_handoff import MemoryStore, SHA, NOW

class NewRoundTests(unittest.TestCase):
    def setUp(self):
        self.store = MemoryStore()
        self.old = enqueue(self.store, commit=SHA, task='Previous attempt')
        self.old['diagnostic'] = {'status': 'manual_reconciliation_required', 'reason': 'provider_or_state_failure'}
        self.store.put('gt47-current.json', self.old, 1)
        self.budget = {'schema': 1, 'claims': {'f'*64: {'at': NOW-600, 'tokens': 4000}}}
        self.store.cas(None, self.budget)
        self.args = dict(commit='b'*40, task=Path('gt47-advisory-task.txt').read_text(),
                         round_id='pilot-round-02', expected_id=self.old['id'], now=NOW)
    def test_archive_exact_and_budget_unchanged(self):
        result = start_new_round(self.store, **self.args)
        self.assertEqual(result['provider_calls'], 0)
        self.assertEqual(self.store.get('gt47-archive/'+self.old['id']+'.json')[0], self.old)
        current = self.store.get('gt47-current.json')[0]
        self.assertEqual(current['previous_task_id'], self.old['id'])
        self.assertNotEqual(current['id'], self.old['id'])
        self.assertEqual(self.store.read()[0], self.budget)
        with self.assertRaises(EnqueueRejected):
            start_new_round(self.store, **self.args)
    def test_preconditions_leave_queue_unchanged(self):
        for overrides in ({'expected_id':'0'*64}, {'commit':SHA}, {'round_id':'invalid'}):
            with self.subTest(overrides=overrides), self.assertRaises(EnqueueRejected):
                start_new_round(self.store, **dict(self.args, **overrides))
            self.assertEqual(self.store.get('gt47-current.json')[0], self.old)
    def test_archive_conflict_leaves_queue_unchanged(self):
        self.store.put('gt47-archive/'+self.old['id']+'.json', {'different':True}, None)
        with self.assertRaises(EnqueueRejected):
            start_new_round(self.store, **self.args)
        self.assertEqual(self.store.get('gt47-current.json')[0], self.old)
    def test_queue_conflict_preserves_archive_and_claims(self):
        original = self.store.put
        self.store.put = lambda path,value,version: False if path=='gt47-current.json' else original(path,value,version)
        with self.assertRaises(EnqueueRejected):
            start_new_round(self.store, **self.args)
        self.assertEqual(self.store.get('gt47-archive/'+self.old['id']+'.json')[0], self.old)
        self.assertEqual(self.store.read()[0], self.budget)
    def test_existing_new_dispatch_claim_cannot_be_bypassed(self):
        evidence={'commit':self.args['commit'],'tests_passed':True,'links_passed':True}
        _,digest=prepare(agent='AGT-ENG',commit=self.args['commit'],task='Round '+self.args['round_id']+'\n'+self.args['task'],evidence=evidence)
        self.budget['claims'][digest]={'at':NOW-600,'tokens':4000}
        self.store.cas(1,copy.deepcopy(self.budget))
        with self.assertRaises(ReconciliationRequired):
            start_new_round(self.store, **self.args)
        self.assertEqual(self.store.get('gt47-current.json')[0], self.old)

    def completed_queue(self, recommendation='ready_for_finalization'):
        from tests.test_gt47_t06_queue_summary import QueueSummaryTests
        value=QueueSummaryTests().completed(recommendation)
        value['id']='1'*64
        self.store.put('gt47-current.json', value, 2)
        self.args['expected_id']=value['id']
        return value
    def test_verified_completed_round_can_be_archived_without_refund(self):
        for recommendation in ('ready_for_finalization', 'needs_changes'):
            with self.subTest(recommendation=recommendation):
                self.setUp()
                old=self.completed_queue(recommendation)
                result=start_new_round(self.store, **self.args)
                self.assertEqual(result['provider_calls'],0)
                self.assertEqual(self.store.get('gt47-archive/'+old['id']+'.json')[0],old)
                self.assertEqual(self.store.read()[0],self.budget)
    def test_corrupt_completed_round_is_not_replaced(self):
        old=self.completed_queue();old['qa']['dispatch_id']='0'*64
        self.store.put('gt47-current.json',old,3)
        with self.assertRaises(EnqueueRejected):
            start_new_round(self.store, **self.args)
        self.assertEqual(self.store.get('gt47-current.json')[0],old)
        self.assertEqual(self.store.get('gt47-archive/'+old['id']+'.json')[0],None)
    def test_active_round_is_not_replaced(self):
        old=dict(self.old);old.pop('diagnostic')
        self.store.put('gt47-current.json',old,2)
        with self.assertRaises(EnqueueRejected):
            start_new_round(self.store, **self.args)
        self.assertEqual(self.store.get('gt47-current.json')[0],old)
    def test_checklist_handoff_fits_full_review_context_limit(self):
        task='Round pilot-round-04\n'+self.args['task']
        evidence={'commit':self.args['commit'],'tests_passed':True,'links_passed':True}
        engineering={'agent':'AGT-ENG','commit':self.args['commit'],'status':'advisory_completed',
                     'review':{'summary':'s'*240,'findings':['f'*100]*3,'recommendation':'ready_for_finalization'}}
        prepare(agent='AGT-QA',commit=self.args['commit'],task=task,evidence=evidence,engineering=engineering)
    def test_new_checklist_round_completes_once_with_verified_qa(self):
        from scripts.gt47_t06_groq_runner import run_once, demand_outcome
        from tests.test_gt47_t06_groq_handoff import response
        import json
        old=self.completed_queue('needs_changes')
        start_new_round(self.store, **self.args)
        calls=[]
        def provider(payload):
            calls.append(payload)
            result=response(payload)
            review={'summary':'Checklist de aceite proposto.',
                    'findings':['JSON versionado persistido por CAS e leitura confirmada.',
                                'dispatch_id reservado antes da chamada; duplicata bloqueada.',
                                'Etapa salva retomada; efeito incerto preserva reserva e impede reenvio.'],
                    'recommendation':'ready_for_finalization'}
            result['choices'][0]['message']['content']=json.dumps(review)
            return result
        args=dict(api_key='synthetic-only',enabled=True,free_plan_confirmed=True,transport=provider)
        self.assertEqual(run_once(self.store,now=NOW,**args)['status'],'qa_pending')
        self.assertEqual(run_once(self.store,now=NOW+299,**args)['status'],'waiting')
        self.assertEqual(len(calls),1)
        self.assertEqual(run_once(self.store,now=NOW+300,**args)['status'],'completed')
        current=self.store.get('gt47-current.json')[0]
        self.assertEqual(current['demand_outcome'],'finalized')
        self.assertEqual(demand_outcome(current),'finalized')
        self.assertEqual(current['engineering']['commit'],current['qa']['commit'])
        self.assertEqual(self.store.get('gt47-archive/'+old['id']+'.json')[0],old)
        self.assertEqual(len(self.store.read()[0]['claims']),3)
        self.assertEqual(run_once(self.store,now=NOW+86401,**args)['status'],'idle')
        self.assertEqual(len(calls),2)
