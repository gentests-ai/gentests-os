import base64
import unittest
from scripts.gt47_t04_blob_verify import git_blob_sha
from scripts.gt47_t04_context_loader import ContextRejected
from scripts.gt47_t04_github_adapter import fetch_file, fetch_issue_comments, API

SHA = "a" * 40
PATH = "00-Constituicao/Matriz-de-Permissoes.md"


class AdapterTests(unittest.TestCase):
    def test_file_integrity(self):
        content = "test policy\n"
        def get(url, params):
            self.assertEqual(url, API + "/contents/" + PATH)
            self.assertEqual(params["ref"], SHA)
            return {"type": "file", "encoding": "base64", "path": PATH,
                    "sha": git_blob_sha(content),
                    "content": base64.b64encode(content.encode()).decode()}
        self.assertEqual(fetch_file(get, PATH, SHA)["text"], content)

    def test_malformed_base64_rejected(self):
        def get(url, params):
            return {"type": "file", "encoding": "base64", "path": PATH,
                    "sha": "0" * 40, "content": "!!!!"}
        with self.assertRaises(ContextRejected):
            fetch_file(get, PATH, SHA)

    def test_tampered_file(self):
        def get(url, params):
            return {"type": "file", "encoding": "base64", "path": PATH,
                    "sha": "0" * 40, "content": base64.b64encode(b"changed").decode()}
        with self.assertRaises(ContextRejected):
            fetch_file(get, PATH, SHA)

    def test_comments_complete(self):
        calls = []
        def get(url, params):
            calls.append(params["page"])
            if params["page"] == 1:
                return [{"id": 8, "body": "data",
                         "html_url": "https://github.com/gentestsai-sudo/gentests-os/issues/47#issuecomment-8"}]
            return []
        self.assertEqual(fetch_issue_comments(get)[0]["id"], "8")
        self.assertEqual(calls, [1, 2])

    def test_comments_full_history_selects_latest(self):
        def get(url, params):
            page = params["page"]
            if page > 4:
                return []
            start = (page - 1) * 100
            return [{"id": i, "body": "data",
                     "html_url": "https://github.com/gentestsai-sudo/gentests-os/issues/47#issuecomment-" + str(i)}
                    for i in range(start + 1, start + 101)]
        selected = fetch_issue_comments(get)
        self.assertEqual(len(selected), 50)
        self.assertEqual(selected[0]["id"], "351")
        self.assertEqual(selected[-1]["id"], "400")

    def test_comments_limit(self):
        def get(url, params):
            return [{"id": i + 1, "body": "data",
                     "html_url": "https://github.com/gentestsai-sudo/gentests-os/issues/47#issuecomment-" + str(i + 1)}
                    for i in range(51)]
        self.assertEqual(len(fetch_issue_comments(get)), 50)

    def test_comments_malformed(self):
        with self.assertRaises(ContextRejected):
            fetch_issue_comments(lambda url, params: {"error": "not found"})


if __name__ == "__main__":
    unittest.main()
