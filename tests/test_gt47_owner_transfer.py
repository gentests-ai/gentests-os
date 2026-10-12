"""Owner transfer must fix routing without resetting replay protection."""
import unittest
from unittest.mock import patch, MagicMock
from scripts.gt47_t06_groq_runner import GitHubStore, NoRedirect
from scripts.gt47_t04_transport import github_readonly_get
from scripts.gt47_t04_context_loader import ContextRejected
from scripts.gt47_t06_dispatch_intent import prepare_dispatch
from scripts.gt47_t06_github_claim_ledger import _claim_ref
from tests.test_gt47_t06_dispatch_intent import fixture

class OwnerTransferTests(unittest.TestCase):
    def test_state_requests_use_canonical_owner_and_refuse_redirects(self):
        response = MagicMock(status=200)
        response.read.return_value = b'{}'
        with patch('scripts.gt47_t06_groq_runner.build_opener') as opener:
            opener.return_value.open.return_value.__enter__.return_value = response
            self.assertEqual(GitHubStore('test-only').request('GET', '/git/ref/heads/gt47-advisory-state'), (200, {}))
            request = opener.return_value.open.call_args.args[0]
            self.assertEqual(request.full_url, 'https://api.github.com/repos/gentests-ai/gentests-os/git/ref/heads/gt47-advisory-state')
            self.assertIs(opener.call_args.args[0], NoRedirect)
        with self.assertRaisesRegex(ValueError, 'redirect refused'):
            NoRedirect().redirect_request(None, None, 301, '', {}, 'https://example.com')

    def test_old_owner_is_rejected_before_readonly_transport(self):
        with patch('scripts.gt47_t04_transport.build_opener') as opener:
            with self.assertRaises(ContextRejected):
                github_readonly_get('https://api.github.com/repos/gentestsai-sudo/gentests-os/issues/47/comments', {'per_page': 10, 'page': 1}, token='test-only')
            opener.assert_not_called()

    def test_pretransfer_claim_identity_stays_stable(self):
        context, request = fixture()
        self.assertEqual(_claim_ref(prepare_dispatch(context=context, request=request)),
            'refs/tags/gt47-claims/0ed9673a6957b2f0e20cdbcd480d48bbce55388cd7aaa5100066e59b1bdfb546')
