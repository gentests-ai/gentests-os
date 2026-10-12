"""GitHub-backed advisory queue; controller code always runs from trusted main.

This is a new bounded advisory pipeline, not a bypass of T05/T08 authorization
for a remote tool executor. Models cannot execute code, publish, or grant access.
"""
import argparse
import base64
import hashlib
import json
import os
import re
from pathlib import Path
import time
from urllib.error import HTTPError
from urllib.request import Request, build_opener, HTTPRedirectHandler

from scripts.gt47_t06_groq_budget import BudgetBlocked, BudgetWaiting, ReconciliationRequired, eligibility
from scripts.gt47_t06_groq_handoff import invoke, prepare

REPO = 'gentests-ai/gentests-os'
BRANCH = 'gt47-advisory-state'

class EnqueueRejected(BudgetBlocked):
    """Task was NOT accepted or persisted; producer must handle the failure."""
    status = 'rejected'

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError('redirect refused')

class GitHubStore:
    def __init__(self, token, *, branch=BRANCH):
        if not token:
            raise ValueError('GitHub state token required')
        self.token = token
        if branch != BRANCH and (type(branch) is not str or not re.fullmatch('gt47-recovery-[a-z0-9-]{8,40}', branch)):
            raise ValueError('unsupported state branch')
        self.branch = branch

    def request(self, method, path, body=None):
        request = Request('https://api.github.com/repos/' + REPO + path,
            data=json.dumps(body).encode() if body is not None else None,
            method=method, headers={'Authorization': 'Bearer ' + self.token,
                'Accept': 'application/vnd.github+json', 'Content-Type': 'application/json',
                'X-GitHub-Api-Version': '2022-11-28'})
        try:
            with build_opener(NoRedirect).open(request, timeout=20) as response:
                raw = response.read(1_000_001)
        except HTTPError as exc:
            if exc.code in (404, 409, 422):
                return exc.code, None
            raise ValueError('GitHub state HTTP failure') from None
        if len(raw) > 1_000_000:
            raise ValueError('GitHub state response too large')
        return response.status, json.loads(raw)

    def get(self, path):
        code, result = self.request('GET', '/contents/' + path + '?ref=' + self.branch)
        if code == 404:
            return None, None
        if code != 200 or not isinstance(result, dict) or result.get('encoding') != 'base64':
            raise ValueError('invalid state response')
        return json.loads(base64.b64decode(result['content'])), result['sha']

    def put(self, path, value, version):
        body = {'message': 'GT47 advisory state', 'branch': self.branch,
                'content': base64.b64encode(json.dumps(value, sort_keys=True).encode()).decode()}
        if version is not None:
            body['sha'] = version
        code, result = self.request('PUT', '/contents/' + path, body)
        return code in (200, 201)

    def initialize(self, commit):
        code, _ = self.request('GET', '/git/ref/heads/' + self.branch)
        if code == 404:
            code, _ = self.request('POST', '/git/refs', {'ref': 'refs/heads/' + self.branch, 'sha': commit})
            if code != 201:
                raise ValueError('state branch initialization failed; reconcile')
        elif code != 200:
            raise ValueError('state branch unavailable')

    def read(self):
        state, version = self.get('gt47-budget.json')
        return ({'schema': 1, 'claims': {}} if state is None else state), version

    def cas(self, version, state):
        return self.put('gt47-budget.json', state, version)

def enqueue(store, *, commit, task):
    # Invoked only AFTER workflow offline checks for precisely this commit.
    from scripts.gt47_t06_groq_handoff import prepare
    evidence = {'commit': commit, 'tests_passed': True, 'links_passed': True}
    prepare(agent='AGT-ENG', commit=commit, task=task, evidence=evidence)
    current, version = store.get('gt47-current.json')
    identifier = hashlib.sha256((commit + task).encode()).hexdigest()
    if current:
        if current.get('id') == identifier:
            return current
        if current.get('status') != 'completed':
            raise EnqueueRejected('previous task pending; new task not accepted', reason='previous_task_pending')
    value = {'id': identifier, 'commit': commit, 'task': task,
             'evidence': evidence, 'status': 'engineering_pending'}
    if not store.put('gt47-current.json', value, version):
        raise EnqueueRejected('queue conflict; task not accepted', reason='queue_contention')
    return value

def start_new_round(store, *, commit, task, round_id, expected_id, now):
    """Archive a blocked attempt without resolving it or refunding any claim.

    Caller validates trusted main offline and serializes with the pilot workflow.
    No provider submission is performed. Archive precedes queue CAS.
    """
    if (type(round_id) is not str or not re.fullmatch('[a-z0-9-]{8,40}', round_id)
            or type(expected_id) is not str or not re.fullmatch('[0-9a-f]{64}', expected_id)):
        raise EnqueueRejected('invalid round or expected task', reason='invalid_round')
    current, version = store.get('gt47-current.json')
    if (type(current) is not dict or current.get('id') != expected_id
            or current.get('status') not in ('engineering_pending', 'qa_pending')
            or type(current.get('diagnostic')) is not dict
            or current['diagnostic'].get('status') != 'manual_reconciliation_required'
            or current.get('commit') == commit):
        raise EnqueueRejected('blocked task changed or commit not new', reason='round_precondition_failed')
    evidence = {'commit': commit, 'tests_passed': True, 'links_passed': True}
    scoped_task = 'Round ' + round_id + '\n' + task
    _, digest = prepare(agent='AGT-ENG', commit=commit, task=scoped_task, evidence=evidence)
    budget, _ = store.read()
    eligibility(budget, dispatch_id=digest, now=now)
    archive_path = 'gt47-archive/' + expected_id + '.json'
    archived, _ = store.get(archive_path)
    if archived is None:
        if not store.put(archive_path, current, None):
            raise EnqueueRejected('archive write uncertain; inspect before retry', reason='archive_storage_uncertain')
        archived, _ = store.get(archive_path)
    if archived != current:
        raise EnqueueRejected('archive mismatch; queue untouched', reason='archive_mismatch')
    value = {'id': hashlib.sha256((commit + scoped_task).encode()).hexdigest(),
             'commit': commit, 'task': scoped_task, 'round_id': round_id,
             'previous_task_id': expected_id, 'evidence': evidence,
             'status': 'engineering_pending'}
    if not store.put('gt47-current.json', value, version):
        raise EnqueueRejected('queue write uncertain; inspect before retry', reason='queue_contention')
    return {'status': 'round_prepared', 'id': value['id'], 'round_id': round_id,
            'previous_task_id': expected_id, 'provider_calls': 0}

def advance(store, *, now, api_key, enabled, free_plan_confirmed, transport=None):
    value, version = store.get('gt47-current.json')
    if value is None:
        return {'status': 'idle'}
    if type(value) is not dict:
        raise ReconciliationRequired('invalid queued state', reason='invalid_queue')
    if value.get('status') == 'completed':
        return {'status': 'idle'}
    status = value.get('status')
    if status not in ('engineering_pending', 'qa_pending'):
        raise ValueError('invalid queued state')
    if type(value.get('diagnostic', {})) is not dict:
        raise ReconciliationRequired('invalid queue diagnostic', reason='invalid_queue')
    if value.get('diagnostic', {}).get('status') == 'manual_reconciliation_required':
        raise ReconciliationRequired('manual reconciliation required', reason='persisted_reconciliation')
    agent = 'AGT-ENG' if status == 'engineering_pending' else 'AGT-QA'
    try:
        result = invoke(store=store, now=now, agent=agent, commit=value['commit'],
                    task=value['task'], evidence=value['evidence'],
                    engineering=value.get('engineering') if agent == 'AGT-QA' else None,
                    api_key=api_key, transport=transport, enabled=enabled,
                        free_plan_confirmed=free_plan_confirmed)
    except BudgetBlocked:
        raise
    except (ValueError, OSError, KeyError, TypeError):
        # Covers injected transports and failures before/while reserving quota.
        # Never infer whether the provider accepted a submission.
        raise ReconciliationRequired('invocation or reservation failed', reason='invocation_or_reservation_failure') from None
    updated = dict(value)
    updated.pop('diagnostic', None)
    updated['engineering' if agent == 'AGT-ENG' else 'qa'] = result
    updated['status'] = 'qa_pending' if agent == 'AGT-ENG' else 'completed'
    try:
        stored = store.put('gt47-current.json', updated, version)
    except (ValueError, OSError, KeyError, TypeError):
        stored = False
    if not stored:
        raise ReconciliationRequired('result storage uncertain; never resubmit provider call', reason='result_storage_uncertain') from None
    return {'status': updated['status'], 'agent': agent, 'commit': value['commit'],
            'approval_granted': False}

def inspect_queue(store, *, now):
    """Only reads state: no branch creation, dependency install or provider call."""
    value, _ = store.get('gt47-current.json')
    if value is None:
        return {'status': 'idle'}
    if type(value) is not dict:
        return {'status': 'manual_reconciliation_required', 'reason': 'invalid_queue'}
    if value.get('status') == 'completed':
        return {'status': 'idle'}
    try:
        if type(value.get('diagnostic', {})) is not dict:
            raise ReconciliationRequired('invalid queue diagnostic', reason='invalid_queue')
        if value.get('diagnostic', {}).get('status') == 'manual_reconciliation_required':
            raise ReconciliationRequired('manual reconciliation required', reason='persisted_reconciliation')
        if value.get('status') not in ('engineering_pending', 'qa_pending'):
            raise ReconciliationRequired('invalid queue state', reason='invalid_queue')
        agent = 'AGT-ENG' if value['status'] == 'engineering_pending' else 'AGT-QA'
        _, digest = prepare(agent=agent, commit=value['commit'], task=value['task'],
                            evidence=value['evidence'], engineering=value.get('engineering'))
        state, _ = store.read()
        eligibility(state, dispatch_id=digest, now=now)
        return {'status': 'ready', 'agent': agent, 'commit': value['commit']}
    except BudgetBlocked as exc:
        return diagnostic(exc)
    except (ValueError, KeyError, TypeError):
        return {'status': 'manual_reconciliation_required', 'reason': 'invalid_queue'}

def diagnostic(exc):
    result = {'status': exc.status, 'reason': exc.reason}
    if exc.retry_at is not None:
        result['retry_at'] = exc.retry_at
    return result

def run_once(store, **kwargs):
    """Persist operational diagnosis so a fresh runner sees the same outcome."""
    try:
        original, _ = store.get('gt47-current.json')
    except (ValueError, OSError, KeyError, TypeError):
        return {'status': 'manual_reconciliation_required', 'reason': 'state_read_failure'}
    try:
        return advance(store, **kwargs)
    except BudgetBlocked as exc:
        result = diagnostic(exc)
    except (ValueError, OSError, KeyError, TypeError):
        result = {'status': 'manual_reconciliation_required', 'reason': 'provider_or_state_failure'}
    try:
        value, version = store.get('gt47-current.json')
        if type(value) is dict and value.get('status') in ('engineering_pending', 'qa_pending'):
            if (not original or value.get('id') != original.get('id')
                    or value.get('status') != original.get('status')):
                return inspect_queue(store, now=kwargs['now'])
            # Do not attach another process's stale error to a newly completed stage.
            state = inspect_queue(store, now=kwargs['now'])
            if state['status'] == 'ready' and result['status'] == 'manual_reconciliation_required':
                return result  # No reservation: an unrelated/configuration failure.
            value['diagnostic'] = result
            if not store.put('gt47-current.json', value, version):
                return {'status': 'manual_reconciliation_required', 'reason': 'diagnostic_storage_conflict'}
    except (ValueError, OSError, KeyError, TypeError):
        return {'status': 'manual_reconciliation_required', 'reason': 'diagnostic_storage_failure'}
    return result

def queue_summary(value, result):
    """Render only bounded metadata; model prose never becomes UI authority."""
    value = value if type(value) is dict else {}
    labels = {'engineering_pending': 'Engenharia pendente', 'qa_pending': 'QA pendente',
              'completed': 'Pareceres concluidos', 'waiting': 'Aguardando intervalo ou quota',
              'ready': 'Pronto para avancar', 'idle': 'Sem etapa a executar',
              'manual_reconciliation_required': 'Bloqueado: reconciliacao manual',
              'rejected': 'Operacao recusada'}
    status = labels.get(value.get('status'), 'Estado indisponivel')
    operation = labels.get(result.get('status'), 'Estado indisponivel')
    def identifier(key, pattern):
        text = value.get(key)
        return text if type(text) is str and re.fullmatch(pattern, text) else 'indisponivel'
    lines = ['### GTS-47 — estado da rodada', '',
             '| Campo | Valor |', '| --- | --- |',
             '| Rodada | ' + identifier('round_id', '[a-z0-9-]{8,40}') + ' |',
             '| Fila | ' + status + ' |', '| Este run | ' + operation + ' |',
             '| Commit da tarefa | ' + identifier('commit', '[0-9a-f]{40}') + ' |', '',
             '| Agente | Parecer salvo | Recomendacao | Tokens consumidos |',
             '| --- | --- | --- | --- |']
    recommendations = {'needs_changes': 'Requer ajustes',
                       'ready_for_human_review': 'Pronto para revisao humana'}
    total = 0
    for key, agent in [('engineering', 'Engenharia'), ('qa', 'QA')]:
        entry = value.get(key)
        entry = entry if type(entry) is dict else {}
        valid = (entry.get('status') == 'advisory_completed'
                 and entry.get('commit') == value.get('commit')
                 and entry.get('agent') == ('AGT-ENG' if key == 'engineering' else 'AGT-QA'))
        review = entry.get('review') if type(entry.get('review')) is dict else {}
        usage = entry.get('usage') if type(entry.get('usage')) is dict else {}
        tokens = usage.get('total_tokens')
        tokens = tokens if valid and type(tokens) is int and 0 <= tokens <= 4000 else None
        total += tokens or 0
        recommendation = recommendations.get(review.get('recommendation'), 'Indisponivel') if valid else 'Pendente'
        lines.append('| ' + agent + ' | ' + ('Sim' if valid else 'Nao') + ' | '
                     + recommendation + ' | ' + (str(tokens) if tokens is not None else '—') + ' |')
    lines += ['', 'Tokens informados nos pareceres: **' + str(total) + '**. Reservas de quota nao sao cobranca.', '',
              '**Aprovacao humana: pendente.** Parecer de modelo nao aprova merge ou deploy.']
    if result.get('status') == 'manual_reconciliation_required':
        lines += ['', 'Proximo passo: pausar e reconciliar; nao reenviar chamadas incertas.']
    elif value.get('status') == 'completed':
        lines += ['', 'Proximo passo: pausar o piloto e revisar os pareceres.']
    elif value.get('status') == 'qa_pending':
        lines += ['', 'Proximo passo: QA consome Engenharia apos o intervalo minimo de 5 minutos.']
    else:
        lines += ['', 'Proximo passo: verificar elegibilidade antes de avancar.']
    return '\n'.join(lines) + '\n'

def write_queue_summary(store, result):
    path = os.environ.get('GITHUB_STEP_SUMMARY')
    if not path:
        return
    try:
        value, _ = store.get('gt47-current.json')
        content = queue_summary(value, result)
        with open(path, 'a', encoding='utf-8') as output:
            output.write(content)
    except (ValueError, OSError, KeyError, TypeError):
        # Optional presentation must not change state or trigger a submission.
        print('GT47 summary unavailable; inspect durable state')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--enqueue', type=Path)
    parser.add_argument('--commit')
    parser.add_argument('--inspect', action='store_true')
    parser.add_argument('--new-round', type=Path)
    parser.add_argument('--round-id')
    parser.add_argument('--expected-id')
    args = parser.parse_args()
    if args.new_round:
        if (os.environ.get('GT47_GROQ_ENABLED') != 'false'
                or not args.commit or args.enqueue or args.inspect
                or os.environ.get('GROQ_API_KEY')):
            parser.exit(2, 'New round requires paused pilot, commit and no provider key\n')
        try:
            result = start_new_round(GitHubStore(os.environ.get('GH_TOKEN', '')),
                commit=args.commit, task=args.new_round.read_text(encoding='utf-8'),
                round_id=args.round_id, expected_id=args.expected_id, now=int(time.time()))
        except BudgetBlocked as exc:
            result = diagnostic(exc)
        except (ValueError, OSError, KeyError, TypeError):
            result = {'status': 'manual_reconciliation_required', 'reason': 'round_storage_uncertain'}
        print(json.dumps(result))
        if result['status'] != 'round_prepared':
            parser.exit(2)
        return
    if (os.environ.get('GT47_GROQ_ENABLED') != 'true'
            or os.environ.get('GROQ_FREE_PLAN_CONFIRMED') != 'true'):
        parser.exit(0, 'GT47 advisory integration disabled\n')
    store = GitHubStore(os.environ.get('GH_TOKEN', ''))
    if args.inspect:
        try:
            result = inspect_queue(store, now=int(time.time()))
        except (ValueError, OSError, KeyError, TypeError):
            result = {'status': 'manual_reconciliation_required', 'reason': 'state_read_failure'}
        print(json.dumps(result))
        write_queue_summary(store, result)
        if os.environ.get('GITHUB_OUTPUT'):
            with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as output:
                output.write('status=' + result['status'] + '\n')
        if result['status'] == 'manual_reconciliation_required':
            parser.exit(2)
        return
    if not args.commit:
        parser.error('--commit required to enqueue or advance')
    if not os.environ.get('GROQ_API_KEY'):
        parser.exit(2, 'GROQ_API_KEY missing; no state or provider call\n')
    try:
        store.initialize(args.commit)
        if args.enqueue:
            enqueue(store, commit=args.commit, task=args.enqueue.read_text(encoding='utf-8'))
        result = run_once(store, now=int(time.time()), api_key=os.environ['GROQ_API_KEY'],
                         enabled=True, free_plan_confirmed=True)
    except BudgetBlocked as exc:
        result = diagnostic(exc)
    except (ValueError, OSError, KeyError, TypeError):
        result = {'status': 'manual_reconciliation_required', 'reason': 'state_or_enqueue_failure'}
    print(json.dumps(result))  # Model text is retained in state, never rendered as authority.
    write_queue_summary(store, result)
    if result['status'] in ('manual_reconciliation_required', 'rejected'):
        parser.exit(2)

if __name__ == '__main__':
    main()
