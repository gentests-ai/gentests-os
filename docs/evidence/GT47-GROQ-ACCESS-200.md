# GTS-47 Groq access observation

On 2026-10-12, read-only probe run 38319196703 succeeded on GitHub Actions:
HTTP 200, target_model_listed=true, inference_calls=0. It used the updated
secret and an explicit GTS47-Access-Probe/1.0 User-Agent. Prior probes returned
403 with urllib default identification. This is consistent with client-header
sensitivity, but does not independently prove why previous requests were denied.
Listing models does not establish successful chat inference.

The advisory transport now identifies itself as GTS47-Advisory/1.0. Redirect
refusal, one submission, quota reservations and manual reconciliation remain.
No retry or claim reset is introduced. Round pilot-round-02 remains blocked
with provider_http_403 and its claim intact; a subsequent authorized round
must archive it using workflow 12 before any new inference.

Validation: offline suite and safe failure regression checks verify the explicit
client header, one request and no repeat submission. No chat call was performed
for this change. Keep Actions USD 0 / Stop usage Yes and Groq Free.
