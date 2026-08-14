# CommentaryStrategies reviewer platform — Wave-1 implementation

_Created: 14-08-2026 · Last updated: 14-08-2026_

Canonical rulings: [PLAN](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PLAN_CommentaryStrategies_review-platform_2026Q3.md).
Boundaries: [ARCHITECTURE](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ARCHITECTURE_CommentaryStrategies_review-platform.md).
Acceptance: [VERIFICATION](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/VERIFICATION_CommentaryStrategies_review-platform.md).
Follow-on waves: [ROADMAP](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ROADMAP_CommentaryStrategies_2026Q3.md).

## Wave-1 outcome

In one 5–8-hour autonomous build, extend the existing apparatus into an official
68-sarga Kostina review portal, add free-tier authenticated draft/submission
transport, preserve immutable evidence, and prove the complete flow with
synthetic data. Infrastructure only: no real votes, reviewer contact, tier-1
content edits, article edits, or editorial resolution.

## Ordered build sequence

### Step 0 — isolate and baseline (20–30 minutes)

Dependencies: none.

1. Work in a linked branch/worktree; re-read the nearest `.ai_state.md` WIP.
2. Record `git status`, current commit, schema version, existing Leonov verdict
   count, and a deterministic hash of the full `verdicts["Леонов"]` subtree.
3. Run the current gates before editing.

```powershell
python scripts/validate.py
python scripts/gate_ledger_selftest.py
python scripts/gate_reviewer_agreement.py
git diff --check
```

Touch: no tracked file. Store the baseline only in test output/implementation
notes, never by rewriting the ledger.

Acceptance: clean baseline or a precisely logged pre-existing failure. Any
concurrent WIP on this subsystem moves execution to a fresh worktree.

### Step 1 — freeze schemas and policies (35–50 minutes)

Dependencies: Step 0.

Add:

- `data/apparatus/reviewer_manifest.schema.json`
- `data/apparatus/submission.schema.json`
- `data/apparatus/adjudication_policy.json`
- `scripts/validate_adjudication_policy.py`
- `votes/submissions/README.md`

Modify:

- `scripts/gate_ledger.py`
- `scripts/gate_ledger_selftest.py`

Contracts to encode:

- manifest contains exactly unique sargas 1–68, reviewer, repo/data revisions,
  counts, and hashes;
- raw submission is create-only and content-addressed;
- policy classes declare risk, evidence revision, action, invariants or blind
  sample statistics, and lower 95% bound;
- schema v2 remains unchanged in meaning; reviewer verdicts never flatten;
- agent-derived `auto_apply` fails unless preregistered lower bound is at least
  0.95; deterministic `auto_apply` fails any invariant error.

Acceptance: boundary fixtures below/at/above 0.95, unknown class, changed class
definition, missing evidence, and schema-v1 overwrite all fail as designed.

### Step 2 — extract the shared ballot client (60–75 minutes)

Dependencies: Step 1.

Add:

- `css/apparatus-review.css`
- `js/apparatus-review.js`
- `js/review-sync.js`

Modify:

- `scripts/build_sarga_apparatus.py`

Preserve existing source assembly. Move repeated inline style/interaction code
to shared assets while keeping reviewer identity and sarga data embedded or
loaded from generated JSON. Add a build-all mode and stable reviewer suffix.

Client requirements:

- reviewer + manifest-revision + sarga scoped localStorage key;
- accept/edit/reject validation and edit/reject text requirements;
- progress and accessible live-region status;
- local, syncing, synced, offline, conflict, submitted states;
- aggregate export with no token/session material;
- tier 1 display-only; Leonov verdicts visible and immutable;
- strict escaping/no unsafe insertion of repository text.

Acceptance: sarga 1 regenerated without loss of data/function; a second build is
byte-stable; no tier-1 control exists.

### Step 3 — generate the official 68-sarga portal (50–70 minutes)

Dependencies: Step 2.

Add:

- `scripts/build_apparatus_review_portal.py`
- `data/apparatus/index.html`
- `data/apparatus/reviewer_manifest.json`
- `data/apparatus/review.webmanifest`
- `data/apparatus/review-sw.js`

Generate:

- `data/apparatus/sarga_01_kostina.html` through
  `data/apparatus/sarga_68_kostina.html` and their data companions.

The landing page presents all 68 sargas, local/synced completion, one aggregate
download, login/sync controls, recovery instructions, and a plain warning that
final submission is explicit. Cache the application shell and previously opened
ballots; never promise unsynced remote availability.

```powershell
python scripts/build_sarga_apparatus.py 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 --reviewer "Костина"
python scripts/build_apparatus_review_portal.py
python scripts/build_apparatus_review_portal.py --check
```

Acceptance: manifest is exactly 1–68 with no gap/duplicate; each ballot declares
Kostina and a unique key; aggregate export round-trips all sargas.

### Step 4 — implement the free mediator and draft store (75–105 minutes)

Dependencies: schemas and stable aggregate shape.

Add:

- `review-api/wrangler.jsonc`
- `review-api/package.json`
- `review-api/src/index.js`
- `review-api/src/auth.js`
- `review-api/src/drafts.js`
- `review-api/src/submit.js`
- `review-api/migrations/0001_initial.sql`
- `review-api/test/worker.test.js`

Cloudflare setup:

- Workers Free and D1 Free only; no paid-plan switch or payment activation;
- exact Pages origin allow-list;
- GitHub App/OAuth client secret and App private key only as Cloudflare secrets;
- allow-list Kostina's confirmed GitHub login in encrypted/configured service
  state, not guessed from her name;
- short-lived HttpOnly/Secure/SameSite session; state + PKCE/CSRF checks;
- indexed D1 draft key: reviewer, manifest revision, sarga;
- optimistic versioning; conflicts return both versions and never overwrite;
- rate limits, payload limits, structured secret-free logs.

Endpoints:

- `GET /auth/start`, `GET /auth/callback`, `POST /auth/logout`
- `GET/PUT /drafts/:revision/:sarga`
- `POST /submissions`
- `GET /health` without sensitive configuration

The final endpoint verifies session, schema, manifest/source hashes, and content
hash; then uses the GitHub App installation token to create a new raw-submission
branch/PR. It cannot edit the canonical ledger.

Acceptance: local Worker tests cover invalid origin/state/login/session, stale
draft version, oversized payload, double submit, GitHub 401/403/409/429/5xx, and
free-limit fallback. No secret appears in Git or browser output.

### Step 5 — raw validation, trusted import, and disagreement queue (60–90 minutes)

Dependencies: stable submission schema.

Add:

- `scripts/validate_apparatus_submission.py`
- `scripts/import_apparatus_submission.py`
- `scripts/build_gate_disagreement_queue.py`
- `tests/fixtures/apparatus_submission_valid.json`
- `tests/fixtures/apparatus_submission_invalid_*.json`

Modify:

- `scripts/apply_apparatus_decisions.py`
- `scripts/gate_reviewer_agreement.py`
- `scripts/gate_ledger_selftest.py`

Validate reviewer identity, schema, hashes, unique IDs, allowed actions,
required text, sarga coverage, and immutability. Validate everything before one
ledger write. Park stale/unknown items with evidence while continuing independent
valid items. Preserve the legacy single-sarga path behind an explicit mode.

Derived outcome rules:

- accept/accept eligible;
- reject/reject excluded;
- any action disagreement or differing edit text queued;
- any reject vetoes automatic inclusion pending resolution;
- a missing second vote remains pending.

Acceptance: importing a synthetic Kostina submission leaves the baseline Leonov
count, values, timestamps, and hash unchanged; rerun is idempotent; disagreement
JSON/HTML is deterministic.

### Step 6 — CI and browser verification (60–90 minutes)

Dependencies: Steps 2–5.

Add:

- `package.json` and locked browser-test dependencies at repository root if not
  already present;
- `playwright.config.js`
- `tests/review-platform.spec.js`

Modify:

- `.github/workflows/ci.yml`

Blocking checks:

1. corpus and URN integrity;
2. schema-v2 ledger self-tests and Leonov losslessness fixture;
3. 68-ballot/manifest deterministic rebuild;
4. raw submission and adjudication policy validation;
5. keyboard/mobile/local-resume/offline/sync-state browser tests;
6. mocked OAuth, autosave, conflict, final-submit, PR, and failed-network flows;
7. PRs touching `votes/submissions/**` validate create-only raw evidence.

Tests must intercept GitHub/Cloudflare writes and can never submit real votes.

### Step 7 — synchronize documentation and deploy (45–60 minutes)

Dependencies: green verification.

Modify together:

- `README.md`
- `docs/MANUAL.md`
- `docs/KOSTINA_SUNDARAKANDA_GUIDE.md`
- affected companion metadocs
- `.ai_state.md`
- `changelog.md`

Replace raw repository navigation with the official Pages portal; explain login,
local/remote save, aggregate fallback, explicit submit, recovery, privacy, and
the fact that the executor does not contact reviewers.

Deploy the Worker Free project and D1 migrations, configure secrets without
printing them, merge only with green checks, then verify Pages/API. If free-tier
deployment requires billing or security acceptance fails, do not deploy the API;
ship the Pages/local/download path and record the parked hosted feature.

## Verification command set

```powershell
python scripts/validate.py
python scripts/derive_urn.py --check
python scripts/gate_ledger_selftest.py
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

Production smoke checks:

```powershell
curl.exe -I https://gasyoun.github.io/CommentaryStrategies/data/apparatus/
curl.exe -I https://gasyoun.github.io/CommentaryStrategies/data/apparatus/sarga_68_kostina.html
curl.exe -I $env:COMMENTARY_REVIEW_API_HEALTH_URL
```

## Commit boundaries

Use targeted micro-commits after: contracts/baseline; shared client + portal;
Worker + D1 tests; validator/importer; browser/CI; documentation/deployment.
Never stage unrelated changes. Final PR may merge only when the full acceptance
matrix in [VERIFICATION](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/VERIFICATION_CommentaryStrategies_review-platform.md)
passes.

## Explicitly outside Wave 1

- real Kostina submissions or votes;
- reviewer outreach;
- resolving actual Leonov–Kostina disagreements;
- changing tier-1 text, articles, rights, or analytical axes;
- declaring an agent class eligible without required evidence;
- paid hosting or a different provider;
- framework migration or replacement of existing apparatus generators.

_Dr. Mārcis Gasūns_
