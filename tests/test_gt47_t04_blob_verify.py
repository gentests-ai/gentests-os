"""Offline Git blob identity tests."""
import unittest
from scripts.gt47_t04_blob_verify import git_blob_sha, require_blob_sha


class BlobIntegrityTests(unittest.TestCase):
    def test_known_git_blob(self):
        self.assertEqual(git_blob_sha("hello\n"), "ce013625030ba8dba906f756967f9e9ca394464a")

    def test_matching_blob(self):
        require_blob_sha("hello\n", "ce013625030ba8dba906f756967f9e9ca394464a")

    def test_tampered_content_rejected(self):
        with self.assertRaises(ValueError):
            require_blob_sha("hello", "ce013625030ba8dba906f756967f9e9ca394464a")

    def test_invalid_sha_type_rejected(self):
        with self.assertRaises(ValueError):
            require_blob_sha("hello\n", None)


if __name__ == "__main__":
    unittest.main()
