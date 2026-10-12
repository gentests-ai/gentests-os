"""GitHub-backed advisory queue; controller code always runs from trusted main.

This is a new bounded advisory pipeline, not a bypass of T05/T08 authorization
for a remote tool executor. Models cannot execute code, publish, or grant access.
"""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import time
from urllib.error import HTTPError
from urllib.request import Request, build_opener, HTTPRedirectHandler

from scripts.gt47_t06_groq_budget import BudgetBlocked
from scripts.gt47_t06_groq_handoff import invoke

REPO = 'gentestsai-sudo/gentests-os'
BRANCH = 'gt47-advisory-state'

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError('redirect refused')

class GitHubStore:
    def __init__(self, token):
        if not token:
            raise ValueError('GitHub state token required')
        self.token = token

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
        code, result = self.request('GET', '/contents/' + path + '?ref=' + BRANCH)
        if code == 404:
            return None, None
        if code != 200 or not isinstance(result, dict) or result.get('encoding') != 'base64':
            raise ValueError('invalid state response')
        return json.loads(base64.b64decode(result['content'])), result['sha']

    def put(self, path, value, version):
        body = {'message': 'GT47 advisory state', 'branch': BRANCH,
                'content': base64.b64encode(json.dumps(value, sort_keys=True).encode()).decode()}
        if version is not None:
            body['sha'] = version
        code, result = self.request('PUT', '/contents/' + path, body)
        return code in (200, 201)

    def initialize(self, commit):
        code, _ = self.request('GET', '/git/ref/heads/' + BRANCH)
        if code == 404:
            code, _ = self.request('POST', '/git/refs', {'ref': 'refs/heads/' + BRANCH, 'sha': commit})
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
            raise BudgetBlocked('previous task pending; do not overwrite')
    value = {'id': identifier, 'commit': commit, 'task': task,
             'evidence': evidence, 'status': 'engineering_pending'}
    if not store.put('gt47-current.json', value, version):
        raise BudgetBlocked('queue conflict')
    return value

def advance(store, *, now, api_key, enabled, free_plan_confirmed, transport=None):
    value, version = store.get('gt47-current.json')
    if value is None or value.get('status') == 'completed':
        return {'status': 'idle'}
    status = value.get('status')
    if status not in ('engineering_pending', 'qa_pending'):
        raise ValueError('invalid queued state')
    agent = 'AGT-ENG' if status == 'engineering_pending' else 'AGT-QA'
    result = invoke(store=store, now=now, agent=agent, commit=value['commit'],
                    task=value['task'], evidence=value['evidence'],
                    engineering=value.get('engineering') if agent == 'AGT-QA' else None,
                    api_key=api_key, transport=transport, enabled=enabled,
                    free_plan_confirmed=free_plan_confirmed)
    updated = dict(value)
    updated['engineering' if agent == 'AGT-ENG' else 'qa'] = result
    updated['status'] = 'qa_pending' if agent == 'AGT-ENG' else 'completed'
    if not store.put('gt47-current.json', updated, version):
        raise ValueError('result storage uncertain; never resubmit provider call')
    return {'status': updated['status'], 'agent': agent, 'commit': value['commit'],
            'approval_granted': False}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--enqueue', type=Path)
    parser.add_argument('--commit', required=True)
    args = parser.parse_args()
    if (os.environ.get('GT47_GROQ_ENABLED') != 'true'
            or os.environ.get('GROQ_FREE_PLAN_CONFIRMED') != 'true'):
        parser.exit(0, 'GT47 advisory integration disabled\n')
    if not os.environ.get('GROQ_API_KEY'):
        parser.exit(2, 'GROQ_API_KEY missing; no state or provider call\n')
    store = GitHubStore(os.environ.get('GH_TOKEN', ''))
    store.initialize(args.commit)
    if args.enqueue:
        enqueue(store, commit=args.commit, task=args.enqueue.read_text(encoding='utf-8'))
    try:
        result = advance(store, now=int(time.time()), api_key=os.environ['GROQ_API_KEY'],
                         enabled=True, free_plan_confirmed=True)
    except BudgetBlocked as exc:
        print(json.dumps({'status': 'waiting_or_reconciliation_required', 'reason': str(exc)}))
        return
    print(json.dumps(result))  # Model text is retained in state, never rendered as authority.

if __name__ == '__main__':
    main()
