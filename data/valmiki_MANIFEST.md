# Vālmīki Rāmāyaṇa corpus — provenance & coverage manifest

Covers [`data/valmiki_shlokas/`](valmiki_shlokas/) (verse text + English glosses) and
[`data/valmiki_commentaries/`](valmiki_commentaries/) (Sanskrit commentaries).

## Source & provenance

- **Source:** [valmiki.gitasupersite.in](https://valmiki.gitasupersite.in) — the "GitaSupersite," IIT Kanpur.
- **Acquired:** 2026-06-29, via [`scripts/scrape_valmiki_shlokas.py`](../scripts/scrape_valmiki_shlokas.py) + [`scripts/scrape_valmiki_commentaries.py`](../scripts/scrape_valmiki_commentaries.py).
- **Regenerable:** yes — re-run the two scrapers with `--force`. The cached files are not authored here.

## ✅ RIGHTS — CLEARED (2026-07-01)

Permission to reproduce, distribute, and make available the **Sanskrit text, the seven traditional
Sanskrit commentaries, and the modern English word‑by‑word glosses and explanations** as published on
<https://valmiki.gitasupersite.in> — for an open‑source research corpus and a Zenodo archive under an open
license — was granted by **Sudalaimuthu Palaniappan, editor of the Vālmīki Rāmāyaṇa section of the Gita
Supersite**, on **1 July 2026**. Non‑exclusive, worldwide, perpetual, royalty‑free; **attribution
required**. Full grant archived verbatim in [`valmiki_PERMISSION.md`](valmiki_PERMISSION.md); summary in
[`data/RIGHTS.md`](RIGHTS.md).

- **License:** CC BY 4.0 (project compilation/derived apparatus; underlying Gita Supersite materials used
  by permission, not claimed as this project's copyright).
- **Required attribution (verbatim):** *Vālmīki Rāmāyaṇa, as published on the Gita Supersite
  (https://valmiki.gitasupersite.in), used by permission of the editor, Sudalaimuthu Palaniappan.*
- Publication/commit/deposit (Zenodo/TEI) is **permitted**. (Historical note: the corpus was in fact
  already tracked in git before clearance; this grant legitimizes the existing commit — no un-ignore was
  needed.)
- Residual-risk note: editor-level grant, relied upon in good faith; not a separate IIT Kanpur
  institutional instrument. See [`valmiki_PERMISSION.md`](valmiki_PERMISSION.md).

## Cleanup applied (2026-06-29)

[`scripts/clean_valmiki_corpus.py --apply`](../scripts/clean_valmiki_corpus.py) removed sarga-1 **fallback
duplicates** — the site silently serves sarga-1 content for out-of-range sarga requests, and a pre-guard
scrape had cached these (every kāṇḍa padded to a uniform ~130 sargas).

| | before | removed | after |
|---|---|---|---|
| shloka files | 781 | 244 | **537** |
| commentary files | 2 416 | 894 | **1 522** |
| size | 130 MB | — | **45 MB** |

Detection is content-based (a non-sarga-1 file whose first real `verse_id` is `<k>.1.1`, or a commentary
file byte-identical to its `*_sarga_01.txt`), so it is safe and reversible. Indexes rebuilt disk-authoritatively.

## Shloka coverage (verse text)

All 6 kāṇḍas; sarga counts now match the GitaSupersite recension:

| kāṇḍa | sargas |
|---|---|
| 1 Bāla | 77 |
| 2 Ayodhyā | 119 |
| 3 Araṇya | 75 |
| 4 Kiṣkindhā | 67 |
| 5 Sundara | 68 |
| 6 Yuddha | 131 *(GitaSupersite recension; critical edition has 128)* |

Note: each `sarga_01.json` carries a few leading entries with an empty `verse_id` whose `sanskrit` field is
an English bracketed sarga summary — filter on empty `verse_id` if processing.

## Commentary coverage (files per commentary × kāṇḍa)

| commentary | Bāla | Ayodhyā | Araṇya | Kiṣk. | Sundara | Yuddha | total |
|---|---|---|---|---|---|---|---|
| tilaka | 75 | 11 | 73 | 67 | 66 | 0 | 292 |
| bhusana | 77 | 3 | 75 | 67 | 68 | 0 | 290 |
| siromani | 77 | 118 | 75 | 67 | 65 | 0 | 402 |
| tattvadipika | 77 | 119 | 74 | 66 | 6 | 0 | 342 |
| kataka | 77 | 119 | 0 | 0 | 0 | 0 | 196 |
| dharmakutam | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| tanisloki | 0 | 0 | 0 | 0 | 0 | 0 | **0** |

**Known gaps — DOCUMENTED AS PERMANENT (do NOT re-scrape; project decision 2026-07-01).**
Acquisition is partial — this is *not* "7 commentaries on all of Vālmīki." Per M.G., **re-scraping will
not recover these cells** (the content is not retrievable from the source), so they are recorded here as
standing coverage limits, not as a TODO:
- `dharmakutam` (tid 9) and `tanisloki` (tid 11) — **zero** files anywhere; absent from GitaSupersite for
  this acquisition. Not retrievable.
- **Yuddhakāṇḍa — zero commentary files** across all commentaries (verse text present). Not retrievable.
- `kataka` exists only for kāṇḍas 1–2; `tilaka`/`bhusana` thin in Ayodhyā; `tattvadipika` thin in Sundara.

**Impact on Phase 2 (Sundarakāṇḍa density layer): none.** Sundara commentary coverage is strong —
`tilaka` 66, `bhusana` 68, `siromani` 65 (of 68 sargas) — which is what the ~38% Sanskrit-commentator
dialogue layer draws on. The gaps above affect other kāṇḍas / the full-corpus deposit's completeness, not
the Sundara apparatus.
