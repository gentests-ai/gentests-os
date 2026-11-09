# GT47 Cloudflare remote executor

This implementation is deliberately inert until separately provisioned and authorized. This repository change creates no Cloudflare resource, secret, key, deployment, inference or paid service.

## Runtime

- HTTPS Worker validates GitHub Actions OIDC using the fixed GitHub JWKS URL, issuer, audience, repository ID, workflow ref/SHA allowlist, main ref, event and actor.
- An independent Ed25519 decision authorizes exactly GT-AI-DISPATCH-001 / issue 47 / AGT-ENG, a pinned commit and contract blob, the task+context digest, nonce, 15-minute maximum validity, one call, <=1024 output tokens, zero incremental BRL and no paid fallback.
- The Worker fetches only the fixed AGT-ENG contract path at the authorized commit and verifies both pre-existing T06 claim and T08 one-shot fence refs using a server-side read-only GitHub token.
- One SQLite Durable Object serializes the ledger. Dispatch, decision, nonce, workflow run/attempt and receipt IDs are unique. Duplicate requests return existing state and never schedule another model call.
- Workers AI uses a fixed model and has no tools. Task/context are untrusted data. No GitHub writes, filesystem, arbitrary commands, PR operations, merge or deploy are exposed.
- Ed25519 receipt v2 binds status, mission, agent, commit, dispatch ID, receipt ID and result digest. A terminal receipt embeds the separately signed accepted receipt, allowing the existing T08 bridge to verify acceptance even if the first poll arrives after completion. The Python bridge retains v1 HMAC compatibility, adds v2 Ed25519 verification, verifies the signed acceptance chain and checks the returned result bytes against the signed digest. An OIDC-only HTTPS transport is available for the Worker endpoint. A signature authenticates the executor's assertion; it is not independent proof of work.

## Routes

- POST /v1/gt47/dispatch: authenticated dispatch; schedules one background execution and returns signed received receipt.
- GET /v1/gt47/receipts/{receipt_id}: signed current state and result.
- GET /v1/gt47/status?dispatch_id={sha256}: reconciliation. A received or accepted execution older than 2 minutes becomes uncertain; no retry occurs.
- GET /health: static health-only response, not readiness or execution proof.

## Bindings and secrets not configured

The caller-side T08 reservation/fence still requires an authorized GitHub Contents:write transport to create two durable Git refs. That permission is not granted by this package and has not been configured. The Worker receives only a short-lived GitHub Actions OIDC JWT; its GitHub API token is a separate read-only secret used only for contract/ref reads. No GitHub write token is sent to the Worker or model.

The historical claim hash intentionally preserves the pre-transfer repository identity gentestsai-sudo/gentests-os from T06. Do not change that namespace without a reviewed migration, or existing claims could be bypassed. Effective protection against deletion/repointing of these Git refs remains unverified; no protection is assumed.


Durable Object LEDGER, Workers AI AI, OIDC_AUDIENCE, EXPECTED_WORKFLOW_REF, ALLOWED_WORKFLOW_SHAS, EXPECTED_ACTOR_ID, AUTHORIZED_ISSUER_ID, AUTHORITY_KEY_ID, AUTHORITY_PUBLIC_KEY_B64 (raw Ed25519 public key), RECEIPT_PRIVATE_KEY_PKCS8_B64 (PKCS#8 private key), and GITHUB_READ_TOKEN (read-only for this private repo).

AI_ENABLED remains false and KILL_SWITCH remains on until separate activation authorization, account/quota/cost verification, and QA of a deployed sandbox. Do not put private keys, tokens, endpoints or Cloudflare API credentials in source or issue text.

## Limits

1. The current AGT-ENG contract frontmatter says status: proposta. It is pinned as instruction data, not treated as permission or policy approval.
2. The T08 bridge can submit its existing reserved intent through the new OIDC transport using a separately signed Worker request. This vertical invokes a bounded Workers AI text model; it is not a ChatGPT session or fully tool-enabled coding agent. It cannot edit repository files or perform GitHub actions.
3. The global ledger is intentionally serialized for the pilot. Sharding needs a separate uniqueness design.
4. A stuck accepted run becomes uncertain; no automatic recovery or retry is allowed because inference may already have occurred.
5. The v2 receipt wire format and OIDC transport are integrated into the T08 Python bridge without removing v1 HMAC compatibility. Received/accepted jobs that exceed the reconciliation window are marked uncertain with a signed receipt; no retry is issued. CI must validate the new cross-language signature, transport and bridge tests. This code has not been run in Cloudflare, against live JWKS/OIDC, real keys, Workers AI or a deployed Durable Object.

Local test command: npm test. These source contract checks are not cloud integration tests.
