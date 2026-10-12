# GTS-47 owner transfer correction

Repository: `gentests-ai/gentests-os`; default branch: `main`.
Observed on 2026-10-12. Base commit: `61085c4c1ab8b42227dea6272099517d1fa266f9`.

## Diagnosis and preserved evidence

Read-only GitHub API inspection of run `38304173359` confirmed attempt 1,
`workflow_run`, conclusion `failure`: probe and validate succeeded, advance failed.
The state ref `refs/heads/gt47-advisory-state` returned HTTP 404.
The reported `state_or_enqueue_failure` is consistent with the old owner URL
and the controller refusing redirects. The job log download was unavailable;
this change does not claim independent verification of that diagnostic text.
No failed job or provider request was replayed.

API access to read and update `GT47_GROQ_ENABLED` returned HTTP 403
(`Resource not accessible by integration`). The user reported the value `true`.
Pause is therefore not established; real validation remains blocked.
The user reports Actions budget USD 0, Stop usage Yes, a Groq free account,
`GROQ_API_KEY` configured and `GROQ_FREE_PLAN_CONFIRMED=true`.
Those billing and secret settings were not independently inspected.

## Correction and safety

Update functional T04–T06 URLs, repository checks and corresponding fixtures
for the canonical owner. Keep redirect refusal, narrowly scoped allowlists,
quota reservations, uncertainty handling and no-retry behavior.
Keep the old claim-ledger repository string as an immutable hash namespace:
it is never an HTTP destination. Changing this namespace would reset replay
identity for prior claims. Keep historical evidence and ENG20 authorization
records unchanged; this is not renewed authorization for ENG20.

The recovery rehearsal workflow previously checked out
`c6ffa661be39a793bcdd43ab226fd4770453cba7`, which still uses the old owner.
It now checks out trusted `main`; the fix must be merged before the rehearsal.
The harness still uses isolated `gt47-recovery-*` refs, an explicit write opt-in,
a synthetic provider, no Groq key, and no inference. Concurrency, timeouts and
termination inspection remain intact. No remote rehearsal was dispatched.

## Validation

269 offline unit tests passed, including canonical state URL, redirect refusal,
old-owner rejection and unchanged pre-transfer reservation identity.
Markdown link validation passed for 104 files. No paid OpenAI API was used;
no Groq call and no Actions dispatch was performed by this session.

## Real pilot gate

Before merge or dispatch: confirm the pilot paused and reconcile any in-flight
runs plus durable queue/budget claims. Do not delete reservations or retry an
uncertain submission. Review/merge the PR into main explicitly. Then perform
one bounded ENG stage and one QA stage only after its cooldown and verified
ENG persistence. Existing completed/uncertain dispatch IDs must never be resent.
Keep Actions USD 0/Stop usage Yes and the confirmed Groq free plan. Re-pause
immediately after the limited pilot. If permissions or free-plan evidence are
unavailable, report validation blocked rather than infer successful execution.
