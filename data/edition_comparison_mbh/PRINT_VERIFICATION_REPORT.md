# MBh edition-apparatus review-gate — verification against print (BORI App. I)

_Created: 12-07-2026 · Last updated: 12-07-2026_

> [H810](https://github.com/gasyoun/Uprava/blob/main/handoffs/H810-Sonnet_CommentaryStrategies_mbh-apparatus-print-verification_12.07.26.md) —
> answers the review-gate caveat left open by every H784/H802/H804 per-parva
> README ("not individually verified against print"): checks the
> `vulgate_extra_adhyayas` and `significant_absences.json` → `structural_absence`
> flags from `compare_editions_mbh.py` against an actual independent print
> source — the BORI critical edition's own apparatus criticus (App. I "star
> passages"), not a reconstruction.

## Source

[`bombay.indology.info/mahabharata/apps/UR/Supp##.txt`](https://bombay.indology.info/mahabharata/apps.html) —
the same critical-edition project (Sukthankar/Belvalkar/Vaidya et al., text
typed by Tokunaga/Smith) that produced the base `MBh##.txt` witness already
used by H784. These are the App. I passages: verses/lines the BORI editors
found in the manuscripts they collated but relegated out of the constituted
critical text, each with a manuscript-siglum note ("After 3.1.10, S ins.:").
**Gitignored, local-only**, same rights posture as `bori-critical/` (© BORI).

## Method

The anchor comments ("After 3.1.10, S ins.:") are heavily line-wrapped
philological prose — too fragile to parse reliably as exact verse anchors.
Instead: each star-passage's **text** is grouped by its passage id
(`parvaNo*NNNN`, ignoring the `_LL` line suffix) into a candidate pool, then
matched against every `structural_absence` vulgate passage (and a sample of
each whole extra-adhyaya) by **4-gram character Jaccard on fully despaced
canon strings** — an inverted n-gram index keeps this fast (~1–50s/parva
instead of the many-minutes a full `SequenceMatcher.ratio()` all-pairs scan
took). Word-token Jaccard was tried first and rejected: it badly penalized
compound-spacing differences between the vulgate's sandhi-fused Devanagari
and App. I's spaced-out scholarly transcription (verified by spot-check — see
`scripts/verify_mbh_apparatus_against_print.py` docstring for the concrete
example). The `best_sim >= 0.3` threshold was **calibrated by manually
inspecting matches across the 0.35–0.45, 0.55–0.65, and 0.95–1.0 score bands**
on Vanaparva — all three bands turned out to be genuine same-passage matches;
low scores in the 0.3–0.5 range are typically *partial* matches where the
vulgate query bundles more content (e.g. a speaker tag) than the specific
App. I entry covers.

## Results

| | confirmed | total | rate |
|---|---:|---:|---:|
| **structural_absence flags** (≥0.3 sim) | 2,969 | 14,581 | **20.4%** |
| — high confidence (≥0.5) | 1,431 | 14,581 | 9.8% |
| — very high confidence (≥0.7) | 685 | 14,581 | 4.7% |
| — near-identical (≥0.9) | 466 | 14,581 | 3.2% |
| **whole extra-adhyaya verses** (≥0.3 sim, sampled) | 233 | 5,552 | 4.2% |

Per-parva structural_absence confirmation:

| parva | struct_abs | confirmed | rate |
|---|---:|---:|---:|
| 1 ādi | 1894 | 510 | 26.9% |
| 2 sabhā | 458 | 162 | 35.4% |
| 3 vana | 2074 | 403 | 19.4% |
| 4 virāṭa | 464 | 154 | 33.2% |
| 5 udyoga | 743 | 169 | 22.7% |
| 6 bhīṣma | 750 | 66 | 8.8% |
| 7 droṇa | 2249 | 410 | 18.2% |
| 8 karṇa | 1594 | 477 | 29.9% |
| 9 śalya | 769 | 98 | 12.7% |
| 10 sauptika | 122 | 16 | 13.1% |
| 11 strī | 107 | 35 | 32.7% |
| 12 śānti | 1328 | 242 | 18.2% |
| 13 anuśāsana | 1460 | 141 | 9.7% |
| 14 āśvamedhika | 266 | 43 | 16.2% |
| 15 āśramavāsika | 124 | 10 | 8.1% |
| 16 mausala | 44 | 9 | 20.5% |
| 17 mahāprasthānika | 10 | 3 | 30.0% |
| 18 svargārohaṇa | 125 | 21 | 16.8% |

## Interpretation

**A ~20% confirmation rate is NOT a defect in the H784/H802/H804 comparator —
it is the expected outcome, and a meaningful positive result.** App. I
records readings BORI's editors found in the specific ~60 manuscripts they
collated for the critical edition; it is not, and was never meant to be, an
exhaustive record of every reading in every later vulgate print tradition.
The Nīlakaṇṭha recension (17th-century Maharashtrian redaction, the basis of
the Bombay/Kinjawadekar print vulgate this project scraped) postdates most of
BORI's base manuscripts and is known to carry its own accretions. That ~1 in
5 flagged "vulgate-only" passages turns out to be independently attested in
BORI's own apparatus — using zero information from this project's own
alignment — is a real, positive confirmation signal: it means the
comparator's structural-absence detection is finding **genuine recension
differences**, not systematically manufacturing false positives out of
alignment noise. The other ~80% is not thereby "wrong" — it is either (a)
Nīlakaṇṭha-specific material with no BORI-collated-manuscript witness, or
(b) still an alignment artifact, and this pass cannot distinguish the two
without a human philologist checking specific passages.

The much lower whole-extra-adhyaya rate (4.2%) makes sense on the same
logic: entire additional chapters are a different scale of addition than the
line/passage-level insertions App. I typically records.

## Caveats

- This confirms **existence of a matching App. I entry**, not that the
  specific vulgate manuscript tradition BORI attributes it to is Nīlakaṇṭha's
  own textual family — App. I sigla span all recensions (Śāradā, Bengali,
  Telugu, Grantha, Malayalam, Devanagari), several unrelated to the
  Nīlakaṇṭha/Bombay line. A hit still means "this is a documented recension
  variant, not comparator noise" — the strongest claim intended here.
  Attributing specific hits to specific recension families would need parsing
  the (fragile) anchor-comment sigla, not attempted in this pass.
- Whole-extra-adhyaya verification only checked verse-level content, not
  whether the App. I sigla imply a matching *whole chapter* boundary.
- No human philologist has reviewed any individual match; this is a
  machine-computed corroboration signal, not a scholarly edition.

## Files

Per-parva `data/edition_comparison_mbh/<parva>/print_verification.json` (rights-safe:
ids/scores/matched-supp-ids only, no verbatim text) — full per-verse
`best_sim` scores and matched App. I passage ids. Reproducible via
[`scripts/verify_mbh_apparatus_against_print.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/verify_mbh_apparatus_against_print.py).

_Dr. Mārcis Gasūns_
