# CommentaryStrategies OxAlpha code-review hardening plan

_Created: 26-08-2026 · Last updated: 26-08-2026_

Goal: give H3551 (OxAlpha) — CommentaryStrategies 30-day risk-ranked code review and future independent review gate an unattended route from canonical tracker setup through bounded retrospective review, urgent evidence-backed repair, and an inactive future review-gate design.

## Decisions taken

| # | Ruling | Rationale |
|---|---|---|
| 1 | One handoff per hotspot | Ownership and tests remain local. |
| 2 | Retrospective review plus gate design | Present defects and recurrence are covered. |
| 3 | Fixed window 26-07-2026 through 25-08-2026 | Evidence cannot drift. |
| 4 | At most ten executable-code slices | Bounded depth beats a skim. |
| 5 | Exclude generated/vendor/data-only churn unless behavior changed | Risk outranks volume. |
| 6 | Independent Standards and Spec passes | One axis cannot mask the other. |
| 7 | GitHub Issues, default labels, PR intake OFF, single-context | Canonical adapter. |
| 8 | PR body → issue → handoff/plan → matching doc → no spec available | Honest provenance. |
| 9 | Severity, location, failure mode, and repro/test required | No proof means no finding. |
| 10 | Fix only proven P0/P1 with regression tests | Limits mutation. |
| 11 | Separate adapter and fix PRs | Setup and remediation remain reviewable. |
| 12 | Design but do not enable the gate | Activation is out of scope. |
| 13 | Human approval additionally covers security/production paths | Model review is not release accountability. |

## Autonomy contract

Apply marked defaults and log them. Missing spec skips only that axis. Stop only the affected fix for secrets/PII, production state, irreversible migration, unclear money behavior, or bulk generated/vendor/data edits; continue safe review. Do not touch hand-written analysis HTML or generated TEI, pages, visualizations, or corpus bulk. Merge adapter and minimal proven P0/P1 PRs only after required checks are green. Never enable the proposed workflow or protection rule.

## Layers

1. [Roadmap](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ROADMAP_COMMENTARYSTRATEGIES_OXALPHA_CODE_REVIEW_2026Q3.md)
2. [Architecture](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ARCHITECTURE_COMMENTARYSTRATEGIES_OXALPHA_CODE_REVIEW.md)
3. [Implementation](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/IMPLEMENTATION_COMMENTARYSTRATEGIES_OXALPHA_CODE_REVIEW.md)
4. [Verification](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/VERIFICATION_COMMENTARYSTRATEGIES_OXALPHA_CODE_REVIEW.md)

## Starter

Read C:\Users\user\Documents\GitHub\Uprava\handoffs\H3551-OxAlpha_CommentaryStrategies_oxalpha-30d-risk-review-gate_26.08.26.md and execute it.

_Dr. Mārcis Gasūns_
