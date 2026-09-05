_Created: 04-07-2026 · Last updated: 05-09-2026_

# Drafting reasoning log — sarga 22

_Model: `claude-sonnet-5`; extracted by scripts/export_agent_logs.py; raw transcript alongside (.jsonl) holds the full record incl. tool results._


I'll start by extracting the relevant data slices for sarga 22.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\silly-diffie-1e1e22" && ls
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\silly-diffie-1e1e22" && ls
Let me look at an example output from batch2 and the pilot report for style calibration, then extract sarga 22 data.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\silly-diffie-1e1e22\data\analysis\phase2_batch2\sarga_35_candidates.json
- 🔧 `Bash` — mkdir -p "C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub-CommentaryStrategie
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\silly-diffie-1e1e22\data\analysis\phase2_batch2\sarga_36_candidates.json
Odd. Let me glob to get the exact path.

- 🔧 `Glob` — data/analysis/phase2_batch2/*
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\silly-diffie-1e1e22" && pw
The directory shows as empty via find but `ls` showed files earlier. Let's recheck.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\silly-diffie-1e1e22" && ls
The directory is actually empty now (my earlier `ls` must have been from a stale listing or cache confusion). Let's check git status / other branches for these files, but regardless, I'll just create the file. Let's check the pilot for style reference instead.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\silly-diffie-1e1e22\data\analysis\phase2_pilot\pilot_candidates.json
Good, style is clear now. Let's extract sarga 22 data slices.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\silly-diffie-1e1e22" && SC
Path mixing issue on Windows python. Let me use a Windows-style path directly with python.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\silly-diffie-1e1e22" && py
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\silly-diffie-1e1e22" && py
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\silly-diffie-1e1e22" && py
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\silly-diffie-1e1e22" && py
Note this file has "0" per_chapter_notes for chapter 22 in meta, but there are 8 actual entries with shloka starting "V.22.". Let me view the extracted files.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub-CommentaryStrategies--claude-worktrees-silly-diffie-1e1e22\54f2e5f4-e089-4d80-bd01-cb3233100ffb\scratchpad\phase1_22.json
Now let's view own_notes_22 and the segmented verses.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub-CommentaryStrategies--claude-worktrees-silly-diffie-1e1e22\54f2e5f4-e089-4d80-bd01-cb3233100ffb\scratchpad\own_notes_22.json
Now let's look at the segmented verse bundles (Sanskrit commentary text).

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\silly-diffie-1e1e22" && py
Now let me dump the full sarga in a readable form to review each verse's commentary content, since I need to actually read Sanskrit Devanagari commentary.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\silly-diffie-1e1e22" && py
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub-CommentaryStrategies--claude-worktrees-silly-diffie-1e1e22\54f2e5f4-e089-4d80-bd01-cb3233100ffb\scratchpad\sarga22_dump.txt
Now I have the full picture. Verses V.22.47-55 seem missing (jump from 46 to 56, and 56/57 have no clean verse text). Let me check that gap and also verify verse count.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\silly-diffie-1e1e22" && py
So sarga 22 has 46 real per-verse bundles (1-46), plus two odd ones (56, 57 — likely mis-tagged/duplicate stray commentary fragments, not real verses of this sarga since sarga 22 ends at 46 per the phalaśruti colophon at line 505), plus 12 ambiguous merged-range markers. Let me check verses 56/57 more — they look like duplicate/misplaced commentary on verses already covered (5 and 20/22).

Comparing: V.22.56 bhusana text "मिथ्या प्रव्रजितं कपटेन..." matches the alternate reading theme of V.22.5 (mithyā pravrajita). V.22.57 tilaka text "एतस्मादिति..." also discusses mithyā pravrajane — same verse 5 theme. These are misassigned duplicates. I'll treat them as rejects (data misalignment / duplicate of verse 5 commentary already reviewed).

Now let's check ambiguous markers content briefly — already dumped above, all reject per rule (e). Now let's draft. Let me cross-check own_notes and phase1 mapping per verse for dedup.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\silly-diffie-1e1e22" && py
Now I have full dedup baseline. Let me go verse by verse (1-46) and decide.

**V.22.1**: Tilaka/Bhusana/Siromani just paraphrase syntax (saṃbandha connecting clauses). No new content. Reject — restates подстрочник/pure grammar.

**V.22.2**: Own note (kostina) already covers vaśyaḥ interpretations (Tilaka=iṣṭa, Siromani... wait own note says Tilaka=iṣṭa, Siromani=priya). Let me check actual Sanskrit: Tilaka says "स स्त्रीणां वश्य इष्टो भवति" (vaśya = iṣṭa). Siromani says "वश्यः प्रियो भवति" (vaśya = priya). This matches own note exactly (tier-1 already covers this). Reject — duplicates own note.

**V.22.3**: Own note covers mārgam/amārgam variant (Tilaka reading). Also phase1 has a note on susārathi (etymology). Bhusana here just says "द्ववतः धावतः । अमार्गमिति च्छेदः" — parses amārgam as separate word (chedaḥ) — confirms segmentation, minor grammar, already covered by own note about the mārgam/amārgam reading. Reject — duplicates own note.

**V.22.4**: Own note (kostina) very extensive already covering vāma=krūra (Tilaka), Amarakośa citation, Siromani's "sundara/utkaṭa" reading — this is comprehensively covered already, including the exact Amarakośa quote. Reject — duplicates own note in full.

**V.22.5**: Own note covers mithyā pravrajane/pravrajite variant. Bhusana here just gives "pravrajite" reading (same as own note). Reject — duplicates own note.

**V.22.6**: Tilaka commentary text here is odd — it discusses "asmin nagare te tava niḥśreyasābhyudaya..." which actually belongs to verse 13, not verse 6 (data misalignment, as noted in pilot caveats). Bhusana/Siromani just paraphrase. Reject — pure grammar/data misalignment.

- 🔧 `Bash` — echo checking done
**V.22.7**: Own note already gives Bhushana's krodhapraṇayābhyāṃ saṃyukta gloss exactly. Reject — duplicates own note.

**V.22.8**: Bhusana/Siromani explain "dvau māsau" cross-reference to Araṇyakāṇḍa vow (12 months, 2 remain) — Siromani adds a striking detail: "śayanam āroha" = death (mahāsvāpaṃ maraṇam), and infers Rāvaṇa's implicit threat: "if you don't give up remembering Rāma, I will kill myself in your presence" — wait let's reread: "एतेन रामस्मृतिं त्यक्त्वा स्वौदासीन्यं न त्यक्ष्यसि तर्हि त्वत्सन्निधावहं स्वप्राणांस्त्यक्ष्यामीति सूचितम्" — this actually says: this implies "if you don't give up remembering Rāma [and abandon your indifference], I will give up my life in your presence" — that's a striking distinct reading: śayanam āroha = death-bed (not "come to my bed" sexually but euphemism for dying), and hints Rāvaṇa threatening suicide. This is genuinely new — not in подстрочник, not tier-1, not phase1. Draft this — Б (textological, reinterprets key phrase).

- 🔧 `Bash` — echo continue
**V.22.9**: Own note doesn't cover verse 9. Tilaka gives simple gloss prātarāśaḥ = morning meal (trivial). Bhusana/Siromani paraphrase syntax. Reject — pure grammar/gloss trivial, restates подстрочник.

**V.22.10**: Bhusana/Siromani paraphrase only. Reject.

**V.22.11**: Tilaka/Bhusana explain ओष्ठप्रकारैः (lip-gestures) in detail — "the wretch, what can he do—no need to fear" conveyed through lip movements; eye blinking etc. This is a nice literary/performative detail beyond подстрочник ("движениями губ... ободряли" is vague in translation) — commentators specify WHAT the gestures communicated. Consider drafting — but is it substantial enough? Siromani: "ओष्ठप्रकारैः क्षुद्रो रावणः किं करिष्यतीत्यादिबोधकाधरप्रचालनैः" = lip-movements conveying "what can this wretch do" — this fills in the silent gesture with actual meaning, giving insight into the scene. This adds real content not in подстрочник. Draft — Б.

**V.22.12**: Own note covers this exactly (ātmahita = hitam for Rāvaṇa, śauṭīrya = patiśaurya). Phase1 also covers vṛttaśauṭīrya etymology. Reject — duplicates both own note and phase1.

- 🔧 `Bash` — echo continue2
**V.22.13**: Own note doesn't cover. Siromani explains: nobody in Laṅkā who cares for Rāvaṇa's welfare (niḥśreyas) restrains him from this disgraceful deed. This mostly restates подстрочник. Reject.

**V.22.14**: Phase1 covers śacīpati at length (Śacī/Indrāṇī parallel, implicit threat). Tilaka here adds a small logical point: "manasāpi kaḥ" — even mentally who would dare, let alone verbally (kiṃ punar vacaseti bhāvaḥ) — this is a minor a fortiori argument. It's a small addition beyond phase1 note. Is it "genuinely distinct facet"? Phase1 note discusses the epithet meaning + threat; Tilaka's a fortiori reading (mental vs verbal) is a different, narrower point about logical structure. Marginal — I'll reject as duplicative in substance (same verse already thoroughly glossed with the key point); Tilaka's addition is grammatical inference, not a new content layer for a Russian reader.

**V.22.15**: Own note (kostina) flags kva gatas omission — meaning changed. Tilaka/Bhusana here: Tilaka explains "yat pāpam" = the very words "mama śayanam āroha" (this connects back to v.8's śayana as sin) — and "tasya mokṣyase" = will you escape from that sin's total destruction (mūlanāśa)? This adds a specific referent (what "the sin" is) plus Bhusana's grammatical note tasya=tasmāt. Given own note already flags this verse's dislocation, but the specific content (identifying "yat pāpam" phrase and consequence "mūlanāśa") is new. Let's check depth — could be worth drafting. But this seems fairly technical/grammar-level. Reject — pure grammar restating referent, low reader value beyond own note's flag.

- 🔧 `Bash` — echo continue3
**V.22.16**: Tilaka/Bhusana explain the simile logic in more depth: Rāma preemptively worried he'd be thought like the elephant-hare comparison meaning himself weak; Bhusana clarifies structure: "atra rāvaṇaḥ svasya mātaṅgasāmyam uktam iti bhrāmyed iti pariharati" — Rāvaṇa forestalls the (mis)reading that he compared himself to the elephant; clarifies Rāma=elephant, Rāvaṇa=hare. This resolves a real ambiguity in the verse (who's the elephant?) not obvious from подстрочник alone (translation says "подобный слону Рама, а ты подобный зайцу" — actually подстрочник already resolves this clearly). So this commentary just supports the given translation; no new content for reader. Reject.

**V.22.17**: ambiguous Tilaka fragment says "он крайне неразумен" (nirbuddhi) implied — a value-add characterization. Siromani: "एतेन त्वमतीव निर्बुद्धिरिति सूचितम्" — this implies Rāvaṇa's utter foolishness (a specific evaluative point: he insults Rāma only because Rāma hasn't yet appeared before him — implying rank stupidity). This is a genuine interpretive addition — commentator draws out an implicit characterization not stated in подстрочник. Draft — Б.

- 🔧 `Bash` — echo continue4
**V.22.18**: Bhusana/Siromani just paraphrase. Reject.

**V.22.19**: Tilaka here (misplaced text likely referring to v.20, discusses asaṃdeśāt) — actually the tilaka block under V.22.19 discusses "śāpaviṣaye rāmājñābhāvāt" — the absence of Rāma's order regarding cursing — same content that appears properly in V.22.20. This is duplicate content misplaced. Siromani second half mentions "śūreṇa..." referring to V.22.22 — again misplaced. This is a data alignment artifact; the substantive commentary belongs to other verses. Reject — data misalignment (duplicate of v.20/22 content).

**V.22.20**: Own notes (kostina) flag both daśagrīva vocative omission AND bhasmārha tejasā "нужен комм." (needs commentary) — this is a direct request from M.G./Kostina for exactly this note! Tilaka (under V.22.19, misplaced) and Bhusana/Siromani under V.22.20 explain: asaṃdeśāt = because Rāma gave no order "śapetha apakāriṣu" (curse those who wrong you); tapasaḥ anupālanāt = preserving her chastity-tapas; bhasmārha = worthy of being reduced to ashes. This is EXACTLY what Kostina flagged as needing commentary. Definitely draft — this is high-value. kazansky Б (textological — supplies the reasoning gap). Also should include "complements_leonov" since own note itself flags the need but leaves it blank.

- 🔧 `Bash` — echo continue5
**V.22.21**: Siromani explains "vidhiḥ" = the specific device of the golden deer (hemamaya-kuraṅga) fated by providence to bring about Rāvaṇa's death — i.e., interprets "vidhi" (the "arrangement/undertaking") as referring specifically to the golden-deer stratagem, not abstract fate. Tilaka also glosses vidhi as "apaharaṇarūpa vidhi" = the abduction-scheme itself as fated for his death. This is a genuinely specific interpretive point — the abstract "судьбою предначертана твоя гибель" in подстрочник doesn't specify HOW/what "vidhi" refers to; commentators specify it's the golden deer ruse. Draft — Б.

**V.22.22**: Bhusana explains "apohya rāmam" = deceived by means of the illusory deer (mṛgacchadmanā apavāhya). Tilaka (misplaced under v.24, discusses "śūreṇetyādyupahāsoktiḥ") calls this whole verse an "upahāsa" (mockery/sarcasm) — Sita is being sarcastic in calling Rāvaṇa "śūra" (brave) ironically, since he needed trickery via Mārīca's illusion to steal her, proving he's the opposite of brave. This is a genuine rhetorical-register point: the "praise" is sarcasm. Draft — Б (reveals ironic register not evident from neutral подстрочник translation "Зачем ты, отважный...").

- 🔧 `Bash` — echo continue6
**V.22.23-30** (Rāvaṇa's ekphrasis description): Most are pure descriptive glosses/paraphrases (chalāgra, śroṇīsūtra parsing etc.) — already largely explained by подстрочник itself which is quite literal here. Let me check each for real additions.

- V.22.23: paraphrase only. Reject.
- V.22.24: Tilaka gloss "siṃhasattvagatiḥ" pāṭhāntara "siṃhasaṃhananaḥ" — a textual variant reading noted. This is a genuine variant-reading note (Б type). Could draft, but it's fairly minor/technical (alternate epithet meaning "lion-boned" vs "lion-like courage/gait") — real textological content though. Let me consider: it's a legitimate variant reading affecting the verse's word choice. I'll draft this — Б, brief.

Actually, let me reconsider scope/density target (~5-10%). Let me be more selective and prioritize the strongest few. Let me continue scanning remaining verses first then decide final cut.

- 🔧 `Bash` — echo continue7
**V.22.25**: paraphrase only (chalāgra parsing, "tāptānga" = intense/glowing said via "tejiṣṭhatvam"). Minor gloss, restates подстрочник sufficiently. Reject.

**V.22.26**: Own note (kostina) flags "amṛtotpādane" needs comm. Tilaka/Siromani explain: śroṇīsūtra = girdle-cord; mecaka = dark blue (from indranīla-jewel-studded ends) OR Siromani cites Medinī lexicon: mecaka = peacock's eye-spot color (śyāmala); bhujaṅga = Vāsuki (specifically named, said to be blue-colored). This directly answers Kostina's flagged need ("нужен комм" on amṛtotpādane) by explaining the Mandara/Vāsuki churning-of-nectar myth reference AND identifies the serpent as Vāsuki specifically, plus explains the color-term via lexicon citation. High value — directly fills Kostina's flagged gap. Draft — В (realia/myth — identifies Vāsuki, Mandara churning myth).

**V.22.27**: Siromani notes: since Rāvaṇa has kāmarūpatva (shape-shifting power), having only two arms here doesn't contradict his usual multi-armed depictions — resolves an implicit reader puzzle (why only 2 arms if he's usually depicted with more?). This is a genuine explanatory point not in подстрочник. Draft — В (doctrinal/mythic clarification about Rāvaṇa's iconography).

- 🔧 `Bash` — echo continue8
**V.22.28-30**: paraphrase only, no commentary beyond bhusana repeating text. Reject each.

**V.22.31**: Own note covers anaya=anīti (Tilaka) already, and phase1 doesn't cover this verse directly (wait phase1 has V.22.31 too — let me check). Phase1 V.22.31 covers anaya etymology in depth (anaya = an+naya, nīti-śāstra term, artha-śāstra vs dharma worldview clash). Own note also covers Tilaka's anīti gloss + Goldman comparison. Siromani here adds: "arthahīnam" = Rāma glossed by Siromani via anaya connection (rāmam anuvrate — devoted to Rāma) — same content already covered. Reject — duplicates both own note and phase1.

**V.22.32**: Tilaka block (misplaced, discusses vrata duration cross-ref to Araṇyakāṇḍa "daśamo māsaḥ, dvau tu śeṣau" — noting Sītā later says 10th month with 2 remaining, reconciling apparent inconsistency with earlier 2-months statement) — this is a genuine textual/narrative-consistency note: commentator reconciles apparent discrepancy between different verse references to time remaining. Interesting cross-reference but content is about internal-text consistency across sargas, valuable for structural readers. Consider drafting — Б (textological, resolves an apparent contradiction). Let's draft this one; it's a solid textological point about narrative consistency across the text.

- 🔧 `Bash` — echo continue9
**V.22.33-38** (rākṣasī catalog + fourfold means): Own note (kostina) already covers V.22.38 exactly (Arthaśāstra fourfold means — sāma/dāna/bheda/daṇḍa) citing the Artha-śāstra passage. Phase1 covers V.22.33 karṇaprāvaraṇā already. V.22.34-37 pure lists of grotesque body parts and imperative repetition — no additional commentary of substance (bhusana just repeats verse text). Reject all of 34-37.

V.22.38: own note already comprehensive with Arthaśāstra citation — reject duplicate. But check bhusana/siromani text under 37/38 — Siromani: "प्रतिलोमानुलोमैः अननुकूलानुकूलक्रियाभिः सामादिभिश्च ... वैदेहीम् आवर्जयत रामासक्तिं न्यवारयत" — glosses āvarjayata as "prevent her attachment to Rāma" — this is a specific interpretive nuance (āvarjayata doesn't just mean generically "persuade" but specifically "wean her off Rāma-attachment"). Marginal, borderline duplicate of own note's Arthaśāstra point which is the main content. Reject.

**V.22.39**: Own note (raw): "Комментарий «Широмани» отождествляет Дханьямалини с Мандодари." — wait, own note ALREADY states this exact identification (Śiromani identifies Dhānyamālinī with Mandodarī). Let me check the segmented commentary text at V.22.39 siromani: "राक्षसी राक्षसीस्वामिनी मन्दोदरी धान्यमालिनी तदभिधरावणकनिष्ठपत्नी च राक्षसीशब्देन मन्दोदर्या ग्रहणं तु वानरान्प्रति वक्ष्यमाणहनुमद्वचनानुरोधेन" — this gives MORE detail than own note: it explains WHY Śiromani identifies her as Mandodarī — because of a later Hanuman speech to the monkeys (forward cross-reference within the text) — and notes Dhānyamālinī is actually Rāvaṇa's youngest wife by that name, but Śiromani takes "rākṣasī" here to mean Mandodarī based on that later textual hint. This is richer than the terse own note and gives the interpretive mechanism. Could complement Leonov's own note with this reasoning. Draft with complements_leonov — Б (textological identification + its textual basis).

- 🔧 `Bash` — echo continue10
**V.22.40-46**: Let's check remaining.

- V.22.40: Tilaka: pariṣvajya = by embracing, restraining Rāvaṇa's blow-in-progress (prahārādi-pravṛttiṃ nirudhya) — small nuance: she doesn't just embrace affectionately but physically restrains him mid-strike, implying he was about to hit Sītā. This is a real added dramatic detail. Draft — Б.

- V.22.41: Tilaka: "devagandharvakanyāḥ ... sītāvad eva balād āhṛtāḥ" — implies the divine/gandharva maidens (mentioned in v.10/41 context) were ALSO abducted by force like Sītā — a mini-realia/narrative detail not in подстрочник ("ей боги сокровища не..."). Wait this is under V.22.41 header but seems to refer back to v.10's devagandharvakanyāḥ. Let me check placement more carefully — likely misaligned again referring to earlier verse content. The subject here is ambiguous; own note flags "rākṣaseśvara" vocative omission for v.41, unrelated to this Tilaka fragment. Given misalignment risk, and the content (other women were also abducted by force) is a stray remark of moderate interest but uncertain placement — I'll reject as data misalignment/uncertain.

- V.22.42: Siromani explicit: "akāmāṃ = rājyādi-icchā-rahitāṃ vyaktim" — one who lacks desire for kingdom-etc = specifically indifferent to royal enjoyments, not just romantically uninterested — sharpens akāmā's referent. Minor. Reject — restates подстрочник adequately.

- V.22.43-46: paraphrase/closing colophon only. Reject all.

Let me also check V.22.14 more, and finalize the reject/accept list, then check the two stray "56/57" verses and merged-range markers.

- 🔧 `Bash` — echo finalize
Now let me compile the final list. Let me tabulate drafted vs rejected decisions:

**Drafted (10):** V.22.8, V.22.11, V.22.17, V.22.20, V.22.21, V.22.22, V.22.24, V.22.26, V.22.27, V.22.32, V.22.39, V.22.40

That's 12 — a bit high for 5-10% of 46 (~2-5 notes). Let me tighten to the strongest candidates matching M.G.'s stated preferences (variant readings changing the image, doctrinal frames, mythic identifications, narrative-function). Re-rank by strength:

- V.22.20 (Kostina explicitly flagged, strong) — KEEP
- V.22.26 (Kostina explicitly flagged, myth Vāsuki/Mandara) — KEEP
- V.22.21 (golden deer identification of "vidhi") — KEEP, strong mythic/narrative
- V.22.22 (sarcasm/irony register) — KEEP, strong literary
- V.22.24 (variant reading, minor) — borderline, keep as it's a genuine variant reading (M.G. values these)
- V.22.27 (kāmarūpa resolves 2-arms puzzle) — KEEP, doctrinal
- V.22.39 (Mandodarī identification mechanism) — KEEP, complements Leonov
- V.22.8 (śayana=death, suicide threat) — KEEP, strong narrative/dramatic
- V.22.32 (cross-reference reconciling month count) — KEEP, textological narrative-consistency
- V.22.11 (lip gestures meaning) — weaker, borderline; drop
- V.22.17 (Rāvaṇa's foolishness implied) — weaker, borderline; drop
- V.22.40 (restraining mid-strike) — moderate; keep, adds real drama

That gives 10 drafted, 36 rejected (46 total, ~22% rate — still high vs 5-10% target). Given M.G.'s explicit flags via Kostina notes count as high-value musts, and several are strong mythic/textological finds, I'll accept a somewhat higher rate here since sarga 22 is unusually dense (Rāvaṇa's threat speech + ekphrasis) but trim further to the clearly strongest 7-8.

Final cut — drop V.22.11 (lip gestures - moderate), V.22.17 (implied foolishness - thin), V.22.40 (restraining detail - thin):

**Final drafted list (9):** V.22.8, V.22.20, V.22.21, V.22.22, V.22.24, V.22.26, V.22.27, V.22.32, V.22.39

That's 9/46 ≈ 19.5%. Still above 5-10% target but this sarga has unusually rich commentary (myth, doctrine, textual variants). I'll go with quality over the target percentage per "depth not bulk" — but let me cut two more borderline ones to get closer to target: drop V.22.24 (minor variant, thin) and V.22.32 (narrative consistency, useful but secondary):

**Final: 7 drafted** — V.22.8, V.22.20, V.22.21, V.22.22, V.22.26, V.22.27, V.22.39 (7/46 ≈ 15%)

Now let me write the notes carefully.

- 🔧 `Bash` — echo drafting
Now let me write the final JSON file.

- 🔧 `Write` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\silly-diffie-1e1e22\data\analysis\phase2_batch2\sarga_22_candidates.json
Let me validate the JSON, no-BOM, and count reconciliation.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\silly-diffie-1e1e22" && py
Everything reconciles cleanly: no BOM, valid JSON, 7 drafted + 39 rejected = 46 verses considered, all verse IDs 5.22.1–5.22.46 accounted for with no gaps or overlaps.

Verses considered / drafted / rejected: 46 / 7 / 39

_Dr. Mārcis Gasūns_
