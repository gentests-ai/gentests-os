"""Failure diagnoses preserve reservations and never disclose provider bodies."""
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

from scripts.gt47_t06_groq_runner import enqueue, run_once
from tests.test_gt47_t06_groq_handoff import MemoryStore, SHA, NOW, response


class SafeFailureDiagnosticsTests(unittest.TestCase):
    def run_failure(self, *, error=None, transport=None, storage_failure=False):
        store = MemoryStore()
        enqueue(store, commit=SHA, task='Synthetic diagnostic test')
        if storage_failure:
            original = store.put
            store.put = lambda path, value, version: False if (
                path == 'gt47-current.json' and 'engineering' in value
            ) else original(path, value, version)
        args = dict(api_key='secret-sentinel', enabled=True, free_plan_confirmed=True)
        if transport is not None:
            args['transport'] = transport
        with patch('urllib.request.build_opener') as opener:
            opener.return_value.open.side_effect = error
            result = run_once(store, now=NOW, **args)
            calls = opener.return_value.open.call_count
            if transport is None:
                self.assertEqual(calls, 1)
                request = opener.return_value.open.call_args.args[0]
                self.assertEqual(request.get_header('User-agent'), 'GTS47-Advisory/1.0')
            claims = store.read()[0]['claims']
            self.assertEqual(len(claims), 1)
            self.assertEqual(result['status'], 'manual_reconciliation_required')
            self.assertNotIn('secret-sentinel', str(result))
            self.assertEqual(run_once(store, now=NOW + 86401, **args)['reason'],
                             'persisted_reconciliation')
            self.assertEqual(opener.return_value.open.call_count, calls)
            self.assertEqual(store.read()[0]['claims'], claims)
        return result

    def test_http_codes_without_body_or_retry(self):
        for code in (401, 403, 429, 500):
            with self.subTest(code=code):
                error = HTTPError('https://example.invalid', code, 'secret-sentinel', {}, None)
                self.assertEqual(self.run_failure(error=error)['reason'], f'provider_http_{code}')

    def test_transport_uncertainty(self):
        self.assertEqual(self.run_failure(error=URLError('secret-sentinel'))['reason'],
                         'provider_transport_uncertain')

    def test_invalid_provider_response(self):
        self.assertEqual(self.run_failure(transport=lambda payload: {})['reason'],
                         'provider_response_invalid')

    def test_successful_response_storage_failure(self):
        calls = []
        def provider(payload):
            calls.append(payload)
            return response(payload)
        self.assertEqual(self.run_failure(transport=provider, storage_failure=True)['reason'],
                         'result_storage_uncertain')
        self.assertEqual(len(calls), 1)
