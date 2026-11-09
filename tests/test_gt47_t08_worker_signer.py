import base64
import hashlib
import unittest

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

from scripts.gt47_sign_worker_decision import (
    DOMAIN, canonical, sign_request,
)


class WorkerDecisionSignerTests(unittest.TestCase):
    def setUp(self):
        self.private = Ed25519PrivateKey.generate()
        self.pem = self.private.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.PKCS8,
            serialization.NoEncryption(),
        )
        self.task = "Execute a bounded engineering task"
        self.context = {"source": "signed", "summary": "contexto válido"}

    def sign(self, **overrides):
        values = {
            "task": self.task, "context": self.context,
            "commit_sha": "a" * 40, "contract_blob_sha": "b" * 40,
            "nonce": "nonce_worker_123456", "decision_id": "decision_123456789",
            "issuer_key_id": "direction-key-v1",
            "issuer_human_id": "director-123", "private_key_pem": self.pem,
            "max_tokens": 512, "max_incremental_cost_usd_micros": 15000,
            "allowed_tools": ["read_file"], "max_model_calls": 2, "max_tool_calls": 1,
            "now": 1794268800,
        }
        values.update(overrides)
        return sign_request(**values)

    def test_signed_envelope_matches_worker_dispatch_and_claim_identity(self):
        envelope = self.sign()
        decision = envelope["decision"]
        self.assertEqual(set(envelope), {"decision", "signature", "task", "context"})
        self.assertEqual(decision["version"], 3)
        self.assertEqual(decision["allowed_tools"], ["read_file"])
        self.assertEqual(decision["max_model_calls"], 2)
        self.assertEqual(decision["max_tool_calls"], 1)
        self.assertNotIn("max_calls", decision)
        self.assertEqual(decision["mission"], "GT-AI-DISPATCH-001")
        self.assertEqual(decision["agent_id"], "AGT-ENG")
        self.assertEqual(decision["max_calls"], 1)
        self.assertEqual(decision["max_incremental_cost_usd_micros"], 10000)
        self.assertTrue(decision["no_paid_fallback"])
        expected_input = hashlib.sha256(canonical({
            "task": self.task, "context": self.context})).hexdigest()
        self.assertEqual(decision["input_sha256"], expected_input)
        expected_dispatch = hashlib.sha256(canonical({
            "mission": decision["mission"], "issue": 47,
            "agent_id": "AGT-ENG", "commit_sha": "a" * 40,
            "nonce": "nonce_worker_123456"})).hexdigest()
        self.assertEqual(decision["dispatch_id"], expected_dispatch)
        public = self.private.public_key()
        signature = base64.urlsafe_b64decode(
            envelope["signature"] + "=" * (-len(envelope["signature"]) % 4))
        public.verify(signature, DOMAIN + canonical(decision))

    def test_signer_requires_budget_for_bounded_tool_loop(self):
        request = self.sign(
            allowed_tools=["read_file", "write_file", "open_pull_request"],
            max_model_calls=4, max_tool_calls=3,
            max_incremental_cost_usd_micros=50000)
        self.assertEqual(request["decision"]["allowed_tools"],
                         ["open_pull_request", "read_file", "write_file"])
        self.assertEqual(request["decision"]["max_model_calls"], 4)
        self.assertEqual(request["decision"]["max_tool_calls"], 3)
        with self.assertRaises(ValueError):
            self.sign(allowed_tools=["merge_pull_request"],
                      max_model_calls=2, max_tool_calls=1,
                      max_incremental_cost_usd_micros=30000)
        with self.assertRaises(ValueError):
            self.sign(allowed_tools=["write_file"],
                      max_model_calls=2, max_tool_calls=1,
                      max_incremental_cost_usd_micros=10000)

    def test_claim_ref_preserves_historical_namespace(self):
        decision = self.sign()["decision"]
        expected = hashlib.sha256(canonical({
            "repo": "gentestsai-sudo/gentests-os",
            "mission": "GT-AI-DISPATCH-001", "issue": 47,
            "agent_id": "AGT-ENG", "commit_sha": "a" * 40,
        })).hexdigest()
        self.assertEqual(decision["claim_ref"],
                         "refs/tags/gt47-claims/" + expected)

    def test_signer_rejects_invalid_scope_and_key_type(self):
        with self.assertRaises(ValueError):
            self.sign(max_tokens=1025)
        with self.assertRaises(ValueError):
            self.sign(max_incremental_cost_usd_micros=0)
        with self.assertRaises(ValueError):
            self.sign(allowed_tools=[])
        with self.assertRaises(ValueError):
            self.sign(commit_sha="not-a-commit")
        with self.assertRaises(ValueError):
            self.sign(context={"chave-é": "value"})

    def test_signer_never_generates_or_writes_private_keys(self):
        import inspect
        from scripts import gt47_sign_worker_decision
        source = inspect.getsource(gt47_sign_worker_decision)
        self.assertNotIn("Ed25519PrivateKey.generate", source)
        self.assertNotIn("write_bytes(key", source)
        self.assertIn("os.O_EXCL", source)
        self.assertIn("os.O_WRONLY", source)


if __name__ == "__main__":
    unittest.main()
