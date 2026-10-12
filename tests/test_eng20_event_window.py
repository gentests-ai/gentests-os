"""Offline tests of the exact embedded gate; never runs ENG-20 or GitHub."""
import ast
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

WORKFLOW = Path(__file__).resolve().parents[1] / '.github/workflows/eng20-synthetic-issue-dispatch.yml'
TEXT = WORKFLOW.read_text(encoding='utf-8')
GATE = '\n'.join(line[10:] for line in TEXT.split('<<\'PY\'\n', 1)[1].split('\n          PY', 1)[0].splitlines())
TREE = ast.parse(GATE)
FUNCTIONS = ast.Module(body=[n for n in TREE.body if isinstance(n, (ast.Import, ast.ImportFrom, ast.FunctionDef))], type_ignores=[])
NS = {}
exec(compile(FUNCTIONS, '<embedded-window>', 'exec'), NS)
window_valid = NS['window_valid']
START = '2026-10-12T07:00:00Z'
END = '2026-10-12T07:15:00Z'
NOW = datetime(2026, 10, 12, 7, 5, tzinfo=timezone.utc)

class WindowTests(unittest.TestCase):
    def test_boundaries(self):
        self.assertTrue(window_valid(START, END, NOW.replace(minute=0)))
        self.assertTrue(window_valid(START, END, NOW.replace(minute=14, second=59)))
        self.assertFalse(window_valid(START, END, NOW.replace(minute=15)))

    def test_missing_invalid_non_utc(self):
        for v in ('', None, True, 'bad', '2026-02-30T07:00:00Z', '2026-10-12T07:00:00+00:00', '2026-10-12T07:00:00', '2026-10-12T07:00:00.0Z'):
            with self.subTest(v=v):
                self.assertFalse(window_valid(v, END, NOW))
                self.assertFalse(window_valid(START, v, NOW))

    def test_future_expired_reversed_equal_overlong(self):
        self.assertFalse(window_valid(START, END, NOW.replace(hour=6)))
        self.assertFalse(window_valid(START, END, NOW.replace(hour=8)))
        for start, end in ((END, START), (START, START), (START, '2026-10-12T07:15:01Z')):
            self.assertFalse(window_valid(start, end, NOW))

    def test_naive_clock_blocked(self):
        self.assertFalse(window_valid(START, END, NOW.replace(tzinfo=None)))

class GateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name)
        self.gate = self.path/'gate.py'
        self.gate.write_text(GATE, encoding='utf-8')
        # Local fixtures only; never written to GitHub configuration.
        self.auth = 'https://github.com/gentestsai-sudo/gentests-os/issues/47#issuecomment-999999999'
        self.event = {'action':'labeled', 'sender':{'login':'gentestsai-sudo','id':340329299},
                      'label':{'name':'gt-synthetic-dispatch-approved'},
                      'issue':{'number':123,'state':'open','title':'SYN-ENG20-001 — authorized synthetic dispatch',
                               'body':'demand_id: SYN-ENG20-001\nsynthetic: true\nauthorization_ref: '+self.auth}}
        now = datetime.now(timezone.utc)
        stamp = lambda v: v.strftime('%Y-%m-%dT%H:%M:%SZ')
        self.env = dict(os.environ, GITHUB_EVENT_PATH=str(self.path/'event.json'), AUTHORIZED_ISSUE_NUMBER='123',
                        EXECUTION_AUTHORIZATION_REF=self.auth, EXECUTION_AUTHORIZATION_ID='GT-AI-DISPATCH-001-AUTO-EVENT-RUN-01',
                        PREPARATION_AUTHORIZATION_REF='https://github.com/gentestsai-sudo/gentests-os/issues/47#issuecomment-6119631271',
                        WINDOW_START_UTC=stamp(now-timedelta(minutes=1)), WINDOW_END_UTC=stamp(now+timedelta(minutes=5)),
                        GITHUB_EVENT_NAME='issues', GITHUB_REPOSITORY='gentestsai-sudo/gentests-os',
                        GITHUB_RUN_ATTEMPT='1',GITHUB_ACTOR='gentestsai-sudo',GITHUB_ACTOR_ID='340329299')

    def run_gate(self, changes=None):
        (self.path/'event.json').write_text(json.dumps(self.event), encoding='utf-8')
        r = subprocess.run([os.sys.executable,str(self.gate)],env={**self.env,**(changes or {})},capture_output=True,text=True)
        self.assertNotIn(self.auth,r.stdout+r.stderr)
        return r.returncode

    def test_synthetic_gate_positive_no_dispatcher(self):
        self.assertEqual(self.run_gate(),0)
        self.assertEqual(sorted(p.name for p in self.path.iterdir()),['event.json','gate.py'])

    def test_authorization_absent_wrong_or_preparation(self):
        for change in ({'EXECUTION_AUTHORIZATION_REF':''}, {'EXECUTION_AUTHORIZATION_ID':''},
                       {'EXECUTION_AUTHORIZATION_ID':'DEC-AUTO-EVENT-B-PREP-01'},
                       {'EXECUTION_AUTHORIZATION_REF':self.env['PREPARATION_AUTHORIZATION_REF']},
                       {'EXECUTION_AUTHORIZATION_REF':'https://github.com/gentestsai-sudo/gentests-os/issues/47#issuecomment-6119093844'},
                       {'EXECUTION_AUTHORIZATION_REF':self.auth+'?extra=1'}):
            self.assertNotEqual(self.run_gate(change),0)

    def test_window_missing_future_expired(self):
        for change in ({'WINDOW_START_UTC':''},{'WINDOW_END_UTC':''},
                       {'WINDOW_START_UTC':'2099-01-01T00:00:00Z','WINDOW_END_UTC':'2099-01-01T00:10:00Z'},
                       {'WINDOW_START_UTC':START,'WINDOW_END_UTC':START}):
            self.assertNotEqual(self.run_gate(change),0)

    def test_issue_zero_and_rerun_denied(self):
        self.assertNotEqual(self.run_gate({'AUTHORIZED_ISSUE_NUMBER':'0'}),0)
        self.assertNotEqual(self.run_gate({'GITHUB_RUN_ATTEMPT':'2'}),0)

    def test_new_run_not_persistently_deduplicated(self):
        # Honest limitation: B does not block a second new event in a valid window.
        self.assertEqual(self.run_gate({'GITHUB_RUN_ID':'synthetic-A'}),0)
        self.assertEqual(self.run_gate({'GITHUB_RUN_ID':'synthetic-B'}),0)

    def test_hostile_body_rejected_without_execution(self):
        self.event['issue']['body']='$(touch '+str(self.path/'injected')+')'
        self.assertNotEqual(self.run_gate(),0)
        self.assertFalse((self.path/'injected').exists())

    def test_wrong_actor_label_and_issue(self):
        self.assertNotEqual(self.run_gate({'GITHUB_ACTOR_ID':'999'}),0)
        self.event['label']['name']='other'
        self.assertNotEqual(self.run_gate(),0)
        self.event['label']['name']='gt-synthetic-dispatch-approved'
        self.event['issue']['number']=True
        self.assertNotEqual(self.run_gate(),0)

    def test_workflow_pending_operator_window_remains_blocked(self):
        self.assertIn('github.event.issue.number == 81',TEXT)
        self.assertIn('if: >-\n      false &&',TEXT)
        for entry in ("AUTHORIZED_ISSUE_NUMBER: '81'", "EXECUTION_AUTHORIZATION_REF: 'https://github.com/gentestsai-sudo/gentests-os/issues/47#issuecomment-6120900019'", "EXECUTION_AUTHORIZATION_ID: 'GT-AI-DISPATCH-001-AUTO-EVENT-RUN-01'", "WINDOW_START_UTC: ''", "WINDOW_END_UTC: ''"):
            self.assertIn(entry,TEXT)
        self.assertEqual(TEXT.count('python3 "${RUNNER_TEMP}/eng20-event-gate.py"'),2)
        self.assertNotIn('${{',GATE)

if __name__ == '__main__':
    unittest.main()
