"""Finite G3 pipeline OFFLINE: Actions -> fake Worker/DO -> fake Workers AI.

No network, SDK, credentials, IAM, cloud, expenses, publication or real inferencing.
"""
import hashlib
import sqlite3

from scripts.gt_cloudflare_mock import FakeWorkersAI
from scripts.gt_t05_security_mock import FakeAuthority, LocalGate, allowed, fingerprint


class FakeActionsRunner:
    """Only simulated identity and authority: never trust this as real IAM."""

    def __init__(self, checkpoint_path, decisions):
        self.authority = FakeAuthority(decisions)
        self.controller = LocalGate(checkpoint_path, self.authority)
        self.inference = FakeWorkersAI()

    def _transition(self, event, fence, now, *, final=False, reply=None):
        """Locally serialized, fail-closed guard for intent and completion."""
        with self.controller.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            k = fingerprint(event)
            row = db.execute(
                "SELECT state,fence,auth_ref FROM jobs WHERE k=?", (k,)
            ).fetchone()
            expected = "intent" if final else "reserved"
            if type(fence) is not int or row != (expected, fence, event.get("auth_ref")):
                return {"state": "blocked", "reason": "stale_fence_or_state", "retry": False}
            control = db.execute("SELECT killed,used,cap FROM control WHERE id=1").fetchone()
            reason = self.authority.verify(event, now)
            if (not control or any(type(v) is not int for v in control)
                    or control[0] != 0 or control[1] < 0 or control[2] < 0
                    or control[1] > control[2]):
                reason = "control_denied"
            if reason:
                db.execute("UPDATE jobs SET state='uncertain' WHERE k=? AND state=?", (k, expected))
                return {"state": "blocked", "reason": reason, "retry": False}
            if not final:
                db.execute("UPDATE jobs SET state='intent' WHERE k=? AND state='reserved'", (k,))
                return {"state": "intent", "key": k, "fence": fence}

            # Never persist done until a fully validated synthetic reply exists.
            if not _valid_reply(reply):
                db.execute("UPDATE jobs SET state='uncertain' WHERE k=? AND state='intent'", (k,))
                return {"state": "blocked", "reason": "invalid_synthetic_reply", "retry": False}
            digest = hashlib.sha256(reply["text"].encode("utf-8")).hexdigest()
            db.execute("""CREATE TABLE IF NOT EXISTS g3_evidence (
                k TEXT PRIMARY KEY, request_id TEXT NOT NULL,
                output_hash TEXT NOT NULL, units INTEGER NOT NULL)""")
            db.execute("INSERT INTO g3_evidence VALUES(?,?,?,?)",
                       (k, reply["request_id"], digest, reply["cost_fictitious_units"]))
            db.execute("UPDATE jobs SET state='done' WHERE k=? AND state='intent' AND fence=?",
                       (k, fence))
            return {"state": "done", "synthetic": True,
                    "request_id": reply["request_id"], "output": reply["text"],
                    "units_fictitious": reply["cost_fictitious_units"]}

    def _uncertain(self, event, fence):
        """Persist ambiguity on failures after intent, without unsafe replay."""
        with self.controller.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            db.execute("UPDATE jobs SET state='uncertain' WHERE k=? AND state='intent' AND fence=?",
                       (fingerprint(event), fence))

    def reconcile(self, event):
        """Read-only local evidence inspection. Never resets uncertain or retries."""
        if type(event) is not dict:
            return {"state": "blocked", "reason": "invalid_event", "retry": False}
        try:
            with self.controller.connect() as db:
                k = fingerprint(event)
                row = db.execute("SELECT state,fence FROM jobs WHERE k=?", (k,)).fetchone()
                evidence = db.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name='g3_evidence'"
                ).fetchone()
                proof = (db.execute(
                    "SELECT request_id,output_hash,units FROM g3_evidence WHERE k=?", (k,)
                ).fetchone() if evidence else None)
            return {"state": row[0] if row else "missing", "fence": row[1] if row else None,
                    "evidence": proof, "retry": False}
        except (KeyError, TypeError, ValueError, sqlite3.Error):
            return {"state": "blocked", "reason": "reconciliation_unavailable", "retry": False}

    def execute(self, event, now, *, principal="future-actions-reader", operation="contents:read",
                failure=None, before_inference=None):
        if not allowed(principal, operation):
            return {"state": "blocked", "reason": "least_privilege", "retry": False}
        if type(event) is not dict:
            return {"state": "blocked", "reason": "invalid_event", "retry": False}
        reserved = self.controller.reserve(event, now)
        if reserved["state"] != "reserved":
            return {**reserved, "retry": False}
        # Harness hook is only a synthetic revocation/kill-switch injection.
        try:
            if before_inference is not None:
                before_inference()
            intent = self._transition(event, reserved["fence"], now)
            if intent["state"] != "intent":
                return intent
            try:
                reply = self.inference.infer(event, failure=failure)
            except Exception:
                self._uncertain(event, reserved["fence"])
                return {"state": "blocked", "reason": "synthetic_inference_exception",
                        "retry": False}
            if not _valid_reply(reply):
                self._uncertain(event, reserved["fence"])
                return {"state": "blocked", "reason": "invalid_synthetic_reply",
                        "retry": False}
            return self._transition(event, reserved["fence"], now, final=True, reply=reply)
        except Exception:
            # Never turn an unhandled mock failure into a successful checkpoint.
            self._uncertain(event, reserved["fence"])
            return {"state": "blocked", "reason": "synthetic_pipeline_exception",
                    "retry": False}


def _valid_reply(reply):
    return (type(reply) is dict and reply.get("ok") is True
            and type(reply.get("request_id")) is str and bool(reply["request_id"].strip())
            and type(reply.get("text")) is str and bool(reply["text"])
            and type(reply.get("cost_fictitious_units")) is int
            and reply["cost_fictitious_units"] >= 0)
