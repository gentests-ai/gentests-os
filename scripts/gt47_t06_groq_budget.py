"""Global rolling-24h budget. Reservations are never refunded, even on error.

Storage must provide read() -> (state, version), cas(version, state) -> bool.
CAS conflicts are retried BEFORE provider submission only. No provider retries.
"""
from copy import deepcopy
import re

CALL_LIMIT = 40
TOKEN_LIMIT = 160_000
TOKENS_PER_CALL = 4_000
MIN_INTERVAL_SECONDS = 300
WINDOW_SECONDS = 86_400

class BudgetBlocked(ValueError):
    status = 'manual_reconciliation_required'
    def __init__(self, message, *, reason='budget_invalid', retry_at=None):
        super().__init__(message)
        self.reason = reason
        self.retry_at = retry_at

class BudgetWaiting(BudgetBlocked):
    status = 'waiting'

class ReconciliationRequired(BudgetBlocked):
    pass

def eligibility(state, *, dispatch_id, now):
    """Read-only gate shared by preflight and the actual CAS reservation."""
    if (type(dispatch_id) is not str or not re.fullmatch('[0-9a-f]{64}', dispatch_id)
            or type(now) is not int or now < 0):
        raise ReconciliationRequired('invalid reservation')
    if (type(state) is not dict or set(state) != {'schema', 'claims'}
            or type(state['schema']) is not int or state['schema'] != 1 or type(state['claims']) is not dict):
        raise ReconciliationRequired('corrupt budget')
    claims = state['claims']
    for key, value in claims.items():
        if (type(key) is not str or not re.fullmatch('[0-9a-f]{64}', key)
                or type(value) is not dict or set(value) != {'at', 'tokens'}
                or type(value['at']) is not int or not 0 <= value['at'] <= now
                or type(value['tokens']) is not int or value['tokens'] != TOKENS_PER_CALL):
            raise ReconciliationRequired('corrupt budget or clock regression')
    if dispatch_id in claims:
        raise ReconciliationRequired('duplicate dispatch; reconcile previous result',
                                     reason='reserved_without_matching_result')
    recent = [c for c in claims.values() if c['at'] > now - WINDOW_SECONDS]
    if len(recent) >= CALL_LIMIT:
        raise BudgetWaiting('waiting for daily call quota', reason='daily_call_quota',
                            retry_at=min(c['at'] for c in recent) + WINDOW_SECONDS)
    if sum(c['tokens'] for c in recent) + TOKENS_PER_CALL > TOKEN_LIMIT:
        raise BudgetWaiting('waiting for daily token quota', reason='daily_token_quota',
                            retry_at=min(c['at'] for c in recent) + WINDOW_SECONDS)
    if recent and now - max(c['at'] for c in recent) < MIN_INTERVAL_SECONDS:
        raise BudgetWaiting('waiting for five-minute spacing', reason='cooldown',
                            retry_at=max(c['at'] for c in recent) + MIN_INTERVAL_SECONDS)

def reserve(store, *, dispatch_id, now):
    for _ in range(5):
        state, version = store.read()
        eligibility(state, dispatch_id=dispatch_id, now=now)
        updated = deepcopy(state)
        updated['claims'][dispatch_id] = {'at': now, 'tokens': TOKENS_PER_CALL}
        if store.cas(version, updated):
            return {'dispatch_id': dispatch_id, 'reserved_tokens': TOKENS_PER_CALL}
    raise BudgetWaiting('budget contention; no provider call permitted', reason='budget_contention')
