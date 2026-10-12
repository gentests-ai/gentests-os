"""GT47 T04: read-only GitHub API adapter, disabled unless explicitly invoked.

Requires a caller-supplied authenticated HTTP GET callable. Never executes
agent actions, dispatches workflows, writes comments, or infers authorization.
"""
from __future__ import annotations
import base64
import binascii
import hashlib
import json
from scripts.gt47_t04_context_loader import ContextRejected, POLICY_PATHS, build_envelope
from scripts.gt47_t04_blob_verify import require_blob_sha
from scripts.gt47_t04_event_selection import select_issue_events

REPO = "gentestsai-sudo/gentests-os"
API = "https://api.github.com/repos/" + REPO


def _response(get, path: str, params: dict | None = None) -> dict | list:
    """Caller authenticates requests and enforces TLS; this module cannot do so."""
    data = get(API + path, params or {})
    if type(data) not in (dict, list):
        raise ContextRejected("invalid GitHub API response")
    return data


def fetch_file(get, path: str, commit_sha: str) -> dict:
    if type(commit_sha) is not str or len(commit_sha) != 40 or any(c not in "0123456789abcdef" for c in commit_sha):
        raise ContextRejected("commit SHA must be pinned")
    if type(path) is not str or not (path.startswith("02-Agentes/") or path in POLICY_PATHS.values()) or ".." in path:
        raise ContextRejected("file path not allowlisted")
    result = _response(get, "/contents/" + path, {"ref": commit_sha})
    if type(result) is not dict or result.get("type") != "file" or result.get("encoding") != "base64":
        raise ContextRejected("unexpected content response")
    try:
        raw = base64.b64decode("".join(result["content"].split()), validate=True)
        content = raw.decode("utf-8")
    except (KeyError, TypeError, ValueError, UnicodeError, binascii.Error) as exc:
        raise ContextRejected("invalid content encoding") from exc
    if result.get("path") != path:
        raise ContextRejected("unexpected file path")
    try:
        require_blob_sha(content, result.get("sha"))
    except ValueError as exc:
        raise ContextRejected("file integrity mismatch") from exc
    return {"path": path, "sha": result["sha"], "text": content}


def fetch_issue_comments(get, *, with_metadata=False):
    """Read all pages and select the newest 50 comments, preserving IDs.

    Older comments remain in GitHub's canonical history. This bounded context
    is not evidence of a human authorization or complete mission history.
    """
    records = []
    seen = set()
    last_id = 0
    for page in range(1, 102):
        batch = _response(get, "/issues/47/comments", {"per_page": 100, "page": page})
        if type(batch) is not list or len(batch) > 100:
            raise ContextRejected("invalid comments page")
        if not batch:
            selected = select_issue_events(records[-50:], complete=True)
            if with_metadata:
                return selected, {"total": len(records), "first_id": records[0]["id"] if records else None,
                                  "last_id": records[-1]["id"] if records else None,
                                  "pages_fetched": page, "complete": True,
                                  "consistency": "ordered IDs checked; concurrent insertions not ruled out"}
            return selected
        for item in batch:
            if type(item) is not dict:
                raise ContextRejected("invalid comment item")
            ident = item.get("id")
            if type(item.get("body")) is not str or not item["body"].strip():
                raise ContextRejected("empty or invalid comment")
            if type(ident) is not int or ident <= last_id or ident in seen:
                raise ContextRejected("duplicate or nonmonotonic comment pagination")
            seen.add(ident)
            last_id = ident
            records.append({key: item.get(key) for key in ("id", "body", "html_url")})
        if len(records) > 10000:
            raise ContextRejected("comment history exceeds safe bound")
    raise ContextRejected("pagination incomplete")


def fetch_context(get, *, commit_sha: str, agent_id: str, contract_path: str) -> dict:
    if type(agent_id) is not str or type(contract_path) is not str or not contract_path.startswith("02-Agentes/") or ".." in contract_path:
        raise ContextRejected("invalid agent or contract path")
    contract = fetch_file(get, contract_path, commit_sha)
    policies = {key: fetch_file(get, path, commit_sha) for key, path in POLICY_PATHS.items()}
    events, provenance = fetch_issue_comments(get, with_metadata=True)
    envelope = build_envelope(
        repo=REPO, issue=47, mission="GT-AI-DISPATCH-001", agent_id=agent_id,
        contract_path=contract["path"], contract_text=contract["text"],
        contract_blob_sha=contract["sha"], policy_sources=policies, issue_events=events,
    )
    envelope["source_provenance"] = {"commit_sha": commit_sha, "comments": provenance}
    envelope.pop("envelope_sha256")
    canonical = json.dumps(envelope, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    envelope["envelope_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return envelope
