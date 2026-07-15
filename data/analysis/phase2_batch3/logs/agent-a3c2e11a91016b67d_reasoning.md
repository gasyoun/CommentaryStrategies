# Agent log agent-a3c2e11a91016b67d

_Model: `claude-sonnet-5`; extracted by scripts/export_agent_logs.py; raw transcript alongside (.jsonl) holds the full record incl. tool results._


I'll start by reading the drafting brief and then the input files for my assigned sargas.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\DRAFTING_BRIEF.md
Now let me check the docs/PHASE2_METHOD.md for the full contrastive-first style contract, then load the data files.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\docs\PHASE2_METHOD.md
Now let me look at existing example outputs from a prior batch to calibrate the exact style, then check the input files.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && l
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch2\sarga_22_candidates.json
Good, I have a solid calibration example. Now let's look for a contrastive example from batch2 or elsewhere, and check the structure of sarga 17's segmented file.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && g
No contrastive examples exist yet in prior batches — this batch introduces that. Let me check the segmented file structure for sarga 17.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
I need to write output to a file to avoid console encoding issues. Let me write a script that dumps data to scratch files.

- 🔧 `Bash` — mkdir -p "C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-
- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\dump_sarga.py
This is a new file, no need to Read first — that error is odd. Let me retry (likely a stale path check false positive; the file didn't exist before).

- 🔧 `Bash` — ls "C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9
- 🔧 `Bash` — ls -la "/c/Users/user/AppData/Local/Temp/claude/C--Users-user-Documents-GitHub/3c92a91d-16fd-4adf-ab
There's already a `dump_sarga.py` from a concurrent/prior agent working other sargas in this same batch (17, 18, 19 are mine; others clearly done 1-16 by other parallel agents). I'll use a uniquely-named script to avoid collision, and use the existing `slice_sarga.py`/`dump_sarga.py` pattern as inspiration but write my own uniquely named files.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\slice_sarga.py
This confirms the data structure. Now let me write my own script for sargas 17/18/19 using distinctive filenames to avoid collisions with the concurrent agents.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\slice_171819.py
This is a small scratch data-slicing script adapted directly from the existing `slice_sarga.py` pattern already in this scratchpad (written by a concurrent agent for the same batch) — not a reinvention, just a straightforward reuse of the same slicing logic for my three assigned sargas. Proceeding.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\p2b3_report_17.txt
Confirms no Tilaka in sarga 17, as noted in the brief. Now let's read the actual verse content for sarga 17.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\p2b3_verses_17.json
Now let's look at the Leonov own notes and Phase-1 notes for sarga 17.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\p2b3_leonov_17.json
Interesting — Leonov's own note for 5.17.5 and 5.17.8 already cite Tilaka (via Goldman's citations), even though our commentary bundle doesn't have Tilaka text for sarga 17. Let me check the Phase-1 notes too.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\p2b3_tier2_17.json
Now I have a full picture for sarga 17. Let me analyze verse by verse.

**Sarga 17 analysis (37 verses, only bhusana + siromani, no tilaka, no tattvadipika):**

- **5.17.1**: bhusana just restates verse text; siromani says Hanuman is the subject viewing this ("hanumatkartrkaspastadarsanam varnayitum aha") — a syntactic framing note, no new content. Reject.
- **5.17.2**: bhusana restates; siromani restates paraphrase. Reject.
- **5.17.3**: bhusana has a long note about "anāsā atināsāśca..." (seems to be misplaced text about verse 5 topics — actually a chunk of content that belongs near v.5, likely marker offset) then restates v.3. Siromani identifies "sa" = Hanuman, and śokabhāraiḥ nyastām = "as if overwhelmed," bhāraiḥ nyastā nāvam iva = "like a laden ship" — states the simile straightforwardly, restates подстrochnik. Reject — restates.
- **5.17.4**: both restate. Reject.
- **5.17.5**: bhusana restates; siromani is mostly a restatement/paraphrase of the composite descriptions (karṇaprāvaraṇa etc — but this content appears to belong to v.5 per Leonov's own note which already extensively covers this verse with Tilaka/Bhushana/Siromani/Tattvadipika readings). Wait — check: Leonov's own note at 5.17.5 already discusses karṇaprāvaraṇā via Tilaka/Bhushana/Siromani citations. Our bundle's siromani text for v.5 is a general descriptive paraphrase, not matching what Leonov cites. Let me check if content differs — need care. Since Leonov's own note already extensively treats this verse citing all commentators (even ones not in our JSON bundle for this sarga), any note we add duplicates tier-1. Reject as duplicate.

Let me look more carefully at verse 46, which seems to actually be content for verse 5 (karṇaprāvaraṇā gloss) misplaced at "5.17.46" per the marker.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
I already have that content read above (5.17.46 — pratika "didṛkṣamāṇa ityādi" — this is bhusana explicating v.4-5's karṇaprāvaraṇā/śaṅkukarṇā/mastakocchvāsanāsikā compounds). The verse itself has no sanskrit_iast/leonov_ru — a merged/orphan marker essentially attached beyond the sarga's real verse count (37 verses but sarga only goes to v.32 canonically, so "46" is clearly a marker artifact). This is a data-misalignment/no independent verse — reject with reason.

Let me now systematically go through all 37 bundles with full judgment. Let me re-check verses I haven't fully examined (9, 617/618 range covered already). Let me write my full verse-by-verse decision now.

**Verse-by-verse decisions:**

1. **5.17.1** — bhusana restates verse; siromani frames "Hanuman is the one seeing clearly" (hanumatkartrkaspastadarsanam) — this is a syntactic/discourse marker (who is the subject of dadarśa-type framing), not exegetical content. Reject: restates подстрочник / pure syntactic framing.

2. **5.17.2** — both restate. Reject.

3. **5.17.3** — bhusana's note actually contains material that belongs to v.5 area (anāsā/atinasā... description of ear-types) — likely marker offset; the part that's genuinely on v.3 restates подстрочник (śokabhāraiḥ nyastām = as if burdened with grief, like a laden ship). Siromani identifies "sa" = Hanuman explicitly (subject clarification) — minor. Reject: restates подстрочник; syntactic subject clarification not independently valuable.

4. **5.17.4** — both restate. Reject.

5. **5.17.5** — Leonov's own note ALREADY extensively covers this exact verse (karṇaprāvaraṇā via Tilaka/Bhūṣaṇa/Śiromaṇi, cites Goldman). Our bundle's siromani text is just descriptive paraphrase of the whole verse's monster-features (not focused on karṇaprāvaraṇā uniquely) — duplicates tier-1 already-rich treatment. Reject: duplicates Leonov's own note.

6. **5.17.6** — bhusana only, restates verse. Reject.

7. **5.17.7** — bhusana glosses compound: ध्वस्तकेशीं = "having sparse hair," अकेशीम् = "hairless," केशकम्बलधारिणीं = "wearing hair as a blanket," लम्बकर्णललाटां = "ears+forehead hanging" — this IS exegetical content beyond подстрочник (подстрочник gives literal "with disheveled hair," etc., but doesn't explain "hairless yet hair as blanket" paradox). Let me reconsider — check original подстрочник for v.6/7.

Let me re-examine v.6-9 carefully since bhusana's gloss under 5.17.7 actually explains terms from v.6.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\p2b3_17_lines.txt
Now I have the full picture. This is the famous rakṣasī catalogue — a long list of grotesque physical features already well-rendered by подстрочник. The bhusana note under 5.17.7 does gloss "ध्वस्तकेशीं स्वल्पकेशीं। अकेशीम् अनुत्पन्नकेशीम्। केशकम्बलधारिणीं कम्बलरूपकेशधारिणीम्" — this actually applies to v.6's terms (dhvastakeśīṃ, akeśīṃ, keśakambaladhāriṇīm), aligned oddly under v.7's marker (offset). Let me check: is this exegetically valuable beyond подстрочник?

- **dhvastakeśī** = "having sparse hair" (svalpakeśī) — подстрочник says "растрёпанные волосы" (disheveled hair), close enough, restates.
- **akeśī** = "having no hair born" (anutpannakeśī) — подстрочник says "безволосых" — matches literally.
- **keśakambaladhāriṇī** = "wearing hair as a blanket" — подстрочник says "одетых [только] волосами" — matches.

This is grammar-level restatement, no new content. Reject.

Let me check verse 9's long bhusana note more carefully — it explains compounds for v.8-9 and also introduces new content: "гजोष्ट्रहयपादीश्च निखातशिरसो ऽपराः" mentioning "nikhātaśirasaḥ" (heads sunk into torso) which parallels Leonov's own note at verse 10 about Kabandha.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\v9_full.txt
This confirms — the note about `nikhātaśiraḥ` ("heads sunk into the torso" = gātrāntarvartiśiraḥ, "head situated inside the body") is actually the content that belongs to the next unaligned verse (Leonov's own note at v.10 already covers this exact term with the Kabandha parallel, citing "nikhātaśirasaḥ"). This confirms it's a duplicate of Leonov's own v.10 note (which is richer — cites Kabandha from Book III). Also note: "एता एकाक्ष्यादि राक्षसीभ्यो ऽन्याः" — bhusana clarifies these rakshasis (vikṛtāḥ etc.) are *different* rakshasis from the "ekākṣī" group of v.5. This is a minor textual/structural point but arguably useful — distinguishing between two groups of monstrous guards rather than one continuous list. Let me check if this is worth drafting.

This "separate group" clarification is genuinely useful — without it a reader might think it's the same continuous description. But is it visible/valuable for the Russian reader of a translated verse? It affects how one reads the whole catalogue (as multiple distinct guard-groups, not one). However this is somewhat marginal — a scholarly nicety about a poetic list-structure, not a "reading that changes the image." I'll lean reject as it doesn't change interpretation meaningfully; the подстрочник already lists them as a plain sequence without implying unity, and Leonov's note at v.10 already covers the more valuable nikhātaśiraḥ point.

Now let's finalize decisions for all verses:

- **5.17.9**: Reject — grammatical syntax connectives (anvaya markers "ddarśety anena anvayaḥ") plus the nikhātaśiraḥ content duplicates Leonov's own note at v.10.
- **5.17.11–5.17.16**: bhusana restates each verse in Sanskrit paraphrase form (basically re-quoting/lightly rephrasing the verse itself). Reject all as restating подстрочник.
- **5.17.17**: bhusana restates verse, adds "skandhavantam upāsīnāḥ parivārya vanaspatim" — content of next verse (18) glued on. No new content. Reject.
- **5.17.18**: bhusana restates + glues v.19's text. Reject.
- **5.17.19**: bhusana restates. Siromani restates ("Hanuman perceived Sita distressed..."). Reject.
- **5.17.20**: bhusana glosses "चारित्रव्यपदेशाढ्यां" = famed for good conduct (pativratā-dharma observance-fame endowed) and "भर्तृदर्शनेन दुर्गतां दरिद्रां" = poor/wretched due to lack of husband's sight. This is a real gloss beyond подстрочник — подстрочник already says "Богатую славой добродетельного поведения, несчастную [желающую] встречи с мужем" which already captures this. Reject — restates.
- **5.17.21**: bhusana glosses "भर्तृवात्सल्यभूषणां वात्सल्यपदमत्र स्नेहमात्रवाचि" = the word vātsalya here means mere affection (not specifically parental-type tenderness). This is a real lexical nuance, but it's already covered by Phase-1 tier-2 note V.17.21 (bhartṛvātsalya). Reject — duplicates Phase-1.

Let me check verse 22, 25, 31-32 more closely for real commentary content.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
I already have v.22's full text from the earlier read. Let me recall it: bhusana glosses "क्लुष्टरूपामसंस्पर्शादयुक्तामिव वल्लकीम्" wait that's actually the content that belongs to v.23 (asaṃsparśād ayuktām iva vallakīm) — this is misaligned/glued content. Note: bhusana here (attached to v.22) explains "payodānte = varṣānte" (at the end of the rainy season) and "chandrarekhāyāḥ spaṣṭāspaṣṭatva-dyotanāya idaṃ viśeṣaṇam" — the epithet clarifies why the moon-crescent simile shows "clear/unclear" — i.e., the candrarekhā (crescent) simile's point is ambiguity (partly obscured by clouds = partly visible/invisible), paralleling Sita's own paradoxical "shines yet doesn't shine" state (as explicitly stated in v.25 "vibhāti ca na bhāti ca"). This is actually a meaningful literary-critical point: the crescent-behind-clouds image at v.22 sets up the vibhāti/na bhāti paradox that recurs explicitly at v.25. Worth considering as a note connecting the imagery across verses (narrative-function type observation, which M.G. valued per the register feedback).

Let me check: does подстрочник or Phase-1 already make this connection? Phase-1 has no entry for v.22. Leonov's own notes have none for v.22 either. This could be a legitimate single-commentator gloss under kazansky type Б (textological — reveals a poetic device linking two similes).

Let's check verse 25's siromani note too, which explicitly states "ardhadvayam ekānvayi" (the two half-verses form one syntactic unit) — that's grammar, skip. But the "vibhāti na vibhāti ca" paradox itself — is it already covered by подстрочник? Yes, подстрочник already renders it fully ("не сияет и все же сияет"). So the v.22 bhusana note's value is specifically in pointing out that the SAME paradox device is set up two verses earlier via the crescent-moon-behind-clouds simile — a cross-verse literary observation.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\v22_check.txt
Confirmed: bhūṣaṇa's note explicitly says "candrarekhāyāḥ spaṣṭāspaṣṭatva-dyotanāya idaṃ viśeṣaṇam" — "this epithet [śāradābhraiḥ ivāvṛtām, 'as if covered by autumn clouds'] serves to indicate the crescent's alternating clarity/unclarity [visible-yet-obscured]." This is a genuine literary-device point: the crescent-behind-clouds image is glossed by Bhūṣaṇa as specifically encoding an ambiguous visibility — the same "shines/doesn't shine" paradox that the poet states explicitly three verses later (v.25). This is worth a note (kazansky **Б**, narrative-function/poetic-device observation, valued per M.G.'s feedback).

Now let's finalize remaining verses: 25, 26, 28, 30, 31, 32, and the merged-range ones.

- **5.17.25**: siromani "ardhadvayam ekānvayi" — pure syntax. Reject (подстрочник already conveys the vibhāti/na-bhāti paradox).
- **5.17.26**: bhusana restates + glues v.27's text (tāṃ devīṃ dīnavadanām...). No new content beyond подстрочник. Reject.
- **5.17.28**: bhusana restates + glues v.29's text (dahantīm iva niḥśvāsair vṛkṣān pallavadhāriṇaḥ). No new content. Reject.
- **5.17.30**: bhusana restates. Reject.
- **5.17.31**: bhusana explains "hariṣajāni... namaścakre" — grammar point about accusative case usage with namaskaroti-type verbs ("upapadavibhaktyapekṣayā kārakavibhakter balīyastvān namaskaroti devān ityādāv iva dvitīyā") — pure Sanskrit grammar (case government), invisible/irrelevant to Russian reader. Siromani restates. Reject — pure grammar.
- **5.17.32**: bhusana notes "saṃvṛtaḥ rākṣasyadarśanāya śiṃśupāparṇaiḥ gūḍho'bhūt" = "concealed — hidden by śiṃśupā-tree leaves so as not to be seen by the rākṣasīs." Siromani: "saṃvṛtaḥ śākhāviśeṣe nilīno'bhavat" = "hid himself in a particular branch." This actually EXPLAINS what "остался скрытым" (saṃvṛtaḥ) means concretely — Hanuman hides specifically among the leaves of the śiṃśupā tree (the same tree under which Sita sits) to avoid being seen by the rākṣasī guards. Подстрочник just says "remained hidden" without specifying how/where/why. This is a genuine narrative-concretizing gloss — worth noting as kazansky Б (textological — supplies what "hidden" concretely means, sets up staging for the following dialogue scene).

Let's check Phase-1 tier2 note at V.17.32 (namaskāra, cross-text to BhG) — that's about namaskāra, not about saṃvṛtaḥ. So this is a different point, not a duplicate. Good — will draft.

Now the merged-range/no-independent-verse bundles (5.17.46, 618, 1112, 1315, 1617, 1819, 2024, 2324, 2627, 2830) — per brief, these are `ambiguous_marker: true` merged tokens with no independent gloss, and per reject discipline (e) must reject. Let me verify 5.17.46 also has `ambiguous_marker: false` per the data even though it has empty sanskrit_iast — check:

Looking back at the verse dump: `5.17.46` has `"ambiguous_marker": false` but empty `sanskrit_iast`/`leonov_ru` fields — it's an orphan marker (verse 46 doesn't exist in a 32-verse sarga), effectively a merged/misaligned fragment despite the flag. I'll treat it under reject reason (e)-equivalent: no independently attachable verse (content already covered — the didṛkṣamāṇa gloss duplicates what's under 5.17.4/5 already, and reused for v.5's compounds already in Leonov's own note).

Now let me write the sarga 17 output file.

- 🔧 `Write` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_17_candidates.json
I need to fix the reject count reconciliation — I have a stray "5.17.22-dup" entry that's not a real verse_id and duplicates the drafted note's verse. Let me fix this: remove that spurious entry and recount.

- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_17_candidates.json
Now let's verify: I need `notes_drafted + notes_rejected == verses_considered`. Let me count: 37 verse bundles total. 2 drafted (5.17.22, 5.17.32). Rejected list now should have 35 entries. Let me verify with a script.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 17 reconciles perfectly: 37 considered = 2 drafted + 35 rejected, all verse_ids match, no duplicates. Now let's move to sarga 18.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\p2b3_report_18.txt
Sarga 18 has Tilaka too. Let me read the verses, Leonov notes, and Phase-1 notes.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\p2b3_verses_18.json
Now let's check Leonov's own notes and Phase-1 notes for sarga 18.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\p2b3_leonov_18.json
This is a densely-annotated sarga. Leonov already covers verses 1, 2, 3, 6(kostina), 8, 12, 15(kostina), 16(kostina)×2, 19(kostina)×2, 21(kostina), 23, 24, 26(kostina), 27, 28(kostina + main), 32×2. Let me check the Phase-1 notes too.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\p2b3_tier2_18.json
Now I have both dedup baselines for sarga 18. Let me methodically go through all 41 bundles.

**Verse-by-verse for sarga 18:**

1. **5.18.1** — Tilaka: "kim cic cheṣā = only a small remaining watch left" + "vicinvataḥ = seeking the moment when the rākṣasīs sleep" (searching for an opportunity while they're asleep). Leonov's own note ALREADY cites Tilaka on this exact verse (three watches passed, 3-6am timing). Our bundle's Tilaka content is different — the *reason* for searching (waiting for rākṣasī sleep-opportunity), not the timing detail. Could this complement Leonov's note? Leonov's note is about timing precision; Tilaka's other point here (Hanuman was searching for the moment when the rākṣasī guards would be asleep, i.e., an opportune moment) is somewhat implied by подстрочник already ("остался лишь остаток ночи" while seeking Sita) but doesn't explicitly say "waiting for the guards to sleep." Actually looking again — bhusana/siromani mostly restate. Tilaka's "avasaram anviṣṭataḥ" = "searching for the opportunity" (i.e. the opportune moment, meaning when rākṣasīs would be asleep) is a subtle addition. This is a borderline case; I'll reject as it complements only marginally and Leonov's own note already treats this verse's key term extensively.

2. **5.18.2** — Leonov's own note already covers brahmarakṣasa (per Tilaka). Phase-1 tier-2 also has two notes on ṣaḍaṅgaveda and brahmarakṣas. Bundle's Tilaka text repeats this: "virātre = rātriviparyāse = apararātra" (timing) + "brahmarakṣasāṃ = brahma vedas tajjña rakṣasām" (same point as Leonov's + Phase-1 already). Reject — duplicates both tier-1 and Phase-1.

3. **5.18.3** — restates. Leonov's own note covers this verse literally. Reject.

4. **5.18.4** — restates. Reject.

5. **5.18.5** — siromani explains why Ravana couldn't hide his desire: "madanena mādakasurāpānādinā madotkaṭaḥ" = intoxicated specifically by love-passion AND (also) by intoxicating liquor (surāpāna) — i.e., double intoxication (love + wine). This is a nuance: подстрочник's "mad-utkaṭaḥ" (madness-excessive) reads ambiguous between love-madness and literal drunkenness; siromani specifies it's fueled by both. Let me check if this adds real content. подстрочник: "обезумевший от страсти" — doesn't mention wine. Siromani's addition of surāpāna (wine) as a contributing factor to his inability to control himself could be worth noting, connecting to the wine-drinking women theme running through this canto (16.19). This is a modest but real addition. I'll consider drafting — but check depth: is this substantial enough? It's fairly minor. I'll lean reject: marginal.

Let me check verse 8 (īhāmṛga) since Leonov's own note discusses translator debates there — our bundle has no commentary on v.8 at all actually (checked earlier — bundle only has bhusana restating). Confirmed no new commentary content beyond restatement.

Let me look closer at verses with real content: 10, 11, 12, 19, 21, 22-25 (Kama-related), 28, 29, 30-32.

**5.18.10** — Tilaka: "vīthīḥ = aśokavanikā-mārga-gamana-vīthīḥ" (the pathways = paths for walking through the aśoka grove) — grammar/reference gloss, restates. Also "śatamātram ity avadhāraṇe iti katakaḥ" — grammatical note about "only a hundred" (restrictive interpretation per Kataka) — pure grammar. Reject.

**5.18.11** — Tilaka: "ata anena laṅkāyāṃ hemantaśiśirayor api śītābhāvo dhvanitaḥ" = "by this [detail of yak-tail fans in what should be a cool season] it is implied that even in the hemanta/śiśira [winter] seasons there is no cold in Lanka" — this is a genuinely interesting realia observation: fans used even implies Lanka has no winter cold (an aside about Lanka's tropical climate, an implicit worldbuilding detail the poet embeds). Подстрочник just lists the fans literally, doesn't draw out this climate implication. This is a good candidate — kazansky **В** (realia/place characteristic). Let me draft this.

**5.18.12** — mostly lexical/grammar (bhṛṅgāra=kalasha, gṛhya=grhītvā). Leonov's own note already discusses maṇḍalāgra variant readings (bṛsī vs asi) extensively citing critical edition, Goldman. Our bundle text: Tilaka "bṛsīr āsanaviśeṣān tapasvinām ime tṛṇādinā, asya tu svarṇeneti viśeṣaḥ" = "bṛsī are seats used by ascetics [normally made] of grass etc., but here [it's] specifically of gold" — this actually is an interesting point: bṛsī are normally ascetics' humble grass mats, but here rendered in gold — a luxury/status inversion detail. This complements Leonov's note (which is about the textual variant reading maṇḍalāgra=sword vs asana) with a different point: WHY bṛsī (if this reading is followed) is notable — the object's usual poverty/asceticism connotation vs. its golden luxury version here. This is genuinely a different facet. Let me check register value — is it worth noting given Leonov's note already extensively handles this verse? Per the brief: "If the commentator adds a genuinely distinct facet, DRAFT the note and add complements_leonov." This does seem to add a real facet (the ironic luxury-vs-asceticism connotation of bṛsī), distinct from the textual-variant discussion Leonov gives. I'll draft this with complements_leonov.

**5.18.13** — restates (kā cid... dakṣiṇā=nipuṇā "skilled" — siromani's gloss). Minor grammar. Reject.

**5.18.14** — bhusana glosses stray content — mostly a big blob describing "mathitāmṛtaphenābham" (already in Leonov's own note at v.24, and note the marker is clearly offset — this content is actually for v.24 glued under v.14). Reject — data-misalignment/restates.

**5.18.15** — restates. Reject (Kostina's own note already flags parītākṣyo, patiṃ vīraṃ).

**5.18.16** — Tilaka: "vyāviddhāḥ = sthānād īṣac calitāḥ" (slightly displaced from position) + "samyag āmṛditaḥ mṛṣṭo varṇako'nulepanam" (thoroughly rubbed-off cosmetic ointment) — restates/lexical, matches подстрочник closely. Kostina's own note flags keyūrā and svedakliṣṭā as omitted-but-worth-noting — but our bundle doesn't cover svedakliṣṭā at all (only vyāviddha, samāmṛdita). Reject — restates.

**5.18.17** — restates. Reject.

**5.18.18** — Tilaka: "madiralocanā = madakaravīkṣaṇāḥ" (restates) + "bahumānād = bhartṛkṛtasammānāt" (respect shown BY the husband, i.e. Ravana's affection toward them) + "kāmāt = svīyāt" (their own desire). This clarifies whose "respect/affection" (bahumāna) — Ravana's toward them, and whose "desire" (kāma) — their own (not his). This resolves a real construal ambiguity in "bahumānāc ca kāmāc ca" (out of great regard and out of desire) — WHOSE regard, WHOSE desire? Tilaka specifies: regard = Ravana's for them; desire = their own for him. This is a real textological disambiguation not obvious from подстрочник alone (подстрочник: "с почтением и любовью" — ambiguous whose). Worth drafting: kazansky Б.

Let me check verse 19, 21-25 (Kama sequence), 26-32 more.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && e
**5.18.19** — Tilaka: "mando = durmatiḥ" (mando = evil-minded, not "slow/dull") + "mandaṃ yathā tathāñcitā gatir yasya" (his gait is such that it matches "mandam," i.e., slow-paced gait) — Leonov's note flags "mando" as omitted, citing Tattvadipika/Tilaka's gloss "मन्दो दुर्मतिः" verbatim — this is EXACTLY what our bundle's Tilaka text says. So this duplicates tier-1 exactly (Leonov's note already gives "मन्दो दुर्मतिः"). Reject — duplicate.

**5.18.21** — Tilaka: "jihmādi-guṇake īkṣaṇe yasya tam" = "whose eyes have qualities like crookedness etc." — actually this seems to be misplaced content (belongs to v.23's jihmatāmrāyatekṣaṇam, glued to v.21 marker). Kostina's own note flags "acintya" needing commentary — but our bundle has no Tilaka/Bhushana content specifically on acintya. Reject.

**5.18.22** — Tilaka: "rātriśeṣa-sattvāt dvādaśyāṃ yāmāvaśiṣṭarātrau candrasyāstagamanāc ca" = "because there is a remainder of night, on the twelfth [tithi], with only a watch(yāma) of night left, and because the moon has set" — this explains WHY torches/lamps were needed despite dawn approaching (moon has set, still dark) and gives a specific tithi (12th lunar day) detail. This is a temporal/astronomical realia detail not in подстрочник (подстрочник just says "lit by lamps," doesn't explain why lamps needed at this hour or the specific lunar day). This connects to Leonov's v.1 note about the exact hour (3-6am) — it's a complementary astronomical detail (specific tithi + moonset). Worth drafting? It's somewhat technical/calendrical — a Russian reader might find "the moon had already set, hence torches needed despite near-dawn" mildly interesting but is this "adds a fact/reading absent from all"? I think this is worthwhile — it explains a small logical puzzle (why lamps if it's near dawn) and gives a precise calendrical detail. Kazansky Б. Let me draft this, keeping to 1-2 sentences.

**5.18.23** — Phase-1 already has TWO notes on this verse (kandarpāpaviddhaśarāsana lexical note + kandarpa cross-text to Kumārasambhava). Bhusana's note: "samakṣaṃ = pratyakṣam" (restates), "apaviddhaśarāsanam = adhṛtaśarāsanam" (restates) — nothing new. Reject — duplicates Phase-1 already rich.

**5.18.24** — Tilaka's note here is actually glued from v.16-17 content (samālyāḥ sapuṣpā ākulā mūrdhajā yāsāṃ tāḥ — belongs to v.17) plus real v.24 content: "amṛtaṃ payaḥ" (amṛta = milk, per Tilaka) — but this exact point is ALREADY in Leonov's own note verbatim ("Комментарий «Тилака» дает для слова amṛta ... значение молоко (payas)"). Duplicate. Additional content: "yad vā sthānācyutam aṅgade saktaṃ vastram avakṛṣya yathāsthāne sthāpayantam" — an alternate reading where Hanuman/Ravana pulls the garment caught on the armlet back into place (a variant construal of avakarṣantam) + textual variant note about "salīlam avakarṣantam" (Tīrtha's reading). This is a genuine textual-variant discussion beyond what Leonov's note covers (Leonov only discusses the amṛta=milk point, not this construal variant of avakarṣantam/salīlam). Consider drafting with complements_leonov, kazansky Б (textual variant). Let me check depth — is this contrastive (Tilaka has two readings itself: standard "sapuṣpam avakarṣantam" vs Tīrtha's "salīlam avakarṣantam")? This is single-commentator-internal-variant, not commentator-vs-commentator. Borderline value — a garment adjustment detail is fairly minor. I'll reject as too technical/marginal (variant reading doesn't change the image significantly — same scene either way).

**5.18.25** — Tilaka: "nidhyātum = vijñātum ayam amuka iti viśeṣeṇa jñātum" (nidhyātum means "to know specifically who this person is," not just "to look") + also glues v.26 content in ("pramadānāṃ krīḍārhaṃ vanaṃ pramadāvanam" — actually that's the note used verbatim in Leonov's own note for v.27, offset). The nidhyātum clarification: Hanuman was studying Ravana specifically to identify him, not just looking generally — this is a nuance beyond подстрочник's "стал разглядывать" (started to look at). Modest value. Let me check for duplication — not covered elsewhere. Could draft, but it's thin. I'll reject — too close to restating the verb's plain sense (разглядывать already implies scrutiny/identification).

**5.18.26** — restates + Kostina's own note flags avekṣamāṇaḥ as omitted but our bundle doesn't add beyond what's there. Reject.

**5.18.27** — Tilaka: "yadvā dūre samāgatam api tejasā samīpe saṃkrāntam iva sthitam" = alternate reading: "or [alternatively] though he was actually far off, by his brilliance/majesty he seemed as if come near" — this reinterprets "samīpam upasaṃkrāntam" (approached nearby) not literally but as an effect of Ravana's tejas (radiance) making him seem to approach even from a distance. That's a real alternate construal — a real interpretive fork (literal proximity vs. optical/majestic illusion of proximity). Also cites Amarakośa for nidhyāna=darśana/ālokana/īkṣaṇa (grammar). The alternate reading about tejas-induced illusion of proximity is a genuine interpretive nuance not in подстrochnik. Let me consider — is this the kind of "doctrinal frame" or reading nuance M.G. valued? It's a minor exegetical alternate, single-commentator internal variant (Tilaka's own "yadvā"). I think this is thin — I'll reject as within-commentator alternate without independent resolving power, and the pramadāvana=antaḥpurodyāna gloss is already in Leonov's own note for this same verse (27) attributed to both Tilaka AND Bhushana. Reject — duplicates tier-1.

**5.18.28** — Leonov's own note ALREADY covers śaṅkukarṇaḥ via Tilaka (proper name = guard of the grove) with Goldman citation and Kostina's note about G-press literal "nail-ears" reading. Our bundle's Tilaka text says exactly this: "śaṅkukarṇa-nāmā tad-vana-rakṣī rākṣasas" (Śaṅkukarṇa by name, guard of that grove) — matches Leonov's note point-for-point. Duplicate. But there's additional content: "tena viśravasaḥ putro rākṣaso rāvaṇo dṛṣṭaḥ na anyena kenāpi puruṣeṇety arthaḥ" — "By him [Śaṅkukarṇa alone — i.e. by that one guard's watch] was Ravana seen — no other person [saw him at this point]" — this actually is a narrative-logic point: only the guard Śaṅkukarṇa (not Hanuman yet — wait, re-read). Hmm, let's reconsider: subject "tena" = "by him" referring back to śaṅkukarṇa? But the verse's main clause elsewhere has Hanuman seeing Ravana. Let me look again: the verse itself is "tena viśravasaḥ putraḥ sa dṛṣṭo rākṣasādhipaḥ" = "by him [Hanuman, tena = instrumental of Hanuman implied from context] the son of Viśravas, that lord of rakshasas, was seen" — actually "tena" refers back to Hanuman from the previous verse's chain (dṛṣṭaḥ = was seen BY tena = by him, i.e. by Hanuman). Tilaka's note is clarifying that ONLY Hanuman (not anyone else) saw this at that point — reinforcing that Hanuman is uniquely positioned/hidden to witness this scene unseen. This is a real narrative-function point (Hanuman's concealment allows exclusive witness) that's slightly different from Leonov's note (which is only about Śaṅkukarṇa's identity). Let me check overlap carefully: Leonov's note title area is entirely about "śaṅkukarṇa = proper name of a guard." Our Tilaka text ALSO makes that same identification point (śaṅkukarṇanāmā tadvanarakṣī rākṣasaḥ) — so that part IS duplicate. The "tena... na anyena kenāpi puruṣeṇa" is additional but represents a fairly trivial narrative logic (of course only Hanuman, hidden, sees this — established already by the whole scene's staging). Reject as duplicate (main point already in Leonov's note) plus marginal addition.

**5.18.29** — siromani restates verse 27/28 content ("tābhiḥ parivṛtaḥ..." recap) + gives an alternate framing ("tad eva bhaṅgy-antareṇa āha" = "the same point stated via another turn of phrase" — i.e. the poet restates the same idea about being surrounded by beautiful women a different way, comparing to moon-and-stars) — this IS a real literary observation: the poet is intentionally repeating the "surrounded by beauties" motif with a NEW simile (moon among stars) rather than just being repetitive — Siromani flags this as deliberate variation (bhaṅgyantara), addressing a potential reader's confusion about redundancy. This connects to Kostina's own concern about repetition ("Не пауперизм ли это? / tān dṛṣṭvā tāṃ prekṣya" — wait, that's a different verse, v.30 area check needed). Let me verify — actually check verse 30's bhusana note re: "tāṃ dṛṣṭvā tāṃ prekṣya" repetition concern is at 5.17.28/2830 region (already handled in sarga 17). For sarga 18 v.29, the siromani "bhaṅgyantareṇa" point about deliberate restatement-with-variation is a genuine poetic-device observation not given by подстрочник. Consider drafting kazansky Б (textological — explains apparent repetition as intentional variation, a poetic device). Let me draft this.

Now let's check verses 30-32.

**5.18.30** — bhusana: "avaplutaḥ = avarūḍhaḥ. rāvaṇa-ceṣṭāḥ sarvā draṣṭuṃ pūrva-sthānād adhaḥ-śākhāṃ samāśrita ity arthaḥ" = "avaplutaḥ [means] descended — in order to see all of Ravana's actions/behavior, he took refuge in a lower branch from his previous position." This explains the PURPOSE of Hanuman's movement (climbing down) — to observe Ravana's behavior fully — which подстрочник doesn't explain (just says "spustilsya," descended). Modest addition — motivates the physical action. Slightly thin though, mostly inferable from context. I'll reject as marginal / largely inferable.

**5.18.31** — Tilaka gives an extensive passage: Hanuman, though himself of fierce power (having crossed the ocean!), was overwhelmed/shaken (nirdhūtaḥ) by Ravana's tejas, unable to remain in front of him, so he clung to a hidden branch — "sarva-māyā-tiraskāraka-māyāvatas tasya dṛṣṭy-agre māyayā alpa-śarīra-āditvena sthātum aśakyatvād evaṃ karaṇam" = "since [Hanuman], being an illusionist himself who can override all illusions, found it impossible through illusion to remain small-bodied before that one's [Ravana's] gaze, he acted thus [hid]." This is a striking theological/narrative point: Tilaka explains WHY Hanuman — who is himself a master of māyā (illusion) capable of shrinking his body at will — could NOT simply stay in plain sight in his tiny form before Ravana; it wasn't that his illusion-power failed generally, but that Ravana's tejas specifically overpowered even Hanuman's illusion-mastery in that moment. This directly explains and deepens Phase-1's own note on this verse (V.18.31 nirdhūta) which already says "not weakness but true acknowledgment of Ravana's power" — but Tilaka's point is more specific: it concerns Hanuman's siddhi (māyā/kāmarūpa shape-shifting power) specifically failing before Ravana's tejas, not just general awe. This is a genuinely distinct facet — Phase-1's note frames it as psychological ("acknowledgment"), Tilaka's frames it as a magical-power contest (māyā vs tejas). Worth drafting with complements_leonov reference to the tier-2/Phase-1 note (though Phase-1 isn't "Leonov's own" — brief's "complements_leonov" field specifically is for when Leonov/Kostina's OWN tier-1 note is on the same verse; Phase-1 tier-2 dedup is separate). Let me check: is there a Leonov OWN note at v.31? No — Leonov's own notes list doesn't include v.31. So no complements_leonov needed, but I do need to check it doesn't just restate Phase-1's already-drafted note. Given Phase-1's note is framed psychologically ("not weakness, but real acknowledgment of power") and Tilaka's is framed as a māyā-power contest (Hanuman's own shape-shifting/illusion mastery being specifically overwhelmed) — I judge this different enough to draft as new content revealing the specific mechanism (magical contest) behind the "nirdhūta" state. Kazansky Б.

**5.18.32** — Multiple commentators present (siromani, tilaka, bhusana) but content: siromani restates v.30 logic (recap) + "rāvaṇaḥ upāvartata tat-samīpaṃ prāpa" restates; Tilaka: "upāvartata = samīpaṃ prāptaḥ" (restates, one-word gloss); bhusana restates verse. All restate. Reject.

Now let's handle the merged-range/orphan bundles: 5.18.57, 5.18.69, 5.18.89 (which have `ambiguous_marker: false` but no sanskrit_iast/leonov_ru — orphan verse numbers outside the 32-verse sarga), and 5.18.1315, 1618, 1920, 2225, 2829, 3132 (marked `ambiguous_marker: true`).

Let me look at 5.18.57 and 5.18.69 content since they have real text with theological content (Tilaka's extensive passage about karma/bhagavat-dhyāna).

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
These are orphan verse numbers (57, 69, 89 don't exist in a 32-verse sarga) with no verse text/подстрочник — they're clearly artifacts of the marker parsing (likely concatenated digits from combined markers, e.g. "5" "7" from some range, or cross-sarga bleed). Per the brief's reject discipline (e) — these carry no independently attachable verse and no подстрочник to anchor against. I'll reject all three as data-misalignment/no independent verse, same as the ambiguous_marker ones. Even though the flag itself says `false`, they function identically to merged-range markers (no real verse to attach to).

Now let's tally: total 41 verses. Drafted: 5.18.11, 5.18.12, 5.18.18, 5.18.22, 5.18.29, 5.18.31 = 6 notes. Let me finalize and check verse 5.18.10 one more time since I want to also verify I haven't missed anything in verses I quickly rejected. Let me also double check verse 5.18.1 one more time — reconsider.

Actually, let me reconsider 5.18.1 once more: Tilaka's "vicinvataḥ tasyāḥ spaṣṭadarśanāya rākṣasī-nidrā-rūpam avasaram anveṣayataḥ" = "seeking [Sita] — searching for the opportunity, in the form of the rākṣasīs' sleep, for clearly seeing her." This actually DOES add something: it explains that Hanuman wasn't just wandering looking for Sita in general — he was specifically waiting for the guards to fall asleep so he could see her clearly/safely. This gives narrative motivation/logic for the timing (why now, why this moment) that's absent from подстрочник ("ищущего Вайдехи" — just "searching for Vaidehi," no mention of waiting for guards' sleep). This is a modest but real narrative-logic addition. However — is it duplicating Leonov's own note? Leonov's note at v.1 is about the exact hour timing (3 watches passed, 3-6am) via Tilaka too — different facet (temporal precision vs. behavioral motivation). Per brief: "If the commentator adds a genuinely distinct facet, DRAFT the note... add complements_leonov." Let me draft this too as it gives real narrative motivation.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Good, 41 total. Now let me finalize my decision on 5.18.1 — I'll include it as a draft. That gives me 7 drafted notes: 5.18.1, 5.18.11, 5.18.12, 5.18.18, 5.18.22, 5.18.29, 5.18.31. Let me write the output file for sarga 18.

- 🔧 `Write` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_18_candidates.json
Now let's verify sarga 18's reconciliation.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Sarga 18 reconciles perfectly. Now let's move to sarga 19.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\p2b3_report_19.txt
This is a rich sarga with 11 bundles having all 3 commentators — likely more contrastive opportunities.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\p2b3_verses_19.json
Now let's check Leonov's own notes and Phase-1 notes for sarga 19.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\p2b3_leonov_19.json
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\p2b3_tier2_19.json
Now I have the full picture for sarga 19. This is the well-known "Sita's grief" catalogue (verses 4-22, series of similes). Both tier-1 and tier-2 already cover this densely. Let me go through methodically.

**Verse-by-verse for sarga 19 (26 bundles):**

1. **5.19.1** — bhusana note is a huge glued blob including v.14's content ("vidhvastāṃ himādihatām... vedīm iva parāmṛṣṭāṃ...") and repeats v.1 verse text at the end. Actual v.1-specific content: none beyond restating "tasmin eva tataḥ kāle... dṛṣṭvaiva tatra dūradeśa eva dṛṣṭvā prāvepateti sambandhaḥ" — connects v.1's syntax to v.2's verb (syntax-linking, restates). Reject — restates/misaligned blob.

2. **5.19.2** — Tilaka: syntax-linking "tato hanūmataḥ plavanānantaram" (after Hanuman's leap) — restates/connects. Bhusana restates. Reject.

3. **5.19.3** — restates + siromani recaps v.1-2. Reject.

4. **5.19.4** — Tilaka: "sannāṃ = śīrṇām. śīrṇanaustham janam iva ity arthaḥ" = restates simile (like a person on a broken/sinking ship). Restates. Reject.

5. **5.19.5** — Tilaka: "asaṃvṛtāyām = āstaraṇarahitāyām" (without any covering/mat — restates "голая земля"); "saṃśitavratāṃ = rāvaṇavadhāya tīkṣṇaṃ vratam iva kurvāṇām" = "as if performing a sharp vow for Ravana's destruction" — this is interesting! It reframes "stoykaya v obetakh" (steadfast in vows) not as general ascetic steadfastness but SPECIFICALLY as a vow aimed at Ravana's death — i.e., Sita's austerity here is functionally a warrior's vow against her captor, not passive religious devotion. Phase-1's tier-2 note on this same term (saṃśitavrata) instead connects it to Mahābhārata's ascetic epithet for Kaśyapa (a rishi) — a formulaic-epithet-transfer reading. Tilaka's point is DIFFERENT: it's about the CONTENT of her vow (Ravana's death specifically), not just the formulaic epithet-transfer. This is a genuine distinct facet — worth drafting, complementing Phase-1's cross-text note (though "complements_leonov" field is specifically for Leonov's OWN tier-1 note; Phase-1 tier-2 is a separate dedup layer per §3.3 vs the reject-discipline point (b) "duplicates a Leonov/Kostina own note" — but reject reason (b) in the brief also covers "duplicates tier-1/Phase-1" per style feedback). Let me check: is this different enough from Phase-1's angle to not be a "duplicate"? Phase-1's note is about the epithet's ascetic pedigree (formulaic parallel to Kaśyapa); Tilaka's is about the specific CONTENT/purpose of Sita's vow (aimed at destroying Ravana) — a genuinely different, sharper point (turns her passive suffering into an active vow against her captor). I'll draft this.

Let me check 5.19.6, 7, 8-22 (Sita's catalogue of similes) more carefully — several of these have real distinguishing content.

**5.19.6** — Tilaka gives an interesting textual variant: standard reading "malamaṇḍanadigdhāṅgīm" (body smeared with dirt-as-ornament) vs. Tīrtha's variant reading "citrāṅgīm" (mottled/variegated body) — "malarūpeṇa maṇḍanena citrāṅgīṃ karburām ity arthaṃ tīrtha āha" (Tīrtha says: by dirt-as-ornament, [she is] "mottled," i.e., dappled/spotted). Also explains WHY dirt counts as "ornament" for her: "sannyāsitvād ucitaiva tasya male 'pi maṇḍanatva-buddhiḥ" = "Since she is [like] an ascetic-renunciant, even in dirt the notion of 'ornament' properly applies to her" — this is a real interpretive point: her dirt-covered body IS her fitting "ornament" BECAUSE she has effectively become an ascetic (saṃnyāsinī) — reframing "maṇḍanārhām amaṇḍanām" (worthy of ornaments, yet unornamented) as not paradoxical but consistent: an ascetic's true ornament IS asceticism/dirt. This is a genuine doctrinal-interpretive point, distinct from Phase-1's cross-text note (Kālidāsa parallel). Worth drafting — kazansky Б, textual variant + interpretive resolution of the apparent paradox. Let me draft.

Let's continue checking remaining verses (7-22) briefly for anything beyond what's already covered.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && e
**5.19.7** — Tilaka: "saṅkalpas tac-cintanam tad-rūpāśva-saṃyuktair manorathair rāma-samīpaṃ yāntīm iva" — restates the manoratha=chariot-of-mind etymology, which Leonov's own note ALREADY covers exactly (manoratha = manas+ratha, echoed in saṃkalpahayasaṃyukta). Duplicate — reject.

**5.19.8** — restates. Reject.

**5.19.9** — Tilaka/bhusana/siromani restate the Rohini/Dhumaketu simile; bhusana adds alternate reading "yad vā graheṇa grāhakeṇa ācchādakena iti dhūmaketur viśiṣyate" = alternative gloss: "grahaṇa" here might mean "the one who seizes/covers" rather than a literal planet — an internal alternate construal, minor grammar. This doesn't add much beyond Phase-1's rich astrological note (dhūmaketu as tāmasagraha). Reject — duplicates Phase-1's cross-text note in effect (though not identical, the added variant is too thin to independently justify a note).

**5.19.10** — Leonov's own note ALREADY extensively covers punaḥsaṃskāra/upanayana parallel with Goldman citation; Phase-1 also has a note. Siromani's text here actually offers something distinct: "duṣkule = rākṣasakule jātām iva rākṣasapura-sthitatvena tatra jātatvena pratīyamānām ity arthaḥ" = "'born in a bad family' [means] — because she now resides in the city of rākṣasas, she SEEMS as if born there" — i.e., duṣkula isn't marriage-as-upanayana metaphor generally, but specifically identifies the "bad family" as the rākṣasa realm she now finds herself immersed in (mere physical presence among rākṣasas makes her SEEM as if born among them, even though she wasn't). This is actually a different, sharper reading than the upanayana-marriage metaphor already given by Leonov's own note + Goldman + Phase-1. Let me check: is this different enough? Leonov's note frames "duṣkule" purely via the upanayana/marriage-as-second-birth parallel (a general social-practice observation about women's marriage). Siromani's reading is about the SPECIFIC referent of "bad family" — not marriage in the abstract but her current forced residence among rākṣasas. This does seem like a genuinely different facet - reframing the whole verse's logic from "marriage=rebirth" (general) to "captivity among rakshasas = an unwilled second birth into their world" (specific to her situation as captive). I'll draft this with complements_leonov.

**5.19.11** — bhusana explains why "śraddhā" (faith) becomes "diminished/humiliated": "avamāne hi kṛte avamantari śraddhā mandī bhavati" = "when disrespect is shown [to someone], faith TOWARD/IN the disrespecter diminishes" — a psychological-causal mechanism gloss, and separately "pūjām iva parikṣīṇāṃ svalpa-pūjā-dravyām ity arthaḥ" (reading pūjā for prajñā — a variant text). This is a fairly technical grammar/psychology point about why disrespect causes faith-diminishment — somewhat philosophically interesting but largely restates the verse's own metaphor rather than adding new content. Reject — restates/thin.

**5.19.12** — Leonov's own note ALREADY covers "āyatīm=dhanaprāpti" (per Tilaka, exactly matching our bundle) AND "kāle=utpātakāle" (per Tilaka, Tattvadipika, Bhushana — again matching our bundle's siromani "utpātasamaye"). Duplicate across the board. Reject.

**5.19.13** — restates. Reject.

**5.19.14** — Leonov's own note ALREADY covers vedī extensively (ritual purity-law framing) via Phase-1. Bundle's tilaka: "parāmṛṣṭāṃ = veda-vedi-rahita-patitair ākrāntām" = "touched by those excluded from Veda/altar-rites, i.e. by outcastes" — this actually specifies WHO touches/defiles the altar: fallen/excluded people (patita), i.e., untouchables specifically, not just generic impurity. Siromani: "parāmṛṣṭāṃ = cāṇḍālena spṛṣṭāṃ devīṃ tat-pratimām iva" = "touched by a caṇḍāla — like an image of a goddess [touched by an outcaste]." Both commentators specify the SAME thing: contact by a caṇḍāla/outcaste specifically (not just impurity in the abstract) — this concretizes Phase-1's already-rich note (which discusses "purity law" abstractly, forward-referencing Uttarakāṇḍa's exile) with a specific real-world defilement scenario (caṇḍāla-touch) that both commentators independently converge on. This IS contrastive-adjacent (two commentators, same specific point, reinforcing) but it's not really divergent — they agree. Per the contrastive-first framework, agreement between 2 commentators on a genuinely new point (not already in подстрочник or tier-1/Phase-1) could still be drafted as either a fallback single-note or noting the convergence. Given both converge on the SAME concrete point (caṇḍāla-touch specifically, deity-statue simile), I'll draft this as complementing Phase-1's note with the concrete defilement scenario both commentators independently supply.

**5.19.15-18** — Let me check for real content.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && e
**5.19.15** — restates elephant/lotus-pond simile. Reject.

**5.19.16** — Kostina's own note flags "patiśokāturāṃ" as needing commentary ("patiśokā ≠ тоска"). Our bundle doesn't have direct commentary on "patiśokāturām" specifically — tilaka/siromani/bhusana comment on "viśrāvitāṃ" (drained river) and "mṛjayā hīnāṃ" (lacking adornment-cleansing) — restating. Bhusana adds a textual-variant note at v.17 area though (checking v.16's second half glued: "gṛhītāṃ dhṛtām. paścāt stambhe lāḍitāṃ baddhām. kaścit tu 'gṛhītām ālitām' iti paṭhitvā ālitām ālānitām ity artham āha" — this is actually content for v.18 (gṛhītām ālitāṃ stambhe) glued under v.16's chunk — a textual variant: kaścit (someone) reads "gṛhītām ālitām" instead, meaning "tethered/tied to a post" (ālāna = tethering post for elephants) rather than the standard reading. This textual variant about "ālitām" (tethered like an elephant) vs. "gṛhītām... lāḍitām" (held... caressed/coaxed) matters for the gajarājavadhū (elephant-queen) simile at v.18 — worth checking there instead.

Let me look at v.18 directly since that's where this variant actually belongs.

**5.19.18** — siromani/bhusana restate "gṛhītām ālitāṃ stambhe yūthapena vinākṛtām" (captured, tethered to a post, separated from the herd-leader) — simple simile of a female elephant separated from her mate. The variant reading discussion (from the misplaced v.16 chunk) actually enriches THIS verse: whether the elephant-queen is "held and caressed" (gṛhītāṃ...lāḍitāṃ, per main reading) at the post, or simply "tethered" (ālitāṃ = ālānitām) — a variant affecting whether the image evokes a captive being handled tenderly despite captivity, or bluntly bound. This textual-variant nuance could shift the emotional coloring of the simile (gentle handling-in-captivity vs. blunt restraint) — a modest gloss. Given it's a single obscure variant-reading footnote though, and Leonov's own notes don't flag this verse at all, I'll consider it thin but somewhat interesting. Let me weigh: is a variant reading of "tethered" vs "caressed-while-bound" significant enough to be a print note? I think it's borderline-interesting but not clearly meeting the bar of "changes the image" — I'll reject as too technical/minor.

**5.19.19** — Kostina's own note asks "мб комм.?" and cross-references v.15.25 (comparing this braid-simile to the "lotus in mud" simile of sarga 15/17 area) but doesn't supply content. Our bundle: tilaka "ayatnataḥ = keśa-saṃskāra-abhāvād ayatnataḥ siddhyeti śeṣaḥ" restates ("without effort" = because there's no hair-styling, beauty arises effortlessly — basically restates подстрочник's own "не прилагая усилий"). Reject — restates, doesn't fill Kostina's open question.

**5.19.20** — Tilaka: "alpāhārāṃ = jala-mātrāhārām asnātayā annasya grahītum aśakyatvāt devarājataḥ pāyasa-lābhena tad-anapekṣaṇāc ca" = "'meager food' means water-only diet, because — being unbathed — she cannot properly accept food [ritually], and because, having received rice-pudding from Indra [devarāja], she has no need of more" — this is a striking narrative-continuity point: it connects back to an EARLIER episode (Indra secretly feeding Sita divine pāyasa/rice-pudding during her captivity, mentioned elsewhere in the Rāmāyaṇa) to explain WHY she eats so little — not just grief-induced appetite loss, but (a) ritual impurity preventing her from eating ordinary food while unbathed, and (b) she has already been sustained by Indra's gift. This is a genuine narrative-continuity + doctrinal (purity-law) point not visible in подстрочник (which just says "voздержанную в пище" — abstinent in food) or Phase-1's note (which frames "tapodhanā" as a general ascetic-inversion image, not this specific narrative reason). Worth drafting — kazansky Б (textological, resolves the reason behind an epithet via forward/background narrative knowledge) or possibly В (mythic/narrative background). I'll draft this.

**5.19.21** — Tilaka: "tapodhanatvād eva raghumukhyasya sakāśād daśagrīva-parābhavam āyācamānām" = "PRECISELY BECAUSE she is 'rich in tapas' [the epithet from the previous verse], she is [able to] pray/petition for Daśagrīva's downfall from Rāghava" — this connects v.20's epithet (tapodhanā) causally to v.21's prayer: her accumulated ascetic power is what grants efficacy to her prayer against Ravana. This is a genuine doctrinal-causal link across two verses (accumulated tapas = spiritual capital that empowers her curse/prayer) that подстрочник doesn't make explicit (it just presents both facts side by side without the causal "because"). Also: "svakuladevatām eva uddiśya prāñjaliṃ kṛtanamaskārām" (she prays specifically to her own family/clan deity, not a generic deity) — specifying "devatām iva" refers to her particular kuladevatā. This is a good candidate. Let me draft — connects tapas-accumulation to prayer-efficacy, and specifies the addressee as her own kuladevatā.

**5.19.22** — Tilaka: "vadhāya tāvanmātraphalakam eva, na tu sveṣṭaphalakam iti tātparyam" = "'[Ravana courts her] for his own destruction' — this yields ONLY that much result [his death], not the result he actually desires [i.e., winning Sita] — that's the point." This is an ironic authorial-voice observation: the phrase "pralobhayām āsa vadhāya" (he tried to seduce her, [unwittingly working] toward his own death) is explained by Tilaka as pure dramatic irony — his seduction attempt will achieve NOTHING he wants, only his own doom. This IS already fairly explicit in подстрочник ("Пытался соблазнить Равана на свою погибель" — the "на свою погибель" already conveys this irony directly). So Tilaka's point restates what подстрочник already makes explicit. Reject.

**5.19.23** (orphan, no sanskrit_iast/leonov_ru, colophon marker) — bhusana content is mostly the colophon (end-of-sarga formula) + a restated gloss of v.22 ("samīkṣamāṇāṃ rakṣakaṃ samīkṣamāṇām" = watching [for] a protector — glossing "gazing about" as "looking for a rescuer") — actually this last bit ("rakṣakaṃ samīkṣamāṇām") is a nice specific reading: she's not just "gazing around" aimlessly (as подстрочник's "озирающуюся" might suggest) but specifically scanning for a protector/rescuer. But this verse_id (5.19.23) is an orphan (sarga only has 22 verses; this is the colophon marker), and its real content (if anchored) would belong under v.22 which is already fully accounted (rejected above with a different reasoning). Given the verse_id itself has no independent verse text, treat per reject discipline (e). Actually — wait, let's reconsider: is this really the same content note as v.22? The "rakṣakaṃ samīkṣamāṇām" reading is a genuine additional facet of v.22's "samīkṣamāṇāṃ" (watching around = watching FOR A RESCUER) that I didn't fully credit in my v.22 rejection. Let me reconsider v.22.

Given this refines "gazing about" specifically to "scanning for a rescuer" — a small but real interpretive nuance (she's not distracted/random but purposefully looking for help) — but it's attached to orphan verse_id 5.19.23, not 5.19.22 itself. Per the brief: "If a bundle's pratika_check shows an unverified anchor with a suggest_verse, treat the attachment as suspect — draft only if the note survives on either verse." Let me check pratika_check for 5.19.23 — it's empty (no pratika_check field at all, no verse text). Since verse 23 doesn't exist as an independent verse (sarga ends at 22 + colophon), and its content substantively belongs to v.22 (already considered, with the "vadhāya" irony point rejected as redundant with подстrochnik) — I'll fold this into the v.22 decision: the "rakṣakaṃ samīkṣamāṇām" facet is real but thin (a single-word specification), and reject overall, noting both points were considered. Keep verse_id 5.19.23 as a separate reject entry per the "no independent verse" rule since it's an orphan/colophon marker.

Now the ambiguous_marker ones: 5.19.1011, 5.19.1920, and orphan 5.19.68.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
26 total bundles confirmed. 5.19.68 is an orphan (sarga only has 22 verses + colophon 23) with content that's actually about v.6 (malamaṇḍanacitrāṅgīm — this matches v.6's topic, likely a marker-offset duplicate of the v.6 discussion, already covered in my v.6 draft). 5.19.1011 and 5.19.1920 are ambiguous_marker merged-range tokens — reject per rule (e).

Now let's tally my drafted notes: 5.19.5, 5.19.6, 5.19.10, 5.19.14, 5.19.20, 5.19.21 = 6 drafted. Let me write the sarga 19 output file.

- 🔧 `Write` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_19_candidates.json
Now let's verify sarga 19's reconciliation.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
All three sargas reconcile perfectly. Let me do a final overall validation pass across all three files to confirm JSON validity and schema compliance (no BOM, correct structure).

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
All three files are valid, no BOM, counts reconcile, schema fields correct. No contrastive notes emerged in these three sargas — every drafted note ended up being a genuine single-commentator gloss (a real translation-choice resolution, textual variant, doctrinal frame, or narrative-continuity point), since in sarga 17 only bhusana+siromani were present (mostly agreeing/restating rather than diverging) and in sargas 18-19 (with tilaka too) the divergences I found were internal-to-one-commentator variants (Tīrtha vs. standard reading) rather than commentator-vs-commentator disagreements on construal, so the contrastive form's precondition (≥2 commentators genuinely diverging on the same point) wasn't met in any of my three sargas — I stayed in the fallback single-commentator mode per the brief's own escape valve.

**Summary:**

sarga 17: 37 considered / 2 drafted / 35 rejected / 0 contrastive
sarga 18: 41 considered / 7 drafted / 34 rejected / 0 contrastive
sarga 19: 26 considered / 6 drafted / 20 rejected / 0 contrastive

Outputs written to:
- [data/analysis/phase2_batch3/sarga_17_candidates.json](../sarga_17_candidates.json)
- [data/analysis/phase2_batch3/sarga_18_candidates.json](../sarga_18_candidates.json)
- [data/analysis/phase2_batch3/sarga_19_candidates.json](../sarga_19_candidates.json)

Sarga 17 confirmed to have only bhūṣaṇa + śiromaṇi (no Tilaka, no Tattvadīpikā) as noted in the launch brief. Every verse bundle was checked against both the Leonov/Kostina own-notes baseline and the Phase-1 tier-2 notes for dedup; accept rate ran 5–27% across the three sargas, consistent with the depth-not-bulk discipline. No git operations were run.

