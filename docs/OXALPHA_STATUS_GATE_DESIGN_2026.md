# Future OxAlpha independent status gate — REQUIRED (live)

_Created: 03-09-2026 · Last updated: 03-09-2026_
Handoff: [Uprava H3551](https://github.com/gasyoun/Uprava/blob/main/handoffs/H3551-OxAlpha_CommentaryStrategies_oxalpha-30d-risk-review-gate_26.08.26.md) (Wave 3) · Plan decision #12 said "design, do not enable" — **overruled by activation rulings the same day**: MG «flip on» (03-09, steps 1–2) and MG «required now» (03-09, steps 3–4, wedge understood).

> **STATE: REQUIRED & LIVE.** `oxalpha-review` is a required commit-status
> context on `main` (strict, enforce_admins). Consequences every agent must
> know: **`main` is PR-only** — a direct push is rejected because the required
> status never ran on it. An in-scope PR arms `pending` (merge blocked) and an
> **OxAlpha session** must run the independent 2-axis pass and record the
> verdict with [scripts/oxalpha_gate.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/oxalpha_gate.py)
> `verdict --pr N --verdict pass|fail|neutral --evidence <url>`. Docs/data-only
> PRs arm `success` automatically (evidenced skip). `neutral` = infra
> unavailable = **blocks** until retried — never a silent pass.

**Status: DESIGN ONLY. Nothing in this document was enabled.** No workflow file, branch-protection rule, or required status check was created, modified, or scheduled by this handoff — verified by the PR manifests of [#213](https://github.com/gasyoun/CommentaryStrategies/pull/213) and [#214](https://github.com/gasyoun/CommentaryStrategies/pull/214) (docs, labels, one JS/PY fix pair; zero `.github/` changes beyond none).

## 1. What the gate is for

Retrospective review (the [30-day evidence report](https://github.com/gasyoun/CommentaryStrategies/blob/main/reports/OXALPHA_30D_CODE_REVIEW_2026-08-26.md)) found its one P1 inside the highest-risk slice (review-api draft concurrency) — exactly the class a pre-merge independent pass would have caught. The gate makes that pass routine instead of retrospective, without adding a human bottleneck to every docs/data PR.

## 2. Executable-code matching (which PRs the gate applies to)

A PR is **in scope** when its changed files, minus exclusions, are non-empty:

- **Include:** `scripts/**`, `review-api/**` (src + test), `js/**`, `review-tests/**`, `mahabharata-nilakantha/**/*.py`, `.github/workflows/**`, `css/**`.
- **Exclude:** `data/**` (generated or vote artifacts — CI's reproducibility gate already covers regeneration), `docs/**`, `*.md`, `tei/**`, `pages/**`, `reports/**`, `votes/**`, `.ai_state.md`, `changelog*`.
- The matcher is a committed script (`tools/gate_needs_review.py --pr <n> --json`), so scope is derivable and auditable, not prose. A PR with an empty in-scope set skips the gate (docs-only / data-only PRs stay fast).

## 3. The independent check (OxAlpha review as a required status check)

1. Trigger: `pull_request` (opened/synchronize/reopened) + 30-min sweep + `workflow_dispatch`, scoped by the §2 matcher.
2. Arming (`ensure`, CI + sweep): an in-scope PR head gets status `oxalpha-review` = **pending** (merge blocked) plus a review-request comment naming the in-scope files and the exact verdict command; a docs/data-only head gets **success** with the skip evidenced. A new push re-arms pending (new SHA = new review).
3. Terminal verdict (`verdict`, OxAlpha session only, after the independent 2-axis pass) — exactly one of (never a silent pass):
   - `pass` → **success** — no P0/P1 findings; `--evidence` URL mandatory;
   - `fail` → **failure** — ≥1 finding with severity ≥ P1, each carrying file/line, failure mode, and repro/test (findings missing any of the four are comments, never a fail);
   - `neutral` → **error** — infrastructure unavailable; **blocks merge until retried**.
4. The status context is `oxalpha-review`, independent of CI's existing jobs — a CI green never substitutes for it. A terminal status is immutable for that SHA; a new commit re-opens review.

## 4. Human approval layer (decision #13)

Single-author constraint: every PR in this repo is authored under the owner's
account, and GitHub forbids self-approval — so a blanket required-approving-review
is unimplementable here (it would make every PR permanently unmergeable). The
§4 layer therefore lands as:

- `enforce_admins: true` on the required `oxalpha-review` status — the gate
  binds the owner's merges too, not only agents';
- the review-request comment on every in-scope PR names the security/production
  paths explicitly (§2's `review-api/**`, `.github/workflows/**`, scrapers,
  release-cut commits) so the human sees the elevated-risk flag at merge time;
- **the merge act itself is the recorded human approval** — the gate never
  merges, a human does.

## 5. Finding bar inside the gate (same as the retrospective)

Severity, exact location, demonstrable failure mode, repro/test — no proof, no finding. P2/P3 leave comments; only P0/P1 fail the check. Stop after four repair attempts per finding, then `neutral` + human handoff.

## 6. Rollout (executed 03-09-2026, accelerated by ruling)

| Step | Action | State |
|---|---|---|
| 1 | Land the matcher + gate workflow | **DONE** — [scripts/gate_needs_review.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/gate_needs_review.py), [PR #216](https://github.com/gasyoun/CommentaryStrategies/pull/216) |
| 2 | Shadow mode on `pull_request` | **DONE (superseded same day)** — shadow ran on [PR #216](https://github.com/gasyoun/CommentaryStrategies/pull/216) itself (2/4 files in scope); replaced hours later by the required state per «required now» |
| 3 | Required `oxalpha-review` on `main` (strict, enforce_admins) + arm/verdict machinery | **DONE** — [scripts/oxalpha_gate.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/oxalpha_gate.py) (`ensure`/`verdict`/`sweep`), 30-min sweep covers dependabot's read-only token gap; protection flipped after the machinery merged |
| 4 | §4 human-approval layer | **DONE as adapted** — see §4 (self-approval constraint) |

## 7. Rollback

Uncheck the required-status flag (and `enforce_admins`) — the repo returns to CI-only merging; workflow file deletes without residue (no webhooks, no App installations, no stored state; statuses on old SHAs are inert). The review lane holds no secrets beyond the workflow token, scoped to `contents: read` + `pull_requests: write` + `statuses: write`.

## 8. Observability

- Per-run: in-scope file list, verdict, findings count by severity, wall time — appended to the run summary (no new telemetry store).
- Quarterly: findings-per-slice counts roll into the retrospective report so the gate's own value stays measured, not assumed.

## 9. Failure policy

`neutral` on infra failure (never silent pass); gate scope changes require the §4 human-approval class themselves (the workflow editing its own scope is in scope). The gate never blocks docs/data-only PRs (§2 empty in-scope set skips).

_Dr. Mārcis Gasūns_
