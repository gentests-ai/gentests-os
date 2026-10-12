"""Finite G3 pipeline OFFLINE: Actions -> Worker -> SQLite DO -> fake Workers AI.

No network, SDK, credentials, actual IAM, cloud, expenses or publication.
"""
from scripts.gt_cloudflare_mock import FakeWorkersAI
from scripts.gt_t05_security_mock import FakeAuthority, LocalGate, allowed


class FakeActionsRunner:
    """Read-only fictitious principal; authoritative decisions remain test fixtures."""

    def __init__(self, checkpoint_path, decisions):
        self.authority = FakeAuthority(decisions)
        self.controller = LocalGate(checkpoint_path, self.authority)
        self.inference = FakeWorkersAI()

    def execute(self, event, now, *, principal="future-actions-reader", operation="contents:read",
                failure=None, before_inference=None):
        if not allowed(principal, operation):
            return {"state": "blocked", "reason": "least_privilege", "retry": False}
        if type(event) is not dict:
            return {"state": "blocked", "reason": "invalid_event", "retry": False}
        reserved = self.controller.reserve(event, now)
        if reserved["state"] != "reserved":
            return {**reserved, "retry": False}
        # Hook is exclusively an offline harness for revocation/kill switch tests.
        if before_inference is not None:
            before_inference()
        # Revalidate authority/control *before* simulated inference; never call a model.
        # In this mock LocalGate.effect encapsulates that revalidation atomically.
        # A provider failure becomes uncertain; never do an automatic retry.
        if failure is not None:
            fake_error = self.inference.infer(event, failure=failure)
            result = self.controller.effect(event, reserved["fence"], now, failure=fake_error["error"])
            return {**result, "retry": False}
        # Do not produce even a fictitious result when revoked in the test hook.
        # effect() is the final gate before the no-network model adapter.
        result = self.controller.effect(event, reserved["fence"], now)
        if result["state"] != "done":
            return {**result, "retry": False}
        reply = self.inference.infer(event)
        return {"state": "done", "synthetic": True,
                "request_id": reply["request_id"], "output": reply["text"],
                "units_fictitious": reply["cost_fictitious_units"]}
