"""Explicit opt-in read-only GitHub API transport.

The caller supplies a token; never print, store or log it. No automatic
execution or dispatch is initiated by importing this module.
"""
from __future__ import annotations
import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlparse
from urllib.request import Request, build_opener, HTTPRedirectHandler
from scripts.gt47_t04_context_loader import ContextRejected

API_HOST = "api.github.com"


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None

MAX_BYTES = 512_000


def github_readonly_get(url: str, params: dict, *, token: str):
    if type(token) is not str or not token.strip():
        raise ContextRejected("GitHub token required")
    if type(url) is not str:
        raise ContextRejected("invalid URL")
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname != API_HOST or parsed.port is not None or parsed.username or parsed.password or parsed.query or parsed.fragment:
        raise ContextRejected("GitHub API host mismatch")
    root = "/repos/gentests-ai/gentests-os/"
    tail = parsed.path[len(root):] if parsed.path.startswith(root) else ""
    if not (tail.startswith("contents/02-Agentes/") or tail.startswith("contents/00-Constituicao/") or tail.startswith("contents/03-Processos/") or tail == "issues/47/comments"):
        raise ContextRejected("GitHub repository mismatch")
    if type(params) is not dict:
        raise ContextRejected("invalid query parameters")
    if tail == "issues/47/comments":
        if set(params) != {"per_page", "page"} or type(params["per_page"]) is not int or params["per_page"] != 10 or type(params["page"]) is not int or not 1 <= params["page"] <= 1001:
            raise ContextRejected("invalid comments pagination")
    else:
        if set(params) != {"ref"} or type(params["ref"]) is not str or len(params["ref"]) != 40 or any(c not in "0123456789abcdef" for c in params["ref"]):
            raise ContextRejected("invalid pinned commit ref")
    full_url = url + ("?" + urlencode(params) if params else "")
    request = Request(full_url, headers={
        "Authorization": "Bearer " + token,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "GenTests-GT47-ReadOnly",
    }, method="GET")
    try:
        with build_opener(NoRedirect).open(request, timeout=15) as response:
            if response.status != 200:
                raise ContextRejected("unexpected GitHub status")
            raw = response.read(MAX_BYTES + 1)
    except HTTPError as exc:
        # Emit only status: never leak response body, URL, token or headers.
        raise ContextRejected(f"GitHub HTTP status {exc.code}") from None
    except (URLError, TimeoutError):
        raise ContextRejected("GitHub network read failed") from None
    if len(raw) > MAX_BYTES:
        raise ContextRejected("GitHub response too large")
    try:
        return json.loads(raw.decode("utf-8"))
    except (ValueError, UnicodeError) as exc:
        raise ContextRejected("invalid GitHub JSON") from exc
