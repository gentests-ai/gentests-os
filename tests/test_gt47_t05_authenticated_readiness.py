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


if __name__ == "__main__":
    unittest.main()
