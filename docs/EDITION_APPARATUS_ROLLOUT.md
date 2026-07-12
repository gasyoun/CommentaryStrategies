_Created: 12-07-2026 · Last updated: 12-07-2026_

# Edition-apparatus rollout — all Rāmāyaṇa kāṇḍas + the Mahābhārata

The helayo-style **Critical ↔ vulgate variant-apparatus** pipeline built for the Sundarakāṇḍa
(book 5) is a general 2-witness collation capability. This doc records what is done, what
remains, and the exact data + engineering gates to roll it out across **all 7 Rāmāyaṇa kāṇḍas**
and the **Mahābhārata (Nīlakaṇṭha vulgate ↔ BORI critical)**.

## Done — the reference implementation (Rām book 5)

- [`scripts/compare_editions.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/compare_editions.py) — book-level content alignment (difflib LCS) of the Baroda critical vs the southern vulgate → identical/variant/structural-absence buckets + sarga-renumbering. **Rāmāyaṇa-specific** (`5.SSS.VVVa` half-verse regex, hardcoded `ram_05_u.htm` path).
- [`scripts/spike_helayo_align.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/spike_helayo_align.py) — the **helayo-method aligner**: char-level Gotoh affine-gap + consonant/vowel/modifier substitution matrix; word-expanded apparatus loci (SHARED_CODE §18 method).
- [`scripts/build_edition_apparatus.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/build_edition_apparatus.py) — runs the aligner over every variant pair → the **positional variant apparatus** (`lemma (crit) ] variant (south)`). Sundara result: **865 clean-variant verses, 2106 apparatus loci, 66 sargas** ([`data/analysis/helayo_spike/APPARATUS_SUNDARA_VARIANTS.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/helayo_spike/APPARATUS_SUNDARA_VARIANTS.md)).

## The engineering thread (shared by every target)

1. **Parameterize `compare_editions.py`** — lift the hardcoded Rāmāyaṇa assumptions into a config: `(work_id, critical_loader, vulgate_loader, verse_id_scheme)`. The critical-side loader (GRETIL half-verse HTML) and southern-side loader (corpus jsonl) become pluggable; MBh needs a different critical loader (BORI) and verse-id scheme (`P.adhyāya.śloka` / Nīlakaṇṭha `P/U/A/S`).
2. **Generalize `build_edition_apparatus.py`** — it is already nearly general; only `verse_key()` parsing is Rāmāyaṇa-shaped (`5.S.V`). Make it scheme-aware.
3. **Similarity gate + Cyrillic-contamination quarantine** already in `build_edition_apparatus.py` — reused as-is (the Cyrillic bug is Rāmāyaṇa-southern-specific; MBh may surface its own source defects).

## Rāmāyaṇa — per-kāṇḍa data matrix ([H783](https://github.com/gasyoun/Uprava/blob/main/handoffs/H783-Sonnet_CommentaryStrategies_ramayana_edition_apparatus_rollout_all_kandas_12.07.26.md))

| kāṇḍa | southern vulgate jsonl | GRETIL Baroda critical | status |
|---|:---:|:---:|---|
| 1 bālakāṇḍa | ✅ present | ❌ absent | need critical → then run |
| 2 ayodhyākāṇḍa | ✅ present | ❌ absent | need critical → then run |
| 3 araṇyakāṇḍa | ✅ present | ❌ absent | need critical → then run |
| 4 kiṣkindhākāṇḍa | ❌ absent | ❌ absent | need **both** |
| 5 **sundarakāṇḍa** | ✅ | (via committed JSON) | **✅ APPARATUS SHIPPED** |
| 6 yuddhakāṇḍa | ❌ absent | ❌ absent | need **both** |
| 7 uttarakāṇḍa | ❌ absent | ❌ absent | need **both** |

The southern jsonls live in [`SamudraManthanam/web/corpus_builder/jsonl/`](https://github.com/gasyoun/SamudraManthanam) (books 1/2/3/5 present; 4/6/7 to be scraped). The GRETIL Baroda critical files (`ram_0N_u.htm`) are **absent for every kāṇḍa** — even Sundara's was lost; only its pre-computed comparison JSON survived. All must be (re)obtained from GRETIL.

## Mahābhārata — Nīlakaṇṭha vulgate ↔ BORI critical ([H784](https://github.com/gasyoun/Uprava/blob/main/handoffs/H784-Sonnet_CommentaryStrategies_mahabharata_nilakantha_vs_critical_apparatus_12.07.26.md))

| witness | status |
|---|---|
| **Nīlakaṇṭha vulgate** (mūla + Bhāratabhāvadīpa ṭīkā) | ✅ **ALREADY SCRAPED** — [`mahabharata-nilakantha/nilakantha_parser.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/mahabharata-nilakantha/nilakantha_parser.py) from [sanatana.in](https://sanatana.in/mahabharata/), 11-07-2026 → `nilakantha_vulgate_full.jsonl` (58.9 MB, **gitignored** for rights); per-parva census in [`NILAKANTHA_VULGATE_CENSUS.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/mahabharata-nilakantha/NILAKANTHA_VULGATE_CENSUS.md) (ādi 8623, sabhā 2713, vana 11859, … ~84k ślokas). |
| **BORI / Poona critical** | ❌ **NOT local** — obtain the John Smith / GRETIL electronic text of the Pune critical edition. **This is the gate.** |
| MBh corpus jsonls (18 parvas, sa IAST+SLP1 + ru) | ✅ present in SamudraManthanam — a *reading text* with the academic Russian translation, useful as a cross-check but NOT the critical witness. |

**MBh-specific work:** a comparator that aligns Nīlakaṇṭha (P/U/A/S addressing) ↔ BORI (`parva.adhyāya.śloka`) by verse content (the two editions differ in ordering, numbering, and inclusion — the vulgate carries the well-known additional passages the critical edition relegates to its apparatus, so structural-absence detection matters here even more than in Rāmāyaṇa). Then the shared aligner → MBh variant apparatus. **Related but distinct:** [csl-atlas `scripts/forensic/f8_mbh_census.py`](https://github.com/sanskrit-lexicon/csl-atlas) is the MBh *citation-locus* census (loci-fitting), not edition collation — same corpora, different task; consume its verse index, don't duplicate.

## Cross-cutting gates

- **Obtaining the critical texts** (GRETIL Baroda for Rāmāyaṇa; BORI/John Smith for MBh) is a file **download** — requires a go-ahead per the data-download policy; a human places the text or approves the fetch.
- **Rights:** the vulgate/critical source texts are third-party (vulgate jsonl + `nilakantha_vulgate_full.jsonl` are gitignored). The **derived variant apparatus** (readings only) is scholarly output, but any publication is gated by [`/publish-safety-check`](https://github.com/gasyoun/claude-config/blob/main/commands/publish-safety-check.md).
- **Multi-witness (Center-Star MSA)** stays latent until a 3rd witness per work is digitised (Gita Press for both epics); at 2 witnesses the deliverable is the pairwise positional apparatus.
- **Production quality (akṣara-level aligner + wiring into `build_edition_footnotes.py`)** is the separate [H776](https://github.com/gasyoun/Uprava/blob/main/handoffs/H776-Sonnet_CommentaryStrategies_helayo_aksara_apparatus_aligner_12.07.26.md) upgrade; the rollout can proceed at spike grade in the meantime.

## Provenance

Rollout doc + H783/H784: Opus 4.8 (`claude-opus-4-8`), 12-07-2026. Method registered in root [`SHARED_CODE.md` §18](https://github.com/gasyoun/github-spine/blob/main/SHARED_CODE.md); prior art memory `reference_helayo_sanskrit_alignment`.

_Dr. Mārcis Gasūns_
