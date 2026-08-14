# PLAN_CommentaryStrategies_review-platform_2026Q3.meta.md — metadoc

_Created: 14-08-2026 · Last updated: 14-08-2026_

This metadoc records the purpose, provenance, maintenance contract, limitations,
and improvement ledger around [the execution PLAN](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PLAN_CommentaryStrategies_review-platform_2026Q3.md).
It does not duplicate the PLAN's decisions or implementation content.

## Subject

- **Document:** [PLAN_CommentaryStrategies_review-platform_2026Q3.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/PLAN_CommentaryStrategies_review-platform_2026Q3.md)
- **Purpose:** Execution-ready control document for a 90-day repository
  improvement program and its first 5–8-hour autonomous build.
- **Audience:** M.G., the Wave-1 executor, future maintainers, and scholarly
  editors evaluating what remains human-gated.
- **Contract:** Dated, cross-linked Markdown; every blocking decision resolved;
  explicit autonomy/fence; Wave-1 architecture, steps, acceptance, and risks;
  no secrets or unpublished reviewer data.

## Provenance

- **Created:** 14-08-2026 after a four-round interview plus one security/cost
  follow-up, 23 question rulings, local prior-art audit, live GitHub issue/Pages
  checks, and official GitHub/Cloudflare documentation checks.
- **Planner:** Codex, with a bounded architect pass for the file-level
  implementation draft; integrated and adjudicated by the primary session.
- **Execution owner:** H2736 (Codex) — Build the 68-sarga Kostina review portal,
  free OAuth autosave, immutable submission, and conservative adjudication gate.
- **Next hardening:** Wave-1 implementation evidence and post-deployment truth
  pass under H2736 (Codex) — Build the 68-sarga Kostina review portal, free OAuth
  autosave, immutable submission, and conservative adjudication gate.

## Ranked improvement backlog

| Rank | Improvement | Why | Status |
|---:|---|---|---|
| 1 | Deploy one portal and all 68 Kostina ballots. | The existing sarga-1 ballot is live but undiscoverable; sargas 2–68 are absent. | Queued: H2736 (Codex) — Build the 68-sarga Kostina review portal, free OAuth autosave, immutable submission, and conservative adjudication gate. |
| 2 | Add free OAuth mediation, remote drafts, and immutable raw submission. | Static Pages cannot safely hold OAuth secrets or durable private drafts. | Queued: H2736 (Codex) — Build the 68-sarga Kostina review portal, free OAuth autosave, immutable submission, and conservative adjudication gate. |
| 3 | Prove Leonov evidence losslessness and content-sensitive disagreement. | The prior schema-v1 defect was one application away from silent overwrite. | Queued: H2736 (Codex) — Build the 68-sarga Kostina review portal, free OAuth autosave, immutable submission, and conservative adjudication gate. |
| 4 | Encode the conservative adjudication policy and statistical gate. | “Agent confidence” must not become an undocumented editorial override. | Queued: H2736 (Codex) — Build the 68-sarga Kostina review portal, free OAuth autosave, immutable submission, and conservative adjudication gate. |
| 5 | Synchronize README, roadmaps, manual, issues, changelog, and state after deployment. | v1.17.1 has outrun several June–July operating descriptions. | Queued: H2736 (Codex) — Build the 68-sarga Kostina review portal, free OAuth autosave, immutable submission, and conservative adjudication gate. |
| 6 | Evaluate automation classes and reduce the final human queue. | Human attention should concentrate on disagreements and scholarly/editorial judgments. | Parked until Wave-1 submission/import contracts are stable; then Wave 2 of the roadmap. |
| 7 | Resolve corpus-number/statistics contradictions. | Corpus reliability affects publications and generated summaries beyond the book gate. | Parked to Wave 3; evidence work must precede prose edits. |

## Known limitations and caveats

- The PLAN authorizes infrastructure, not the creation/import of real Kostina
  votes or reviewer contact.
- Cloudflare authorization is conditional on the Free plan remaining sufficient;
  the durable fallback is local autosave plus aggregate JSON.
- A GitHub account and confirmed allow-listed login remain human prerequisites
  for hosted submission.
- The plan does not decide actual Leonov–Kostina disagreements or the fate of
  Kostina's editorial marks.
- Estimated 5–8 hours assumes existing generator/ledger code is extended and
  account prerequisites are available; security/cost stops remain binding.

## Intended use / known misuse

Use this PLAN as the single execution entry point and decision record. Do not
use it as permission to bypass reviewers, lower the statistical bar, replace
canonical JSON/ledger structures, or pay for infrastructure. Historical June–
July roadmaps remain evidence of project evolution, not the Wave-1 build brief.

## Maintenance and sunset plan

H2736 owns the open Wave-1 rows. At implementation merge, mark each completed
row with its full PR link, append a revision-history row, and reconcile the
PLAN/roadmap/architecture/implementation/verification set. The PLAN becomes
`superseded` only when the 90-day program has a new canonical control document;
it remains permanently useful as the ruling/provenance record.

## Deprecation status

**Active.**

## Related documents

- [Roadmap](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ROADMAP_CommentaryStrategies_2026Q3.md) — program waves and non-goals.
- [Architecture](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ARCHITECTURE_CommentaryStrategies_review-platform.md) — boundaries and contracts.
- [Implementation](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/IMPLEMENTATION_CommentaryStrategies_review-platform.md) — file-level Wave-1 sequence.
- [Verification](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/VERIFICATION_CommentaryStrategies_review-platform.md) — acceptance matrix and risk register.
- [Current operator manual](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md) — deployed workflow reference after implementation.
- [Current architecture of record](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/ARCHITECTURE.md) — repository-wide data/artifact architecture.

## Revision history of the subject

| Date | Event | Who |
|---|---|---|
| 14-08-2026 | PLAN and four layer documents created after audit/interview; autonomy-readiness gate passed. | Codex planning session |

_Dr. Mārcis Gasūns_
