"""G3 offline integration contract tests; no network or real authority."""
import copy
import sqlite3
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

from scripts.gt_t05_g3_offline import FakeActionsRunner
from scripts.gt_t05_security_mock import identity

NOW = datetime(2026, 10, 11, 20, tzinfo=timezone.utc)
BASE = dict(repo='synthetic/example', issue=123, mission='SYNTH-001', stage='simulate',
            generation=1, corpus_sha='f'*40, scope='simulate:synthetic', operation='dry_run',
            synthetic=True, auth_ref='TEST-DEC-001', decision_version=1)


class G3OfflineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.event = copy.deepcopy(BASE)
        self.decisions = {'TEST-DEC-001': dict(status='authorized', revoked=False, version=1,
                          scope='simulate:synthetic', expires_at='2026-10-12T00:00:00Z',
                          identity=identity(self.event))}
        self.runner = FakeActionsRunner(Path(self.temp.name)/'mock.sqlite', self.decisions)

    def test_success_and_replay(self):
        ok = self.runner.execute(self.event, NOW)
        self.assertEqual(ok['state'], 'done')
        self.assertTrue(ok['request_id'].startswith('fake-'))
        self.assertEqual(ok['units_fictitious'], 1)
        self.assertEqual(self.runner.execute(self.event, NOW)['reason'], 'replay_requires_reconciliation')

    def test_forged_authorization_and_scope(self):
        for field, value in [('auth_ref','FORGED'), ('scope','admin'), ('generation',True),
                             ('corpus_sha','e'*40), ('decision_version',True)]:
            with self.subTest(field=field):
                event = copy.deepcopy(self.event)
                event[field] = value
                self.assertEqual(self.runner.execute(event, NOW)['state'], 'blocked')

    def test_least_privilege_and_no_publication(self):
        for operation in ('contents:write','merge','publish','permissions:write'):
            self.assertEqual(self.runner.execute(self.event, NOW,operation=operation)['reason'],
                             'least_privilege')
        self.assertFalse(hasattr(self.runner, 'publish'))

    def test_revocation_between_reservation_and_effect(self):
        def revoke():
            self.decisions['TEST-DEC-001']['revoked']=True
        result = self.runner.execute(self.event, NOW, before_inference=revoke)
        self.assertEqual(result['state'], 'blocked')
        self.assertIs(result['retry'], False)
        self.assertEqual(self.runner.controller.connect().execute('SELECT state FROM jobs').fetchone(),
                         ('uncertain',))

    def test_kill_switch_and_uncertain_replay(self):
        result = self.runner.execute(self.event,NOW,before_inference=lambda: self.runner.controller.set_killed(True))
        self.assertEqual(result['state'],'blocked')
        self.assertEqual(self.runner.execute(self.event,NOW)['state'],'blocked')

    def test_synthetic_timeout_without_retry(self):
        result = self.runner.execute(self.event,NOW,failure='timeout')
        self.assertEqual(result['state'],'blocked')
        self.assertIs(result['retry'],False)
        self.assertEqual(self.runner.execute(self.event,NOW)['state'],'blocked')

    def test_unknown_provider_error_without_retry(self):
        result = self.runner.execute(self.event,NOW,failure=418)
        self.assertEqual(result['state'],'blocked')
        self.assertIs(result['retry'],False)

    def test_persistent_synthetic_quota_exhaustion(self):
        with self.runner.controller.connect() as db:
            db.execute('UPDATE control SET cap=0')
        self.assertEqual(self.runner.execute(self.event,NOW)['reason'],'quota_exhausted')

    def test_corrupt_counter_blocks(self):
        with self.runner.controller.connect() as db:
            db.execute('UPDATE control SET used=?',('corrupt',))
        self.assertEqual(self.runner.execute(self.event,NOW)['reason'],'counter_corrupt')

    def test_fencing_stale_token(self):
        reserved = self.runner.controller.reserve(self.event,NOW)
        result = self.runner.controller.effect(self.event,reserved['fence']+1,NOW)
        self.assertEqual(result['reason'],'stale_fence_or_state')

    def test_concurrency_one_reservation(self):
        with ThreadPoolExecutor(max_workers=2) as executor:
            responses = list(executor.map(lambda _:self.runner.execute(self.event,NOW),range(2)))
        self.assertEqual(sorted(x['state'] for x in responses),['blocked','done'])

if __name__ == '__main__':
    unittest.main()
