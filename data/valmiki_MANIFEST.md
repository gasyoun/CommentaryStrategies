# Vālmīki Rāmāyaṇa corpus — provenance & coverage manifest

Covers [`data/valmiki_shlokas/`](valmiki_shlokas/) (verse text + English glosses) and
[`data/valmiki_commentaries/`](valmiki_commentaries/) (Sanskrit commentaries).

## Source & provenance

- **Source:** [valmiki.gitasupersite.in](https://valmiki.gitasupersite.in) — the "GitaSupersite," IIT Kanpur.
- **Acquired:** 2026-06-29, via [`scripts/scrape_valmiki_shlokas.py`](../scripts/scrape_valmiki_shlokas.py) + [`scripts/scrape_valmiki_commentaries.py`](../scripts/scrape_valmiki_commentaries.py).
- **Regenerable:** yes — re-run the two scrapers with `--force`. The cached files are not authored here.

## ⚠️ RIGHTS — NOT yet cleared (blocks publication/commit)

The Vālmīki text and the 7 traditional Sanskrit commentaries are old works, **but** GitaSupersite's
specific digital edition, its **modern English word-by-word glosses and explanations** (captured in the
`word_by_word` / `explanation` fields of every shloka file), and the site's database compilation may carry
their own copyright / terms-of-use. GitaSupersite's ToS and `robots.txt` were **not** consulted by the
scrape. [`data/RIGHTS.md`](RIGHTS.md) covers only the five Soviet/Russian translation editions — it does
**not** extend to this source. **Do not republish, commit to history, or deposit (Zenodo/TEI) until rights
are cleared** (read the ToS / obtain IIT Kanpur permission, or ship scrapers-only + a regeneration manifest).

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

**Known gaps (acquisition is partial — not "7 commentaries on all of Vālmīki"):**
- `dharmakutam` (tid 9) and `tanisloki` (tid 11) produced **zero** files anywhere — verify the tids against
  the live site or confirm these commentaries are absent from GitaSupersite.
- **Yuddhakāṇḍa has zero commentary files** (shlokas were scraped, commentaries were not) — the run was
  interrupted.
- `kataka` exists only for kāṇḍas 1–2; `tilaka`/`bhusana` thin in Ayodhyā; `tattvadipika` thin in Sundara.

Completing the missing cells requires a re-scrape (network load on the source) and is gated on the rights
question above.
