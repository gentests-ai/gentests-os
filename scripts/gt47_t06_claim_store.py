"""T06 offline: persistent, fail-closed claim of a prepared dispatch intent.

No agent invocation or GitHub write. Caller controls the SQLite database path.
"""
from __future__ import annotations
import sqlite3

from scripts.gt47_t04_context_loader import ContextRejected


def claim_dispatch(db_path: str, intent: dict) -> dict:
    """Atomically claim once; replay of the same dispatch_id is rejected."""
    if type(intent) is not dict or set(intent) != {
        "status", "mission", "issue", "agent_id", "commit_sha",
        "dispatch_id", "context_sha256", "execution_allowed",
        "authorization_granted", "external_agent_invoked",
        "write_performed", "replay_protection_persistent"
    }:
        raise ContextRejected("invalid prepared intent shape")
    if (intent["status"] != "prepared_offline"
            or intent["execution_allowed"] is not False
            or intent["authorization_granted"] is not False
            or intent["external_agent_invoked"] is not False
            or intent["write_performed"] is not False
            or intent["replay_protection_persistent"] is not False):
        raise ContextRejected("unsafe dispatch intent")
    dispatch_id = intent["dispatch_id"]
    if (type(dispatch_id) is not str or len(dispatch_id) != 64
            or any(c not in "0123456789abcdef" for c in dispatch_id)):
        raise ContextRejected("invalid dispatch id")
    if type(db_path) is not str or not db_path:
        raise ContextRejected("missing durable store path")
    try:
        with sqlite3.connect(db_path, timeout=5) as conn:
            conn.execute("CREATE TABLE IF NOT EXISTS gt47_claims (dispatch_id TEXT PRIMARY KEY)")
            conn.execute("INSERT INTO gt47_claims(dispatch_id) VALUES (?)", (dispatch_id,))
    except sqlite3.IntegrityError as exc:
        raise ContextRejected("duplicate dispatch / replay rejected") from exc
    except sqlite3.Error as exc:
        raise ContextRejected("dispatch claim store unavailable") from exc
    return {"dispatch_id": dispatch_id, "status": "claimed_offline",
            "execution_allowed": False, "external_agent_invoked": False}
