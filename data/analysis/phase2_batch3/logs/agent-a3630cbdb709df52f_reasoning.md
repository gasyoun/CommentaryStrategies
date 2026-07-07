# Agent log agent-a3630cbdb709df52f

_Model: `claude-sonnet-5`; extracted by scripts/export_agent_logs.py; raw transcript alongside (.jsonl) holds the full record incl. tool results._


I'll start by reading the judge brief to understand the exact rubric, gates, and output format.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\JUDGE_BRIEF.md
Now let me look at the rubric doc and the file structures before starting.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\docs\PHASE2_METHOD.md
- 🔧 `Glob` — data/analysis/phase2_batch3/sarga_*_candidates.json
Now let me look at one candidate file and its segmented bundle to understand exact structure before I start judging.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_19_candidates.json
Now let me look at the segmented bundle for sarga 19 and the tier-1 baseline files.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_19_segmented.json
Now let me check the tier-1 baseline files (leonov_own_notes.json and sundara_commentary_to_add.json) for sarga 19.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Windows console encoding issue. Let me write output to a file instead and read it with the Read tool.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
I need to use the scratchpad directory instead of /tmp. Let me redo this.

- 🔧 `Bash` — mkdir -p "C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s19_leonov.json
Good, this confirms the tier-1 baseline. Now let's check the Phase-1 data (`sundara_commentary_to_add.json`) for sarga 19.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
The first element is a `_meta` dict. Let me inspect the actual structure of note entries.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Console encoding garbled the Cyrillic in that print but the JSON itself is fine (it's a UTF-8 file, just cp1251 console). Now let's filter for sarga 19 (shloka starting "V.19.").

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s19_phase1.json
Now I have full context for sarga 19. I have both baselines (tier-1 Leonov/Kostina and Phase-1 lexical/kavya notes). Let me judge each of the 6 notes.

**Judging sarga 19 notes:**

1. **5.19.5** (`saṃśitavratām`): Tilaka reads it as a specific vow for Ravana's death, vs Phase-1 note which gives the Kashyapa formulaic-epithet parallel (ascetic overtone via MBh). Note gives concrete content of the vow (Ravana's death) — different angle from Phase-1's formulaic epithet parallel. Checking bundle: Tilaka's text = "संशितव्रतां रावणवधाय तीक्ष्णं व्रतमिव कुर्वाणाम्" — "saṃśitavratāṃ [as if] performing an intense vrata for the killing of Rāvaṇa" — matches note's claim exactly. Faithful (2). Non-trivial vs Phase-1 (2, different angle). Contrastive: single commentator (1). Register: clean, 1 sentence, names Tilaka, IAST lemma present, no Devanagari (2). Anchoring: pratika_check shows tilaka matches_verse true (2). Verdict: keep.

2. **5.19.6** (`maṇḍanārhām amaṇḍanām`): Note claims Tilaka resolves the paradox (dirt = ornament of ascetic) AND cites a variant reading "citrāṅgī" by "Tīrtha". Bundle text: "मलेन मण्डनस्थानेषु दिग्धाङ्गीं रूषिताङ्गीम् । "चित्राङ्गीम्" इति पठित्वा मलरूपेण मण्डनेन चित्राङ्गीं कर्बुरामित्यर्थं तीर्थ आह । संन्यासित्वादुचितैव तस्य मले ऽपि मण्डनत्वबुद्धिः" — This matches well: Tīrtha reads "citrāṅgīm" and Tilaka's own comment about संन्यासित्व justifying dirt-as-ornament. Faithful (2). Non-trivial (2 — new variant + doctrinal resolution not in подстрочник/Phase-1). Contrastive: single commentator with two glosses/a variant — contrastive_value =1 (real exegetical gain, not two commentators strictly compared since "Tīrtha" is cited within Tilaka's own text as a variant reading, not an independent named commentator in the corpus). Register clean (2). Anchoring: pratika_check tilaka matches_verse **false** but `content_anchor: true` (containment 0.375) — this is "unverified but plausible" per anchoring rubric (1), since it's not a straight pratīka match but was verified via content anchor. Let me treat content_anchor:true as the "verified" case per §11 item 3 (anchor_verified counts pratika ∪ content anchor as verified). So anchoring = 2.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\JUDGE_BRIEF.md
Confirmed: "verified (pratīka or content anchor) ⇒ 2". So `content_anchor: true` (regardless of `matches_verse`) counts as anchoring=2. Only when neither pratika matches nor content_anchor is present (and no suggest_verse contradiction) is it "unverified but plausible"=1. Let me now go through all 6 notes systematically with this rule clear.

Note re-check for **5.19.6**: tilaka pratika_check has `matches_verse: false, content_containment: 0.375, content_anchor: true` → anchoring = 2 (verified via content anchor).

**5.19.10** (`jātam iva ca duṣkule`): siromani pratika_check: `matches_verse: false, content_containment: 0.455, content_anchor: true` → anchoring=2. Note text checks against bundle Siromani commentary: "दुष्कुले राक्षसकुले जातामिव राक्षसपुरस्थितात्वेन तत्र जातात्वेन प्रतीयमानामित्यर्थः" — matches note's claim (referent = current captivity among rakshasas, not general upanayana-marriage metaphor). Faithful (2). The note explicitly contrasts with Leonov/Kostina's own note (which does cite upanayana via Goldman) — this is a genuine `complements_leonov` field showing awareness of tier-1. Non-triviality (2). Contrastive_value: single commentator vs Leonov's own note is a genuine exegetical gain, but is this "translation choice resolved"? It's contrasting Siromani vs Leonov's tier-1 interpretation — arguably resolves an interpretive divergence but not between 2 traditional commentators. I'll score contrastive_value=1 (single commentator, real exegetical gain). Register clean (2).

- 🔧 `Bash` — echo checking
Now let's check remaining notes 5.19.14, 5.19.20, 5.19.21.

**5.19.14** (`vedīm iva parāmṛṣṭāṃ`): Note claims both Tilaka AND Siromani independently specify who defiled the altar — untouchables/chandalas — Siromani directly compares Sita to a deity's image defiled by a chandala's touch. Bundle: Tilaka: "परामृष्टां वेदवेदिरहितपतितैराक्रान्ताम्" (touched by those fallen/degraded, lacking Veda-knowledge — roughly outcastes). Siromani: "परामृष्टां चाण्डालेन स्पृष्टां देवीं तत्प्रतिमामिव" (touched by a caṇḍāla, like a deity's image). Faithful (2) — both do specify defilement by low-caste persons; Siromani explicitly names caṇḍāla; Tilaka says "patita" (fallen/degraded ones) which is close enough to "outcastes" — reasonable characterization, not "chandalas" verbatim for Tilaka but the note says "прикосновение отверженных/чандалов" (touch of outcasts/chandalas) — hedged with "outcasts" for Tilaka and specifically chandala for Siromani via "Широмани прямо сравнивает..." — accurate. Non-triviality (2, absent from Phase-1's vedī note which discusses ritual purity generally but not the chandala specifics — checking: Phase-1 note says "Сита = осквернённый алтарь, но её осквернение вынужденное" — general framing, no chandala detail). Good — non-trivial. Contrastive_value: TWO commentators genuinely converging/contrasted (Tilaka + Siromani) = 2. Register clean (2). Anchoring: tilaka pratika_check `matches_verse: true`; siromani pratika_check `matches_verse: true` → anchoring=2.

**5.19.20** (`alpāhārāṃ`): Note claims Tilaka gives dual explanation — ritual (unwashed, can't eat normal food) + Indra secretly gave her pāyasa. Bundle Tilaka: "अल्पाहारां जलमात्राहाराम् अस्नातयान्नस्य ग्रहीतुमशक्यत्वात् देवराजतः पायसलाभेन तदनपेक्षणाच्च" — "alpāhārāṃ = only water as food, because being unbathed she cannot take rice/grain-food, and also because she has received pāyasa from the king of gods (Indra) so does not need [more]." This matches the note closely — faithful (2). Non-trivial vs Phase-1 tapodhanā note (which is about the "rich in tapas" epithet generally, not the ritual+Indra-payasa explanation) — non-trivial (2). Contrastive_value: single commentator, real exegetical gain, with reference to "known from other parts of the poem" — 1. Register clean (2). Anchoring: tilaka pratika_check `matches_verse: true` → 2.

- 🔧 `Bash` — echo checking 21
**5.19.21** (`tapodhanatvād eva … āyācamānām`): Note claims Tilaka establishes causal link (tapas from previous verse → efficacy of prayer) and specifies she prays to her own family deity, not a generic one. Bundle Tilaka: "तपोधनत्वादेव रघुमुख्यस्य सकाशाद्दशग्रीवपराभवमायाचमानां प्रार्थयन्तीम्, अत एव भावेनान्तरध्यानेन देवतामिव एवार्थे इव । स्वकुलदेवतामेवोद्दिश्य प्राञ्जलिं कृतनमस्काराम्" — "tapodhanatvād eva ... = precisely because of being tapo-rich, she is praying for Daśagrīva's defeat ... addressing her own family deity (svakuladevatām), having made añjali." This matches the note's two claims well. Faithful (2). Non-trivial vs Phase-1/подстрочник — подстрочник juxtaposes tapas-epithet and prayer without causal claim; Phase-1 has no note on this verse. Non-trivial (2). Contrastive_value: single commentator, real exegetical gain (causal link + addressee specification) = 1. Register clean (2). Anchoring: tilaka pratika_check `matches_verse: true` → 2.

Now let me write the judge object for each note and update sarga 19's file.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_19_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_19_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_19_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_19_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_19_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_19_candidates.json
Now update `_meta` for sarga 19 with judged status and verdict counts.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_19_candidates.json
Let me validate the JSON parses correctly.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 19 is done: 6 keep. Now let's move to sarga 20. Let me read the candidates and segmented files.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_20_candidates.json
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_20_segmented.json
I have enough context. Let me check the specific verses I need: 5.20.6, 5.20.16, 5.20.26, 5.20.28, 5.20.30. All are within what I've read except I should verify 5.20.26 details (already seen) and check tier-1/Phase-1 baselines for sarga 20.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s20_leonov.json
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s20_phase1.json
Now I have full baselines for sarga 20. Let me judge the 5 notes.

**5.20.6**: Note claims Tilaka's variant reading "evaṃ caitad akāmāṃ tvām" shifts the meaning to Ravana's restraint being a rakshasa-dharma rule rather than personal choice. Bundle Tilaka text confirms: "\"एवं चैतदकामां त्वाम्\" इति पाठे एतद्रक्षोधर्मत्वम्" = "In the reading 'evaṃ caitad akāmāṃ tvām', this [is stated to be] the rakshasa-dharma-ness [of it]." Matches exactly. Faithful (2). Non-trivial vs подстрочник (not in Phase-1/tier-1, no note on this verse) — 2. Contrastive_value: single-commentator variant reading — real exegetical gain (1). Register clean (2). Anchoring: tilaka pratika_check `matches_verse: true` → 2. **Verdict: keep**.

**5.20.16**: Note contrasts Tilaka+Bhushana (императив "будь") vs Siromani (compound epithet "bhava-maithilī"). Bundle: Siromani's chunk: "भवेति । हे भवमैथिलि भवति भावयति नितरां स्वपतिं चिन्तयति सा एव मैथिली तत्संबोधनम्" — confirms Siromani reads "bhavamaithili" as one address meaning "she who constantly thinks of her husband." Tilaka/Bhusana don't explicitly gloss "bhava" as imperative in the visible chunk shown (Tilaka's chunk is about "moham" the delusion, not directly glossing "bhava" as imperative) — but the note's claim is that Tilaka and Bhushana read it "as does the translator" (i.e., they don't dispute it, matching Leonov's rendering) — this is a weaker but still fair characterization since neither explicitly contradicts the imperative reading and their preserved verse-text quotes literally repeat "bhava maithili bhāryā me" unchanged (Bhushana quotes the verse verbatim: "भव मैथिलि भार्या मे मोहमेनं विसर्जय"). This is consistent with the imperative reading (not a variant). Faithful — reasonable, borderline; I'll call it 2 since nothing in bundle contradicts it and Siromani's contrast is solidly confirmed. Non-trivial (2, not in подстрочник/tier-1/Phase-1). Contrastive_value: genuine ≥2 commentators (Tilaka+Bhushana vs Siromani) diverging = **2**. Register clean (2). Anchoring: bhusana/siromani/tilaka pratika_check all `matches_verse: true` → 2. **Verdict: keep**.

- 🔧 `Bash` — echo "checking 26 28 30"
**5.20.26**: Note claims Siromani explains Ravana's rhetorical doubt as revenge-motivated (for Shurpanakha), not just mockery. Bundle Siromani: "शूर्पणखाविरूपादिकरणजनिततापशान्तये रामविषयकसीतातिप्रीतिं निवारयितुमाह निक्षिप्तेति" = "To pacify the distress caused by [Rama's] disfiguring Śūrpaṇakhā etc., in order to prevent Sītā's excessive love toward Rāma, [Rāvaṇa] speaks the words beginning 'nikṣiptaḥ...'" This confirms the note's claim precisely — Faithful (2). The `complements_leonov` field correctly distinguishes from Kostina's own note on this verse (which is about the translation of "nikṣiptavijayaḥ" per Gita Press/Goldman, not narrative motivation). Non-trivial (2). Contrastive_value: single commentator, real narrative-motivation gain = 1. Register clean (2). Anchoring: siromani pratika_check `matches_verse: true` → 2. **Verdict: keep**.

**5.20.28**: Note claims Tilaka: Hiranyakashipu got back not the goddess Kīrti herself but a wife "like Kīrti" (kīrti-tulyā bhāryā), taken by Indra, returned through Narada's plea, and Tilaka names Bhagavata Purana as the source. Bundle Tilaka: "इन्द्रहस्तगतां कीर्तिं कीर्तितुल्यां भार्यामिन्द्रहृतां नारदमुखेन प्रार्थनया यथा हिरण्यकशिपुः प्राप्तवान् ... इयं च कथा भागवते प्रसिद्धेति तीर्थः" = "Indrahastagatāṃ kīrtim — a wife like Kīrti (kīrti-tulyāṃ bhāryām), taken by Indra, whom Hiraṇyakaśipu obtained back through supplication via Nārada's mouth ... and this story is well-known in the Bhāgavata, says Tīrtha." This matches the note precisely, including the Tīrtha attribution (the note says "Тилака" but the bundle text attributes the Bhagavata-source remark to "तीर्थः" = Tīrtha, a variant-reading authority frequently cited within Tilaka's commentary, similar to sarga 19's citrāṅgī case). This is a minor attribution nuance: the note says "по «Тилаке»" throughout, but the specific detail "комментатор прямо называет источник сюжета — Бхагавата-пурану" is attributed by the text to Tīrtha, not Tilaka. This is a wording overreach — minor conflation of Tīrtha (a variant-authority voice embedded in Tilaka's commentary) with Tilaka himself for the Bhagavata-attribution clause specifically. This is a faithfulness concern: the bulk of the note (kīrti-tulyā bhāryā, Indra, Narada's plea) is squarely Tilaka's own words, but the closing clause misattributes Tīrtha's remark to Tilaka. Given the rubric ("Misattributed commentator ... ⇒ 0"), this is a real but narrow issue — most of the note is verbatim-correct Tilaka, and only the final clause blurs Tīrtha into "Tilaka." I'll score this as **minor wording overreach = 1** (not a full misattribution of the whole note, but a specific claim attributed to the wrong voice within the same commentary block), which caps faithfulness at 1, triggering the reject gate per rubric ("must be 2, else verdict `reject`").

Let me double check by re-reading the exact bundle text and note wording once more carefully.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
I already have the note text from the earlier Read (line 74-76 of sarga_20_candidates.json): "По «Тилаке», Хираньякашипу вернул не саму богиню Кирти, а «подобную Кирти» жену (kīrti-tulyāṃ bhāryām), похищенную Индрой, — и вернул ее через заступничество (просьбу) Нарады, а не силой. Комментатор прямо называет источник сюжета — Бхагавата-пурану."

The note says "Комментатор" (the commentator, ambiguous referent, could still refer to Tilaka's chunk as a whole since Tīrtha is quoted within Tilaka's chunk, introduced with "इति तीर्थः" as an aside). This is a defensible reading in context since the whole passage is filed under "tilaka" as `source_commentary`, and Tīrtha's aside is embedded inside it as a supporting citation, not a separate commentator in this corpus's schema (unlike Tilaka/Bhushana/Siromani/Tattvadipika which are the four tracked commentators). I'll treat this as acceptable — not a misattribution of a **tracked commentator's identity**, but a defensible loose "commentator" referring to the whole Tilaka gloss-block which includes an embedded citation. This is closer to "minor wording overreach" than "misattributed commentator" in the rubric's intended sense (the rubric's 0-gate targets attributing content to the *wrong dictionary-tracked commentator*, e.g., saying Bhushana said something Tilaka said). Given genuine ambiguity, I will score faithfulness = 2 but flag this nuance in the reason, since the substantive content (Kirti-like wife, Indra, Narada's plea, Bhagavata source) is fully entailed by the bundle text under the "tilaka" key.

- 🔧 `Bash` — echo "sarga20 continuing to 5.20.30"
Non-triviality for 5.20.28: not restating Phase-1's Hiranyakashipu note (which discusses his name etymology and Prahlada-connection generally, but not the "kīrti-tulyā bhāryā via Narada's plea" detail) — non-trivial (2). Contrastive_value: single commentator, real mythic detail = 1. Register clean (2). Anchoring: tilaka pratika_check `matches_verse: true` → 2. **Verdict: keep.**

**5.20.30**: Note claims Siromani reads Ravana's admission (no joy in his own wives after seeing suffering Sita) as evidence of his "dayālutvam" (compassion). Bundle Siromani: "एतेन रावणस्य दयालुत्वं सूचितम्" = "By this, Rāvaṇa's compassionateness (dayālutvam) is indicated." Matches exactly. Faithful (2). Non-trivial vs Phase-1/tier-1 (no note on this verse in either baseline) — 2. Contrastive_value: single commentator, real characterological gain = 1. Register clean (2). Anchoring: siromani pratika_check `matches_verse: true` → 2. **Verdict: keep**.

Now let's write all 5 judge objects for sarga 20.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_20_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_20_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_20_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_20_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_20_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_20_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 20 done: 5 keep. Now sarga 21.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_21_candidates.json
Now let's read the segmented bundle for sarga 21, focused on verses 3, 9, 17, 19, 32.

- 🔧 `Grep` — "verse_id": "5\.21\.(3|9|17|19|32)"
No line numbers returned for -n with just a match. Let me use Grep with output content and get line numbers to know where to Read.

- 🔧 `Grep` — "verse_id": "5\.21\.(3|9|17|19|32)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_21_segmented.json
Now for 5.21.9, 5.21.17, 5.21.19, 5.21.32:

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_21_segmented.json
Excellent — this confirms 5.21.9. Now check 5.21.17, 5.21.19, 5.21.32:

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_21_segmented.json
This is important — I see the note attributed the "sādhu rāvaṇa" analysis to Bhushana, but this Bhushana chunk (about the path-thief/water-beggar simile) is actually the segmenter's chunk for **verse 19** (labeled `"5.21.19"` in the JSON, but internally the Bhushana text explicitly says `४.२१.१८` = "4.21.18" as its own verse marker, and it discusses "साधु रावण..." which is verse 18's opening words). Let me check the candidate note's text again carefully.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
I already have the note text from the initial read of sarga_21_candidates.json (verse_id 5.21.19, lemma "sādhu rāvaṇa"):

> «Бхушана» поясняет, что обращение Ситы к Равану («sādhu rāvaṇa») звучит как мольба путника к разбойнику или нищего, просящего воды у чужого: сама вынужденная просительность ее речи, по его прочтению, свидетельствует, что разлука с ней лишь усилила жестокость Раваны.

This is a **critical anchoring problem**. The note is tagged `verse_id: "5.21.19"` and `lemma_iast: "sādhu rāvaṇa"`, but "sādhu rāvaṇa" is the opening phrase of **verse 18** (`5.21.18`), not verse 19. Looking at the bundle: verse 18's own text is `sādhu rāvaṇa rāmeṇa māṃ samānaya duḥkhitām` — that's where "sādhu rāvaṇa" belongs. The Bhushana commentary text quoted in the note ("pathicoraṃ pānīyayācakavad rāvaṇam arthayate sādhu iti" = "like a wayfarer [begging] a thief, or a beggar asking for water from a stranger, she entreats Rāvaṇa, [saying] 'sādhu'...") is indeed the Bhushana gloss on **verse 18**'s "sādhu rāvaṇa" phrase — but in the segmented bundle it's been placed (segmentation artifact) under the `5.21.19` bundle's `bhusana` field, with an internal marker "4.21.18" confirming its *true* verse anchor is 18, not 19. Also `pratika_check` for this exact Bhushana chunk under 5.21.19 shows `matches_verse: false, content_containment: 0.636, content_anchor: true` — flagged as unverified pratīka, salvaged only via content-anchor to verse 19, but the internal `४.२१.१८` colophon-style marker embedded in the text is strong internal evidence it actually glosses v.18, which is a **misalignment the drafter should have caught** by checking verse 18's own bundle where the same simile literally is present.

This is exactly the kind of case the rubric's anchoring axis exists for. Let me verify verse 18's own bundle already has this exact material (it does — I read it above, lines 476-479, `bhusana`: "साधु रावण रामेण मां समानय दुःखिताम् । वने वाशितया सार्धं करेण्वेव गजाधिपम्" — that's the verse-repeat quote, not the elaborate simile). Let me re-check: the elaborate "pathicoraṃ pānīyayācakavad" simile text appears attached to the **5.21.19** bundle's bhusana field, immediately followed by internal cross-reference marker "४.२१.१८" mid-text, then continuing with verse 19's actual content ("mitram aupayikaṃ kartuṃ...").

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_21_segmented.json
This confirms it precisely: the Bhushana chunk under bundle `5.21.19` is actually the Bhushana gloss on **verse 18** ("sādhu rāvaṇa rāmeṇa māṃ samānaya..." — its pratīka literally begins "pathicoraṃ pānīya-yācakavat rāvaṇam arthayate sādhu iti" = commenting on "sādhu"), followed mid-block by a marker "।। 4.21.18।।" (an internal sarga/verse label — note this uses "4." prefix likely a scan/OCR quirk for kāṇḍa 5, but the verse number 18 is clear), and only afterward does the actual verse-19 commentary begin ("mitram aupayikaṃ kartuṃ..."). This is a **merged/shifted bhusana chunk**: content genuinely belongs to v.18, mis-segmented into the v.19 bundle. The note draws entirely from the v.18-belonging portion of this chunk while citing it as `verse_id: 5.21.19`.

This is the anchoring rubric's contradicted case: "contradicted (segmenter's own chunk shows internal `।।4.21.18।।` marker pointing elsewhere and the note's content fits that other verse) ⇒ 0 ⇒ verdict `flag_anchor`."

- 🔧 `Bash` — echo "confirmed anchoring issue for 5.21.19"
Now let's check verse 32 for the Vṛtra myth note.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_21_segmented.json
Confirmed: Tilaka's chunk for 5.21.32 matches note precisely ("vajracchinnaikabāhur vṛtro bahukālam indreṇa sahaikabāhunā yuddhaṃ kṛtavān parājitaś ceti bhāgavate prasiddham" = "Vṛtra, whose one arm was severed by the vajra, fought for a long time against Indra with his remaining single arm and was [eventually] defeated — this is well-known in the Bhāgavata"). Matches the note claim exactly, including the Bhagavata source attribution (this time correctly attributed to Tilaka's own voice, no Tīrtha aside). Faithful (2).

Now let me pull the tier-1/Phase-1 baselines for sarga 21.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s21_leonov.json
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s21_phase1.json
Baselines confirmed for verses 3, 9, 17, 19, 32. Notably, tier-1 Kostina's own note on v.19 already flags confusion about "было бы хорошо его внедрить, потому что в 18 стихе речь про слона, потом появляется бык меж мужами, читатель может запутаться" — confirming she noted the same v.18/v.19 boundary risk, which strengthens my anchoring concern. Now let me score all 5 sarga 21 notes.

**5.21.3** (`tṛṇam antarataḥ kṛtvā`): Note explains the ritual logic of the straw gesture. Bundle Tilaka: "तृणमन्तरतः कृत्वा परपुरुषस्य साक्षात्संभाषणानर्हत्वात् भूम्यां किञ्चिदन्तर्धाय मूत्रादिविसर्जनवत्तृणान्तरेण तस्य मुखे प्रत्युत्तरदानम् ... एतेन तृणीकृतप्राणतया तृणतुल्यतया रावणस्य ग्रहणाच्च निभयप्रत्युत्तरदानमिति बोध्यम्" — matches both claims (ritual barrier logic + treating Ravana as a mere straw/insignificant). Faithful (2). Non-trivial vs tier-1's own note (which only cites the Āraṇyakāṇḍa parallel and requests "comm. needed on the straw itself") — Tilaka fills exactly that gap (2). Contrastive_value: single commentator, real exegetical gain (1). Register clean (2). Anchoring: tilaka pratika_check `matches_verse: true` → 2. **Verdict: keep**.

- 🔧 `Bash` — echo "sarga21 continue"
**5.21.9** (`santo na vā santi`): Note contrasts Tilaka+Siromani (open question) vs Bhushana (rhetorical answer citing Vibhishana as proof of righteous people in Lanka). Bundle Bhushana: "सन्तः त्वामनर्थान्निवारयन्तः । न सन्ति वा न सन्ति किम्? सन्त्येव । श्रीविभीषणप्रभृतीनां सम्भवान्न सन्तीति कथं वक्तुं शक्यम्?" = "Are there no righteous ones dissuading you from ruin? [Rhetorical:] No such — how could one possibly say there are none, given the existence of Śrī Vibhīṣaṇa and others?" Matches note precisely. Tilaka/Siromani chunks are indeed open/neutral in phrasing ("इह लङ्कानगरे सन्त ... न वा नैव सन्ति" / "इह लङ्कायां सन्तो महात्मानो न सन्ति वा"). Faithful (2). Non-trivial (2, absent from any baseline — Kostina's own note is about translation register of "बунтует"/"ниспровергая", not this exegetical divergence). Contrastive_value: genuine ≥2/3 commentators diverging = **2**. Register clean (2). Anchoring: tilaka/bhusana pratika `matches_verse:true`; siromani `matches_verse:false, content_anchor:true` → still verified (2). **Verdict: keep**.

**5.21.17** (`viprasya viditātmanaḥ`): Note claims Tilaka gives variant reading "dhīrasya" for "viditātmanaḥ", and that some commentators broaden "vipra" to all three twice-born varnas (not just brahmins) since they hold brahmavidya is available to any of the three. Bundle Tilaka: "अन्ये तु-- विप्रपदं त्रैवर्णिकपरम्, त्रैवर्णिकस्यैव ब्रह्मविद्यायामधिकारः, अत एव \"धीरस्य\" इति क्वचित्पाठ इत्याहुः" = "Others say: the word 'vipra' here refers to all three varnas [twice-born], since only the twice-born (trai-varṇika) have entitlement to brahmavidyā — hence the variant reading 'dhīrasya' in some [texts]." This matches the note's claims very precisely (though the note reverses the causal order slightly — presenting the "dhīrasya" variant first and the varna-broadening as "noting" a consequence, while the source presents the reasoning then cites the variant as consequence — but this is a stylistic compression, not a factual distortion). Faithful (2). Non-trivial vs подстрочник/baselines (no baseline note on this verse) — 2. Contrastive_value: single commentator, doctrinal variant = 1. Register clean (2). Anchoring: tilaka pratika_check `matches_verse: true` → 2. **Verdict: keep**.

**5.21.19** (`sādhu rāvaṇa`) — as established above, the cited content genuinely belongs to verse 18 (the segmenter's own embedded marker "।। 4.21.18 ।।" mid-chunk confirms this), not verse 19 where the note is filed. The note's lemma itself ("sādhu rāvaṇa") is the opening of v.18, not v.19 (v.19's actual text is "mitram aupayikaṃ kartuṃ rāmaḥ sthānaṃ parīpsatā..."). This is a genuine anchoring contradiction: the segmenter's chunk shows an internal marker pointing to verse 18, and the note's entire content (the wayfarer/beggar simile) fits verse 18, not verse 19. Faithfulness of the note's content against the *actual* Bhushana text is fine (2) — but anchoring fails hard. Non-triviality: irrelevant given the anchor issue, but genuinely new content (2). Contrastive_value: single commentator (1). Register: clean prose (2). **Anchoring = 0** (contradicted — chunk's internal marker points to v.18, note's content fits v.18, filed under v.19). Per precedence, `flag_anchor` overrides all except `reject`; since faithfulness=2 (not <2), verdict = **flag_anchor**.

- 🔧 `Bash` — echo "continue to 32"
**5.21.32** (`vṛtrasyevendrabāhubhyāṃ`): Already confirmed above — Tilaka's chunk matches exactly, including Bhagavata Purana source attribution correctly in Tilaka's own voice. Faithful (2). Non-trivial vs подстрочник (which has the simile but not the backstory) and Phase-1 (no note on this verse) — 2. Contrastive_value: single commentator, mythic backstory = 1 (though kazansky_type is В for realia/myth — still single-commentator, not ornament, real gain). Register clean (2). Anchoring: tilaka pratika `matches_verse: true` → 2. **Verdict: keep**.

Now let me write all 5 judge objects for sarga 21.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_21_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_21_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_21_candidates.json
Now the flag_anchor case for 5.21.19:

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_21_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_21_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_21_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 21 done: 4 keep, 1 flag_anchor. Now sarga 23.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_23_candidates.json
Sarga 23 has zero notes to judge — nothing to score. Just update `_meta`.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_23_candidates.json
Now sarga 25.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_25_candidates.json
Now let's check the segmented bundle for sarga 25 (verses 3, 5, 6) and baselines.

- 🔧 `Grep` — "verse_id": "5\.25\.[356]"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_25_segmented.json
Now let's check baselines for sarga 25.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s25_leonov.json
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s25_phase1.json
Now I have full baselines. Let me judge the 3 notes for sarga 25.

**5.25.3** (`kāmaṃ khādata māṃ sarvā`): Note claims Tilaka reads Sita's whole speech as "actor-like imitation" (naṭavad anukaraṇa-rūpa) since she has taken a human body — reminding the reader she's a goddess whose despair is part of her assumed human nature. Bundle Tilaka: "अयं सर्वः सीताप्रलापो गृहीतमनुष्यशरीरतया नटवदनुकरणरूप इति बोध्यम्" = "This entire lament of Sītā is to be understood as actor-like imitation (naṭavad anukaraṇarūpa), on account of her having taken on a human body." Matches note precisely. Faithful (2). Non-trivial vs подстрочник/tier-1 (tier-1 only has a poetics-formula note, no doctrinal frame)/Phase-1 (no note here) — 2. Contrastive_value: single commentator, real doctrinal gain = 1. Register: clean, though note has a small typo "авāтара" (should be "аватара") — this is a minor typo, not a register-breaking issue (still readable Russian, no Devanagari, no essay) — I'll treat register as 2 since the typo doesn't break intelligibility, but flag it in the reason for a human fix (this could arguably be "edit" for a fixable wording issue — let me reconsider). Actually the rubric says "register — Fixable wording ⇒ 1 (verdict `edit` + say what to fix)." A typo is a fixable wording issue. Given the typo "авāтара" is a garbled rendering of "аватара" (avatar/incarnation) with a stray macron and missing letter, this is a minor OCR/typo-like defect. I'll score register = 1 and verdict = **edit** to flag the fix needed.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
I already have the why_proposed text from the earlier full read: "даёт доктринальную рамку (авāтара играет человеческую роль), отсутствующую в подстрочнике..." — confirms the typo "авāтара" is in the `why_proposed` field, not the `note_ru` field itself. Let me re-check note_ru text precisely.

The `note_ru` text (from the earlier full read) is: "По Тилаке, вся речь Ситы перед ракшаси — это речь актёра, играющего роль (наṭавад анукараṇарӯпа), поскольку она приняла человеческое тело; комментатор напоминает, что перед читателем не обычная испуганная женщина, а богиня, чьё отчаяние — часть принятой ею человеческой природы."

I see the actual issue now: the transliteration "наṭавад анукараṇарӯпа" mixes Cyrillic and IAST diacritics awkwardly (ṭ, ṇ, ӯ inserted into Cyrillic letters) — this is a genuine register violation: the style contract requires "no Devanagari" and clean Russian prose with a "short IAST pratīka lemma," but here the Sanskrit term is transliterated as a garbled Cyrillic/IAST hybrid embedded mid-sentence ("наṭавад анукараṇарӯпа" instead of proper IAST "naṭavad anukaraṇarūpa" or leaving it in clean Cyrillic transcription "натавад анукаранарупа"). This is a fixable wording defect — the term should either be pure IAST in a separate clause or transliterated cleanly into Cyrillic, not this hybrid. This confirms register = 1, verdict = **edit** (fix: replace "наṭавад анукараṇарӯпа" with clean IAST "naṭavad anukaraṇarūpa" set off properly, matching the note's own lemma_iast convention).

Non-triviality (2), contrastive_value (1), faithfulness (2), anchoring: tilaka pratika `matches_verse: true` → 2.

**5.25.5**: Note claims Tilaka and Siromani gloss "viśantīvāṅgam ātmanaḥ" as literally "shrunk into her body from fear, like a turtle (kamaṭha)". Bundle Tilaka: "आत्मनो ऽङ्गं विशन्तीव भीत्यातिसङ्कुचितशरीरा कमठवदभूदित्यर्थः" = "as if entering into her own limb — became extremely contracted in body from fear, like a turtle (kamaṭhavat)." Siromani: "आत्मनो ऽङ्गम् आविशन्तीव कमठवत् सङ्कचितशरीरेत्यर्थः" — same turtle image. Matches note exactly. Faithful (2). Non-trivial vs Phase-1 (Phase-1's note on this verse is about "koka" = wolf, not this turtle image) — 2. Contrastive_value: two commentators converging on the same image = 2 (though not exactly "contrasted," they "genuinely... contrasted OR a translation choice resolved" — this is convergence not contrast; per the rubric's "single commentator with real exegetical gain ⇒ 1" vs "≥2 commentators genuinely contrasted ⇒ 2" — two commentators independently confirming the same image is not really a "contrast" but a convergence. I'll score this conservatively as 1 (real exegetical gain, from what functions as essentially one shared reading, not a divergence)). Register clean (2). Anchoring: tilaka/bhusana/siromani all pratika `matches_verse: true` → 2.

- 🔧 `Bash` — echo "checking 5.25.6"
**5.25.6** (`aśokasya … śākhām`): Note claims three-way divergence on identifying the tree: Siromani says it's not actually ashoka but a shinshupa "called ashoka-like" (aśoka-sadṛśā śiṃśupā); Bhushana says it's a specific ashoka tree near the shinshupa where Hanuman later sits; Tilaka (referring the explanation to both vv.6-7) allows both readings. Leonov's translation keeps neutral "ashoka" without choosing.

Bundle Siromani (v.6): "अशोकस्य अशोकसदृशस्य शिंशुपायाः विपुलां शाखामालम्ब्य" = "of ashoka, i.e., of the ashoka-like shiṃśupā, having grasped the broad branch" — matches note's claim about Siromani exactly. Bundle Bhushana (v.6): "अशोकस्य हमुमदधिष्ठतशिंशुपासन्निहितस्य" = "of the ashoka situated near the shiṃśupā where Hanuman [later] resides" — matches note's Bhushana claim exactly (specific ashoka near the shinshupa). Bundle Tilaka (v.7, but explicitly relating to "5.25.6,7"): "अशोकस्याशोकवनिकासंबन्धिनः शिंशपावृक्षस्य तत्समीपवर्तिनो ऽशोकस्यैव वा" = "of ashoka — [meaning] either the shiṃśapā tree belonging to the ashoka-grove, or of the nearby ashoka tree itself" — matches note's claim that Tilaka allows both readings. All three claims confirmed faithful (2).

Non-trivial: absent from any baseline (tier-1 only flags an omitted word "śokena"; Phase-1 has no note on this verse) — 2. Contrastive_value: genuine three-way divergence on tree identification = **2**. Register clean, well-structured contrastive note (2). Anchoring: bhusana pratika `matches_verse: true`; siromani `matches_verse: false, content_anchor: true` (v.6); tilaka's relevant chunk is filed under v.7's bundle but explicitly self-labeled "।। 5.25.6,7 ।।" indicating it covers both verses — this is a merged-range self-declared scope, not a contradiction, and its pratika_check for v.7 shows `matches_verse: true`. Since the note draws on Tilaka's material explicitly spanning both v.6 and v.7 (labeled as such in-text), and the drafter's own `rejected` entry for v.7 explicitly says "материал (идентификация ашоки) уже учтён в контрастивном примечании к 5.25.6" (cross-referencing this exact reuse), this is handled transparently, not a hidden misattribution. Anchoring = 2 (verified, cross-verse scope is self-declared by the source).

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_25_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_25_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_25_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_25_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 25 done: 2 keep, 1 edit. Now sarga 27.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_27_candidates.json
This is a rich one with 4 notes, including 2 interpolation notes with self-declared internal addressing. Let me check the segmented bundle for verses 12, 19, 30, 53.

- 🔧 `Grep` — "verse_id": "5\.27\.(12|19|30|53)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_27_segmented.json
Confirmed for 5.27.12: Tilaka's chunk "सङ्गता तत्रैव पर्वत इति शेषः । एतेन लङ्कायामेव रामस्य सीतादर्शनं सूचितम्" = "'saṃgatā' [means] there itself on the mountain — thus is indicated that Rāma's seeing Sītā [will occur] precisely in Lankā." This matches the note's claim exactly. Now let's check 5.27.19 and 5.27.30.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_27_segmented.json
Confirmed for 5.27.19: Tilaka's chunk verbatim: "अत्र मध्ये "साण्डं भुवनम्" इत्यादयो बहवः श्लोका रामानुजसंप्रदायपुस्तकेषु दृश्यन्ते ते प्रक्षिप्ता इति कतकादयो ऽन्ये च" = "Here in the middle, many verses beginning 'sāṇḍaṃ bhuvanam' etc. are seen in books of the Rāmānuja tradition [śrīvaiṣṇava]; these are interpolated — [say] Kataka and other [commentators]." Matches note precisely, including "Kataka" attribution. Now let's check 5.27.30.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_27_segmented.json
I don't see the "pibatāṃ rakṣasāṃ" Tilaka interpolation reference in this bundle for verse 30 explicitly. The note claims: "по Тилаке (со ссылкой на комментатора Катаку), два последующих стиха о ракшасах, пьющих масло на тонущей в океане Ланке, считаются интерполяцией. Сегментация приписывает эту помету... соседнему стиху из-за смещения маркера." Let me search for where this Tilaka interpolation note about "pibatāṃ" actually is located in the bundle.

- 🔧 `Grep` — pibat|पिबत|प्रक्षिप्त
There's no Tilaka commentary text about interpolation of "pibatāṃ rakṣasāṃ" verses visible in this bundle at all — I only found the Bhushana quote of the verse itself (not a Tilaka interpolation note), and line 440 which was already the "sāṇḍaṃ bhuvanam" interpolation note for verse 19 (different interpolation, different location, different tradition citation). Let me check line 99 and 1225, and also search for "kataka" / "कतक" more broadly.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_27_segmented.json
Found it — the Tilaka interpolation note is actually located under the **5.27.3** bundle (not 5.27.30), with an explicit internal scope marker "।। 5.27.30,31 ।।" declaring it applies to verses 30–31. The text: "एतदग्रे श्लोकद्वयं प्रक्षिप्तमिति कतकः ... पिबतां तैलादि पिबतां रक्षसां वासभूता लङ्का सागरे पतितेत्यन्वयः" = "The next two verses [from here] are interpolated — says Kataka ... [referring to] 'pibatāṃ' oil etc. — 'of the rakshasas drinking, [as their] abode Lankā fell into the ocean' is the construal." This matches the note's claim precisely, and the note itself correctly explains the misalignment: "Сегментация приписывает эту помету... соседнему стиху из-за смещения маркера; по содержанию она относится именно к этому месту" (the segmentation attributes this note to a neighboring verse due to marker offset; by content it belongs here) — and further: "привязка стиха взята из собственной внутренней ссылки Тилаки (।। 5.27.30,31 ।।), а не только из маркера сегментации — комментарий сам называет адрес" (the verse-attachment comes from Tilaka's own internal reference, not just the segmentation marker — the commentary itself names the address).

This is a case where the drafter has **correctly diagnosed and corrected** a segmentation misalignment by relying on the source's own internal cross-reference, exactly as the method doc's §11 anticipates as a residual failure mode. This is good practice, not a violation — but let's verify anchoring carefully per rubric: the note's `verse_id` is `5.27.30`, but the segmented bundle's `pratika_check` for verse_id 5.27.30 does not contain this Tilaka chunk at all (it's actually filed under bundle 5.27.3's `pratika_check`, which shows `tilaka: matches_verse: true` — matching verse 3, not verse 30). The chunk is correctly pratīka-verified **for its filed location (verse 3)**, but the *note* reassigns it to verse 30 based on the commentator's own internal cross-reference.

- 🔧 `Bash` — echo "assessing anchoring for 5.27.30 note"
This is a legitimate but unusual anchoring case. The rubric's anchoring axis is meant to check whether the *cited content* truly belongs to the verse the note claims. Here, the segmenter's own automated `pratika_check` mechanism verified the chunk against verse 3 (where it happens to sit due to a marker/OCR position glitch), but the source text itself carries an explicit internal marker "।। 5.27.30,31 ।।" that is stronger and more specific evidence than the segmenter's automated verification — this is exactly analogous to sarga 21's `5.21.19` case, except there the internal marker contradicted the note's claimed verse (making it wrong), while here the internal marker **confirms** the note's claimed verse (making it right) despite the segmenter's mechanical pratīka match pointing elsewhere. This is the mirror-image case: correctly reassigned per the source's own explicit self-reference, not a genuine misattribution. I'll score anchoring = 1 ("unverified but plausible" by the automated `pratika_check` signal, but well-supported by the source's own explicit in-text address) — reflecting that automated verification doesn't confirm it, but the reasoning is sound and traceable. This doesn't trigger `flag_anchor` per rubric (only 0 does that); a 1 keeps the note eligible for `keep` if other gates pass.

Now let's check verse 53 (the pakṣī note).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_27_segmented.json
This confirms the note precisely for 5.27.53. Tilaka: literal bird auspicious-omen reading ("शाखानिलयं शाखास्थनीडं प्रविष्टो ... शोभनप्राप्तिं सूचयतीव" = a bird entering its branch-nest, foretelling good news). Siromani: similarly literal (auspicious bird reading). Bhushana: the extended allegorical Śrīvaiṣṇava reading is present in full (the massive block about Lankā=body, senses=rakshasas, Rāvaṇa/Kumbhakarṇa=ahaṅkāra/mamakāra, bird=guru with two wings of jñāna and karma, etc.) — this matches the note's claims about all three commentators exactly, including the specific allegorical mapping details. Faithful (2).

Now let's get the baselines for sarga 27.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Given the volume, let me quickly filter to just the relevant verses (12, 19, 30, 53) from both baselines.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s27_filtered.json
Good — this confirms tier-1's own note discusses only the literal bird-type identification (crow/piṅgalikā/Garuḍa per various commentaries), not the allegorical Śrīvaiṣṇava reading the drafted note highlights — confirming non-triviality (2) for the contrastive note. No baseline covers verses 12, 19, or 30. Now let's finalize scores for all 4 sarga 27 notes.

**5.27.12**: Faithful (2), non-trivial (2, no baseline), contrastive_value: single commentator = 1, register clean (2), anchoring: tilaka pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.27.19**: Faithful (2), non-trivial (2, distinct from the separate interpolation note at v.30-31 as explicitly noted), contrastive_value: single commentator, textological gain = 1, register clean (2), anchoring: tilaka pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.27.30**: Faithful (2, content matches Tilaka's chunk exactly, correctly cross-referenced via source's own internal marker), non-trivial (2), contrastive_value: single commentator = 1, register clean (2), anchoring = 1 (mechanically verified against a different verse (3) by the automated pratika_check, but strongly and correctly supported by the source's own explicit internal address "।। 5.27.30,31 ।।" — plausible but not machine-verified for its claimed verse). **Verdict: keep** (anchoring=1 doesn't trigger flag_anchor; only 0 does).

**5.27.53**: Faithful (2), non-trivial (2, tier-1 only covers bird-species identification, not the allegorical reading), contrastive_value: genuine 2-vs-1 divergence between literal (Tilaka+Siromani) and allegorical (Bhushana) reading = **2**, register clean — though this note is dense/long conceptually but stays within the "1-3 sentences" formal limit in note_ru (it's actually a single well-formed sentence structure) = 2, anchoring: all three pratika `matches_verse: true` → 2. **Verdict: keep**.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_27_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_27_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_27_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_27_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_27_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 27 done: 4 keep. Now sarga 28.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_28_candidates.json
Now let's check the segmented bundle for verses 14, 18, 20 in sarga 28.

- 🔧 `Grep` — "verse_id": "5\.28\.(14|18|20)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_28_segmented.json
This confirms all 3 notes precisely.

**5.28.14**: Note claims Siromani directly rebuts the jealous inference with "etena rāmasya bhāryāntaraṃ nāsti iti sūcitam". Bundle Siromani: "एतेन रामस्य भार्यान्तरं नास्तीति सूचितम्" — exact match. Faithful (2). Non-trivial (Kostina's tier-1 note only covers "vītabhayaḥ" etymology, this adds a different point about the rhetorical status of Sita's speech) — 2. Contrastive_value: single commentator, real exegetical gain = 1. Register clean (2). Anchoring: siromani pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.28.18**: Note claims Bhushana gives a second reading "as if entering fire" (agnipraveśaṃ kurvantīva) foreshadowing the future agni-parīkṣā. Bundle Bhushana: "यद्वा पुष्पितमाससाद अग्निग्रवेशं कुर्वन्तीवेत्यर्थः" (note: "अग्निग्रवेशं" is likely OCR of "अग्निप्रवेशं") — matches note precisely (alternate reading = "as if performing fire-entry"). Faithful (2). Non-trivial vs подстрочник/baselines (no baseline note on this verse) — 2. Contrastive_value: single commentator, striking narrative foreshadowing = 1. Register clean (2). Anchoring: bhusana pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.28.20**: Note claims Bhushana reads Sita's remembering her own family as revealing fear of "durmaraṇa" (bad/sinful death, i.e., suicide), and that good omens appear exactly when she's about to transgress this taboo. Bundle Bhushana: "स्वं च कुलं विचिन्तयन्त्या इत्यनेन दुर्मरणात् भीतत्वं व्यज्यते" = "By this—'thinking of her own family'—her fear of a bad/sinful death (durmaraṇa) is conveyed." Matches note's core claim exactly. The "good omens appear exactly when she's about to transgress" framing is the drafter's own inferential synthesis but is a reasonable reading given the verse's content (auspicious omens appear right as she contemplates suicide) — not an invented claim, but a light interpretive gloss atop the confirmed textual point. I'll treat this as within acceptable synthesis, not overreach — faithful (2). Non-trivial vs baselines (no note on this verse in either tier-1 or Phase-1) — 2. Contrastive_value: single commentator, psychological subtext = 1. Register clean (2). Anchoring: bhusana pratika `matches_verse: true` → 2. **Verdict: keep**.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_28_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_28_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_28_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_28_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 28 done: 3 keep. Now sarga 29.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_29_candidates.json
Now let's check the segmented bundle for sarga 29 verses 1, 5, 7.

- 🔧 `Grep` — "verse_id": "5\.29\.(1|5|7)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_29_segmented.json
This confirms all three notes. Let me check the tier-1/Phase-1 baselines for sarga 29.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s29_leonov.json
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s29_phase1.json
Now let me judge the 3 notes.

**5.29.1** (`tathāgatāṃ tāṃ vyathitām`): Note claims Bhushana reads "tathā" not as neutral but as marking extremity of grief, citing Sita's own earlier words about 12 peaceful years. Bundle Bhushana: "तां धर्मिस्वरूपातिरिक्तयत्किंचिदतिशयरहिताम् । व्यथिताम् ... तथा च पूर्वोक्तं सर्वं धर्मिस्वरूपमात्रम् । इतः परमेव व्यसनानि भविष्यन्तीति मन्यमानाम् । "समा द्वादश तत्राहं राघवस्य निवेशने । भुञ्जाना मानुषान् भोगान् सर्वकामसमृद्धिनी ।" इत्युक्तं भोगजातं सर्वमकिंचित्करमासीत्, दुःखमेव निरूपकमासीत्" — matches note precisely, including the verbatim 12-years quote ("samā dvādaśa tatrāhaṃ rāghavasya niveśane bhuñjānā mānuṣān bhogān sarvakāmasamṛddhinī"). Faithful (2). Non-trivial vs подстрочник/tier-1 (tier-1 has no note on this verse)/Phase-1 (Phase-1's note on this verse is about "nimitta" term generally, not this specific narrative-callback point) — 2. Contrastive_value: single commentator, real narrative-callback gain = 1. Register clean (2). Anchoring: bhusana pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.29.5** (`śikharāgradantyāḥ`): Note claims Bhushana adds a samudrika-śāstra (body-signs science) doctrine that teeth-like-pomegranate-seeds ensure the husband's longevity. Bundle Bhushana: "शिखरदन्तत्वे सामुद्रिकम् "स्निग्धास्समानुरूपाः सुपङ्क्तयः शिखरिणः श्लक्ष्णाः । दन्ता भवन्ति यासां तासां पादे जगत्सर्वम् ।।" इति, "यासां शिखरिणो दन्ता दीर्घं जीवन्ति ताः स्त्रियः" इति च" — this quotes samudrika verses about women with such teeth: "at whose feet the whole world [bows]" and "women whose teeth are śikhariṇa [pointed like pomegranate seeds] — their [husbands] live long" (यासां शिखरिणो दन्ता दीर्घं जीवन्ति ताः स्त्रियः — literally "those women whose teeth are śikhariṇa, [their husbands? they themselves?] live long" — the Sanskrit is ambiguous about whose longevity, but "तासां...दीर्घं जीवन्ति" more naturally parses with an implied husband subject in this genre of physiognomy verses about auspicious wife-signs). This is a defensible reading of the samudrika citation matching the note's claim. Faithful (2). Non-trivial vs Kostina's tier-1 note (which covers only the Tilaka translation of the compound + the "approaching lover" sign, not the samudrika longevity omen) and Phase-1 (no note on this verse) — 2. Contrastive_value: single commentator, real doctrinal addition = 1. Register clean (2). Anchoring: bhusana pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.29.7** (`bhrukeśāntam`): Note claims Bhushana explains the omitted compound "bhrukeśānta" as not just "brows and hair" but disheveled locks at the temples framing the upper face. Bundle Bhushana: "स्वक्षिभ्रुशोभनाक्षिश्रूयुक्तम् । केशाः अन्ते यस्य तत् केशान्तम् । उपरिभागप्रकीर्णालकमित्यर्थः" = "svakṣibhru = endowed with beautiful eyes and brows; keśānta = 'that which has hair at its end' — meaning locks scattered in the upper region." Matches note's claim well ("растрёпанные у висков пряди" — disheveled locks at the temples/upper region). Faithful (2). Non-trivial vs Kostina's note (which just flags the omission without content) — 2. Contrastive_value: single commentator = 1. Register clean (2). Anchoring: bhusana pratika `matches_verse: true` → 2. **Verdict: keep**.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_29_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_29_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_29_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_29_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 29 done: 3 keep. Now sarga 31.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_31_candidates.json
Now let's check the segmented bundle for verses 9, 19 in sarga 31.

- 🔧 `Grep` — "verse_id": "5\.31\.(9|19)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_31_segmented.json
Confirmed for 5.31.9: Bhushana's chunk "मृगयां परिधावता मृगयामुद्दिश्य परिधावता । अनेन लीलया खरादिवधः सूच्यते" = "'mṛgayāṃ paridhāvatā' [means] roaming about for the purpose of hunting; by this [word] it is indicated that the killing of Khara etc. was [done] playfully (līlayā)." Matches note exactly. Now let's check verse 19.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_31_segmented.json
Confirmed for 5.31.19: Bhushana's chunk gives the full reasoning chain: "स्वरविशेषेणायं वानरः, तत्रापि न स्वतन्त्रः, किन्तु स्वसजातीयस्य राज्ञः कस्यचिदमात्यो ऽयम्, तद्राज्यकार्यमेतद्धस्तगतमिति निश्चितवती" = "by the particular quality of the voice, [she inferred] this is a monkey — moreover, not independent, but the minister of some king of his own kind; she concluded this matter [her rescue] is now in his hands." Then the sun/Aruṇa lexical fork: "सूर्यशब्देन तत्संबन्ध्यरुणो लक्ष्यते । "सूर्यो ऽरुणे च सूर्ये च" इति निघण्टुरस्तीत्याहुः" = "By the word 'sūrya' his relative Aruṇa is meant — some say there is a lexicon entry 'sūrya [means] both Aruṇa and the sun.'" This matches the note precisely, including both claims (inference chain + sun/Aruṇa lexical fork). Faithful (2).

Now let's get baselines for sarga 31.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s31_leonov.json
Good — this confirms tier-1's note on 5.31.19 is only about omitted words, not the reasoning chain/lexical fork. No Phase-1 note on either verse, no tier-1 note on 5.31.9. Both notes are clearly non-trivial.

**5.31.9**: Faithful (2), non-trivial (2, no baseline covers this), contrastive_value: single commentator = 1, register clean (2), anchoring: bhusana pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.31.19**: Faithful (2), non-trivial (2, distinct from Kostina's omission-flag note), contrastive_value: single commentator, but this note bundles two distinct exegetical points (inference chain + lexical fork) — still from one commentator = 1, register clean (2, note is a bit long/two-part but stays within reasonable bounds and the register contract allows up to "1-3 sentences" — checking sentence count: the note_ru has essentially 2 sentences plus a closing clause — acceptable), anchoring: bhusana pratika `matches_verse: true` → 2. **Verdict: keep**.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_31_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_31_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_31_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 31 done: 2 keep. Now sarga 32.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_32_candidates.json
Let's check the segmented bundle for verses 4, 6, 8, 11.

- 🔧 `Grep` — "verse_id": "5\.32\.(4|6|8|11)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_32_segmented.json
This confirms 5.32.4, 5.32.6, and 5.32.8. Let's check note claims closely:

**5.32.4**: Note claims Tilaka: fear of illusion (māyā) recurrence, Siromani: longing for Rama (rāmātismṛtyā vaicittyam). Bundle Tilaka: "पुनरपि मायैवेयमिति भयान्मुमोह" = "again fainted from fear [thinking] 'this is māyā again'." Bundle Siromani: "अत एव दुर्निरीक्ष्यमिदमिति मत्वापि पुनर्मुमोह रामातिस्मृत्या वैचित्यं प्राप" = "even having thought 'this is hard to look upon,' she again fainted — she attained distraction through excessive remembrance of Rāma (rāmātismṛtyā vaicittyam)." Matches note exactly, including verbatim quoted term. Faithful (2).

**5.32.6**: Note claims Tilaka+Siromani: Sita cries deliberately softly out of caution so rakshasis won't notice the unfamiliar monkey. Bundle Tilaka: "मन्दमन्दस्वरा । अस्य दैवगत्या वास्तवत्वे राक्षस्यो मा जानन्त्वित्यतिमन्दस्वररोदनम्" = "mandamandasvarā — [meaning] weeping in an extremely soft voice, [with the thought] 'may the rakshasis not know of this [monkey's] reality by chance'." Bundle Siromani: "मन्दस्वरेत्यनेनेमं वानरं राक्षस्यो न जानन्त्वित्यभिप्रायः सूचितः" = "by 'mandasvara' the intention 'may the rakshasis not know of this monkey' is indicated." Matches note exactly. Faithful (2).

**5.32.8**: Note claims Tilaka+Siromani: Sita faints because she thinks this is Ravana in disguise again. Bundle Tilaka: "सा तं कपिरूपं रावणमित्येव समीक्ष्य भृशं विसञ्ज्ञा" = "having beheld him thinking 'this monkey-form is indeed Rāvaṇa,' she became extremely unconscious." Bundle Siromani: "तं हनूमन्तं समीक्ष्य रावणत्वेन वितर्क्य गतासुकल्पा" = "having beheld Hanumān and inferred [him to be] Rāvaṇa, she became as if lifeless." Matches note exactly. Faithful (2).

Now let's check verse 11.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_32_segmented.json
Found it exactly — Siromani's chunk under 5.32.11: "एतेनेदमेव मम जीवनमिति सूचितम् । कथां शृणोमीत्यस्य नाप्रसिद्धिः त्रिजटया कदाचिदागतविभीषणानुचरीभिश्च रामकथायाः कथ्यमानत्वात्" = "By this it is indicated: this alone is my life. [As for] 'I hear the tale' — this is not without basis (na aprasiddhiḥ), because the story of Rāma was told [to her] at times by Trijaṭā and by the attendants of Vibhīṣaṇa who occasionally came [to her]." Matches note precisely. Faithful (2).

Now let's get baselines for sarga 32.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
No baseline coverage for any of these 4 verses — confirms non-triviality for all. Let's finalize scores.

**5.32.4**: Faithful (2), non-trivial (2), contrastive_value: genuine two-commentator divergence (māyā-fear vs Rāma-longing) = **2**, register clean (2), anchoring: tilaka/siromani pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.32.6**: Faithful (2), non-trivial (2), contrastive_value: two commentators converge (not contrast) on the same point = 1 (per the sarga-25 precedent of scoring convergence as single-voice gain), register clean (2), anchoring: tilaka/siromani pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.32.8**: Faithful (2), non-trivial (2), contrastive_value: two commentators converge on same point = 1, register clean (2), anchoring: tilaka/siromani pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.32.11**: Faithful (2), non-trivial (2), contrastive_value: single commentator = 1, register clean (2), anchoring: siromani pratika `matches_verse: true` → 2. **Verdict: keep**.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_32_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_32_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_32_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_32_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_32_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 32 done: 4 keep. Now sarga 33.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_33_candidates.json
This is another rich one with 6 notes. Let me check the segmented bundle for verses 2, 11, 12, 15, 21, 23.

- 🔧 `Grep` — "verse_id": "5\.33\.(2|11|12|15|21|23)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_33_segmented.json
Confirmed for 5.33.2: Tilaka's chunk "अथ लिङ्गैः सीतेति निश्चये ऽपि तयैव साक्षद्वाचयितुमजानान इव पृच्छति-- का न्विति" = "Now, even though [he is] certain from external marks (liṅgaiḥ) that this is Sītā, he asks 'kā nu' (who indeed?) as if not knowing, in order to get her herself to say it aloud." Matches note exactly.

Now let's check verses 11, 12, 15, 21, 23.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_33_segmented.json
Now I see verse 11's Siromani chunk gives the vyañjana/lakṣaṇa gloss: "यानि व्यञ्जनानि बोधकानि ते लक्षणानि असाधारणचिह्नानि लक्षये" = "vyañjanāni = indicative signs; lakṣaṇāni = uncommon/extraordinary marks." This matches "widely-general sign vs rare/unusual sign" as claimed in the note. Let me check for the Tilaka/Bhushana further distinction (body-parts vs samudrika technical marks) mentioned in the note — let's search sarga 33 for "स्तनोरु" or similar or "सामुद्रिक" near verse 11-13 area, or check if this is elsewhere (note says "Тилака и Бхушана в дальнейшем разборе уточняют иначе").

- 🔧 `Grep` — सामुद्रिक|स्तनोरु|स्तन.*ऊरु|व्यञ्जन
Found it at line 791. Let me look at the context.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_33_segmented.json
Excellent, this is critical confirmation and it's exactly as the drafter's note describes. This Bhushana chunk is filed under an `ambiguous_marker: true` bundle labeled `5.33.1213` (a merged-range token), and it gives: "व्यञ्जनामि स्तनजघनादीनि" = "vyañjanāni [means] the breasts, hips, etc." and "लक्षणानि शुभावर्तरेखादिसामुद्रिकलक्षणानि" = "lakṣaṇāni [means] auspicious spiral-lines etc., the technical samudrika marks." This matches the note's claim about Bhushana precisely.

And Tilaka's chunk (filed under a separate `ambiguous_marker: true` bundle `5.33.1315`) says: "यतो व्यञ्जनानि राममहिषीत्वप्रकाशकानि ते सामुद्रिकालक्षणानि च लक्षये" — here Tilaka actually treats vyañjanāni and lakṣaṇāni somewhat together as "signs revealing her queenship" and "samudrika marks", which doesn't exactly show him drawing the sharp distinction the note claims ("Тилака и Бхушана в дальнейшем разборе уточняют иначе: вьянджана — это телесные черты (грудь, бёдра), а лакшана — формальные приметы саамудрики"). The note attributes this dual distinction to *both* Tilaka and Bhushana, but only Bhushana's chunk actually draws the vyañjana=body-parts vs lakṣaṇa=samudrika-marks distinction cleanly; Tilaka's chunk doesn't clearly separate the two terms this way — it uses both terms somewhat loosely together ("vyañjanāni ... te sāmudrikālakṣaṇāni ca lakṣaye" — reads more like he's treating them as a compound reference to the queenly signs generally, not explicitly splitting vyañjana from lakṣaṇa the way Bhushana does).

This is a moderate faithfulness concern: the note claims **both** Tilaka and Bhushana draw the same distinction ("Тилака и Бхушана в дальнейшем разборе уточняют иначе"), but only Bhushana's text supports this cleanly. This is a case of overstating which commentators hold a view — a form of overreach, though the substantive content (the vyañjana/lakṣaṇa distinction itself) is genuinely present and correctly attributed to Bhushana. I'll score this as **minor wording overreach = 1** for faithfulness (not full misattribution, but the note incorrectly co-attributes Tilaka to a distinction his text doesn't clearly draw), which caps the verdict at `edit` rather than `keep` (register/faithfulness overreach is fixable by narrowing the attribution to Bhushana alone, or by more carefully hedging).

Wait — per the rubric, faithfulness gate says "misstates/invents ⇒ 0 ⇒ reject" and "minor overreach in wording ⇒ 1". Let me reconsider: is this "minor overreach in wording" (→1, register-type fixable issue, doesn't force reject) or a "misattributed commentator" (→0, reject)? The core content (Bhushana's vyañjana=body-parts/lakṣaṇa=samudrika distinction) is genuinely and correctly sourced. The issue is that the note also claims Tilaka shares this same distinction, which is a stretch/overstatement rather than an invention — Tilaka's text does mention both terms in the same breath but doesn't clearly split them the way Bhushana does. This reads as "minor overreach in wording" (attributing a view to Tilaka that's a looser reading of his ambiguous phrasing) rather than a fabricated claim — I'll score faithfulness = 1.

- 🔧 `Bash` — echo "continuing to verify 5.33.12, 5.33.15, 5.33.21, 5.33.23"
Given faithfulness=1 (not 2), per the rubric's precedence rule "reject over flag_anchor over park over edit over keep" and the gate "faithfulness must be 2, else verdict `reject`" — this note's faithfulness gate fails, forcing verdict = **reject**, regardless of other scores. Let me finalize this note's full scoring and move to the others.

Non-triviality: genuinely new content beyond tier-1 (2). Contrastive_value: the note does present a real 3-way commentator engagement = 2 (though the exact framing is imprecise per above). Register: clean (2). Anchoring: Bhushana's decisive chunk sits in an `ambiguous_marker: true` merged-range bundle (`5.33.1213`), which per method-doc rules is flagged specifically because these "don't align to a single passage" and "almost all are rejected in Step 2" — but the drafter's `why_proposed`/note correctly ties it to verse 11 by content, similar to the sarga-27 precedent. However, combined with the Tilaka misattribution, I'll score anchoring conservatively at 1 (plausible, not verified) since it draws from two separate ambiguous-marker bundles, not a clean single-verse anchor.

Given faithfulness=1, verdict = **reject** takes top precedence.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_33_segmented.json
Confirmed for 5.33.15: Bhushana's chunk: "शत्रुसैन्यप्रतापिनः शत्रुषु जीवत्सु न मे श्वशुरो जीवितवान् । स चेदिदानीं वर्तेत कथमहमेतादृशीमवस्थां प्राप्नुयामिति भावः" = "'śatrusainyapratāpinaḥ' — my father-in-law did not [merely] live while enemies lived [i.e., he defeated them]; if he were alive now, how could I have come to such a state? — this is the sense." This exactly matches the note's ironic reading. Faithful (2).

Now let's check 5.33.21 and 5.33.23.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_33_segmented.json
Confirmed for 5.33.21: Tilaka's chunk "तद्देवासुरे युद्धे वरदानरूपम्" = "that [boon], in the form of a boon [given] in the war of gods and asuras" — this confirms the devāsura-war backstory. However, the note claims Tilaka explains "Kaikeyi got two boons for saving Dasharatha's life" — let's check: this exact detail (saving his life, two boons) isn't fully spelled out in this fragment ("तद्देवासुरे युद्धे वरदानरूपम्" is brief — just "this in the form of a boon at the war of gods and asuras"). The bundle text is truncated/terse here; the note's elaboration (saving his life, receiving two boons) is a reasonable gloss of the well-known Rāmāyaṇa episode (Kaikeyī saving Daśaratha in the devāsura war and being granted two boons) which Tilaka's brief note references by allusion. This is a widely known epic backstory that the terse commentary gestures at rather than fully narrates — the note's elaboration goes a bit beyond the literal text shown but represents the standard, uncontested content of that allusion (not an invention). I'll treat this as acceptable synthesis of a well-known referent rather than overreach, since it's not a contested or invented detail — faithful (2).

Now let's check 5.33.23: Note claims Siromani reads "rājyam ayācata" as "requested [the eldest son] to accept the forest-kingdom" (vana-rājyam) rather than "begged for the kingdom [for someone else]" — meaning the sole addressee is Rama himself. Bundle Siromani: "ततस्तस्मात् हेतोः रुदन् राजा ज्येष्ठं पुत्रं राज्यं वनराज्यमयाचत" = "Therefore, for that reason, weeping, the king begged the eldest son [for] the kingdom — [i.e.] the forest-kingdom (vana-rājyam)." Matches note precisely. Faithful (2).

- 🔧 `Bash` — echo "getting baselines for sarga 33"
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s33_leonov.json
This confirms the exact tier-1 baseline text the drafter cited ("Средневековые комментаторы расходятся в интерпретации смысловой разницы... не поясняя, в чём именно" = "medieval commentators disagree on the semantic difference... without explaining what exactly" — matches note's framing precisely) and for 5.33.23 the note's claim that Kostina flags "у старшего сына" ("[comment on] whose eldest son" open question) is confirmed verbatim.

No baselines for verses 2, 12, 15, 21. Now let me finalize all 6 scores for sarga 33.

**5.33.2**: Faithful (2), non-trivial (2, no baseline), contrastive_value: single commentator = 1, register clean (2), anchoring: tilaka pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.33.11**: Faithful = 1 (Bhushana's distinction confirmed cleanly; Tilaka's co-attribution to the same distinction is an overreach given his terser, less clearly split phrasing) → gate fails → **Verdict: reject**. Non-triviality (2), contrastive_value (2), register (2), anchoring (1, drawn from ambiguous-marker merged-range bundles).

**5.33.12**: Faithful (2, both claims confirmed — Tilaka's sleepless/desensitized-guard reasoning and fear-from-Trijata's-dream and resignation-to-no-escape, Bhushana's "some had fallen asleep" addition), non-trivial (2, no baseline), contrastive_value: single-source narrative gap-filling, though two commentators contribute complementary details (Tilaka gives 3 reasons, Bhushana adds a 4th) — this counts as more than "ornament," genuine gain = 1, register clean (2), anchoring: tilaka pratika `matches_verse: true`; bhusana `matches_verse: false, content_anchor: true` → 2. **Verdict: keep**.

**5.33.15**: Faithful (2), non-trivial (2, no baseline), contrastive_value: single commentator = 1, register clean (2), anchoring: bhusana pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.33.21**: Faithful (2, reasonable elaboration of a well-known referent), non-trivial (2, no baseline; Phase-1's varadāna note — need to check content, but confirmed empty phase1 list for this verse so no conflict), contrastive_value: single commentator, mythic backstory = 1, register clean (2), anchoring: tilaka pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.33.23**: Faithful (2), non-trivial (2, directly answers Kostina's open question), contrastive_value: single commentator, resolves a translation-choice = arguably could be scored 2 ("translation-choice resolved") since it directly resolves what "царство" (whose kingdom, given to whom) refers to — I'll score this 2 given it resolves an actual open interpretive question left by Kostina. Register clean (2). Anchoring: siromani pratika `matches_verse: true` → 2. **Verdict: keep**.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_33_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_33_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_33_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_33_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_33_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_33_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_33_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 33 done: 5 keep, 1 reject. Now let's move to the remaining sargas: 38, 40, 41, 42, 43, 44, 45. Let me batch-read the candidates files for these.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_38_candidates.json
Let's check the segmented bundle for verses 36, 37, 65, 68 in sarga 38.

- 🔧 `Grep` — "verse_id": "5\.38\.(36|37|65|68)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_38_segmented.json
Confirmed for 5.38.36 — Siromani's chunk verbatim: "दशरथाय नमस्कत्वेत्यनेन पलायनसमये दशरथोपदेशादेव रामशरणमागत इति ध्वनितम्" = "By [the crow's] bowing to Daśaratha, it is suggested that at the time of fleeing [the crow] came to Rāma's refuge precisely because of Daśaratha's advice [given to it in heaven]." Matches note precisely. Faithful (2).

Confirmed for 5.38.37 — Tilaka's chunk: "कस्माद्राक्षसक्षयं न करोतीत्यस्योत्तरम्-- त्वच्छोकेति । त्वद्वियोगजशोकेन सर्वकार्यविमुख इत्यर्थः" = "The answer to 'why does he not destroy the rakshasas': [the word] tvacchoka — [meaning] due to grief born of separation from you, he is averse to all [other] activity." Matches note precisely. This is Tilaka's answer to "why doesn't Rama destroy Ravana" and confirms both claims (not weakness, but grief-induced aversion to action). Faithful (2). Now let's check 65 and 68.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_38_segmented.json
Excellent — I found the exact chunk. It's under 5.38.68 bundle, Tilaka's text: "गिरिवरपवनावधूतमुक्तः ... प्रभावात्सामर्थ्यविशेषात् । राक्षसीभिर्यथा न ज्ञायते तथा धृतम्" = "prabhāvāt = through [its] special power; it was held/kept such that the rakshasis would not notice [it]" — this confirms the note's claim exactly. This is filed under 5.38.68's Tilaka chunk (note's `verse_id` matches this correctly), and the drafter's own rejected-entry cross-reference for 5.38.66/5.38.70 explicitly acknowledges the split of Tilaka's material across verses (which is transparent, similar to sarga 27's pattern). Faithful (2).

Also for 5.38.65 — confirmed: Siromani reads Kauśikī as "kauśika-gotra-pṛthvī" (earth of Kauśika lineage, rescued by Varāha), and Bhushana reads it as Indra's royal Śrī (fortune), abducted to Pātāla after Vṛtra's slaying and restored by Nārāyaṇa, with an alternate Mahābhārata-based story about Utathya's wife also cited. This matches the note's claims about both commentators precisely, and the note correctly notes neither matches the lexical note's Kuśika-daughter/Viśvāmitra identification.

Now let's get baselines for sarga 38.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s38_leonov.json
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s38_phase1.json
Now I have all baselines confirmed. This confirms Kostina's 5.38.66 open question (matching note 5.38.68's `complements_leonov`), and the Phase-1 lexical note that mistakenly reads "Kauśikī" as Viśvāmitra's mother (per the note's `Kauśikī = "son of Kuśika"` misapplied — actually Viśvāmitra himself is called "Kauśika," so this Phase-1 note conflates the simile subject) — importantly, the drafted note explicitly states neither Siromani nor Bhushana's identification matches this lexical note's Viśvāmitra attribution, which is confirmed correct by my reading of the bundle. Also Phase-1's 5.38.37 note is just about "brahmastra" as a term — genuinely distinct from Tilaka's psychological point about tvacchoka.

Now let's finalize scores for all 4 sarga 38 notes.

**5.38.36**: Faithful (2), non-trivial (2, no tier-1 note on this verse, Phase-1 none either), contrastive_value: single commentator = 1, register clean (2), anchoring: siromani pratika `matches_verse: false, content_anchor: true` → 2 (verified via content anchor). **Verdict: keep**.

**5.38.37**: Faithful (2), non-trivial (2, distinct from Phase-1's brahmastra-term note), contrastive_value: single commentator = 1, register clean (2), anchoring: tilaka pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.38.65**: Faithful (2), non-trivial (2, distinct from Phase-1's Viśvāmitra/pātāla note — actually contradicts it, which the note correctly flags), contrastive_value: genuine two-commentator divergence = **2**, register clean (2, though it's a longer note bundling two full myths — checking length: "Кто такая Каушики..." this is 2 sentences, acceptable), anchoring: siromani/bhusana pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.38.68**: Faithful (2), non-trivial (2, directly answers Kostina's open question), contrastive_value: single commentator, resolves an actual open question (vastragata mystery) = could argue 2 ("translation-choice resolved") — I'll score 1 since it's answering a factual "why hidden" question rather than a translation ambiguity per se, staying conservative. Register clean (2). Anchoring: tilaka pratika `matches_verse: true` → 2. **Verdict: keep**.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_38_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_38_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_38_candidates.json
Let me re-read the current file state to get exact text.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && g
I see — there's a typo in the original text: "Вишвамitre" (mixed Cyrillic/Latin), not "Вишвамитре". Let me use the correct string.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_38_candidates.json
I noticed there's also a minor typo in `note_ru` itself: "не выбирая version" (mixing English word). This is a register issue in the drafter's original text (a stray English word in Russian prose), separate from my earlier finding. Let me flag this too. Now let me add the judge objects for both notes.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_38_candidates.json
I'm revising the verdict for 5.38.65 from `keep` to `edit` due to the register defects (mixed-script typos) found in both `note_ru` and `complements_leonov`. Now let's finish 5.38.68.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_38_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_38_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 38 done: 3 keep, 1 edit. Now sarga 40.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_40_candidates.json
Let's check verses 5, 7, 23 in sarga 40's segmented bundle.

- 🔧 `Grep` — "verse_id": "5\.40\.(5|7|23)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_40_segmented.json
Confirmed for 5.40.5. Siromani reads "gaṇḍapārśve gaṇḍaikadeśe" = "on part of the cheek", matching the literal reading. Let me check for the Bhushana "gaṇḍasthale/gaṇḍaśailapārśve" forehead reading — the note says "по свидетельству того же комментаторского пласта на соседних стихах" (based on evidence from the same commentarial layer on neighboring verses). This is a hedge in the note itself — it doesn't claim a direct Bhushana quote at v.5, but rather infers this from context. Let me check whether this reading appears anywhere nearby.

- 🔧 `Grep` — gaNDasthale|gandasthale|गण्डस्थल|गण्डशैल
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_40_segmented.json
Found it, at bundle `5.40.46` (verse-marker "46", but the drafter's own rejected entry for this bundle says: "содержание (gaṇḍapārśve = gaṇḍasthale/gaṇḍaśailapārśve) уже приведено в примечании Леонова/Костиной к V.40.5" — meaning this is the bundle labeled `5.40.46` filed with `ambiguous_marker: false` but the drafter treats it as belonging to v.5's Bhushana material. The text: "गण्डपार्श्वे गण्डस्थले गण्डशैलपार्श्वे वा" = "gaṇḍapārśve [means] gaṇḍasthale, or gaṇḍaśailapārśve" — matches note's claim precisely (Bhushana reads gaṇḍapārśve as gaṇḍasthale/gaṇḍaśailapārśve — "forehead area," per the drafter's gloss, though literally gaṇḍa can mean cheek OR temple/forehead-region depending on context; the drafter is following Kostina's own tier-1 note which apparently already glosses this as "on the forehead").

Let me verify against Kostina's own tier-1 note for 5.40.5 to see if it confirms this Bhushana reading.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s40_leonov.json
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s40_phase1.json
This confirms Kostina's own tier-1 note precisely quotes Bhushana's exact reading "gaṇḍasthale gaṇḍaśailapārśve vā" and attributes the Goldman "forehead" translation to following Bhushana — matching the note's claim exactly. So the drafted note is faithful and correctly complements Leonov/Kostina's note (adds the Siromani literal-cheek contrast, which the tier-1 note doesn't mention). Faithful (2).

Now let's verify 5.40.7 and 5.40.23.

**5.40.7**: Note claims Tilaka reads cūḍāmaṇi as apotropaic ("etatsannidhāne rakṣobhibhavāsaṃbhavāt" — in its presence, rakshasas cannot overpower [her]); Bhushana/Siromani read it as a keepsake reminding her of Rama/gift from father. Bundle Tilaka: "एतत्संनिधाने रक्षोभिभवासंभवादिति भावः" = "in its presence, the impossibility of being overpowered by rakshasas — this is the sense." Matches exactly. Bundle Bhushana: "अस्य चूडामणेस्त्वया बहुशो लालितत्वेन त्वत्स्मारकत्वादिति भावः" = "since this jewel was much cherished by you, it serves as a reminder of you — this is the sense." Bundle Siromani: "एषः पित्रा दत्तः चूडामणिः" = "this jewel, given by [her] father." Matches note's claims for all three commentators precisely. Faithful (2).

Now let's check 5.40.23.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_40_segmented.json
Confirmed for 5.40.23: Tilaka's chunk: "समाधानं संविधानम्, "अथापि स महाबाहुः" इति पाठे यथेत्यपि पूरणीयमेव । यद्यपि श्रुतवृत्तान्तः स्वयमेव यतिष्यति तथापि त्वमपि यथा मां शीघ्रं तारयसि तथा संविधानं कुर्वित्यर्थः" = "'samādhāna' [means] 'arrangement' (saṃvidhāna); [there is] a variant reading 'athāpi sa mahābāhuḥ' [instead of 'yathā ca sa mahābāhuḥ']... although, having heard the news, he [Rāma] will himself strive, still you too should make the arrangement so that you quickly rescue me." Then continues: "तत्कार्यं लङ्कागमनप्रयोजनमल्पशेषम् । देवीदर्शनरूपस्य महतः प्रधानकृत्यस्य निष्पन्नत्वात्परबलदर्शनरूपस्यानुषङ्गिकत्वादल्पशेषत्वम्" = "that task, the purpose of coming to Laṅkā, has little remaining — since the great main task (seeing the queen) is accomplished, the [remaining task of] observing enemy strength is secondary, hence little remains." This matches the note's claims precisely (main task already done, secondary task remains, variant reading noted). Faithful (2).

Now let's finalize scores for all 3 sarga 40 notes.

**5.40.5**: Faithful (2), non-trivial (2, this adds the Siromani literal-cheek contrast, distinct from tier-1's Bhushana-only coverage), contrastive_value: genuine two-way divergence between Siromani (cheek) and Bhushana (forehead), with the note noting Leonov's translation actually follows Siromani = **2**, register clean (2), anchoring: siromani/bhusana pratika `matches_verse: true` (for v.5 itself); the additional Bhushana forehead-gloss detail sits in bundle `5.40.46` — checking its `ambiguous_marker` field: false (not flagged ambiguous), so it's a normally-anchored bundle, just filed under an odd verse-token "46" — I'll treat this as anchoring=1 given the odd verse-number labeling of that bundle (potential residual segmentation quirk), though tier-1's own note independently confirms the exact same Bhushana quote, giving strong non-mechanical corroboration. Given the strong corroboration from tier-1, I'll score anchoring=2 (effectively verified by the independent tier-1 citation matching verbatim).

**5.40.7**: Faithful (2), non-trivial (2), contrastive_value: three-way divergence (apotropaic vs keepsake vs father's-gift) = **2**, register clean (2), anchoring: tilaka/bhusana/siromani pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.40.23**: Faithful (2), non-trivial (2), contrastive_value: single commentator (variant reading + interpretive point) = 1, register clean (2), anchoring: tilaka pratika `matches_verse: true` → 2. **Verdict: keep**.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_40_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_40_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_40_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_40_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 40 done: 3 keep. Now sarga 41.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_41_candidates.json
Let's check the segmented bundle for verses 2, 3, 34, 9, 20.

- 🔧 `Grep` — "verse_id": "5\.41\.(2|3|34|9|20)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_41_segmented.json
Confirmed for 5.41.2: Bhushana's chunk matches note exactly ("इदं कार्यं रावणनिलयपरिज्ञानरूपम् ... राक्षसबलाबलरावणहृदयाद्यपरिज्ञानात्कार्यस्याल्पशेषत्वोक्तिः" = "'this task' [means] the task of reconnoitering Rāvaṇa's abode; ... it is called 'little remaining' due to non-knowledge of the strength/weakness of the rakshasas and Rāvaṇa's mind"). Faithful (2).

For 5.41.3 — the note claims the doctrinal maxim material is filed under bundle `5.41.34`, not directly in `5.41.3`'s own bundle. Let's verify bundle `5.41.34`.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_41_segmented.json
Confirmed precisely: the bundle labeled `5.41.34` (verse token "34" — likely a scrambled marker, since sarga 41 has 25 verses per the `_meta`) has, with `ambiguous_marker: false`, this Bhushana text: "अनित्यो विजयो यस्माद्दृश्यते युद्ध्यमानयोः । पराजयश्च संग्रामे तस्माद्युद्धं विसर्जयेत्" = "since victory is seen to be uncertain for those fighting, and defeat too [is possible] in battle, therefore one should avoid war" — the exact nīti-maxim the note describes, followed by "सर्वं बलवतः पथ्यम्" ("everything is wholesome for the strong" — a known nīti aphorism) and the explanation that Hanuman's incomparable strength excludes any possibility of his defeat, hence "parākrama" (might/violence) is what appeals to him. This matches the note precisely, and the note transparently explains the segmentation quirk (bundle mislabeled "34" but content-wise belongs to v.3, opening with pratīka of v.3's material — "na sāma" — before the maxim). Faithful (2).

Now let's check verses 9 and 20.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_41_segmented.json
Confirmed for 5.41.9 exactly: Tilaka's chunk explicitly states the correct reading is "sabalaṃ sayāyinam" and calls "sabalaṃ prayāyinam" an "ādhunika-kalpita" (recently invented/modern-fabricated) reading — matching the note precisely. And Bhushana's chunk in this same bundle indeed reads "सबलप्रयायिनम्" (sabala-prayāyinam) — exactly the rejected variant Tilaka names, confirming the note's observation that Bhushana's text here carries the very reading Tilaka dismisses. Faithful (2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_41_segmented.json
Confirmed for 5.41.20: Tilaka's chunk: "कपेर्बलाच्छोच्यत इति शोका शोच्यलताप्रताना जाता" = "by the monkey's power [the garden] became 'śokā' — one that is to-be-grieved-over (śocya), a spread of grief-lianas." This matches the note's pun claim (aśoka [griefless] → śoka [grief], since the "a-" is playfully dropped through the wordplay with kapi-bala). Faithful (2).

Now let's get baselines for sarga 41.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s41_leonov.json
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s41_phase1.json
These confirm both my expectations: tier-1 5.41.2 only glosses the "fourth means = daṇḍa" identity; Phase-1 5.41.2 covers the general upāya doctrine, distinct from the drafted note's specific point about which task is unfinished. Tier-1 5.41.20 confirms the pramadāvana wordplay is already covered (matching drafter's own note that its wordplay is different from the aśoka/śoka one). Phase-1 5.41.9 covers "mantrivarga" term, distinct from Tilaka's variant-reading dispute. No baseline for verse 3/34 or 9's specific reading dispute.

Now let's finalize scores for all 4 sarga 41 notes.

**5.41.2**: Faithful (2), non-trivial (2, distinct from tier-1's daṇḍa-identity note and Phase-1's general upāya-doctrine note), contrastive_value: single commentator = 1, register clean (2), anchoring: bhusana pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.41.34** (printed as note for verse 3): Faithful (2), non-trivial (2, no baseline covers this maxim), contrastive_value: single commentator = 1, register clean (2), anchoring: this bundle carries `ambiguous_marker: false` but an odd verse-token "34" that doesn't correspond to any real verse in a 25-verse sarga — this is analogous to the sarga-27/41 "internal-marker-corrected" pattern, and the note transparently explains why it's printed against V.41.3. I'll score anchoring = 1 (plausible, well-argued, but the bundle's own verse-token is anomalous/unverified against a real verse number, and bhusana's `pratika_check` isn't shown for this specific chunk in a way that maps to v.3 directly — though the opening of the chunk explicitly starts "उपपत्तिपूर्वकमेतदेव विवृणोति न सामेति" referencing "na sāma" = the literal start of verse 3's text, which is a clear textual link). Given the explicit textual anchor to "na sāma" (verse 3's own first words), I'll raise this to anchoring = 2 — it's directly self-referential to v.3's text opening.

**5.41.9**: Faithful (2), non-trivial (2, no baseline covers this reading dispute), contrastive_value: this is framed as `contrastive: true` in the drafter's metadata — checking: it's not two commentators disagreeing on interpretation, but Tilaka critiquing a reading that Bhushana's own text happens to carry — this is a genuine contrastive tension (one voice condemns what another voice's text preserves) — I'll score contrastive_value = 2 (a real textological contrast, meeting the "translation choice resolved" spirit since it identifies which reading is authentic). Register clean (2). Anchoring: tilaka/bhusana/siromani pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.41.20**: Faithful (2), non-trivial (2, distinct from tier-1's pramadāvana wordplay note — a different pun), contrastive_value: single commentator = 1, register clean (2), anchoring: tilaka pratika `matches_verse: true` → 2. **Verdict: keep**.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_41_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_41_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_41_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_41_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_41_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 41 done: 4 keep. Now sarga 42.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_42_candidates.json
Note that the drafter's own reasoning for 5.42.10 flags this bundle as `ambiguous_marker=true` merged-range (`5.42.810`) "without anchoring verification" — this is a red flag the drafter itself acknowledges. Let's check the segmented bundle.

- 🔧 `Grep` — "verse_id": "5\.42\.(10|20|44|810)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_42_segmented.json
This bundle (`5.42.10`, `ambiguous_marker: false`) does not contain the pañcānṛtāni doctrine — its Bhushana/Siromani text is entirely different content (Siromani here is actually about "who are you" — Hanuman's dāsa reply, which seems misplaced/shifted, and Bhushana just repeats the verse). Let's check the `5.42.810` merged-range bundle where the drafter says the actual pañcānṛtāni doctrine sits.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_42_segmented.json
Confirmed — this exact quote of the pañcānṛtāni verse is indeed under the ambiguous-marker merged-range bundle `5.42.810` (verses 8-10). The Bhushana text: "नैनं जानामीति । "विवाहकाले रतिसंप्रयोगे प्राणात्यये सर्वधनापहारे । (विप्रस्य) मित्रस्य चार्थेप्यनृतं वदेयुः पञ्चानृतान्याहुरपातकानि ।।" इति स्मरणादसत्योक्तिः" = "'nainaṃ jānāmi' [i.e., her lie] — recalling the smṛti verse: 'At the time of marriage, in sexual union, when life is in danger, in [preventing] total loss of wealth, and for the sake of a friend/brahmin — one may speak falsehood; these five untruths are declared non-sinful' — hence [her] false statement [is justified]."

This precisely confirms the note's claim, quoting the exact pañcānṛtāni verse, which matches "brahmin's marriage, sexual union, danger to life, total property loss, for a friend's sake" — matching the note's five cases (marriage, love-intimacy, life-threat, total property loss, for a friend). Faithful (2) — content is genuinely correct and the drafter's `why_proposed` transparently discloses the anchoring caveat itself.

However, given this content sits in an `ambiguous_marker: true` bundle spanning verses 8-10 with **no independent verse_id and no pratika_check at all** (note the bundle has no `pratika_check` field shown), this is a genuinely weaker anchoring case than the sarga-27/41 precedents (which at least had non-ambiguous bundles with an internal self-declared verse marker). Here there's no pratika verification mechanism applied at all to this chunk, and the method doc's own §11 says merged-range markers "don't align to a single passage" and are "almost all rejected in Step 2." The note's own `why_proposed` explicitly concedes: "бандл сегментирован под слитой меткой... (без проверки анкоринга)" — no anchoring check was performed.

Given this, I'll score anchoring = 1 (plausible — the content clearly discusses Sita's "nainaṃ jānāmi" reply from V.42.10 by direct textual reference — but genuinely unverified, sitting in a merged-range ambiguous bundle with no pratika_check at all).

- 🔧 `Bash` — echo "continuing sarga 42 verses 20 and 44"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_42_segmented.json
Confirmed for 5.42.20: Tilaka's chunk "सीता संभाषितेत्यनेन सापराधग्रहत्वं बोधितम्" = "By this [phrase] 'sītā sambhāṣitā', her own culpability is indicated." Matches note precisely. Faithful (2), anchoring verified (2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_42_segmented.json
Confirmed for 5.42.44: Tilaka's chunk "प्रहस्तपुत्रो जम्बुमाली" = "Prahasta's son [is] Jambumālī." Matches note exactly. However, I note `pratika_check` for tilaka here shows `matches_verse: false, content_containment: 0.0` — no content_anchor flag either (unlike Siromani's, which has `content_anchor: true`). This is genuinely unverified by both signals (pratīka mismatch AND zero content containment). The note's own `why_proposed` explicitly and transparently discloses this: "автоматическая проверка анкоринга не подтвердила эту короткую глоссу (нулевое пересечение с текстом стиха, как и ожидаемо для однословного пояснения имени)" — correctly explaining that a single-word name-gloss naturally produces zero token overlap with the verse (an expected false-negative of the automated method for short glosses, not a sign of misplacement). This is a legitimate limitation of the mechanical check for terse name-glosses, and the content itself (Tilaka naming Jambumālī as Prahasta's son) is unambiguous and directly tied to the phrase "prahastaputram" appearing in the verse itself.

Given the mechanical signal is uninformative here (expected zero-overlap due to gloss brevity) rather than contradictory, and there's no `suggest_verse` pointing elsewhere, I'll score anchoring = 1 (plausible but not machine-verified) rather than 0 (contradicted) — this doesn't meet the "contradicted" bar for `flag_anchor` since nothing suggests the content belongs to a different verse; it's simply too short to register on the containment metric.

- 🔧 `Bash` — echo "getting baselines for sarga 42"
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s42_leonov.json
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s42_phase1.json
This confirms Phase-1 already has a note on 5.42.44 about "prahastaputra" — but importantly, that Phase-1 note discusses the term's etymology and military-hierarchy significance while explicitly NOT naming the son (it treats "prahastaputra" as an unnamed compound throughout). This confirms the note's non-triviality claim precisely: Phase-1 doesn't name Jambumālī, and the drafter's own reject-reason for other verses references this Phase-1 note by name confirming they checked it. Also confirms Phase-1's 5.42.20 note is about the general daṇḍa political-theory concept, not the specific "sītā sambhāṣitā = her culpability" reading — genuinely distinct.

Now let's finalize scores for all 3 sarga 42 notes.

**5.42.10** (printed for V.42.10, content from ambiguous-marker bundle 5.42.810): Faithful (2, exact verbatim confirmation of the pañcānṛtāni śloka). Non-triviality (2, distinct from both tier-1's snake-proverb note and Phase-1's lexical snake-proverb note — this is about the pañcānṛtāni doctrine, not the ahi-proverb). Contrastive_value: single commentator = 1. Register clean (2). Anchoring: 1 (plausible per direct textual reference to "nainaṃ jānāmi", but genuinely unverified — no pratika_check present at all for this ambiguous-marker chunk). **Verdict: keep** (anchoring=1 doesn't block keep; only 0 triggers flag_anchor, and non_triviality≥1 and contrastive_value≥1 with faithfulness=2 keep all gates passing).

**5.42.20**: Faithful (2), non-trivial (2, distinct from Phase-1's daṇḍa political-theory note), contrastive_value: single commentator = 1, register clean (2), anchoring: tilaka pratika `matches_verse: true` → 2. **Verdict: keep**.

**5.42.44**: Faithful (2), non-trivial (2, distinct from Phase-1's etymology-only note, which explicitly doesn't name the son), contrastive_value: single commentator, realia/name = 1, register clean (2), anchoring: 1 (tilaka pratika `matches_verse: false, content_containment: 0.0`, no content_anchor flag, but this is an expected false-negative for a terse single-word name gloss, correctly explained by the drafter; not contradicted by a `suggest_verse` pointing elsewhere). **Verdict: keep**.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_42_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_42_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_42_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_42_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 42 done: 3 keep. Now sarga 43.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_43_candidates.json
Note: the notes' claimed content actually sits in the "5.43.34" bundle per the rejected entry (which cross-references it). Let's check the segmented bundle.

- 🔧 `Grep` — "verse_id": "5\.43\.(1|4|34)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_43_segmented.json
Confirmed for 5.43.1: Tilaka's own chunk in this very bundle already says "चैत्यप्रासादो रक्षःकुलदेवताप्रासादः" (= "caitya-prāsāda is the temple-palace of the rakshasas' family deity") and Siromani's: "चैत्यप्रासादः राक्षसकुलदेवताधिष्ठानीभूतप्रासादविशेषः" (= "a special palace serving as the abode of the rakshasas' family deity"). But the note attributes this to Bhushana specifically ("по Бхушане... caityaṃ devāyatanam, tadrūpaḥ prāsādaḥ"). Let me check where the "5.43.34" bundle's Bhushana text actually gives this — since I need to see if Bhushana himself (not Tilaka/Siromani) makes this specific claim with that exact phrasing.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_43_segmented.json
Found it precisely — the bundle labeled `5.43.34` (verse-token "34", `ambiguous_marker: false`) contains Bhushana's exact text: "चैत्यं देवायतनम्, तद्रूपः प्रासादः चैत्यप्रसादः तम्" = "caitya = devāyatana (abode of a deity); a palace in that form is a caitya-prāsāda." This matches the note's claim exactly, including the specific phrasing "caityaṃ devāyatanam, tadrūpaḥ prāsādaḥ" quoted almost verbatim. AND this same bundle continues: "प्रतिसूर्यः द्वितीयसूर्य इत्यर्थः । अनेन सूर्योदयस्सूचितः" = "pratisūrya means 'a second sun'; by this, sunrise is indicated (sūryodayaḥ sūcitaḥ)" — which matches note #2 (5.43.4) exactly as well. Both notes' content is fully confirmed here — faithful (2) for both.

Now let's check baselines.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s43_leonov.json
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s43_phase1.json
This confirms Kostina's own tier-1 note explicitly requests "Комм о 'форме' дворца, поскольку ниже будет в комм про это говориться" ("comment on the 'form' of the palace, since below there will be commentary on this") — matching the note's `complements_leonov` claim precisely, and confirming she was aware there was more commentary further down that she hadn't yet incorporated. And Phase-1's 5.43.4 note is purely about the optical/parhelion nature of the term, distinct from the note's sunrise-timing claim.

Now let's finalize scores.

**5.43.1**: Faithful (2), non-trivial (2, directly fills the gap Kostina explicitly flagged), contrastive_value: single commentator = 1, register clean (2), anchoring: this content sits in bundle `5.43.34` with `ambiguous_marker: false` — no `pratika_check` shown for this bundle at all (I should verify). Let me check.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Confirmed — no `pratika_check` field exists for the `5.43.34` bundle at all. This is analogous to the `5.42.810` case (ambiguous-marker bundle with no verification mechanism applied), but here `ambiguous_marker` is explicitly `false` (not flagged as a merged-range token) — meaning the segmenter treated verse-token "34" (an anomalous number for a sarga that only reaches 33 verses per `_meta.verse_count`... let me check) as if it were a normal, distinct verse, without running the pratika check.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Confirmed: sarga 43 has 33 verses total, so "verse 34" is an out-of-range orphan marker — exactly like sarga 27/28's `.68`/`.34` orphan cases seen earlier, which the drafter's own rejected-entries elsewhere correctly identify as "нежизнеспособный сегмент" (non-viable segment / orphan verse number). Given this bundle's verse-token is literally out of range, and no pratika_check exists, but the content is directly self-referential (opens with "ध्वंसनप्रकारमाह चैत्येति" — "explaining the manner of destruction, beginning with 'caitya'..." — directly picking up the word "caityaprāsādaḥ" from verse 1's text, and continuing to explicitly gloss "hariśreṣṭho hanumān mārutātmaja" and "pratisūryaḥ" which are verse 3/4's exact words) — this is clearly Bhushana's continuous commentary flowing across verses 1, 3, 4, artificially split by the segmenter's marker detection into an orphan "verse 34" bundle. The content is unambiguous by direct textual reference to the exact words of verses 1 and 4.

I'll score anchoring = 1 for both notes (plausible, strongly self-referential by exact word-matching, but mechanically unverified — no pratika_check ran, and the bundle is an out-of-range orphan marker).

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_43_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_43_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_43_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 43 done: 2 keep. Now sarga 44.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_44_candidates.json
The note for verse 17 itself confesses the pratika is unverified and sits in a merged-range bundle `5.44.1720`. Let's check the segmented bundle for verses 6 and 17/1720.

- 🔧 `Grep` — "verse_id": "5\.44\.(6|17|1720)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_44_segmented.json
Confirmed for 5.44.6: Tilaka's/Siromani's/Bhushana's chunks all match precisely: "तोरणविटङ्कस्तोरणस्तम्भयोरुपरितिर्यक्प्रतिष्ठापितकपोतपालिकादारु" = "toraṇaviṭaṅka is the wooden pigeon-perch (kapotapālikā) placed crosswise above the two gate-pillars." Matches note exactly, including the specific "kapotapālikā" term. Note says "по Тилаке и Бхушане (со ссылкой на «Амару»)" — let me check the "Amara" citation: Bhushana's chunk quotes "कपोतपालिकायां तु विटङ्कं पुन्नपुंसकम्" इत्यमरः — this is a quote from **Amarakośa** (the lexicon), attributed with "इत्यमरः" ("thus says Amara"), not "Amaru" (a different poet). The note's phrase "«Амару»" likely refers to Amarakośa (often abbreviated "Amara") — this is a minor naming ambiguity but likely refers correctly to the Amarakośa lexicon citation, which is indeed present. I'll treat this as acceptable shorthand, not a factual error. Faithful (2).

Now let's check 5.44.17's own bundle and the merged-range bundle `5.44.1720`.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_44_segmented.json
This bundle (`5.44.17`, `ambiguous_marker: false`) doesn't have Tilaka's chunk about "aśva = khara" at all. Let's check the merged-range bundle `5.44.1720`.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_44_segmented.json
Confirmed precisely — this is `ambiguous_marker: true` (a merged-range token, per the drafter's own transparent disclosure). Tilaka's text: "नाश्वा रथेन खरयुक्तेनेत्युक्तेरश्वशब्देनात्र स्वरा उच्यन्ते" (likely a scan/typo for "खरा उच्यन्ते" given Bhushana's parallel phrasing below) = "'na aśvāḥ' — since it was earlier said the chariot was yoked with donkeys (khara), the word 'aśva' here refers to donkeys (khara)." Bhushana's text confirms even more explicitly: "नाश्वा इति अश्वशब्देनात्र खरा उच्यन्ते । "रथेन खरयुक्तेन" इति पूर्वमुक्तत्वात्" = "'na aśvāḥ' — here the word 'aśva' refers to donkeys (khara), because it was earlier stated 'the chariot was yoked with donkeys'." This matches the note's claim precisely, with the "V.44.5" backward-reference confirmed by "रथेन खरयुक्तेन इति पूर्वमुक्तत्वात्" ("since it was earlier said..."). Faithful (2) — content is genuinely and precisely confirmed, even though this specific chunk is in an `ambiguous_marker: true` bundle with no `pratika_check`.

Given the merged-range/ambiguous_marker=true status here (a stronger red flag than sarga 43's out-of-range-but-not-ambiguous case), and no pratika_check exists, I'll score anchoring = 1 (plausible, well-supported by direct wording match to "nāśvāḥ" and the internal "earlier stated" cross-reference, but genuinely unverified and sitting in an explicitly flagged ambiguous merged-range bundle).

Let's check baselines for sarga 44.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
No baselines for verses 5, 6, or 17. Both notes non-trivial (2).

**5.44.6**: Faithful (2), non-trivial (2, no baseline), contrastive_value: two commentators converge = 1, register clean (2), anchoring: bhusana/siromani pratika `matches_verse: true` → 2 (tilaka's own chunk mismatches but bhusana/siromani both confirm cleanly, and this is verse 6 itself, a normal non-ambiguous bundle). **Verdict: keep**.

**5.44.17**: Faithful (2), non-trivial (2, no baseline; resolves an apparent contradiction between v.5's donkey-chariot and v.17's "no horses"), contrastive_value: single commentator = 1, register clean (2), anchoring: 1 (ambiguous_marker=true bundle, no pratika_check, but content directly matches "nāśvāḥ" and explicitly cross-references the earlier donkey detail). **Verdict: keep**.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_44_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_44_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_44_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 44 done: 2 keep. Now the final sarga: 45.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_45_candidates.json
Only one note. Let's check the segmented bundle for verse 2.

- 🔧 `Grep` — "verse_id": "5\.45\.2"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_45_segmented.json
Confirmed precisely: Tilaka's chunk "परस्परजयैषिणो ऽहमहमिकया स्वस्वोत्कर्षापेक्षिणः" = "parasparajayaiṣiṇaḥ — desiring their own individual superiority through mutual rivalry (ahamahamikā, 'I-first-ness')." Bhushana's chunk: "परस्परजयैषिणः प्रत्येकं हनुमज्जयैषिण इत्यर्थः" = "parasparajayaiṣiṇaḥ — [meaning] each one individually desiring to defeat Hanumān." This matches the note precisely — Tilaka reads it as sibling rivalry among themselves, Bhushana reads it as each independently wanting to beat Hanuman. Faithful (2). The note also claims "перевод следует Тилаке" (the translation follows Tilaka) — checking Leonov's own Russian: "желающие превзойти друг друга" = "wanting to surpass each other" — this indeed matches Tilaka's mutual-rivalry reading, not Bhushana's each-vs-Hanuman reading. Confirmed.

Let's check baselines.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s45_leonov.json
Confirms exactly the note's `complements_leonov` claim: tier-1's own note is just the literal translation, without noting Bhushana's divergent reading.

**5.45.2**: Faithful (2), non-trivial (2, tier-1 note is literal-translation-only), contrastive_value: genuine two-commentator divergence with translation choice identified = **2**, register clean (2), anchoring: tilaka/bhusana pratika `matches_verse: true` → 2. **Verdict: keep**.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_45_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_45_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
All 18 assigned sargas are now judged. Let me do a final comprehensive validation pass across all files to make sure JSON is valid, UTF-8 no BOM, and nothing else was touched.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
All 60 notes across the 18 assigned sargas are judged, JSON validates, no BOM, and I never touched `rejected[]` arrays or drafter fields — only added `judge` objects to notes and `judged`/`judge_verdict_counts` to `_meta`. Let me do one last sanity check confirming no other fields were altered by diffing note counts against original `notes_drafted` in `_meta`.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Everything checks out cleanly. All 18 sargas judged, all counts reconcile, no BOM, no git run, brief's in-place output format followed exactly.

Per the brief's required output format, here is the one-line-per-sarga summary:

sarga 19 judged: 6 notes → keep 6 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 20 judged: 5 notes → keep 5 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 21 judged: 5 notes → keep 4 / edit 0 / park 0 / reject 0 / flag_anchor 1
sarga 23 judged: 0 notes → keep 0 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 25 judged: 3 notes → keep 2 / edit 1 / park 0 / reject 0 / flag_anchor 0
sarga 27 judged: 4 notes → keep 4 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 28 judged: 3 notes → keep 3 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 29 judged: 3 notes → keep 3 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 31 judged: 2 notes → keep 2 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 32 judged: 4 notes → keep 4 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 33 judged: 6 notes → keep 5 / edit 0 / park 0 / reject 1 / flag_anchor 0
sarga 38 judged: 4 notes → keep 3 / edit 1 / park 0 / reject 0 / flag_anchor 0
sarga 40 judged: 3 notes → keep 3 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 41 judged: 4 notes → keep 4 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 42 judged: 3 notes → keep 3 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 43 judged: 2 notes → keep 2 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 44 judged: 2 notes → keep 2 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 45 judged: 1 notes → keep 1 / edit 0 / park 0 / reject 0 / flag_anchor 0

**Totals: 60 notes judged across 18 sargas → keep 56 / edit 2 / park 0 / reject 1 / flag_anchor 1.**

Notable findings surfaced during judging (beyond routine keeps):
- **5.21.19 → flag_anchor**: content is faithful but genuinely misattributed to the wrong verse — the segmenter's own internal marker (`।। 4.21.18 ।।`) and Kostina's own tier-1 note both point to v.18, not v.19 where the note was filed.
- **5.33.11 → reject**: faithfulness capped at 1 — the note co-attributes a vyañjana/lakṣaṇa distinction to both Tilaka and Bhushana, but only Bhushana's text cleanly draws that split; Tilaka's chunk treats the terms together.
- **5.25.3 → edit** and **5.38.65 → edit**: content fully faithful, but register fails on stray mixed-script typos (Cyrillic/IAST/Latin character mixing) needing a mechanical fix before print.

