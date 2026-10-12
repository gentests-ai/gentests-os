import json
import unittest
from scripts.gt47_t04_context_loader import ContextRejected
from scripts.gt47_t06_event_planner import plan_issue_event


def event(labels, number=47, repo="gentestsai-sudo/gentests-os", action="labeled"):
    return json.dumps({"action": action, "repository": {"full_name": repo},
        "issue": {"number": number, "labels": [{"name": x} for x in labels]},
        "label": {"name": labels[-1] if labels else ""}}).encode()


class EventPlannerTests(unittest.TestCase):
    def test_valid_route_is_inert(self):
        result = plan_issue_event(event(["gt47-agent:AGT-QA"]))
        self.assertEqual(result["agent_id"], "AGT-QA")
        self.assertFalse(result["github_write"])
        self.assertFalse(result["external_agent_invoked"])

    def test_rejects_ambiguous_routes(self):
        with self.assertRaises(ContextRejected):
            plan_issue_event(event(["gt47-agent:AGT-QA", "gt47-agent:AGT-ENG"]))

    def test_rejects_unknown_agent(self):
        with self.assertRaises(ContextRejected):
            plan_issue_event(event(["gt47-agent:AGT-ROOT"]))

    def test_rejects_wrong_issue(self):
        with self.assertRaises(ContextRejected):
            plan_issue_event(event(["gt47-agent:AGT-QA"], number=48))

    def test_rejects_wrong_repo(self):
        with self.assertRaises(ContextRejected):
            plan_issue_event(event(["gt47-agent:AGT-QA"], repo="other/repo"))

    def test_rejects_stale_reopen_and_unrelated_label(self):
        with self.assertRaises(ContextRejected):
            plan_issue_event(event(["gt47-agent:AGT-QA"], action="reopened"))
        payload = json.loads(event(["gt47-agent:AGT-QA", "documentation"]))
        with self.assertRaises(ContextRejected):
            plan_issue_event(json.dumps(payload).encode())

    def test_rejects_unsupported_action(self):
        with self.assertRaises(ContextRejected):
            plan_issue_event(event(["gt47-agent:AGT-QA"], action="edited"))

    def test_rejects_oversized_event(self):
        with self.assertRaises(ContextRejected):
            plan_issue_event(b"x" * 32769)


if __name__ == "__main__":
    unittest.main()
