import unittest
from scripts.gt47_t04_context_loader import ContextRejected
from scripts.gt47_t06_dispatch_intent import prepare_dispatch
from scripts.gt47_t06_github_claim_ledger import reserve_dispatch_on_github, _claim_ref
from tests.test_gt47_t06_dispatch_intent import fixture


class GithubClaimLedgerTests(unittest.TestCase):
    def setUp(self):
        self.ctx, self.request = fixture()
        self.intent = prepare_dispatch(context=self.ctx, request=self.request)
        self.posts = []
        self.refs = {}

    def create(self, ref, sha):
        self.posts.append(ref)
        if ref in self.refs:
            return 422, {"message": "already exists"}
        self.refs[ref] = sha
        return 201, {"ref": ref, "object": {"type": "commit", "sha": sha}}

    def read(self, ref):
        if ref not in self.refs:
            return 404, {}
        return 200, {"ref": ref, "object": {"type": "commit", "sha": self.refs[ref]}}

    def reserve(self, intent=None, enabled=True, create=None, read=None):
        return reserve_dispatch_on_github(intent=intent or self.intent,
            enabled=enabled, create_ref=create or self.create,
            get_ref=read or self.read)

    def test_disabled_is_no_write(self):
        with self.assertRaisesRegex(ContextRejected, "disabled"):
            self.reserve(enabled=False)
        self.assertEqual(self.posts, [])

    def test_claim_and_replay_across_invocations(self):
        result = self.reserve()
        self.assertEqual(result["status"], "reserved_remote")
        self.assertFalse(result["execution_allowed"])
        self.assertFalse(result["agent_mission_executed"])
        with self.assertRaisesRegex(ContextRejected, "replay"):
            self.reserve()

    def test_nonce_cannot_bypass_cross_run_dedup(self):
        other = dict(self.request, nonce="unique_nonce_8888")
        intent2 = prepare_dispatch(context=self.ctx, request=other)
        self.assertNotEqual(intent2["dispatch_id"], self.intent["dispatch_id"])
        self.assertEqual(_claim_ref(intent2), _claim_ref(self.intent))
        self.reserve()
        with self.assertRaises(ContextRejected):
            self.reserve(intent=intent2)

    def test_fail_closed_if_claim_ref_is_wrong(self):
        with self.assertRaises(ContextRejected):
            self.reserve(create=lambda ref, sha: (201, {"ref": "refs/tags/other", "object": {"type": "commit", "sha": sha}}))

    def test_422_without_matching_existing_ref_is_not_replay(self):
        with self.assertRaisesRegex(ContextRejected, "conflict not verified"):
            self.reserve(create=lambda ref, sha: (422, {}), read=lambda ref: (404, {}))

    def test_network_error_has_uncertain_status_and_no_retry(self):
        attempts = []
        def fail(ref, sha):
            attempts.append(ref)
            raise TimeoutError("timeout")
        with self.assertRaisesRegex(ContextRejected, "uncertain"):
            self.reserve(create=fail)
        self.assertEqual(len(attempts), 1)

    def test_denied_auth_or_limits_do_not_trigger_lookup(self):
        for code in (401, 403, 409, 429, 500):
            with self.subTest(code=code), self.assertRaises(ContextRejected):
                self.reserve(create=lambda ref, sha: (code, {}),
                    read=lambda ref: self.fail("unexpected read"))

    def test_tampered_and_forged_intent_no_write(self):
        for key, value in (("authorization_granted", True),
                           ("execution_allowed", True),
                           ("agent_id", "AGT-ROOT/../"),
                           ("commit_sha", "z" * 40),
                           ("issue", True),
                           ("mission", "other")):
            with self.subTest(key=key):
                forged = dict(self.intent, **{key: value})
                with self.assertRaises(ContextRejected):
                    self.reserve(intent=forged)
        self.assertEqual(self.posts, [])

    def test_missing_transport_no_write(self):
        with self.assertRaises(ContextRejected):
            reserve_dispatch_on_github(intent=self.intent, enabled=True)
        self.assertEqual(self.posts, [])


if __name__ == "__main__":
    unittest.main()
