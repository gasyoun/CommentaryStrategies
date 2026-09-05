_Created: 14-08-2026 · Last updated: 05-09-2026_

# H2736 review-platform production gate — 2026-08-14

## Verdict

**GO for the static Kostina review portal and fail-closed local workflow.**

**PARKED for the optional hosted autosave/submission mediator.** The Worker bundle,
D1 migration, OAuth/CSRF/session controls, immutable-submission tests, and Wrangler
Free-plan dry run pass, but deployment requires a human-authenticated Cloudflare
account, GitHub OAuth/App configuration, allowlist, and secrets. No credential was
available or created during this run. The supported fallback remains local save plus
aggregate JSON download/import; no reviewer data is lost or silently submitted.

This split verdict is intentional: the optional mediator cannot block publication of
the static portal, and it cannot be represented as deployed until the human setup is
complete.

## Acceptance matrix

| Axis | Result | Evidence |
|---|---|---|
| 68-sarga static portal | PASS | Manifest and generated-artifact validators pass for exactly 68 Kostina ballots; sarga 1 and 68 are covered by browser tests. |
| Reviewer usability/offline behavior | PASS | Playwright: 10/10 desktop/mobile tests pass, including save, reload, export, and offline fallback. |
| Ledger and conservative policy | PASS | Corpus, URN, ledger, manifest, submission, import, disagreement-queue, and lower-95%-bound boundary self-tests pass. The automation bar remains locked at 0.95. |
| Leonov preservation | PASS | 126 existing verdicts; deterministic subtree SHA-256 before and after: `91414d11045c4fce625b196ac564bde8fc4184dcfa62253cb26b29449fcc07b2`. |
| Worker/D1 implementation | PASS (offline) | Worker tests: 6/6; Wrangler `deploy --dry-run`: PASS. GitHub App installation-token flow uses an app JWT and no PAT. |
| Hosted Worker deployment | PARKED | `wrangler whoami` reports no authenticated account. Human-owned Free-plan/App configuration is required. |
| Repository CI | PASS | All repository-owned PR checks pass, including Review platform contracts, Python matrix, corpus integrity, formatting, and CodeQL. |
| Cloudflare repository integration | PRE-EXISTING FAILURE | `Workers Builds: commentarystrategies` also fails on untouched base commit `0f2cfdfe1a22012b271f6eb51545dd89bd5cf0c8`; it is not a regression from H2736. GitHub Pages is the static publication target. |

## Reproduction commands

```text
python scripts/validate.py
python scripts/gate_ledger_selftest.py
python scripts/gate_policy_selftest.py
python scripts/validate_reviewer_manifest.py data/apparatus/reviewer_manifest.json
python scripts/validate_submission.py tests/fixtures/submission_valid.json
python scripts/import_reviewer_submission.py tests/fixtures/submission_valid.json --check
python scripts/build_disagreement_queue.py --check
python scripts/review_platform_selftest.py
cd review-tests && npm ci && npx playwright test
cd review-api && npm ci && npm test
cd review-api && npx wrangler deploy --dry-run
```

## Provenance and exclusions

Executing model: **Codex GPT-5**. PR: [#167](https://github.com/gasyoun/CommentaryStrategies/pull/167).

No real reviewer vote, reviewer outreach, secret creation, paid Cloudflare feature,
tier-1/article/four-axis edit, Leonov verdict change, or production Worker deployment
was performed. The final hosted check after merge covers GitHub Pages only.

_Dr. Mārcis Gasūns_
