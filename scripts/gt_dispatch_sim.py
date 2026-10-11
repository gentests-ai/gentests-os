"""Deterministic offline simulation: no cloud, authentication, or model."""
import argparse
import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

REQUIRED = ('repo', 'issue', 'mission', 'stage', 'generation', 'corpus_sha')
PERMITTED = 'simulate:synthetic'

def key(event):
    raw = json.dumps([event[k] for k in REQUIRED], separators=(',', ':'))
    return hashlib.sha256(raw.encode()).hexdigest()

def authorize(event, now):
    auth = event.get('authorization')
    if not isinstance(auth, dict) or auth.get('approved') is not True:
        return 'authorization_missing'
    if auth.get('revoked') is not False:
        return 'authorization_revoked_or_unknown'
    if auth.get('scope') != PERMITTED or event.get('scope') != PERMITTED:
        return 'scope_denied'
    if auth.get('generation') != event.get('generation') or auth.get('corpus_sha') != event.get('corpus_sha'):
        return 'version_mismatch'
    if not isinstance(auth.get('expires_at'), str):
        return 'expiration_missing'
    try:
        expiry = datetime.fromisoformat(auth['expires_at'].replace('Z', '+00:00'))
        if expiry.tzinfo is None or expiry <= now:
            return 'expired'
    except ValueError:
        return 'expiration_invalid'
    if event.get('synthetic') is not True or event.get('operation') != 'dry_run':
        return 'external_effect_denied'
    if not all(isinstance(event.get(k), (str, int)) and event[k] != '' for k in REQUIRED):
        return 'invalid_identity'
    if not isinstance(event['generation'], int) or event['generation'] < 1:
        return 'invalid_generation'
    return None

def run(db_path, event, now=None, crash_after_reserve=False):
    now = now or datetime.now(timezone.utc)
    why = authorize(event, now)
    if why:
        return {'status': 'blocked', 'reason': why}
    db = sqlite3.connect(str(db_path), timeout=5)
    try:
        db.execute('PRAGMA busy_timeout=5000')
        db.execute('CREATE TABLE IF NOT EXISTS runs (key TEXT PRIMARY KEY, status TEXT NOT NULL, output_hash TEXT)')
        db.commit()
        k = key(event)
        with db:
            cursor = db.execute('INSERT OR IGNORE INTO runs(key, status) VALUES (?, ?)', (k, 'reserved'))
            owned = cursor.rowcount == 1
            row = db.execute('SELECT status, output_hash FROM runs WHERE key=?', (k,)).fetchone()
        if not owned:
            if row[0] == 'done':
                return {'status': 'duplicate', 'key': k, 'output_hash': row[1]}
            return {'status': 'blocked', 'reason': 'pending_requires_reconciliation', 'key': k}
        if crash_after_reserve:
            raise RuntimeError('synthetic_crash_after_reserve')
        # No network, GitHub writes, model calls, subprocess, or arbitrary generated code.
        output = json.dumps({'mission': event['mission'], 'result': 'synthetic_ok', 'corpus_sha': event['corpus_sha']}, sort_keys=True)
        digest = hashlib.sha256(output.encode()).hexdigest()
        with db:
            changed = db.execute("UPDATE runs SET status='done', output_hash=? WHERE key=? AND status='reserved'", (digest, k)).rowcount
            if changed != 1:
                raise RuntimeError('reservation_lost')
        return {'status': 'done', 'key': k, 'output_hash': digest}
    finally:
        db.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fixture', required=True, type=Path)
    parser.add_argument('--db', required=True, type=Path)
    parser.add_argument('--now', required=True)
    args = parser.parse_args()
    try:
        now = datetime.fromisoformat(args.now.replace('Z', '+00:00'))
        if now.tzinfo is None:
            raise ValueError('timezone required')
        event = json.loads(args.fixture.read_text(encoding='utf-8'))
        result = run(args.db, event, now)
        print(json.dumps(result, sort_keys=True))
        return 0 if result['status'] in ('done', 'duplicate') else 2
    except (ValueError, KeyError, TypeError, json.JSONDecodeError, sqlite3.DatabaseError, RuntimeError) as exc:
        print(json.dumps({'status': 'blocked', 'reason': type(exc).__name__}))
        return 2

if __name__ == '__main__':
    raise SystemExit(main())
