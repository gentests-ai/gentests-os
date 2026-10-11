"""Offline deterministic tests of synthetic dispatch state machine."""
import importlib.util
import json
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

if __name__ == '__main__':
    unittest.main()
