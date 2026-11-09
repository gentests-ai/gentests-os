import unittest
from datetime import datetime, timezone
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

from scripts.gt47_t04_context_loader import ContextRejected
from scripts.gt47_t06_dispatch_intent import prepare_dispatch
from scripts.gt47_t08_executor_bridge import (
    _canonical, _claim_ref, execute_reserved_intent, validate_attestation,
)
from tests.test_gt47_t06_dispatch_intent import fixture

DOMAIN = b"GT47-RECEIPT-v1\x00"


class Ed25519ReceiptV2Tests(unittest.TestCase):
    def setUp(self):
        context, request = fixture()
        self.intent = prepare_dispatch(context=context, request=request)
        self.private = Ed25519PrivateKey.generate()
        self.public = self.private.public_key().public_bytes(
            serialization.Encoding.Raw, serialization.PublicFormat.Raw)
        self.receipt_id = "receipt_ed25519_123456"

    def sign(self, receipt):
        unsigned = dict(receipt)
        unsigned.pop("signature", None)
        receipt["signature"] = self.private.sign(
            DOMAIN + _canonical(unsigned)
        )
        import base64
        receipt["signature"] = base64.urlsafe_b64encode(
            receipt["signature"]
        ).decode("ascii").rstrip("=")
        return receipt

    def receipt(self, status, *, digest=None, accepted=None):
        value = {
            "schema": "gt47-executor-receipt-v2",
            "status": status,
            "mission": self.intent["mission"],
            "issue": self.intent["issue"],
            "agent_id": self.intent["agent_id"],
            "commit_sha": self.intent["commit_sha"],
            "dispatch_id": self.intent["dispatch_id"],
            "receipt_id": self.receipt_id,
            "result_sha256": digest,
            "updated_at": "2026-11-09T22:00:00.000Z",
            "executor": "gt47-cloudflare-worker-v1",
        }
        if accepted is not None:
            value["accepted_receipt"] = accepted
        return self.sign(value)

    def test_received_receipt_verifies_with_public_key(self):
        received = self.receipt("received")
        result = validate_attestation(
            value=received, key=self.public, intent=self.intent,
            receipt_id=None, allowed_states=("received",))
        self.assertEqual(result["status"], "received")
        self.assertFalse(result["accepted_attested"])

    def test_completed_receipt_carries_independently_signed_acceptance(self):
        accepted = self.receipt("accepted")
        completed = self.receipt(
            "completed", digest="a" * 64, accepted=accepted)
        result = validate_attestation(
            value=completed, key=self.public, intent=self.intent,
            receipt_id=self.receipt_id,
            allowed_states=("received", "accepted", "completed", "failed"))
        self.assertEqual(result["status"], "completed")
        self.assertTrue(result["accepted_attested"])
        self.assertEqual(result["result_sha256"], "a" * 64)

    def test_completed_without_acceptance_is_rejected(self):
        completed = self.receipt("completed", digest="a" * 64)
        with self.assertRaisesRegex(ContextRejected, "acceptance history"):
            validate_attestation(
                value=completed, key=self.public, intent=self.intent,
                receipt_id=self.receipt_id, allowed_states=("completed",))

    def test_tampered_outer_receipt_is_rejected(self):
        completed = self.receipt(
            "completed", digest="a" * 64, accepted=self.receipt("accepted"))
        completed["result_sha256"] = "b" * 64
        with self.assertRaisesRegex(ContextRejected, "authentication"):
            validate_attestation(
                value=completed, key=self.public, intent=self.intent,
                receipt_id=self.receipt_id, allowed_states=("completed",))

    def test_tampered_nested_acceptance_is_rejected(self):
        accepted = self.receipt("accepted")
        completed = self.receipt(
            "completed", digest="a" * 64, accepted=accepted)
        completed["accepted_receipt"]["status"] = "received"
        completed = self.sign(completed)
        with self.assertRaises(ContextRejected):
            validate_attestation(
                value=completed, key=self.public, intent=self.intent,
                receipt_id=self.receipt_id, allowed_states=("completed",))

    def test_wrong_commit_and_wrong_dispatch_are_rejected(self):
        received = self.receipt("received")
        received["commit_sha"] = "f" * 40
        received = self.sign(received)
        with self.assertRaisesRegex(ContextRejected, "binding"):
            validate_attestation(
                value=received, key=self.public, intent=self.intent,
                receipt_id=None, allowed_states=("received",))

    def test_receipt_cannot_be_replayed_under_another_receipt_id(self):
        received = self.receipt("received")
        with self.assertRaisesRegex(ContextRejected, "identifier changed"):
            validate_attestation(
                value=received, key=self.public, intent=self.intent,
                receipt_id="other_receipt_123456", allowed_states=("received",))

    def test_wrong_key_is_rejected(self):
        received = self.receipt("received")
        wrong = Ed25519PrivateKey.generate().public_key().public_bytes(
            serialization.Encoding.Raw, serialization.PublicFormat.Raw)
        with self.assertRaisesRegex(ContextRejected, "authentication"):
            validate_attestation(
                value=received, key=wrong, intent=self.intent,
                receipt_id=None, allowed_states=("received",))


    def test_existing_t08_bridge_accepts_completed_v2_with_signed_acceptance_chain(self):
        claim = _claim_ref(self.intent)
        reservation = {
            "status": "reserved_remote", "claim_ref": claim,
            "dispatch_id": self.intent["dispatch_id"], "github_write": True,
            "execution_allowed": False, "agent_mission_executed": False,
        }
        refs = {claim: self.intent["commit_sha"]}
        posts = []

        def get_ref(ref):
            if ref not in refs:
                return 404, {}
            return 200, {"ref": ref, "object": {
                "type": "commit", "sha": refs[ref]}}

        def create_ref(ref, sha):
            if ref in refs:
                return 422, {"message": "already exists"}
            refs[ref] = sha
            return 201, {"ref": ref, "object": {"type": "commit", "sha": sha}}

        def submit(payload):
            posts.append(payload)
            return 202, self.receipt("received")

        result_text = "AGT-ENG remote result: bounded and verified"
        result_digest = __import__("hashlib").sha256(
            result_text.encode("utf-8")).hexdigest()

        def lookup(receipt_id):
            accepted = self.receipt("accepted")
            completed = self.receipt(
                "completed", digest=result_digest, accepted=accepted)
            return 200, {"receipt": completed, "result": result_text}

        result = execute_reserved_intent(
            intent=self.intent, reservation=reservation, receipt_key=self.public,
            verify_authorization=lambda _: True, create_ref=create_ref,
            get_ref=get_ref, submit=submit, lookup=lookup, enabled=True,
            max_polls=1)
        self.assertEqual(result["status"], "remote_completed_attested")
        self.assertEqual(result["result"], "AGT-ENG remote result: bounded and verified")
        self.assertEqual(len(posts), 1)


if __name__ == "__main__":
    unittest.main()
