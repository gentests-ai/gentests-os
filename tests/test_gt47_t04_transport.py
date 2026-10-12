import unittest
from scripts.gt47_t04_context_loader import ContextRejected
from scripts.gt47_t04_transport import github_readonly_get


class TransportTests(unittest.TestCase):
    def test_missing_token_rejected(self):
        with self.assertRaises(ContextRejected):
            github_readonly_get("https://api.github.com/repos/gentests-ai/gentests-os/issues/47/comments", {}, token="")

    def test_external_host_rejected(self):
        with self.assertRaises(ContextRejected):
            github_readonly_get("https://example.com/repos/gentests-ai/gentests-os/issues/47/comments", {}, token="test")

    def test_cross_repo_rejected(self):
        with self.assertRaises(ContextRejected):
            github_readonly_get("https://api.github.com/repos/other/repo/issues/47/comments", {}, token="test")

    def test_write_endpoint_rejected(self):
        with self.assertRaises(ContextRejected):
            github_readonly_get("https://api.github.com/repos/gentests-ai/gentests-os/actions/workflows", {}, token="test")

    def test_unpinned_content_ref_rejected(self):
        with self.assertRaises(ContextRejected):
            github_readonly_get("https://api.github.com/repos/gentests-ai/gentests-os/contents/02-Agentes/x.md", {"ref": "main"}, token="test")

    def test_unbounded_pagination_rejected(self):
        with self.assertRaises(ContextRejected):
            github_readonly_get("https://api.github.com/repos/gentests-ai/gentests-os/issues/47/comments", {"per_page": 100, "page": 99}, token="test")

    def test_query_in_url_rejected(self):
        with self.assertRaises(ContextRejected):
            github_readonly_get("https://api.github.com/repos/gentests-ai/gentests-os/issues/47/comments?page=1", {}, token="test")


if __name__ == "__main__":
    unittest.main()
