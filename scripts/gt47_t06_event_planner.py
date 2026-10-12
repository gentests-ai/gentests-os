"""No-cost deterministic handoff planner for GitHub issue events.

Produces a plan only. Never executes an agent, writes to GitHub, or infers
authorization from untrusted issue text.
"""
from __future__ import annotations
import json
import re
from scripts.gt47_t04_context_loader import ContextRejected

AGENTS = frozenset(("AGT-ENG", "AGT-QA", "AGT-INFRA", "AGT-PROC", "AGT-GOV"))
LABEL_PREFIX = "gt47-agent:"
MAX_EVENT_BYTES = 32768


def plan_issue_event(raw: bytes) -> dict:
    if type(raw) is not bytes or len(raw) > MAX_EVENT_BYTES:
        raise ContextRejected("invalid event size")
    try:
        event = json.loads(raw)
    except (ValueError, UnicodeError) as exc:
        raise ContextRejected("invalid event JSON") from exc
    if type(event) is not dict or event.get("action") not in ("labeled", "opened", "reopened"):
        raise ContextRejected("unsupported event action")
    repository = event.get("repository")
    issue = event.get("issue")
    if (type(repository) is not dict or repository.get("full_name") != "gentestsai-sudo/gentests-os"
            or type(issue) is not dict or issue.get("number") != 47
            or type(issue.get("labels")) is not list):
        raise ContextRejected("wrong mission or repository")
    # Only a newly applied routing label may initiate a plan. Opening/reopening
    # an issue with stale labels must not redispatch old work.
    if event["action"] != "labeled":
        raise ContextRejected("route requires a new label event")
    changed_label = event.get("label")
    if type(changed_label) is not dict or type(changed_label.get("name")) is not str:
        raise ContextRejected("missing changed routing label")
    labels = issue["labels"]
    names = []
    for label in labels:
        if type(label) is not dict or type(label.get("name")) is not str:
            raise ContextRejected("invalid label")
        names.append(label["name"])
    targets = [name[len(LABEL_PREFIX):] for name in names if name.startswith(LABEL_PREFIX)]
    if (len(targets) != 1 or targets[0] not in AGENTS
            or changed_label["name"] != LABEL_PREFIX + targets[0]):
        raise ContextRejected("exactly one allowed agent label required")
    return {
        "status": "planned_only", "mission": "GT-AI-DISPATCH-001",
        "issue": 47, "agent_id": targets[0],
        "execution_allowed": False, "external_agent_invoked": False,
        "github_write": False,
    }
