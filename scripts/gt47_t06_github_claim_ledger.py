"""GT47 Infra: opt-in, cross-run reservation using GitHub Git refs.

No HTTP client, secrets, Actions trigger, or automatic execution is provided.
The caller must separately verify authorization and inject authenticated HTTPS
functions; tests inject local fakes. This only claims a dispatch attempt; it
is NOT a receipt, acceptance, mission execution, or exactly-once guarantee.
"""
from __future__ import annotations
import hashlib
import json
import re
from scripts.gt47_t04_context_loader import ContextRejected

_REPO = "gentestsai-sudo/gentests-os"
_SHA40 = re.compile(r"[0-9a-f]{40}\Z")
_SHA64 = re.compile(r"[0-9a-f]{64}\Z")
_AGENT = re.compile(r"AGT-[A-Z][A-Z0-9-]{1,30}\Z")
_REQUIRED = frozenset({
    "status", "mission", "issue", "agent_id", "commit_sha", "dispatch_id",
    "context_sha256", "execution_allowed", "authorization_granted",
    "external_agent_invoked", "write_performed", "replay_protection_persistent",
})


def _claim_ref(intent: dict) -> str:
    """Stable across changed client nonces and unchanged mission/agent/commit.

    This intentionally permits only one attempt per agent and pinned commit.
    Any new generation requires a separately reviewed versioned protocol.
    """
    if type(intent) is not dict or set(intent) != _REQUIRED:
        raise ContextRejected("invalid prepared intent shape")
    if (intent["status"] != "prepared_offline"
            or intent["mission"] != "GT-AI-DISPATCH-001"
            or type(intent["issue"]) is not int or intent["issue"] != 47
            or type(intent["agent_id"]) is not str
            or not _AGENT.fullmatch(intent["agent_id"])
            or type(intent["commit_sha"]) is not str
            or not _SHA40.fullmatch(intent["commit_sha"])
            or type(intent["dispatch_id"]) is not str
            or not _SHA64.fullmatch(intent["dispatch_id"])
            or type(intent["context_sha256"]) is not str
            or not _SHA64.fullmatch(intent["context_sha256"])
            or any(intent[key] is not False for key in (
                "execution_allowed", "authorization_granted",
                "external_agent_invoked", "write_performed",
                "replay_protection_persistent"))):
        raise ContextRejected("unsafe prepared dispatch provenance")
    canonical = json.dumps({
        "repo": _REPO, "mission": intent["mission"],
        "issue": intent["issue"], "agent_id": intent["agent_id"],
        "commit_sha": intent["commit_sha"],
    }, sort_keys=True, separators=(",", ":"))
    return "refs/tags/gt47-claims/" + hashlib.sha256(canonical.encode()).hexdigest()


def _matches_ref(reply: object, ref: str, sha: str) -> bool:
    return (type(reply) is dict and reply.get("ref") == ref
            and type(reply.get("object")) is dict
            and reply["object"].get("type") == "commit"
            and reply["object"].get("sha") == sha)


def reserve_dispatch_on_github(*, intent: dict, enabled: bool = False,
                               create_ref=None, get_ref=None) -> dict:
    """Reserve once with POST /git/refs; verify 422 via GET /git/ref/{ref}.

    `enabled` is a local safety switch, NOT an authorization signature.
    Caller must supply a separately authorized and minimum-privilege transport.
    No retries: transport failures leave the effect uncertain.

    Transport signatures: create_ref(ref, sha) -> (HTTP status, JSON dict)
                          get_ref(ref) -> (HTTP status, JSON dict)
    """
    ref = _claim_ref(intent)
    if enabled is not True:
        raise ContextRejected("remote reservation disabled")
    if not callable(create_ref) or not callable(get_ref):
        raise ContextRejected("authenticated GitHub transport required")
    try:
        status, payload = create_ref(ref, intent["commit_sha"])
    except Exception as exc:
        raise ContextRejected("remote claim outcome uncertain; reconcile before retry") from exc
    if type(status) is not int or type(payload) is not dict:
        raise ContextRejected("malformed claim response; outcome uncertain")
    if status == 201:
        if not _matches_ref(payload, ref, intent["commit_sha"]):
            raise ContextRejected("claim response not verifiable; reconcile")
        return {"status": "reserved_remote", "claim_ref": ref,
                "dispatch_id": intent["dispatch_id"], "execution_allowed": False,
                "agent_mission_executed": False, "github_write": True}
    if status == 422:
        try:
            read_status, read_payload = get_ref(ref)
        except Exception as exc:
            raise ContextRejected("claim conflict unverified; reconcile") from exc
        if (type(read_status) is int and read_status == 200
                and _matches_ref(read_payload, ref, intent["commit_sha"])):
            raise ContextRejected("duplicate mission attempt / replay rejected")
        raise ContextRejected("claim conflict not verified; fail closed")
    raise ContextRejected("remote claim failed or uncertain; no automatic retry")
