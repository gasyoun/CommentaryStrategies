# CommentaryStrategies OxAlpha code-review implementation

_Created: 26-08-2026 · Last updated: 26-08-2026_

## Ordered sequence

1. Create a fresh worktree from origin/main; read [agent instructions](https://github.com/gasyoun/CommentaryStrategies/blob/main/CLAUDE.md), state, README, changelog, CI, and relevant plans.
2. Add canonical files under [docs/agents](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/agents), update the existing instruction file, preserve PR intake OFF, create only missing canonical labels, and merge this PR alone.
3. Validate and rank candidate slices #167, #170, #159, #183, #185, #178, #182, #175, #194, #181; replace any out-of-window or non-executable candidate without exceeding ten.
4. Fetch PR body, commits, files, issues, base SHA, and head SHA; resolve the Spec source in the ruled order.
5. Run independent bounded passes. Focus: review-api authentication and submission, review portal/sync JavaScript, apparatus portal builders, gate ledger, sarga apparatus, alignment, transliteration, and review-sheet generators.
6. Publish [the evidence report](https://github.com/gasyoun/CommentaryStrategies/blob/main/reports/OXALPHA_30D_CODE_REVIEW_2026-08-26.md) with separate axes, explicit exclusions, and no-spec outcomes.
7. For each proven P0/P1, add an adjacent regression test, make the smallest repair, run focused and repository gates, and merge a minimal green PR.
8. Write [the future-gate design](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/OXALPHA_STATUS_GATE_DESIGN_2026.md); do not alter live protection or workflows.
9. Update changelog/state and close only when adapter, report, applicable fixes, and design exist.

_Dr. Mārcis Gasūns_
