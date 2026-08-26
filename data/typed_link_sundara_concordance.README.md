# typed_link_sundara_concordance — dataset resolution note

_Created: 26-08-2026 · Last updated: 26-08-2026_

**What.** The Q4.1 Type-D `commentary-citation` pilot concordance on the
Sundarakāṇḍa lexical layer ([H3346](https://github.com/gasyoun/Uprava/blob/main/handoffs/H3346-OxAlpha_CommentaryStrategies_q41-type-d-pilot-concordance_22.08.26.md)):
258 rows, each a WhitneyRoots MW root cited in a lexical note, keyed end-to-end
by [sanskrit-util](https://github.com/sanskrit-lexicon/sanskrit-util) v0.10.0
`linkid` IDs per Uprava's
[TYPED_LINK_ID_GRAMMAR.md](https://github.com/gasyoun/Uprava/blob/main/TYPED_LINK_ID_GRAMMAR.md)
— the first Type-D dataset built through the library itself
(`linkid_build_anchor_id` → `linkid_build_target_locus` →
`linkid_validate_link_record`, 0 errors; any error aborts the build).

Files:

- [typed_link_sundara_concordance.tsv](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/typed_link_sundara_concordance.tsv)
  — the §1 record shape (10 columns, typed_link_lint convention).
- [typed_link_sundara_concordance.jsonl](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/typed_link_sundara_concordance.jsonl)
  — same rows plus dedup/provenance fields; `_row_key` is
  `<anchor_id>|<target_locus>` (linkid-only, nothing synthetic).
- [analysis/typed_link_sundara/dedup_vs_1058_report.md](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/typed_link_sundara/dedup_vs_1058_report.md)
  (+ machine [.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/typed_link_sundara/dedup_vs_1058.json))
  — dedup vs Leonov/Kostina's own 1058-note tier-1 baseline.
- [analysis/typed_link_sundara/commentarystrategies-sundarakanda-typed-link-q41_review.html](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/typed_link_sundara/commentarystrategies-sundarakanda-typed-link-q41_review.html)
  — the human gate (shared csl-pyutil emitter, sheet_id
  `commentarystrategies-sundarakanda-typed-link-q41`, V9 manifest + screening +
  V13 identity gate). Registered in Uprava
  [REVIEW_SHEETS_INDEX.md](https://github.com/gasyoun/Uprava/blob/main/REVIEW_SHEETS_INDEX.md).

**IDs (reuse, don't mint — grammar §0).**

- Anchor: `root:<SLP1>` — tail accepted only if already present in
  [WhitneyRoots/crosswalk/mw_roots.json](https://github.com/gasyoun/WhitneyRoots/blob/main/crosswalk/mw_roots.json)
  (704 distinct keys) after `to_slp1` normalization. 89 cited forms fell
  outside that inventory and were skipped and counted, never minted.
- Target: `commentary:sundara-lexical:V.<sarga>.<verse>` — work slug names this
  repo's lexical layer; the cite tail is the layer's own stable `shloka`
  address, carried verbatim.

**Dedup result vs the 1058.** 156 rows unique-vs-1058 (no tier-1 note on the
verse), 102 verse-overlap (tier-1 covers the verse but never cites this root),
0 root-overlap after word-boundary-aware citation matching — the lexical layer
genuinely never duplicates a tier-1 note's exact root point. All three tiers
are shown per card; the vote decides promotion, not the counts.

**Human gate before ANY store write (handoff Fail condition).** Nothing here
has been written into `data/apparatus/*`, the book aggregate, or any other
store. The review sheet is the only path to promotion: vote it, save
`commentarystrategies-sundarakanda-typed-link-q41_decisions.json`, then run
`python scripts/build_typed_link_sundara_concordance.py --apply-decisions FILE`
which refuses unvoted/partial files (all-or-nothing) and writes only the
confirmed tier TSV/JSONL beside the proposed ones.

**Registration scope (§5 D2b).** Per-consumer-repo only — NOT added to the
kosha manifest until roadmap Q2.1 freezes Type A–D schema.

Rebuild: `python scripts/build_typed_link_sundara_concordance.py`
(deterministic; byte-identical re-runs are the regression gate). Requires
sibling checkouts `../sanskrit-util`, `../kosha`, `../csl-pyutil`,
`../WhitneyRoots`.

_Dr. Mārcis Gasūns_
