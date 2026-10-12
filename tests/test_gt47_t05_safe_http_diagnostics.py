import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError
from scripts.gt47_t04_context_loader import ContextRejected
from scripts.gt47_t04_transport import github_readonly_get

URL = "https://api.github.com/repos/gentests-ai/gentests-os/contents/02-Agentes/QA/Contrato-Agente-QA.md"
PARAMS = {"ref": "a" * 40}

class SafeHttpDiagnosticTests(unittest.TestCase):
    def test_http_status_no_secrets(self):
        class FakeOpener:
            def open(self, request, timeout):
                raise HTTPError(request.full_url, 403, "Forbidden", {}, None)
        with patch("scripts.gt47_t04_transport.build_opener", return_value=FakeOpener()):
            with self.assertRaises(ContextRejected) as caught:
                github_readonly_get(URL, PARAMS, token="sensitive-token")
        self.assertEqual(str(caught.exception), "GitHub HTTP status 403")
        self.assertNotIn("sensitive-token", str(caught.exception))
        self.assertNotIn(URL, str(caught.exception))

    def test_network_error_no_secrets(self):
        class FakeOpener:
            def open(self, request, timeout):
                raise URLError("sensitive-token")
        with patch("scripts.gt47_t04_transport.build_opener", return_value=FakeOpener()):
            with self.assertRaises(ContextRejected) as caught:
                github_readonly_get(URL, PARAMS, token="sensitive-token")
        self.assertEqual(str(caught.exception), "GitHub network read failed")

if __name__ == "__main__":
    unittest.main()
