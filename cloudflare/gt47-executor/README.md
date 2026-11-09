# GT47 Cloudflare remote executor

This implementation is deliberately inert until separately provisioned and authorized. Repository changes create no Cloudflare resource, secret, key, deployment, inference or paid service.

## Runtime

- HTTPS Worker validates GitHub Actions OIDC using the fixed GitHub JWKS URL, issuer, audience, repository ID, workflow ref/SHA allowlist, main ref, event and actor.
- A version-3 Ed25519 decision authorizes exactly GT-AI-DISPATCH-001 / issue 47 / AGT-ENG, a pinned commit and contract blob, task+context digest, nonce, short validity, a positive USD-micros budget, a fixed tool allowlist, and hard limits of six model calls, five tool calls and 4,096 completion tokens.
- The Worker fetches only the fixed AGT-ENG contract path at the authorized commit and verifies the existing T06 claim and T08 one-shot fence refs using a server-side read-only GitHub token.
- One SQLite Durable Object serializes the global dispatch ledger. Dispatch, decision, nonce, workflow run/attempt and receipt IDs are unique. Duplicate requests return existing state and never schedule a second agent run.
- The model uses Workers AI function calling with fixed tools. The model receives only tools explicitly included in the signed decision; the Worker independently validates every tool name and argument.
- Read tools: read a repository file at the signed base commit, list open PRs, inspect one PR and read commit checks. Write tools: update a restricted source/test/docs file on a deterministic per-dispatch branch and open one PR to main.
- The Durable Object records branch initialization, branch-head fencing and PR number. A write is completed only after the PR handoff is durably recorded. A write timeout or branch-head mismatch makes the dispatch uncertain; no automatic retry occurs.
- There is no merge, approval, deploy, issue/comment, shell, arbitrary URL, workflow-dispatch, policy/contract write or caller-selected endpoint tool. The agent cannot write to main.
- Ed25519 receipt v2 binds status, mission, agent, commit, dispatch ID, receipt ID and result digest. A terminal receipt embeds the separately signed accepted receipt, allowing the existing T08 bridge to verify acceptance even if the first poll arrives after completion. The Python bridge retains v1 HMAC compatibility, adds v2 Ed25519 verification, verifies the signed acceptance chain and checks returned result bytes against the signed digest. An OIDC-only HTTPS transport is available for the Worker endpoint.
- A signature authenticates the executor's assertion; it is not independent proof that the claimed engineering work occurred. The PR, branch, checks and repository state remain independently inspectable.

## Offline authorization signer

`scripts/gt47_sign_worker_decision.py` signs exactly one AGT-ENG decision with an already-existing Ed25519 PEM key. It never generates, writes, exports or uploads private keys.

The local JSON input must include task, context, commit_sha, contract_blob_sha, nonce, decision_id, issuer_key_id, issuer_human_id, max_incremental_cost_usd_micros and a non-empty allowed_tools list. max_tokens, max_model_calls and max_tool_calls have bounded defaults; write_file and open_pull_request must be authorized together.

```sh
python -m scripts.gt47_sign_worker_decision --input decision-input.json --private-key /offline/path/authority-ed25519.pem --output signed-worker-request.json
```

The output file is created exclusively with restrictive permissions; it is not committed or sent anywhere by the script. It contains task/context and the signed decision, so protect and delete it according to the data classification. The private key stays in its existing offline custody.

## AGT-ENG tool execution

The selected model, GLM-4.7-Flash, is listed as supporting Workers AI function calling (feature documented as beta): https://developers.cloudflare.com/workers-ai/features/function-calling/. Tool definitions are fixed in `src/tools.js` and filtered by the signed `allowed_tools` list.

- `read_file`: reads only from the signed base commit.
- `list_open_prs`, `get_pull_request`, `get_check_status`: read-only repository metadata.
- `write_file`: writes only under `scripts/`, `tests/`, `docs/` or `cloudflare/`, on the dispatch-specific branch. It rejects secret-like content and checks file size.
- `open_pull_request`: opens or returns the single PR from that dispatch branch to `main`; it never merges.

Writes require the optional server-side `GITHUB_WRITE_TOKEN`; the model never receives the token. The token is not configured. If a write outcome is uncertain, the execution becomes uncertain and is never retried automatically. A write-enabled run cannot be marked completed until the PR number is durably recorded.

## Paid inference cost gate

Cloudflare currently lists GLM-4.7-Flash at **$0.0605 per million input tokens** and **$0.40 per million output tokens** (official model page: https://developers.cloudflare.com/workers-ai/models/glm-4.7-flash/). This is a paid model; no free-tier assumption is made. Prices and account entitlements can change.

Before inference, the Worker estimates an upper bound from the canonical UTF-8 prompt bytes (up to 120,000 bytes, including framing/tool schemas) and maximum completion tokens. The signed decision must carry a positive `max_incremental_cost_usd_micros` within the separately configured `MAX_EXECUTION_COST_USD_MICROS` ceiling, with `AI_COST_AUTHORIZED=true`. The signer and Worker require budget for the worst-case prompt bound across all signed model calls. The maximum is four model calls and three tool calls. Cost authorization is false and the ceiling is zero by default. This estimate is a preflight guard, not an invoice guarantee; account quotas, billing, current model pricing and actual usage still require operator verification.

## Routes

- `POST /v1/gt47/dispatch`: authenticated dispatch; reserves one execution and returns a signed received receipt.
- `GET /v1/gt47/receipts/{receipt_id}`: signed current state and result, plus branch/PR reconciliation metadata.
- `GET /v1/gt47/status?dispatch_id={sha256}`: status reconciliation. A received or accepted execution older than five minutes becomes uncertain; no retry occurs.
- `GET /health`: static health-only response, not readiness or execution proof.

## Bindings and secrets not configured

The caller-side T08 reservation/fence still requires an authorized GitHub Contents:write transport to create two durable Git refs. That permission is not granted by this package and has not been configured. The Worker receives only a short-lived GitHub Actions OIDC JWT; its GitHub API read token is a separate secret used for contract/ref reads. An optional GitHub write token is required for the signed write tools. No token is sent to the model.

The historical claim hash intentionally preserves the pre-transfer repository identity `gentestsai-sudo/gentests-os` from T06. Do not change that namespace without a reviewed migration, or existing claims could be bypassed. Effective protection against deletion/repointing of these Git refs remains unverified; no protection is assumed.

Required bindings/secrets when separately authorized: Durable Object `LEDGER`, Workers AI `AI`, `OIDC_AUDIENCE`, `EXPECTED_WORKFLOW_REF`, `ALLOWED_WORKFLOW_SHAS`, `EXPECTED_ACTOR_ID`, `AUTHORIZED_ISSUER_ID`, `AUTHORITY_KEY_ID`, `AUTHORITY_PUBLIC_KEY_B64` (raw Ed25519 public key), `RECEIPT_PRIVATE_KEY_PKCS8_B64` (PKCS#8 private key), `GITHUB_READ_TOKEN` (read-only), optional `GITHUB_WRITE_TOKEN` (Contents:write and Pull requests:write only; no Actions/admin/merge scope), `AI_COST_AUTHORIZED` and `MAX_EXECUTION_COST_USD_MICROS`.

Wrangler defaults remain `AI_ENABLED=false`, `AI_COST_AUTHORIZED=false`, `MAX_EXECUTION_COST_USD_MICROS=0` and `KILL_SWITCH=on`. Do not put private keys, tokens, endpoints or Cloudflare API credentials in source or issue text.

## Limits and remaining gates

1. The current AGT-ENG contract frontmatter says `status: proposta`. It is pinned as instruction data, not treated as permission or policy approval.
2. The Worker and Durable Object have not been deployed or exercised in Cloudflare. There is no live OIDC/JWKS, real-key, Workers AI, Durable Object restart, concurrency, timeout or recovery evidence.
3. No GitHub read/write token, signing key, Cloudflare account binding, quota or cost budget has been configured. No external permission or ACL was changed.
4. Independent security review and QA of a deployed sandbox are required before activation.
5. The one-shot T06/T08 fence and branch-head CAS are fail-closed. Uncertain outcomes are reconciled manually; no retry is issued.
6. This code does not prove work independently. A completed result is accompanied by a signed digest, a branch/PR reference and CI evidence where available.

Local checks: `npm test` and `python -m unittest discover -s tests`. Source tests are not Cloudflare integration tests.