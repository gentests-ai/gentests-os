"""Adulterated records cannot finalize or become QA input."""
import json
import unittest
from scripts.gt47_t06_groq_handoff import invoke, prepare, validate_response
from scripts.gt47_t06_groq_runner import demand_outcome
from tests.test_gt47_t06_groq_handoff import MemoryStore, response, NOW

class AdvisoryIntegrityTests(unittest.TestCase):
    def value(self):
        from tests.test_gt47_t06_queue_summary import QueueSummaryTests
        return QueueSummaryTests().completed('ready_for_finalization')
    def test_adulterated_records_cannot_finalize(self):
        mutations = [
            lambda q: q.update(task='Changed task'),
            lambda q: q['evidence'].update(tests_passed=False),
            lambda q: q['evidence'].update(commit='b'*40),
            lambda q: q['engineering'].update(dispatch_id='0'*64),
            lambda q: q['qa'].update(dispatch_id='0'*64),
            lambda q: q['qa'].update(model='other-model'),
            lambda q: q['qa'].update(code_executed=True),
            lambda q: q['qa'].update(approval_granted=0),
            lambda q: q['qa'].update(unexpected=True),
            lambda q: q['qa']['usage'].update(total_tokens=999),
            lambda q: q['engineering']['review'].update(summary='Changed review'),
            lambda q: q['qa']['review'].update(summary=''),
            lambda q: q['qa']['review'].update(findings=['x'*101]),
            lambda q: q['qa']['review'].update(extra='unexpected'),
        ]
        for index, mutate in enumerate(mutations):
            with self.subTest(index=index):
                value=self.value();mutate(value)
                self.assertEqual(demand_outcome(value),'unverified')
    def test_missing_fields_never_finalize(self):
        for key in self.value()['qa']:
            value=self.value(); del value['qa'][key]
            self.assertEqual(demand_outcome(value),'unverified')
    def test_invalid_engineering_blocks_qa_before_reservation(self):
        value=self.value(); value['engineering']['dispatch_id']='0'*64
        store=MemoryStore();calls=[]
        with self.assertRaises(ValueError):
            invoke(store=store,now=NOW,agent='AGT-QA',commit=value['commit'],
                task=value['task'],evidence=value['evidence'],engineering=value['engineering'],
                api_key='offline',enabled=True,free_plan_confirmed=True,
                transport=lambda payload:calls.append(payload))
        self.assertEqual(calls,[])
        self.assertEqual(store.read()[0]['claims'],{})
    def test_new_response_rejects_legacy_recommendation(self):
        value=self.value()
        payload,digest=prepare(agent='AGT-ENG',commit=value['commit'],task=value['task'],evidence=value['evidence'])
        result=response(payload)
        review=json.loads(result['choices'][0]['message']['content'])
        review['recommendation']='ready_for_human_review'
        result['choices'][0]['message']['content']=json.dumps(review)
        with self.assertRaises(ValueError):
            validate_response(result,agent='AGT-ENG',commit=value['commit'],digest=digest)
    def test_realistic_historical_read_is_preserved(self):
        value=self.value();value['qa']['review']['recommendation']='ready_for_human_review'
        self.assertEqual(demand_outcome(value),'finalized')
