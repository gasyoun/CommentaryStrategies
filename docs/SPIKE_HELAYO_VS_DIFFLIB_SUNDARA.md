_Created: 12-07-2026 · Last updated: 12-07-2026_

# Spike: helayo-style optimal alignment vs difflib for the Sundarakāṇḍa edition apparatus

**Question.** Is Charles Li's `helayo` method (multiple-sequence alignment for critical
editions — [SHARED_CODE §18](https://github.com/gasyoun/github-spine/blob/main/SHARED_CODE.md),
[docs](https://chchch.github.io/sanskrit-alignment/docs/)) worth adopting over the current
`difflib`-based aligner in
[`scripts/compare_editions.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/compare_editions.py)
/ [`scripts/sa_align.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/sa_align.py)
for the critical↔southern edition-divergence work that feeds
[`scripts/build_edition_footnotes.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/build_edition_footnotes.py)?

Follow-on decision is tracked as [H776](https://github.com/gasyoun/Uprava/blob/main/handoffs/H776-Sonnet_CommentaryStrategies_helayo_aksara_apparatus_aligner_12.07.26.md).

## Setup

- **Witnesses (2):** critical = GRETIL/Baroda `ram_05_u.htm`; southern vulgate = the text
  M. Leonov translates. Only these two are digitised; a 3rd (Gita Press, named in
  `ramayana-leonov/Костина.txt`) is not.
- **Input:** the committed difflib-matched **variant pairs** in
  [`data/edition_comparison/critical_only_and_variants.json`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/edition_comparison/critical_only_and_variants.json)
  (each carries both edition texts + difflib scalar similarity), so the spike is fully
  reproducible without the raw critical file.
- **Sargas:** critical 3 (14 variant pairs, similarity 0.66–0.99) and critical 6 (5 pairs) —
  a variant-rich and a clean sarga.
- **Spike aligner** ([`scripts/spike_helayo_align.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/spike_helayo_align.py)):
  a faithful **minimal helayo** — character-level **Gotoh affine-gap global alignment** (gap
  open −2.5, extend −0.5) with a **consonant/vowel/modifier substitution matrix** (ā~a, ṃ~m,
  ś~ṣ, n~ṇ, t~ṭ, k~g-adjacent score as *near*, not hard mismatch). Loci are word-expanded for a
  readable apparatus. Contrasted with `difflib.SequenceMatcher` (what the current tool uses).
- **Not run:** the real `helayo` Haskell binary (prebuilt Windows binary exists in the upstream
  `helayo/dist/`) — executing a downloaded binary was out of spike scope, and with only 2
  witnesses its Center-Star MSA reduces to pairwise global alignment anyway, which this spike
  implements directly. Raw JSON: `data/analysis/helayo_spike/spike_sarga{3,6}_result.json`.

## What the two methods produce on the same pair

| verse | difflib (current tool) | helayo-spike (this) |
|---|---|---|
| 5.3.4 | `ratio=0.950`, 2 opaque edit-blocks, **no readings** | 1 locus: **supuṣṭabalasaṃguptāṃ** (crit) \| **supuṣṭabalasampuṣṭāṃ** (south) |
| 5.3.10 | `ratio=0.978`, 2 edit-blocks | 1 locus: **vaidūryatalasopānaiḥ** \| **vaidūryakṛtasopānaiḥ** (tala/kṛta) |
| 5.3.16 | `ratio=0.931` | 1 locus: **ketumālasya** \| **kapimukhyasya** (substantive lexical variant) |
| 5.3.18 | `ratio=0.989` | 1 locus: **koṣṭhāgārāvataṃsakām** \| **goṣṭhāgārāvataṃsakām** (k/g) |
| 5.3.31~5.4.19 | `ratio=0.640`, 10 edit-blocks | 7 substantive loci (virūpān\|nātigaurān …) — makes the "reworded" verdict transparent |

## Findings

1. **The core win: readings, not a number.** `difflib` gives one scalar per verse pair plus
   opaque character edit-blocks that carry **no lemma and no competing readings**. The
   Gotoh aligner emits **positional apparatus loci with the actual competing readings** — the
   exact datum a critical apparatus / a «в критическом издании…» footnote needs. This is a
   qualitative capability the current tool structurally cannot provide.
2. **Affine gaps + the substitution matrix consolidate fragmentation.** Sarga 6: difflib's 28
   edit-blocks collapse to **22 clean apparatus loci**; near-equivalent alternations (vowel
   length, nasal series, sibilants, dental/retroflex) stop spawning spurious variant loci.
3. **Localises variants inside long compounds and across word-boundary mismatch.** It pinpoints
   `-saṃguptāṃ`/`-sampuṣṭāṃ` inside one compound, and aligns cleanly through the
   `maṇisphaṭika muktābhir` (crit, spaced) vs `vajrasphaṭikamuktābhir` (south, fused) boundary
   difference — both cases where naive word-level tokenisation fails and difflib's scalar just
   absorbs the noise.
4. **Sharpens the reworded↔structural-absence boundary** the `.ai_state` flagged as crude: the
   low-similarity 5.3.31 pair (difflib's opaque 0.64) resolves into concrete substantive loci,
   making "this is a reworded verse, not an absence" a transparent, inspectable judgment.
5. **Char-level loci need word-expansion to be readable** (raw output fragmented mid-syllable,
   `ṃg`|`mp`). The spike bolts on word-expansion; **`helayo`'s native akṣara-level mode would
   produce linguistically coherent loci directly** — a concrete reason to prefer real helayo (or
   an akṣara-level reimplementation) over a naive char aligner.

## Verdict

**Promising — adopt for the apparatus/footnote layer, not for the coarse bucketing.**

- ✅ **Adopt for** per-locus edition-divergence readings in
  `build_edition_footnotes.py` and any future printed critical apparatus: it turns opaque
  "variant, sim=0.95" rows into citable apparatus entries.
- ❌ **Do not replace** the cheap book-level `difflib` LCS in `compare_editions.py` that does the
  coarse identical/variant/structural-absence **bucketing + sarga-renumbering** — that job is
  fine and fast as is; helayo operates one level finer (within a matched pair).
- ⏳ **Center-Star MSA advantage is latent** until a 3rd witness (Gita Press) is digitised; at 2
  witnesses the gain is the positional apparatus, not multi-way collation.

## If adopted (H776)

1. Prefer **akṣara-level** granularity (real `helayo` binary with TEI/FASTT I/O, or an
   akṣara-segmented reimplementation of this Gotoh core) so loci are coherent without
   word-expansion hacks.
2. Feed the loci into `build_edition_footnotes.py` so each footnote carries the competing
   readings, not just "absent/reworded".
3. Re-run once Gita Press is digitised to exploit Center-Star across 3 witnesses.
4. Residual spike rough edges to fix in a production pass: a few spurious adjacency loci from
   insertion/deletion next to a substitution (5.3.11, 5.3.19).

## ✅ ADOPTED and implemented (12-07-2026, Sonnet 5 `claude-sonnet-5`)

Item 1 (akṣara reimplementation, option (b) — no external binary) and item 2 (footnote
wiring) are done; item 3 stays latent (Gita Press still not digitised); item 4's two named
cases are fixed (verified below).

- `scripts/spike_helayo_align.py`: added `syllabify()` (maximal-onset IAST akṣara
  segmentation — onset consonant cluster + vowel nucleus incl. ai/au + trailing
  anusvāra/visarga/candrabindu), `gotoh_aksara()` (Gotoh over akṣara tokens, gap costs
  length-scaled to stay comparable with the char-level constants), `collapse_loci_aksara()`
  + `align_aksara()`. The char-level `gotoh`/`sub_score`/`_NEARMAP` are reused unchanged as
  the nested substitution-cost engine between two akṣara strings — the near-equivalence
  matrix (ā~a, ṃ~m, ś~ṣ, n~ṇ, ...) applies inside a syllable too, not just discarded.
- **5.3.11 fixed:** char-level gave 3 fragmented loci incl. a spurious duplicate
  (`pratināditām`/`''`, `pratināditām`/`parināditām`); akṣara-level gives 2 clean loci.
- **5.3.19 fixed:** char-level gave 4 garbled loci (`rākṣasendrasya`/``, `sa`/``,
  `dadarśa`/``, `sa`/`` — an uninterpretable duplicate-`sa` mess); akṣara-level gives 1
  clean locus (`sa`/``).
- Cases that were already clean at char level (5.3.4, 5.3.10, 5.3.16, 5.3.18) are
  byte-identical at akṣara level — no regression.
- Book-wide (`build_edition_apparatus.py`, all 66 sargas): 865→839 clean-variant verses,
  **2106→1664 apparatus loci** (21% fewer/cleaner; some previously-"clean" verses now
  correctly yield zero substantive loci once mid-syllable fragments consolidate).
- `scripts/build_edition_footnotes.py`: new `variant_reading` candidate kind (839
  candidates, one per clean-variant verse, carrying its actual competing readings) —
  previously this layer was computed but never reached the footnote review gate at all.
  `scripts/build_footnotes_review_html.py` renders the new kind with its own readings
  block. `scripts/compare_editions.py`'s book-level bucketing is untouched
  (`git diff` on `data/edition_comparison/book_summary.json` empty — regression-verified).

_Dr. Mārcis Gasūns_
