# CommentaryStrategies OxAlpha code-review roadmap

_Created: 26-08-2026 · Last updated: 26-08-2026_

Owner: H3551 (OxAlpha) — CommentaryStrategies 30-day risk-ranked code review and future independent review gate; intended executor OxAlpha (x-preview-f-free).

## Wave 0 — adapter

Add canonical GitHub tracker, default labels, PR intake OFF, single-context domain docs, and an in-place Agent skills block. Merge setup alone.

## Wave 1 — retrospective

Rank fixed-window PRs by executable and critical-path risk; retain at most ten; exclude generated/vendor/data-only changes unless behavior changed; run separate Standards and Spec passes; publish one evidence ledger without reranking axes.

## Wave 2 — urgent fixes

Reproduce candidates, discard unproven claims, and merge only minimal regression-tested P0/P1 repairs.

## Wave 3 — future gate

Design executable-path filtering, independent OxAlpha review, extra human approval for security/production paths, failure policy, rollout, observability, and rollback. Do not activate it.

## Non-goals

No P2/P3 repair, generated-data rewrite, deployment, workflow activation, or branch-protection mutation.

_Dr. Mārcis Gasūns_
