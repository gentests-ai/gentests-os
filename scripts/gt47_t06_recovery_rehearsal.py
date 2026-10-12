"""Manual remote evidence harness: isolated test refs, fake provider, no Groq key.

This is not automatically executed by PR CI. It requires explicit opt-in to
GitHub state writes. Delays/runner availability must be observed, not inferred.
"""
import argparse
import json
import os
import re
import time

from scripts.gt47_t06_groq_handoff import MODEL
from scripts.gt47_t06_groq_runner import GitHubStore, enqueue, inspect_queue, run_once

def test_branch(trial):
    if type(trial) is not str or not re.fullmatch('[a-z0-9-]{8,40}', trial):
        raise ValueError('invalid rehearsal trial')
    return 'gt47-recovery-' + trial

def synthetic_provider(store, *, interrupt=False):
    def submit(payload):
        agent = 'AGT-QA' if payload['messages'][0]['content'].startswith('QA:') else 'AGT-ENG'
        journal, version = store.get('gt47-test-submissions.json')
        if journal is None:
            journal = []
        journal.append({'agent': agent, 'at': int(time.time()), 'synthetic': True})
        if not store.put('gt47-test-submissions.json', journal, version):
            raise ValueError('synthetic submission journal conflict')
        if interrupt:
            print('SYNTHETIC_SUBMISSION_PERSISTED', flush=True)
            while True:
                time.sleep(1)  # Operator/timeout terminates this OS process.
        return {'model': MODEL,
                'usage': {'prompt_tokens': 400, 'completion_tokens': 100, 'total_tokens': 500},
                'choices': [{'finish_reason': 'stop', 'message': {'content': json.dumps({
                    'summary': 'Synthetic remote state rehearsal, no model invoked.',
                    'findings': [], 'recommendation': 'ready_for_human_review'})}}]}
    return submit

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trial', required=True)
    parser.add_argument('--commit', required=True)
    parser.add_argument('--phase', choices=('seed', 'advance', 'interrupt', 'inspect'), required=True)
    parser.add_argument('--allow-test-writes', action='store_true')
    args = parser.parse_args()
    if not args.allow_test_writes:
        parser.exit(2, 'Rehearsal requires explicit isolated-state-write opt-in\n')
    if not re.fullmatch('[0-9a-f]{40}', args.commit):
        parser.error('invalid commit')
    store = GitHubStore(os.environ.get('GH_TOKEN', ''), branch=test_branch(args.trial))
    now = int(time.time())
    if args.phase == 'seed':
        store.initialize(args.commit)
        enqueue(store, commit=args.commit, task='Synthetic runner recovery rehearsal. No inference.')
        old, version = store.get('gt47-test-seed.json')
        if old is None and not store.put('gt47-test-seed.json', {'at': now, 'commit': args.commit}, version):
            raise ValueError('seed metadata storage conflict')
        result = inspect_queue(store, now=now)
    elif args.phase == 'inspect':
        result = inspect_queue(store, now=now)
    else:
        result = run_once(store, now=now, api_key='synthetic-no-secret', enabled=True,
                          free_plan_confirmed=True,
                          transport=synthetic_provider(store, interrupt=args.phase == 'interrupt'))
    seed, _ = store.get('gt47-test-seed.json')
    submissions, _ = store.get('gt47-test-submissions.json')
    result.update(test_branch=store.branch, inference_calls=0,
                  synthetic_submissions=len(submissions or []),
                  elapsed_since_seed=now - seed['at'] if seed else None)
    print(json.dumps(result), flush=True)
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as output:
            output.write('GT47 isolated rehearsal: `' + json.dumps(result) + '`\n')
    if result['status'] == 'manual_reconciliation_required':
        parser.exit(2)

if __name__ == '__main__':
    main()
