# GT47 Cloudflare remote executor

This implementation is deliberately inert until separately provisioned and authorized. This repository change creates no Cloudflare resource, secret, key, deployment, inference or paid service.

## Runtime

- HTTPS Worker validates GitHub Actions OIDC using the fixed GitHub JWKS URL, issuer, audience, repository ID, workflow ref/SHA allowlist, main ref, event and actor.
- An independent Ed25519 decision authorizes exactly GT-AI-DISPATCH-001 / issue 47 / AGT-ENG, a pinned commit and contract blob, the task+context digest, nonce, 15-minute maximum validity, one call, <=1024 output tokens, zero incremental BRL and no paid fallback.
- The Worker fetches only the fixed AGT-ENG contract path at the authorized commit, using a server-side read-only GitHub token.
- One SQLite Durable Object serializes the ledger. Dispatch, decision, nonce, workflow run/attempt and receipt IDs are unique. Duplicate requests return existing state and never schedule another model call.
- Workers AI uses a fixed model and has no tools. Task/context are untrusted data. No GitHub writes, filesystem, arbitrary commands, PR operations, merge or deploy are exposed.
- Ed25519 receipts bind status, mission, agent, commit, dispatch ID, receipt ID and result digest. A signature authenticates the executor's assertion; it is not independent proof of work.

## Routes

- POST /v1/gt47/dispatch: authenticated dispatch; schedules one background execution and returns signed received receipt.
- GET /v1/gt47/receipts/{receipt_id}: signed current state and result.
- GET /v1/gt47/status?dispatch_id={sha256}: reconciliation. An accepted execution older than 2 minutes becomes uncertain; no retry occurs.
- GET /health: static health-only response, not readiness or execution proof.

## Bindings and secrets not configured

Durable Object LEDGER, Workers AI AI, OIDC_AUDIENCE, EXPECTED_WORKFLOW_REF, ALLOWED_WORKFLOW_SHAS, EXPECTED_ACTOR_ID, AUTHORIZED_ISSUER_ID, AUTHORITY_KEY_ID, AUTHORITY_PUBLIC_KEY_B64 (raw Ed25519 public key), RECEIPT_PRIVATE_KEY_PKCS8_B64 (PKCS#8 private key), and GITHUB_READ_TOKEN (read-only for this private repo).

AI_ENABLED remains false and KILL_SWITCH remains on until separate activation authorization, account/quota/cost verification, and QA of a deployed sandbox. Do not put private keys, tokens, endpoints or Cloudflare API credentials in source or issue text.

## Limits

1. The current AGT-ENG contract frontmatter says status: proposta. It is pinned as instruction data, not treated as permission or policy approval.
2. This vertical invokes a bounded Workers AI text model; it is not a ChatGPT session or fully tool-enabled coding agent. It cannot edit repository files or perform GitHub actions.
3. The global ledger is intentionally serialized for the pilot. Sharding needs a separate uniqueness design.
4. A stuck accepted run becomes uncertain; no automatic recovery or retry is allowed because inference may already have occurred.
5. This code and its tests have not been run in Cloudflare, against live JWKS/OIDC, real keys, Workers AI or a deployed Durable Object.

Local test command: npm test. These source contract checks are not cloud integration tests.
