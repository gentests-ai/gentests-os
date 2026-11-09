"""T08 bridge contract tests: no remote network calls or live authorization."""
import hashlib
import hmac
import json
import unittest

from scripts.gt47_t04_context_loader import ContextRejected
from scripts.gt47_t06_dispatch_intent import prepare_dispatch
from scripts.gt47_t06_github_claim_ledger import _claim_ref
from scripts.gt47_t08_executor_bridge import (
    execute_reserved_intent, validate_attestation,
)
from tests.test_gt47_t06_dispatch_intent import fixture

KEY = b"t08-test-receipt-key-only-not-a-production-secret"
RID = "receipt_synthetic_123456"


def signed_receipt(intent, status, *, rid=RID, key=KEY,
                   agent=None, digest=None):
    result = {
        "schema": "gt47-executor-receipt-v1",
        "status": status, "agent_id": agent or intent["agent_id"],
        "dispatch_id": intent["dispatch_id"], "receipt_id": rid,
        "result_sha256": digest if status == "completed" else None,
    }
    unsigned = json.dumps(result, sort_keys=True, ensure_ascii=False,
                          separators=(",", ":")).encode()
    result["signature"] = hmac.new(key, unsigned, hashlib.sha256).hexdigest()
    return result


class ExecutorBridgeTests(unittest.TestCase):
    def setUp(self):
        context, req = fixture()
        self.intent = prepare_dispatch(context=context, request=req)
        self.reservation = {
            "status": "reserved_remote",
            "claim_ref": _claim_ref(self.intent),
            "dispatch_id": self.intent["dispatch_id"], "github_write": True,
            "execution_allowed": False, "agent_mission_executed": False,
        }
        self.posts = []
        self.polls = []
        self.refs = {self.reservation["claim_ref"]: self.intent["commit_sha"]}
        self.ref_posts = []

    def create_ref(self, ref, sha):
        self.ref_posts.append(ref)
        if ref in self.refs:
            return 422, {"message": "already exists"}
        self.refs[ref] = sha
        return 201, {"ref": ref, "object": {"type": "commit", "sha": sha}}

    def get_ref(self, ref):
        if ref not in self.refs:
            return 404, {}
        return 200, {"ref": ref, "object": {"type": "commit", "sha": self.refs[ref]}}

    def post(self, payload):
        self.posts.append(payload)
        return 202, signed_receipt(self.intent, "received")

    def poll(self, receipt_id):
        self.polls.append(receipt_id)
        status = "accepted" if len(self.polls) == 1 else "completed"
        return 200, signed_receipt(self.intent, status, digest="b" * 64)

    def execute(self, *, intent=None, reservation=None, enabled=True,
                authorization=None, submit=None, lookup=None, max_polls=2):
        return execute_reserved_intent(
            intent=intent or self.intent,
            reservation=reservation or self.reservation,
            receipt_key=KEY,
            verify_authorization=authorization or (lambda _: True),
            create_ref=self.create_ref, get_ref=self.get_ref,
            submit=submit or self.post, lookup=lookup or self.poll,
            enabled=enabled, max_polls=max_polls,
        )

    def test_entire_signed_receive_accept_complete_sequence(self):
        result = self.execute()
        self.assertEqual(result["status"], "remote_completed_attested")
        self.assertEqual(result["result_sha256"], "b" * 64)
        self.assertEqual(self.polls, [RID, RID])
        self.assertFalse(result["independently_verified"])
        self.assertNotIn("source_provenance", json.dumps(self.posts))
        self.assertNotIn("authorization", json.dumps(self.posts))
        self.assertNotIn("token", json.dumps(self.posts))

    def test_same_reservation_cannot_be_reused_for_second_post(self):
        first = self.execute()
        self.assertEqual(first["status"], "remote_completed_attested")
        with self.assertRaisesRegex(ContextRejected, "already consumed"):
            self.execute()
        self.assertEqual(len(self.posts), 1)
        self.assertEqual(len(self.ref_posts), 2)

    def test_missing_durable_claim_ref_fails_before_post(self):
        self.refs.clear()
        with self.assertRaisesRegex(ContextRejected, "reservation not verified"):
            self.execute()
        self.assertEqual(self.posts, [])
        self.assertEqual(self.ref_posts, [])

    def test_disabled_refuses_to_call_remote(self):
        with self.assertRaises(ContextRejected):
            self.execute(enabled=False)
        self.assertEqual(self.posts, [])
        self.assertEqual(self.ref_posts, [])

    def test_absent_verified_authorization_fails_before_post(self):
        with self.assertRaises(ContextRejected):
            self.execute(authorization=lambda _: False)
        self.assertEqual(self.posts, [])

    def test_forged_reservation_is_rejected(self):
        bad = dict(self.reservation, claim_ref="refs/tags/other")
        with self.assertRaises(ContextRejected):
            self.execute(reservation=bad)
        self.assertEqual(self.posts, [])

    def test_forged_authorization_callback_failure_fails_closed(self):
        def fail(_):
            raise ValueError("secret-error")
        with self.assertRaises(ContextRejected) as ctx:
            self.execute(authorization=fail)
        self.assertNotIn("secret-error", str(ctx.exception))
        self.assertEqual(self.posts, [])

    def test_receipt_signature_tamper(self):
        fake = signed_receipt(self.intent, "received")
        fake["receipt_id"] = "forged_receipt_1234"
        with self.assertRaises(ContextRejected):
            self.execute(submit=lambda _: (202, fake))

    def test_receipt_bound_to_wrong_agent(self):
        fake = signed_receipt(self.intent, "received", agent="AGT-ENG")
        with self.assertRaises(ContextRejected):
            self.execute(submit=lambda _: (202, fake))

    def test_submit_timeout_no_automatic_retries(self):
        attempts = []
        def timeout(_):
            attempts.append(1)
            raise TimeoutError("gateway")
        with self.assertRaisesRegex(ContextRejected, "uncertain"):
            self.execute(submit=timeout)
        self.assertEqual(len(attempts), 1)

    def test_executor_error_does_not_become_success(self):
        with self.assertRaises(ContextRejected):
            self.execute(submit=lambda _: (503, {}))

    def test_completion_before_acceptance_is_rejected(self):
        with self.assertRaisesRegex(ContextRejected, "without verified acceptance"):
            self.execute(lookup=lambda _: (200, signed_receipt(
                self.intent, "completed", digest="b" * 64)))

    def test_bad_digest_on_completion_fails_closed(self):
        called = []
        def poll(rid):
            called.append(rid)
            if len(called) == 1:
                return 200, signed_receipt(self.intent, "accepted")
            return 200, signed_receipt(self.intent, "completed", digest="bad")
        with self.assertRaises(ContextRejected):
            self.execute(lookup=poll)

    def test_bounded_pending_is_not_execution_success(self):
        result = self.execute(lookup=lambda _: (200, signed_receipt(
            self.intent, "accepted")), max_polls=2)
        self.assertEqual(result["status"], "remote_pending_attested")
        self.assertIs(result["agent_mission_executed"], False)

    def test_changed_receipt_id_fails_closed(self):
        counter = []
        def poll(_):
            counter.append(1)
            return 200, signed_receipt(self.intent, "accepted",
                                       rid="another_receipt_12345")
        with self.assertRaises(ContextRejected):
            self.execute(lookup=poll)

    def test_invalid_status_signature_and_payload(self):
        with self.assertRaises(ContextRejected):
            validate_attestation(value={}, key=KEY, intent=self.intent,
                                 receipt_id=None, allowed_states=("received",))
        with self.assertRaises(ContextRejected):
            validate_attestation(value=signed_receipt(self.intent, "received"),
                                 key=b"weak", intent=self.intent,
                                 receipt_id=None, allowed_states=("received",))


if __name__ == "__main__":
    unittest.main()
