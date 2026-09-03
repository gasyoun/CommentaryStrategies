# Future OxAlpha independent status gate — design (NOT enabled)

_Created: 03-09-2026 · Last updated: 03-09-2026_
Handoff: [Uprava H3551](https://github.com/gasyoun/Uprava/blob/main/handoffs/H3551-OxAlpha_CommentaryStrategies_oxalpha-30d-risk-review-gate_26.08.26.md) (Wave 3) · Plan decision #12: **design but do not enable**; plan decision #13: human approval additionally covers security/production paths.

**Status: DESIGN ONLY. Nothing in this document was enabled.** No workflow file, branch-protection rule, or required status check was created, modified, or scheduled by this handoff — verified by the PR manifests of [#213](https://github.com/gasyoun/CommentaryStrategies/pull/213) and [#214](https://github.com/gasyoun/CommentaryStrategies/pull/214) (docs, labels, one JS/PY fix pair; zero `.github/` changes beyond none).

## 1. What the gate is for

Retrospective review (the [30-day evidence report](https://github.com/gasyoun/CommentaryStrategies/blob/main/reports/OXALPHA_30D_CODE_REVIEW_2026-08-26.md)) found its one P1 inside the highest-risk slice (review-api draft concurrency) — exactly the class a pre-merge independent pass would have caught. The gate makes that pass routine instead of retrospective, without adding a human bottleneck to every docs/data PR.

## 2. Executable-code matching (which PRs the gate applies to)

A PR is **in scope** when its changed files, minus exclusions, are non-empty:

- **Include:** `scripts/**`, `review-api/**` (src + test), `js/**`, `review-tests/**`, `mahabharata-nilakantha/**/*.py`, `.github/workflows/**`, `css/**`.
- **Exclude:** `data/**` (generated or vote artifacts — CI's reproducibility gate already covers regeneration), `docs/**`, `*.md`, `tei/**`, `pages/**`, `reports/**`, `votes/**`, `.ai_state.md`, `changelog*`.
- The matcher is a committed script (`tools/gate_needs_review.py --pr <n> --json`), so scope is derivable and auditable, not prose. A PR with an empty in-scope set skips the gate (docs-only / data-only PRs stay fast).

## 3. The independent check (OxAlpha review as a required status check)

1. Trigger: `pull_request` (types: opened, synchronize) + `workflow_dispatch`, scoped by the §2 matcher.
2. The workflow job posts a machine-readable review request (PR diff, in-scope file list, repo rules excerpt from `docs/agents/` + CLAUDE.md hard rules) to the OxAlpha lane and awaits a structured verdict.
3. The check returns exactly one of three conclusions (plan contract: never a silent pass):
   - `pass` — no P0/P1 findings on the executable diff;
   - `fail` — ≥1 finding with severity ≥ P1, each carrying file/line, failure mode, and repro/test (findings without all four are reported as comments, never as fail);
   - `neutral` — infrastructure unavailable (runner/API down). **Never** mapped to pass; the PR simply cannot merge while neutral, and the job marks itself retried.
4. Findings post as a single PR comment (one finding per heading, the §5 bar verbatim), and the check name is `oxalpha-review` (independent of CI's existing jobs, so a CI green never substitutes for it).

## 4. Human approval layer (decision #13)

Even with `oxalpha-review` green, a PR additionally requires a human `review` approval when its in-scope diff touches any of:

- `review-api/**` (authentication, sessions, submissions — security surface),
- `.github/workflows/**` (CI/CD mutation),
- anything writing outside the repo (scrapers: `mahabharata-nilakantha/**`, `scripts/scrape_*.py`, `scripts/yadisk_inventory.py`),
- `CHANGELOG.md` release-cut commits (production-versioning path).

This is the GitHub required-approval, not a second bot: model review is not release accountability.

## 5. Finding bar inside the gate (same as the retrospective)

Severity, exact location, demonstrable failure mode, repro/test — no proof, no finding. P2/P3 leave comments; only P0/P1 fail the check. Stop after four repair attempts per finding, then `neutral` + human handoff.

## 6. Rollout (when a human decides to enable)

| Step | Action | Reversible by |
|---|---|---|
| 1 | Land `tools/gate_needs_review.py` + the workflow file with `if: false` guard, run only via `workflow_dispatch` | delete branch |
| 2 | Two weeks shadow mode on `pull_request` (report-only comment, check always `neutral`) | flip the guard |
| 3 | Flip `oxalpha-review` to required on `main` (branch protection) | uncheck required |
| 4 | Add the §4 human-approval ruleset | uncheck approval |

## 7. Rollback

Removing the required-check flag restores merge-on-CI alone; the workflow file deletes without residue (no webhooks, no App installations, no stored state). The review lane holds no secrets beyond the existing Actions token scope, scoped to `contents: read` + `pull_requests: write` for comments.

## 8. Observability

- Per-run: in-scope file list, verdict, findings count by severity, wall time — appended to the run summary (no new telemetry store).
- Quarterly: findings-per-slice counts roll into the retrospective report so the gate's own value stays measured, not assumed.

## 9. Failure policy

`neutral` on infra failure (never silent pass); gate scope changes require the §4 human-approval class themselves (the workflow editing its own scope is in scope). The gate never blocks docs/data-only PRs (§2 empty in-scope set skips).

_Dr. Mārcis Gasūns_
