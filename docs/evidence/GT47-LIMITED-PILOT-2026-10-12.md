# GTS-47 limited real pilot: reconciliation required

PR #107 merged into main at `86ffb9f425cd05f34ec031e0deacfae41702cd42`.
The user confirmed pause before merge, then enabled the pilot and confirmed
Groq free-plan and Actions USD 0 / Stop usage Yes controls. Variable API access
was denied with HTTP 403; confirmations are user-reported. Post-merge QG and
Markdown checks passed; 269 local tests and 104 Markdown link checks passed
on that exact commit.

The state branch was absent before initialization. After offline validation,
the queue was initialized and enqueued without any provider call. Preflight
returned ready for AGT-ENG. No initial budget file existed.

Run [38305746286](https://github.com/gentests-ai/gentests-os/actions/runs/38305746286)
was dispatched exactly once on main. Probe succeeded; advance failed.
The logs confirm `GT47_GROQ_ENABLED=true`, `GROQ_FREE_PLAN_CONFIRMED=true`,
and masked GitHub/Groq keys. The runner reported:

```json
{"status":"manual_reconciliation_required","reason":"provider_or_state_failure"}
```

The queue remains `engineering_pending`, with that diagnostic. No engineering
result was persisted, and no QA stage was invoked by this session.
The budget retains one dispatch reservation:

```json
{"schema":1,"claims":{"7b7bc7a2a583a72ba4ed39db5cdaeaa3426718d712e2715a78e909d6c9a1aec0":{"at":1791837644,"tokens":4000}}}
```

This is a quota reservation, not measured token usage or evidence of a provider
receipt. The generic diagnostic does not distinguish HTTP failure, malformed
provider output, transport uncertainty or state write failure. Do not infer
zero inference or successful inference. Do not resubmit, refund/delete the
reservation, clear the diagnostic or create a different dispatch to bypass it.
Reconcile read-only Groq activity for 2026-10-12 around 17:40:44–17:40:48
America/Sao_Paulo before any further real call. The user was asked to re-pause;
at the last reply GT47_GROQ_ENABLED was still true. The durable preflight blocks
this queue, but configuration pause remains outstanding.

Automatic handoff runs after PR CI and merge were skipped while paused:
38305095099 and 38305395722. They are separate workflow_run events, not retries
of the manual provider submission. No failed job was rerun by this session.

A follow-up review found the second recovery harness copy in
`.github/workflows/gt47-t06-offline-tests.yml` still checked out the old commit.
Update it to trusted main, matching the standalone recovery workflow. The
provider remains synthetic, no Groq key is supplied, and write opt-in plus
isolated trial branches remain mandatory. Historical evidence is unchanged.
