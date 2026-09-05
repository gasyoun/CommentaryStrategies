_Created: 07-07-2026 · Last updated: 05-09-2026_

# Agent log agent-a3f1622632298c32d

_Model: `claude-sonnet-5`; extracted by scripts/export_agent_logs.py; raw transcript alongside (.jsonl) holds the full record incl. tool results._


I'll start by reading the drafting brief and then the three sarga input files.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\DRAFTING_BRIEF.md
Now let me look at the input files for sarga 20, plus the two supporting note sources.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_20_segmented.json
Let me continue reading the rest of sarga 20.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_20_segmented.json
Now let me pull the relevant slices from `leonov_own_notes.json` and `sundara_commentary_to_add.json` for sarga 20 using a quick Python script, and check sarga 21 and 23 files too.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && m
I'll write scratch scripts to a file and redirect output to files in the scratchpad to avoid console encoding issues.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\slice_notes.py
This is a small scratch-slicing script explicitly directed by the brief itself ("Extract your sarga's slice with a short Python script to a scratch file") — not a reusable helper to check prior art for. Proceeding.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Good, the slicing worked (the "sample item keys" line just picked up the `_meta` dict as items[0], but the shloka-prefix filter still worked correctly on the real entries). Let me verify the sundara structure a bit more and then read the sliced files.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Good — it's a top-level list of 904 items. Now let's read the sliced files.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_sarga_20.json
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sundara_sarga_20.json
Now let me read sarga 21 and 23 segmented files, and their sliced note files.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_21_segmented.json
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_21_segmented.json
Now let me check the leonov and sundara slices for sarga 21.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_sarga_21.json
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sundara_sarga_21.json
Now let's look at sarga 23.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_23_segmented.json
Now the leonov and sundara slices for sarga 23.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_sarga_23.json
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sundara_sarga_23.json
I now have complete data for all three sargas. Let me mark a chapter and begin drafting sarga 20.

- 🔧 `mcp__ccd_session__mark_chapter`
Now let me work through sarga 20 verse by verse against the brief's criteria. Let me organize my analysis systematically for each verse bundle in sarga 20 (verses considered: all verse entries with actual sanskrit_iast content — the ambiguous_marker merged-range entries at the end are excluded per rule (e), but let me check the brief's counting convention first).

Looking at the data: sarga 20 has verses 1-9, 11-36 with full data (real verse entries with `sanskrit_iast`), plus verse "56" (isolated, no sanskrit_iast/leonov_ru — actually a preambleish orphan), and several merged-range ambiguous entries (810, 1112, 1419, 2122, 2425, 2830, 3132, 3134, 3334, 3536). Per rule (e) reject discipline, merged-range ambiguous_marker tokens get "no independent gloss" rejects. Let me count real verses to consider.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
This confirms: 33 real verse bundles (with sanskrit_iast) + verse "56" (no sanskrit_iast/leonov_ru, ambiguous_marker false but empty content — this is a stray commentary snippet, treat like the merged-range ones) + 10 ambiguous merged-range entries = 44 "considered" entries total (excluding the true duplicate range entries would undercount; the brief says one reject per verse so counts reconcile). Let me treat all 44 non-preamble entries as "considered" (verse 56 is anomalous, treating it like an ambiguous_marker entry for rejection purposes since it has no independent verse text).

Now let me go through the 33 substantive verses first and decide draft/reject.

- 🔧 `mcp__ccd_session__mark_chapter`
Let me now carefully work through each verse of sarga 20, applying the brief's rules.

**5.20.1**: Tilaka/Bhusana note parivṛtām elided "rakshasi"; Siromani commentary here is clearly misplaced (talks about "mat-prasādāt lalantyās" — belongs to a different verse, likely 22-23 area, a segmentation artifact). Leonov's own note (Kostina) already covers the "parivṛtām" ellipsis exactly. Reject — duplicates tier-1.

**5.20.2**: Leonov's own note already covers the adarśanam-as-question point. Reject — duplicates tier-1 (Kostina explicitly flags "не все придерживаются этой трактовки" but no second reading is given in the bundle to contrast). No draft.

**5.20.3-4**: Tilaka's commentary is misplaced (talks about "svadharma", clearly belongs to v.5-6 area). Bhusana/Siromani on 3 are surface-level (restate подстрочник). No net addition. Reject both.

Let me check sundara notes for v.5 (svadharma) — there are rich cross-text notes already covering this exact point (Manu 3.33, 10.97, BhG 2.31/3.35) as tier-2/Phase-1. Since Phase-1 already thoroughly covers svadharma at v.5, I should not duplicate. Let me check v.6 and v.7-9.

**5.20.5**: Sundara/Phase-1 already has THREE notes on svadharma at this verse (Manu 3.33, Manu 10.97, BhG 2.31/3.35). Bhusana here just quotes the verse. Reject — duplicates Phase-1.

**5.20.6**: Tilaka has an interesting variant-reading note (`एवं चैतदकामां त्वाम्` alternate pāṭha) that's not covered elsewhere. Let me check this more closely.

- 🔧 `Bash` — echo checking
Looking at verse 6's Tilaka commentary: it discusses a textual variant `"एवं चैतदकामां त्वाम्" इति पाठे एतद्रक्षोधर्मत्वम्` — an alternate reading where "evaṃ caitad akāmāṃ tvām" makes the "non-desire" a rākṣasa-dharma trait rather than describing Kāma acting freely. This is a genuine textual-variant note (kazansky_type Б) not covered by Leonov's own notes (which for v.6 don't exist in the slice) nor Phase-1. This is draftable.

Let me continue through the remaining verses systematically, checking each against tier-1/Phase-1.

**5.20.7**: Tilaka/Bhusana/Siromani all just gloss "praṇayasva" as "show affection/respect" — restates подстрочник. Reject.

**5.20.8**: Siromani has an interesting point: "asthāne'py" = even in a NON-mourning-appropriate place/occasion, one shouldn't wear ekaveṇī etc. But Phase-1 already has a rich note at V.20.8 on ekaveṇī (mourning/vow marker, Draupadi parallel). Bhusana/Tilaka just restate/repeat the подстрочник. Reject — Phase-1 covers ekaveṇī's meaning; the Siromani point about "asthāne" grammatically is too technical/invisible to a Russian reader without Sanskrit.

**5.20.9**: Siromani groups this with v.10-11 with "श्लोकद्वयेकान्वयि" - a syntactic bridging note not visible to reader. Reject.

**5.20.11**: Tilaka: "anarhā bhūṣaṇānām iti śeṣaḥ" — supplies ellipsis "unworthy OF ORNAMENTS" — minor grammatical supply, not really adding image/content beyond подстрочник (which already says "укрась тело драгоценностями"). Reject.

**5.20.12**: All three commentators gloss "srotasvinām" as "rivers/streams" — restates подстрочник simile. Reject.

**5.20.13**: Siromani has a notable point: the "unmatched beauty" hyperbole extends to "even Brahmā (pitāmahaḥ) himself would not transgress" (this actually belongs to v.14, appears misassigned to v.13's block). Tilaka/Bhusana on v.13 just describe विश्वकृत् = creator stopped after making her — restates подстрочник. Reject v.13.

**5.20.14**: This is the "kaḥ punar nātivarteta" variant — Leonov's OWN note already extensively covers this (Tilaka/Tattvadipika read ativṛt as "kṣubh"; Siromani reads it as "svauddhatya prakāś"; Kostina explicitly asks for the note to be developed, also cites Goldman). This is already in tier-1. However — the brief says: "When Leonov/Kostina ALREADY note the verse: do NOT auto-reject. If the commentator adds a genuinely distinct facet, DRAFT the note." Let's check: does the bundle add anything Kostina's own note doesn't? Kostina's note already names all three commentator readings (Tilaka/Tattvadipika="взволноваться", Widomani="выказывать волнение") — that's exactly the contrastive content. The bundle doesn't give tattvadipika text (this sarga only has 3 commentators in this bundle: tilaka/bhusana/siromani — wait, but Kostina's note mentions Tattvadipika, which isn't in this bundle's commentary object at all, meaning that note might reflect a different source view). Given Kostina's own note already states both readings almost verbatim, this would be a straight duplicate. Reject — duplicates tier-1 note in full.

**5.20.15**: Restates подстрочник (gaze fixed on each body part). Reject.

**5.20.16**: Siromani has a wordplay etymology: bhava→"bhavati bhāvayati" (she who dwells on/thinks of her husband) as folk-etymology for "Maithili" epithet used in vocative "bhava maithili" — actually re-reading: `भव इति। हे भवमैथिलि भवति भावयति नितरां स्वपतिं चिन्तयति सा एव मैथिली` — this glosses "bhava" as part of an epithet-vocative "bhava-maithili" = one who constantly thinks of her husband, rather than an imperative "be!". That's a real distinct reading not in подстрочник (which reads "будь моей женой, Майтхили" — the imperative reading) and not in tier-1 (Kostina's note for v.16 only flags "опущено обращение"). This is a genuine syntactic/semantic divergence worth a contrastive note (Siromani's construal vs. the straightforward imperative Leonov follows).

- 🔧 `Bash` — echo "checking v16 in more detail via already-read text"
Let me re-examine v.16 carefully. Tilaka and Bhusana both take "bhava" straightforwardly (bhava = imperative "be", matches подстрочник exactly — Tilaka glosses "mohaṃ" and "tava hetoḥ", Bhusana just quotes text). Only Siromani reads "bhava-maithilī" as a compound epithet. This is a genuine single-commentator divergent construal that changes the grammatical reading (imperative verb vs. vocative epithet) — draftable per the fallback rule (single-commentator gloss when it resolves a real translation choice). Good candidate, contrastive since Tilaka/Bhusana agree with the translation's reading and Siromani diverges.

**5.20.17-18**: Only Bhusana present, just quotes verse text, no interpretive content. Reject both.

**5.20.19**: Siromani has extra content about "asakṛt...bhagnāḥ" surāsurāḥ (gods and demons alike defeated) tied into v.20, and also references back to v.17 material (rāj­yaṃ dadāmi) misplaced. The core "pratibalaḥ = yuddhe jetā" gloss (Tilaka) restates подстрочник. Reject.

**5.20.20**: Bhusana glosses "vimṛditadhvajāḥ" = "flags broken/crushed" and "pratyanīkeṣu" = "amidst enemies" — restates подстрочник. Reject.

**5.20.21**: Siromani has an interesting logical bridge: "since you have no fear, therefore let the finest ornaments be prepared" — restates подстрочник's implicit logic; not a distinct fact. Reject.

**5.20.22**: Kostina's own note flags the present-tense-for-future point ("Увижу" — оригинал наст. время). Tilaka has additional content here bleeding in from elsewhere (`ललस्व... मत्प्रसादान्मयि प्रसादात्... वर्धमानायाः` — belongs to v.23 material). Nothing new beyond tier-1/подстрочник. Reject.

**5.20.23**: Bhusana/Siromani gloss "yatheṣṭam...prayaccha" and "ramyatām" — restates. Reject.

Let me now examine 25-36 for candidates.

**5.20.25**: Tilaka glosses ṛddhi = "parākramādi-sampad" (might/valor-wealth) and śrī = "dhanādi-sampad" (wealth-riches) — a genuine semantic differentiation between the two near-synonyms Leonov renders together ("богатства... могущество и славу"). This clarifies that ṛddhi ≠ śrī ≠ yaśas are three distinct registers (valor vs. wealth vs. fame), which the подстрочник flattens. This is a modest lexical distinction worth noting — but is it substantial enough? Let's weigh against the "restates подстрочник" reject criterion. The подстрочник already renders богатства/могущество/славу distinctly. Tilaka's split (ṛddhi=valor-related, śrī=wealth-related) actually differs somewhat from what "богатства" suggests for ṛddhi. This is borderline — I'll reject as it doesn't change the image, just labels near-synonyms.

**5.20.26**: Kostina's own note explicitly asks for commentary on "nikṣiptavijayaḥ" citing Goldman variant. The bundle's Tilaka/Siromani do NOT address this specific compound's meaning (they discuss gataśrī, jīvati-na-vā doubt). Siromani's note has interesting content: Ravana casts doubt "jīvati na vā" as a rhetorical device to quell Sita's affection for Rama ("शूर्पणखाविरूपादिकरणजनितताप­शान्तये... निवारयितुम्") — this is a distinct narrative-function point: Ravana's rhetorical strategy is explicitly linked back to Shurpanakha's mutilation and pacifying his own frustration. That's a genuine facet complementing Kostina's note (which is about translation of "nikṣiptavijayaḥ" itself, not about narrative motive). Let's check: does this complement Leonov's note? Kostina's note is purely lexical (word choice); Siromani's is about rhetorical/narrative strategy (why Ravana casts doubt on Rama's survival at all — as continuation/consequence of the Shurpanakha episode). This is genuinely different and valuable (M.G. valued "narrative-function observations"). Draftable as complements_leonov.

**5.20.27**: Tilaka just glosses "upalabhyate" as passive/optional reading variance in grammar (śyan-pratyaya) — too technical/grammar-invisible. Leonov's own note already discusses the purobalākaiḥ crane image. Reject.

**5.20.28-29**: This is the Hiranyakashipu myth reference. Tilaka has genuinely useful content: he explicitly names the source as Bhagavata ("iyaṃ ca kathā bhāgavate prasiddhā iti tīrthaḥ") and glosses "kīrtim" as "kīrti-tulyāṃ bhāryām" (a wife comparable to Kīrti — i.e., not just "Kīrti" but "a wife of Kirti's rank/comparable")... Actually wait, re-reading: "इन्द्रहस्तगतां कीर्तिं कीर्तितुल्यां भार्यामिन्द्रहृतां नारदमुखेन प्रार्थनया यथा हिरण्यकशिपुः प्राप्तवान्" — this says Hiranyakashipu got back "Kīrti-tulyāṃ bhāryām" (a wife comparable to Kīrti) that had been taken by Indra, through Narada's intercession/request. This is actually a variant myth-detail: not just "Kīrti fell into Indra's hands and Hiranyakashipu took her back," but that it was HIS WIFE (compared to Kīrti) taken by Indra, recovered via Narada's plea. Phase-1's note for V.20.28 already covers the Hiranyakashipu reference generally but doesn't mention the Narada-intercession detail or the "wife comparable to Kirti" reading. Let me check Phase-1's note text again: it says "Хираньякашипу... сравнивает себя... получившим Кирти (богиню, дочь Индры)". Tilaka's reading differs: it's not "the goddess Kīrti" literally, but "a wife equal to Kīrti" that Hiranyakashipu recovered from Indra through Narada's plea. This is a genuine divergent identification — draftable as complements_leonov / contrastive with Phase-1's own gloss. Actually, per brief scope, "complements_leonov" is only for Leonov/Kostina's OWN notes, not Phase-1 (which is a different comparison — Phase-1 IS a separate corpus). But rule (b) says "duplicates tier-1/Phase-1" is a reject reason UNLESS it adds a distinct facet — this applies broadly. I'll draft this noting it adds the Narada-intercession detail and reframes "Kīrti" as "a wife comparable to Kīrti" rather than the goddess herself, which is a genuinely different reading worth flagging even against Phase-1.

Let me continue checking remaining verses.

- 🔧 `Bash` — echo checking
**5.20.29**: Siromani: "dauda­sīnyaṃ nivārayitum" — this comment addresses Ravana's motive (dispelling Sita's indifference/coldness) — narrative-function, but minor; Bhusana just quotes verse. Phase-1 has a rich note on the pannaga/Garuda inversion already (Mahabharata Aranyaka parallel). No new facet beyond that. Reject.

**5.20.30**: Siromani has a notable point: "एतेन रावणस्य दयालुत्वं सूचितम्" — "this indicates Ravana's compassion/kindness" — i.e., the commentator reads Ravana's admission (he finds no pleasure with his own wives after seeing Sita's suffering) as evidence of a compassionate side to Ravana, a genuinely interesting characterization note not visible from подстрочник alone. This is a real interpretive facet (M.G. values "doctrinal frames," "narrative-function observations" — this is closer to a characterization observation). Let's check if Phase-1/tier-1 covers this. No such note found for v.30 in either slice. Draftable — single-commentator gloss revealing an interpretive facet about Ravana's characterization.

**5.20.31**: Siromani restates подстрочник (glosses aiśvaryam as "svāmitva" = mastery). Reject.

**5.20.32**: Siromani glosses "asita-keśānte" = "abaddha-keśa-bhāge" (with hair let down/unbound) rather than just "black-haired" as подстрочник has it ("черноволосая"). This is actually a different image: unbound hair vs. black hair color. Let's verify: `हे असितकेशान्ते हे अबद्धकेशभागे` — Siromani glosses "asita-keśa-anta" (the ends of black hair) as "abaddha-keśa-bhāga" (the part where hair is unbound) — reinterpreting "asita" not as "black" but somehow linked to "unbound"? Actually more likely he's just paraphrasing the vocative addressing her by a hair-related feature, not necessarily changing "black" to "unbound" — this looks like an idiosyncratic non-standard commentarial vocative-gloss that's hard for a reader to parse meaningfully and doesn't cleanly change the image. I'll reject as too subtle/ambiguous for a clean note; risk of misrepresenting the source.

**5.20.33**: Phase-1 already has the Vaiśravaṇa/Kubera note (V.20.33) covering exactly this (brother, Lanka theft). No additional distinct fact in the bundle beyond подстрочник. Reject.

**5.20.34**: Siromani: "एतेन स इह नागमिष्यतीति सूचितम्" — this indicates that [Ravana implies] Rama will not come here — a narrative-function inference (Ravana's rhetorical point is to imply Rama's incapacity to reach Lanka). This is a modest but real narrative-function reading. Let's check for redundancy — Kostina hasn't noted this verse. I'll consider this draftable but let's weigh: is it substantial enough? It essentially restates the boast's rhetorical purpose which is already obvious from context ("Рама ни тапасом... не сравнится со мною"). Marginal — I'll reject as restating the obvious rhetorical thrust already clear from подстрочник.

**5.20.35-36**: Formulaic invitation to pleasure, all three commentators just paraphrase/quote. Reject both.

Now let me check verse "56" and the ambiguous merged-range entries — all get formulaic rejects.

Let me also check verse 810 more carefully since it has actual content (about ekaveṇī gloss, "yuktam aupayikam ityamaraḥ" — a lexicon citation), even though it's an ambiguous_marker merged range.

- 🔧 `Bash` — echo "reviewing ambiguous entries per rule (e): reject regardless of content richness, since these a
Good — per the brief rule (e), all `ambiguous_marker: true` merged-range entries get a uniform reject reason. Now let me finalize my sarga 20 draft list. Let me tally:

**Drafted (5):**
- 5.20.6 — Tilaka variant reading (textological, Б)
- 5.20.16 — Siromani vs Tilaka/Bhusana contrastive on "bhava" (textological, Б, contrastive)
- 5.20.26 — Siromani narrative-function (complements Leonov's lexical note) — В (realia/narrative) — actually this is about Ravana's rhetorical motive tied to Shurpanakha backstory — let me classify as В (historical-narrative) since it's about narrative motivation/backstory link, not wording ambiguity. Actually per the brief: Б = textological (wording/meaning/ellipsis/variant), В = realia/historical-cultural. Narrative-function/motive observation is closer to Б (meaning) since it explains why the text says what it says, not a realia/place/custom. I'll classify as Б.
- 5.20.28 — Tilaka Hiranyakashipu myth detail (Narada intercession) — В (myth/realia)
- 5.20.30 — Siromani characterization observation about Ravana's compassion — Б (interpretive/meaning-level, not realia)

Let me now write the note texts carefully, then compile rejects for all remaining verses (28 substantive + 1 stray verse56 + 10 ambiguous = 39 rejects, 5 drafts = 44 considered).

- 🔧 `Bash` — echo "Sarga 20 tally check: 33 real verses + verse56(stray) + 10 ambiguous = 44 total considered"
Now let me write out the sarga 20 candidates JSON via a script (to guarantee correct UTF-8 no-BOM encoding).

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\build_sarga20.py
This is a scratch build script that assembles the drafting output directly per the brief's schema — not a reusable helper to check prior art for. Proceeding.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
I need to fix the JSON-literal `false`/`true` to Python `False`/`True` throughout. Let me rewrite properly.

- 🔧 `Bash` — cd "C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9
Good, the fix applied correctly. Now let's run it.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
I have a count mismatch — 45 instead of 44 (5+40=45, but I set verses_considered=44). Let me recheck: I listed 40 reject entries but only counted 39 in my earlier tally. Let me verify and fix the `_meta` counts.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Good — all 45 entries from the segmented file are covered (44 was my miscount; the file actually has 45 total verse entries: 33 real verses + verse56 + 10 ambiguous + ... let me recount precisely: 33 real + 1 stray (56) + 10 ambiguous = 44, but unique covered = 45). Let me recheck the actual total entries in the source file.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
The source actually has 45 entries (the earlier `_meta.verse_count: 45` field confirms this — I misread it as 44). My earlier count of "33 real + 10 ambiguous + verse56" = 44 was off by one; there are actually 45 entries total and I've covered all of them (5 drafted + 40 rejected = 45). Let me fix the `_meta.verses_considered` and `notes_rejected` counts to match.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_20_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_20_candidates.json
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_20_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_20_candidates.json
Sarga 20 is complete: 45 considered / 5 drafted / 40 rejected / 2 contrastive. Now let's move to sarga 21.

- 🔧 `mcp__ccd_session__mark_chapter`
Let me get the full list of verse_ids in sarga 21 to make sure I account for every entry.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Good — 34 real verses + 3 ambiguous merged-range = 37 total. Now let me work through each verse.

**5.21.1**: Restates подстрочник (dīnam as adverb, structural note). Reject.

**5.21.2**: Kostina's own note flags "преданная" (pativratā) as needing stronger emphasis. Phase-1 already has a rich note on pativratā (V.21.2, Manu 3.262/9.3). Tilaka's note here is purely syntactic (patim eva cintayantī connects to pratyuvāca). Reject — duplicates Phase-1 + Kostina already flagged the point.

**5.21.3**: Kostina's own note asks for a comment about the straw/soleminka (tṛṇam antarataḥ kṛtvā), referencing a parallel in Araṇyakāṇḍa 56. Tilaka's commentary here is rich and directly on point: he explains the straw as a barrier because direct conversation with another man is improper (parapurusasya sākṣāt-saṃbhāṣaṇa-anarhatvāt), like placing something between oneself and impurity when urinating/excreting (mūtrādi-visarjanavat), and explicitly notes that repeating "pratyuvāca" indicates she answered without fear, treating Ravana as contemptible as straw (tṛṇa-tulyatā). This is a genuinely rich realia/ritual explanation that Kostina's own note doesn't cover (her note wants a comment on the straw itself — this bundle's Tilaka commentary directly supplies exactly that missing comment, with real ritual-purity logic + the "treating him as worthless as straw" reading). This is draftable — and note it complements Leonov's note (which just references the Aranyakanda parallel and asks for more).

- 🔧 `Bash` — echo "5.21.3 confirmed draftable - directly answers Kostina's own flagged gap"
**5.21.4**: Leonov's own note already covers "siddhim iva pāpakṛt" (Tilaka: brahmalokaprāpti). Reject — duplicates tier-1.

**5.21.5**: Tilaka/Bhusana/Siromani all restate подстрочник (turning away, etc.). Reject.

**5.21.6**: Leonov's own note (no editor, likely Kostina's collaborator) already covers the "satī" double-meaning point extensively citing Goldman. The bundle's Siromani commentary here is misplaced (about "vā mithyā... rākṣasānām abhavāya" — belongs to v.9-10 area). Tilaka/Bhusana restate подстрочник on "aupayikī". Reject — duplicates tier-1.

**5.21.7**: Phase-1 already has TWO rich notes here (dārā rakṣyā — Manu 9.5; dharma — MBh Śāntiparvan 12.128.47). Kostina's own note also flags the "chужих/своих" emphasis issue. The bundle's commentary content (mandodari parallel, mutual symmetry logic) doesn't add beyond what Phase-1 covers. Reject — duplicates Phase-1 twice over.

**5.21.8**: Kostina's own note here is rich, quoting Tilaka's ātmānam eva dṛṣṭāntīkṛtya and Bhusana's yathā tava... tathā'nyeṣāṃ gloss — already fully covers the bundle's content. Phase-1 also has an upamā note and paradāra/Manu 4.134 note for this verse. Reject — thoroughly duplicated by both tier-1 and Phase-1.

**5.21.9**: Kostina's own note discusses the "мятежный" translation choice question but doesn't cover Bhusana's rich alternative point: Bhusana explicitly refutes an interpretation that "there are no righteous people (santaḥ) in Lanka" — pointing to Vibhishana's existence as counter-evidence, and reinterprets "na vā santi" as a rhetorical question meaning "surely they exist!" rather than "perhaps they don't exist." This is Bhusana's OWN distinct construal (vs Tilaka/Siromani's straightforward reading), a genuine contrastive point — and it's thematically significant (foreshadowing Vibhishana). Let me verify this reading carefully.

- 🔧 `Bash` — echo "re-reading v9 bhusana text closely"
Re-reading Bhusana on v.9: `इह अतिविशाले ऽपि दुर्जनसङ्कुले देशे । सन्तः त्वामनर्थान्निवारयन्तः । न सन्ति वा न सन्ति किम्? सन्त्येव । श्रीविभीषणप्रभृतीनां सम्भवान्न सन्तीति कथं वक्तुं शक्यम्?` — Bhusana asks rhetorically "are there none? No — there ARE, given the existence of Vibhishana and others!" This directly reinterprets the verse's rhetorical structure: Tilaka/Siromani read it as a straightforward disjunction (either there are no righteous ones OR you don't follow them), while Bhusana insists "santo na vā santi" must be answered "they do exist — Vibhishana proves it" and pivots the blame entirely onto Ravana for not heeding them. This is a genuine contrastive divergence with a real interpretive payoff (foreshadowing Vibhishana). Draftable, contrastive.

**5.21.10**: Restates подстрочник (mithyā-praṇītātmā = false-minded). Reject.

**5.21.11-14**: These verses (about the doomed kingdom, Ravana's self-destruction) — content restates подстрочник mostly. Let me check v.14 Siromani closely: restates "so people are happy at his misfortune." Reject 11-14 as restating подстрочник; Kostina's own note on v.12,14 already covers the specific ellipsis/emphasis points.

**5.21.15**: Phase-1 doesn't cover this specific verse but Tilaka/Siromani just restate подстрочник (ananyā = not separate). Reject.

**5.21.16**: Tilaka/Bhusana/Siromani all restate подстрочник (upadhāya = having placed/embraced). Bhusana explains "lokanāthasya" as "him who is sought after (nāthyamānasya) by Brahma and other gods for their own positions" — this is actually an interesting expansion: lokanātha isn't just "lord of the world" generically but specifically "he whom even the gods petition for their own stations" — but this seems formulaic praise/hyperbole rather than a real added fact. Reject.

**5.21.17**: Tilaka/Bhusana/Siromani gloss "vratasnātasya" as one who completed his Vedic vow-bath; there's an interesting variant note by Tilaka: some read "dhīrasya" (the wise/steadfast) instead of "viditātmanaḥ", restricting the analogy specifically to a trivarṇika (three-varṇa member) rather than all brahmins, tied to eligibility for brahmavidyā. Let's check this in detail — this is a genuine textual-variant note with doctrinal content (who has access to brahma-vidyā).

- 🔧 `Bash` — echo "checking v17 tilaka variant reading detail"
Re-reading Tilaka on v.17: `अन्ये तु-- विप्रपदं त्रैवर्णिकपरम्, त्रैवर्णिकस्यैव ब्रह्मविद्यायामधिकारः, अत एव "धीरस्य" इति क्वचित्पाठ इत्याहुः` — "Others say: the word 'vipra' here refers to any of the three twice-born varnas (not just brahmins), since only the trivarṇika has a right (adhikāra) to brahmavidyā, and that's why some editions read 'dhīraḥ' (the steadfast/wise) instead." This is a genuine doctrinal variant-reading note about eligibility for Vedic knowledge, distinct from подстрочник's simple "ученый брахман." Draftable — kazansky_type Б (variant reading with doctrinal content).

**5.21.18**: Tilaka has an interesting aside acknowledging the simile's "asymmetry" (comparing Sita to a female elephant and Rama to a male elephant lord is odd since she's speaking of herself in the elephant image) — but this is a stylistics/rhetoric-defense note ("this doesn't count as a flaw since it's spoken by an angry separated woman"). This is somewhat interesting (a poetic-defense note) but marginal—too much inside-baseball for a Russian reader without deep alaṃkāra context, and doesn't change the image itself. Reject.

**5.21.19**: Bhusana has a rich passage: he compares Ravana to "a highway robber or a water-beggar" (pathicoraṃ pānīyayācakavat) being petitioned — Sita begging Ravana as if begging a thief. Let me check this carefully — it's a striking image about the humiliating position Sita is put in (having to plead with her captor).

- 🔧 `Bash` — echo "re-check v19 bhusana pathicoram detail"
Re-reading v.19 Bhusana carefully: `पथिचोरं पानीययाचकवद्रावणमर्थयते साध्विति । साधु रावण मद्वियोगेन त्वत्क्रौर्यमधिकं जातमिति भावः` — "She entreats Ravana as one begs a highway-robber for water — [saying] 'sādhu Rāvaṇa,' meaning: through separation from me your cruelty has increased." This is a striking rhetorical/characterization observation: Bhusana reads Sita's uncharacteristically deferential address to Ravana ("sādhu rāvaṇa" — literally "well done, Ravana" or "properly, Ravana") as an act of pleading with a robber, and interprets this plea as evidence that separation from her has made Ravana MORE cruel. This is a genuine interpretive facet with real characterization payoff, not visible in подстрочник. Also worth noting this passage seems misassigned (references v.18's "sādhu rāvaṇa" address, but appears attached to v.19's segment due to alignment). Let me verify which verse "sādhu rāvaṇa" belongs to — it's verse 18 ("sādhu rāvaṇa rāmeṇa māṃ samānaya duḥkhitām"). The commentary segmentation here has attached this Bhusana block to v.19's entry, but content-wise it discusses v.18's opening words. This is a pratika_check flagged issue — let me check: v.19's pratika_check shows Bhusana's `pratika_iast` "pathicoran paniyayacakavadravananarthayate sadhviti" with `matches_verse: false, content_containment: 0.636, content_anchor: true`. So the system itself already flags this as an unverified anchor with content_anchor true (meaning it likely belongs here contentwise despite not matching the verse text exactly) — but per the brief's suggest_verse rule, I should check if there's a suggest_verse field.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
No `suggest_verse` field present, just `content_anchor: true` (meaning the content does substantively relate/overlap with this verse's content region, even if the pratika phrase itself doesn't textually match the verse). Since there's no suggested alternate anchor, and the content_anchor is true, I'll treat this as a legitimate (if imprecise) attachment per the brief's guidance ("draft only if the note survives on either verse, and say so in why_proposed" — applies specifically when there IS a suggest_verse). Since there's no suggest_verse here, I'll treat it as attached to v.19 as given, but note the content's actual reference to "sādhu rāvaṇa" (v.18's phrase) in the note itself for transparency. This is draftable — a genuine characterization/rhetorical observation.

**5.21.20**: Tilaka/Siromani restate подстрочник (dharmajña, śaraṇāgatavatsala glosses). Phase-1 already covers dharmajña/śaraṇāgatavatsala (Manu 6.92, MBh 12.69.16). Reject — duplicates Phase-1.

**5.21.21**: Kostina's own note covers "prayato bhūtvā" literally. Tilaka/Siromani restate подстрочник. Reject.

**5.21.22**: Restates подстрочник (sampradāya = having given). Reject.

**5.21.23**: Kostina flags "lokanāthaḥ" omitted. Bhusana/Siromani gloss content restates подстрочник (vajra/antaka won't spare you but Raghava will kill you regardless). Reject — restates подстрочник, and Kostina already flagged the specific omission.

**5.21.24**: Restates подстрочник (mahāsvanam = loud sound). Reject.

**5.21.25**: Leonov's own note flags that Siromani reads "rāmalakṣmaṇalakṣitāḥ" as "released BY Rama and Lakshmana" rather than "marked WITH the names of Rama/Lakshmana." Let me check: does the bundle confirm this? Bhusana explicitly glosses "rāmalakṣmaṇalakṣaṇāḥ रामलक्ष्मणनामाङ्काः" = "marked with the names of Rama and Lakshmana" — matching Tilaka's reading too (tannāmāṅkāḥ). But Siromani's reading in the bundle says "rāmalakṣmaṇalakṣitāḥ tābhyāṃ visṛṣṭāḥ iṣavaḥ" = "released BY them" — matching what Kostina's note already describes. So this bundle just confirms Kostina's own note without adding anything beyond it. Reject — duplicates tier-1.

**5.21.26**: Restates подстрочник (asaṃpātam = no gap/space). Reject.

**5.21.27**: Leonov's own note covers the Vainateya/Garuda simile literally. Siromani adds an extension: he links this simile to Vishnu's three strides taking Śrī from the asuras (an early preview/foreshadow of verse 28's simile, drawing the two similes together as one continuous mythic argument): "अत एव त्रिभिः क्रमैः पादैः असुरेभ्यः श्रियं विष्णुरिव उरगान् वैनतेय इव भर्ता रामो मामपनेष्यति". This bridges to Phase-1's own trivikrama note at v.28 — but the SPECIFIC point that Siromani links the Garuda-simile (v.27) forward to the Vishnu-simile (v.28) as one continuous rhetorical escalation isn't captured by Phase-1's note (which is scoped narrowly to v.28's trivikrama reference alone). This is a modest but real structural/rhetorical observation. Let me weigh: is this substantial enough on its own? It largely restates what's coming in v.28. I'll reject as marginal — the actual added content (myth detail) is already in Phase-1 at v.28, and the "bridging" observation isn't independently meaningful to a Russian reader without also seeing v.28's note.

**5.21.28**: Phase-1 already has a rich trivikrama/BhG 13.16 note here. Bundle content restates подстрочник + cross-refs v.20's "na capi mama hastāt" — no new fact. Reject.

**5.21.29**: Bhusana has an interesting point: "janasthāna" episode is described as achieved "without battle, by theft" (yuddhaṃ vinā cauryeṇa apaharaṇam) — contrasting with Ravana's earlier boasts of martial prowess (vs. gods/asuras in sarga 20). This underscores Sita's accusation that stealing her while the real heroes were away was cowardly, not valorous. Let me check if this adds beyond подстрочник, which already conveys "you did this being powerless" (aśaktena). The commentary's specific point that it was accomplished "without battle, by theft" reinforces/specifies the accusation somewhat but is largely implicit already in подстрочник's "бессильным... сделано было это нечестивое дело". Marginal — reject as restating.

**5.21.30**: Kostina's own note already covers the "gocara" (field/forest) gloss via Tilaka. Reject — duplicates tier-1.

**5.21.31**: Restates подстрочник (dog vs tigers simile). Reject.

**5.21.32**: This is the Vritra/Indra myth reference — Tilaka and Siromani both give the same myth detail (Vritra fought a long time with one arm against Indra's two arms after Vajra cut off one of Vritra's arms) explicitly sourced "bhāgavate prasiddham" (per Tilaka). This is a genuine mythological detail not in подстрочник (which just says "как в битве Вритры с одной рукой от двух рук Индры" — the подстрочник ALREADY states the one-arm-vs-two-arms detail, but doesn't explain WHY Vritra had only one arm, i.e., that Vajra had severed it). Let me verify this precisely.

- 🔧 `Bash` — echo "checking v32 vritra myth detail vs leonov_ru"
Re-reading v.32 leonov_ru: "Сойдясь в битве с ними обоими, не выстоять тебе, / Как в битве Вритры с одной рукой от двух рук Индры." — the подстрочник already conveys "one-armed Vritra vs two-armed Indra." Tilaka adds: "vajra-cchinna-eka-bāhuḥ vṛtro bahukālam indreṇa sahaikabāhunā yuddhaṃ kṛtavān parājitaśca iti bhāgavate prasiddham" — Vritra's arm was severed BY THE VAJRA, and he fought on with the remaining one for a long time before losing — this explains WHY Vritra only had one arm (backstory the подстрочник's simile presupposes but doesn't state), sourced explicitly to the Bhagavata. This is a genuine myth-completion note. Draftable — В (myth/realia).

**5.21.33**: Restates подстрочник (nātha = lord). Reject.

**5.21.34**: Kostina's own note already covers both the Kailāsa/Gandhamādana variant (Tilaka vs Tattvadipika) AND the "kālahata" ambiguity (whether it modifies Ravana or the tree, per G-press). This bundle's content matches exactly what Kostina's note already states. Reject — duplicates tier-1 fully.

Now the 3 ambiguous merged-range entries (1012, 1921, 3031) — reject per rule (e).

- 🔧 `Bash` — echo "Sarga 21 tally: drafted = 5.21.3, 5.21.9, 5.21.17, 5.21.19, 5.21.32 = 5 drafts; ambiguous reje
Let me double check I haven't missed re-examining verse 13 and 14 fully, since Phase-1 has a note at V.21.13 (pāpa/Manu 12.54-69) that I should check doesn't conflict, and also verify no additional draftable candidates were missed among 11-14.

- 🔧 `Bash` — echo "confirmed v13/14 restate - phase1 pāpa note already covers karma/pretya framing; siromani v14
Now let me write the sarga 21 candidates file.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\build_sarga21.py
Same as before — this is the sarga-21 output-assembly script per the brief's own schema, not a reusable helper. Proceeding.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
5+32=37 matches the total entries. Let me verify all verse_ids are covered with no duplicates or omissions.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 21 complete and verified: 37 considered / 5 drafted / 32 rejected / 1 contrastive. Now sarga 23.

- 🔧 `mcp__ccd_session__mark_chapter`
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
25 total entries: 19 real verses (1-19) + 2 stray entries without sanskrit_iast (20, 21 — these have `ambiguous_marker: false` but empty content, similar to sarga 20's verse 56) + 4 ambiguous merged-range. Let me go through each.

**5.23.1**: Kostina's own note asks for a comment on "рощу ашоки" (an added detail in translation, needing commentary) — but the bundle's commentary (just Bhusana quoting the verse) doesn't address the aśoka grove at all. No content to draft from in this bundle. Reject — bundle content doesn't address the gap; restates подстрочник only.

**5.23.2**: Kostina's own note asks about "покои" (needing comment or reference to earlier note). Bundle has no commentary at all for v.2 addressing this specific point beyond restating подстрочник (bhusana/siromani just paraphrase "when the rakshasa lord went out, rakshasis rushed at Sita"). Reject.

**5.23.3**: Tilaka's commentary here is misplaced (talks about ekajaṭā, belongs to v.5 area). Bhusana/Siromani restate подстрочник. Reject.

**5.23.4**: Restates подстрочник (bhāryātvam = wifehood). Reject.

**5.23.5**: Leonov's own note covers "karatalodarīm" literally already. Siromani restates подстрочник (glosses karatalodarīm the same way, plus responds to an implied objection about whether Sita would refuse worship from a rakshasi — but this is attached oddly). Reject — duplicates tier-1.

**5.23.6**: Kostina's own note flags "Отпрыск разума" (mānasaḥ putraḥ) needing comment. Phase-1 has a rich note on ṣaṭ prajāpatayaḥ (six Prajapatis, cosmogonic frame, Ravana's paradoxical brahminical lineage). This bundle's Tilaka/Siromani just list the same six Prajapati names Phase-1 already covers, with Tilaka adding "tasya putra ityanena kulīnatvaṃ sūcitam" (mentioning "his son" indicates good lineage) — a modest additional point about the rhetorical purpose (establishing Ravana's high birth) but this is essentially implicit/restates the obvious rhetorical strategy of the whole genealogical speech. Reject — duplicates Phase-1's cosmogonic explanation; Tilaka's addendum is too thin to stand alone.

**5.23.7**: Phase-1 already has a rich etymology note on Viśravas (vi+śravas, "renowned", cognate with κλέος/sravah-, contrast with Rama's ikṣvāku lineage). Bundle commentary (Bhusana/Siromani) just restates подстрочник ("Pulastya's son was Vishravas"). Reject — duplicates Phase-1.

**5.23.8**: Restates подстрочник (Ravana as Vishravas's son). Reject.

**5.23.9**: Kostina's own note here is thin ("почему... не согласишься" is glossed literally by Tilaka — matches). Bhusana adds a physical detail: "vivartya nayane kopān mārjāra-sadṛśekṣaṇā" (rolling her eyes in anger, cat-like gaze) describing Harijaṭā's appearance before she speaks — this is a vivid physical/realia detail about the rakshasi's demonic appearance (cat-eyes) not conveyed in Leonov's rendering for this verse (which doesn't mention cat-eyes at v.9; that detail appears at v.10's leonov_ru "с глазами, красными от гнева" — actually let me check, the подстрочник for v.10 says "Округлив в гневе глаза, подобные кошачьим" — so it IS already in подстрочник at v.10. This is the same content, just attached at v.9 by segmentation. Reject as restating подстрочник (just misplaced by verse boundary).

**5.23.10**: Restates подстрочник exactly (cat-eyes, defeating thirty-three gods and Indra). Reject.

**5.23.11**: Leonov's own note explains "kiṃ na lipsase" per Tilaka (necchasi). Bundle repeats exactly this. Reject — duplicates tier-1.

**5.23.12**: Leonov's own note explains the added name "Mandodari" (added by translator, per Tilaka/context). Bundle's Siromani/Bhusana restate подстрочник without adding the Mandodari identification point beyond what's in Kostina's note. Reject — duplicates tier-1.

**5.23.13**: Restates подстрочник (leaving behind the harem of a thousand women). Reject.

**5.23.14**: Introducing the rakshasi Vikatā — restates подстрочник (nagas, gandharvas, danavas defeated). Reject.

**5.23.15**: Restates подстрочник (why don't you want to be his wife). Reject.

**5.23.16**: Phase-1 has a rich note on nairṛtarāja (V.23.18, actually attached there) but this verse (16) discusses sun/wind fearing him. Restates подстрочник. Reject.

**5.23.17**: Phase-1 has a rich note on puṣpavṛṣṭi (V.23.17) already covering the ritual-inversion point (trees showering flowers out of fear, inverting the normal divine-approval meaning). Siromani's commentary here restates the same content without adding beyond Phase-1's point. Reject — duplicates Phase-1.

**5.23.18**: Phase-1 has a rich note on nairṛtarāja here already (cosmological epithet, Nirṛti connection). Tilaka's gloss (bhāryārthe = "for the purpose of being a wife") restates подстрочник. Reject — duplicates Phase-1.

**5.23.19**: Restates подстрочник (accept our words or die). Reject.

Now the stray verses 20, 21 (no sanskrit_iast/leonov_ru, similar to sarga 20's verse 56) and the 4 ambiguous merged-range entries.

- 🔧 `Bash` — echo "checking v20 and v21 content - do they have any commentary that's independently attachable?"
Verses 20 and 21 have `ambiguous_marker: false` but no `sanskrit_iast`/`leonov_ru` — they contain only stray Bhusana blocks (repeating v.18/19 content verbatim, plus the colophon "इत्यार्षे... त्रयोविंशः सर्गः"). These are effectively duplicate/overflow segments with no independent verse to anchor to — reject as isolated fragments (same treatment as sarga 20's verse "56").

Now let me compile the sarga 23 output. Let me verify I haven't missed a genuinely draftable note — let me reconsider v.9's cat-eyes and v.6's kulīnatva point once more against the M.G. pilot preferences (mythic identifications, narrative-function). None of sarga 23's bundle content clears the bar beyond what tier-1/Phase-1 already cover — this sarga is a genealogical recitation + threats, heavily pre-covered by Phase-1's etymology/myth notes (Prajapatis, Viśravas, vīryotsikta, puṣpavṛṣṭi, nairṛtarāja all already drafted in Phase-1). This gives a 0-draft sarga, which is plausible per the brief's ~5-10% target rate (0/25 = 0%, still within "depth not bulk" — many sargas may legitimately draft nothing when Phase-1 coverage is already dense).

Let me do one more pass checking if I'm being too harsh — re ***checking v.14 (Vikatā) and the "Ravana's boast" pieces for any variant/contrastive divergence I may have missed.

- 🔧 `Bash` — echo "re-verify v14: bhusana lists 'asakrddevata yuddhe' vs verse text 'asakrd bhimaviryena' - check
Looking again at v.14: Bhusana's pratīka is "असकृद्देवता युद्धे नागगन्धर्वदानवाः" while the verse itself reads "असकृद् भीमवीर्येण नागगन्धर्वदानवाः" — these differ ("devatā yuddhe" vs "bhīmavīryeṇa"). This could be a genuine textual variant, but it's unclear if it's a meaningful variant or simply a garbled/OCR-style corruption of the pratīka extraction (the pratika_check flags `matches_verse: true` for this Bhusana entry despite the visible difference, suggesting the alignment tool considered it a match, likely due to fuzzy matching tolerance). Given the ambiguity and no explicit commentator remark drawing attention to this as a deliberate variant reading (unlike the sarga-20 cases where Tilaka explicitly says "iti pāṭhe"), I won't draft this — too speculative given no explicit variant-marking language, and risks misrepresenting the source per the reject discipline (rule about suspect anchors).

This confirms sarga 23 nets zero drafts. Let me write the output file.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\build_sarga23.py
Same as prior two — output-assembly script per the brief's schema, not a reusable helper.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
All three sargas verified complete with no gaps or duplicates. Let me do a final sanity check on all three output files' JSON validity and BOM-free encoding, plus re-verify sarga 20's final counts one more time.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
I notice sarga 20 should have 2 contrastive notes (5.20.16) but the count shows 1 — wait, let me check: sarga 20 has one contrastive note (5.20.16, marked `"contrastive": True`), that's correct — I only drafted 1 contrastive note for sarga 20, not 2. Let me verify by re-reading my draft list: 5.20.6 (false), 5.20.16 (true), 5.20.26 (false), 5.20.28 (false), 5.20.30 (false) — yes, exactly 1 contrastive. That's correct.

All three files are valid, BOM-free, and internally consistent. Final verification complete.

**Summary:**

- [sarga_20_candidates.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch3/sarga_20_candidates.json) — drafted: 5.20.6 (variant reading, dharma-framing), 5.20.16 (bhava-maithilī contrastive), 5.20.26 (Śūrpaṇakhā-motive, complements Leonov), 5.20.28 (Hiraṇyakaśipu/Nārada myth detail), 5.20.30 (Rāvaṇa-compassion characterization).
- [sarga_21_candidates.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch3/sarga_21_candidates.json) — drafted: 5.21.3 (straw-gesture ritual logic, complements Leonov), 5.21.9 (santo na vā santi contrastive, Vibhīṣaṇa foreshadowing), 5.21.17 (dhīrasya variant/brahmavidyā-eligibility), 5.21.19 (sādhu rāvaṇa characterization), 5.21.32 (Vṛtra one-arm backstory).
- [sarga_23_candidates.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch3/sarga_23_candidates.json) — 0 drafts; this sarga's genealogical/threat content is thoroughly pre-covered by Phase-1 lexical/myth notes (six Prajāpatis, Viśravas, vīryotsikta, puṣpavṛṣṭi, nairṛtarāja) and tier-1 Kostina notes, leaving nothing that clears the reject-discipline bar.

One-line summary per the brief:

sarga 20: 45 considered / 5 drafted / 40 rejected / 1 contrastive
sarga 21: 37 considered / 5 drafted / 32 rejected / 1 contrastive
sarga 23: 25 considered / 0 drafted / 25 rejected / 0 contrastive

_Dr. Mārcis Gasūns_
