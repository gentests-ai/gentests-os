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


def _canonical(value: dict) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":")).encode("utf-8")


def _validate_ed25519_receipt(*, value: dict, key: bytes, intent: dict,
                                receipt_id: str | None, allowed_states: tuple,
                                nested: bool = False) -> dict:
    from base64 import urlsafe_b64decode
    from cryptography.exceptions import InvalidSignature
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

    base = {"schema", "status", "mission", "issue", "agent_id", "commit_sha",
            "dispatch_id", "receipt_id", "result_sha256", "updated_at",
            "executor", "signature"}
    expected = base | ({"accepted_receipt"} if "accepted_receipt" in value else set())
    if type(value) is not dict or set(value) != expected:
        raise ContextRejected("invalid Ed25519 receipt schema")
    if (value["schema"] != "gt47-executor-receipt-v2"
            or value["status"] not in allowed_states
            or value["mission"] != intent["mission"]
            or value["issue"] != intent["issue"]
            or value["agent_id"] != intent["agent_id"]
            or value["commit_sha"] != intent["commit_sha"]
            or value["dispatch_id"] != intent["dispatch_id"]):
        raise ContextRejected("Ed25519 receipt binding mismatch")
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
        if nested or value["status"] not in ("completed", "failed"):
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
                            submit=None, lookup=None,
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
    fence = begin_executor_invocation_on_github(
        intent=intent, reservation=reservation, enabled=True,
        create_ref=create_ref, get_ref=get_ref,
    )
    execution_ref = fence["execution_ref"]
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
        value = validate_attestation(
            value=response, key=receipt_key, intent=intent,
            receipt_id=rid,
            allowed_states=("received", "accepted", "completed", "failed"),
        )
        state = value["status"]
        if state == "failed":
            raise ContextRejected("remote executor reported failed")
        if state == "accepted":
            accepted = True
        elif state == "completed":
            if value.get("accepted_attested") is True:
                accepted = True
            if not accepted:
                raise ContextRejected("executor completed without verified acceptance")
            return {"status": "remote_completed_attested",
                    "dispatch_id": intent["dispatch_id"],
                    "receipt_id": rid,
                    "execution_ref": execution_ref,
                    "result_sha256": value["result_sha256"],
                    "agent_id": intent["agent_id"],
                    "agent_mission_executed": "attested_by_remote_only",
                    "independently_verified": False}
    return {"status": "remote_pending_attested", "dispatch_id": intent["dispatch_id"],
            "receipt_id": rid, "execution_ref": execution_ref,
            "agent_id": intent["agent_id"],
            "agent_mission_executed": False, "independently_verified": False}
