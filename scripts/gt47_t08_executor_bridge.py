"""GT47 T08: bounded authenticated bridge to an independently deployed executor.

No provider endpoint is configured here. A caller must explicitly enable it,
verify authorization OUTSIDE the issue/comments, reserve a durable claim, and
supply an authenticated transport. This module cannot turn chats into agents.
The remote worker must produce signed receipts; signatures authenticate
assertions, not independent proof of work performed.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import math
import re

from scripts.gt47_t04_context_loader import ContextRejected
from scripts.gt47_t06_github_claim_ledger import (
    _claim_ref, begin_executor_invocation_on_github,
)

_HASH = re.compile(r"[0-9a-f]{64}\Z")
_RECEIPT = re.compile(r"[a-zA-Z0-9_-]{16,64}\Z")
_SCHEMA = "gt47-executor-receipt-v1"
_RECEIPT_KEYS = frozenset((
    "schema", "status", "agent_id", "dispatch_id", "receipt_id",
    "result_sha256", "signature",
))
_WORKER_DECISION_FIELDS = frozenset((
    "version", "decision_id", "issuer_key_id", "issuer_human_id",
    "repository_id", "issue", "mission", "agent_id", "commit_sha",
    "contract_blob_sha", "input_sha256", "dispatch_id", "claim_ref",
    "scope", "not_before", "expires_at", "nonce", "max_tokens",
    "max_model_calls", "max_tool_calls", "allowed_tools",
    "max_incremental_cost_usd_micros", "no_paid_fallback",
))
_WORKER_TOOLS = frozenset((
    "read_file", "list_open_prs", "get_pull_request",
    "get_check_status", "write_file", "open_pull_request",
))
_WRITE_TOOLS = frozenset(("write_file", "open_pull_request"))
_SHA40 = re.compile(r"[0-9a-f]{40}\Z")
_WORKER_SIGNATURE = re.compile(r"[A-Za-z0-9_-]{86}\Z")



def _validate_worker_json(value, depth=0):
    if depth > 12:
        raise ContextRejected("Worker context nesting too deep")
    if value is None or type(value) in (str, bool):
        if type(value) is str and len(value.encode("utf-8")) > 20000:
            raise ContextRejected("Worker context string too large")
        return
    if type(value) is int:
        if not -(2**53 - 1) <= value <= 2**53 - 1:
            raise ContextRejected("Worker context integer outside safe range")
        return
    if type(value) is list:
        if len(value) > 500:
            raise ContextRejected("Worker context array too large")
        for item in value:
            _validate_worker_json(item, depth + 1)
        return
    if type(value) is dict:
        if len(value) > 200:
            raise ContextRejected("Worker context object too large")
        for key, item in value.items():
            if (type(key) is not str or not key.isascii()
                    or key in {"__proto__", "constructor", "prototype"}):
                raise ContextRejected("Worker context key is not canonical")
            _validate_worker_json(item, depth + 1)
        return
    raise ContextRejected("Worker context contains unsupported JSON values")


def _validate_worker_request(worker_request, intent, expected_ref):
    if (type(worker_request) is not dict
            or set(worker_request) != {"decision", "signature", "task", "context"}):
        raise ContextRejected("invalid signed Worker request")
    decision, task, context = (worker_request["decision"], worker_request["task"],
                               worker_request["context"])
    if (type(decision) is not dict or set(decision) != _WORKER_DECISION_FIELDS
            or type(task) is not str or not task.strip() or len(task.encode("utf-8")) > 8192
            or type(context) is not dict):
        raise ContextRejected("invalid signed Worker decision schema")
    _validate_worker_json(context)
    tools = decision["allowed_tools"]
    if (decision["version"] != 3 or type(tools) is not list or not tools
            or len(tools) > len(_WORKER_TOOLS)
            or any(type(tool) is not str or tool not in _WORKER_TOOLS for tool in tools)
            or len(set(tools)) != len(tools) or tools != sorted(tools)):
        raise ContextRejected("invalid signed Worker tool allowlist")
    write_pair = _WRITE_TOOLS.issubset(tools)
    if bool(_WRITE_TOOLS.intersection(tools)) != write_pair:
        raise ContextRejected("write_file and open_pull_request must be authorized together")
    model_calls, tool_calls = decision["max_model_calls"], decision["max_tool_calls"]
    max_tokens, budget = decision["max_tokens"], decision["max_incremental_cost_usd_micros"]
    if (type(model_calls) is not int or not 2 <= model_calls <= 4
            or type(tool_calls) is not int or not 1 <= tool_calls <= 3
            or tool_calls > model_calls - 1 or (write_pair and tool_calls < 2)
            or type(max_tokens) is not int or not 1 <= max_tokens <= 4096
            or type(budget) is not int or budget < 1):
        raise ContextRejected("invalid signed Worker execution limits")
    minimum = model_calls * math.ceil(120000 * 0.0605 + max_tokens * 0.4)
    if budget < minimum:
        raise ContextRejected("signed Worker budget below worst-case estimate")
    if (decision["repository_id"] != 1412714626 or decision["issue"] != 47
            or decision["mission"] != intent["mission"]
            or decision["agent_id"] != intent["agent_id"]
            or decision["commit_sha"] != intent["commit_sha"]
            or not _SHA40.fullmatch(decision["contract_blob_sha"])
            or not _HASH.fullmatch(decision["input_sha256"])
            or decision["dispatch_id"] != intent["dispatch_id"]
            or decision["claim_ref"] != expected_ref
            or decision["scope"] != "gt47:execute:AGT-ENG"
            or not _RECEIPT.fullmatch(decision["decision_id"])
            or not _RECEIPT.fullmatch(decision["nonce"])
            or type(decision["issuer_key_id"]) is not str or not decision["issuer_key_id"] or len(decision["issuer_key_id"]) > 128
            or type(decision["issuer_human_id"]) is not str or not decision["issuer_human_id"] or len(decision["issuer_human_id"]) > 256
            or type(decision["not_before"]) is not int or not 0 <= decision["not_before"] <= 2**53 - 1
            or type(decision["expires_at"]) is not int or not 1 <= decision["expires_at"] <= 2**53 - 1
            or decision["expires_at"] <= decision["not_before"]
            or decision["expires_at"] - decision["not_before"] > 900
            or decision["no_paid_fallback"] is not True):
        raise ContextRejected("signed Worker request does not match reserved intent")
    expected_input = hashlib.sha256(
        _canonical({"task": task, "context": context})).hexdigest()
    if decision["input_sha256"] != expected_input:
        raise ContextRejected("signed Worker input digest mismatch")
    signature = worker_request["signature"]
    if type(signature) is not str or not _WORKER_SIGNATURE.fullmatch(signature):
        raise ContextRejected("invalid Worker signature encoding")
    encoded_size = len(json.dumps(
        worker_request, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
    if encoded_size > 30000:
        raise ContextRejected("signed Worker request exceeds safe transport size")
    return worker_request


def _canonical(value: dict) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":")).encode("utf-8")


def _validate_ed25519_receipt(*, value: dict, key: bytes, intent: dict,
                                receipt_id: str | None, allowed_states: tuple,
                                nested: bool = False) -> dict:
    from base64 import urlsafe_b64decode
    from cryptography.exceptions import InvalidSignature
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

    if type(value) is not dict:
        raise ContextRejected("invalid Ed25519 receipt schema")
    base = {"schema", "status", "mission", "issue", "agent_id", "commit_sha",
            "dispatch_id", "receipt_id", "result_sha256", "updated_at",
            "executor", "signature"}
    expected = base | ({"accepted_receipt"} if "accepted_receipt" in value else set())
    if set(value) != expected:
        raise ContextRejected("invalid Ed25519 receipt schema")
    if (value["schema"] != "gt47-executor-receipt-v2"
            or value["status"] not in allowed_states
            or value["mission"] != intent["mission"]
            or value["issue"] != intent["issue"]
            or value["agent_id"] != intent["agent_id"]
            or value["commit_sha"] != intent["commit_sha"]
            or value["dispatch_id"] != intent["dispatch_id"]):
        raise ContextRejected("Ed25519 receipt binding mismatch")
    if (type(value["updated_at"]) is not str or not value["updated_at"]
            or value["executor"] != "gt47-cloudflare-worker-v1"):
        raise ContextRejected("invalid Ed25519 receipt metadata")
    rid = value["receipt_id"]
    if type(rid) is not str or not _RECEIPT.fullmatch(rid):
        raise ContextRejected("invalid Ed25519 receipt identifier")
    if receipt_id is not None and rid != receipt_id:
        raise ContextRejected("Ed25519 receipt identifier changed")
    result = value["result_sha256"]
    if value["status"] == "completed":
        if type(result) is not str or not _HASH.fullmatch(result):
            raise ContextRejected("missing completed result digest")
    elif result is not None:
        raise ContextRejected("premature result digest")
    signature = value["signature"]
    if type(signature) is not str or not re.fullmatch(r"[A-Za-z0-9_-]{86}", signature):
        raise ContextRejected("invalid Ed25519 signature encoding")
    try:
        sig = urlsafe_b64decode(signature + "=" * (-len(signature) % 4))
        unsigned = {k: v for k, v in value.items() if k != "signature"}
        Ed25519PublicKey.from_public_bytes(key).verify(
            sig, b"GT47-RECEIPT-v1\x00" + _canonical(unsigned))
    except (ValueError, InvalidSignature) as exc:
        raise ContextRejected("Ed25519 receipt authentication failed") from exc
    accepted_attested = False
    if "accepted_receipt" in value:
        if nested or value["status"] not in ("completed", "failed", "uncertain"):
            raise ContextRejected("unexpected nested acceptance receipt")
        accepted = _validate_ed25519_receipt(
            value=value["accepted_receipt"], key=key, intent=intent,
            receipt_id=rid, allowed_states=("accepted",), nested=True)
        accepted_attested = accepted["status"] == "accepted"
    if value["status"] == "completed" and not accepted_attested:
        raise ContextRejected("completed receipt lacks signed acceptance history")
    return {"status": value["status"], "receipt_id": rid,
            "result_sha256": result, "accepted_attested": accepted_attested}


def validate_attestation(*, value: dict, key: bytes, intent: dict,
                         receipt_id: str | None, allowed_states: tuple) -> dict:
    if type(value) is dict and value.get("schema") == "gt47-executor-receipt-v2":
        if type(key) is not bytes or len(key) != 32:
            raise ContextRejected("Ed25519 public key must be 32 raw bytes")
        return _validate_ed25519_receipt(
            value=value, key=key, intent=intent, receipt_id=receipt_id,
            allowed_states=allowed_states)
    if type(value) is not dict or set(value) != _RECEIPT_KEYS:
        raise ContextRejected("invalid remote receipt schema")
    if type(key) is not bytes or len(key) < 32:
        raise ContextRejected("receipt verification key missing or too weak")
    if value["schema"] != _SCHEMA or value["status"] not in allowed_states:
        raise ContextRejected("invalid remote receipt status")
    if (value["agent_id"] != intent["agent_id"]
            or value["dispatch_id"] != intent["dispatch_id"]):
        raise ContextRejected("remote receipt bound to wrong mission")
    rid = value["receipt_id"]
    if type(rid) is not str or not _RECEIPT.fullmatch(rid):
        raise ContextRejected("invalid remote receipt identifier")
    if receipt_id is not None and rid != receipt_id:
        raise ContextRejected("remote receipt identifier changed")
    result = value["result_sha256"]
    if value["status"] == "completed":
        if type(result) is not str or not _HASH.fullmatch(result):
            raise ContextRejected("missing completed result digest")
    elif result is not None:
        raise ContextRejected("premature result digest")
    signature = value["signature"]
    if type(signature) is not str or not _HASH.fullmatch(signature):
        raise ContextRejected("invalid remote receipt signature format")
    unsigned = {k: v for k, v in value.items() if k != "signature"}
    expected = hmac.new(key, _canonical(unsigned), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, signature):
        raise ContextRejected("remote receipt authentication failed")
    # Never return free-text from the remote worker or issue comments.
    return {"status": value["status"], "receipt_id": rid,
            "result_sha256": result}


def execute_reserved_intent(*, intent: dict, reservation: dict,
                            receipt_key: bytes, verify_authorization=None,
                            create_ref=None, get_ref=None,
                            submit=None, lookup=None, worker_request: dict | None = None,
                            enabled: bool = False, max_polls: int = 2) -> dict:
    """Transmit a reserved intent once, then collect signed states.

    submit(payload) -> (202, signed_received_receipt)
    lookup(receipt_id) -> (200, signed_accepted_or_completed_receipt)
    GitHub ref callbacks atomically consume a durable one-shot fence before
    submit. Reusing the same reservation object cannot cause a second POST.
    On uncertainty no resubmission or automatic replay is permitted.
    """
    expected_ref = _claim_ref(intent)
    if (enabled is not True or not callable(verify_authorization)
            or not callable(create_ref) or not callable(get_ref)
            or not callable(submit) or not callable(lookup)):
        raise ContextRejected("external dispatch disabled or unconfigured")
    if (type(reservation) is not dict
            or reservation.get("status") != "reserved_remote"
            or reservation.get("claim_ref") != expected_ref
            or reservation.get("dispatch_id") != intent["dispatch_id"]
            or reservation.get("github_write") is not True
            or reservation.get("execution_allowed") is not False
            or reservation.get("agent_mission_executed") is not False):
        raise ContextRejected("missing matching durable claim")
    if type(max_polls) is not int or not 1 <= max_polls <= 5:
        raise ContextRejected("poll bound required")
    if type(receipt_key) is not bytes or len(receipt_key) < 32:
        raise ContextRejected("receipt verifier not configured")
    try:
        permitted = verify_authorization(intent)
    except Exception as exc:
        raise ContextRejected("out-of-band authorization verification failed") from exc
    if permitted is not True:
        raise ContextRejected("no verified out-of-band authorization")
    if worker_request is None:
        payload = {
            "schema": "gt47-executor-request-v1",
            "mission": intent["mission"], "issue": intent["issue"],
            "agent_id": intent["agent_id"],
            "commit_sha": intent["commit_sha"],
            "context_sha256": intent["context_sha256"],
            "dispatch_id": intent["dispatch_id"],
            "claim_ref": expected_ref,
            # No executable command, issue body, credentials, policy, or tool output.
        }
    else:
        payload = _validate_worker_request(worker_request, intent, expected_ref)
    # Validate the complete request before consuming the one-shot side-effect fence.
    fence = begin_executor_invocation_on_github(
        intent=intent, reservation=reservation, enabled=True,
        create_ref=create_ref, get_ref=get_ref,
    )
    execution_ref = fence["execution_ref"]
    try:
        code, initial = submit(payload)
    except Exception as exc:
        raise ContextRejected("executor submission outcome uncertain; reconcile") from exc
    if type(code) is not int or code != 202:
        raise ContextRejected("executor did not acknowledge submission; reconcile")
    received = validate_attestation(value=initial, key=receipt_key,
                                    intent=intent, receipt_id=None,
                                    allowed_states=("received",))
    rid = received["receipt_id"]
    accepted = False
    for _ in range(max_polls):
        try:
            code, response = lookup(rid)
        except Exception as exc:
            raise ContextRejected("remote receipt lookup uncertain; reconcile") from exc
        if type(code) is not int or code != 200:
            raise ContextRejected("remote receipt lookup failed; reconcile")
        result_text = None
        metadata_info = {}
        receipt_value = response
        if type(response) is dict and "receipt" in response:
            receipt_value = response["receipt"]
            result_text = response.get("result")
            branch_name = response.get("branch_name")
            pr_number = response.get("pr_number")
            if branch_name is not None:
                if type(branch_name) is not str or not re.fullmatch(r"agents/gt47/[0-9a-f]{64}", branch_name):
                    raise ContextRejected("invalid remote branch metadata")
                metadata_info["branch_name"] = branch_name
            if pr_number is not None:
                if type(pr_number) is not int or pr_number < 1:
                    raise ContextRejected("invalid remote PR metadata")
                metadata_info["pr_number"] = pr_number
        value = validate_attestation(
            value=receipt_value, key=receipt_key, intent=intent,
            receipt_id=rid,
            allowed_states=("received", "accepted", "completed", "failed", "uncertain"),
        )
        state = value["status"]
        if state == "failed":
            raise ContextRejected("remote executor reported failed")
        if state == "uncertain":
            raise ContextRejected("remote execution uncertain; manual reconciliation required")
        if state == "accepted":
            accepted = True
        elif state == "completed":
            if value.get("accepted_attested") is True:
                accepted = True
            if not accepted:
                raise ContextRejected("executor completed without verified acceptance")
            result_info = {}
            if receipt_value.get("schema") == "gt47-executor-receipt-v2":
                if (type(result_text) is not str or not result_text
                        or hashlib.sha256(result_text.encode("utf-8")).hexdigest()
                        != value["result_sha256"]):
                    raise ContextRejected("remote result missing or digest mismatch")
                result_info["result"] = result_text
            return {"status": "remote_completed_attested",
                    "dispatch_id": intent["dispatch_id"],
                    "receipt_id": rid,
                    "execution_ref": execution_ref,
                    "result_sha256": value["result_sha256"],
                    **result_info,
                    **metadata_info,
                    "agent_id": intent["agent_id"],
                    "agent_mission_executed": "attested_by_remote_only",
                    "independently_verified": False}
    return {"status": "remote_pending_attested", "dispatch_id": intent["dispatch_id"],
            "receipt_id": rid, "execution_ref": execution_ref,
            "agent_id": intent["agent_id"],
            "agent_mission_executed": False, "independently_verified": False}


def reconcile_executor_receipt(*, intent: dict, receipt_id: str,
                               receipt_key: bytes, lookup) -> dict:
    """Read-only reconciliation; never submits or retries an uncertain dispatch."""
    if not callable(lookup):
        raise ContextRejected("remote receipt lookup is not configured")
    if type(receipt_key) is not bytes or len(receipt_key) < 32:
        raise ContextRejected("receipt verifier not configured")
    try:
        code, response = lookup(receipt_id)
    except Exception as exc:
        raise ContextRejected("receipt reconciliation outcome uncertain") from exc
    if type(code) is not int or code != 200 or type(response) is not dict:
        raise ContextRejected("remote receipt unavailable; manual reconciliation required")
    receipt_value = response.get("receipt", response)
    result_text = response.get("result") if "receipt" in response else None
    metadata_info = {}
    if "receipt" in response:
        branch_name, pr_number = response.get("branch_name"), response.get("pr_number")
        if branch_name is not None:
            if type(branch_name) is not str or not re.fullmatch(r"agents/gt47/[0-9a-f]{16}", branch_name):
                raise ContextRejected("invalid remote branch metadata")
            metadata_info["branch_name"] = branch_name
        if pr_number is not None:
            if type(pr_number) is not int or pr_number < 1:
                raise ContextRejected("invalid remote PR metadata")
            metadata_info["pr_number"] = pr_number
    value = validate_attestation(
        value=receipt_value, key=receipt_key, intent=intent,
        receipt_id=receipt_id,
        allowed_states=("received", "accepted", "completed", "failed", "uncertain"),
    )
    state = value["status"]
    if state == "failed":
        raise ContextRejected("remote executor reported failed")
    if state == "uncertain":
        return {"status": "manual_reconciliation_required",
                "dispatch_id": intent["dispatch_id"], "receipt_id": receipt_id,
                "agent_mission_executed": "uncertain",
                "independently_verified": False}
    if state != "completed":
        return {"status": "remote_pending_attested",
                "dispatch_id": intent["dispatch_id"], "receipt_id": receipt_id,
                "agent_mission_executed": False, "independently_verified": False}
    result_info = {}
    if receipt_value.get("schema") == "gt47-executor-receipt-v2":
        if (type(result_text) is not str or not result_text
                or hashlib.sha256(result_text.encode("utf-8")).hexdigest()
                != value["result_sha256"]):
            raise ContextRejected("remote result missing or digest mismatch")
        result_info["result"] = result_text
    return {"status": "remote_completed_attested",
            "dispatch_id": intent["dispatch_id"], "receipt_id": receipt_id,
            "result_sha256": value["result_sha256"], **result_info, **metadata_info,
            "agent_id": intent["agent_id"],
            "agent_mission_executed": "attested_by_remote_only",
            "independently_verified": False}


def reconcile_executor_dispatch(*, intent: dict, receipt_key: bytes, status) -> dict:
    """Reconcile by stable dispatch ID when the original POST response was lost."""
    if not callable(status):
        raise ContextRejected("remote status lookup is not configured")
    try:
        code, response = status(intent["dispatch_id"])
    except Exception as exc:
        raise ContextRejected("dispatch status outcome uncertain") from exc
    if (type(code) is not int or code != 200 or type(response) is not dict
            or type(response.get("receipt")) is not dict):
        raise ContextRejected("dispatch status unavailable; manual reconciliation required")
    receipt_id = response["receipt"].get("receipt_id")
    if type(receipt_id) is not str or not _RECEIPT.fullmatch(receipt_id):
        raise ContextRejected("dispatch status has no valid receipt identifier")
    return reconcile_executor_receipt(
        intent=intent, receipt_id=receipt_id, receipt_key=receipt_key,
        lookup=lambda _receipt_id: (code, response))
