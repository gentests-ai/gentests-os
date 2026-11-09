# GTS-47 post-transfer reconciliation

Read-only observations on 2026-10-12, after PR #107 merged into `main`
at `86ffb9f425cd05f34ec031d0e`.

The owner-routing correction is already on main. The original run
`38304173359` remains failed (attempt 1); it was not rerun in this session.
Historical evidence and the immutable pre-transfer claim namespace remain intact.

## Current production evidence

The previously absent `gt47-advisory-state` branch now exists. Its observed
head is `af9f0a8d6af0b1b61d7dca20856e432d94ccc0d4`.
`gt47-current.json` records the main commit above, task ID
`cc83d5def2d9a0c5f2f918964568e695467130ff9083062deca00157c4aadcc9`,
status `engineering_pending`, and diagnostic `manual_reconciliation_required`
with reason `provider_or_state_failure`. No Engineering or QA result is stored.

`gt47-budget.json` preserves claim
`7b7bc7a2a583a72ba4ed39db5cdaeaa3426718d712e2715a78e909d6c9a1aec0`
with `at=1791837644`, `tokens=4000`, schema 1.
This reservation does not prove provider acceptance or billing. The provider
outcome is uncertain: do not clear the claim, replace the task, or resend it.

Run `38305746286` (`workflow_dispatch`) and run `38306489982`
(`schedule`) failed after the owner fix; subsequent observed workflow_run
entries were skipped. These observations do not establish that the pilot is paused.
At inspection, queued and in-progress advisory run queries both returned zero.
The manual run passed probe and failed advance; the later scheduled run failed
probe and skipped advance. Job log download was unavailable, so no specific
provider error or request receipt could be independently recovered.
Reading repository Actions variables returned HTTP 403, so
`GT47_GROQ_ENABLED` and free-plan settings could not be independently verified.

## Remaining functional correction

The T06 offline-tests workflow also contained an isolated recovery job pinned
to pre-fix controller `c6ffa661be39a793bcdd43ab226fd4770453cba7`.
Use trusted `refs/heads/main`, as in the dedicated recovery workflow corrected
by PR #107. Preserve isolated recovery refs, synthetic transport, explicit
write opt-in, no provider secret, concurrency and interruption controls.
ENG20 authorization records are outside this pilot and remain unchanged.

## Validation and stop condition

269 offline unit tests passed; Markdown link validation passed for 105 files;
`git diff --check` passed. No provider invocation, workflow dispatch, rerun,
production state write, claim reset or paid OpenAI API was performed here.

Real ENG → QA validation is blocked pending confirmed pause and manual
reconciliation of the uncertain Engineering submission. Keep Actions budget
USD 0 / Stop usage Yes and Groq Free. Confirm provider outcome using available
receipts before deciding any recovery; an absent persisted result alone is
not evidence that no request was accepted. Do not resume scheduling or advance
QA until the Engineering result and its commit binding are verified.
