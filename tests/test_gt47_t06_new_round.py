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
