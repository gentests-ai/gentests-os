# GTS-47 safe failure diagnostics

## Evidence supplied on 2026-10-12

The user queried `GT47_GROQ_ENABLED` using their GitHub CLI and confirmed the
exact value `false` after normalizing its trailing newline. The pilot is paused
according to that supplied evidence; the integration's variable access was 403.
The Groq recording shows the current USD 0 plan. The supplied Activity screenshot
shows no usage for October 2026 with all projects selected. The dashboard warns
of up to 15 minutes of delay; absence of aggregate usage is not a receipt proving
the uncertain request was never accepted.

The user supplied failed-job logs for run `38305746286`. They show
`manual_reconciliation_required`, reason `provider_or_state_failure`, exit 2,
and main commit `86ffb9f425cd05f34ec031e0deacfae41702cd42`.
They do not disclose the provider error or distinguish it from result storage.
The existing claim and production state must remain unchanged.

## Diagnostic change

Future failures distinguish `provider_http_<status>`,
`provider_transport_uncertain`, `provider_response_invalid`, and
`result_storage_uncertain`. HTTP diagnoses contain only a validated status code,
never response bodies, prompts, credentials or raw exception text. Unknown
invocation/reservation errors remain conservative rather than infer acceptance.
All diagnoses still require manual reconciliation and retain quota claims.
No retry or recovery authorization is introduced. This cannot retroactively
resolve the old ambiguous failure.

## Offline validation

273 tests passed, including HTTP 401/403/429/500, transport uncertainty,
invalid responses and successful provider response followed by storage failure.
The regression checks preserve claims, suppress secrets and prevent repeated
submission even after 24 hours. No production state write, Groq/OpenAI request,
workflow dispatch or rerun was performed during this change.

Maintain Actions USD 0 / Stop usage Yes. Keep the pilot paused pending manual
reconciliation; do not clear its diagnostic, delete its claim or resend its task.
