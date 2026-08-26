# CommentaryStrategies OxAlpha code-review architecture

_Created: 26-08-2026 · Last updated: 26-08-2026_

## Components

1. Canonical [issue tracker](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/agents/issue-tracker.md), [triage labels](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/agents/triage-labels.md), and [domain rules](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/agents/domain.md).
2. Risk selector with at most ten fixed-window PRs; executable/critical-path risk outranks churn.
3. Independent Standards reviewer using repo rules and the smell baseline.
4. Independent Spec reviewer using the ruled evidence chain.
5. [Evidence ledger](https://github.com/gasyoun/CommentaryStrategies/blob/main/reports/OXALPHA_30D_CODE_REVIEW_2026-08-26.md) preserving both axes, exclusions, and proof.
6. Fix lane admitting only proven P0/P1, one minimal regression-tested PR per defect.
7. Inactive [future-gate design](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/OXALPHA_STATUS_GATE_DESIGN_2026.md).

## Contract

Each manifest row records PR, base/head SHA, executable paths, exclusions, risk reasons, spec source, and both review states. Findings require severity, exact location, failure mode, and repro/test. The proposed check returns pass, evidence-backed fail, or infrastructure-neutral; never a silent pass when unavailable.

## Prior art

PARTIAL: existing CI or content-review assets are not formal PR code review. Reuse the canonical adapter and two-axis method; build only selection, evidence, urgent fixes, and inactive gate design.

_Dr. Mārcis Gasūns_
