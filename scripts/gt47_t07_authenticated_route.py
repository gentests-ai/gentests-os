"""GT47 T07: authenticated GitHub event -> verified T04 context -> inert T06 intent.

This is an executable read-only vertical path, not an agent dispatcher.
No writes, cloud executor calls, ChatGPT invocation or authorization inference.
"""
from __future__ import annotations
import re

from scripts.gt47_t04_context_loader import ContextRejected
from scripts.gt47_t04_github_adapter import fetch_context
from scripts.gt47_t04_transport import github_readonly_get
from scripts.gt47_t06_event_planner import plan_issue_event
from scripts.gt47_t06_dispatch_intent import prepare_dispatch

CONTRACTS = {
    "AGT-ENG": "02-Agentes/Engenharia/Contrato-Agente-Executor-Tecnico.md",
    "AGT-QA": "02-Agentes/QA/Contrato-Agente-QA.md",
    "AGT-INFRA": "02-Agentes/Infraestrutura/Contrato-Agente-Infraestrutura.md",
    "AGT-PROC": "02-Agentes/Processos/Contrato-Agente-Processos.md",
    "AGT-GOV": "02-Agentes/Governanca/Contrato-Agente-Governanca.md",
}


def prepare_authenticated_route(*, raw_event: bytes, token: str,
                                commit_sha: str, nonce: str, get=None) -> dict:
    """Prepare a dispatch intent from an actual GitHub issue event and pinned sources.

    get(url, params) is an optional injected read-only transport for tests.
    token must be explicitly supplied; without get, the allowlisted T05
    authenticated HTTP transport is used. Never return/log comments or token.
    """
    route = plan_issue_event(raw_event)
    if type(token) is not str or not token.strip():
        raise ContextRejected("authenticated GitHub read token required")
    if type(commit_sha) is not str or re.fullmatch(r"[0-9a-f]{40}", commit_sha) is None:
        raise ContextRejected("pinned commit required")
    if type(nonce) is not str or re.fullmatch(r"[a-zA-Z0-9_-]{16,64}", nonce) is None:
        raise ContextRejected("invalid idempotency nonce")
    path = CONTRACTS.get(route["agent_id"])
    if path is None:
        raise ContextRejected("unmapped agent contract")
    if get is None:
        def get(url, params):
            return github_readonly_get(url, params, token=token)
    context = fetch_context(get, commit_sha=commit_sha,
                            agent_id=route["agent_id"], contract_path=path)
    intent = prepare_dispatch(
        context=context,
        request={"mission": route["mission"], "issue": route["issue"],
                 "agent_id": route["agent_id"], "commit_sha": commit_sha,
                 "nonce": nonce},
    )
    return {
        "status": "verified_prepared_only",
        "agent_id": route["agent_id"],
        "contract_path": path,
        "commit_sha": commit_sha,
        "dispatch_id": intent["dispatch_id"],
        "context_sha256": intent["context_sha256"],
        "intent": intent,
        "execution_allowed": False,
        "external_agent_invoked": False,
        "github_write": False,
    }
