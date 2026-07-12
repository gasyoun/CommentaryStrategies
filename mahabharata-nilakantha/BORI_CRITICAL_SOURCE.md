_Created: 12-07-2026 · Last updated: 12-07-2026_

# BORI critical Mahābhārata — e-text provenance (the `bori-critical/` witness)

The **Poona / BORI critical edition** electronic text, obtained 12-07-2026 as the missing witness for the MBh Nīlakaṇṭha ↔ critical variant apparatus ([H784](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H784-Sonnet_CommentaryStrategies_mahabharata_nilakantha_vs_critical_apparatus_12.07.26.md)). The **text itself is gitignored** (`bori-critical/`); this doc is the committed record — same pattern as [`NILAKANTHA_VULGATE_CENSUS.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/mahabharata-nilakantha/NILAKANTHA_VULGATE_CENSUS.md) for the vulgate.

## ⚠️ Rights — local-only, DO NOT redistribute

- **© Bhandarkar Oriental Research Institute (BORI), Pune, India, 1999.**
- John D. Smith's stated terms (in `MBh00.txt`): the authorised text *"is available only via the web page [bombay.indology.info/mahabharata/statement.html](https://bombay.indology.info/mahabharata/statement.html). **Please do not provide copies of the text to others.**"*
- Therefore: **gitignored, never committed, never published.** Any derived apparatus carries BORI critical readings → gated by [`/publish-safety-check`](https://github.com/gasyoun/claude-config/blob/main/commands/publish-safety-check.md) before it goes anywhere public. Treat exactly like the gitignored Nīlakaṇṭha vulgate jsonl.

## Source & preparation

- **Text:** typed by Prof. **Muneo Tokunaga** (Kyoto) from the BORI critical edition (Sukthankar/Belvalkar/Vaidya et al., 1917–1966); revised & maintained by **John D. Smith** (Cambridge), corrections by a BORI team.
- **Downloaded from:** `https://bombay.indology.info/mahabharata/text/UR/MBh{00..18}.txt` (encoding **UR = Unicode Roman, ISO-15919**), 12-07-2026. Header stamp: "Last updated: Fri Sep 25 2020".
- Other encodings offered by the site: **UD** (Unicode Devanāgarī), and ASCII (Harvard-Kyoto). We took **UR** because ISO-15919 Roman maps cleanly to our IAST/SLP1 pipeline.

## Files (19, ~11 MB total, gitignored)

`MBh00.txt` = general-info header; `MBh01.txt`–`MBh18.txt` = the 18 parvans. Line counts (a/c half-verses + prose lines):

| parva | lines | parva | lines | parva | lines |
|---|---:|---|---:|---|---:|
| 01 ādi | 15 791 | 07 droṇa | 17 072 | 13 anuśāsana | 14 134 |
| 02 sabhā | 5 155 | 08 karṇa | 8 222 | 14 āśvamedhika | 5 945 |
| 03 vana | 22 468 | 09 śalya | 7 099 | 15 āśramavāsika | 2 252 |
| 04 virāṭa | 4 003 | 10 sauptika | 1 639 | 16 mausala | 575 |
| 05 udyoga | 12 961 | 11 strī | 1 556 | 17 mahāprasthānika | 240 |
| 06 bhīṣma | 11 458 | 12 śānti | 27 624 | 18 svargārohaṇa | 416 |

## Format (for the H784 comparator)

- **Verse addressing:** `PPAAASSSh` — 2-digit parva + 3-digit adhyāya + 3-digit śloka + half-verse letter (`a`/`c`), or a capital letter (`A`, `B`, …) for numbered **prose** lines. Example — the maṅgala:
  `01001000a nārāyaṇaṁ namaskr̥tya naraṁ caiva narottamam`
  `01001000c devīṁ sarasvatīṁ caiva tato jayam udīrayet`
- **ISO-15919 quirks vs IAST:** anusvāra is `ṁ` (not `ṃ`); vocalic ṛ is `r̥` (r + combining ring, NFD). `sanskrit_util.nfold` already folds nasals→n and strips diacritics, so canon matching is unaffected — but a comparator that displays readings should normalise ISO-15919 → IAST first.
- **Nīlakaṇṭha ↔ BORI alignment** must be **by verse content, not by number**: the vulgate carries the additional passages the critical edition relegates to its apparatus (`Supp*.txt` on the same site), so many vulgate ślokas have no critical counterpart (structural absence).

## Re-fetch (if lost)

```sh
mkdir -p bori-critical && cd bori-critical
for n in 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18; do
  curl -s -o "MBh$n.txt" "https://bombay.indology.info/mahabharata/text/UR/MBh$n.txt"
done
```

## Consumer

[H784](https://github.com/gasyoun/Uprava/blob/main/handoffs/archive/H784-Sonnet_CommentaryStrategies_mahabharata_nilakantha_vs_critical_apparatus_12.07.26.md) — the MBh comparator (`compare_editions_mbh`) aligns this against `nilakantha_vulgate_full.jsonl` → the MBh variant apparatus via the shared helayo aligner. **Data gate now cleared:** both witnesses are local; only the comparator engineering remains.

_Dr. Mārcis Gasūns_
