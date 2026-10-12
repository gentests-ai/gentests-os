"""Pure selection of already authenticated issue #47 comments.

Never interpret comment bodies as authorization to execute. Only validates
identity, order and provenance for the T04 evidence envelope.
"""
from scripts.gt47_t04_context_loader import ContextRejected

PREFIX = "https://github.com/gentestsai-sudo/gentests-os/issues/47#issuecomment-"


def select_issue_events(records: list[dict], limit: int = 50) -> list[dict]:
    if type(records) is not list or type(limit) is not int or not 1 <= limit <= 50:
        raise ContextRejected("invalid event collection")
    if len(records) > limit:
        raise ContextRejected("event limit exceeded; pagination required")
    selected = []
    seen = set()
    for record in records:
        if type(record) is not dict or set(record) != {"id", "body", "html_url"}:
            raise ContextRejected("unexpected comment record")
        eid = record["id"]
        if type(eid) is not int or eid <= 0 or eid in seen:
            raise ContextRejected("invalid or duplicate comment identity")
        if type(record["body"]) is not str or not record["body"].strip():
            raise ContextRejected("invalid comment body")
        if record["html_url"] != PREFIX + str(eid):
            raise ContextRejected("comment URL mismatch")
        seen.add(eid)
        selected.append({"id": str(eid), "body": record["body"], "url": record["html_url"]})
    return selected
