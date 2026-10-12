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
    pass

def reserve(store, *, dispatch_id, now):
    if (type(dispatch_id) is not str or not re.fullmatch('[0-9a-f]{64}', dispatch_id)
            or type(now) is not int or now < 0):
        raise BudgetBlocked('invalid reservation')
    for _ in range(5):
        state, version = store.read()
        if (type(state) is not dict or set(state) != {'schema', 'claims'}
                or state['schema'] != 1 or type(state['claims']) is not dict):
            raise BudgetBlocked('corrupt budget')
        claims = state['claims']
        for key, value in claims.items():
            if (type(key) is not str or not re.fullmatch('[0-9a-f]{64}', key)
                    or type(value) is not dict or set(value) != {'at', 'tokens'}
                    or type(value['at']) is not int or not 0 <= value['at'] <= now
                    or type(value['tokens']) is not int or value['tokens'] != TOKENS_PER_CALL):
                raise BudgetBlocked('corrupt budget or clock regression')
        # Keep old claims: same commit/role/input must never be dispatched twice.
        if dispatch_id in claims:
            raise BudgetBlocked('duplicate dispatch; reconcile previous result')
        recent = [c for c in claims.values() if c['at'] > now - WINDOW_SECONDS]
        if len(recent) >= CALL_LIMIT:
            raise BudgetBlocked('waiting for daily call quota')
        if sum(c['tokens'] for c in recent) + TOKENS_PER_CALL > TOKEN_LIMIT:
            raise BudgetBlocked('waiting for daily token quota')
        if recent and now - max(c['at'] for c in recent) < MIN_INTERVAL_SECONDS:
            raise BudgetBlocked('waiting for five-minute spacing')
        updated = deepcopy(state)
        updated['claims'][dispatch_id] = {'at': now, 'tokens': TOKENS_PER_CALL}
        if store.cas(version, updated):
            return {'dispatch_id': dispatch_id, 'reserved_tokens': TOKENS_PER_CALL}
    raise BudgetBlocked('budget contention; no provider call permitted')
