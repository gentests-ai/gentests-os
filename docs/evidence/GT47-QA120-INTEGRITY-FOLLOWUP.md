# GTS-47: follow-up to QA review of PR 120

The user supplied a read-only independent QA report: PASS WITH OBSERVATIONS.
This change addresses incomplete persisted-result validation and separates
legacy recommendation acceptance from fresh provider response validation.

Before demand finalization, validate exact top-level fields, agent, status,
commit, model, false technical authorization flags, full review contract and
token arithmetic/bounds. Recompute semantic dispatch IDs using the task,
matching offline evidence and model; QA identity also binds the Engineering
review. Invalid records return unverified. Invalid Engineering input blocks
QA before quota reservation or provider submission.

Fresh responses accept needs_changes or ready_for_finalization only.
Historical saved-result validation retains ready_for_human_review. Synthetic
recovery fixtures now emit the new recommendation. Production history and
reservations are not rewritten, and no retry or new generation is performed.

These checks detect malformed or mismatched records, not forgery by an actor
with authorized GitHub state write access. They do not independently prove
provider origin, test execution or model authenticity. GitHub access control
remains the trust boundary; no cryptographic receipt is fabricated.

Negative coverage includes changed tasks, evidence, dispatch IDs, model,
authorization flags, token counts, missing/extra fields, changed Engineering
review, invalid QA review and rejection of fresh legacy responses.
The deferred automatic return-for-adjustments flow remains out of scope.
