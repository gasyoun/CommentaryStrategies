# CommentaryStrategies reviewer platform — verification and risk register

_Created: 14-08-2026 · Last updated: 14-08-2026_

Decisions: [PLAN](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PLAN_CommentaryStrategies_review-platform_2026Q3.md).
Architecture: [ARCHITECTURE](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ARCHITECTURE_CommentaryStrategies_review-platform.md).
Build order: [IMPLEMENTATION](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/IMPLEMENTATION_CommentaryStrategies_review-platform.md).
Program: [ROADMAP](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ROADMAP_CommentaryStrategies_2026Q3.md).

## Gate verdict definition

Wave 1 passes only when every P0 criterion below is green and supported by an
exact command, test artifact, or production response. A deployed page that
cannot preserve votes, a backend that can overwrite evidence, or an unmeasured
automation class is a failure, not partial completion.

## Acceptance matrix

| ID | Priority | Criterion | Proof | Failure |
|---|---|---|---|---|
| V1 | P0 | Manifest contains exactly unique sargas 1–68 for Kostina. | Portal `--check` plus schema validation. | Gap, duplicate, wrong reviewer, or stale hash. |
| V2 | P0 | Landing page and all 68 reviewer ballots are deployed. | HTTP 200 crawl from the Pages root. | Any missing page/asset or non-200 response. |
| V3 | P0 | Tier 1 is display-only and Leonov votes are preserved. | Baseline/final count + deterministic subtree hash + ledger self-test. | Any changed/missing/reattributed Leonov field. |
| V4 | P0 | Local save survives refresh/offline and aggregate export round-trips. | Playwright desktop/mobile/offline scenarios. | Lost or mismatched decision. |
| V5 | P0 | Remote autosave is authenticated, versioned, recoverable, and free-tier. | Worker tests plus deployed synthetic session. | Silent overwrite, unauthorized read/write, secret exposure, or paid activation. |
| V6 | P0 | Final submit creates one immutable raw-submission PR, not a ledger edit. | Mocked end-to-end plus one synthetic test repository/branch flow if authorized. | Mutable path, direct ledger write, or non-idempotent double submit. |
| V7 | P0 | Raw validation rejects malformed, stale, duplicate, and misattributed payloads. | Fixture matrix. | Invalid payload passes. |
| V8 | P0 | Import is schema-v2 compatible, transactional in effect, and idempotent. | Dry-run/import/rerun fixtures. | Partial write, flattened reviewer, or changed prior evidence. |
| V9 | P0 | Disagreements and different edits become a compact queue; rejection vetoes auto-inclusion. | Agreement/queue fixtures. | Conflict silently resolves or disappears. |
| V10 | P0 | Automation fails closed below the statistical/invariant bar. | Policy validator boundary fixtures. | Any unqualified class receives `auto_apply`. |
| V11 | P0 | Corpus, URN, generated-artifact, ledger, browser, and Worker CI are green. | Required GitHub checks. | Any required check failing/skipped. |
| V12 | P0 | No real vote, reviewer contact, protected-content edit, or secret occurs. | Git diff, test interception, secret scan, audit log review. | Fence violation. |
| V13 | P1 | Keyboard, focus, labels, sync announcements, and mobile layout work. | Playwright accessibility/viewport assertions plus manual smoke. | Core action inaccessible. |
| V14 | P1 | README/manual/Kostina guide/state point to the same official flow. | Link and truth pass. | Stale counts, raw file instructions, or contradictory gate state. |

## Exact local gate

```powershell
python scripts/validate.py
python scripts/derive_urn.py --check
python scripts/gate_ledger_selftest.py
python scripts/gate_reviewer_agreement.py
python scripts/validate_adjudication_policy.py
python scripts/build_apparatus_review_portal.py --check
python scripts/validate_apparatus_submission.py tests/fixtures/apparatus_submission_valid.json
python scripts/import_apparatus_submission.py tests/fixtures/apparatus_submission_valid.json --dry-run
npm ci
npx playwright test
Push-Location review-api
npm ci
npm test
Pop-Location
git diff --check
```

The executor records versions and full exit codes. A command absent because its
file has not yet been built is not a pass.

## Browser scenario matrix

1. First load at desktop and narrow mobile widths.
2. Keyboard-only accept, edit, reject, save, navigation, export, and submit.
3. Visible focus and announced progress/sync/error changes.
4. Refresh during unsynced work; local state restores exactly.
5. Previously opened ballot while offline; edits queue and later sync.
6. Two-tab optimistic conflict; neither version silently wins.
7. Expired/invalid session; local work remains and re-auth resumes.
8. GitHub/Worker 401, 403, 409, 429, and 5xx responses; recovery is explicit.
9. Aggregate JSON equals the payload proposed for final submission.
10. Double submit returns the same immutable content identity.
11. Repository text containing markup/script-like characters renders as text.
12. Tests intercept every external write; production reviewer data is untouched.

## Submission fixture matrix

- valid complete aggregate;
- valid partial draft that cannot be finalized;
- wrong reviewer or unauthenticated login;
- wrong schema/manifest/source revision;
- missing/duplicate sarga or decision ID;
- unknown/stale note ID;
- invalid action;
- edit without edited text; reject without reason;
- mismatched content hash;
- existing raw path;
- same submission repeated;
- second reviewer accept preserving Leonov accept;
- second reviewer reject preserving Leonov accept and creating disagreement;
- two edits with different text;
- malicious HTML/control characters and oversized payload.

## Automation evidence gate

Every policy class is validated independently.

### Deterministic class

Required: frozen transformation, input/output schema, declared invariants,
adversarial fixtures, reversibility, and all invariants green. Confidence scores
cannot substitute for failed invariants.

### Agent-derived class

Required: preregistered class definition, frozen model/prompt/data revision,
blind sample, sample size/successes, confidence method, lower 95% bound, risk,
and audit/reversal path. `auto_apply` requires lower bound `>= 0.95`; equality
passes, any lower value fails. Disagreement, scholarly interpretation, uncertain
anchor, or editorial rewriting remains human escalation regardless of score.

## Production verification

After merge and deployment:

```powershell
curl.exe -I https://gasyoun.github.io/CommentaryStrategies/data/apparatus/
curl.exe -I https://gasyoun.github.io/CommentaryStrategies/data/apparatus/sarga_01_kostina.html
curl.exe -I https://gasyoun.github.io/CommentaryStrategies/data/apparatus/sarga_68_kostina.html
curl.exe -I $env:COMMENTARY_REVIEW_API_HEALTH_URL
```

Then run one synthetic account/session through login, draft save, conflict,
aggregate download, and submission into a test branch/repository. Do not submit a
synthetic ballot into the production evidence path unless it is unmistakably
namespaced and automatically rejected by the scholarly importer.

## Risks and spikes

| Risk / unknown | Pre-commit spike or control | Stop/fallback |
|---|---|---|
| Cloudflare account demands billing or exceeds Free plan | Verify dashboard plan and set CPU/request/payload limits before deployment. | Do not activate paid service; local save + aggregate download remains. |
| GitHub OAuth/App permissions are broader than needed | Create test registration, inspect requested permissions, verify allow-listed identity and installation scope. | Stop auth deployment; never use a PAT or embed a secret. |
| Reviewer lacks/does not want GitHub account | Document as human prerequisite before invitation. | Aggregate JSON path remains available; no invented identity. |
| D1 draft loss or conflict | Versioned rows, optimistic concurrency, local copy retained, export always available. | Prefer local/newer evidence and surface conflict; never overwrite. |
| Worker compromise exposes GitHub capability | Short-lived installation/user tokens, secret rotation, allow-list, rate limit, minimal app permissions. | Revoke app/session, disable API, retain static portal. |
| XSS steals session or changes votes | Shared escaping, CSP, no unsafe HTML, malicious-content browser fixtures. | P0 failure; do not deploy. |
| Generated 68-page duplication inflates repository | Shared JS/CSS and manifest; measure size in Wave 1. | Optimize generated data only without changing canonical inputs. |
| Source changes make saved IDs stale | Manifest/source hashes and park-on-stale importer. | Park affected records; continue independent records. |
| Second reviewer overwrites Leonov | Schema-v2 keyed reviewers plus subtree hash regression. | P0 failure; restore from immutable evidence and stop import. |
| Same action hides different edit text | Content-sensitive disagreement classification. | Queue both texts; no automatic winner. |
| Statistical class is tuned after seeing sample | Preregister/version class before blind scoring. | Class remains in sample/human review. |
| High accuracy masks scholarly harm | Risk exclusions override score for interpretive/editorial classes. | Human escalation. |
| Tests create real submissions | Network interception and test-only credentials/repository. | Revoke credentials/remove synthetic artifact; deployment fails. |
| Documentation again drifts | Generated-link/count checks and one official portal URL. | CI failure or queued truth-pass before release. |

## Autonomy-readiness checklist

| Wave-1 deliverable | Architecture | Ordered steps | Acceptance | Risks |
|---|---:|---:|---:|---:|
| 68-ballot portal | Yes | Steps 2–3 | V1–V4, V13 | XSS, size, offline |
| Free auth/autosave mediator | Yes | Step 4 | V5, V12 | cost, OAuth, compromise |
| Immutable GitHub submission | Yes | Steps 4–5 | V6–V8 | permissions, idempotency |
| Dual-reviewer resolution | Yes | Step 5 | V3, V9 | overwrite, hidden edit conflict |
| Automation policy | Yes | Steps 1 and 5 | V10 | tuning, scholarly harm |
| CI/docs/deployment | Yes | Steps 6–7 | V11–V14 | test writes, drift |

Gate verdict at plan time: **PASS**. All Wave-1 deliverables have boundaries,
ordered work, acceptance evidence, risk controls, a chosen ambiguity policy, and
a free-cost fallback. No blocking `@DECIDE` remains. Human account creation,
real voting, invitation delivery, and editorial disagreement resolution are
explicitly outside autonomous execution.

_Dr. Mārcis Gasūns_
