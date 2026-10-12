"""Offline T05 safety and integration tests."""
import unittest
from unittest.mock import patch
from scripts.gt47_t04_context_loader import ContextRejected
from scripts.gt47_t05_authenticated_readiness import authenticated_readiness


class T05ReadinessTests(unittest.TestCase):
    def test_missing_token_rejected_without_network(self):
        with patch("scripts.gt47_t05_authenticated_readiness.github_readonly_get") as network:
            with self.assertRaises(ContextRejected):
                authenticated_readiness(token="", commit_sha="a" * 40,
                                        agent_id="AGT-QA", contract_path="02-Agentes/qa.md")
            network.assert_not_called()

    def test_unpinned_commit_rejected_without_network(self):
        with patch("scripts.gt47_t05_authenticated_readiness.github_readonly_get") as network:
            with self.assertRaises(ContextRejected):
                authenticated_readiness(token="test-token", commit_sha="main",
                                        agent_id="AGT-QA", contract_path="02-Agentes/qa.md")
            network.assert_not_called()

    def test_invalid_envelope_fails_closed(self):
        with patch("scripts.gt47_t05_authenticated_readiness.fetch_context",
                   return_value={"envelope_sha256": "fake", "execution_allowed": False}):
            with self.assertRaises(ContextRejected):
                authenticated_readiness(token="test-token", commit_sha="a" * 40,
                                        agent_id="AGT-QA", contract_path="02-Agentes/qa.md",
                                        get=lambda url, params: None)

    def test_execution_enabled_fails_closed(self):
        with patch("scripts.gt47_t05_authenticated_readiness.fetch_context",
                   return_value={"envelope_sha256": "fake", "execution_allowed": True}):
            with self.assertRaises(ContextRejected):
                authenticated_readiness(token="test-token", commit_sha="a" * 40,
                                        agent_id="AGT-QA", contract_path="02-Agentes/qa.md",
                                        get=lambda url, params: None)


    def test_missing_provenance_fails_closed(self):
        import hashlib
        import json
        envelope = {"agent_id": "AGT-QA", "execution_allowed": False}
        envelope["envelope_sha256"] = hashlib.sha256(json.dumps(
            envelope, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")).hexdigest()
        with patch("scripts.gt47_t05_authenticated_readiness.fetch_context",
                   return_value=envelope):
            with self.assertRaises(ContextRejected):
                authenticated_readiness(token="test-token", commit_sha="a" * 40,
                                        agent_id="AGT-QA", contract_path="02-Agentes/qa.md",
                                        get=lambda url, params: None)

    def test_agent_identity_mismatch_fails_closed(self):
        import hashlib
        import json
        envelope = {"agent_id": "AGT-ENG", "execution_allowed": False,
                    "source_provenance": {"commit_sha": "a" * 40,
                                          "comments": {"complete": True}}}
        envelope["envelope_sha256"] = hashlib.sha256(json.dumps(
            envelope, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")).hexdigest()
        with patch("scripts.gt47_t05_authenticated_readiness.fetch_context",
                   return_value=envelope):
            with self.assertRaises(ContextRejected):
                authenticated_readiness(token="test-token", commit_sha="a" * 40,
                                        agent_id="AGT-QA", contract_path="02-Agentes/qa.md",
                                        get=lambda url, params: None)


    def test_valid_verified_envelope_returns_readonly_summary(self):
        import hashlib
        import json
        envelope = {"target": {"agent_id": "AGT-QA", "repo": "gentests-ai/gentests-os",
                               "issue": 47, "mission": "GT-AI-DISPATCH-001"}, "execution_allowed": False,
                    "source_provenance": {"commit_sha": "a" * 40,
                                          "comments": {"complete": True, "total": 1}}}
        envelope["envelope_sha256"] = hashlib.sha256(json.dumps(
            envelope, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")).hexdigest()
        with patch("scripts.gt47_t05_authenticated_readiness.fetch_context",
                   return_value=envelope):
            result = authenticated_readiness(
                token="test-token", commit_sha="a" * 40,
                agent_id="AGT-QA", contract_path="02-Agentes/qa.md",
                get=lambda url, params: None)
        self.assertEqual(result["status"], "read_only_e2e_pass")
        self.assertFalse(result["execution_allowed"])
        self.assertFalse(result["external_agent_invoked"])
        self.assertNotIn("test-token", repr(result))


    def test_wrong_mission_fails_closed_with_valid_digest(self):
        import hashlib
        import json
        envelope = {"target": {"agent_id": "AGT-QA", "repo": "gentests-ai/gentests-os",
                               "issue": 48, "mission": "GT-AI-DISPATCH-001"},
                    "execution_allowed": False,
                    "source_provenance": {"commit_sha": "a" * 40,
                                          "comments": {"complete": True}}}
        envelope["envelope_sha256"] = hashlib.sha256(json.dumps(
            envelope, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")).hexdigest()
        with patch("scripts.gt47_t05_authenticated_readiness.fetch_context",
                   return_value=envelope):
            with self.assertRaises(ContextRejected):
                authenticated_readiness(token="test-token", commit_sha="a" * 40,
                                        agent_id="AGT-QA", contract_path="02-Agentes/qa.md",
                                        get=lambda url, params: None)


if __name__ == "__main__":
    unittest.main()
