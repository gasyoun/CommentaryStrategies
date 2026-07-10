---
paper_id: A22
title: "Submission-readiness report — A22 Nīlakaṇṭha commentary traditions (EN)"
manuscript: "article3_nilakantha_en.md"
venue: "@DECIDE — was Indologica Taurinensia (ceased with issue 45, 2019)"
byline: "M. Gasūns (sole author)"
orcid: 0000-0003-4513-884X
readiness_now: 4/5
date: 2026-07-10
lang: en
---

# Submission-readiness report — A22 (EN)

_Created: 10-07-2026 · Last updated: 10-07-2026_

Manuscript: [`article3_nilakantha_en.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/articles/article3_nilakantha_en.md) (~5,850 words after this pass).
RU original (A21): [`article3_nilakantha.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/articles/article3_nilakantha.md) (draft v3, 4/5 HOLD).
Sibling report: [`SUBMISSION_READINESS_A21.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/articles/SUBMISSION_READINESS_A21.md) (incl. the 02-07-2026 hostile pre-send check).
Handoff of record: [`H040-Fable_CommentaryStrategies_nilakantha_en_26.06.26.md`](https://github.com/gasyoun/Uprava/blob/main/handoffs/H040-Fable_CommentaryStrategies_nilakantha_en_26.06.26.md).
This pass: Fable 5 (`claude-fable-5`), 10-07-2026 — translation-fidelity + RU-v3 sync pass (translation v1 → v2).

---

## What this pass verified and did

### Table parity — VERIFIED IDENTICAL (mechanical check)

A script compared every data cell of Table 1 (30 Nīlakaṇṭha loci: locus number, Devanāgarī
term, Devanāgarī gloss content, type I–IV, Paribok code) and Table 2 (16 V/N notes: locus,
IAST tokens, Paribok code) between RU and EN.

| Check | Result |
|---|---|
| Table 1 row count | 30 = 30 |
| Table 1 Devanāgarī terms + glosses | identical, all 30 rows |
| Table 1 type / Paribok codes | identical, all 30 rows |
| Table 2 row count | 16 = 16 |
| Table 2 loci + Paribok codes | identical, all 16 rows |
| Distribution figures (§4.1, §7.1) | 43/37/17 and 63/37/0 — consistent in both files, abstract included |

One divergence found, and it was a **RU defect, not an EN one**: RU Table 2 row 10 read
`atīndriyāni`; the correct IAST (and the EN reading) is `atīndriyāṇi`. **Fixed in the RU
file this pass.**

### RU-v3 sync applied to EN (the RU moved after the v1 translation was made)

- **Three references promoted** from the trailing HTML comment into References
  (alphabetized) **and cited in-text at the same three places as RU v3**: Vassilkov
  1995–1996 (§1, on the MBh as a typological object), Pollock 2006 (§6, Sanskrit as the
  language of authoritative knowledge), Bronkhorst 1996 (§7.2, nature of authoritative
  utterance). HTML comment deleted.
- **Minkowski §7.4 parenthetical** reworded to "on Nīlakaṇṭha's Vedic and Tantric
  interests" — matching the cited *Mantrakāśīkhaṇḍa* article (ports the A21 P2 fix).
- **Footnote `[^1]` anchored** in §1 at the first mention of the *CommentaryStrategies*
  corpus (ports the A21 P1 fix; it was orphaned in EN too).

### Terminology alignment — VERIFIED (handoff punch-list item)

All load-bearing terms render consistently and match RU 1:1: *functional inversion*;
*selection divergence*; *inversion of selection / execution* (§5 also uses the RU's own
English glosses "selection inversion" / "execution inversion"); *selection zone*; P/K/D =
"concept" / "codifier" / "discursive"; *adhikārin* / *pratīka* / *ṭīkā* in italic
transliteration; the four Nīlakaṇṭha move types carry identical labels (I synonymic gloss,
II definition, III contextual exegesis, IV narrative motivation) in §2.2, §3 and both
tables.

### Byline reconciled (handoff punch-list item)

Handoff byline of record: **M. Gasūns (sole)**. Applied: front-matter `author:` changed
from "Mārcis Gasūns" to **"M. Gasūns"**, with `author-ru: "М. Ю. Гасунс"` added (mirrors
the RU file's own front-matter). The References entry **"Gasūns M. Yu."** is deliberately
kept: it cites the Russian-language Voprosy Jazykoznanija paper (A19), whose byline is
«Гасунс М. Ю.», and a transliteration of the published byline is standard citation
practice. In-text "(Gasūns 2026)" citations are consistent.

### Cross-reference hygiene (handoff punch-list item)

"Gasūns 2026 [= Article 1]" = A19 (*Conceptual Untranslatability*, Вопросы языкознания).
Per [`ARTICLES.md`](https://github.com/gasyoun/Uprava/blob/main/ARTICLES.md) A19 is 4/5
submission-staged (verification passed 02-07-2026, 3 gates) — "[Forthcoming]" remains
accurate today but **must be re-checked at submission time**; if A19 is not yet accepted
by then, soften to "submitted" or "in preparation" per venue convention.

## What this pass deliberately did NOT do

- **Cover letter — SKIPPED.** The handoff asked for an *Indologica Taurinensia* cover
  letter, but the 02-07-2026 hostile check established the journal **ceased publication
  with issue 45 (2019)**. Writing it would be waste; it follows the venue @DECIDE.
- **Paribok-attribution rewording — GATED.** The A21 hostile check requires softening
  «Таксономия Парибка (2011)» to a "tripartite distinction derived from Paribok" pending
  the [@DO] source check in
  [`docs/AXIS4_KD_DECISION.md`](https://github.com/gasyoun/CommentaryStrategies/blob/main/docs/AXIS4_KD_DECISION.md) §5.
  The EN §3/§1/§4.1/§7.2 + abstract carry the same claim and **must mirror whatever
  rewording A21 adopts** — flagged in the manuscript's STATUS comment. Rewording EN ahead
  of the RU ruling would desynchronize the pair.
- **Paribok 2011 bibliography entry — left as-is (defective in both files).** External
  evidence does not attest a «Шабдапракаша 2» ed. Paribok/Lelyukhin (2011); the entry must
  be verified against the physical volume (same [@DO] as the attribution gate). EN
  mirrors RU until that check lands.
- **No readiness bump.** 4/5 stands: author review is still the draft's own named gate.

## Remaining gates to 5/5 → submitted

1. **[@DECIDE] Venue** — shared with A21 (IT defunct; Scrinium out of scope). The venue
   choice decides which of the RU/EN pair leads and the cover-letter target.
2. **[@DO] Author review pass** — sign off that the EN faithfully renders the RU argument
   and reads as native scholarly English (the draft's own in-file gate).
3. **[@DO] Paribok source check** (AXIS4_KD_DECISION §5) → then mirror the A21 rewording
   into EN §1/§3/§4.1/§7.2 + abstract, and fix the Парибок 2011 / Paribok 2011 entry in
   both files.
4. On sign-off: bump A22 to 5/5 in
   [`ARTICLES.md`](https://github.com/gasyoun/Uprava/blob/main/ARTICLES.md), flip the
   front-matter/STATUS from draft to ready, and draft the cover letter for the ruled venue.

_(The handoff's ORCID gate is stale — resolved 28-06-2026: 0000-0003-4513-884X, already in
both files' front-matter.)_

_Dr. Mārcis Gasūns_
