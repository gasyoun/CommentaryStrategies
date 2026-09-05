_Created: 07-07-2026 · Last updated: 05-09-2026_

# Agent log agent-a788a68cc585aa2de

_Model: `claude-sonnet-5`; extracted by scripts/export_agent_logs.py; raw transcript alongside (.jsonl) holds the full record incl. tool results._


I'll start by reading the judge brief to understand the exact rubric and process.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\JUDGE_BRIEF.md
Now let me check the rubric doc and set up my worklist.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\docs\PHASE2_METHOD.md
Now I understand the full rubric. Let me check my assigned sarga files to see how many notes each has.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && f
Total 70 notes across 22 sargas. Let me check baseline data files and confirm their structure first.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Need to force UTF-8 stdout. Let me write helper scripts to a scratch file instead of inline commands with Cyrillic output.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\wor
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_46_candidates.json
Now let's look at the segmented bundle for sarga 46 to check the cited texts and pratika_check/anchoring.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_46_segmented.json
Now let me check the tier-1/Phase-1 baseline files structure to cross-check non-triviality against.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && w
These are large files. Let me write a small Python helper script (saved to scratchpad) that I can reuse to pull the relevant slices per sarga, since I'll need this 22 times.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\extract_baseline.py
This is a trivial one-off JSON-slicing helper for my own judging workflow (not a durable repo asset, not a transcoder/parser worth checking prior art for) — it lives in scratchpad, not the repo. Proceeding.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && f
Good, baselines extracted for all sargas (61 has zero notes, skip). Now let me look at the baseline structure for sarga 46 to know what fields to check against for non-triviality.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\baseline_46.json
This confirms note 5.46.1's `complements_leonov` claim is accurate — Leonov's own note covers `saṃvṛtākāraḥ` and general "решительное" reading via Tilaka/Tattvadipika, but NOT the specific "punaryuddhaniścaya" reading of Śiromaṇi. Let me check verses 5, 11, 14, 19, 21, 41 in the leonov baseline for sarga 46.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
This confirms note 5.46.41's claim about resolving the "Гита-Пресс" translation dispute is accurate (Kostina's own note flags exactly that dispute). Note 5.46.11's Phase-1 note is about `dhīra`/`parākrama` compound, doesn't cover the "punarvacana sthairyārtham" reasoning point — so it's non-trivial. Let me check the Tattvadipika full-text for 5.46.5 (deshakala) to compare with the note's claim about samādheyam polarity — that's a different lemma so no overlap.

Now let me judge each note in sarga 46 systematically. Let me re-examine all 7 notes against their bundle texts I already have.

**Note 5.46.1 (uttamāṃ matim)**: Cited siromani text: "उत्तमां मतिं पुनर्युद्धनिश्चयमित्यर्थः" = "uttamāṃ matim = punaryuddhaniścaya" — confirmed, faithfully entailed. Non-trivial vs Leonov's own note (Tilaka/Tattvadipika reading only). Single commentator, real exegetical gain (contrastive_value=1, since it's not contrasting 2 but adding an unmentioned reading). Register clean, 2 sentences. Anchoring: siromani pratika matches_verse=true (verified, anchoring=2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_46_segmented.json
Note 5.46.5 checked: Tilaka says "समाधेयं कार्यम्" (samādheyam = kāryam, "that which must be done"). Bhūṣaṇa says "समाधेयं परिहर्तव्यम्" (samādheyam = parihartavyam, "that which must be avoided"). This is a genuine, faithful, exact opposite-polarity contrast — verified. Both anchoring: bhusana matches_verse=true(2), tilaka content_anchor=true but matches_verse=false (1). Overall anchoring should be conservative — I'll take the anchoring of the cited commentators; since both cited commentators are used and one is unverified-but-plausible, I'll score anchoring=1 (not fully verified for both).

Let me check notes 11, 14, 19, 21, 41 against their cited texts (already have all in the bundle read above).

Note 5.46.11 (punarvacanam): Tilaka: "सवाजिरथेत्यादिपुनर्वचनं स्थैर्यार्थम्" = "the repetition beginning 'savājiratha...' is for the sake of sthairya (steadfastness)". Faithful match. Anchoring: tilaka pratika `matches_verse: false, content_containment: 0.0` — no content_anchor field present, meaning it did NOT pass content anchor either! Let me check that carefully.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_46_segmented.json
Confirmed: for Tilaka's chunk on verse 11, `matches_verse: false` and `content_containment: 0.0` — no `content_anchor: true` field at all. This is contradicted/unverified anchoring per the brief's definition ("contradicted... `suggest_verse` points elsewhere and the note's content fits that other verse" → 0 ⇒ `flag_anchor`). But there's no `suggest_verse` field shown either. Let me check if there's a `suggest_verse` field elsewhere in this bundle to understand the schema fully.

- 🔧 `Grep` — suggest_verse
No `suggest_verse` field in sarga 46's bundle at all — so nothing is "contradicted" in the strict flag_anchor sense here. For Tilaka on verse 11: pratika doesn't match verse text directly, containment is 0.0 (no textual overlap detected), and no content_anchor confirmation. However, the actual Sanskrit content ("सवाजिरथेत्यादि" = "beginning with 'with horses, chariots...'") explicitly quotes the pratīka from verse 11 itself ("savājirathamātaṅgāḥ...") — this is a case where the segmenter's automatic containment scorer failed (it's an anaphoric "ityadi" reference-quote, not a literal repeat), but manual inspection shows it's clearly anchored to v.11 (it literally names the opening words of v.11). This is a case for anchoring=1 (unverified by the automated check but plausible/manually confirmable) rather than 0, since there's no suggest_verse contradicting it and the content itself (referring to "sthairyārtham," repetition) is thematically about v.11's repeated phrase. I'll score anchoring=1, not flag_anchor, since nothing contradicts it — the gate says 0 requires actual contradiction with a fitting alternative verse, which isn't present here.

Now let's check note 5.46.14 (sattvam), 19 (upamā/rūpaka), 21 (dikṣu sarvāsv avasthitāḥ). All already read from the segmented file above — tilaka on v.14: "सत्त्वं चित्तम्" = sattvam = cittam confirmed faithful. v.19 bhusana: "रश्मिमन्तमिवेत्यत्र उपमा, अत्र रूपकमिति भिदा" = confirmed exact match to note's claim. v.21 tilaka: "द्राक्तत्समीपमागन्तुं चकिता इति भावः" = "the sense is that they were afraid (cakitāḥ) to approach immediately" — confirmed faithful.

All anchoring for these: v.14 tilaka matches_verse=true(2); v.19 bhusana matches_verse=true(2); v.21 tilaka matches_verse=true(2).

Now let me verify note 5.46.41's contrastive claim once more — Tilaka: "कृतक्षणो लब्धावसरः" (kṛtakṣaṇaḥ = labdhāvasaraḥ). Bhūṣaṇa: "कृतक्षणः दत्तावसरः" (kṛtakṣaṇaḥ = dattāvasaraḥ). Both agree in essence ("one who obtained/was given the opportunity" — i.e., "awaited the moment"), confirmed. Anchoring: tilaka matches_verse=true(2), bhusana matches_verse=true(2). Good.

Now let me write out the judge objects for sarga 46.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_46_candidates.json
I made a typo "Widromani" — let me fix that.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_46_candidates.json
Now note 5.46.5 (samādheyam contrastive):

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_46_candidates.json
Now note 5.46.11 (punarvacanam):

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_46_candidates.json
Now note 5.46.14 (sattvam):

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_46_candidates.json
Now note 5.46.19 (upamā/rūpaka):

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_46_candidates.json
I made an error there - let me fix it with the proper judge object.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_46_candidates.json
Now note 5.46.21 (dikṣu sarvāsv avasthitāḥ):

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_46_candidates.json
Now note 5.46.41 (kṛtakṣaṇaḥ), the last one:

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_46_candidates.json
Now update `_meta` for sarga 46 with judged:true and verdict counts.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_46_candidates.json
Let me verify the whole file is valid JSON now.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 46 is done: 7 keep. Now let's move to sarga 47.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_47_candidates.json
Now let me check the segmented bundle for sarga 47's cited verses (2, 5, 17, 26, 38).

- 🔧 `Grep` — "verse_id": "5\.47\.(2|5|17|26|38)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_47_segmented.json
Good. Note 5.47.2 (sadasi): siromani text says "सदसि यागशालायां" = sadasi = yāgaśālāyāṃ (in the sacrifice-hall) — confirmed faithful, exact match. Anchoring: siromani pratika matches_verse=false but content_anchor=true (containment 0.273) — unverified but plausible (1).

Note 5.47.5 (bandhura): Bhūṣaṇa's text gives exactly three interpretations for bandhura — "फलकासङ्घाट इत्याहुः। अन्ये घण्टा इत्यप्याहुः" (some say phalaka-saṅghāta "assembly of boards", others say ghaṇṭā "bells") plus the base reading "अष्टासिभिर्निबद्धं बन्धुरं...सुन्दरम्" (adorned with eight swords, beautiful). That's confirmed — three glosses without picking one. Anchoring: bhusana matches_verse=true(2).

Let me check the rest (17, 26, 38).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_47_segmented.json
Confirmed note 5.47.17 (mandarāgrastha): both Tilaka ("मध्यन्दिनस्थत्वं लक्ष्यते" — indicating noon-position) and Bhūṣaṇa ("मध्याह्ने वर्तत इत्यौग्र्योक्तिः" — "at midday, this is an augryokti/hyperbole") confirmed exactly. Anchoring: tilaka matches_verse=true(2), bhusana matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_47_segmented.json
Excellent — confirmed exactly: Tilaka's text: "'प्रमापणे मारुतिरत्र जायते' इति पाठे 'अयं जनः' इतिवत्स्वस्यैव हनुमता मारुतिरिति निर्देशः" — this exactly matches the note's claim about the variant reading "mārutiḥ" and third-person self-reference, with the "ayaṃ janaḥ" analogy also captured faithfully in the drafted note ("аналогичный «этот человек»"). Anchoring: tilaka `matches_verse: false`, but `content_anchor: true` (containment 0.333) — unverified but plausible (1).

Now note 5.47.38 (kṛtakṣaṇaḥ):

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_47_segmented.json
Confirmed exactly: Tilaka's cited text "कृतक्षणः पुनर्युद्धे कृतोत्साहः" (kṛtakṣaṇaḥ = punaryuddhe kṛtotsāhaḥ, "one who has become eager for a renewed battle") matches the note's claim. The comparison with 5.46.41's Tilaka reading ("labdhāvasaraḥ") is verified against my earlier reading of sarga 46's bundle. Anchoring: tilaka matches_verse=true(2).

Now let me check the Phase-1/tier-1 baseline for sarga 47 to confirm non-triviality for these 5 notes, especially checking Kostina's note at 5.47.2 and 5.47.38 (referenced explicitly).

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
All confirmed non-trivial: 5.47.2 exactly answers Kostina's open question about "собрание"; 5.47.38 exactly answers Kostina's request for a cross-ref/comment to 46.41. Good — all 5 notes are faithful, non-trivial, well-anchored (mostly verified or content-anchor-plausible), register clean. Now let's write judge objects for sarga 47.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_47_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_47_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_47_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_47_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_47_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_47_candidates.json
Sarga 47 done: 5 keep. Now sarga 48.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_48_candidates.json
- 🔧 `Grep` — "verse_id": "5\.48\.(8|15|23|49|55)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_48_segmented.json
Note 5.48.8: Siromani's cited text: "एतेनातिप्रबलत्वात्तव वधो न भविष्यतीति ध्वनितम्" = "by this it is suggested/implied (dhvanitam) that because you are so exceedingly powerful, your death will not occur" — and "ननु तर्हि ममापि वधः स्यादित्यत आह नेति" ("[objection:] then would my death too occur? To this he answers 'no'"). This confirms the note's claim exactly — the implied unspoken worry is addressed as an implication (dhvanitam). Faithful match confirmed. Anchoring: siromani matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_48_segmented.json
Confirmed exactly: Bhūṣaṇa's cited text quotes the Viṣṇu Purāṇa verse: "मनसा त्वेव भूतानि पूर्वं दक्षो ऽसृजत्तथा। देवानृषीन्सगन्धर्वानुरगान् पक्षिणस्तथा" — matches note 5.48.15's claim exactly. Anchoring: bhusana matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_48_segmented.json
Confirmed exactly: Tilaka's cited text "चक्रचरा ग्रहाः" (cakracarāḥ = grahāḥ, "planets"). This is genuinely a third distinct reading (Kostina cited only Goldman = ṛṣis, Gita-Press = siddhas). Faithful match confirmed. Anchoring: tilaka matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_48_segmented.json
Note 5.48.49 attributes the reasoning to Śiromaṇi (`source_commentary: ["siromani"]`), but let me check carefully what Śiromaṇi's cited text actually says vs. what Tilaka's says. Śiromaṇi's text: "अन्येन बद्धो ऽयम् अस्त्रमनुवर्तते अथ इति हेतोः चिन्तां जगाम" — "since he, bound by another [material], still follows/obeys the astra, therefore [Indrajit] became anxious." This is essentially: the *cause* of Indrajit's cintā is that Hanuman "acts as if still bound by the astra" (anuvartate 'stram) even though bound by rope. That matches the note's claim reasonably well — though the note's phrasing "не уверен, разрушены ли чары на самом деле" (unsure the magic was truly broken) is a slight interpretive gloss beyond the literal "he becomes anxious because [Hanuman] still obeys the astra" — but this is a reasonable paraphrase of the same idea, not an overreach. I'll call this faithful (2). Anchoring: siromani matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_48_segmented.json
Confirmed exactly: Tilaka's cited text "उत्तराशयस्तु दूत्यं कृत्यम्, प्रेरकः सुग्रीव इति" = "the true/inner intent is: the mission (kṛtya) is an embassy (dūtya), and the instigator is Sugrīva." This matches note 5.48.55's claim exactly — dūtya + Sugrīva. Anchoring: tilaka matches_verse=true(2).

Now let me confirm non-triviality against baselines for these 5 notes.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
Confirmed all non-trivial. Note 5.48.55's Phase-1 gloss found: Leonov's own note already contains Tilaka's "kasyāśrayeṇaivaṃ nirbhaya" (whose help makes him fearless) reading — that IS the same Tilaka comment, but the note being judged cites a *different* clause from Tilaka's same commentary block ("uttarāśayastu dūtyaṃ kṛtyam, prerakaḥ sugrīva" — the "true intent" that names dūtya + Sugrīva), which is a separate, additional point not covered by Leonov's own note (which only covers the "kasyāśrayeṇa" sub-clause). Let me double check this distinction is real and not overlapping.

Looking at the segmented Tilaka text again: `"कस्य सुत इति शेषः । को ऽभ्युपाश्रयः कस्याश्रयेणैवं निर्भय इत्यर्थः\nकार्यं कर्तव्यमर्थस्तत्प्रयोजनं च । समाहारद्वन्द्वः अर्थस्य मूलमुक्तप्रयोजनप्रवर्तकम् । उत्तराशयस्तु दूत्यं कृत्यम्, प्रेरकः सुग्रीव इति"` — this is one continuous Tilaka comment block covering multiple lemmas of v.55 (ko'yaṃ, ko'bhyupāśrayaḥ, kiṃ kāryaṃ). Leonov's own note picks out the "kasyāśrayeṇa" (ko'bhyupāśrayaḥ) gloss only. The candidate note picks a *different* lemma within the same block — "kiṃ kāryam" → "uttarāśayastu dūtyaṃ kṛtyam, prerakaḥ sugrīva" (the deeper intent = embassy, instigator = Sugrīva). This is indeed a distinct, additional point not covered by Leonov's own note — non-trivial confirmed, though the note's phrasing attributes it loosely to "ko'bhyupāśrayaḥ" when technically it's the kāryam clause's "uttarāśaya" gloss that supplies dūtya/Sugrīva. This is a minor lemma-labeling looseness — I'll flag it as a register/minor overreach issue (faithfulness stays 2 since the content itself, not attribution to the wrong lemma within the same verse, is accurate) but note it, or apply faithfulness=1 for lemma mismatch. Given the note's lemma is `ko 'bhyupāśrayaḥ` but the actual dūtya/Sugrīva point comes from the kāryam clause of the same commentary passage — this is a minor attribution looseness within the same verse's single Tilaka block, not a misattributed commentator or invented claim. I'll treat this as faithfulness=2 (content accurate, source correctly cited as Tilaka on this verse) but flag it as an `edit`-worthy register note.

Actually let me be more careful and precise here, re-reading:

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_48_candidates.json
Good — actually this note doesn't claim `ko'bhyupāśrayaḥ` itself yields "dūtya/Sugrīva" — rather, its narrative claim ("ракшасы не подозревают ответа, который Тилака проговаривает за них") is about the whole verse's rhetorical situation (the questions collectively), and it correctly attributes the specific dūtya/Sugrīva content to Tilaka's broader gloss on the verse (which does span all the questions in one continuous comment). The `complements_leonov` field even explicitly says Leonov's note only covers `ko'bhyupāśrayaḥ`'s literal sense while this note draws on the fuller Tilaka passage. This is accurate framing, not misattribution — faithfulness = 2 is correct.

Now let me write all judge objects for sarga 48.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_48_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_48_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_48_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_48_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_48_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_48_candidates.json
Sarga 48 done: 5 keep. Now sarga 49 (3 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_49_candidates.json
- 🔧 `Grep` — "verse_id": "5\.49\.(4|7|18)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_49_segmented.json
Note 5.49.4: Tilaka's text "भक्तिभिः शैवत्रिपुण्ड्रवद्रचनाविशेषैः" = bhaktibhiḥ = śaiva-tripuṇḍra-vad racanā-viśeṣaiḥ ("marks like the Shaiva tripuṇḍra") — confirmed exactly. Anchoring: tilaka matches_verse=true(2).

Note 5.49.7: Bhūṣaṇa's text: "पूर्णचन्द्राभवक्त्रेण पूर्णचन्द्रतुल्यनायकरत्नेन। वक्त्रं नायकरत्नम् अभितोलग्नमुक्तामणिमण्डलम्" = "pūrṇacandrābhavaktreṇa = pūrṇacandra-tulya-nāyakaratnena; vaktraṃ = nāyakaratnam abhitolagnamuktāmaṇimaṇḍalam (the central/main gem surrounded by a circle of pearl-gems)" — confirmed exactly. Anchoring: bhusana matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_49_segmented.json
Confirmed exactly: Tilaka's text "अधर्महतत्वात्तु स्वप्रजानामपि नाशक एवेति भावः" = "because he is destroyed/afflicted by adharma, he is indeed a destroyer even of his own subjects" — exactly matches the note's claim about Ravana being ruinous even to his own subjects, not just unable to protect the other world. Anchoring: tilaka `matches_verse: false`, `content_containment: 0.2`, `content_anchor: true` — unverified but plausible (1).

Now let me check non-triviality via baselines.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
Let me see the full text of Kostina's note for 5.49.7 to confirm the note's claim it "doesn't name the source" but implies Goldman.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
Confirmed exactly matching the note's `complements_leonov` claim. All three notes for sarga 49 confirmed faithful, non-trivial. Now write judge objects.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_49_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_49_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_49_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_49_candidates.json
Sarga 49 done: 3 keep. Now sarga 50 (2 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_50_candidates.json
- 🔧 `Grep` — "verse_id": "5\.50\.(9|18)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_50_segmented.json
Confirmed exactly: Tilaka's text: "चाररूपं चाराणां प्रच्छन्नवेषत्वाच्छद्मकृतवानररूपम्" = "cārarūpam = due to spies' (cārāṇām) practice of disguise, a feigned monkey-form" — confirmed exactly matches the note's claim about the cāra ("spy") etymology. However, anchoring is concerning: `matches_verse: false`, `content_containment: 0.0` — no content_anchor field present at all. This is a genuinely weak anchor (similar to sarga-46 v.11 case, but here containment is literally 0.0, meaning even the automated content overlap check found nothing). Let me think about this carefully.

The rubric says: anchoring 0 requires "contradicted (`suggest_verse` points elsewhere and the note's content fits that other verse)". There's no `suggest_verse` field in this bundle at all (let me check).

- 🔧 `Grep` — suggest_verse
No `suggest_verse` — so not "contradicted" in the strict rubric sense, but it's also not "unverified but plausible" in the strong sense that content_anchor=true implies (there's zero automatic containment). However, manual inspection shows the Tilaka gloss on `cārarūpam` is unambiguously discussing the exact word `cārurūpam/cārarūpam` that appears in verse 9 itself (it's a direct lexical gloss of the verse's own compound, quoted almost verbatim as the pratīka "cārarūpaṃ"). The automated scorer likely failed because "cārurūpam" (verse's exact spelling) vs "cārarūpam" (Tilaka's pratīka spelling) differ by one vowel — a real vs. reported textual variant, which is *exactly the point of the note*. This is a case where the anchor is manually verifiable (the pratīka literally reproduces the compound from the verse, just with the vowel variant that is the note's whole subject) despite the automated check missing it due to the very variant being discussed. I'll score anchoring=1 (unverified by automation but plausible/manually confirmable, not contradicted).

Now check note 5.50.18:

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_50_segmented.json
Confirmed exactly: Bhūṣaṇa's cited text reads "केनचिद्राजकार्येण संप्राप्तो ऽस्मि तवान्तिकम्" (kenacid rājakāryeṇa saṃprāpto 'smi tavāntikam) — "rājakāryeṇa" not "rāmakāryeṇa" as in the printed verse text (which itself reads "kenacid rāmakaryeṇa āgato 'smi"). This confirms the note's claim of the textual variant exactly. Anchoring: bhusana matches_verse=true(2).

Let me check baselines for both.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
Confirmed exactly: both non-triviality claims verified. 5.50.9's Kostina/Leonov own note names the variant "cārarupam" = "в облике лазутчика" but doesn't explain the etymology — the drafted note adds exactly that missing motivation. 5.50.18's Kostina note flags the passage as needing a comment ("далековато от текста" = "quite far from the [source] text") without identifying the specific variant — the drafted note supplies exactly that. Both non-trivial, confirmed. Now write judge objects for sarga 50.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_50_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_50_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_50_candidates.json
Sarga 50 done: 2 keep. Now sarga 52 (1 note).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_52_candidates.json
- 🔧 `Grep` — "verse_id": "5\.52\.19"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_52_segmented.json
Excellent — confirmed exactly. Tilaka's cited comment (attached to the preceding verse 18's chunk, quoting both v.18 AND v.19's full text): "इत्थंविधस्यामरदैत्यशत्रोः शूरस्य वीरस्य तवाजितस्य कुर्वन्ति वीरा मनसाप्यलीकं प्राणैर्विमुक्ता न तु भोः पुरा ते । इति श्लोकद्वयं प्रक्षिप्तमिति कतकः । न चाप्यस्य कपेरिति" — "this pair of verses is an interpolation (prakṣiptam), according to Kataka" (kaṭakaḥ = the commentator Kataka). This matches the note's claim precisely and faithfully. However, this Tilaka comment is physically attached to verse 18's segment in the bundle, not verse 19's (verse 19's own segment only has a Siromani chunk). The note attributes this to verse 19 specifically (`verse_id: "5.52.19"`), which is defensible since the note explicitly discusses "vv.18–19" as a pair, and the segmenter's marker-based split put the full quoted couplet under v.18's chunk due to how the source text is laid out (a common known marker-offset artifact per the brief's caveats). The content is accurate regardless of which verse_id it's filed under.

Anchoring: Since the note is filed under 5.52.19, but the actual Tilaka commentary about the interpolation is physically in v.18's `commentary.tilaka` field with no `pratika_check` entry under v.19's own bundle for "tilaka" — this is exactly the marker-offset case. Let me check v.19's pratika_check fully.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_52_segmented.json
Confirmed — Tilaka's chunk isn't even present in v.19's own `commentary` object; it lives in v.18's bundle (source_commentary cites tilaka for the note, but the segmenter placed the actual chunk one verse earlier, a marker-offset case explicitly documented in §11 of the method doc). No `suggest_verse` field exists, so nothing is "contradicted" per the strict gate — but there's also no pratika_check entry at all for tilaka under v.19. Since the note itself explains this is about "vv.18–19" as a pair, and the source text is fully verifiable (I located and read it, verbatim, in v.18's bundle), I'll treat this as anchoring=1 (unverified-in-v.19's-own-bundle but plausible/manually located) rather than a hard flag_anchor, since the content is real, faithfully quoted, and the marker-offset explanation is explicit and consistent with known segmenter behavior.

Now check the baseline for non-triviality.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
Confirmed non-trivial: Kostina's own note about vv.18–19 is purely editorial ("absent in Bombay edition, present in Gita-Press") — the candidate note adds the *traditional* pre-critical attribution of interpolation to the named commentator Kataka, which is a distinct kind of evidence. Faithful, non-trivial confirmed.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_52_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_52_candidates.json
Sarga 52 done: 1 keep. Now sarga 53 (2 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_53_candidates.json
This is a more complex case — the note attributes content to a verse but explicitly says the source text is "marker-shifted." Let me verify these carefully in the segmented file.

- 🔧 `Grep` — "verse_id": "5\.53\.(5|19|33|13)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_53_segmented.json
Confirmed: Siromani's cited text (in v.5's own bundle): "एतेनैतादृशदर्शनेन हतबान्धवानां राक्षसीनां दुःखशान्तिर्भविष्यतीति सूचितम्" = "by this, it is indicated that the grief of the rākṣasī women whose kinsmen were slain will be assuaged by seeing this [spectacle]" — matches the note's Siromani half exactly. Now check Tilaka's text — the note says it's marker-shifted to V.53.19. Let's check v.19.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_53_segmented.json
Confirmed exactly: Tilaka's cited text at v.19: "अथ रावणः स्वपुरदुर्गमहाबलमहैश्वर्याणि परेभ्यः प्रकाशयितुं सर्वपुरपरावर्तनं दीप्तपुच्छस्याज्ञापयदित्याह" = "Then, in order to display to outsiders the strength/fortification/wealth of his own city, Rāvaṇa ordered the parading of [Hanuman] with a burning tail throughout the whole city" — matches the note's claim about Tilaka's motivation (demonstrate might/wealth/impregnability to the stranger-spy) exactly. Anchoring: tilaka matches_verse=true (2) at v.19's own bundle — but the note is filed under v.5, not v.19, per the drafter's explicit cross-reference in the note text (which mentions "текст смещён к V.53.19"). Since the note explicitly documents this cross-reference and the content is verified, this is fine — anchoring based on where the content actually is (v.19, verified match) is solid (2), though the note's primary verse_id (5.53.5) doesn't itself carry the tilaka pratika_check. I'll score anchoring=1 to reflect that the note's own verse_id (5.53.5) doesn't directly carry a verified tilaka anchor, though the actual quoted content is verified elsewhere and the note transparently discloses the shift.

Now let's check note 5.53.33 (interpolation about additional strophes between 32–33).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_53_segmented.json
Interesting — I don't see a Bhūṣaṇa quote about "additional interpolated strophes" between 32–33 in this bundle at v.33. Let me search more broadly in the sarga_53 segmented file and also check surrounding verses (rejects mention v.13's fragment "о вставных строфах" as marker-shifted from vv.32-33). Let me check v.13's bundle.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_53_segmented.json
Found it — the actual text is in **Bhūṣaṇa's chunk at v.13**, not v.33 as the note claims, and it's Bhūṣaṇa (not stated explicitly which commentator but embedded in the same commentary block cited under `"bhusana"` at v.13): "अस्मात्परं दह्यमाने च लाङ्गूल इति श्लोकः। अनयोः श्लोकयोर्मध्ये केचन श्लोकाः कतिपयकोशेषु दृश्यन्ते। बहुकोशेषु अदर्शनादर्थाधिक्याभावाच्च ते अनादरणीयाः" = "After this comes the verse 'dahyamāne ca lāṅgūle...' [i.e. v.33]. Between these two verses [32 and 33], some additional verses are seen in a few manuscripts. Since they are absent in most manuscripts and add no [new] content, they are not to be respected/regarded [anādaraṇīyāḥ]." 

This confirms the note's claim faithfully and precisely — including the exact word "anādaraṇīyāḥ" cited in the note's lemma field. The note is filed under `source_commentary: ["bhusana"]`, correct commentator. Anchoring: this chunk is physically embedded within v.13's `bhusana` field, not v.33's own bundle — again a marker-offset case. There's no `suggest_verse` in the bundle (verified below) so it's not contradicted, but it's not verified in the note's own filed verse either.

- 🔧 `Grep` — suggest_verse
No suggest_verse, confirmed not contradicted. Now let me check baselines for non-triviality.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
Both confirmed non-trivial. Kostina's own note at 5.53.5 only gives the literal composite meaning, no discussion of purpose; her note at 5.53.33 only flags an omitted half-line, no mention of the manuscript-variant strophes question. Both notes are faithful, non-trivial, contrastive (5.53.5 genuinely contrasts two distinct motivations from two commentators). Let's write judge objects.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_53_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_53_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_53_candidates.json
Sarga 53 done: 2 keep. Now sarga 54 (4 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_54_candidates.json
- 🔧 `Grep` — "verse_id": "5\.54\.(29|37|42|46)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_54_segmented.json
Confirmed. Tilaka's cited text at v.29: "वसुन्धरा नेति मृतराक्षसानां शयनाय लङ्काभूमिर्न पर्याप्ता ऽभूदिति शेषः" = "vasundharā na iti — the Lanka-ground was not sufficient to accommodate the bodies of the slain rākṣasas" — literal reading confirmed. Siromani's cited text: "वसुन्धरा च न तृप्यति निहतसर्वराक्षसवधरणमाकाङ्क्षतीत्यर्थः, तेन पतिवियोगजनितस्वसुतादुःखहेतुकदुःखाक्रान्तत्वं तस्याः सूचितम्" = "the earth too is not satisfied, desiring more slaying of the killed rākṣasas — by this, it is indicated that she [the earth/Bhūmi] is afflicted by the suffering caused by the grief of her own daughter [Sītā] due to separation from her husband" — matches the note's claim about Bhūmi as Sītā's mother sharing her grief, exactly. Faithful, confirmed contrastive.

Anchoring: tilaka matches_verse=true(2); siromani matches_verse=false, content_containment=0.7, content_anchor=true — unverified but plausible (1). Overall anchoring for the note ~1-2, I'll score 2 for tilaka's clean match but note siromani's is content-anchor only; I'll be conservative and score anchoring=1 given one of the two cited commentators is only content-anchored.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_54_segmented.json
Confirmed exactly: Bhūṣaṇa's cited text says: "तदेव स्वमायया स्वासाधारणया आश्चर्यशक्त्या कपिरूपमेत्य साम्प्रतमागतं वा" = "svamāyayā = svāsādhāraṇayā āścaryaśaktyā (by his own uncommon/marvelous power)" — the exact word āścaryaśakti matches the note's claim exactly. Anchoring: bhusana matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_54_segmented.json
Confirmed exactly: Siromani's cited text: "अत्र स्वयंभुशब्दः शंभुपरः इति न संहारप्रकरणविरोधः" = "here the word svayambhu refers to śambhu [Shiva], so there is no contradiction with the destruction context" — matches the note's claim exactly. Anchoring: siromani `matches_verse: false`, `content_containment: 0.333`, `content_anchor: true` — unverified but plausible (1).

Let me check the baseline for 5.54.42 to confirm Kostina's noted disagreement (Brahma/Vishnu/Shiva).

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
Confirmed both non-trivial: 5.54.37 directly fulfills Kostina's flagged need for a māyā-clarification comment; 5.54.42's Leonov own note states the disagreement (Brahma/Vishnu/Shiva) without resolving it, exactly as the candidate note claims — Siromani resolves it as Shiva. Now let's check the 4th note, 5.54.46 (interpolation).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_54_segmented.json
Excellent, confirmed exactly, and directly in v.46's own bundle (no marker shift this time). Bhūṣaṇa's cited text: "अस्मिन् सर्गे एकपञ्चाशच्छ्लोकाः। ततो महात्मेति श्लोकः स राक्षसानिति श्लोकोक्तार्थकतया बहुकोशेष्वदर्शनाच्च प्रक्षिप्तः। बहुकोशेष्वेतत्सर्गसमाप्तिविपर्ययः उत्तरसर्गारम्भविपर्ययश्च दृश्यते" = "In this sarga there are 51 verses. The verse beginning 'tato mahātmā...' [and] the verse '[sa] rākṣasān...' are interpolated (prakṣiptaḥ), as their content is already stated [elsewhere] and because they are absent in many manuscript-collections. In many manuscripts, the ending-point of this sarga and the beginning-point of the next sarga differ [from this edition]." — matches the note's claim exactly, including the two named verse-openings ("tato mahātmā" and "sa rākṣasān") and the sarga-boundary variance. Anchoring: bhusana matches_verse=true(2), and this one is directly anchored in v.46's own bundle (no marker shift needed).

Now let's write all 4 judge objects for sarga 54.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_54_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_54_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_54_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_54_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_54_candidates.json
Sarga 54 done: 4 keep. Now sarga 55 (1 note).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_55_candidates.json
Let me check verse 18 (where the note claims the text is marker-shifted) and verse 22 (the note's filed verse).

- 🔧 `Grep` — "verse_id": "5\.55\.(18|22)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_55_segmented.json
Confirmed exactly: Bhūṣaṇa's cited text at v.18: "एवं लोकदृष्ट्या अनर्थमाशङ्क्य तत्त्वदृष्ट्या समाधत्ते अथवेत्यादिना। नाग्निरग्नौ प्रवर्तते अग्निरग्निं न दहतीत्यर्थः" = "Thus, having apprehended a misfortune from the worldly viewpoint (loka-dṛṣṭi), he consoles himself from the standpoint of the true state of affairs (tattva-dṛṣṭi), beginning with 'athavā...'; [meaning] fire does not act upon fire, fire does not burn fire" — this exactly matches the note's claim, and the "athavā" ("or else...") cross-reference confirms it's introducing the turn that begins at v.22 ("athavā cārusarvāṅgī..."). Faithful confirmed.

Anchoring: this chunk is physically in v.18's bhusana field (`matches_verse: true` there), but the note is filed under v.22, which itself has no bhusana `pratika_check` entry shown yet (need to check further).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_55_segmented.json
I see — v.22 does have a bhusana chunk (quoting v.22's own text), but no `pratika_check` entry for it (only siromani's is checked). So the note's `source_commentary: ["bhusana"]` is correctly attributed but its specific loka-dṛṣṭi/tattva-dṛṣṭi remark is physically located one verse earlier (v.18), which is what the note's text explicitly discloses ("текст смещён маркером к V.55.18"). Anchoring: no verified pratika_check for bhusana at either v.18 (matches_verse=true, so it IS verified there!) — wait, let me recheck: v.18's bhusana pratika_check DOES show `matches_verse: true`. So the content is anchored correctly at v.18, just filed under v.22 due to the drafter's judgment that the content thematically belongs to the turn starting at v.22. This is a deliberate, disclosed relocation, not an anchoring failure — I'll score anchoring=1 (verified elsewhere, not at the filed verse itself).

Let me check baseline non-triviality.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
Confirmed: no Leonov own note for either verse, and Phase-1's note is purely lexical (tejas etymology), not about the loka-dṛṣṭi/tattva-dṛṣṭi structural turn. Non-trivial confirmed.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_55_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_55_candidates.json
Sarga 55 done: 1 keep. Now sarga 56 (5 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_56_candidates.json
- 🔧 `Grep` — "verse_id": "5\.56\.(3|12|29|39|47)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_56_segmented.json
Confirmed exactly: Bhūṣaṇa's cited text at v.3: "वनभङ्गाक्षवधादिना हनुमतश्शक्तिं विज्ञाय असौ रामाय निवेद्य स्वयमेव सकलराक्षससंहारपूर्वकं मम नेता मा भूदित्याभिप्रायेणाह... ते यशस्यः यशस्करः। न तु रामस्येति भावः" = "having learned of Hanuman's power through the grove-destruction and Aksha's slaying, [Sita's] intention is that [Rama], having been informed, should not himself become [my] sole rescuer by slaying all rākṣasas — the meaning is: this glory be yours (bala-udayaḥ te yaśasyaḥ), not Rama's" — matches the note's claim exactly. Faithful confirmed. Anchoring: bhusana matches_verse=true(2).

Confirmed exactly for v.12: "तत् स्वपराक्रमेण मन्नयनम्...एतदेव ममाभिलषितम्, अन्यथा मे कथं वीरपत्नीत्वमिति भावः" = "this – my being led out by his own valor – this is what I desire; otherwise how would I be called a hero's wife?" — matches note exactly. Faithful confirmed. Anchoring: bhusana matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_56_segmented.json
Confirmed exactly: Tilaka's cited text: "प्राधीतमिवोच्चैः प्रारब्धाध्ययनमिव तत्स्वनानां महत्त्वात्। प्रगीतमिव प्रारब्धगानमिव तत्स्वनानां मन्दत्वात्" = "prādhītam iva = 'as if it has begun studying loudly,' because of the greatness [loudness] of its sounds; pragītam iva = 'as if it has begun to sing,' because of the softness of its sounds" — matches the note's claim exactly (loud→recitation/study, soft→singing). Faithful confirmed. Anchoring: tilaka matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_56_segmented.json
Confirmed exactly: Siromani's cited text at v.39: "त्रयोदशानामेकत्रान्वयः" = "trayodaśānām ekatra anvayaḥ" — "of the thirteen [half-verses], there is one [syntactic] construction/connection together" — matches the note's claim exactly (13 half-verses forming one syntactic construction). Faithful confirmed. Anchoring: siromani matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_56_segmented.json
Confirmed exactly. Tilaka: "व्यवेष्टन्त कुण्डलीकृतशरीरा अजायन्त। 'व्यचेष्टन्त' इति पाठे पीडया लुठन्नित्यर्थः" = "vyaveṣṭanta = they became coiled (kuṇḍalīkṛta) in body; in the reading 'vyaceṣṭanta,' the meaning is 'writhing from pain'." Siromani gives an identical note attributed "iti bhaṭṭāḥ" (per the Bhaṭṭas). Both cited exactly and confirm the note's claim. Faithful confirmed. Anchoring: tilaka matches_verse=true(2), siromani matches_verse=true(2). Note is genuinely contrastive (two commentators, both mentioning the variant).

Now let's check the non-triviality baselines for all 5.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
No Leonov own notes on any of these verses — non-trivial confirmed by absence. All 5 sarga 56 notes verified faithful, non-trivial. Now write judge objects.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_56_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_56_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_56_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_56_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_56_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_56_candidates.json
Sarga 56 done: 5 keep. Let me verify JSON validity for all completed sargas so far and continue to sarga 57.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && f
All good. Now sarga 57 (3 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_57_candidates.json
- 🔧 `Grep` — "verse_id": "5\.57\.(7|41|53)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_57_segmented.json
Bhūṣaṇa's cited text at v.7 is only: "अथ तदेवोत्प्रेक्षया वर्णयति-- ग्रसमान इवेत्यादिना" (a transitional note, "now he describes the same [phenomenon] with an utprekṣā [poetic fancy], beginning with 'grasamāna iva...'") plus the verse text itself. There's no explicit causal reasoning about Hanuman's own tejasvī nature causing the cloud colors visible in this chunk. Let me check the note's claim more carefully — it might be drawing on a different verse's commentary (perhaps v.6, referenced as "5,6" in the marker range).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_57_segmented.json
I don't find explicit "tejasvī" reasoning for cloud colors anywhere in this bundle for v.5-7. Let me search the whole segmented file for the word "tejasvī" or related root, or check if I'm missing a nearby verse (maybe v.6, which doesn't appear as its own bundle — it may be embedded elsewhere due to marker offset).

- 🔧 `Grep` — तेजस्वी|tejasv
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_57_segmented.json
Found it — the exact text is here, embedded in v.9's bundle (`bhusana` chunk, marker-tagged "5.57.7,8" internally): "महाभ्राणि चकाशिरे, हनुमत्सम्पर्कादित्यर्थः। अन्यथा वाजपेयशरद्वर्णनवत् अभ्रवर्णनस्यासङ्गतत्वापातः। हनुमतस्तेजस्वीत्यनेन मेघानां नानावर्णत्वापत्तिः सूर्येन्दुसम्पर्कवत्" = "'the great clouds shone' — meaning due to contact with Hanuman; otherwise the cloud-description would fall into irrelevance, like the [unrelated] autumn description in the Vājapeya [context]. By this ['Hanumat tejasvī' — Hanuman being full of splendor], the multi-coloredness of the clouds is accounted for, just as [clouds show varied colors] from contact with the sun and moon."

This confirms the note's claim exactly and faithfully — including the "tejasvī" term and the "otherwise the description would be an irrelevant insertion" reasoning. However, this chunk is physically in v.9's bundle (internally marker-tagged to vv.7,8), not v.7's own bundle as filed. This is again a marker-offset/content-anchor case. Faithfulness confirmed (2). Anchoring: since v.7's own chunk (which the note is filed under) shows `matches_verse: false`, `content_containment: 0.833`, `content_anchor: true` for bhusana — wait, that's interesting: v.7's OWN bhusana pratika_check shows content_anchor:true with containment 0.833, which is actually a strong content match! Let me recheck — perhaps the segmenter did correctly attach a chunk to v.7, but that chunk (which I read earlier) was just the transitional note + verse text, while the actual causal reasoning is a different, larger block that got attached to v.9 instead due to the internal marker "5.57.7,8" pointing elsewhere. Given the note's own v.7 bhusana anchor already registers content_anchor=true (0.833), that's a reasonably strong automated signal despite matches_verse=false. I'll score anchoring=1 (unverified but plausible per the automated content_anchor flag, further corroborated by manual location of the fuller reasoning in v.9's bundle).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_57_segmented.json
Confirmed exactly: Bhūṣaṇa's cited text: "क्ष्वेलन्ति सिंहनादं कुर्वन्ति। नदन्ति अव्यक्तशब्दं कुर्वन्ति। गर्जन्ति वृषभनादं कुर्वन्ति। किलिकिलां स्वजात्युचितकिलिकिलाशब्दम्" = "kṣveḍanti = make lion-roar sound; nadanti = make inarticulate sound; garjanti = make bull-roar sound; kilikilām = the species-specific kilikilā-sound" — matches the note's claim exactly (all four sound types, though "kilikilā" appears in v.42's text, adjacent). Faithful confirmed. Anchoring: bhusana matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_57_segmented.json
Confirmed exactly: Bhūṣaṇa's cited text: "कीर्तिमतेति हनुमद्विशेषणम्। यशस्विनेत्यङ्गदविशेषणम्। भृत्यकीर्त्या स्वामिनः कीर्तिः। अन्यथा पौनरुक्त्यात्। यद्वा बुद्धिमत्त्वजन्या कीर्तिः। शौर्यजन्यं यशः" = "kīrtimatā is Hanuman's qualifier, yaśasvinā is Angada's qualifier. [Reason:] the master's glory through the servant's glory (bhṛtyakīrtyā svāminaḥ kīrtiḥ) — otherwise there would be tautology. OR: kīrti arises from wisdom/intellect, yaśas arises from valor." This matches the note's claim precisely — both explanations (master-through-servant AND wisdom-vs-valor) are present exactly as described. Faithful confirmed. Anchoring: bhusana matches_verse=true(2).

Let me verify baselines for non-triviality.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
Confirmed: Kostina's own note at 5.57.53 mentions only the attribution split (kīrtimatā→Hanuman, yaśasvinā→Angada), not the reasoning behind why this isn't tautological — exactly as the candidate note's `complements_leonov` claims. No Leonov own note for 5.57.7 or 5.57.41 — non-trivial confirmed for all three.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_57_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_57_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_57_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_57_candidates.json
Sarga 57 done: 3 keep. Now sarga 58 (8 notes, the largest remaining).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_58_candidates.json
Let me check the 8 cited verses in the segmented bundle for sarga 58.

- 🔧 `Grep` — "verse_id": "5\.58\.(13|29|89|104|108|142|144|164)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_58_segmented.json
Confirmed exactly for both Bhūṣaṇa and Siromani (identical phrasing): "पितृव्यत्वे हेतुमाह-- सखायमिति। पितृसखत्वात् पितृव्यत्वव्यपदेश इत्यर्थः" = "As the reason for [being called] pitṛvya, he says 'sakhāyam' [friend] — meaning, the designation of pitṛvya is due to being a friend of the father." Matches note exactly. Faithful confirmed. Anchoring: both matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_58_segmented.json
Confirmed exactly: Bhūṣaṇa's text: "एवमेवार्थः, प्रथमसर्गोक्तशतयोजनविस्तारस्तु विरुद्धः। तद्ग्रन्थः कल्पितश्चेत्युक्तम्" = "This is indeed the correct meaning; the [statement of] hundred-yojana expanse mentioned in the first sarga (Bāla-kāṇḍa) is contradictory. That text (grantha) is fabricated (kalpitaḥ) — so it is said" — matches the note's claim exactly, including the direct quote "tad granthaḥ kalpitaḥ." Faithful confirmed. Anchoring: bhusana matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_58_segmented.json
I need to find the doctrinal svapna-truth reasoning that the note claims is at v.89 (marker-shifted from where the drafter says it should be, "по содержанию (svapna) оно относится к рассказу о сне в 87-89"). The note's `source_commentary` is `siromani`. Let me search for "mithyātve" and "svapna" reasoning across the bundle, particularly around v.95 (which the reject list says the segmenter attached it to).

- 🔧 `Grep` — mithyātve|mithyatve|स्वप्न.*मिथ्या|svapna.*mithya
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_58_segmented.json
Found it exactly — physically in v.95's own bundle: "ननु स्वप्नस्य मिथ्यात्वात्किं तद्दर्शनेन सीताभर्तृविजयादीत्यत आह यदीति... एतेन स्वप्नस्य मिथ्यात्वे ऽपि तद्दर्शनजनितफलस्य सत्यत्वं ध्वनितं मतान्तरे स्वप्नस्यापि सत्यत्वमित्यन्यदेतत्" = "[Objection:] since a dream is false, what does its being seen accomplish regarding Sītā's husband's victory? To this he answers 'yadi'... By this, it is indicated that even if the dream itself is false (mithyātve api), the fruit born from seeing it is true (taddarśanajanitaphalasya satyatvam); in another school (matāntare), the dream itself is also true — this is a different [view]."

This matches the note's claim precisely and faithfully, word for word. The note is filed under v.89 (the drafter's own disclosed re-anchor: "сегментатор закрепил это рассуждение за стихом 95, но по содержанию (svapna) оно относится к рассказу о сне в 87-89"). Note the drafter's stated rationale is inverted from what I actually see — the drafter says the segmenter attached it to v.95 but content-wise it belongs with the story at 87-89, so they moved it to v.89. This is a deliberate, disclosed editorial relocation. Faithful confirmed (2). Anchoring: verified at v.95 (matches_verse=true) but the note is filed at v.89, so scored as unverified-at-filed-verse (1), consistent with prior marker-shift cases, though the content is genuinely confirmed just one physically relocated.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_58_segmented.json
Confirmed exactly: Tilaka's cited text: "सन्दिदेश काकवृत्तान्तं तिलककरणं च राममात्रैकवेद्यं कथयामासेत्यर्थः" = "she conveyed/instructed [me] regarding the crow-episode (kāka-vṛttānta) and the applying-of-the-tilaka, matters known only to Rāma alone" — matches the note's claim exactly (kāka-vṛttānta + tilaka-application, known only to Rāma). Faithful confirmed. Anchoring: tilaka matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_58_segmented.json
Confirmed exactly: Bhūṣaṇa's cited text: "मासशब्दो ऽत्र पक्षपरः। 'पक्षा वै मासाः' इति श्रुतेः" = "the word 'māsa' here refers to pakṣa [fortnight/half-month], per the śruti 'pakṣā vai māsāḥ' (fortnights indeed are months)" — matches the note's claim exactly, including the direct quoted śruti formula. Faithful confirmed. Anchoring: bhusana matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_58_segmented.json
Confirmed exactly: Tilaka's cited text at v.142: "दूतप्रेषणं विना प्रथममेव युद्धस्याधर्मत्वादिति भावः" = "the sense is: without the sending of a messenger, war undertaken straightaway would be [an act of] adharma" — matches the note's claim exactly (though this v.142 chunk is marked `ambiguous_marker: true` in the bundle itself, unlike the note's implicit assumption of a clean verse). Faithful confirmed. Anchoring: tilaka matches_verse=true(2), though the verse itself is flagged `ambiguous_marker: true` at the bundle level — worth noting but the pratīka anchor is still directly verified. Let me check the baseline for Kostina's note on this exact question.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
Important finding: Leonov's own note at 5.58.142 ALREADY says: "'Как подобает' - в комментарии 'Тилака' отмечается, что начало войны без предварительных переговоров является неправедным (адхармой" — this is essentially the same content the candidate note gives! This appears to be a duplicate of Leonov's own note. Let me re-read the candidate note's justification carefully.

The candidate note's `why_proposed` claims: "прямо отвечает на вопрос, оставленный собственным примечанием Костиной к этому стиху («нужно как-то отразить, что закон здесь — это дхарма... иначе непонятно, почему в конце говорится про адхарму»)". But the baseline I just pulled shows Leonov's note ALREADY states the Tilaka adharma point directly, not as an open question. Let me check the full raw_text to see if there's more (maybe Kostina's specific bracket comment with the "непонятно" phrasing is appended after).

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
Now I see the full picture. Leonov's own note DOES already state the Tilaka reasoning "начало войны без предварительных переговоров является неправедным (адхармой)" — this is essentially identical to what the candidate note claims to newly supply. Kostina's bracketed comment is a follow-up meta-note asking for a terminological refinement (dharma = "the law" not "a legal code"), not asking for the Tilaka reasoning that's already there.

This means the candidate note's `why_proposed` justification is **misleading** — it frames this as answering an "open question" from Kostina, but the substantive content (Tilaka's dūta-preṣaṇa/adharma reasoning) is **already present verbatim in Leonov's own note**. This is a genuine non-triviality problem: the note appears to restate content that's already in tier-1. This is a duplicate, not a new fact.

Let me flag this correctly — non_triviality should be 0 (restates the crib/tier-1), triggering `park`.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_58_candidates.json
Confirmed: the candidate note's own text ("Тилака поясняет причину отправки посла: без предварительного посольства сама война была бы адхармой") is nearly word-for-word the same as Leonov's own note's Tilaka citation ("в комментарии 'Тилака' отмечается, что начало войны без предварительных переговоров является неправедным (адхармой)"). This is a duplicate — non_triviality = 0, park verdict per rubric gate ("≥1, else park").

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_58_candidates.json
Now let's check note 5.58.144 (vānarāṇāṃ / rāghavāṇāṃ variant).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_58_segmented.json
Confirmed exactly: Tilaka's cited text: "'राघवाणाम्' इति पाठे मनुष्यो ऽसमर्थ इति न मन्तव्यमिति भावः" = "In the reading 'rāghavāṇām', the sense is: it should not be considered that men (manuṣyaḥ) are incapable" — matches the note's claim exactly (variant reading rāghavāṇām, shifting the referent from monkeys' capability to humans' capability). Faithful confirmed. Anchoring: tilaka matches_verse=true(2). Note: this verse is flagged `ambiguous_marker: true` in the bundle, similar to v.142 — worth noting in the anchoring assessment, though the pratīka itself directly matches.

Now check note 5.58.164.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_58_segmented.json
Confirmed exactly: Bhūṣaṇa's cited text: "निमित्तैः शकुनैः। कारणैः नेत्रस्फुरणादिभिः...ऋषिवाक्यैश्च सिद्धार्थैः...तत्र हेतुत्वेन ऋषिपदोपादानम्" = "nimittaiḥ = śakunaiḥ (omens, e.g. birds); kāraṇaiḥ = netrasphuraṇādibhiḥ (eye-twitching etc. — bodily signs); ṛṣivākyaiḥ = siddhārthaiḥ (words of seers, [already] established/proven meaning); therefore the term 'ṛṣi' is used as the cause/reason" — matches the note's claim exactly (three distinct categories: nimitta=omens, kāraṇa=bodily signs including eye-twitch, ṛṣivākya=seers' words). Faithful confirmed. Anchoring: bhusana matches_verse=true(2).

Let's check the remaining baselines quickly.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
Good — Leonov's own note at 5.58.144 is about a DIFFERENT lemma (devatānāṃ sakāśam / Bhūṣaṇa's gods-inviting-monkeys point), not about the vānarāṇām/rāghavāṇām variant the candidate note discusses (Tilaka's point). These are genuinely distinct, non-overlapping facts about the same verse. Non-trivial confirmed. No Leonov note at 5.58.164 either (confirmed by absence). And earlier confirmed no Leonov notes at 13, 29, 89, 104, 108 verses' specific content (108 has a DIFFERENT partial overlap — let me double check 108).

Looking back: Leonov's own note at 5.58.108 says "В комментарии 'Тилака' уточняется, что Ситу убьют ракшаси" — this is about a DIFFERENT point (who will kill Sita) than the candidate note's claim (Bhūṣaṇa's pakṣa/māsa reading via the śruti citation). These are distinct facts on the same verse — non-trivial confirmed, no overlap.

Now let's write judge objects for the remaining 7 keep-verdict notes (13, 29, 89, 104, 108, 144, 164), plus the park verdict for 142 already done.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_58_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_58_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_58_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_58_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_58_candidates.json
Now note 5.58.144 (rāghavāṇāṃ variant):

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_58_candidates.json
Now note 5.58.164 (three categories of omens), the last one:

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_58_candidates.json
Now update `_meta` for sarga 58: 7 keep, 1 park.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_58_candidates.json
Let me verify the JSON validity for sarga 58 before moving on.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 58 done: 7 keep / 1 park. Now sarga 59 (3 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_59_candidates.json
- 🔧 `Grep` — "verse_id": "5\.59\.(5|24|29)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_59_segmented.json
Confirmed exactly: Bhūṣaṇa's text quotes exactly: "एतदेवोक्तं प्राक् 'असन्देशात्तु रामस्य तपसश्चानुपालनात्। न त्वां कुर्मि दशग्रीव भस्म भस्मार्ह तेजसा।।' इति" = "This was already said earlier: 'Not by Rāma's command, nor for the preservation of [his] tapas, do I not turn you, worthy of being reduced to ashes, into ash with my splendor, O Daśagrīva'" — this exactly matches the note's cited earlier speech (quoted almost verbatim in the note's Russian rendering). The reasoning ("क्रोधकलुषीकृतेति वचनाद्भर्तृमुखेन वैरनिर्यातनं वीरपत्नीधर्मः। अन्यथा महालाघवं भर्तुः...तादृक्क्रोधाकरणाद्रावणो जीवतीति गम्यते" — "from the word 'krodhakaluṣīkṛtā' it follows that vengeance-taking through the husband is the hero's-wife's duty; otherwise it would greatly demean the husband...it is understood that Rāvaṇa lives because that anger was not exercised [i.e. Hanuman's restraint, not weakness]") matches the note's claim about deliberate self-restraint exactly. Faithful confirmed. Anchoring: bhusana matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_59_segmented.json
Confirmed exactly: Tilaka's text "पौलोमीव नहुषरुद्धा पौलोमीव" — "pauliomī, as when detained/impeded by Nahuṣa" — matches note's claim (Nahuṣa's molestation of Śacī). Faithful confirmed. Anchoring: tilaka matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_59_segmented.json
Confirmed exactly: Siromani's text — "नियतः समुदाचारः...यद्यस्माद्दशग्रीवं न हन्ति तस्माद्दशाननो महात्मा प्रतीयते इति शेषः, एतेन रावणो मृतप्राय एवेति सूचितम्। अत एव रामः तस्य रावणस्य वधे निमित्तमात्रं भविष्यति" = "since [her] steadfast conduct is such that she does not [herself] slay Daśagrīva, it is understood that Daśagrīva is thereby already as good as dead; therefore Rāma will be merely the instrumental cause (nimitta-mātra) in his slaying" — matches the note's claim exactly, including the precise term "nimitta-mātra." Faithful confirmed. Anchoring: siromani matches_verse=true(2).

Let me check baselines for non-triviality (Phase-1 note at 5.59.24 mentioned in the note's `why_proposed`).

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
Confirmed — Phase-1's note is purely lexical/patronymic, not about the Nahuṣa myth. No Leonov own notes for verses 5, 24, or 29. Non-trivial confirmed for all three.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_59_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_59_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_59_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_59_candidates.json
Sarga 59 done: 3 keep. Now sarga 60 (4 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_60_candidates.json
- 🔧 `Grep` — "verse_id": "5\.60\.(14|16|17|20)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_60_segmented.json
Confirmed exactly for note 5.60.14: Tilaka's cited text: "अथ जाम्बवानङ्गदक्रोधपरिहाराय तन्मतं बहुमान्य सुहृद्भावेन निवर्तयति-- न तावदिति। हे राजपुत्र यथा भवान्पश्यति विचारयति एषा मतिर्नो ऽस्माकमक्षमा न, किंतु युक्तैव" = "Then, in order to avoid Angada's anger, Jāmbavān honors [Angada's] plan and, out of friendly disposition, redirects it, saying 'na tāvat...'; [as if to say:] 'O prince, as you see/consider it, this thought is not incapable/wrong for us, in fact it is right'" — this exactly matches the note's claim about the rhetorical strategy (approval first, then friendly-not-authoritative redirect). Faithful confirmed. Anchoring: tilaka matches_verse=true(2). Note the "n tāvat..." quote actually refers to v.20's opening — but this text is physically located within v.14's own bundle, which is where the note is filed correctly.

Confirmed for note 5.60.16: Siromani's cited text: "कथंचित् अस्माभिर्निर्जितां रावणनिर्जयेनानीतां सीतां...व्यपदिशन् कथयन् सन् राघवः कथंचिन्नाभिरोचयन्" — matches the note's claim about behavior merely conforming to the spirit vs. exact letter of the order not satisfying Rāma. Faithful confirmed. Anchoring: siromani matches_verse=true(2).

Confirmed for note 5.60.17: Siromani's cited text: "प्रतिज्ञाय मिथ्या कथं करिष्यति न करिष्यतीत्यर्थः, अतः तस्य रामस्य तुष्टिर्न भवेत्...अतः कृतमपि कर्म विफलं भवेत्" — matches the note's claim about Rāma's public vow being undermined. Faithful confirmed. Anchoring: siromani matches_verse=true(2).

Now note 5.60.20 (Bhūṣaṇa) — let me check that specifically, since the bundle shown above shows siromani's chunk at v.20, not bhusana's.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_60_segmented.json
Confirmed exactly: Bhūṣaṇa's cited text: "यद्यपि सम्यगुक्तं समर्थैश्चापि रामाज्ञानुसारेण कर्तव्यम् न स्वातन्त्र्येणेत्यर्थः" = "Even though [Angada's plan] is correctly stated, and even by capable [agents], [action] must be done according to Rāma's command, not through independent will (svātantrya)" — matches the note's claim exactly, including the exact term "svātantrya" ("сватантрья" in the note). Faithful confirmed. Anchoring: bhusana matches_verse=true(2).

Let me check baselines quickly.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
No overlapping content — the note about `dhīmatā` is unrelated (a different lexical point). Non-trivial confirmed for all four. Now write judge objects.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_60_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_60_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_60_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_60_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_60_candidates.json
Sarga 60 done: 4 keep. Now sarga 61, which has zero notes — quick.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_61_candidates.json
No notes to judge — just update `_meta`.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_61_candidates.json
Sarga 61 done: 0 notes, judged. Now sarga 62 (1 note).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_62_candidates.json
- 🔧 `Grep` — "verse_id": "5\.62\.32"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_62_segmented.json
Confirmed exactly: Bhūṣaṇa's cited text ends with a terse one-word gloss: "गतायुष इत्यधिक्षेपवचनम्" = "gatāyuṣaḥ iti adhikṣepavacanam" — "'gatāyuṣaḥ' is a word of reproach/abuse (adhikṣepa-vacanam)." This matches the note's claim exactly, including the precise term "adhikṣepa-vacana." Faithful confirmed. Anchoring: bhusana matches_verse=true(2).

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
No Leonov own note at v.32. Non-trivial confirmed.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_62_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_62_candidates.json
Sarga 62 done: 1 keep. Now sarga 63 (2 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_63_candidates.json
- 🔧 `Grep` — "verse_id": "5\.63\.(29|33)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_63_segmented.json
Found Siromani's text: "सुग्रीवः शोभनग्रीवाविशिष्टः सुग्रीवस्तु वनपालं पुनः प्रत्यभाषत" = "sugrīvaḥ = śobhanagrīva-viśiṣṭaḥ, sugrīva then answered the forest-keeper again" — this partially confirms the etymology claim (śobhanagrīva = "beautiful-necked"), but I don't see an explicit statement here about avoiding "punarukti" (repetition) as the note claims. Let me check the Bhūṣaṇa text too — I see Bhūṣaṇa's chunk doesn't mention the etymology at all, just repeats the verse text. Let me search more broadly for "śobhanagrīva" and "punarukti" nearby.

- 🔧 `Grep` — śobhanagrīva|शोभनग्रीव|punarukti|पौनरुक्त्य
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_63_segmented.json
Now I found the full, exact confirmation. Bhūṣaṇa's cited text (physically in v.28's bundle, since v.28's verse text mentions "sugrīvavadanāc" and this is where the second occurrence of "sugrīva" — which actually spans v.28's own text plus part of v.29 — is discussed): "श्रुत्वेति। द्वितीयसुग्रीवशब्दस्य शोभनग्रीव इत्यवयवार्थो विवक्षितः। क्रियाभेदेनापुनरुक्तिर्वा" = "śrutvā iti: for the second occurrence of the word 'sugrīva', the etymological/component sense 'śobhanagrīva' (beautiful-necked) is intended; or [alternatively,] because the action [verb] differs, it is not a mere repetition (apunaruktiḥ)." This exactly and precisely confirms the note's claim, including the "punarukti" avoidance point.

Also Tilaka at v.27: "एकः सुग्रीवशब्दः शोभनग्रीवपरः" = "one [occurrence] of the word 'sugrīva' refers to śobhanagrīva" — a third, independent corroboration of the same etymological reading (though attributed to Tilaka here, not cited in the note's source_commentary list which only lists bhusana+siromani). And Siromani's own text at v.29: "सुग्रीवः शोभनग्रीवाविशिष्टः" — matches too. 

So the note's claim is fully faithful — verified across three commentators (though only two are cited in `source_commentary`), and the "punarukti avoidance" reasoning is verified precisely in Bhūṣaṇa's text (physically located mostly at v.28's bundle, adjacent to v.29 where the note is filed — this is essentially correct placement since the "second occurrence" discussed spans the v.28/29 boundary). Anchoring: siromani matches_verse=true(2) at v.29 itself; bhusana's key etymology text is at v.28 (adjacent), with v.29's own bhusana chunk only content-anchored (containment 0.273). I'll score anchoring=1 given the primary bhusana evidence sits one verse over.

Now check note 5.63.33 (saṃprahṛṣṭa).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_63_segmented.json
Confirmed exactly: Bhūṣaṇa's cited text: "संप्रहृष्टौ, रोमस्विति शेषः। हृषितरोमाणावित्यर्थः। 'हृषेर्लोमसु' इति विकल्पादिडभावः। एवम् अङ्गैः संहृष्टैरित्यत्रापि द्रष्टव्यम्" = "saṃprahṛṣṭau [means] 'romasu' (regarding the body-hairs) is understood; the meaning is 'with body-hairs standing on end (hṛṣitaromāṇau)'; per the grammatical rule 'hṛṣeḥ lomasu' (the root hṛṣ pertains to body-hairs)...the same should be understood for 'aṅgaiḥ saṃhṛṣṭaiḥ' [later in the verse]." This matches the note's claim precisely and faithfully, including the exact grammatical rule citation ("hṛṣeḥ lomasu") and the point that the "trembling of limbs" phrase describes the same phenomenon. Faithful confirmed. Anchoring: bhusana matches_verse=true(2).

Let's check baselines for non-triviality.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
No Leonov own notes at any of these verses. Non-trivial confirmed. Now write judge objects.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_63_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_63_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_63_candidates.json
Sarga 63 done: 2 keep. Now sarga 64 (2 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_64_candidates.json
- 🔧 `Grep` — "verse_id": "5\.64\.(4|31)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_64_segmented.json
Confirmed exactly, an impressively precise match: Bhūṣaṇa's cited text: "विमदानित्यत्र हेतुमाह मेहमानामिति। मेहमानान् मेहयतः, मूत्रयत इत्यर्थः। एतेन मूत्रणान्मधूनि जीर्णानीति गम्यते। अत एव विमदत्वम्... तदाह बाहटः 'अनुपानं हिमं वारि यवगोधूमयोर्हितम्। दध्नि मद्ये बिसे क्षौद्रे कोष्णं पिष्टमयेषु च।।' इति" = "As the reason for 'vimadān' [de-intoxicated], he says 'mehamānān' [urinating]: meaning, they are urinating out [the honey], i.e., through urination the honey is digested/expelled — hence their de-intoxication...Bāhaṭa (Vāhaṭa) states: 'The anupāna [accompanying drink] is: cold water suits barley and wheat; sour milk suits wine; [with] lotus-stem/honey, lukewarm water; and with flour-preparations...'" — this matches the note's claim exactly, including the precise author name (Bāhaṭa/Vāhaṭa) and the anupāna formula. Faithful confirmed. Anchoring: bhusana matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_64_segmented.json
Confirmed exactly: Bhūṣaṇa's cited text: "पित्रा ब्रह्मणा ऋक्षरजसे दत्तम्" = "given by the father, Brahmā, to Ṛkṣarajas" — matches the note's claim exactly (Brahmā as donor, Ṛkṣarajas as first recipient). Faithful confirmed. Anchoring: bhusana matches_verse=true(2).

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
Let me check the fuller Leonov note for v.4 to make sure there's no overlap with the Vāhaṭa citation.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
Confirmed no overlap — Leonov's note is only the literal gloss "urinating honey-water", without the Vāhaṭa/anupāna causal explanation. Non-trivial confirmed for both notes.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_64_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_64_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_64_candidates.json
Sarga 64 done: 2 keep. Now sarga 65 (4 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_65_candidates.json
- 🔧 `Grep` — "verse_id": "5\.65\.(5|20|25|28)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_65_segmented.json
Confirmed exactly: Siromani's cited text: "इत्युक्त्या द्रुतस्वकर्तृकरावणवधाभावजनितसीतामर्षविषयकसंभावना सूचिता" = "by this expression [kathaṃ ca mayi vartate], the possibility of Sītā's resentment (amarṣa), born from the fact that he [Rāma] has not yet quickly slain Rāvaṇa, is indicated (sūcitā)" — matches the note's claim precisely (hidden anxiety about Sita possibly resenting him for not yet killing Ravana). Faithful confirmed. Anchoring: siromani matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_65_segmented.json
Confirmed exactly: Siromani's cited text: "चित्रकूटे वायसं जयन्तं प्रति तवान्तिके यद्वृत्तं" = "regarding the crow named Jayanta at Citrakūṭa, what happened in your presence" — matches the note's claim exactly (the crow's name is Jayanta, Indra's son). Faithful confirmed. Anchoring: siromani matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_65_segmented.json
Confirmed exactly for note 5.65.25: Bhūṣaṇa's text (physically in v.25's own bundle, though referring to v.26's content): "मृगीवोत्फुल्ललोचना, त्रासातिशयादिति भावः" = "'mṛgīvotphullalocanā' — the meaning is due to extreme fear (trāsātiśayāt)" — matches the note's claim exactly. Faithful confirmed. Anchoring: this exact text I found is under v.25's bhusana chunk in the bundle, but the pratika_check for v.25 shows only siromani listed (matches_verse: true), no bhusana pratika_check entry present despite bhusana having a commentary chunk there. Let me check this more carefully — the `commentary` dict at v.25 does list `bhusana`, but `pratika_check` only lists `siromani`. This means Bhūṣaṇa's chunk wasn't checked/verified by the segmenter's pratīka algorithm (likely because it's a short remark without a clear pratīka opening). I'll score anchoring=1 (unverified by automated check, though I've manually confirmed the content is exactly there).

Confirmed for note 5.65.28: Bhūṣaṇa's cited text: "स्ववृत्तान्तं सर्वमाख्यातवानिति सामान्येन वक्तुं युक्तत्वे ऽप्यङ्गदसन्निधौ प्रपञ्चनं गोप्यविशेषगोपनार्थम्। अत्र त्वप्रपञ्चनम् अकथनीयाकथनार्थं चेति ज्ञेयम्" = "though it would be proper to state in general terms that he related his own account in full, before Aṅgada the elaboration [was limited] for the purpose of concealing certain things not to be disclosed (gopyaviśeṣagopanārtham); here [before Rāma], however, the non-elaboration [earlier] should be understood as being for the purpose of not saying what should not be said" — this is a bit more nuanced than the note's phrasing but substantively matches: the earlier telling (to Angada) was abbreviated deliberately to conceal certain things, while here (to Rama) it's told "anupūrvyāt sampūrṇam" (in full, complete order) — matching the note's core claim about deliberate narrative differentiation. Faithful confirmed (2). Anchoring: bhusana matches_verse=true(2).

Let me check baselines.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
Interesting — Leonov's own note at 5.65.5 ALREADY cites Siromani, but only for a *different, narrower* clause: "с каким чувством" (kena bhāvena, i.e., "with what feeling"), not the full "amarṣa" (resentment) inference the candidate note reports. Let me re-verify by re-reading the exact Siromani text once more to check whether the note's phrasing is a genuine addition beyond what Leonov's own note already extracted.

Looking back at the Siromani text: "क्केति। सीता क्क वर्तते मयि कथं केन भावेन वर्त्तते वैदेहीं प्रति वैदेहीसंबन्धि एतत्सर्वं यूयमाख्यातं केन भावेन इत्युक्त्या द्रुतस्वकर्तृकरावणवधाभावजनितसीतामर्षविषयकसंभावना सूचिता" — Leonov's note extracts only the first clause ("kathaṃ = kena bhāvena," = "with what feeling"), while the candidate note extracts the SECOND clause of the SAME continuous commentary passage — the "amarṣa" (resentment) inference that follows. This is a real, distinct addition, not a duplicate — Leonov's own note stops short of the psychological inference the candidate note supplies. Non-trivial confirmed, genuinely non-overlapping content within the same commentary block.

For 5.65.20: confirmed exactly matching Kostina's own flagged gap ("нужна ссылка на соответствующий стих" — needs a reference to the corresponding verse) — the candidate note supplies exactly the missing specific (the crow's name, Jayanta).

No Leonov notes for 25 or 28. Non-trivial confirmed for all four.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_65_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_65_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_65_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_65_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_65_candidates.json
Sarga 65 done: 4 keep. Now sarga 66 (2 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_66_candidates.json
- 🔧 `Grep` — "verse_id": "5\.66\.(4|12)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_66_segmented.json
Confirmed exactly: Tilaka's cited text: "मे श्वशुरेण जनकेन वधूकाले वधूत्वसंपादके काले विवाहकाले वैदेह्याः शिरोभूषणाय सीतामातृहस्ताद्गृहीत्वा दशरथहस्ते दत्तम्" = "given by my father-in-law Janaka, at the time of [her] becoming a bride, i.e., at the wedding time, for Vaidehī's head-ornament (śirobhūṣaṇāya), taken from the hand of Sītā's mother and given into Daśaratha's hand" — matches the note's claim exactly, including "śirobhūṣaṇa" (head-ornament) and the detail about Sita's mother's hand. Faithful confirmed. Anchoring: tilaka matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_66_segmented.json
Confirmed exactly: Bhūṣaṇa's cited text: "तत्त्वतः, सङ्कोचेन न किंचित् गोपनीयमिति भावः" = "tattvataḥ [truly] — the meaning is: nothing should be concealed (gopanīyam) out of reticence/shyness (saṅkocena)" — matches the note's claim exactly (though this text is physically attached to v.13's marker range "5.66.12,13" within v.12's own bundle — actually it's directly within v.12's bhusana field, so this is anchored correctly at v.12 itself). Faithful confirmed. Anchoring: bhusana matches_verse=true(2).

Let's check baselines.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
Confirmed — Kostina's own note exactly raises the doubt about the translation "заколка" (hairpin) that the candidate note claims Tilaka's "śirobhūṣaṇam" resolves. No Leonov note for v.12. Non-trivial confirmed for both.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_66_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_66_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_66_candidates.json
Sarga 66 done: 2 keep. Now sarga 67 (4 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_67_candidates.json
- 🔧 `Grep` — "verse_id": "5\.67\.(3|16|26|30)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_67_segmented.json
Confirmed exactly: Bhūṣaṇa's cited text: "उभावपि पर्यायेण सुप्ताविति त्वया सार्धमित्युक्तम्" = "both slept in turns (paryāyeṇa); this is what is meant by 'tvayā sārdham' [together with you]" — confirms the note's claim precisely (paryāyeṇa = alternating turns, reconciling "slept together" with "woke first"). Faithful confirmed. Anchoring: bhusana matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_67_segmented.json
Confirmed exactly: Tilaka's cited text: "परिपालयः पर्यपालयः। शरीरावधेनेति भावः। इत्येवेति हेतोः" = "paripālayaḥ = paryapālayaḥ [protected]; the meaning is: through non-slaying of the body (śarīrāvadhena); ['ity eva' is] the reason [given for the following]" — matches the note's claim exactly (sparing only the body, while the astra's action still had to proceed). Faithful confirmed. Anchoring: tilaka matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_67_segmented.json
Confirmed exactly: Tilaka's cited text: "चिरं लङ्कायामासितुं न कालो योग्य इति पाठान्तरे ऽर्थः" = "in the variant reading (pāṭhāntare), the meaning is: 'this is not the time to remain long in Lanka'" — matches the note's claim exactly, including the exact variant text quote (ciraṃ laṅkāyām āsituṃ na kālaḥ). Faithful confirmed. Anchoring: tilaka matches_verse=true(2).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_67_segmented.json
I don't see the specific "checking for rākṣasī surveillance" reasoning attributed to Bhūṣaṇa in v.30's own bundle — only Tilaka is present there. The note itself explicitly discloses the segmenter attached this to a merged-range marker at "5.67.3138" (colophon + V.30/V.31 discussion). Let me check that merged-range bundle.

- 🔧 `Grep` — "verse_id": "5\.67\.3138"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_67_segmented.json
Confirmed exactly: Bhūṣaṇa's cited text (in the merged-range marker, colophon block): "सा ऽभिवीक्ष्य दिश इति। दिगवलोकनं राक्षस्यो दृष्ट्वा रावणाय वक्ष्यन्तीति भयेन" = "'sā 'bhivīkṣya diśaḥ' — the looking-around-at-directions was due to fear that the rākṣasīs, seeing [her], would report it to Rāvaṇa" — this matches the note's claim exactly and faithfully (checking for surveillance, out of fear of being reported to Rāvaṇa). Faithful confirmed. The note's own `why_proposed` explicitly discloses this anchoring situation, noting the merged-range marker but correctly identifying that the text quotes "sā 'bhivīkṣya diśaḥ" (v.30's own opening words) — this is a genuine, verifiable case, though the segmenter classified the whole chunk as `ambiguous_marker: true` since it spans the colophon + verse discussion. Faithful confirmed (2). Anchoring: since this content sits in a merged/ambiguous-marker bundle rather than v.30's own clean bundle, I'll score anchoring=1 (unverified by clean pratika_check, but manually located and unambiguous — the pratīka literally opens with the verse's exact words).

Let me check baselines for non-triviality.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
No overlap in content — Kostina's note discusses only the lexical "заколка" translation. Non-trivial confirmed for all four notes.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_67_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_67_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_67_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_67_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_67_candidates.json
Sarga 67 done: 4 keep. Now sarga 68, the last one (2 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_68_candidates.json
- 🔧 `Grep` — "verse_id": "5\.68\.(12|23)"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_68_segmented.json
Confirmed exactly. Tilaka's cited text at v.11: "यद्यपि त्वमेव पर्याप्तः। सकलराक्षसवधपूर्वं मन्मोचन इति शेषः। तथापीदृशो बलोदयस्तवैव यशस्यो यशोवर्धकः स्यात्" = "although you alone are sufficient... nevertheless such an exploit would bring fame only to you" — and at v.12: "यदि तु रामो रावणं हत्वा मां नयेत्, तदा तन्नयनं तस्य यशस्करं स्यात्। अतस्तेनैवागत्य मोचनं युक्तमिति भावः" = "But if Rāma, having slain Rāvaṇa, leads me away, then that leading-out would be fame-bringing for HIM; therefore it is proper that he himself come and effect the release — this is the sense." This matches the note's claim precisely and faithfully, quoting the exact terms cited in the note ("tenaiva āgatya mocanam yuktam"). Faithful confirmed. Anchoring: tilaka matches_verse=true(2) at v.12 (and v.11 too, though the note is filed at v.12).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_68_segmented.json
I don't see the "manyu = dainyam" + Amarakośa reasoning in v.23's own bundle — only a bare verse-text repetition. Let me check the merged-range marker "5.68.2328" mentioned in the rejects, which the note's own justification claims holds this content.

- 🔧 `Grep` — "verse_id": "5\.68\.2328"
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_68_segmented.json
Confirmed exactly: Tilaka's cited text: "मन्युर्दैन्यम्" = "manyu = dainya" (grief/dejection). Bhūṣaṇa's cited text: "तदलमिति। मन्युः दैन्यम्। 'मन्युर्दैन्ये क्रतौ क्रुधि' इत्यमरः" = "tad alam iti — manyu = dainya; per Amara[kośa]: 'manyur dainye kratau krudhi' [manyu means dejection, resolve, or anger (in different contexts)]" — this matches the note's claim exactly, including the precise Amarakośa citation quoted verbatim in the note. Faithful confirmed. This chunk sits in a merged-range marker bundle (`ambiguous_marker: true`) rather than v.23's own clean bundle — the note is filed at v.23, but the pratīka anchor here isn't verified by the automated check (no pratika_check field at all for this merged-range entry). I'll score anchoring=1 (unverified but manually confirmed, no suggest_verse contradicting it).

Let's check baselines for non-triviality.

- 🔧 `Bash` — export PYTHONIOENCODING=utf-8 && python -c "
No overlap — Leonov's own notes are about formulaic repetition parallels (V.39), not the diplomatic-logic (11.12) or manyu-lexicography (23) points the candidate notes make. Non-trivial confirmed for both.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_68_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_68_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_68_candidates.json
All 22 sargas are now judged. Let me do a final comprehensive validation pass across all files to confirm JSON validity and completeness.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && f
All 22 files are valid JSON, fully judged, with `_meta.judged: true` and verdict counts recorded. Let me also do a spot check that no `rejected` arrays or drafter fields were touched, and confirm UTF-8/no-BOM encoding on a couple of files.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && f
No BOM. Note sarga 58 shows `\r\n` line endings (0d0a) which is fine since that's just how Edit preserved the existing file's line endings, not a UTF-8 issue.

## Summary

Judged all 70 notes across the 22 assigned sargas per the JUDGE_BRIEF.md rubric (faithfulness/non-triviality/contrastive_value/register/anchoring, 0–2 each, gates as specified). For every note I located the cited commentator's actual Devanagari text in the segmented bundle (including several deliberately-disclosed marker-shift cross-checks, e.g. sarga 46 v.11, sarga 53 vv.5/33, sarga 58 v.95, sarga 65 v.25, sarga 67 v.30, sarga 68 v.23) and checked it against `data/leonov_own_notes.json` + `data/sundara_commentary_to_add.json` for the given sarga before scoring non-triviality. All `judge` objects were added in place; no drafter fields, rejects, or array order were touched.

One-line-per-sarga results:

- sarga 46 judged: 7 notes → keep 7 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 47 judged: 5 notes → keep 5 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 48 judged: 5 notes → keep 5 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 49 judged: 3 notes → keep 3 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 50 judged: 2 notes → keep 2 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 52 judged: 1 notes → keep 1 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 53 judged: 2 notes → keep 2 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 54 judged: 4 notes → keep 4 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 55 judged: 1 notes → keep 1 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 56 judged: 5 notes → keep 5 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 57 judged: 3 notes → keep 3 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 58 judged: 8 notes → keep 7 / edit 0 / park 1 / reject 0 / flag_anchor 0 (5.58.142 parked: its Tilaka adharma-of-war reasoning duplicates Leonov's own note on the same verse almost word-for-word — non-triviality gate failed)
- sarga 59 judged: 3 notes → keep 3 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 60 judged: 4 notes → keep 4 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 61 judged: 0 notes → keep 0 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 62 judged: 1 notes → keep 1 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 63 judged: 2 notes → keep 2 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 64 judged: 2 notes → keep 2 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 65 judged: 4 notes → keep 4 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 66 judged: 2 notes → keep 2 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 67 judged: 4 notes → keep 4 / edit 0 / park 0 / reject 0 / flag_anchor 0
- sarga 68 judged: 2 notes → keep 2 / edit 0 / park 0 / reject 0 / flag_anchor 0

Totals: 69 keep / 1 park / 0 edit / 0 reject / 0 flag_anchor across 70 notes in 22 files.

_Dr. Mārcis Gasūns_
