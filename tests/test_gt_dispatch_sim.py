"""Offline deterministic tests of synthetic dispatch state machine."""
import importlib.util
import json
import sqlite3
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('gt_dispatch_sim', ROOT / 'scripts' / 'gt_dispatch_sim.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
NOW = datetime(2026, 10, 11, 20, tzinfo=timezone.utc)

class DispatchTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.db = Path(self.temp.name) / 'checkpoint.sqlite'
        self.e = json.loads((ROOT / 'tests/fixtures/gt_dispatch_event.json').read_text())

    def test_positive_and_replay(self):
        first = mod.run(self.db, self.e, NOW)
        second = mod.run(self.db, self.e, NOW)
        self.assertEqual(first['status'], 'done')
        self.assertEqual(second['status'], 'duplicate')
        self.assertEqual(first['output_hash'], second['output_hash'])

    def test_missing_auth(self):
        del self.e['authorization']
        self.assertEqual(mod.run(self.db, self.e, NOW)['reason'], 'authorization_missing')

    def test_revoked(self):
        self.e['authorization']['revoked'] = True
        self.assertEqual(mod.run(self.db, self.e, NOW)['reason'], 'authorization_revoked_or_unknown')

    def test_expired(self):
        self.e['authorization']['expires_at'] = '2026-10-10T00:00:00Z'
        self.assertEqual(mod.run(self.db, self.e, NOW)['reason'], 'expired')

    def test_scope_and_generation(self):
        self.e['scope'] = 'merge'
        self.assertEqual(mod.run(self.db, self.e, NOW)['reason'], 'scope_denied')
        self.e['scope'] = 'simulate:synthetic'
        self.e['generation'] = 2
        self.assertEqual(mod.run(self.db, self.e, NOW)['reason'], 'version_mismatch')

    def test_external_effect_denied(self):
        self.e['operation'] = 'merge'
        self.assertEqual(mod.run(self.db, self.e, NOW)['reason'], 'external_effect_denied')

    def test_restart_after_failure_fail_closed(self):
        with self.assertRaisesRegex(RuntimeError, 'synthetic_crash'):
            mod.run(self.db, self.e, NOW, crash_after_reserve=True)
        result = mod.run(self.db, self.e, NOW)
        self.assertEqual(result['reason'], 'pending_requires_reconciliation')

    def test_bad_expiration(self):
        self.e['authorization']['expires_at'] = 'invalid'
        self.assertEqual(mod.run(self.db, self.e, NOW)['reason'], 'expiration_invalid')

    def test_different_generation_new_record(self):
        self.assertEqual(mod.run(self.db, self.e, NOW)['status'], 'done')
        self.e['generation'] = 2
        self.e['authorization']['generation'] = 2
        self.assertEqual(mod.run(self.db, self.e, NOW)['status'], 'done')

    def test_missing_and_corrupt_checkpoint(self):
        self.assertEqual(mod.run(self.db, self.e, NOW)['status'], 'done')
        self.db.write_bytes(b'not-sqlite')
        with self.assertRaises(Exception):
            mod.run(self.db, self.e, NOW)

    def test_stage_allowlist(self):
        for stage in ('merge', 'unknown-stage'):
            with self.subTest(stage=stage):
                event = json.loads(json.dumps(self.e))
                event['stage'] = stage
                self.assertEqual(mod.run(self.db, event, NOW)['status'], 'blocked')

    def test_identity_change_without_authorization(self):
        changes = {'repo':'synthetic/other','issue':124,'mission':'SYNTH-OTHER',
                   'stage':'unknown-stage','generation':2,'corpus_sha':'e'*40}
        for field, value in changes.items():
            with self.subTest(field=field):
                event = json.loads(json.dumps(self.e))
                event[field] = value
                self.assertEqual(mod.run(self.db, event, NOW)['status'], 'blocked')

    def test_authorization_forged_mismatch(self):
        for field in mod.REQUIRED:
            with self.subTest(field=field):
                event = json.loads(json.dumps(self.e))
                event['authorization'][field] = None
                self.assertEqual(mod.run(self.db, event, NOW)['status'], 'blocked')

    def test_bool_issue_and_generation(self):
        for field in ('issue', 'generation'):
            with self.subTest(field=field):
                event = json.loads(json.dumps(self.e))
                event[field] = True
                event['authorization'][field] = True
                self.assertEqual(mod.run(self.db, event, NOW)['status'], 'blocked')

    def test_invalid_identity_types_and_sha(self):
        for field, value in [('repo',42),('mission',[]),('issue',0),
                             ('corpus_sha','xxx'),('corpus_sha','F'*40)]:
            with self.subTest(field=field):
                event = json.loads(json.dumps(self.e))
                event[field] = value
                event['authorization'][field] = value
                self.assertEqual(mod.run(self.db, event, NOW)['status'], 'blocked')

    def test_logical_checkpoint_corruption(self):
        for status, digest in [('done',None),('done',''),('done','not-a-hash'),
                               ('done','X'*64),('unknown','a'*64),('reserved',None)]:
            with self.subTest(status=status, digest=digest):
                with tempfile.TemporaryDirectory() as temp:
                    db = Path(temp) / 'state.sqlite'
                    self.assertEqual(mod.run(db, self.e, NOW)['status'], 'done')
                    with sqlite3.connect(db) as conn:
                        conn.execute('UPDATE runs SET status=?, output_hash=?',
                                     (status, digest))
                    result = mod.run(db, self.e, NOW)
                    self.assertEqual(result['status'], 'blocked')
                    self.assertEqual(result['reason'], 'pending_requires_reconciliation')

if __name__ == '__main__':
    unittest.main()
