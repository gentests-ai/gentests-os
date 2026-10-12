"""T05: explicit, read-only authenticated integration readiness.

No token storage, agent execution, GitHub mutation, workflow dispatch or LLM.
"""
from __future__ import annotations
import hashlib
import json
from scripts.gt47_t04_context_loader import ContextRejected
from scripts.gt47_t04_github_adapter import fetch_context
from scripts.gt47_t04_transport import github_readonly_get


def authenticated_readiness(*, token: str, commit_sha: str, agent_id: str,
                            contract_path: str, get=None) -> dict:
    """Run a real read-only E2E only when explicitly called with a token.

    A caller-supplied GET permits fully offline tests. Do not log the token.
    """
    if type(token) is not str or not token.strip():
        raise ContextRejected("explicit authenticated token required")
    if type(commit_sha) is not str or len(commit_sha) != 40 or any(
        c not in "0123456789abcdef" for c in commit_sha
    ):
        raise ContextRejected("pinned commit required")
    if get is None:
        def get(url, params):
            return github_readonly_get(url, params, token=token)
    envelope = fetch_context(
        get, commit_sha=commit_sha, agent_id=agent_id,
        contract_path=contract_path,
    )
    digest = envelope.get("envelope_sha256")
    unsigned = {key: value for key, value in envelope.items() if key != "envelope_sha256"}
    expected = hashlib.sha256(json.dumps(
        unsigned, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")).hexdigest()
    if digest != expected or envelope.get("execution_allowed") is not False:
        raise ContextRejected("unsafe or corrupted context envelope")
    provenance = envelope.get("source_provenance")
    if type(provenance) is not dict or provenance.get("commit_sha") != commit_sha:
        raise ContextRejected("missing or mismatched source provenance")
    comments = provenance.get("comments")
    if type(comments) is not dict or comments.get("complete") is not True:
        raise ContextRejected("incomplete source provenance")
    if envelope.get("target", {}).get("agent_id") != agent_id:
        raise ContextRejected("agent identity mismatch")
    return {
        "status": "read_only_e2e_pass",
        "commit_sha": commit_sha,
        "agent_id": agent_id,
        "envelope_sha256": digest,
        "source_provenance": envelope["source_provenance"],
        "execution_allowed": False,
        "external_agent_invoked": False,
        "authorization_granted": False,
    }
