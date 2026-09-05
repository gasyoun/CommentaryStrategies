_Created: 07-07-2026 · Last updated: 05-09-2026_

# Agent log agent-ab060b327a86784d4

_Model: `claude-sonnet-5`; extracted by scripts/export_agent_logs.py; raw transcript alongside (.jsonl) holds the full record incl. tool results._


I'll start by reading the drafting brief and the input files.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\DRAFTING_BRIEF.md
Now let me look at the canonical method doc and check the docs/PHASE2_METHOD.md referenced, plus prior batch outputs for calibration.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && l
Let me check sarga 30's candidates (drafted in batch-2) for calibration, plus look at a recently drafted batch-3 sarga (e.g. sarga_27) as a close-style reference.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Console encoding issue. Let me write output to a file instead of stdout for Cyrillic/IAST-safe review.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\scratch_s30.json
Good calibration. Now let me check a batch-3 sarga already drafted (e.g. sarga_27) to see the exact schema used most recently, and check `_meta` conventions.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Good, schema confirmed. Now let's look at a few notes from sarga_27 for contrastive examples, and check reject reason phrasing conventions.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\scratch_s27.json
Now I have a solid calibration. Let me look at the structure of one segmented file to understand the data shape precisely.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Only 8 verses for sarga 29? Let me check the _meta and preambles, and see the full structure of a verse bundle.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\scratch_meta29.json
Interesting — sarga 29 has only 8 verses. Let's check the other three sargas' sizes too, before diving in.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Now let's slice `leonov_own_notes.json` and `sundara_commentary_to_add.json` for all 4 sargas up front.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Now let me slice out the relevant sarga data into scratch files for all 4 sargas at once.

- 🔧 `Bash` — SCRATCH="C:/Users/user/AppData/Local/Temp/claude/C--Users-user-Documents-GitHub/3c92a91d-16fd-4adf-a
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Element 0 is a `_meta` dict, not a note. Let me check its structure and a real entry.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sundara_sample.json
Now I understand the shape. Let me write a slicing script that extracts everything I need for all 4 sargas into scratch files.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\slice.py
That's a new file, no need to read first — it errored because it doesn't exist yet, let me just retry (Write should work for new files).

- 🔧 `Bash` — ls "C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9
The file was actually written despite the error message. Let's verify content and run it.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\slice.py
Interesting — this looks like leftover content from a previous session's scratch file with a similar name, not what I wrote. That's fine, it's actually a more thorough version. Let's run it for all 4 sargas.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && f
All slices are small. Now let's start with sarga 29. Read the verses, leonov notes, and phase1 notes.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_29_verses.json
Now let's read the leonov own notes and phase1 notes for sarga 29.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_29_leonov_notes.json
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_29_phase1_notes.json
Now I have full context for sarga 29. Let me analyze each verse for a possible commentator-note.

**Verse 1**: Tilaka gives only "upasevinaḥ = sevakāstha iva" (grammar gloss). Bhūṣaṇa gives an extended interpretation but mostly paraphrase with philosophical framing (tathā = "as things really are," referencing that even a sage would use "tathā" this way, i.e., pointing to the completeness of her suffering). Let me check if this is note-worthy — Bhūṣaṇa's reading of "tathā" as referring to the totality of suffering already lived (12 years) seems distinctive. Siromani mostly paraphrases. This could be a candidate — Bhūṣaṇa's specific point that "tathā" implies she thought no further suffering was possible, referencing the 12 years quote. Let me check this against подстрочник: "Пребывающей в таком состоянии" — generic. Bhūṣaṇa's point is specific and adds a narrative dimension.

Let me continue reviewing verses 2-8 before drafting.

**Verse 2**: Tilaka/Siromani/Bhūṣaṇa all describe physical details of eye (arāla pakṣma = curved lashes, etc.) — pure descriptive paraphrase, no added content beyond подстрочник. Leonov's own note cross-refs to V.27.50 (already covered).

**Verse 3**: Tilaka gives "adhyuṣitaḥ = kṛtasaṃparkaḥ" (grammar gloss) — matches_verse false with content_containment 0.0, likely misplaced (belongs elsewhere or just a stray gloss). Bhūṣaṇa/Siromani paraphrase.

**Verse 4**: Leonov/Kostina note already flags "упругое" (sujātaḥ) needing literal comm — Bhūṣaṇa's गloss सुजातः सुन्दरः is literally what Kostina cites. No new content beyond that already in the note.

**Verse 5**: Extensive Bhūṣaṇa content. Let's examine — "śikharāgradantyāḥ" already noted by Leonov (dantyāḥ per Tilaka). But there's more content here — Bhūṣaṇa gives a second meaning for "vāsaḥ parisraṃsata" (slipping garment) as "kāntāgamana-sūcaka" (a sign that indicates the arrival of the beloved) — cited partly by Leonov's own note ("приспустившееся платье – знак, указывающий на приближение возлюбленного" — that's literally Bhūṣaṇa's second interpretation, already captured). But Bhūṣaṇa ALSO cites samudrika (physiognomy) verses about women with pomegranate-seed-like teeth having long-lived husbands — that's a distinct addition not in Leonov's note.

Let me check this carefully — this could be a good candidate (realia/physiognomy doctrine, kazansky_type В).

**Verse 6**: Tilaka mentions a variant reading "saṃvādibhiḥ" for "sādhusiddhaiḥ" — a textual variant not in подстрочник. This is a candidate (Б, textual variant).

**Verse 7**: Leonov/Kostina's note flags "bhrukeśāntam" as omitted from подстрочник — Bhūṣaṇa explains this compound in detail (eyebrows+hair-ends = "upper region with scattered locks"). This might complement Leonov's note.

**Verse 8**: Bhūṣaṇa/Siromani mostly paraphrase; note the colophon appears embedded in Bhūṣaṇa's text (not commentary content).

Let me verify the variant reading in verse 6 more carefully and check verse 5's physiognomy passage.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && e
I've reviewed the content directly already (Devanagari read above). Let me now decide the full verse-by-verse draft/reject and write sarga 29's output.

Decisions for sarga 29:
- 5.29.1: DRAFT — Bhūṣaṇa's distinctive point that "tathā" signals totality/completeness of suffering (referencing the earlier 12-years-of-happiness quote), i.e. she believed no further misfortune possible, hence the omens. Contrastive not needed (single commentator).
- 5.29.2: REJECT — pure descriptive paraphrase across all 3 commentators; cross-ref already in Leonov's own note.
- 5.29.3: REJECT — Tilaka's gloss is a stray grammar note (content_containment 0.0, likely misplaced); Bhūṣaṇa/Siromani paraphrase.
- 5.29.4: REJECT — duplicates Leonov/Kostina's own note (Bhūṣaṇa's sujātaḥ=sundaraḥ already cited verbatim).
- 5.29.5: DRAFT — Bhūṣaṇa's samudrika-śāstra citation (physiognomy verses: women with pomegranate-seed-shaped teeth have long-lived husbands) is a distinct doctrinal/realia addition beyond Leonov's own note (which only covers the "signals approaching lover" reading and the tooth-simile translation choice).
- 5.29.6: DRAFT — Tilaka's variant reading साधुसिद्धैः/संवादिभिः (textual variant, type Б).
- 5.29.7: Consider — Bhūṣaṇa's explanation of bhrukeśāntam complements Kostina's flagged omission. Let me check if it's substantive enough.
- 5.29.8: REJECT — paraphrase only.

Let me re-examine verse 7 Bhūṣaṇa gloss more closely and verse 1 Bhūṣaṇa passage for exact wording before finalizing.

Looking again at verse 1 Bhūṣaṇa: "तथागतां... तथाशब्दप्रयोगादित्थमिति परिच्छिद्य वक्तुमशक्यदुःखाम्... इतः परमेव व्यसनानि भविष्यन्तीति मन्यमानाम्। "समा द्वादश तत्राहं राघवस्य निवेशने। भुञ्जाना मानुषान् भोगान् सर्वकामसमृद्धिनी।" इत्युक्तं भोगजातं सर्वमकिंचित्करमासीत्, दुःखमेव निरूपकमासीत्।" — This is indeed distinctive: Bhūṣaṇa reads "tathāgatām" (arrived at such a state) as pointing to indescribable suffering, and glosses it against her own earlier words (quoting V.28, "for twelve years I enjoyed all pleasures...") to say all that former happiness now counts as nothing — pure suffering defines her state. This is a genuine narrative-psychological point, distinct from подстрочник's flat "in such a state."

Now let me check verse 7's Bhūṣaṇa content for bhrukeśāntam.

Bhūṣaṇa: "स्वक्षिभ्रुशोभनाक्षिश्रूयुक्तम्। केशाः अन्ते यस्य तत् केशान्तम्। उपरिभागप्रकीर्णालकमित्यर्थः।" — This explains bhrukeśānta as "hair scattered at the upper region" (i.e., disheveled locks framing forehead), which is indeed the specific content Kostina flagged as omitted from подстрочник ("bhrukeśāntam Опущено"). This directly fills that gap — worth drafting as complements_leonov.

Let me check the `pratika_check` for verse 1 more carefully — Tilaka's note there matches_verse true, fine.

Now let me draft the JSON for sarga 29.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_29_candidates.json
Wait — I need to reconsider verse 6. Let me re-read the brief's reject discipline: variant readings that change the image are explicitly valued by M.G.'s pilot gate feedback ("variant readings that change the image"). Let me check if this variant changes anything meaningfully.

`sādhusiddhaiḥ` = "well-established/well-proven" (omens); `saṃvādibhiḥ` = "concordant/corroborating" (omens). This is a genuine semantic variant — not just orthographic. Let me reconsider drafting it as a minor textological note.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_28_candidates.json
Let me check if sarga 28 has a similar variant-reading example to see the bar for what counts as draftable.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
The variant here (sādhusiddhaiḥ / saṃvādibhiḥ) is genuinely a "pāṭhāntara" flagged by the commentator himself, but it doesn't change the image/meaning substantially (both mean roughly "well-confirmed/concordant omens") — this is a borderline case. Given the expected accept rate is 5-10% (depth not bulk), and this variant doesn't shift meaning, I'll keep it rejected but tighten the reasoning. Let me finalize sarga 29 as-is — 3/8 = 37.5% is too high actually. Let me reconsider more critically.

Given the target accept rate ~5-10%, with only 8 verses, 3 drafts might be over-drafting. But brief says "Expected accept rate ~5-10% — depth, not bulk" as guidance across the whole corpus, not a hard per-sarga quota, and small sargas can have outliers. Let me scrutinize verse 1 and verse 7 once more for genuine strength.

Verse 1 (Bhūṣaṇa's tathā point) — this is a real narrative-psychological insight tied to specific prior text quote, matches M.G.'s stated preference for "narrative-function observations." Keep as DRAFT.

Verse 5 (samudrika teeth-longevity) — genuine doctrinal/realia frame, matches M.G.'s valued category "doctrinal frames." Keep as DRAFT.

Verse 7 (bhrukeśāntam) — this is a legitimate lexical fill of Kostina's own flagged gap. Let me double check this isn't too thin/grammatical. The brief says reject "(c) pure Sanskrit grammar invisible to a Russian reader." Bhūṣaṇa's explanation is grammatical parsing (केशाः अन्ते यस्य तत्... = bahuvrīhi analysis) but the actual content — "scattered locks at the temples" — is visible/meaningful to a Russian reader and directly fills a gap Kostina herself flagged as omitted. This is legitimate per the "When Leonov/Kostina ALREADY note the verse: do NOT auto-reject... genuinely distinct facet" rule — here it's not "already note" but "flagged omission," even better justification to draft. Keep as DRAFT.

I'll keep all 3 drafts for sarga 29. Now let's write the final file to the actual output path.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 29 done. Now let's move to sarga 31 — 27 verses, 5 ambiguous markers.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_31_leonov_notes.json
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_31_phase1_notes.json
Now let's read the verses for sarga 31.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_31_verses.json
Now I have all 27 bundles for sarga 31. Verses 20-23, 25-45, 47-56, 58+ are missing entirely from this list — but the segmented file has exactly 27 items and `verse_count: 27`. Let me verify the count and check the merged-range/no-text bundles carefully.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
27 confirmed. Note: 5.31.24, 5.31.46, 5.31.57 have `ambiguous_marker: false` but empty sanskrit/leonov_ru — these are "content_anchor" style leftover commentary fragments attached to verse numbers beyond the segmented range (this sarga's actual verse count must be less than 24/46/57 — likely a mis-tagged verse token, similar to the "89" issue in sarga 27). Let me check.

Looking at bhusana/siromani text under 5.31.24 — it clearly says "राजेत्यादि" referencing "rājā" (verse 2's opening) and discusses "cakravartikule jātaḥ... lakṣmivardhanaḥ" content from verses 2-6, with siromani saying "श्लोकत्रयमेकान्वयि" (three verses in one syntactic unit) — this is actually commentary content belonging to verses 2-6 (already covered separately in verses 2-6's own bundles as empty/bhusana-only). The "24" numbering must be a katamana/misalignment artifact from the segmentation script (verse numbers restart or a secondary numbering scheme is used in this edition, likely bhusana's separate verse-numbering that differs from the main pāṭha).

Given no Sanskrit/podstrochnik text at all for 24/46/57 and the ambiguous markers merged 10-13 etc., these look like segmentation artifacts (`content_anchor`-type reassignments), similar to sarga 27's "89" case. Let's treat them per the reject discipline: no independent verse text exists, and content is a duplicate/misattached commentary. I'll reject all of them citing the reassignment issue and, where the content actually duplicates a verse already covered, note that.

Let me check the "1013", "1014" etc. bundles more carefully - they look like merged ambiguous ranges of verse numbers 10-13, 10-14, 15-16, 16-18, 17-18. These match the ambiguous_marker=true reject category (f).

Now let's go through each verse 1-19 for draftable content.

**Verse 1**: Tilaka gives an internal ref "5.31.1,2" and a note about "mukhyasya rājavaṃśeṣu śreṣṭhasya... lakṣmivardhana iti hrasva ārṣaḥ" — this seems to be leftover content from verse 4 (mukhyaś cekṣvākuvaṃśasya) misattached to verse 1's bundle, discussing a "hrasva ārṣa" (short-vowel archaism) grammar note. That's grammar-only, reject. Bhūṣaṇa's extended note on "saṃśrave madhuraṃ" as either "nearby" or (alternate reading) "sweet to hear" with an ornate rasa-theory digression (words become "rasa-producing" through sound-contact even without prior semantic processing) — that's an alaṃkāra-śāstra point, somewhat abstract/technical grammar-poetics; arguably too abstract/invisible to a general reader and not adding a concrete image. I'll reject.

Let's check verses 2-8 (formulaic hero-praise verses, mostly no commentary or bare text repeats, already covered by Phase-1 etymology notes for cakravartin/puraṃdara/paraṃtapa/satyābhisaṃdha).

- 🔧 `Bash` — echo "reviewing verses 2-19 content directly from already-read JSON above"
Let me go through carefully:

- **5.31.2–7**: bhūṣaṇa only, and it's just a repeat of the verse text itself (no interpretive commentary) — these are text reproductions, not commentary. REJECT all (restates подстрочник/verse, no interpretation).
- **5.31.8**: Tilaka: "satyābhisaṃdhasya = satyasaṃkalpasya" (gloss, already covered in Phase-1 note) + "tasyā hetostadanveṣaṇahetoḥ. yathārūpāṃ..." — wait, this seems to be commentary for verse 15 misattached here (yathārūpāṃ yādṛg-rūpāṃ...). Let me note that as a reassignment issue, but the content is fully covered in verse 15's own bundle context anyway. Bhūṣaṇa here: just grammar "svārthe ṇic" (causative gloss) — no. REJECT.
- **5.31.9**: Tilaka: mṛgayām uddiśya dhāvatā (gloss) — grammar. Siromani: paraphrase. Bhūṣaṇa: "mṛgayāṃ paridhāvatā... anena līlayā kharādivadhaḥ sūcyate" — this is interesting: Bhūṣaṇa reads "playfully hunting" as implying Rāma's killing of Khara etc. was effortless/playful (līlā), not stated as such directly in подстрочник ("охотясь" is neutral). This adds a theological/heroic dimension — Rāma's slaying of the rakshasas was done as sport, not effort. This is a genuine addition — a doctrinal frame about Rāma's effortless power (avatāra doctrine implicit). DRAFT candidate.
- **5.31.10**: Tilaka/Siromani/Bhūṣaṇa mostly paraphrase; Phase-1 already has extensive note on Janasthāna crossref. Siromani here also has extra content: "tata iti. tataḥ sugrīvamaitrīkaraṇānantaraṃ rāmo vālinaṃ hatvā kapirājyaṃ sugrīvāya prāyacchat" — this is actually commentary belonging to verse 12/13 (misattached/leaked into verse 10's bundle due to segmentation). Not new content beyond what's already in verses 12-13. REJECT verse 10 (dupes Phase-1 crossref + misattached content already covered elsewhere).
- **5.31.11**: bare bhūṣaṇa text reproduction. REJECT.
- **5.31.12**: Siromani: "sa iti. sītāṃ mārgamāṇaḥ sa rāmaḥ sugrīvaṃ nāma vānaraṃ mitram āsasāda prāpa cakāra ity arthaḥ. ardhadvayam ekānvayi" — paraphrase/grammar (syntax linking half-verses). Bhūṣaṇa bare text. REJECT — content_anchor flagged too (matches_verse false, content_containment 0.417) suggesting the pratika might belong elsewhere, but content is paraphrase regardless.
- **5.31.13**: Siromani/Bhūṣaṇa paraphrase. REJECT.
- **5.31.14**: Siromani: "ahaṃ iti. vegavān ahaṃ saṃpātivacanāt sītābodhaka-saṃpāti-vākyaṃ saṃśrutya tasyāḥ sītāyā hetoḥ samudraṃ plutaḥ" — paraphrase, no new content beyond Phase-1's extensive Sampāti note. REJECT.
- **5.31.15**: Siromani/Bhūṣaṇa paraphrase (yathārūpāṃ etc. gloss already noted by Leonov's own note). REJECT — dupes Leonov's own note.
- **5.31.16**: Tilaka: "rāghavasya mukhād aham aśrauṣaṃ seyam āsāditā dṛṣṭā iha" — adds "dṛṣṭā iha" (seen HERE, i.e. specifically at this location under the shinshapa tree) — minor gloss, arguably grammar/paraphrase. Siromani/Bhūṣaṇa: pure paraphrase/narrative transition. REJECT — no substantive addition.
- **5.31.17**: Bhūṣaṇa bare text; Siromani paraphrase + misattached content from v.18 ("niśamyeti..."). REJECT.
- **5.31.18**: bare bhūṣaṇa text. REJECT.
- **5.31.19**: This is the big one — Siromani AND Bhūṣaṇa both give extensive commentary. Let's look closely.

Siromani: "sā sītā acintyabuddhiṃ piṅgādhipateḥ sugrīvasya amātyaṃ vātātmajam udayasthaṃ udayagiristhitaṃ sūryam iva dadarśa" — mostly paraphrase.

Bhūṣaṇa gives a MUCH longer psychological commentary: Sita observing Hanuman infers *before even seeing his body* (tadvapuravalokanāt pūrvaṃ) that: (1) he's clever/capable enough to penetrate the inner women's quarters of Lanka (niipuṇatara-matiḥ), (2) by his voice-quality (svara-viśeṣa) she deduces he's a vānara, but not independent — he must be an amātya (minister) serving some king of his own kind, and this business (of finding her) is in his hands, (3) "vātātmajam" — he's the son of the Wind, the very cause of life-breath (prāṇana-hetu) for all beings, (4) "sūryam ivodayastham" — either compared to the sun on the eastern mountain, OR (following a lexicon "sūryaḥ = araṇa" possible reading) actually compared to Aruṇa (the sun's charioteer/dawn) rather than the sun itself, based on lexical ambiguity of "sūrya."

This is genuinely rich: Sita's chain of inference (competence → vānara identity → subordinate status → connection to Vāyu → simile choice) is a real narrative-psychological point completely absent from the подстрочник, which just states the visual comparison. Also the lexical ambiguity (sūrya = sun OR Aruṇa) is a real textological point. This deserves a note — possibly TWO notes (psychological inference chain = one facet; sūrya/Aruṇa lexical ambiguity = another), but per style contract "1-3 sentences," I should pick the strongest single facet or contrastive form. Since only Bhūṣaṇa discusses this (Siromani doesn't diverge), it's single-commentator, not contrastive. I'll draft one note focusing on the inference chain (the more narratively rich point), and consider whether to also note the sūrya/aruṇa ambiguity separately — but the brief warns against padding, so I'll fold the key point into one note, mentioning the sūrya/aruṇa alternative briefly if it fits within style limits, or make it a second focused note since it's a genuinely separate observation (lexical/textual variant vs. psychological/narrative point). Given "depth not bulk," I'll produce ONE strong note per verse and pick the more valuable point: the inference chain, since it's the more distinctive and rarer type of note category (narrative-function/psychological), matching M.G.'s preferences exactly.

Now let's also check 5.31.24, 46, 57, and the ambiguous merged ones for legitimate reject reasons.

- **5.31.24**: content = leftover material discussing verses 2-6 (rājā... cakravartikule... lakṣmivardhanaḥ), explicitly marked by Siromani as "ślokatrayam ekānvayi" (three verses forming one syntactic unit) — this is a segmentation artifact where the verse-numbering token "24" doesn't correspond to a real verse in this range (sarga only goes to ~19 in this bundle's visible range, but the full sarga is longer — but since sarga_31 verse_count=27 total, and we only see 19 real verses + 3 "ghost" numbered fragments + 5 merged-ambiguous — this suggests the actual full sarga probably has ~60 verses but only some carry commentary, and these ghost numbers (24, 46, 57) are literal bhūṣaṇa/siromani sub-commentary section labels misassigned as verse numbers by the extraction script). Either way, no independent verse text = can't ground a note. REJECT citing content is duplicative of verses 2-7 already rejected, and no independent verse text exists.
- **5.31.46**: content = pārthivavyañjanaiḥ gloss (already same lemma as verse 5, "rājacihnaiḥ" = royal marks) — paraphrase, duplicative of verse 5 content (already rejected as bare text there too). REJECT.
- **5.31.57**: content = duplicate of verses 7-8 material (rakṣitā, satyābhisaṃdhasya, pravrajito vanam) marked "ślokatrayam ekānvayi" — REJECT, no independent text, duplicative of already-rejected 7/8.
- **5.31.1013, 1014, 1516, 1618, 1718**: ambiguous_marker=true, merged ranges — reject per rule (e).

Now let's finalize sarga 31's draft/reject decisions and write the file.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_31_candidates.json
I left a placeholder reject entry for 5.31.9 by mistake since it's actually drafted. Let me fix that — remove the duplicate reject entry for 5.31.9 (it's in notes, not rejected).

- 🔧 `Edit` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_31_candidates.json
Now let's validate counts and write to the actual output path.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 31 verified and written. Now sarga 32 (15 verses, 0 ambiguous markers).

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_32_verses.json
Now let's check leonov_notes and phase1 notes for sarga 32.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_32_leonov_notes.json
This is very useful. Verse 7's own note already covers the vajra scar backstory (Uttarakāṇḍa 35). Let's check phase1 notes.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_32_phase1_notes.json
Now let's work through sarga 32's verses.

**Verse 1**: Bhūṣaṇa gives text reproduction + colophon. Nothing new. Also has stray content ("namo 'stu vācaspataye..." from verse 14 misattached, and a devatā prayer explanation) which duplicates verse 14 material. REJECT.

**Verse 2**: Siromani gives paraphrase. Leonov's own note already covers "строфа есть не во всех редакциях" (textual variant across editions) — no additional commentator content on that point here. REJECT — dupes Leonov's own note implicitly (textual point is about verse presence, not discussed further by commentators here); content is paraphrase only.

**Verse 3**: Bhūṣaṇa/Siromani — mostly paraphrase + misattached content belonging to verse 4 (aho bhīmam idaṃ sattvaṃ...). REJECT.

**Verse 4**: Tilaka: "vānarasya nirdhāraṇe ṣaṣṭhī jātāv ekavacanam... bhīmaṃ prākṛtaprāṇibhayāvaham, ata eva taiḥ durāsadaṃ durnirīkṣyaṃ ceti matvā punarapi māyaivēyam iti bhayān mumoha" — Tilaka adds that Sita's renewed fainting/confusion stems from suspecting this apparition might STILL be an illusion (māyā) — i.e., she fears it might be another magical deception (like the Māyā-Mārīca deer earlier in the story). Siromani: "punar mumoha rāmātismṛtyā vaicittyaṃ prāpa" — Siromani gives a DIFFERENT reason for the fainting: renewed memory/longing for Rāma (rāma-ati-smṛtyā), not fear of māyā. This is a genuine divergence — two commentators give different causes for the same narrative moment (fear of illusion vs. grief-triggered memory of Rāma). This is a strong CONTRASTIVE candidate.

Let's check подстрочник for verse 4: "О ужасное это создание из обезьян... думая [так], она снова пришла в растерянность." — подстрочник gives no reason for renewed confusion beyond the thought itself. This is a good contrastive note.

**Verse 5**: Tilaka/Siromani/Bhūṣaṇa mostly paraphrase; Leonov's own note covers "bhāminī" omission — no additional content here.

**Verse 6**: Tilaka gives an ELABORATE philosophical passage about Sita's reasoning process — distinguishing "manorājya" (mental fantasy/wish, characterized as fickle, saṅkalpa-vikalpa) versus "buddhi" (fixed cognitive judgment) — arguing that if this were mere fantasy it would have no perceptible form, but here there IS a perceptible form, hence it's real (vāstava). Also "mandamandasvarā" — Tilaka explains this as Sita deliberately speaking very softly so the rākṣasīs won't notice/understand ("daivagatyā vāstavatve rākṣasyo mā jānantv ity ati-mandasvara-rodanam"). Siromani has similar content: "mandasvareṇa imaṃ vānaraṃ rākṣasyo na jānantv ity abhiprāyaḥ sūcitaḥ" — the SAME point (Sita's quiet crying is deliberate concealment from the rākṣasīs), so this is convergent, not contrastive, but IS a genuine narrative-psychological point not in подстрочник (which just says "тихо-тихо"). This deserves a single-commentator-style note (both agree, so I could cite both without needing full contrastive machinery, or note it's convergent). Given the brief's contrastive-first framing, when 2+ commentators AGREE (not diverge), it's not "contrastive" per the technical definition (divergence) — I'll draft this as a single-facet note citing both since they converge.

Actually the philosophical manorājya/buddhi distinction is Tilaka-only, while the "mandasvara = concealment from rākṣasīs" is shared by Tilaka+Siromani. Let me pick the concealment motif as it's the more concrete, translatable point and cite both commentators.

**Verse 7**: Own note already covers the vajra-scar point thoroughly (referencing Uttarakāṇḍa 35). Bhūṣaṇa/Siromani/Tilaka here mostly paraphrase or explain "yathoktakāram" (obedient to command) — is there anything beyond what's in Leonov's note? Let me check: Tilaka offers TWO readings for "yathoktakāram": either "obedient" (ājñākaram) OR (alternate) "as previously described" referring back to the earlier description (veṣṭitārjunavastrādyākāram) — a lexical ambiguity/interpretive choice. This is a minor point, likely too thin (interpretive nuance without a real image shift) — skip, or fold briefly. I'll reject as it doesn't add enough beyond Leonov's own already-thorough note.

**Verse 8**: Tilaka: "sā taṃ kapirūpaṃ rāvaṇam ity eva samīkṣya bhṛśaṃ visañjñā..." — Tilaka explicitly states Sita mistook Hanuman for Rāvaṇa in monkey-disguise (a specific identification), while Siromani ALSO says the same: "taṃ hanūmantaṃ samīkṣya rāvaṇatvena vitarkya gatāsukalpā" — both agree Sita thought it was Rāvaṇa in disguise. Bhūṣaṇa doesn't specify who she thought it was, just "vikṛta-vānara-veṣa-darśanena mūrcchitā" (fainted from seeing the deformed monkey-form). This IS a genuine addition: подстрочник gives no reason for her fainting beyond seeing him; Tilaka+Siromani specify she thought it was Rāvaṇa in disguise (echoing her prior fear pattern from the abduction). This connects thematically to sarga 30's already-drafted note about Rāvaṇa-disguise fear (5.30.18) — reinforcing that motif here too, which is a nice narrative link. DRAFT candidate (convergent Tilaka+Siromani vs. Bhūṣaṇa's vaguer version — arguably contrastive since Bhūṣaṇa doesn't specify Rāvaṇa).

Let me treat this as contrastive: Tilaka & Siromani specify Rāvaṇa; Bhūṣaṇa doesn't name a specific fear. Actually for contrastive framing we need actual divergence in interpretation, and here Bhūṣaṇa is just less specific, not contradicting. I'll draft as single/convergent citing tilaka+siromani, noting Bhūṣaṇa leaves it unspecified is optional color, not necessary.

**Verse 9**: Own note thoroughly covers this (śāstra prohibition of monkey-dreams). Bhūṣaṇa/Siromani: "svapne vānaradarśanaṃ bandhu-vināśakaram iti bhāvaḥ" (Bhūṣaṇa: seeing a monkey in a dream is inauspicious — portends destruction of kin) — that's a specific gloss on WHY it's inauspicious (destruction of relatives specifically, not general ill fortune) which Leonov's note doesn't specify (it just says "shastras forbid/predict misfortune"). This might be worth a small addition — but let's check if it's substantive enough. Leonov's note: "chтобы отвести от своих близких беду, которую предвещает увиденная во сне обезьяна" — wait, Leonov's OWN note already explicitly connects the dream-monkey to danger for her relatives/blessing for Rama-Lakshmana-Janaka. So Bhūṣaṇa's "bandhu-vināśakaram" is essentially already captured. REJECT — duplicates own note.

**Verse 10**: Tilaka/Bhūṣaṇa/Siromani — elaborate logical syllogism (no sleep because no happiness because separated from Rama, therefore this can't be a dream) — this is basically restating/formalizing what's already in подстрочник (which itself is already a logical statement). Pure logical restatement, no new content. REJECT.

**Verse 11**: Siromani has an interesting note: "kathāṃ śṛṇomi ity asya na aprasiddhiḥ tri-jaṭayā kadācid āgata-vibhīṣaṇānucarībhiś ca rāma-kathāyāḥ kathyamānatvāt" — Siromani explains WHY Sita's claim "I hear tales of him" isn't baseless — she has heard Rāma-kathā from Trijaṭā and from Vibhīṣaṇa's servant-women visitors. This is a genuine textual cross-reference clarifying a potentially puzzling claim (how would Sita hear Rāma-stories in captivity?) — grounding it in the narrative (Trijaṭā's role, established earlier in sarga 27's dream narration, and mentions of Vibhīṣaṇa's household women visiting). подстрочник doesn't explain how she'd hear such tales. DRAFT candidate — genuine narrative-grounding note, single commentator (Siromani only).

**Verse 12**: Tilaka: "uktam evārtham vivṛṇoti" (elaborates the same point) — grammar/structural comment. Bhūṣaṇa: text reproduction. REJECT.

**Verse 13**: Both Bhūṣaṇa and Siromani give the SAME logical structure (if it were a mere mental fantasy/manoratha, it would have no form; but this has a clear form and speaks to me, therefore not manoratha) — this is essentially restating подстрочник's own logic (which already says exactly this). Siromani ALSO adds an extra clause: "ataḥ [hetuḥ...] ... tathāpi tad-gata-sarva-bhāvā... etena pratyakṣato rāma-lābham antarā duḥkha-nivṛttir na bhaviṣyati iti sūcitam" — this seems to be content bleeding from verse 12 (misattached). Not new. REJECT.

**Verse 14**: Siromani: pure paraphrase of the prayer. Own etymological note on Vācaspati already exists in Phase-1. REJECT.

**Verse "56"**: ghost/misattached verse number with no text — content "rurodety ardham. mandaṃ rākṣasyaḥ śrutvā kim idam iti vicārayiṣyantīti bhayeneti bhāvaḥ" — this duplicates the concealment-motif already covered under verse 6 (mandamandasvarā — fear rākṣasīs will hear/investigate). REJECT — no independent text, duplicative.

Now let me finalize and write sarga 32's output.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_32_candidates.json
Now validate and write to actual output.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 32 done. Now sarga 33 — the largest (40 verses, 7 ambiguous markers).

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_33_leonov_notes.json
Interesting — a note at 5.33.11 explicitly says "средневековые комментаторы расходятся" (medieval commentators disagree) on vyañjanāni vs lakṣaṇāni but doesn't spell out the divergence — this is exactly a contrastive-note opportunity if the commentary text spells out what the actual disagreement is. Let's check the verses and phase1 notes now.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_33_phase1_notes.json
Now let's read the segmented verses for sarga 33.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_33_verses.json
Let me read the rest of the file.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_33_verses.json
Let me see the remainder.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_33_verses.json
Good, I have all 40 bundles for sarga 33. Let me now verify the total count.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
40 confirmed (32 sequential real verses + verse "57" ghost + 7 ambiguous merged ranges). Now let me go through verses 1-32 and 57 carefully for draftable content.

**Verse 1**: Tilaka: "kṛpaṇo mātuḥ sītāyā duḥkhadarśanād dīnaḥ" — glosses "kṛpaṇaḥ" as Hanuman appearing pitiable/humbled BECAUSE OF seeing Sita's suffering (as if her sorrow affects even him, "like a mother's grief"). Also "dūrāt praṇipatya tata upasṛtya samīpam āgatya" — bowing from a distance THEN approaching (already covered in Leonov's own note). The "mātuḥ" (like [seeing] a mother's grief) framing is interesting but subtle — could be too thin. Let's check: подстрочник already conveys "скромно одетый, выглядящий ничтожным". Tilaka's addition (his humility stems specifically from empathetic reaction to Sita's visible suffering, likened to a mother) is a small but real interpretive point. Borderline — I'll likely reject as thin/paraphrase-adjacent, since Leonov's own note already covers the "bowed from afar" detail which was the more substantive point.

**Verse 2**: Tilaka: "atha liṅgaiḥ sīteti niścaye 'pi tayaiva sākṣād vācayitum ajānann iva pṛcchati" — Tilaka explains WHY Hanuman asks "who are you?" even though he's already certain (from the signs/liṅgas) that this is Sita: he wants HER OWN voice to confirm it directly (sākṣāt vācayitum), pretending not to know. This is a genuine narrative-psychological point — Hanuman's question is rhetorical/strategic, not genuine uncertainty. подстрочник gives no such framing. DRAFT candidate — matches M.G.'s preference for narrative-function observations.

**Verse 3-9**: These are Hanuman's rhetorical questions (are you a goddess? apsara? Rohini? Arundhati?...) — mostly text reproduction by Bhūṣaṇa, structural connectives by Siromani/Tilaka ("ka nv ity ādi ślokadvayoktārthasyaiva prapañcaḥ" = "elaboration of the same point made in the previous two verses" — grammar/structural note). Nothing distinctive beyond подстрочник itself. REJECT block.

**Verse 8** (Arundhatī): Tilaka: "pātivratyād arundhatītva-śaṅkā" — the suspicion that she's Arundhatī arises specifically BECAUSE OF her wifely devotion (pātivratya) visible in her demeanor — this connects the wild guess to a visible trait (chastity/devotion), not random. This is a fine point but might be too thin given Phase-1 already has a rich note on Arundhatī. REJECT — the pātivratya-link is implicit already in why one would guess Arundhatī (an already devotion-themed goddess), not a big reveal.

**Verse 10**: Bhūṣaṇa: "devīṃ devastriyam. saṃjñāvadhāraṇāt saṃjñāyate anayeti saṃjñā lakṣaṇam. rājalakṣaṇa-niścayād ity arthaḥ" — glosses "saṃjñāvadhāraṇāt" as "from ascertaining royal marks/insignia" rather than "mentioning the king's name" — this is actually a DIFFERENT reading from what Leonov's подстрочник implies ("упоминаешь имя царя" = mentioning the king's name). Let me check — подстрочник says "по тому, что ты упоминаешь имя царя [Рамы]" (because you mention the king's name), but Bhūṣaṇa's gloss suggests "saṃjñā" here means "royal mark/sign" (lakṣaṇa) rather than "name," i.e., "from ascertaining the royal insignia [on your body]" — that's a genuinely different construal! This could be a strong textological/interpretive note: подстрочник follows one reading (name-utterance) while Bhūṣaṇa suggests another (bodily royal marks). But wait — Leonov's own note for verse 10 is about "bhūmisaṃsparśanāt" (feet touching ground = mark of mortality vs. divinity), not about saṃjñāvadhāraṇāt. So this is a fresh point not covered by Leonov's own note. Let me check if this is genuinely divergent or just an alternate phrasing. Given "rājñaḥ saṃjñāvadhāraṇāt" — "sam-jñā" = also can mean "name" (from sam+jñā, cognition/name) OR "sign/token" (lakṣaṇa) — Bhūṣaṇa explicitly glosses it as rāja-lakṣaṇa-niścaya (ascertaining royal-marks), which reinterprets what Sita is doing: not simply "you say the king's name" but "I can tell from your discernment of royal signs/insignia [on Rama]" — actually rereading, this seems to be about HANUMAN discerning something about Sita via her having identified royal marks, OR it could mean Sita's precise knowledge of royal protocol/identification marks marks her as non-divine (since a goddess wouldn't need lakṣaṇa to identify a king — she'd just know). This is subtle enough that I should present it as a genuine alternate construal: подстрочник reads "poминаешь имя царя", Bhūṣaṇa's gloss suggests "distinguishing royal insignia" instead. This is worth drafting as a textological/interpretive note (kazansky Б), single-commentator (Bhūṣaṇa).

**Verse 11**: Own note already extensively covers this (vyañjanāni/lakṣaṇāni synonym distinction — flagged as commentators disagreeing but not detailed in Leonov's note; and "bhūmipālasya" = Rāma specifically, per Tilaka). Let's look at the actual commentary content: Siromani here (misattached, actually about verse 10-11 combined) explains what vyañjanāni/lakṣaṇāni refer to via the AMBIGUOUS bundle 5.33.1213: "vyañjanāni stanajaghanādīni... lakṣaṇāni śubhāvartarekhādi-sāmudrika-lakṣaṇāni" — Bhūṣaṇa (in the ambiguous 1213 bundle) DOES spell out the distinction explicitly: vyañjana = bodily marks like breasts/hips (stana-jaghana, physical secondary sexual characteristics), lakṣaṇa = sāmudrika (palmistry/physiognomy) signs like auspicious spiral-marks (āvartarekhā). This is a genuinely interesting textological distinction (vyañjana=visible bodily traits vs lakṣaṇa=technical physiognomic signs) that Leonov's note flagged as unresolved ("средневековые комментаторы расходятся, но не поясняется в чём"). However, this content lives in the AMBIGUOUS merged-range bundle 5.33.1213, which per reject rule (e) should generally be rejected as "no independent gloss" UNLESS I can determine it attaches cleanly to verse 11. Let me check — the ambiguous_marker=true bundle 5.33.1213 has ONLY Bhūṣaṇa's vyañjana/lakṣaṇa distinction, no verse text. Given verse 11 (5.33.11) itself already has Bhūṣaṇa text reproduction and Siromani content mostly about the OTHER lexical points, and the specific vyañjana/lakṣa�a distinction sits in the ambiguous "1213" bucket — but the content clearly and unambiguously belongs to THIS verse (11), since verse 11 itself contains "vyañjanāni ... lakṣaṇāni ca lakṣaye" verbatim. The rule says: "If a bundle's pratika_check shows an unverified anchor with a suggest_verse, treat the attachment as suspect — draft only if the note survives on either verse, and say so in why_proposed." Here it's not a suggest_verse case but an ambiguous_marker merged-range token which the reject discipline explicitly calls out as reject-by-default (rule e: "ambiguous_marker merged-range token («no independent gloss»)"). However, the content here is clearly NOT ambiguous in referent — it's an unambiguous elaboration of verse 11's exact vocabulary. Given the strength of directly answering Leonov's own flagged puzzle (what's the difference between vyañjana and lakṣaṇa?), I think this is worth drafting attached to verse 11 itself (since verse 11 bundle exists separately and is NOT ambiguous), treating the "1213" ambiguous bundle as sourcing material that supports/confirms the verse-11 note, but I will draft the note under 5.33.11 (not 5.33.1213) and reject 5.33.1213 separately per rule (e), citing that its content was folded into 5.33.11's note.

Let me re ​-examine: is this appropriate? The instructions are clear that I must not draft FROM the ambiguous bucket itself, but verse 11's own bundle already contains "vyañjanāni... lakṣaṇāni..." from Bhūṣaṇa (text reproduction) and Siromani's extended discussion. Let me check if Siromani's own text in verse 11 gives the same distinction independently. Looking back at 5.33.11's siromani text: "yāni vyañjanāni bodhakāni te lakṣaṇāni asādhāraṇa-cihnāni lakṣaye" — Siromani glosses vyañjanāni = "bodhaka" (indicative signs) and lakṣaṇāni = "asādhāraṇa-cihnāni" (extraordinary/uncommon marks) — this is Siromani's OWN gloss within verse 11's own (non-ambiguous) bundle, distinguishing the two terms differently from Bhūṣaṇa's later (ambiguous-bundle) gloss (stana-jaghana vs sāmudrika-lakṣaṇa). 

This is genuinely rich: Siromani (in verse 11's clean bundle) reads vyañjana as general "indicative marks" and lakṣaṇa as "special/rare marks" (a difference of degree), while Bhūṣaṇa (whose fuller gloss appears attached to the ambiguous "1213" bucket, but the SAME distinction is implicit in his commentary) reads them as two different CATEGORIES entirely — bodily secondary-sex-traits vs. formal palmistry-signs. This is EXACTLY the kind of divergence Leonov's own note gestures at ("commentators disagree on the semantic difference") without resolving. Given I can attach a contrastive note cleanly to verse 11 itself using Siromani's own-bundle content, and only USE the ambiguous bundle's Bhūṣaṇa content as supporting confirmation (noting it in why_proposed), I'll draft this as a contrastive note on 5.33.11, complementing Leonov's own note.

Let me also check Siromani's note in v.11 about "Rāvaṇeneti" — that's actually content for verse 12 (misattached), duplicate of verse 12's own content.

**Verse 12**: Tilaka gives a notable narrative-frame note: "rākṣasīnāṃ niśā-jāgarataḥ nidrā-jāḍyāt tri-jaṭā-svapna-śravaṇa-janya-bhayonā ātma-trāṇāya sītaika-śaraṇatvena upekṣaṇāc ca daivānugrahāc cāpratyūhaḥ sītā-hanūmator saṃlāpaḥ iti bodhyam" — Tilaka explains WHY the rākṣasīs (guards) don't interrupt/notice this long conversation between Sita and Hanuman despite standing watch all night: they are drowsy from staying awake all night, AND fear-paralyzed after hearing Trijaṭā's dream (which predicted Rāvaṇa's doom via Rama), AND they've given up watching Sita closely since Sita alone is now beyond escape anyway (nowhere to flee), AND divine grace. This is a genuinely valuable narrative-mechanical point — explaining the plausibility of an extended dialogue that подстрочник doesn't address at all (why aren't the guards intervening?). This deserves a DRAFT — matches M.G.'s valued "narrative-function observations."

Bhūṣaṇa here also adds: "saḥ rākṣasīṣu suptāsu labdhāvasara ity arthaḥ. kṛpaṇaḥ sītā-dausthya-darśanena dīnaḥ. jānann api vaidehyaiva vācayitum abravīt" — similar point (rākṣasīs asleep = opportunity) plus reaffirms that Hanuman ALREADY knows it's Sita but wants her own confirmation (same point as verse 2's Tilaka note — I should avoid redundancy; since verse 2 already covers "wants her own voice to confirm," I'll fold the "guards asleep" reasoning into this verse-12 note and keep verse 2's note focused on the rhetorical-question motif, distinct facets).

**Verse 13**: Tilaka: "sītā rāmaṃ stauti dadyād iti" — cryptic gloss, likely misattached grammar pointer to verse 25's "dadyāt" line. Siromani: paraphrase of atimānuṣa (already Phase-1). REJECT.

**Verse 14**: Bhūṣaṇa explains "drumāśritam" (given by Kostina's flagged issue — wait, that's verse 14 in Leonov's list too!). Let me check: Bhūṣaṇa: "drumāśritaṃ drumamūlāśritam. so 'vatīrya iti druma-avataraṇasya pūrvam uktatvāt. yadvā pūrvam agrād avataraṇam uktam iti jñeyam" — this reasoning IS the exact point Kostina's own note already covers (drumāśritam = at the foot of the tree per Tattvadīpikā and Bhūṣaṇa, contra a literal "on the tree" reading that would contradict context since he already descended in v.1). This duplicates Leonov's own note fully. REJECT.

**Verse 15**: Siromani/Bhūṣaṇa mostly paraphrase, but Bhūṣaṇa gives an interesting point: "śatrusainyapratāpinaḥ śatruṣu jīvatsu na me śvaśuro jīvitavān. sa ced idānīṃ varteta katham aham etādṛśīm avasthāṃ prāpnuyām iti bhāvaḥ" — Bhūṣaṇa reads the epithet "conqueror of enemy armies" ironically/poignantly: Sita implies that if her father-in-law (a conqueror who vanquished all enemies) were alive NOW, she wouldn't be in this wretched state — an implicit lament that Daśaratha's protective power has ended with his death, and his epithet becomes bitterly ironic given her current plight. This is a real literary/narrative point — подстрочник gives only the epithet flatly. DRAFT candidate.

**Verse 16-18**: Mostly paraphrase/grammar. Own note covers "vaidehasya" omission (v16). REJECT block, except let me double check v18 for the trayodaśa content (Phase-1 already covers it).

**Verse 19-21**: Tilaka in v.19: "idānīṃ devayonitvāśaṅkāṃ svayam eva nivartayati rodanāditi. aśru-sambandho bhū-sparśaś ca devānāṃ nāsti iti śrutam, tadvatvāt tvāṃ devīṃ na manye" — wait, this is misattached content from verse 10 (about devī/goddess-suspicion refutation via tears/ground-touching) leaked into verse 19's bundle. Not new — duplicate of verse-10 content which itself connects to Leonov's own note there (bhūmisaṃsparśanāt = gods don't touch ground). REJECT — content misattached and duplicative.

**Verse 20**: Siromani here has misattached content actually about verse 21 (the "yadi" conditional about not making the promise false, Rāma should go to the forest) — paraphrase. REJECT.

**Verse 21**: Tilaka: "tad deva-asure yuddhe varadāna-rūpam" — clarifies that the boon (varadāna) was originally granted in the context of the war between gods and asuras (i.e., Kaikeyī saved Daśaratha's life in battle and was granted two boons then) — this is useful background info not in подстрочник, connecting to the well-known epic backstory of Kaikeyī's boons. Phase-1 already has a note on varadāna (v.22) but doesn't mention the deva-asura-yuddha origin story specifically. Let me check Phase-1's varadāna note again — it discusses the legal mechanics (satyābhisaṃdha framework) but doesn't mention this is from the deva-asura war. This could be a good addition. DRAFT candidate (realia/textual background, В type since it's mythic backstory).

**Verse 22**: Siromani paraphrase (already partly duplicated by Leonov's own extensive note quoting Grintser's translation of the same scene). REJECT.

**Verse 23**: Own note already flags need for clarification "у старшего сына" — Siromani here gives: "tatas tasmāt hetoḥ rudan rājā jyeṣṭhaṃ putraṃ rājyaṃ vana-rājyam ayācata" — interprets "rājyam ayācata" as specifically "vana-rājyam" (forest-kingship/exile), a curious gloss reading "rājyam" not as "kingdom" but as "banishment-order" — that's odd but could be a genuine textual nuance (the king begged his ELDEST son to accept VANA-rājya = "sovereignty of exile," i.e., to go into exile, rather than "requested the kingdom [for Bharata]"). Let me reconsider — actually this reading changes the whole meaning of "rājyam ayācata": instead of "begged for the KINGDOM [from Rama, to give to Bharata]" it becomes "begged [Rama to accept] exile-kingship" — a distinct construal that resolves the ambiguity Kostina flagged (whose kingdom, given to whom). Actually wait, this might resolve exactly the confusion Kostina flagged: "Комм., что у старшего сына" (comment on "at the eldest son's [place]") — suggesting Kostina wanted clarification about WHOSE kingdom is being requested from whom. Siromani's "vana-rājyam" gloss offers exactly this disambiguation. Let me draft this as complementing Leonov's flagged gap.

Given the density of good options here, let me be selective and prioritize the strongest few to keep to a reasonable accept rate, while not being stingy about clearly valuable narrative-function/doctrinal-frame notes matching M.G.'s stated preferences. Let's continue checking verses 24-32.

**Verse 24**: Siromani/Tilaka/Bhūṣaṇa paraphrase of Rāma's dutiful acceptance. REJECT.

**Verse 25**: Bhūṣaṇa gives only text reproduction; Phase-1 has extensive dharmaśāstra crossref already. REJECT.

**Verse 26**: Bhūṣaṇa: "jananyai kausalyāyai" (identifies "mother" as specifically Kausalyā, not just any mother) — this is already covered in Leonov's own note ("имеется в виду Каусалья"). REJECT — duplicates own note.

**Verse 27**: Tilaka gives internal verse-linking notes (grammar); Siromani/Bhūṣaṇa mostly paraphrase. REJECT.

**Verse 28**: Bhūṣaṇa gives an extended point: even though Lakṣmaṇa's adopting the bark-garment (kuśacīra) technically happened AFTER Rāma's own (since Rāma went first), the verse says "prāg eva" (even beforehand) — Bhūṣaṇa explains this is a rhetorical exaggeration (atiśaya) emphasizing Lakṣmaṇa's eagerness/haste to serve, not literal chronological precedence. Also ties to Lakṣmaṇa's vow "ahaṃ sarvaṃ kariṣyāmi" and his birth being predestined for forest-service ("sṛṣṭas tvaṃ vanavāsāya" — a quote about Lakṣmaṇa being "created for forest-dwelling"). This is a nice doctrinal/characterization point about Lakṣmaṇa's devotion — but is it beyond подстрочник enough? подстрочник already conveys "eagerness" via "прежде" (before/earlier). The specific mythic-quote framing ("sṛṣṭas tvaṃ vanavāsāya" — you were created/destined for forest exile) is a real addition — a divine-predestination point about Lakṣmaṇa's character that doesn't appear elsewhere. Borderline candidate — let me weigh against other strong ones. I'll include this if I have room; it fits "mythic identifications behind names/similes" preference loosely (predestination motif). I'll draft it.

**Verse 29**: Siromani/Bhūṣaṇa paraphrase. REJECT.

**Verse 30**: Bhūṣaṇa/Siromani paraphrase. REJECT.

**Verse 31**: Siromani explains: "dvau māsau jīvitānugrahaḥ kṛtaḥ... rāma-anāgamane tyaktum icchāmi" — clarifies WHY exactly two months (Rāvaṇa's deadline), tying it to "if Rama doesn't come" — but this is basically already in подстрочник. REJECT — restates подстрочник.

**Verse 32 (ghost, no text)**: content = repeat of verse 31 + colophon. No independent value. REJECT.

**Verse 57 (ghost, no text)**: Bhūṣaṇa: "surāṇām ity ādiṣu nirdhāraṇe ṣaṣṭhī. kā tvaṃ kasya sambandhinī ity arthaḥ" — pure grammar note (genitive case usage in v.5's "surāṇām"). REJECT — grammar only, duplicative of already-rejected v.5.

Now let's handle the ambiguous merged-range bundles (5.33.1213, 1315, 1618, 1819, 2324, 2526, 3031). I already plan to fold 1213's content into verse 11's note and reject 1213 itself. Let's check the others:

- **5.33.1315**: Tilaka — "bhūmipālasya rāmasya mahiṣīti me matiḥ... ataḥ rāvaṇena janasthānād balāt pramathitā... yathā hīti apratyakṣa-anubhava-viṣayām ity arthaḥ" — this actually confirms/repeats verse 11's "bhūmipālasya = Rāma" point (already in Leonov's own note for v.11) and verse 13's content. No new independent point. REJECT per rule (e).
- **5.33.1618**: Tilaka: "ahaṃ nāmnā sītā iti" — trivial gloss ("I am named Sita" = just restating verse 16's text). REJECT per rule (e).
- **5.33.1819**: Bhūṣaṇa — elaborate grammar/semantic analysis of "samāḥ" (12 years, accusative of extent), and a point that "mānuṣān" implies Sita's humanity isn't inherent/natural but adopted through her marriage-experience ("na ātmano mānuṣatvaṃ svābhāvikam iti sūcyate") — this is interesting (a subtle theological point: Sita's enjoying "human pleasures" implies her nature ISN'T inherently human, hinting at her divine origin, consistent with the goddess-questions asked earlier in this very sarga!). This connects nicely to the earlier goddess-identity theme (vv 5-9). However it sits in an ambiguous merged-range bucket (1819, verses 18-19) with no independent verse anchor — per rule (e), reject by default. Given the strength of the point, let me reconsider: is there a clean non-ambiguous verse it could attach to? The content is glossing "mānuṣān bhogān" from verse 17 (samā dvādaśa... bhuñjānā mānuṣān bhogān), which has its OWN clean bundle (verse 17) already reviewed above (I rejected it as paraphrase). Let me revisit — verse 17's own bundle doesn't contain this deeper point (it was in the ambiguous "1819" bucket instead, misattached). Given the instruction to draft "only if the note survives on either verse, and say so in why_proposed" applies specifically to pratika_check-suggested reattachment, not necessarily to ambiguous_marker merged buckets generally — but the reject-discipline rule (e) explicitly names ambiguous_marker as a default-reject category. I'll follow the brief strictly here: reject 1819 citing rule (e), since it's a genuinely merged/ambiguous token not confidently anchored to one verse, despite being interesting content. This preserves the discipline given in the brief.
- **5.33.2324**: Bhūṣaṇa — "saḥ ... devyāḥ sambandhi svakṛtaṃ varadānaṃ smṛtvā kaikeyyāḥ vacanaṃ śrutvā mumoha" — pure paraphrase repeat of v.22/23. REJECT per rule (e).
- **5.33.2526**: Bhūṣaṇa — "abhiṣekāt paraṃ priyaṃ pitur vacanaṃ vivāsayācanā-rūpam" — glosses "father's words dearer than coronation" as specifically "in the form of a request for exile" — minor gloss, paraphrase-adjacent. REJECT per rule (e).
- **5.33.3031**: Bhūṣaṇa — "atra gambhīra-śabdena duṣpraveśatvam, darśana-śabdena svarūpam apy ucyate" — grammar-lexical note on "gambhīradarśanam" (both "hard to penetrate" AND "of profound appearance"). REJECT per rule (e) — merged range, thin lexical point.

Now let's also double check verse 10's Bhūṣaṇa content once more, and finalize my full draft list: verses 2, 10, 11, 12, 15, 21, 23, 28. That's 8 drafts out of 40 (20%) — a bit high relative to the "5-10%" guidance. Let me reconsider more critically and trim to the strongest.

Let me re-rank by strength:
1. **Verse 12** (guards asleep/distracted — narrative mechanics): STRONG, unique, directly addresses a real narrative gap.
2. **Verse 2** (rhetorical question strategy): STRONG, narrative-psychological, distinctive.
3. **Verse 11** (vyañjana/lakṣaṇa contrastive, resolves Leonov's flagged puzzle): STRONG, directly complements a flagged Leonov gap, contrastive.
4. **Verse 15** (bitter irony of "conqueror of enemies" epithet): MEDIUM-STRONG — genuine literary point.
5. **Verse 21** (varadāna origin in deva-asura war): MEDIUM — useful background, somewhat encyclopedic/factual rather than commentator-interpretive; borderline whether this counts as "commentator adds something" vs just backstory. Actually this IS what Tilaka says explicitly ("tad deva-asure yuddhe varadāna-rūpam") — a commentator gloss, legitimate.
6. **Verse 23** (vana-rājyam reading, resolving Kostina's flagged confusion): MEDIUM-STRONG — directly complements a flagged own-note gap.
7. **Verse 28** (Lakṣmaṇa predestination quote): MEDIUM — nice but more decorative.
8. **Verse 10** (saṃjñā = royal marks vs name-utterance): MEDIUM — genuine alternate construal.

Given 40 verses and target ~5-10% (2-4 notes), but this sarga is unusually rich in Hanuman-Sita first encounter material with several genuinely valuable points, I'll aim for around 6, keeping the strongest and cutting the two weakest (10 and 28), since 10 is subtle/uncertain in translation impact and 28 is more decorative/character color rather than resolving something concrete.

Let me finalize: DRAFT verses 2, 11, 12, 15, 21, 23 (6 notes = 15%, still elevated but justified by density of real complements-Leonov content in this pivotal encounter scene). Let me reconsider once more — the brief says "Expected accept rate ~5-10% — depth, not bulk; do NOT pad" as an overall corpus guideline, and individual sargas can vary based on real content richness (sarga 27 had 4/64=6.25%, sarga 30 had 5/~44). Given this sarga is THE first-contact scene (high commentator density, many identity-questions, several genuine own-note-complement opportunities), I think 6 is defensible, but let me cut to 5 by dropping the weaker "verse 10" idea (already dropped) and reconsidering verse 21 vs 23 — both are good, I'll keep both since they're genuinely distinct (mythic backstory vs. textual disambiguation).

Final list: 2, 11, 12, 15, 21, 23 = 6 drafts, 34 rejects (40 total). Let me write this out now.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sarga_33_candidates.json
Now let's validate and write to the actual output path.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
All four sargas verified and written. Let me do a final sanity pass across all four output files to confirm they're valid JSON, no BOM, and schema-complete.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
All four files are valid: no BOM, counts reconcile (drafted + rejected == considered), one file per sarga. Let me clean up the scratch files (session-scoped, not required to keep) — leaving them is fine since they're in the scratchpad, not the repo.

All four sargas are complete.

sarga 29: 8 considered / 3 drafted / 5 rejected / 0 contrastive
sarga 31: 27 considered / 2 drafted / 25 rejected / 0 contrastive
sarga 32: 15 considered / 4 drafted / 11 rejected / 1 contrastive
sarga 33: 40 considered / 6 drafted / 34 rejected / 1 contrastive

Outputs written to [sarga_29_candidates.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch3/sarga_29_candidates.json), [sarga_31_candidates.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch3/sarga_31_candidates.json), [sarga_32_candidates.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch3/sarga_32_candidates.json), [sarga_33_candidates.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch3/sarga_33_candidates.json).

_Dr. Mārcis Gasūns_
