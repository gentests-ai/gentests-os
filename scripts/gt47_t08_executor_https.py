"""GT47 T08 HTTPS transport for a separately authorized connected executor.

Nothing is invoked on import. Caller configures an approved endpoint, an
independent host allowlist, a bearer secret, and an explicit runtime activation
gate. Issue payloads must NEVER choose the endpoint, path or credentials.
"""
from __future__ import annotations
import ipaddress
import json
import re
from urllib.parse import urlsplit
from urllib.request import Request, build_opener, HTTPRedirectHandler
from urllib.error import HTTPError, URLError

from scripts.gt47_t04_context_loader import ContextRejected

_MAX_BODY = 32768
_RID = re.compile(r"[a-zA-Z0-9_-]{16,64}\Z")
_SHA40 = re.compile(r"[0-9a-f]{40}\Z")
_SHA64 = re.compile(r"[0-9a-f]{64}\Z")
_AGENT = re.compile(r"AGT-[A-Z][A-Z0-9-]{1,30}\Z")
_CLAIM_REF = re.compile(r"refs/tags/gt47-claims/[0-9a-f]{64}\Z")
_HOST = re.compile(
    r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)"
    r"(?:\.(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?))+\Z"
)
_REQUEST_KEYS = frozenset({
    "schema", "mission", "issue", "agent_id", "commit_sha",
    "context_sha256", "dispatch_id", "claim_ref",
})


class _RejectRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ContextRejected("executor redirect rejected")


def _unique_json_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ContextRejected("duplicate executor JSON property")
        result[key] = value
    return result


class ExecutorHTTPS:
    def __init__(self, *, endpoint: str, allowed_hosts: tuple,
                 bearer: str, timeout: int = 12, opener=None):
        try:
            parts = urlsplit(endpoint) if type(endpoint) is str else None
            port = parts.port if parts is not None else None
        except ValueError as exc:
            raise ContextRejected("invalid executor endpoint") from exc
        if (parts is None or parts.scheme != "https"
                or parts.username is not None or parts.password is not None
                or parts.query or parts.fragment
                or parts.path != "/v1/gt47/dispatch"
                or port not in (None, 443)
                or type(allowed_hosts) is not tuple
                or not allowed_hosts):
            raise ContextRejected("invalid approved executor endpoint")
        host = parts.hostname or ""
        try:
            ipaddress.ip_address(host)
        except ValueError:
            pass
        else:
            raise ContextRejected("IP literal executor endpoint forbidden")
        valid_hosts = all(
            type(value) is str and _HOST.fullmatch(value)
            and not value.endswith((".local", ".internal"))
            for value in allowed_hosts
        )
        if (not valid_hosts or not _HOST.fullmatch(host)
                or host.endswith((".local", ".internal"))
                or host not in allowed_hosts
                or parts.netloc not in (host, host + ":443")):
            raise ContextRejected("executor endpoint not allowlisted")
        if (type(bearer) is not str or len(bearer.strip()) < 24
                or any(ord(ch) < 33 or ord(ch) > 126 for ch in bearer)):
            raise ContextRejected("executor credential missing")
        if type(timeout) is not int or not 1 <= timeout <= 30:
            raise ContextRejected("executor timeout out of bounds")
        self._base = "https://" + host
        self._bearer = bearer
        self._timeout = timeout
        self._opener = opener if opener is not None else build_opener(_RejectRedirects())

    def _request(self, path: str, data: dict | None):
        body = None
        if data is not None:
            body = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
            if len(body) > _MAX_BODY:
                raise ContextRejected("executor request too large")
        request = Request(self._base + path, data=body,
                          method="POST" if body is not None else "GET",
                          headers={"Authorization": "Bearer " + self._bearer,
                                   "Accept": "application/json",
                                   "Content-Type": "application/json"})
        try:
            with self._opener.open(request, timeout=self._timeout) as response:
                code = response.status
                if response.headers.get_content_type() != "application/json":
                    raise ContextRejected("executor content type mismatch")
                raw = response.read(_MAX_BODY + 1)
        except ContextRejected:
            raise
        except HTTPError as exc:
            # Discard all response bodies; no external URL or secret in errors.
            return exc.code, {}
        except (URLError, TimeoutError, OSError) as exc:
            raise ContextRejected("executor HTTPS outcome uncertain") from None
        if len(raw) > _MAX_BODY:
            raise ContextRejected("executor response too large")
        try:
            payload = json.loads(raw.decode("utf-8"),
                                 object_pairs_hook=_unique_json_object)
        except (ValueError, UnicodeError) as exc:
            raise ContextRejected("malformed executor JSON response") from exc
        if type(payload) is not dict:
            raise ContextRejected("executor response must be object")
        return code, payload

    def submit(self, payload: dict):
        if (type(payload) is not dict or set(payload) != _REQUEST_KEYS
                or payload.get("schema") != "gt47-executor-request-v1"
                or payload.get("mission") != "GT-AI-DISPATCH-001"
                or type(payload.get("issue")) is not int or payload["issue"] != 47
                or type(payload.get("agent_id")) is not str
                or not _AGENT.fullmatch(payload["agent_id"])
                or type(payload.get("commit_sha")) is not str
                or not _SHA40.fullmatch(payload["commit_sha"])
                or type(payload.get("context_sha256")) is not str
                or not _SHA64.fullmatch(payload["context_sha256"])
                or type(payload.get("dispatch_id")) is not str
                or not _SHA64.fullmatch(payload["dispatch_id"])
                or type(payload.get("claim_ref")) is not str
                or not _CLAIM_REF.fullmatch(payload["claim_ref"])):
            raise ContextRejected("invalid or unbounded executor request")
        return self._request("/v1/gt47/dispatch", payload)

    def lookup(self, receipt_id: str):
        if type(receipt_id) is not str or not _RID.fullmatch(receipt_id):
            raise ContextRejected("invalid receipt lookup ID")
        return self._request("/v1/gt47/receipts/" + receipt_id, None)
