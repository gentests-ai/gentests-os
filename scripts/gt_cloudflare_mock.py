"""Cloudflare-shaped OFFLINE mocks. No SDK, network, worker or model."""
import hashlib
import json
import re
import sqlite3
from datetime import datetime, timedelta, timezone

from scripts.gt_dispatch_sim import authorize, key

_ALLOWED = frozenset(("simulate:synthetic",))
_SHA256 = re.compile(r"^[0-9a-f]{64}$")


class FakeWorkersAI:
    """Fully deterministic response. Errors injected without real HTTP."""
    def infer(self, event, failure=None):
        if failure in ("401", "429", "500", "503", "timeout"):
            return {"ok": False, "error": failure, "effect": "unknown" if failure == "timeout" else "none"}
        message = {"mission": event["mission"], "text": "synthetic_ok", "corpus_sha": event["corpus_sha"]}
        raw = json.dumps(message, sort_keys=True, separators=(",", ":"))
        return {"ok": True, "text": raw, "request_id": "fake-" + hashlib.sha256(raw.encode()).hexdigest()[:16],
                "tokens_fictitious": 7, "cost_fictitious_units": 1}


class FakeDurableObject:
    """SQLite LOCAL approximation of atomic reservation and fencing, not a remote DO."""
    def __init__(self, path):
        self.path = str(path)

    def _connect(self):
        db = sqlite3.connect(self.path, timeout=5)
        db.execute("PRAGMA busy_timeout=5000")
        db.execute("""CREATE TABLE IF NOT EXISTS runs (
            k TEXT PRIMARY KEY, state TEXT NOT NULL, fence INTEGER NOT NULL,
            until TEXT, result_hash TEXT, spent INTEGER NOT NULL DEFAULT 0)""")
        return db

    def reserve(self, k, now, lease_seconds=30):
        with self._connect() as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute("SELECT state, fence, until, result_hash FROM runs WHERE k=?", (k,)).fetchone()
            if row is None:
                db.execute("INSERT INTO runs(k,state,fence,until) VALUES(?,?,?,?)",
                           (k, "leased", 1, (now + timedelta(seconds=lease_seconds)).isoformat()))
                return {"state": "leased", "fence": 1}
            state, fence, until, digest = row
            if state == "done" and isinstance(digest, str) and _SHA256.fullmatch(digest):
                return {"state": "duplicate", "result_hash": digest}
            if state == "leased" and isinstance(until, str):
                try:
                    deadline = datetime.fromisoformat(until)
                except ValueError:
                    return {"state": "blocked", "reason": "corrupt_checkpoint"}
                if deadline.tzinfo is None:
                    return {"state": "blocked", "reason": "corrupt_checkpoint"}
                if deadline > now:
                    return {"state": "blocked", "reason": "lease_held"}
                # Lease expiry is NOT proof the external effect did not occur.
                db.execute("UPDATE runs SET state='uncertain', until=NULL WHERE k=?", (k,))
                return {"state": "blocked", "reason": "expired_lease_requires_reconciliation"}
            return {"state": "blocked", "reason": "reconciliation_required"}

    def complete(self, k, fence, text):
        if type(fence) is not int or not text:
            return {"state": "blocked", "reason": "invalid_completion"}
        digest = hashlib.sha256(text.encode()).hexdigest()
        with self._connect() as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute("SELECT state,fence FROM runs WHERE k=?", (k,)).fetchone()
            if row != ("leased", fence):
                return {"state": "blocked", "reason": "stale_fence"}
            db.execute("UPDATE runs SET state='done',result_hash=?,until=NULL WHERE k=?", (digest, k))
        return {"state": "done", "result_hash": digest}

    def uncertain(self, k, fence):
        with self._connect() as db:
            db.execute("BEGIN IMMEDIATE")
            updated = db.execute("UPDATE runs SET state='uncertain',until=NULL WHERE k=? AND state='leased' AND fence=?",
                                 (k, fence)).rowcount
        return updated == 1

    def status(self, k):
        with self._connect() as db:
            return db.execute("SELECT state,fence,result_hash FROM runs WHERE k=?", (k,)).fetchone()


class MockPipeline:
    def __init__(self, checkpoint_path, max_units=2, max_attempts=1):
        self.store = FakeDurableObject(checkpoint_path)
        self.ai = FakeWorkersAI()
        self.max_units = max_units
        self.max_attempts = max_attempts

    def execute(self, event, now, *, failure=None, kill_switch=False, attempted=0, spent=0):
        # Authorization is entirely fictitious; no real identity attestation.
        try:
            reason = authorize(event, now)
            if reason:
                return {"state": "blocked", "reason": reason}
            if event.get("stage") != "simulate" or event.get("scope") not in _ALLOWED:
                return {"state": "blocked", "reason": "invalid_stage"}
            if kill_switch:
                return {"state": "blocked", "reason": "kill_switch"}
            if type(attempted) is not int or type(spent) is not int or attempted < 0 or spent < 0:
                return {"state": "blocked", "reason": "invalid_budget"}
            if attempted >= self.max_attempts or spent + 1 > self.max_units:
                return {"state": "blocked", "reason": "budget_exceeded"}
            k = key(event)
        except (KeyError, TypeError, ValueError):
            return {"state": "blocked", "reason": "invalid_input"}
        reservation = self.store.reserve(k, now)
        if reservation["state"] != "leased":
            return reservation
        reply = self.ai.infer(event, failure)
        if not reply["ok"]:
            self.store.uncertain(k, reservation["fence"])
            return {"state": "blocked", "reason": "provider_" + reply["error"],
                    "effect": reply["effect"], "retry": False}
        return self.store.complete(k, reservation["fence"], reply["text"])
