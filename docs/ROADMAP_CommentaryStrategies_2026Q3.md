# CommentaryStrategies — 90-day improvement roadmap, 2026 Q3

_Created: 14-08-2026 · Last updated: 14-08-2026_

Canonical decisions and autonomy contract: [PLAN](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PLAN_CommentaryStrategies_review-platform_2026Q3.md).
Technical boundaries: [ARCHITECTURE](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ARCHITECTURE_CommentaryStrategies_review-platform.md).
Ordered first build: [IMPLEMENTATION](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/IMPLEMENTATION_CommentaryStrategies_review-platform.md).
Acceptance bar: [VERIFICATION](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/VERIFICATION_CommentaryStrategies_review-platform.md).

## Outcome after 90 days

CommentaryStrategies has one truthful operating surface: Kostina can review all
68 sargas through a public Pages portal with resilient saving and authenticated
submission; Leonov's votes remain intact; disagreements are compact and
actionable; defensible agent decisions pass only through a measured policy; and
the repository's roadmap, manual, README, issues, and session state describe the
same current system.

## Wave 1 — reviewer platform and book unblock (5–8 autonomous hours)

### Deliverables

1. Official `data/apparatus/index.html` portal with all 68 Kostina ballots,
   progress, resume, aggregate download, sync state, and recovery instructions.
2. Shared vanilla-JS/CSS ballot client; existing five-source generator extended
   rather than rewritten.
3. Cloudflare Worker + D1 on the Free plan for OAuth mediation and draft autosave;
   explicit submit creates an immutable raw-submission PR through GitHub.
4. Strict raw validator and idempotent schema-v2 importer that cannot overwrite
   `verdicts["Леонов"]`.
5. Evidence-backed Leonov–Kostina disagreement queue with editorial veto.
6. Versioned automation policy with deterministic invariants and the lower-95%-
   bound threshold of 0.95.
7. Publication-grade CI/browser checks and updated operator/Kostina documentation.

### What this unblocks

- Gives Kostina a real `github.io` entry point instead of a repository file path.
- Converts her completed work into one aggregate, attributable submission.
- Makes the final assembly gate computable without destroying Leonov's evidence.
- Establishes the safe substrate for reducing later item-by-item review.

### Completion evidence

The exact commands and production checks live in [VERIFICATION](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/VERIFICATION_CommentaryStrategies_review-platform.md).
Wave 1 is complete only when the portal and all 68 ballots return HTTP 200, the
mocked end-to-end submit/import passes, Leonov's verdict subtree is byte-stable,
CI is green, and no paid Cloudflare feature is enabled.

## Wave 2 — measured autonomy and compact editorial work (weeks 2–4)

### Deliverables

1. Retrospective evaluation of each proposed automation class against existing
   adjudication evidence and human votes, with frozen definitions and blind
   samples.
2. Only qualifying classes receive `auto_apply`; near-threshold classes receive
   `sample_review`; scholarly, anchor, edit, and disagreement classes remain
   `human_escalation`.
3. One compact disagreement/exception sheet replaces full-corpus re-review.
4. Statistical report records sample size, successes, method, interval, model
   provenance, data revision, and reversibility.
5. Dry-run final assembly proves which residual items genuinely need a person.

### Dependencies

Wave 1 raw-submission and ledger contracts must be stable. Real reviewer votes
remain outside autonomous execution and are imported only after receipt.

### Acceptance

No class auto-applies without passed invariants or a preregistered blind sample
whose lower 95% confidence bound is at least 0.95. Policy validation fails
closed on missing or changed evidence.

## Wave 3 — repository coherence and corpus reliability (weeks 5–8)

### Deliverables

1. Reconcile [README](https://github.com/gasyoun/CommentaryStrategies/blob/main/README.md),
   [architecture](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ARCHITECTURE.md),
   [2026H2 roadmap](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ROADMAP_2026H2.md),
   [commentary roadmap](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/COMMENTARY_ROADMAP.md),
   [manual](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md),
   and `.ai_state.md` with v1.17.1 and the deployed reviewer flow.
2. Close or re-scope issues whose fixes are already merged; keep human residuals
   explicit and small.
3. Add drift checks for generated reviewer assets, documentation counts/URLs,
   submission schemas, and changelog/state claims.
4. Resolve high-value corpus contradictions already recorded in state: the
   unattributed 241-record residual and conflicting translator statistics,
   without altering article prose until evidence is fixed.
5. Restore an honest test description: distinguish the corpus/ledger/browser
   gates from any no-op pytest job.

### Acceptance

A cold-start maintainer can identify the canonical data, current book gate,
official reviewer URL, automation limits, and next human action from README plus
one linked manual, without consulting historical WIP blocks.

## Wave 4 — submission-ready Sundarakāṇḍa assembly (weeks 9–12)

### Deliverables

1. Import real Kostina submission after human delivery and validation.
2. Produce the dual-reviewer agreement and disagreement reports.
3. Resolve only the compact editorial queue through the humans; do not rerun the
   full ballot.
4. Apply qualifying deterministic/agent classes under the frozen policy.
5. Rebuild the book master in dry-run, then production after explicit editorial
   resolution; record provenance for every inclusion/exclusion.
6. Cut the release and archive completed gate issues when evidence supports it.

### Acceptance

Every tier-2 note is included, excluded, or parked with attributable evidence;
no single reviewer overwrites the other; the camera-ready build is reproducible;
and residual human decisions are enumerated rather than hidden in prose.

## Non-goals

- No new analytical axis or change to the four-axis framework.
- No rewriting tier-1 scholarly text or article prose in Wave 1.
- No replacement of JSON, TEI, schema v2, or the five-source apparatus generator.
- No framework migration to React/Vite.
- No automatic resolution of editorial disagreements.
- No real vote creation, reviewer impersonation, or automated outreach.
- No paid hosting, paid Cloudflare activation, or silent provider substitution.
- No re-scrape of ruled-nonextractable Vālmīki commentary gaps.

## Human actions outside autonomous execution

- M.G. creates/owns the free Cloudflare account and GitHub OAuth/App registration
  if those credentials do not already exist; secrets go only into Cloudflare.
- M.G. sends the verified portal invitation to Kostina after Wave-1 acceptance.
- Kostina supplies her actual editorial rulings and ballot submission.
- Leonov/Kostina resolve the compact disagreement queue and book-policy residuals.

_Dr. Mārcis Gasūns_
