import hashlib
import json
import unittest
from scripts.gt47_t04_context_loader import ContextRejected
from scripts.gt47_t06_dispatch_intent import prepare_dispatch


def fixture():
    context = {
        "execution_allowed": False, "authorization_granted": False,
        "target": {"repo": "gentestsai-sudo/gentests-os", "issue": 47,
                   "mission": "GT-AI-DISPATCH-001", "agent_id": "AGT-QA"},
        "source_provenance": {"commit_sha": "a" * 40, "comments": {"complete": True}},
    }
    context["envelope_sha256"] = hashlib.sha256(json.dumps(
        context, sort_keys=True, ensure_ascii=False,
        separators=(",", ":")).encode("utf-8")).hexdigest()
    request = {"mission": "GT-AI-DISPATCH-001", "issue": 47, "agent_id": "AGT-QA",
               "commit_sha": "a" * 40, "nonce": "unique_nonce_0001"}
    return context, request


class T06Tests(unittest.TestCase):
    def test_prepared_is_inert_and_deterministic(self):
        context, request = fixture()
        result = prepare_dispatch(context=context, request=request)
        self.assertEqual(result["status"], "prepared_offline")
        self.assertFalse(result["execution_allowed"])
        self.assertFalse(result["external_agent_invoked"])
        self.assertFalse(result["replay_protection_persistent"])
        self.assertEqual(result["dispatch_id"],
                         prepare_dispatch(context=context, request=request)["dispatch_id"])

    def test_tampered_context_rejected(self):
        context, request = fixture()
        context["target"]["agent_id"] = "AGT-ENG"
        with self.assertRaises(ContextRejected):
            prepare_dispatch(context=context, request=request)

    def test_incomplete_history_rejected(self):
        context, request = fixture()
        context["source_provenance"]["comments"]["complete"] = False
        with self.assertRaises(ContextRejected):
            prepare_dispatch(context=context, request=request)

    def test_wrong_destination_rejected(self):
        context, request = fixture()
        request["agent_id"] = "AGT-ENG"
        with self.assertRaises(ContextRejected):
            prepare_dispatch(context=context, request=request)

    def test_untrusted_fields_rejected(self):
        context, request = fixture()
        request["execute"] = True
        with self.assertRaises(ContextRejected):
            prepare_dispatch(context=context, request=request)

    def test_unsafe_nonce_rejected(self):
        context, request = fixture()
        request["nonce"] = "../run"
        with self.assertRaises(ContextRejected):
            prepare_dispatch(context=context, request=request)

    def test_authority_never_inferred_from_context(self):
        context, request = fixture()
        context["authorization_granted"] = True
        with self.assertRaises(ContextRejected):
            prepare_dispatch(context=context, request=request)


if __name__ == "__main__":
    unittest.main()
