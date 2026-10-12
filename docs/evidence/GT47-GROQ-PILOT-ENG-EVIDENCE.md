# GTS-47: Engineering advisory persisted

On 2026-10-12, run 38319900411 succeeded. Durable round pilot-round-03 contains
an AGT-ENG advisory_completed result bound to task commit
c1282a59a6dd7431555d6a28ac38847e5fd7b033, dispatch ID
94cf60eca677fb4bd2205e2e8495d6c4787c8b58be097d52c495680c5b44e8c6.
Reported usage: 374 prompt + 102 completion = 476 tokens.
Recommendation: needs_changes; approval_granted=false; code_executed=false.
Observed queue status: qa_pending. This record does not assert QA completion.

User-supplied Groq screenshots show one API request for openai/gpt-oss-120b,
374 input + 102 output = 476 tokens exactly matching the persisted result,
and Total Spend USD 0.00. This is observed
provider dashboard evidence, not an estimate or guarantee of future billing.
Keep Groq Free and Actions USD 0 / Stop usage Yes.

The run summary now displays bounded round metadata, persisted stage,
recommendation categories, reported tokens and the next operational step.
Raw model text, prompts and credentials are excluded. Human approval remains
pending even when both advisory stages complete. Historical claims remain
separate from actual token usage and are not evidence of billing.
