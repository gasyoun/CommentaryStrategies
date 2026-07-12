# Sundara commentary OCR (Phase 2) — superseded by the scraped corpus

_Created: 08-07-2026 · Last updated: 10-07-2026_
> Ролевой слой (10-07-2026): операторский справочник тома — [`docs/MANUAL.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/MANUAL.md); персональные руководства участников — [`docs/LEONOV_SUNDARAKANDA_GUIDE.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/LEONOV_SUNDARAKANDA_GUIDE.md) · [`docs/KOSTINA_SUNDARAKANDA_GUIDE.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/KOSTINA_SUNDARAKANDA_GUIDE.md) · [`docs/GASUNS_SUNDARAKANDA_GUIDE.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/GASUNS_SUNDARAKANDA_GUIDE.md).


**Disposition of handoff [H370](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H370-Opus_CommentaryStrategies_sundara_revival_ocr_phase2_08.07.26.md)** — "Sundara revival: Gemini-OCR phase 2 of the 5 commentaries."
Executor Opus 4.8 (`claude-opus-4-8`), 08-07-2026.

## Verdict: no OCR to do — the gap is zero

H370 was minted from year-roadmap ruling **R8** ([ROADMAP_FABLE_YEAR_2026_2027.md §2](https://github.com/gasyoun/Uprava/blob/main/ROADMAP_FABLE_YEAR_2026_2027.md)) to "revive the Sundara front" by turning the five traditional Sanskrit commentaries into apparatus-usable text via Gemini-OCR — because the standing roadmap named Gemini-OCR as the measured Phase-2 lever. The handoff carried an explicit Phase-0 gate: *"read the repo's roadmap/`.ai_state.md` for what OCR already exists — build only the gap."*

That gate has now fired. **The OCR lever was already delivered — by a superior method — on 2026-07-01**, one week before H370 was minted. It is registered in the repo but the roadmap ruling that produced H370 referenced the pre-2026-07-01 plan.

Three independent reasons the OCR premise is moot:

1. **The commentary text is already acquired by scraping, not OCR.** All seven traditional Sanskrit commentaries were scraped from [valmiki.gitasupersite.in](https://valmiki.gitasupersite.in) (IIT Kanpur) on 2026-06-29 into [`data/valmiki_commentaries/`](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/valmiki_commentaries) — structured digital text, not page images, so it is more faithful than any OCR pass could be. Full provenance + coverage: [`data/valmiki_MANIFEST.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/valmiki_MANIFEST.md).
2. **There are no commentary scans in the repo to OCR.** The only PDFs present are secondary literature (Lidova, Kazansky); [`sources/`](https://github.com/gasyoun/CommentaryStrategies/tree/main/sources) holds annotation guides and notes JSON. There is no scan staging for the five commentaries — OCR has no input.
3. **Rights are cleared and residual gaps are ruled permanent.** Reproduction/distribution granted by the Gita Supersite section editor (Sudalaimuthu Palaniappan), 2026-07-01, CC BY 4.0, attribution-required ([`data/valmiki_PERMISSION.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/valmiki_PERMISSION.md)). The uncovered cells (`dharmakutam`, `tanisloki`, all of Yuddhakāṇḍa) were ruled by MG on 2026-07-01 as **not retrievable — do NOT re-scrape or OCR** (documented in the manifest).

Running Gemini-OCR now would re-derive already-cleared, higher-quality data and violate both the org "check prior art / build only the gap" rule and H370's own Phase-0 gate.

## Coverage report — Sundarakāṇḍa commentary layer (the H370 deliverable, honestly)

Source of truth: [`data/valmiki_MANIFEST.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/valmiki_MANIFEST.md) § *Commentary coverage*. Sundarakāṇḍa is 68 sargas; the density layer draws on the three strong commentaries:

| commentary | Sundara sargas covered | of 68 | acquisition |
|---|---|---|---|
| tilaka | 66 | 97% | scraped (structured text) |
| bhūṣaṇa | 68 | 100% | scraped |
| śiromaṇi | 65 | 96% | scraped |
| tattvadīpikā | 6 | 9% | scraped (thin at source — not OCR-recoverable) |
| dharmakūṭam | 0 | — | absent from source, ruled permanent |
| taniśloki | 0 | — | absent from source, ruled permanent |

**Pages OCR'd / remaining: n/a — the corpus is scraped digital text, not OCR'd images. Pages "remaining to OCR" = 0** (no scans exist; residual coverage gaps are source-limited and ruled not-retrievable, not an OCR backlog). The three strong commentaries that the ~38% Sanskrit-commentator dialogue layer relies on are effectively complete for Sundarakāṇḍa.

## What actually revives the Sundara front (the real live lever)

Note production is **no longer scan-bound** — the commentary text is in hand. The revival R8 intended has already happened at the data layer; the front is now **human-review-gated**, not acquisition-gated. The commentator-dialogue apparatus has been drafted, judged, and staged across the Phase-2 batches (pilot + batch 2 + batch 3 + lexical layer + edition footnotes; LP camera-ready master built under [H268](https://github.com/gasyoun/Uprava/blob/main/handoffs/H268-Fable_CommentaryStrategies_sundara_lp_camera_ready_07.07.26.md)).

The single thing gating further note production is the **four pending browser review sheets** (MG/Kostina/Leonov votes → `decisions.json`), tracked in [`.ai_state.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/.ai_state.md):

- batch 2 — 38 candidates · [`data/analysis/phase2_batch2/review.html`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch2/review.html)
- batch 3 — 227 candidates · [`data/analysis/phase2_batch3/`](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/analysis/phase2_batch3)
- edition footnotes — 51 candidates · [`data/edition_footnotes/`](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/edition_footnotes)
- lexical layer — 611 notes · [`data/analysis/lexical_judge/`](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/analysis/lexical_judge)

**Apparatus integration is already owned by existing handoffs — no follow-on minted.** H370 said "apparatus integration is the NEXT handoff — mint it at close." That handoff already exists and must not be duplicated: [H159](https://github.com/gasyoun/Uprava/blob/main/handoffs/H159-Fable_CommentaryStrategies_batch2_apply_04.07.26.md) (batch-2 apply) and [H276](https://github.com/gasyoun/Uprava/blob/main/handoffs/H276-Fable_CommentaryStrategies_sundara_gates_apply_final_assembly_07.07.26.md) (gated apply + final assembly) are the live apply-on-vote fronts. The revival's actual next action is **human votes**, not more agent work.

_Dr. Mārcis Gasūns_
