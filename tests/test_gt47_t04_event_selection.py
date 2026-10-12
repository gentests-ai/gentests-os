import unittest
from scripts.gt47_t04_context_loader import ContextRejected
from scripts.gt47_t04_event_selection import select_issue_events, PREFIX


class EventSelectionTests(unittest.TestCase):
    def event(self, eid=12):
        return {"id": eid, "body": "evidence only", "html_url": PREFIX + str(eid)}

    def test_valid_comment(self):
        self.assertEqual(select_issue_events([self.event()])[0]["id"], "12")

    def test_duplicate_rejected(self):
        with self.assertRaises(ContextRejected):
            select_issue_events([self.event(), self.event()])

    def test_spoofed_url_rejected(self):
        record = self.event()
        record["html_url"] += "9"
        with self.assertRaises(ContextRejected):
            select_issue_events([record])

    def test_partial_page_rejected(self):
        with self.assertRaises(ContextRejected):
            select_issue_events([self.event()], limit=0)

    def test_limit_rejected(self):
        with self.assertRaises(ContextRejected):
            select_issue_events([self.event(10), self.event(11)], limit=1)

    def test_boolean_id_rejected(self):
        with self.assertRaises(ContextRejected):
            select_issue_events([self.event(True)])


if __name__ == "__main__":
    unittest.main()
