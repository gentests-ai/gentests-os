"""Offline integrity check for already fetched GitHub UTF-8 files."""
import hashlib


def git_blob_sha(content: str) -> str:
    if type(content) is not str:
        raise ValueError("content must be UTF-8 text")
    data = content.encode("utf-8")
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\x00" + data).hexdigest()


def require_blob_sha(content: str, expected_sha: str) -> None:
    if type(expected_sha) is not str or git_blob_sha(content) != expected_sha:
        raise ValueError("Git blob SHA mismatch")
