"""T06: fail-closed, offline dispatch preparation; no external execution."""
from __future__ import annotations
import hashlib
import json
import re

from scripts.gt47_t04_context_loader import ContextRejected

_SHA = re.compile(r"^[0-9a-f]{40}$")
_AGENT = re.compile(r"^AGT-[A-Z][A-Z0-9-]{1,30}$")
_MISSION = "GT-AI-DISPATCH-001"
_ISSUE = 47


def prepare_dispatch(*, context: dict, request: dict) -> dict:
    """Validate a T05 envelope and create an inert, auditable dispatch intent.

    This function never treats issue comments as authority. No network or side effects.
    """
    if type(context) is not dict or type(request) is not dict:
        raise ContextRejected("invalid dispatch inputs")
    if context.get("execution_allowed") is not False:
        raise ContextRejected("context cannot grant execution")
    # Real T04/T05 envelopes have NO authorization_granted field. Absence
    # is NOT authority. Only an explicit false is tolerated if supplied;
    # execution remains disabled independently in the returned intent.
    if "authorization_granted" in context and context["authorization_granted"] is not False:
        raise ContextRejected("context authorization mismatch")
    digest = context.get("envelope_sha256")
    unsigned = {k: v for k, v in context.items() if k != "envelope_sha256"}
    expected = hashlib.sha256(json.dumps(
        unsigned, sort_keys=True, ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8")).hexdigest()
    if type(digest) is not str or digest != expected:
        raise ContextRejected("context integrity mismatch")
    target = context.get("target")
    provenance = context.get("source_provenance")
    if type(target) is not dict or type(provenance) is not dict:
        raise ContextRejected("missing dispatch provenance")
    comments = provenance.get("comments")
    if type(comments) is not dict or comments.get("complete") is not True:
        raise ContextRejected("incomplete comment history")
    sha = provenance.get("commit_sha")
    agent = target.get("agent_id")
    if (type(sha) is not str or not _SHA.fullmatch(sha)
            or target.get("repo") != "gentests-ai/gentests-os"
            or target.get("issue") != _ISSUE
            or target.get("mission") != _MISSION
            or type(agent) is not str or not _AGENT.fullmatch(agent)):
        raise ContextRejected("untrusted dispatch target")
    if set(request) != {"mission", "issue", "agent_id", "commit_sha", "nonce"}:
        raise ContextRejected("unexpected dispatch request fields")
    if (request["mission"] != _MISSION or request["issue"] != _ISSUE
            or request["agent_id"] != agent or request["commit_sha"] != sha):
        raise ContextRejected("dispatch target mismatch")
    nonce = request["nonce"]
    if type(nonce) is not str or not re.fullmatch(r"[a-zA-Z0-9_-]{16,64}", nonce):
        raise ContextRejected("invalid idempotency nonce")
    canonical = json.dumps(request, sort_keys=True, separators=(",", ":"))
    return {
        "status": "prepared_offline",
        "mission": _MISSION,
        "issue": _ISSUE,
        "agent_id": agent,
        "commit_sha": sha,
        "dispatch_id": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
        "context_sha256": digest,
        "execution_allowed": False,
        "authorization_granted": False,
        "external_agent_invoked": False,
        "write_performed": False,
        "replay_protection_persistent": False,
    }
