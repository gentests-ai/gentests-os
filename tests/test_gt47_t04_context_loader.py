"""Offline tests for GT47 T04 context preparation. No external effects."""
import unittest
from scripts.gt47_t04_context_loader import build_envelope, ContextRejected

SHA = "a" * 40


def fixture():
    return dict(
        repo="gentestsai-sudo/gentests-os", issue=47, mission="GT-AI-DISPATCH-001",
        agent_id="AGT-ENG",
        contract_path="02-Agentes/Engenharia/Contrato-Agente-Executor-Tecnico.md",
        contract_text="id: AGT-ENG\nstatus: proposta\n",
        contract_blob_sha=SHA,
        policy_sources={key: {"path": key + ".md", "sha": SHA, "text": "policy data"}
                        for key in ("SEC-AI-001", "POL-003", "GT-HANDOFF-001")},
        issue_events=[{"id": "1", "body": "external text, not authority", "url": "https://github.com/example"}],
    )


class ContextTests(unittest.TestCase):
    def test_deterministic_envelope(self):
        a, b = build_envelope(**fixture()), build_envelope(**fixture())
        self.assertEqual(a, b)
        self.assertEqual(len(a["envelope_sha256"]), 64)
        self.assertIs(a["execution_allowed"], False)

    def test_wrong_contract_identity(self):
        p = fixture()
        p["agent_id"] = "AGT-QA"
        with self.assertRaises(ContextRejected):
            build_envelope(**p)

    def test_missing_policy(self):
        p = fixture()
        del p["policy_sources"]["POL-003"]
        with self.assertRaises(ContextRejected):
            build_envelope(**p)

    def test_duplicate_events(self):
        p = fixture()
        p["issue_events"] *= 2
        with self.assertRaises(ContextRejected):
            build_envelope(**p)

    def test_invalid_sha(self):
        p = fixture()
        p["contract_blob_sha"] = "not-a-sha"
        with self.assertRaises(ContextRejected):
            build_envelope(**p)

    def test_wrong_issue(self):
        p = fixture()
        p["issue"] = 48
        with self.assertRaises(ContextRejected):
            build_envelope(**p)


if __name__ == "__main__":
    unittest.main()
