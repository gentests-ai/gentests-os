"""Offline one-dispatch signer for the GT47 Cloudflare Worker.

Never generates or persists keys. The private key must already exist and remain
under the authority owner's offline custody. Output is a signed request envelope,
not an execution command or proof that an executor ran.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import math
import os
import re
import sys
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

DOMAIN = b"GT47-DECISION-v1\x00"
MISSION = "GT-AI-DISPATCH-001"
REPO_ID = 1412714626
ISSUE = 47
AGENT = "AGT-ENG"
CLAIM_REPO = "gentestsai-sudo/gentests-os"  # immutable T06 pre-transfer hash namespace
SHA40 = re.compile(r"[0-9a-f]{40}\Z")
ID = re.compile(r"[A-Za-z0-9_-]{16,64}\Z")
TOOL_NAMES = ("get_check_status", "get_pull_request", "list_open_prs", "open_pull_request", "read_file", "write_file")
WRITE_TOOLS = {"open_pull_request", "write_file"}
MAX_PROMPT_BYTES = 120000
INPUT_MICROUSD_PER_TOKEN = 0.0605
OUTPUT_MICROUSD_PER_TOKEN = 0.4


def canonical(value: object, depth: int = 0) -> bytes:
    if depth > 12:
        raise ValueError("JSON nesting too deep")
    if value is None or type(value) in (str, bool):
        if type(value) is str and len(value.encode("utf-8")) > 20000:
            raise ValueError("JSON string too large")
        return json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    if type(value) is int:
        if not -(2**53 - 1) <= value <= 2**53 - 1:
            raise ValueError("integer outside interoperable range")
        return str(value).encode("ascii")
    if type(value) is list:
        if len(value) > 500:
            raise ValueError("array too large")
        return b"[" + b",".join(canonical(item, depth + 1) for item in value) + b"]"
    if type(value) is dict:
        if len(value) > 200 or any(
            type(k) is not str or not k.isascii()
            or k in {"__proto__", "constructor", "prototype"}
            for k in value
        ):
            raise ValueError("invalid JSON object")
        parts = []
        for key in sorted(value):
            parts.append(json.dumps(key, ensure_ascii=False).encode("utf-8")
                         + b":" + canonical(value[key], depth + 1))
        return b"{" + b",".join(parts) + b"}"
    raise ValueError("unsupported JSON value")


def sign_request(*, task: str, context: dict, commit_sha: str,
                 contract_blob_sha: str, nonce: str, decision_id: str,
                 issuer_key_id: str, issuer_human_id: str,
                 private_key_pem: bytes, max_tokens: int = 1024,
                 max_incremental_cost_usd_micros: int | None = None,
                 allowed_tools: list | None = None,
                 max_model_calls: int = 2, max_tool_calls: int = 1,
                 now: int | None = None) -> dict:
    import time

    if type(task) is not str or not task.strip() or len(task.encode("utf-8")) > 8192:
        raise ValueError("invalid task")
    if type(context) is not dict:
        raise ValueError("context must be an object")
    if not SHA40.fullmatch(commit_sha) or not SHA40.fullmatch(contract_blob_sha):
        raise ValueError("invalid pinned commit or contract blob SHA")
    if not ID.fullmatch(nonce) or not ID.fullmatch(decision_id):
        raise ValueError("invalid nonce or decision ID")
    if (type(issuer_key_id) is not str or not issuer_key_id
            or type(issuer_human_id) is not str or not issuer_human_id):
        raise ValueError("issuer identity and key ID are required")
    if type(max_tokens) is not int or not 1 <= max_tokens <= 1024:
        raise ValueError("max_tokens outside approved bound")
    if (type(max_incremental_cost_usd_micros) is not int
            or max_incremental_cost_usd_micros < 1):
        raise ValueError("an explicit positive USD-micros budget is required")
    if (type(allowed_tools) is not list or not allowed_tools or len(allowed_tools) > len(TOOL_NAMES)
            or any(type(name) is not str or name not in TOOL_NAMES for name in allowed_tools)
            or len(set(allowed_tools)) != len(allowed_tools)):
        raise ValueError("invalid allowed tool list")
    allowed_tools = sorted(allowed_tools)
    write_pair = {"write_file", "open_pull_request"}
    has_write_pair = write_pair.issubset(allowed_tools)
    if (bool(write_pair.intersection(allowed_tools)) != has_write_pair):
        raise ValueError("write_file and open_pull_request must be authorized together")
    if (type(max_model_calls) is not int or not 1 <= max_model_calls <= 6
            or type(max_tool_calls) is not int or not 0 <= max_tool_calls <= 5
            or max_tool_calls > max_model_calls - 1
            or max_model_calls < 2 or max_tool_calls < 1
            or (has_write_pair and max_tool_calls < 2)):
        raise ValueError("invalid bounded agent/tool call limits")
    per_call_budget = int(math.ceil(
        MAX_PROMPT_BYTES * INPUT_MICROUSD_PER_TOKEN
        + max_tokens * OUTPUT_MICROUSD_PER_TOKEN))
    required_budget = max_model_calls * per_call_budget
    if max_incremental_cost_usd_micros < required_budget:
        raise ValueError("budget below the signed worst-case inference bound")

    current = int(time.time()) if now is None else now
    if type(current) is not int:
        raise ValueError("invalid signing time")
    input_sha = hashlib.sha256(canonical({"task": task, "context": context})).hexdigest()
    dispatch_id = hashlib.sha256(canonical({
        "mission": MISSION, "issue": ISSUE, "agent_id": AGENT,
        "commit_sha": commit_sha, "nonce": nonce,
    })).hexdigest()
    claim_ref = "refs/tags/gt47-claims/" + hashlib.sha256(canonical({
        "repo": CLAIM_REPO, "mission": MISSION, "issue": ISSUE,
        "agent_id": AGENT, "commit_sha": commit_sha,
    })).hexdigest()
    decision = {
        "version": 3, "decision_id": decision_id,
        "issuer_key_id": issuer_key_id, "issuer_human_id": issuer_human_id,
        "repository_id": REPO_ID, "issue": ISSUE, "mission": MISSION,
        "agent_id": AGENT, "commit_sha": commit_sha,
        "contract_blob_sha": contract_blob_sha, "input_sha256": input_sha,
        "dispatch_id": dispatch_id, "claim_ref": claim_ref,
        "scope": "gt47:execute:AGT-ENG", "not_before": current,
        "expires_at": current + 600, "nonce": nonce,
        "max_tokens": max_tokens, "max_model_calls": max_model_calls,
        "max_tool_calls": max_tool_calls, "allowed_tools": allowed_tools,
        "max_incremental_cost_usd_micros": max_incremental_cost_usd_micros,
        "no_paid_fallback": True,
    }
    key = serialization.load_pem_private_key(private_key_pem, password=None)
    if not isinstance(key, Ed25519PrivateKey):
        raise ValueError("existing Ed25519 private key required")
    signature = base64.urlsafe_b64encode(
        key.sign(DOMAIN + canonical(decision))
    ).decode("ascii").rstrip("=")
    return {"decision": decision, "signature": signature,
            "task": task, "context": context}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="JSON file with task/context and pinned IDs")
    parser.add_argument("--private-key", required=True, help="path to an existing offline Ed25519 PEM key")
    parser.add_argument("--output", required=True, help="new output file; never overwrite")
    args = parser.parse_args()
    try:
        source = json.loads(Path(args.input).read_text(encoding="utf-8"))
        key = Path(args.private_key).read_bytes()
        envelope = sign_request(
            task=source["task"], context=source["context"],
            commit_sha=source["commit_sha"],
            contract_blob_sha=source["contract_blob_sha"],
            nonce=source["nonce"], decision_id=source["decision_id"],
            issuer_key_id=source["issuer_key_id"],
            issuer_human_id=source["issuer_human_id"],
            private_key_pem=key, max_tokens=source.get("max_tokens", 1024),
            max_incremental_cost_usd_micros=source["max_incremental_cost_usd_micros"],
            allowed_tools=source["allowed_tools"],
            max_model_calls=source.get("max_model_calls", 2),
            max_tool_calls=source.get("max_tool_calls", 1),
        )
        target = Path(args.output)
        fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(envelope, handle, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"))
            handle.write("\n")
        print("Signed one-dispatch request written; private key was not copied or persisted.")
        return 0
    except FileExistsError:
        print("Output already exists; refusing to overwrite.", file=sys.stderr)
        return 2
    except Exception as exc:
        # Never print exception details that could contain paths or input data.
        print("Signing failed; inspect local inputs and key custody.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
