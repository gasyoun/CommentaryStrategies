_Created: 12-07-2026 · Last updated: 12-07-2026_

# BORI App. I apparatus criticus — e-text provenance (the `bori-apps/` witness)

The **Poona/BORI critical edition's own apparatus criticus** (App. I "star passages" —
manuscript readings the editors collated but relegated out of the constituted critical
text), obtained 12-07-2026 as the independent verification source for
[H810](https://github.com/gasyoun/Uprava/blob/main/handoffs/H810-Sonnet_CommentaryStrategies_mbh-apparatus-print-verification_12.07.26.md)
(review-gate check of the H784/H802/H804 `structural_absence`/`vulgate_extra_adhyayas`
flags). **The text itself is gitignored** (`bori-apps/`); this doc is the committed
record — same pattern as
[`BORI_CRITICAL_SOURCE.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/mahabharata-nilakantha/BORI_CRITICAL_SOURCE.md)
for the base critical text.

## ⚠️ Rights — local-only, DO NOT redistribute

Same source, same rights posture as the base critical text: **© Bhandarkar Oriental
Research Institute (BORI), Pune, India** — John D. Smith's stated terms apply
identically ("do not provide copies to others"). **Gitignored, never committed, never
published.**

## Source & preparation

- **Text:** the App. I star-passage apparatus, same critical-edition project
  (Sukthankar/Belvalkar/Vaidya et al.; text prepared by Tokunaga/Smith).
- **Downloaded from:** `https://bombay.indology.info/mahabharata/apps/UR/Supp{00..18}.txt`
  (ISO-15919 Roman), 12-07-2026, per the file-naming convention documented at
  [`/mahabharata/apps.html`](https://bombay.indology.info/mahabharata/apps.html).
  `Supp00.txt` = general info; `Supp01–18.txt` = the 18 parvans.

## Format

- **Star-passage lines:** `PP*NNNN_LL <reading>` — 2-digit parva, `*`, 4-digit
  passage-sequence number, `_`, 2-digit line-within-passage. Lines sharing the same
  `PP*NNNN` are one continuous inserted passage (grouped by
  `scripts/verify_mbh_apparatus_against_print.py`'s `load_supp_passages()`).
- **Anchor comments** (`% After 3.1.10, S ins.:`) give the manuscript siglum (S/T/G/M/D/K/B/Dn
  family = Śāradā/Telugu/Grantha/Malayalam/Devanagari/Kashmiri/Bengali/Devanagari-northern
  recension groups) and the critical-text verse the passage follows. **Not machine-parsed**
  in H810 — heavily line-wrapped philological prose, too fragile to parse reliably; the
  verification instead matches passage TEXT content directly (n-gram Jaccard), sidestepping
  anchor parsing entirely.

## Re-fetch (if lost)

```sh
mkdir -p bori-apps && cd bori-apps
for n in 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18; do
  curl -s -o "Supp$n.txt" "https://bombay.indology.info/mahabharata/apps/UR/Supp$n.txt"
done
```

## Consumer

[H810](https://github.com/gasyoun/Uprava/blob/main/handoffs/H810-Sonnet_CommentaryStrategies_mbh-apparatus-print-verification_12.07.26.md) —
[`scripts/verify_mbh_apparatus_against_print.py`](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/verify_mbh_apparatus_against_print.py)
matches this against every H784/H802/H804 `structural_absence` flag. Results (rights-safe:
ids/scores only) in `data/edition_comparison_mbh/<parva>/print_verification.json` +
[`data/edition_comparison_mbh/PRINT_VERIFICATION_REPORT.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/edition_comparison_mbh/PRINT_VERIFICATION_REPORT.md).

_Dr. Mārcis Gasūns_
