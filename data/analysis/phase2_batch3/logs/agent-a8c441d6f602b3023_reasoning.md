# Agent log agent-a8c441d6f602b3023

_Model: `claude-sonnet-5`; extracted by scripts/export_agent_logs.py; raw transcript alongside (.jsonl) holds the full record incl. tool results._


I'll start by reading the judge brief and understanding the task structure.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\JUDGE_BRIEF.md
Now let me look at the rubric doc and the data directory structure.

- 🔧 `Bash` — List phase2_batch3 directory contents
- 🔧 `Bash` — Read phase2 method doc section
Now I have the rubric. Let me check the candidate files for sargas 1-18, the segmented bundles, and the baseline files.

- 🔧 `Bash` — Count notes per sarga candidate file
- 🔧 `Bash` — List segmented bundles and baseline files
97 notes total across 18 sargas. Let's look at the structure of one candidates file and its segmented bundle in detail.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_01_candidates.json
Good, I understand the structure. Now let's look at the segmented bundle to check faithfulness/anchoring for these 4 notes.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Need to write output to a file to avoid console encoding issues on Windows.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s01_verses.json
I now have a solid picture. Let me also check the leonov_own_notes.json and sundara_commentary_to_add.json structure for baseline dedup checks.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Good — the file wrote before the print error (print to stdout fails on Windows cp1251, but file writes with encoding='utf-8' succeed). Let me check the note keys and the file for sarga 1.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_s1.json
This is critical: **Leonov's own note for 5.1.3 already covers exactly what candidate note 5.1.3 (salilakalpa) claims** — Kostina's note explicitly says "В комментарии «Широмани» поясняется... Автор «Таттвадипики» полагает, что оно означает «прохладный» (śītala)." This is the SAME contrast the candidate note presents. This is a critical finding for non-triviality. Let me check `sundara_commentary_to_add.json` too, and look at more Leonov notes for the other 3 verses (92, 154, 190).

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_s1_targets.json
Excellent, this confirms the drafter's `why_proposed` claims for 5.1.92 (Leonov's own note is trivial, just "Sea goddess" — the candidate note adds the parigha/Pātāla myth, genuinely new), 5.1.154 (n/a for this note, cited about viṣayavāsini — Leonov's note here is different content: it's about Rāma's rule/help, note is about textual interpolation — genuinely new), 5.1.166 flagged as needing comment (matches candidate's claim), and 5.1.190 flagged as needing comment (matches candidate's claim). Now let me check `sundara_commentary_to_add.json` for sarga 1 as well.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
The "found 6" for those 4 shloka IDs suggests duplicates. Let me dump them to a file properly to inspect.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sundara_s1_targets.json
Important — no Phase-1 note duplicates the specific claims of candidate notes at 5.1.92/5.1.154/5.1.190 (those Phase-1 notes are about different lemmas: mahābala, vaidūrya, dhīra, surasā-as-realia — not the parigha/Pātāla-guard myth, not the Bhūṣaṇa interpolation judgment, not the Śiromaṇi doctrinal point). Good, all 4 sarga 1 notes pass non-triviality and contrastive checks convincingly. Let me now score sarga 1 in detail.

**Sarga 1 analysis:**

1. **5.1.3 salilakalpa**: Note claims Tilaka+Śiromaṇi read by color (sāgarajala), Tattvadīpikā reads by temperature (śītala). Checking Sanskrit: Śiromaṇi: "सलिलकल्पेषु राशीभूतत्वेन सागरजलसदृशेषु" = yes, sāgarajala-like. Tattvadīpikā: "सलिलकल्पेषु तद्वत् शीतलेष्वित्यर्थः" = yes, śītala. But note claims "в «Тилаке» ... сравнение прочитано по цвету" — checking bundle, Tilaka's text isn't present in this bundle at all for 5.1.3! Only siromani, bhusana, tattvadipika are present. `source_commentary` lists `["tilaka","siromani","tattvadipika"]` but bundle has no "tilaka" key for 5.1.3 — bhusana's text is generic ("शाद्वलानां सलिलकल्पत्वं वैडूर्यवर्णतया" — incomplete, doesn't mention sāgarajala explicitly). This is a **faithfulness problem**: the note attributes a reading to Tilaka, but Tilaka isn't in the bundle's commentary for this verse at all — bhusana is, not tilaka.

Let me double check this carefully — searching for a possible tilaka key I may have missed.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Confirmed: no `tilaka` key in the bundle for 5.1.3. The note attributes a reading to "Тилаке" which is not present in the cited bundle text — this is a faithfulness violation (misattributed commentator per the rubric's explicit example). Let me check Leonov's own note again — Kostina's note for 5.1.3 says "Таким же образом трактует это слово и автор «Тилаки»" (Tilaka reads it the same way) — so Leonov's own apparatus DOES attribute a color-reading to Tilaka, but the segmented bundle used by this judging pass doesn't contain Tilaka's text for this verse. Per the brief, faithfulness is checked "against the cited commentator's Devanagari text" in the bundle — Tilaka's text is absent, so the note's claim can't be verified from the source given. This is a gate failure.

Let me check note 2 (5.1.92) and note 4 (5.1.190) for bhusana/siromani sourcing carefully, plus note 3 (5.1.154).

**5.1.92 parigha**: `source_commentary: ["tilaka","siromani"]`. Bundle has `tattvadipika`, `tilaka`, `siromani`. Tilaka: "परिघ इति पक्षच्छेदभयात्समुद्रप्रवेशानन्तरं पातालस्थराक्षसनिरोधार्थं द्वारनिरोधकपरिघवन्मैनाकः स्थापित इत्यर्थः" — yes: fear of wing-cutting, after entering ocean, for blocking Pātāla-dwelling rākṣasas, placed like a door-blocking bolt = Maināka. Matches note's claim about Indra cutting wings and Maināka placed as guard. Śiromaṇi's text similarly discusses parighatva/asura confinement. This matches well — faithful.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Both 5.1.154 and 5.1.190 are `ambiguous_marker: true` — flagged as merged-range markers by the segmenter. This matters for **anchoring**. Let's inspect `pratika_check` for these two more carefully, and cross-check the note content against the actual cited text.

For **5.1.154 (viṣayavāsini, source: bhusana only)**: note claims Bhūṣaṇa cites Kataka and rejects as later interpolation the whole episode of Surasā's mouth growing from 10 to 100 yojanas, because Lanka's vānaras/rākṣasas would have noticed. Checking bhusana text: yes — "केचन श्लोकाः प्रक्षिप्ताः असङ्गताश्च, शतयोजनायतत्वे वानरैर्लङ्कावासिभिश्च ज्ञातः स्यादिति विरोधात्" = "some verses are interpolated and inconsistent, because at hundred-yojana extent it would be known by the vānaras and Lanka-dwellers — contradiction." This matches well. But note: does the text mention "Kataka" as cited authority? Let me check more closely — I don't see "कटक" (Kataka) explicitly in the bhusana text shown. Let me search.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
No mention of "Kataka" anywhere in the bhusana text in the bundle. The candidate note explicitly says "со ссылкой на комментатора Катаку" (with reference to the commentator Kataka) — this is **not entailed by the cited commentary text** in the bundle. This is an invented/added detail — a faithfulness violation (overstated/invented claim not in the source shown).

Let me check note 4 (5.1.190, Śiromaṇi) carefully against the text.

For **5.1.190 (chāyāgrāhi, source: siromani)**: Note claims: Śiromaṇi says the Siṃhikā episode cannot be understood as murder — dharmic Hanuman cannot be a killer of women, so "torn innards" is only overcoming her magical power, not killing; explains why Hanuman didn't kill Surasā the same way; consistent with later Lanka episode where he restrains anger considering her a woman.

Checking Śiromaṇi text: "अत्र सिंहिकायाः प्राणवियोगपरत्वेन व्याख्यानं हेयमेव परमधर्मज्ञहनुमतो ऽत्र स्त्रीप्राणावियोगकर्तृत्वस्यासंभवात् अत एव सुरसावधाभावः सङ्गच्छते । अत एव वक्ष्यमाणलङ्काकर्मकप्रहारसमये स्त्री चेति मन्यमानेन नातिक्रोधः स्वयं कृत इत्युक्तिः संगच्छते ।"

Translation check: "here the interpretation as Siṃhikā's death (prāṇa-viyoga) should be rejected, since it is impossible for the supremely dharma-knowing Hanuman to be an agent of killing a woman's life; for this very reason the non-killing of Surasā fits together; for this very reason, at the time of the strike in Lanka to be mentioned later, thinking 'she is a woman,' the statement that he himself did not become excessively angry, fits together." This is an excellent, faithful match to the note's claims — all three points (not murder, consistency with Surasā, consistency with Lanka restraint) are directly entailed.

Now let's check the anchoring/pratika_check for all 4 notes and the ambiguous_marker flags, and also double check note 1's contrastive claim issue more (the bhusana text for 5.1.3 is truncated/incomplete in bundle).

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
I already have this text from the earlier read: `bhusana: "अथ वैडूर्यवर्णेषु शाद्वलेषु महाबलः । धीरस्सलिलकल्पेषु विचचार यथासुखम् अथेति । शाद्वलानां सलिलकल्पत्वं वैडूर्यवर्णतया"`. This is truncated (cuts off mid-explanation) but confirms bhusana connects sāgara-water-likeness to the vaidūrya-color — i.e. bhusana too reads by color, consistent with the note's color-reading claim... but the note attributes the color-reading specifically to **"Тилаке и Широманьи"**, not to Bhūṣaṇa, and Tilaka is simply absent from the bundle. Since `source_commentary` explicitly lists `tilaka`, and the bundle contains no Tilaka text for this verse, the claim about Tilaka is unverifiable/unfaithful per the bundle provided. This is a genuine faithfulness gate failure.

Now let me verify the pratika_check anchoring states for all four notes (already have them from the earlier read):

- 5.1.3: siromani pratika "atheti" matches_verse=true; bhusana pratika matches_verse=true; tattvadipika matches_verse=true. No `tilaka` pratika_check entry at all (confirms tilaka absent).
- 5.1.92: tattvadipika/tilaka/siromani all matches_verse=true, ambiguous_marker=false.
- 5.1.154: bhusana/tattvadipika matches_verse=true, but ambiguous_marker=true.
- 5.1.190: siromani/tattvadipika/bhusana matches_verse=true, ambiguous_marker=true.

Let me check if there's a `suggest_verse` field anywhere (the anchoring-contradiction signal per rubric) in these bundles.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
No `suggest_verse` contradictions in sarga 1 — so anchoring is never a hard "0" here; it's either verified (2, matches_verse=true) or, for ambiguous_marker=true verses, a softer signal. Per the rubric, anchoring is about the segmenter's pratika_check specifically, and `matches_verse: true` means the pratīka aligns to the cited verse — that's a verified anchor (2), regardless of the `ambiguous_marker` flag (which is about merged-range commentary text, a separate faithfulness/scope concern already captured in my faithfulness analysis, not anchoring per se). I'll score anchoring 2 for all four since `matches_verse: true` for the cited commentators in each.

Now let me write the judge objects for sarga 1 notes.

**Note 1 (5.1.3, salilakalpa):** faithfulness=0 (Tilaka reading invented/unverifiable — absent from bundle's cited text) → reject. non_triviality would be 2 (genuinely resolves a translation choice, and matches Leonov's own note contrast, so it's arguably duplicative of Leonov's OWN note too — Kostina already gives this exact contrast in her note for 5.1.3!). Actually this is doubly bad: Leonov/Kostina's own note ALREADY states this exact contrast (Śiromaṇi=sāgarajala reading, Tilaka=same, Tattvadīpikā=śītala). So non_triviality should actually be 0 (restates the crib/tier-1). Let me confirm precisely by rereading Kostina's note text.

Kostina's note (5.1.3): "В комментарии «Широмани» поясняется, что имеется в виду морская вода (sagarajala). Таким же образом трактует это слово и автор «Тилаки». Автор «Таттвадипики» полагает, что оно означает «прохладный» (śītala)." — This is **exactly** the contrast the candidate note presents, just phrased differently. So non_triviality = 0, gate → `park` (but faithfulness=0 → `reject` takes precedence). Verdict: **reject** (faithfulness gate fails, and also duplicates Leonov's own note).

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Console encoding garbled but I already have the file-based version from before ("Claude.AI — строго] [термин] (не учтено) Сураса — морская богиня, мать змей; испытывает Ханумана" — 97 chars, trivial). Good, confirms my earlier reading. Now let's finalize scores for all 4 notes in sarga 1.

**Note 2 (5.1.92, parigha):** faithfulness=2 (Tilaka text fully supports the myth: wing-cutting fear, Pātāla-guard). non_triviality=2 (Leonov's own note is trivial one-liner "Sea goddess..."; Phase-1 doesn't cover this myth either — confirmed no Phase-1 note on V.1.92 besides the trivial "surasā" realia note about her being a test-goddess, which doesn't mention parigha/Maināka-guard myth at all). contrastive_value: source_commentary=[tilaka, siromani], both cited, but note doesn't present them as "contrasting" - it's a single unified doctrinal reading, not two different readings compared, so contrastive_value=1 (single-commentator-class real exegetical gain, though two commentators corroborate). register: 2 (single paragraph, in-note commentator naming "по Тилаке и Широмани", IAST lemma present, no Devanagari, no essay — good). anchoring=2. Verdict: **keep**.

**Note 3 (5.1.154, viṣayavāsini):** faithfulness=0 — "Катаку" (Kataka) invented, not in bundle text. Verdict: **reject**.

**Note 4 (5.1.190, chāyāgrāhi):** faithfulness=2 (fully entailed). non_triviality=2 (fills gap Leonov/Kostina flagged as unclear — "Комм. (уточнить...)"). contrastive_value: single commentator (Śiromaṇi) with real doctrinal resolution = 1. register=2. anchoring=2 (matches_verse=true for siromani). Verdict: **keep**.

Now let me write the sarga_01 output file with judge objects added.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_01_candidates.json
Given the volume of work across 18 sargas / 97 notes, I'll write a Python script to do the mechanical JSON manipulation (reading, inserting judge objects, writing back with correct formatting), while I supply the actual judged content (scores/verdicts/reasons) after doing the analytical reading myself for each note. Let me process sarga by sarga. First, let me build my judgments for sarga 1 into a script-applied patch.

- 🔧 `Bash` — Create judgments scratch directory
- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\judgments\sarga_01.json
Now let me look at sarga 2 candidates and its bundle in parallel with the Leonov/Phase-1 baselines.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_02_candidates.json
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_02_candidates.json
Now let me get the segmented bundle and Leonov notes for sarga 2, targeting the 13 verse_ids.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s02_verses.json
This is very rich. Let me analyze each note against its bundle text carefully.

**5.2.4 (kavivakya)**: Tilaka: "हनुमदभिप्रायानुवादः कवेः" = "hanumad-abhiprāya-anuvāda kaveḥ" = "the poet's rendering of Hanuman's intention/view" — this literally supports "kavivākyam... hanumadabhiprāyānuvādaḥ kaveḥ" as the note phrases. Faithful=2. Note claims "podstrochnik передаёт слова Ханумана впрямую, не маркируя этот приём" — reasonable. non_triviality: need to check Leonov/Phase-1 for 5.2.4.

**5.2.9 (muculinda)**: Tilaka: "मुचुलिन्दा जम्बीरा इत्याहुः" = "muculindā jambīrāḥ ity āhuḥ" = "muculinda they call jambīra" — matches note exactly (dikiy limon/citron identification is jambīra = citron). Faithful=2.

**5.2.12 (akrida)**: Tattvadīpikā: "आक्रीडान् राजसम्बन्धित्वेपि साधारणोद्यानानि, उद्यानानि राज्ञामसाधारणानि" = "ākrīḍān — even though royal-connected, are common/public gardens; udyānas are exclusively royal." Bhūṣaṇa: "आक्रीडान् सर्वसाधारणक्रीडास्थानानि" = "ākrīḍān = places of play common to all." Both match note precisely. Faithful=2.

**5.2.16 (girisamkasaih/grahasamkasaih)**: Bhūṣaṇa: reads "गृहैश्च ग्रहसङ्काशैः" (grahasaṃkāśaiḥ not girisaṃkaśaiḥ) with gloss "ग्रहसङ्काशैः नवग्रहतुल्यैः" = "like the nine planets." Matches note precisely. Faithful=2.

**5.2.18 (devo devapurim iva)**: Tilaka: "देव इन्द्रो देवपुरीममरावतीमिव । अनेन परनगरादिकृतक्षोभाभावः सूचित इति बोध्यम्" = "deva = Indra, devapurī = Amarāvatī-like; by this the absence of disturbance caused by enemy-city etc. is indicated" — matches note's claim about absence of enemy-invasion traces. Faithful=2.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
5 verses have Leonov notes (5.2.9, 5.2.18, 5.2.24, 5.2.44, 5.2.55). Let me view those.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_s2_targets.json
Now I have full data. Let me analyze non-triviality carefully for each:

- **5.2.4**: No Leonov note, no Phase-1 (need to check). Candidate = new. non_triviality likely 2.
- **5.2.9 (muculinda)**: Leonov's own note is about **karnikāra** = Pterospermum acerifolium (a different lemma entirely!). Candidate note is about **muculinda** = jambīra. These are different plants in the same verse (verse lists multiple trees). Not duplicative. non_triviality=2.
- **5.2.12**: no Leonov, need Phase-1 check.
- **5.2.16**: no Leonov, need Phase-1.
- **5.2.18 (devo devapurim iva)**: Leonov's own note covers the **devo/divi textual variant** (Jhala 1966 critical edition). The candidate explicitly says "деталь, которой нет ни в подстрочнике, ни в собственном примечании Леонова к этому стиху (о разночтении devo/divi)" — acknowledging Leonov's note covers a different point (textual variant) while candidate adds the interpretive detail (no invasion traces). This is a genuinely different point — non_triviality=2, `complements_leonov` field explicitly present.
- **5.2.20**: no Leonov, check Phase-1.
- **5.2.22**: no Leonov, check Phase-1.
- **5.2.24 (praksipta-patha)**: Leonov's own note (Kostina) discusses the **Gita-press verse-numbering variance** (24 vs 24-26) — a different issue than the candidate's claim about Tilaka citing Kataka on interpolation suspicion of the Bhogavatī simile. Let me verify Tilaka's text: "एतदग्रे \"संपूर्णां राक्षसैर्घोरैर्गुहामाशीविषैरिव\" इति पाठः, इतरत्प्रक्षिप्तमिति कतकः" = "before this, the reading was 'saṃpūrṇāṃ rākṣasair ghorair guhām āśīviṣair iva'; the other [reading] is interpolated, says Kataka." This **fully confirms** the note's claim of Kataka's interpolation suspicion — unlike the earlier sarga-1 case, here Kataka IS explicitly named in the text (कतकः). Faithful=2. Good catch — this is a different case from 5.1.154 where Kataka wasn't in the text at all.
- **5.2.44**: Leonov's own note explains Tilaka's gloss on "svena rūpeṇa... hrasvatāṃ gataḥ" — a lexical clarification. The candidate's note is about a different point: the logical motivation (rākṣasās know everything, so no disguise helps, hence partial size-reduction not full disguise) — reasoning drawn from the preceding argument chain in Tilaka's commentary, which is distinct from Leonov's note. Let me verify Tilaka's text supports this reasoning chain: "किं च यावदस्तमयं स्वगोपनमेवोचितमित्याह... स्वेन रूपेण संवृतः सन्युक्तः सन्निहाह्नि देशे च यदि तिष्ठामि तदा स्पष्टं परैरवगम्यमानत्वाद्विनाशमुपयास्यामि... तस्मादासायमत्रैव क्वचिद्गिरिगुहायां निःशङ्कं स्थित्वा रजन्यामपि स्वेन रूपेणैव, परन्तु ह्रस्वतां गतो भूत्वा लङ्कामभिपतिष्यामीत्यन्वयः" — this is about staying hidden till dusk and then descending in his own form but reduced in size at night. This matches partial disguise reasoning, but does it say the rākṣasas already know everything and no disguise would help? Let me check the immediately preceding verse (43) content, and confirm the "nothing unknown to rākṣasas" reasoning links causally to the *choice* described in the note.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\dump.json
Excellent, this confirms it: Tilaka on verse 42 says "रक्षसामविदितं रक्षोभिरविदितं न किञ्चिदस्ति कृत्रिमरूपमिति शेषः । अतः प्राकृतसहजकपिरूपेणैव स्थातव्यमिति भावः" = "there is nothing not-known to the rākṣasas by disguise; therefore one should remain in one's natural monkey-form." This exactly supports the reasoning chain the note describes (leading into verse 44's decision to stay in his own form but reduced in size). The note's chain-of-reasoning claim is well-supported and non-trivial (Leonov's note at 5.2.44 only glosses the lexical meaning of "hrasvatām gataḥ," not this argument chain). Faithful=2, non_triviality=2.

Now let's check Phase-1 (`sundara_commentary_to_add.json`) entries for the remaining verses.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sundara_s2_targets.json
Good — Phase-1 notes for these verses are different lemmas/angles (haṃsakāraṇḍava, prākāra, viśvakarman, bhogavatī, vāyu, gandharva/prāsāda, purī/devapurī cross-text). None duplicate the candidate notes' specific claims:

- 5.2.12 candidate is about ākrīḍa (public vs royal gardens) — Phase-1's V.2.12 is about haṃsakāraṇḍava (bird species) — different lemma, non-duplicative. non_triviality=2.
- 5.2.16 candidate is about girisaṃkaśaiḥ/grahasaṃkaśaiḥ variant reading — Phase-1's V.2.16 is about prākāra (wall) — different, non-duplicative. non_triviality=2.
- 5.2.18 candidate — already analyzed, complements Leonov + Phase-1 (toraṇa/viśvakarman-adjacent/purī/devapurī entries are different angles) — non_triviality=2.
- 5.2.20 candidate (punarukti — Tilaka on repetition-as-device) — Phase-1's V.2.20 is about viśvakarman (architect) — different. non_triviality=2.
- 5.2.22 candidate (cintā ambiguity resolved contrastively) — no Phase-1/Leonov entry at all for this verse. non_triviality=2, contrastive_value=2 (genuine 2-commentator contrast, bhusana vs tattvadipika, on what exactly Hanuman pondered).
- 5.2.51 candidate (gandharvanagara as war omen) — Phase-1 has V.2.51 gandharva (heavenly musicians / Bhūṣaṇa apsara-lovers) and prāsāda (architecture) — candidate's `complements_leonov` field explicitly notes this ("дополняет уже введённое в корпусе примечание к gandharva... новым, не пересекающимся мотивом"). Let me verify: Phase-1's gandharva note says "в «Бхушане» — любовники апсар... маркируют атмосферу Ланки как перевёрнутого рая" — this is a DIFFERENT point from candidate's "war omen" reading, but is it possible the candidate's claim duplicates it partially (both cite Bhūṣaṇa on gandharvanagara)? Let me check: Phase-1 says apsara-lovers/paradise-atmosphere; candidate says war-omen/portent. These are different facets, but both from Bhūṣaṇa's commentary on the same lemma — worth checking the actual Bhūṣaṇa text to see if BOTH ideas (apsara-lovers AND war omen) are present, and whether Phase-1 already "used up" Bhūṣaṇa's gloss.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
I already have this text from the earlier read of s02_verses.json (5.2.51 bhusana): it discusses "gandharvanagaraṃ nāma..." meaning a marvelous wondrous city-like sky-formation, "yathoktam..." then quotes the verse about blood-drinking earth in battle when such a city appears. There's no mention of apsarā-lovers in this bundle's bhusana text for 5.2.51 at all. The Phase-1 note's claim about "Бхушана — любовники апсар" likely comes from a different verse's Bhūṣaṇa gloss on gandharva elsewhere (not this exact chunk) or is a general dictionary sense, not specific to this bundle text. Regardless, the candidate note's specific claim (war-omen quotation) is fully faithful to the cited bhusana text here, and is a distinct point from Phase-1's apsara-note. Good — non_triviality=2, faithful=2.

- 5.2.24: already confirmed faithful (Kataka explicitly named), non-triviality=2 (different from Leonov's Gita-press numbering note).
- 5.2.44: already confirmed faithful, non-triviality=2.
- 5.2.49 (vrsadamsaka etymology): Tattvadīpikā: "पृषदंशकमात्रः, पृषान् मूषिकान् दशतीति पृषदंशः मार्जारः । "ओतुर्बिडालो मार्जारः पृषदंशक आखुभुक् " इत्यमरः" — matches note exactly (etymology pṛṣat+daṃśa, Amarakośa citation). Faithful=2. Note: pratika_check shows `matches_verse: false, content_containment: 0.0` for tattvadipika at 5.2.49! This is an anchoring concern — the pratīka itself didn't match cleanly, though the content clearly does align (it's literally glossing "vṛṣadaṃśaka" which appears in verse 49). This looks like a segmenter false-negative (the pratīka extraction failed to match due to phonetic scrambling in OCR, e.g. "nusikan" for mūṣikān) but the content is unmistakably about this verse's word. This is "unverified but plausible" (anchoring=1), not contradicted — no suggest_verse pointing elsewhere.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
No Phase-1 entries for 5.2.49 or 5.2.55 either. Good, non_triviality=2 for both.

- **5.2.54 (candra/хронология)**: Tilaka's text is long — verify claim: ekādaśī (11th day) reasoning, torch scene chronology, "10 months passed, 2 remain" — let me check the text again: "शुक्लैकादश्यां खमध्यसमीपगतत्वेन मध्यगतत्वोपचारात्पूर्णत्वं च पूर्णकल्पत्वेन व्यवहृतम्" = "on śukla-ekādaśī (bright 11th), due to being near mid-sky it's treated as 'mid-sky', and its fullness is treated as quasi-fullness" — confirms ekādaśī reasoning, resolving apparent contradiction (moon described as full/mid-sky but not literally full moon). Then: "अत एव रात्रिशेषे हनूमत्यशोकवनिकास्थे सीतासविधे रावणस्यागमनकाले दीपिकावर्णनं कृतम्। तेन हि तदा चन्द्रास्तानुमानम्। सा चेयं मार्गशीर्षस्य फाल्गुने लङ्कां प्रविष्टायाः सीतायाः "वर्तते दशमो मासो द्वौ तु शेषौ प्लवङ्गम" इति हनूमन्तं प्रति वचनात्। हरणदिन एव च सीताया लङ्काप्रवेशनं रामभयादिति स्पष्टमेव" = confirms the torch-scene chronology, "ten months passed, two remain" citation, and same-day abduction+arrival at Lanka. This is **fully faithful** — a rich, detailed match. Faithful=2, non_triviality=2 (no Leonov/Phase-1 note on this at all), contrastive_value: single-commentator = 1.

- **5.2.55 (visanno hrstas ca)**: Tilaka: "अचिन्त्यामश्क्यान्वेषणचिन्ताम्। अयं विषादहेतुः। अद्भुताकारामिति हर्षहेतुः" = acintyām = unsearchable-with-thought = cause of sorrow; adbhutākārām = cause of joy. Bhūṣaṇa: "अचिन्त्येति। विषण्णः हृष्टश्चेति। अचिन्त्या दुष्प्रवेशेति च विषण्णः, यते ऽद्भुताकारा अतो विस्मयनीयतया हृष्टः" = viṣaṇṇaḥ because acintyā/duṣpraveśā (hard to enter), hṛṣṭaḥ because adbhutākārā (wondrous form). The note says "по Тилаке... печаль — от невозможности... проникновения (по Бхушане) — трудности проникновения" — note attributes "невозможность" to Tilaka and "трудность проникновения" to Bhūṣaṇa, but Tilaka's actual text says "aśakya-anveṣaṇa-cintām" (impossible-to-investigate-thought), not "impossible to enter" — this is close but the note's phrasing "невозможности... проникновения в такой город" attributes an "entering" idea to Tilaka's viṣāda-hetu, when Tilaka actually says the cause is about the impossibility of comprehending/investigating (anveṣaṇa = "seeking/investigating", could loosely be about seeking a way in, not exactly "entering"). This is a minor overreach in wording — slight paraphrase drift, not a misattribution or invention. I'd score faithfulness=1 (minor wording overreach — the "invisibility of entry" framing is a slight gloss beyond aśakya-anveṣaṇa) rather than outright 0.

Let's double check: is "aśakya-anveṣaṇā" plausibly about entering the city? Actually "anveṣaṇa" = search/investigation — could refer to "impossible to find a way in" contextually. This is a defensible reading, not an invention. I'll treat this as faithfulness=2 (reasonable paraphrase, not misattribution), since the semantic gist (impossible for thought/investigation → difficulty engaging with the city) is preserved and both commentators are correctly distinguished as the sources. non_triviality: Leonov's own note on 5.2.55 is about a completely different lemma (śaṅkhaprabham/moon simile at a different verse actually — wait let me check, the Leonov note listed was for verse_id 5.2.55 but discusses "śaṅkhaprabham kṣīramṛṇālavarṇam" — is that even in this verse?

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\v255.txt
Confirmed: this Leonov note (about śaṅkhaprabham/moon-conch simile) doesn't match this verse's actual content at all — it looks like a misfiled/mismatched entry in `leonov_own_notes.json` (likely an indexing artifact from the extraction script, verse-numbering drift between Leonov's print and this segmentation). Regardless, it's irrelevant to the candidate note's actual claim (viṣaṇṇa/hṛṣṭa causal split), so non_triviality=2 for the candidate note, since nothing in tier-1/Phase-1 covers this causal-split point.

Now let me finalize scores for all 13 sarga-2 notes. Let me check Phase-1 for 5.2.4 too (already saw no entries beyond what I found).

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
All confirmed empty. Now writing the sarga 2 judgments file.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\judgments\sarga_02.json
Now let's move to sarga 3.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_03_candidates.json
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_03_candidates.json
Good, 10 notes. Let me pull the segmented bundle entries for these verse_ids.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s03_verses.json
Now let me carefully check faithfulness for each of the 10 sarga-3 notes.

**5.3.6 (amarāvatīm)**: Tilaka: "अत्रामराः सन्त्यस्यामित्यमरावती द्यौः... न त्विहेन्द्रपुर्यमरावती उक्तलक्षणाभावात्" = "here amarāvatī = 'where immortals dwell' = the sky (dyauḥ)... not here Indra's city Amarāvatī, due to lack of the said characteristics [of that city]." This matches note's claim (Tilaka rejects literal Amarāvatī, reads as heaven/sky generally). Siromani: "अमरावतीं यथा संपत्त्या इन्द्रपुरीसदृशीं" = "amarāvatī, like — by prosperity, resembling Indra's city" — matches note's claim that Śiromaṇi reads it as directly comparable to Indra's city. But does Tilaka give a "grammatical argument" as the note claims ("грамматический довод")? Text: "असञ्ज्ञायामपि "मतौ बह्वचः" इत्यार्षो दीर्घः" — this references a grammatical rule (Pāṇini-style, "मतौ बह्वचः" dīrgha rule) about the long vowel in "-vatī" not requiring proper-noun status — yes, this is indeed a grammatical argument. Faithful=2.

**5.3.16 (ṛkṣasya kuśaparvaṇaḥ)**: Tilaka: "कुशपर्वण इति कुशपर्वसदृशलोमवत इत्यर्थकमृक्षस्य विशेषणम्" = "kuśaparvaṇaḥ" is an epithet of ṛkṣa meaning "having fur/hair like kuśa-grass blades" — confirms note's claim that Tilaka treats it as an epithet, not separate name. Bhūṣaṇa: "ऋक्षस्य केतुमालस्य" = reads ṛkṣa = Ketumāla explicitly — confirms note's claim about Bhūṣaṇa's alternate identification. Faithful=2. Also check: note says Leonov glosses ṛkṣa as Jāmbavān — need Leonov note to verify.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_s3_targets.json
This is a critical finding for **5.3.6**: Leonov's own note **already gives exactly the same content** — "в оригинале говорится об Амаравати... в комментарии «Тилака» подчеркивается, что речь здесь идет не о нем, а о небе... (amarāḥ)." The candidate note restates this near-verbatim, and additionally adds the Śiromaṇi contrast + "grammatical argument" + "перевод следует более естественному прочтению" — is that additional content enough to earn non_triviality ≥1? Let's check: does the candidate add the Śiromaṇi alternate reading (accepting literal Amarāvatī) that Leonov's note omits? Yes — Leonov's note ONLY covers Tilaka's reading; it says nothing about Śiromaṇi's contrasting acceptance of "город Индры" reading. That is genuinely new (non_triviality ≥1, since it adds the contrastive half). Also adds "грамматический довод" detail (the "मतौ बह्वचः" rule) not in Leonov's note. So non_triviality=1 (partially new — the Tilaka half restates Leonov, but Śiromaṇi half + grammar detail is new).

Also check 5.3.32: Leonov's own note **already gives exactly** the Tilaka gloss "vikṛtastrīrūpām" that the candidate's note cites as its opening claim ("«Тилака»... читают composит как «уродливая в женском облике»"). The candidate's added value is the Śiromaṇi second reading (vikṛtā = "явленная, представшая"). Let's verify this against Śiromaṇi's text: "स्त्रीरूपं विकृतं यस्याः तां कर्मधारयो वा, किंच स्त्रीरूपेण विकृतां प्रकटितां तां लङ्कां" — "...or [alternatively, if it's a] karmadhāraya compound, moreover, 'vikṛtā' = 'prakaṭitā' (revealed/manifested) in female form" — yes! This confirms Śiromaṇi does give a second, less pejorative reading (vikṛtā = manifested/appeared, not "deformed"). This matches the note's claim precisely. So for 5.3.32: Tilaka-half restates Leonov (already known), Śiromaṇi-half is new. non_triviality=1.

Now let's check 5.3.16 vs Leonov's cross-reference note ("Ср. с перечнем в V,2,28" — trivial pointer, no content) — doesn't diminish non-triviality of candidate. non_triviality=2 for 5.3.16.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sundara_s3_targets.json
These Phase-1 notes are different lemmas (śātakumbha, vivasvant) — no conflict with the candidate notes' claims (amarāvatīm interpretive contrast; ṛkṣa/kuśaparvaṇaḥ identity dispute). Good, no additional duplication concerns.

Now checking 5.3.25, 5.3.29, 5.3.34, 5.3.44, 5.3.45, 5.3.48, 5.3.51 faithfulness:

**5.3.25 (kathayiṣyāmi)**: Śiromaṇi: "कथयामीत्यपहाय कथयिष्यामीत्युक्त्या अहमपि किंचित्पृच्छामीति सूचितम्" = "having set aside 'kathayāmi', by saying 'kathayiṣyāmi' it is indicated that 'I too will ask something [in return]'" — matches note precisely. Faithful=2. Non_triviality: no Leonov/Phase-1 note for 5.3.25 found. non_triviality=2.

**5.3.29 (na śakyā/na śakyam)**: Tilaka: "त्वयैषा प्रवेष्टुं न शक्यम् । क्षुदुपहन्तुं शक्यमितिवत् । "न शक्या" इति पाठस्तु सुगम एव" = "by you, entry [into] this [city] is not possible" [explaining na śakyam as impersonal construction, like "kṣut upahantum śakyam"]; "the reading 'na śakyā' is indeed simpler." This matches the note's claim about two variant readings (impersonal na śakyam vs. agreeing na śakyā) and that the accepted reading is simpler. Faithful=2.

**5.3.34 (vanāny upavanāni kānanāni)**: Tilaka: "वनं कृत्रिमम्, काननमकृत्रिमम्" = vana=artificial, kānana=natural. Śiromaṇi: "वनमकृत्रिमं, काननं कृत्रिमम्" — wait, this REVERSES Tilaka! Śiromaṇi says vana=natural (akṛtrima), kānana=artificial (kṛtrima) — the OPPOSITE assignment from Tilaka! But the note claims "по «Тилаке» и «Широмани»... vana — «искусственный»... kānana — «естественный»" — grouping them together as agreeing. Let me re-read carefully.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\v334.txt
Confirmed: Tilaka says **vana=kṛtrima (artificial), kānana=akṛtrima (natural)**. Śiromaṇi says **vana=akṛtrima (natural), kānana=kṛtrima (artificial)** — the exact **opposite** assignment. The candidate note's claim that "по «Тилаке» и «Широмани», vana — «искусственный»... kānana — «естественный»" (grouping them as agreeing) **misrepresents Śiromaṇi's actual position**, which is the reverse. This is a faithfulness violation — misattribution/overstated claim not entailed by the text (in fact contradicted by it for the Śiromaṇi half). This is a significant error since it's the crux of the note's "why_proposed" claim (that commentators disagree on which word is which — but the note gets the actual assignment for one of the two commentators backwards, presenting a false consensus and thus mischaracterizing the disagreement's nature).

Let's also check Tattvadīpikā's part: "उपवनानि कुत्रिमवनानि । वनानि क्षुद्राणि" = upavana=artificial groves, vana=small/scrubby forests. This roughly matches the note's claim ("upavana как «искусственные рощи», а vana как «мелколесье»"). That part is faithful. But the Tilaka/Siromani part has the reversal error. Given faithfulness requires EVERY claim to be entailed, and one claim (Śiromaṇi agrees with Tilaka on vana=artificial) is actually contradicted by the source — **faithfulness=0** for this note.

Continuing with the rest:

**5.3.44 (samaye)**: Tilaka: "समय इति । स्त्री न हन्तव्येति शास्त्रमर्यादायामित्यर्थः" = samaya = the śāstra-rule that "a woman should not be killed." Bhūṣaṇa: "समये स्त्रीवधवर्जनव्यवस्थायाम्" = samaye = in the arrangement of avoidance-of-woman-killing. Tattvadīpikā: "समये स्त्री न हन्तव्येति व्यवस्थायाम्" = same. Śiromaṇi's text doesn't explicitly gloss "samaye" this way (it says "समये प्रार्थनाकाले तिष्ठन्ति" = "at the time of petition, they stand" — a slightly different reading, about "waiting at petition-time" rather than the dharmic-norm reading). The note claims "все комментаторы (Тилака, Бхушана, Широмани, Таттвадипика) сходятся" — but Śiromaṇi's actual gloss here is about samaye = "at the time of pleading/prayer" (prārthanā-kāle), NOT explicitly the same dharmic norm about not killing women. This is a partial overreach — 3 of 4 commentators clearly state the dharmic-norm reading, but Śiromaṇi's text as given doesn't explicitly state it (though it's compatible/implied). This is a minor overreach in attributing unanimity where one commentator's text doesn't explicitly confirm it — I'll score faithfulness=1 (minor wording overreach: claiming "all four" when Śiromaṇi's actual text doesn't explicitly voice the samaya=dharmic norm point, even if not contradicting it).

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
No baseline overlaps for these 7 — all non_triviality=2 (or as applicable given faithfulness issues).

**5.3.45 (durjayā/nirjitā)**: Tattvadīpikā: "अहं स्वयं साक्षात् लङ्कानगर्येव लङ्कानगर्यधिष्ठात्री देवतैव, अधिष्ठानदेवतात्वादेवाहं दुर्जयेत्यर्थः । ततः किमत आह निर्जितेति । दुर्जया ऽप्यहं त्वया बलान्निर्जिता अतः सत्यं सर्वे लङ्कान्तर्वर्तिनो राक्षसाः निर्जिता इति भावः" — "I am myself the presiding deity of the city Laṅkā, hence I am durjayā (unconquerable); then what? It says nirjitā — 'though unconquerable, I am conquered by you by force; hence truly all rākṣasas dwelling within Laṅkā are conquered' — this is the idea." Perfectly matches note's claim. Faithful=2.

**5.3.48 (svayaṃbhūvihitaḥ/nandikeśvaraśāpa)**: Tilaka: "न तस्यास्ति व्यतिक्रमः भगवद्दत्तवरस्य रावणस्य स्वकृताधिक्षेपक्षुभितनन्दिकेश्वरशापात्तु सद्यः प्राप्तो विनाशः, स्वयंभूवरवशाद्वानरास्कन्दनपर्यन्तं प्रतिबद्ध इति कथात्रानुसन्धेयेति तीर्थः" = "there is no violation of it [Brahma's boon] — Rāvaṇa's boon given by the Lord [Brahma] — but the destruction that has now come is due to the curse of Nandikeśvara, provoked by Rāvaṇa's own insult; [the boon] is bound/conditioned until the monkey's assault — this story should be recalled here, says [the sub-commentator] Tīrtha." This confirms the note's claim entirely (the boon isn't violated because destruction stems from Nandikeśvara's curse, conditioned to hold until a monkey's incursion). Faithful=2.

**5.3.51 (satīm)**: Tilaka: "अनेन च वचनेन सीता ऽकल्मषात्र पुरे वर्तत इत्युपदिष्टम्" = "by this statement it is taught that Sītā remains akalmaṣā ['unstained'] in this city." Matches note precisely. Faithful=2.

Now let me finalize contrastive_value and register for all 10, and write the sarga-3 judgments file.

For contrastive_value:
- 5.3.6: 2 commentators genuinely diverge on referent (heaven vs literal Amarāvatī) = 2.
- 5.3.16: genuine divergence on identity across commentators = 2 (three-way divergence, arguably even stronger).
- 5.3.25: single commentator = 1.
- 5.3.29: single commentator, textual variant = 1.
- 5.3.32: contrastive within Śiromaṇi alone (two readings) plus Tilaka agreeing with first — real exegetical gain but not exactly "2 commentators contrasted" as much as one commentator giving 2 readings; still resolves a translation choice = 2.
- 5.3.34: faithfulness=0 anyway → reject regardless of other scores, but let's still score reasonably: contrastive would have been 2 if correct, but moot.
- 5.3.44: 4 commentators corroborating, not contrasting = ornament-adjacent but genuine exegetical gain (single unified reading across many) — I'll call this 1 (not a contrast, but real gain: reveals the hidden dharmic rule).
- 5.3.45: single commentator = 1.
- 5.3.48: single commentator = 1.
- 5.3.51: single commentator = 1.

Register: all appear compliant (1-3 sentences, IAST lemma, commentator named, no Devanagari in note_ru, no essay) — checking 5.3.16 and 5.3.34 for length/essay concerns — they're a bit longer but still single-paragraph, terse enough. I'll score register=2 for all except where wording needs fixing.

Let me also double check anchoring for the ambiguous ones (5.3.6, 5.3.29 siromani, 5.3.32 siromani, 5.3.48 bhusana have `matches_verse:false` with `content_anchor:true`) — these are "unverified but plausible" = anchoring 1, not full 2, since pratīka itself didn't match.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\judgments\sarga_03.json
Now let's move to sarga 4 (3 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_04_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s04_verses.json
**5.4.1 (advāreṇa)**: Bhūṣaṇa: "स निर्जित्येत्यादि । अद्वारेणेत्यनेन लङ्कापरिभवो राक्षसैर्न ज्ञातुं शक्य इति द्योत्यते" = "sa nirjitya etc. — by 'advāreṇa' it is indicated that the humiliation of Lanka cannot be known by the rākṣasas." Matches note precisely. Faithful=2.

**5.4.13 (dīkṣita)**: Tilaka: "ननु लङ्काया भारतखण्डाद्बहिर्भावेन कर्मभूमित्वाभावात्कथं तत्र रक्षसां दीक्षितत्वमिति चेन्न । नित्यकर्मस्वन्यदेशेप्यधिकारात् । रावणादेस्तपोमाहात्म्यात्तत्र काम्यकर्मसिद्धिरपीत्यन्यत् । "यथा त्वष्टुरमेन्द्रमेव सोममाजह्रे" इत्यादिशतपथोक्तरीत्या... रक्षसामपि देवयोनित्वात्" — this fully confirms: objection about Lanka being outside karma-bhūmi (Bharata region) → response: right to nitya-karma isn't location-bound; Rāvaṇa's tapas grants kāmya-karma success too; cites Śatapatha ("as Tvaṣṭṛ brought soma meant for Indra"); rākṣasas as deva-yoni (semi-divine class). This is an extremely precise match to the note's claims. Faithful=2.

**5.4.22 (darbhamuṣṭi/agnikuṇḍa)**: Tilaka: "अरिष्टनिवारणपूर्वकमनुष्ठाननिर्वाहाय दर्भमुष्टिप्रहरणत्वं केषाचित् "यथा वज्रं हरेः पाणौ तथा विप्रकरे कुशाः" इति स्मृतेः । कृत्याद्युत्पादनद्वारा शत्रुमारकतयाग्निकुण्डानामायुधत्वम्" — "for some, the darbha-fistful is a weapon-nature for warding off evil in rite-performance, per the smṛti 'as vajra in Hari's hand, so kuśa in the brahmin's hand'; through producing kṛtyā etc., agni-kuṇḍas have weapon-nature as enemy-killers." Matches note precisely (vajra comparison, kṛtyā magic). Faithful=2.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_s4_targets.json
Note 1 (5.4.1) at verse 5.4.1 vs. the Leonov note which is filed at verse 5.4.2 — but the content ("не в ворота вошел... в город врага не полагается входить через ворота") is about the SAME advāreṇa event, just anchored to a different verse number in the print apparatus (likely the actual advāreṇa word appears across the two adjoining verses in the print numbering scheme, a common verse-boundary drift). The candidate's own `complements_leonov` field explicitly acknowledges this and states Leonov's note only gives the ritual prohibition rule, while Bhūṣaṇa (cited by the candidate) adds the "concealment from rākṣasas" reasoning — this is confirmed distinct content by the bundle text quoted above. non_triviality: Leonov's note gives the norm-based reason ("не полагается входить через ворота во вражеский город"); the candidate's Bhūṣaṇa content gives an entirely different, non-overlapping reason (concealment of the humiliation) — genuinely new. non_triviality=2.

5.4.13: Leonov's own note DOES already state "речь идет о ведийских гимнах (vedamantra)" for mantrān, and gives the Goldman citation about yātudhāna. The candidate's note goes considerably further — the theological difficulty (karma-bhūmi problem) and its resolution (Śatapatha precedent, deva-yoni status) is **entirely new**, not in Leonov's note. non_triviality=2 (adds substantially beyond the trivial vedamantra gloss).

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sundara_s4_targets.json
Different topic (kāvya cross-text, not the advāreṇa concealment reasoning). Doesn't affect non-triviality of the candidate note.

Now finalize sarga 4 scores. Anchoring: 5.4.1 bhusana matches_verse=true (2). 5.4.13 tilaka/bhusana both matches_verse=true (2). 5.4.22 tilaka/bhusana both matches_verse=true (2). Contrastive_value: all three are single-commentator notes with real exegetical gain = 1.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\judgments\sarga_04.json
Now sarga 5 (7 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_05_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s05_verses.json
Now let me carefully check each note against the text.

**5.5.1 (madhyaṃ gatam)**: Bhūṣaṇa: "लङ्काप्रवेशे चन्द्रोदयोक्तेः रावणनगरप्रवेशे अर्धरात्र इति सूच्यते" = "since moonrise was mentioned at [Hanuman's] entry into Lanka [ch.1], at the entry into Rāvaṇa's dwelling it is indicated to be midnight (ardharātra)." Matches note precisely. Faithful=2.

**5.5.2 (lokasya pāpāni)**: Tattvadīpikā: "लोकस्येति । पापशब्देन पापफलं दुःखमुच्यते, लोकः ह्लादकत्वाच्चन्द्रस्य दुःखविनाशकत्वम्। यद्वा सूर्यचन्द्रादीनां लोकपावनत्वादिति भावः" = "pāpāni means the suffering resulting from sins; due to the moon's world-delighting nature (loka-hlādakatva), it is destructive of suffering [not as retribution but as natural nature]; alternatively, sun/moon etc. purify the world by nature." Note claims this is "не как возмездие за грех" (not as retribution) — the text doesn't explicitly negate a punitive reading, but frames it as a "loka-hlādakatva"-based effect, which supports the note's characterization reasonably. Faithful=2 (close, reasonable paraphrase). Note also references "прочитанным у Леонова толкованием «Тилаки»" — let's verify against Leonov's note.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_s5_targets.json
Excellent confirmation. Leonov's note for 5.5.2 states "pāpajanakaduḥkhāni в «Тилаке»" — exactly matching the note's premise ("прочитанным у Леонова толкованием «Тилаки» (pāpāni = страдания от грехов)"). And the candidate adds Tattvadīpikā's alternative (natural loka-hlādakatva reading) which is genuinely not in Leonov's note. non_triviality=2 (adds a distinct second reading).

For 5.5.6: Leonov's own note ALREADY covers the Śiromaṇi explanation about the moon moving away from the Himalayas AND the sun-ray-conjunction darkness dispersal — matching the candidate's claim that "Бхушана подкрепляет астрономическое толкование ... прямой цитатой из Варахамихиры" — let's check: does the candidate's note ADD something Leonov doesn't have? Yes — the candidate specifically cites the **Varāhamihira quotation** ("सलिलमये शशिनि रवेर्दीधितयो..."), which is a distinct, new citation not in Leonov's note, PLUS the alternate etymology of śaśāṅka via Hariwaṃśa (not "hare" but "earth's shadow") — let's verify this against the bundle text: Bhūṣaṇa: "शशाङ्कः इति। भूच्छायामयः शशरूपः अङ्कः यस्य स तथा। "लोकच्छायामयं लक्ष्म तवाङ्के शशसन्निभम्" इति हरिवंशोक्तेः" = "śaśāṅka: whose mark is earth-shadow shaped-like-a-hare; per Hariwaṃśa's statement 'your mark on the moon, world-shadow shaped like a hare'." This confirms the note's claim precisely: candidate says "поясняет знак на луне (śaśāṅka) не как зайца, а как тень земли, ссылаясь на «Хариванщу»" — the Hariwaṃśa quote literally says the mark is "loka-chāyā-maya... śaśa-sannibham" = "shaped like a hare but actually being world/earth-shadow" — so it's not "not as hare" exactly but "hare-appearing but actually earth-shadow" — a subtle nuance, but the note's characterization ("не как зайца, а как тень земли") is a defensible compressed paraphrase of this dual reading. I'll treat as faithful=2 (reasonable compression, not invented). Non_triviality: 2 (Varāhamihira quote + earth-shadow etymology both absent from Leonov's note, which only covers the Himalaya-distance and sun-conjunction explanations).

**5.5.9 (svavṛttāḥ)**: Tilaka: "स्ववृत्ताः" इति पाठे स्वं स्वीयं सहजपातिव्रत्यलक्षणं वृत्तं चारित्रं यासां ताः" = "in the reading 'svavṛttāḥ', [it means] those whose conduct is characterized by their own innate wifely-fidelity." Matches note exactly. Faithful=2.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
No Leonov notes for 5.5.9, 5.5.18, 5.5.22, and 5.5.21 has only a trivial Kostina remark unrelated to the candidate's claim (about a translation-order ambiguity, not about the prasamīkṣya rāmāḥ variant). Let me check Phase-1 for these too.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sundara_s5_targets.json
Different lemmas (śaśāṅka etymology, tantrī, naktaṃcara, niśītha) — none duplicate the specific candidate claims (svavṛttāḥ variant reading; architectural sapphire-chamber detail for the bird simile). Good, non-triviality holds for 5.5.9 and 5.5.18.

**5.5.18 (vihaṃgā vihagopagūḍāḥ)**: Tilaka: "प्रमदेन हर्षेणोपगूढाः संबद्धा यथा विहङ्गाः विहङ्गीरिवेत्यर्थः । इन्द्रनीलमणिमयोर्ध्वगेहेषु नीलतमःसदृशेषु शयनात्तत्सादृश्यम्" = "joined in joy, like male birds embracing female birds; the resemblance is because they sleep in upper chambers made of sapphire, resembling deep darkness." Matches note precisely (sapphire chamber = darkness, appropriate for bird simile with night-lovers). Faithful=2. non_triviality=2, contrastive=1 (single commentator).

**5.5.21 (prasamīkṣya rāmāḥ)**: Tilaka: ""प्रसमीक्ष्य रामाः" इति पाठे प्रियान्प्राप्य तान्समीक्ष्य प्रीतियुक्ता रामस्तैः प्रियै रम्यमाणाः, अत एव गृहेषु हृष्टा रामाः" — confirms the variant reading "prasamīkṣya rāmāḥ" exists, with rāmāḥ (women) as the ones looking. Bhūṣaṇa: "प्रियान्प्राप्य अभिसृत्य सुप्रीतियुक्ताः मनोभिरामाः रामाः प्रसमीक्ष्य गृहेषु रामाश्च ददर्श । अभिसारिकाः कुलपालिकाश्च ददर्शेत्यर्थः" — confirms exactly the two groups distinction (abhisārikāḥ = secretly-tryst-seeking, kulapālikāḥ = house-keeping faithful wives). Faithful=2, non_triviality=2 (Leonov's note for 5.5.21 only addresses an unrelated translation-order ambiguity issue), contrastive_value=2 (genuine 2-commentator, textual-variant based contrast with real interpretive payoff).

**5.5.22 (vaktramālā/vibhūṣaṇānāṃ mālāḥ)**: Bhūṣaṇa: "चन्द्रेति । वक्त्रनेत्रदर्शनं मानुषीत्वराक्षसीत्वविवेकार्थम्। आभरणदर्शनं स्वदृष्टसीताभरणतुल्याभरणदर्शनार्थम्" = "seeing faces/eyes is for the purpose of distinguishing human-ness from rākṣasī-ness; seeing ornaments is for the purpose of seeing ornaments similar to those seen on Sītā." Matches note exactly. Faithful=2, non_triviality=2 (no Leonov/Phase-1 for this verse).

Now let's finalize anchoring scores — noting matches_verse:false cases: 5.5.2 siromani (content_anchor=true, but siromani isn't the cited commentator for this note — note cites tattvadipika only, which has matches_verse=true) — fine, anchoring=2 for 5.5.2 since the cited commentator's pratika matches. 5.5.9 tilaka matches_verse=false (content_anchor=true) — and tilaka IS the cited commentator here — anchoring=1. 5.5.18 siromani matches_verse=false but note cites tilaka only (matches_verse=true) — anchoring=2. 5.5.22 tilaka matches_verse=false (content_anchor=true) but note cites bhusana only for the specific claim (bhusana matches_verse=true) — anchoring=2.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\judgments\sarga_05.json
Now let's move to sarga 6 (4 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_06_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s06_verses.json
**5.6.5 (mahāmātra)**: Tilaka: "महामात्रैर्हस्तिपकैः" = elephant-drivers. Śiromaṇi: "महामात्रौ" (unclear gloss, doesn't explicitly define but groups with gajārūḍhaiḥ context implying drivers). Tattvadīpikā: "महामात्रैः प्रधानैः । "महामात्राः प्रधानानि" इत्यमरः" = "mahāmātra = pradhāna (chief officials); per Amarakośa 'mahāmātrāḥ = pradhānāni'." This confirms the note's contrast precisely — Tilaka reads hastipaka (elephant-driver), Tattvadīpikā reads pradhāna (chief officials) with Amarakośa citation. Note claims Śiromaṇi agrees with Tilaka (hastipaka) — but Śiromaṇi's text here doesn't explicitly gloss mahāmātra as hastipaka; it just says "gajeti । gajasthitaiḥ gajārūḍhaiḥ mahāmātrau..." (leaves mahāmātra ungloseed, using it in a compound). This is a minor overreach — attributing an explicit hastipaka gloss to Śiromaṇi when the text doesn't actually gloss it that way (it's ambiguous/left as-is). I'll call this faithfulness=1 (minor overreach: Śiromaṇi doesn't explicitly confirm hastipaka).

**5.6.7 (mahāratha)**: Tilaka: "महरथानाम् "एको दशसहस्राणि योधयेद्यस्तु धन्विनाम्। शस्त्रशास्त्रप्रवीणश्च स महारथ उच्यते।।" = "of mahārathas: 'one who alone can fight against ten thousand archers and is skilled in weapons and śāstra is called mahāratha.'" Śiromaṇi cites the identical verse. Confirms note's claim exactly (formal śāstra definition: one warrior vs 10,000 archers + weapon mastery). Faithful=2. non_triviality: check Leonov.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_s6_targets.json
Good. Kostina's own note at 5.6.12 is literally an open question flag ("Комм." — needs a comment) for exactly this phrase — the candidate note explicitly closes this gap, matching its own `why_proposed` claim. Confirmed non_triviality=2 for 5.6.12.

For 5.6.10 (a different verse than in our candidate set but relevant context): Leonov's note there explains "шум производили украшения" (ornaments) via Tilaka. This is about verse 10, and the candidate note about 5.6.13 explicitly contrasts with content from verse 10 ("«звучание, подобное океану» из стиха 10 (samudrasvananiḥsvanam) относится лишь к внешнему двору"). Let's verify 5.6.13's bhusana text for this claim: "समुद्रस्वननिस्वनमिति तु बाह्यकक्ष्यापेक्षया" = "but 'samudrasvananiḥsvanam' [from the earlier verse] is with respect to the outer chamber (bāhya-kakṣyā)." This confirms the note's claim about verse 10's phrase applying to the outer courtyard specifically. And "समुद्रमिव निःस्वनं निःशब्दम्, रावणभीत्या जनकोलाहलरहितमित्यर्थः" = "'like the ocean, niḥsvanam' [means] silent — devoid of people's clamor due to fear of Rāvaṇa" — confirms Bhūṣaṇa's opposite reading (niḥsvanam = silent, not "sounding"). Faithful=2 for 5.6.13.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
No Leonov notes for 5.6.5, 5.6.7, 5.6.13 directly, and no Phase-1 entries either (confirmed earlier: 0 results for all 4 target shlokas). All non_triviality=2.

Now let me check anchoring: 5.6.5 all matches_verse=true → anchoring=2. 5.6.7: tilaka matches_verse=false (content_containment 0.0, no content_anchor flag even) but note cites tilaka — this is concerning; however bhusana matches_verse=true, siromani matches_verse=true, and the note's core claim (formal śāstra definition) is directly quoted verbatim by BOTH tilaka and siromani identically, and siromani's pratika DOES match_verse=true. Since siromani corroborates the exact same quoted definition, and it is cited alongside tilaka, I'll treat anchoring=2 (the content is doubly anchored via siromani even though tilaka's own pratika match failed). 5.6.12: all match_verse=true → anchoring=2. 5.6.13: both bhusana/siromani matches_verse=true → anchoring=2.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\judgments\sarga_06.json
Now sarga 7 (3 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_07_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s07_verses.json
**5.7.4 (mayena sākṣād iva nirmitāni)**: Bhūṣaṇa: "मयेनेति विश्वकर्मा लक्ष्यते... रावणप्रयत्नेनैव निर्मितानीत्यर्थः। यद्वा अन्यानि गृहाणि विश्वकर्मनिर्मितानि, इमानि तु मयं व्याजीकृत्य स्वयमुपायप्रदर्शनमुखेन निर्मितानीति पूर्वगृहेभ्यो विशेष उच्यते" = "'mayena' refers to Viśvakarman... [but really] built by Rāvaṇa's own effort; or, other houses were made by Viśvakarman, but THESE were made by Rāvaṇa himself under the guise/pretext of Maya, through demonstrating his own means — this distinguishes them from the earlier houses." This confirms note's claim about Bhūṣaṇa (Rāvaṇa built it himself, under pretext of Māya). Śiromaṇi: "मयेन साक्षान्निर्मितानीव विश्वकर्मणा निर्मितत्वे ऽपि अनेकमायामयत्वान्मयनिर्मितसदृशानीत्यर्थः" = "though actually made by Viśvakarman, due to abundant illusion it merely resembles being made by Māya." Confirms note's claim about Śiromaṇi (genuinely Viśvakarman's work, appears Māya-made due to illusion). Faithful=2. Excellent, precise match on both sides of the contrast.

**5.7.9 (kṛtā)**: Tilaka: "प्रवतादयश्चात्र मणिस्वर्णादिनिर्मिताः, न त्विदं चित्ररूपमिति भ्रमितव्यम् अनन्तवानरसेनाया निर्बाधं तत्रावस्थानस्य वक्ष्यमाणत्वात्। किं च स्वामीच्छानुसारेण सङ्कोचविकासौ तस्य वक्ष्यति स्वेच्छया हनुमद्देहवत्" = "the mountains etc. here are made of gems/gold, one should not be confused thinking this is a picture (citrarūpam), since it will be said later that an infinite army of monkeys can stay there unobstructed; moreover, according to the owner's will it expands and contracts, like Hanuman's own body." This confirms the note's claim precisely (magically real, not depiction; army fits later; expands/contracts like Hanuman's body). Faithful=2. But interesting: Bhūṣaṇa explicitly takes the OPPOSITE view here: "यत्र विमाने पर्वतराजिपूर्णा मही कृता चित्ररूपेण लिखिता" = "in this vimāna, the mountain-filled earth was made, PAINTED in picture-form (citrarūpeṇa likhitā)" — i.e. Bhūṣaṇa explicitly says it IS depiction/painting, contradicting Tilaka! The note only cites Tilaka (`source_commentary: ["tilaka"]`) and doesn't mention this direct contradiction from Bhūṣaṇa in the same bundle — but since the note doesn't make any claim about Bhūṣaṇa, and only attributes its content to Tilaka (correctly), this doesn't violate faithfulness for what IS claimed. However, it does raise a `why_proposed`/contrastive_value consideration: the note misses an opportunity to flag genuine contrastive value (both readings exist in the very bundle) — but that's a completeness critique, not a faithfulness violation. I'll note this doesn't block faithfulness, but affects contrastive_value scoring (still single-commentator as drafted, could have been elevated to `contrastive:true` had it included Bhūṣaṇa, but as drafted it's not marked contrastive — accurate as is).

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_s7_targets.json
Trivial, unrelated to the candidate's claim about patiguṇaveganirjitām. non_triviality=2 for 5.7.16 (and 5.7.4, 5.7.9 have no Leonov notes at all).

**5.7.16 (patiguṇaveganirjitām)**: Śiromaṇi: "पतिगुणवेगनिर्जितां पतिगुणानां समाधिकरहितवात्सल्यादीनां वेगेन स्मरणजनितोद्वेगेन निर्जितां स्थातुमशक्यां" = "patiguṇavegan-nirjitām = overcome by the force [born] of remembering, without any counterbalance, her husband's incomparable affection etc.-qualities, unable to remain composed." This confirms the note's claim about the psychological mechanism (unceasing memory, no counterbalance since husband absent). Faithful=2.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sundara_s7_targets.json
Both different topics (Māya's general cultural rank; Janaka's identity) — don't overlap with candidate claims (authorship contrast; psychological mechanism). non_triviality=2 for both 5.7.4 and 5.7.16.

Anchoring: 5.7.4 both bhusana/siromani matches_verse=true=2. 5.7.9 tilaka matches_verse=true=2. 5.7.16 all three matches_verse=true=2.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\judgments\sarga_07.json
Now sarga 8 (3 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_08_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s08_verses.json
**5.8.2 (tadaprameyapratikārakṛtrimam)**: Tilaka: "पाठान्तरं त्वसांप्रदायिकमिति कतकः" = "the variant reading, however, is non-traditional, says Kataka." Kataka is named here explicitly, matching the note's claim precisely. Faithful=2.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_s8_targets.json
Good. Leonov's own note for 5.8.2 only covers "не было ей равных красотой" — trivial (unrelated to the Kataka textual-variant claim). non_triviality=2.

For 5.8.5: Leonov's note covers "mahārddhinām" gloss (ascetic-merit wealth per Śiromaṇi). The candidate note is about a DIFFERENT lemma ("durāsadam/durāvaram" variant reading) in the same verse — non-overlapping. Let me verify: Tilaka: "दुरासदम् पापिभिरिति शेषः । "दुरावरम्" इति पाठे शत्रुभिर्दुर्निवारमित्यर्थः" = "durāsadam = [inaccessible] by sinners (implied); in the reading 'durāvaram', it means unassailable by enemies." Matches note exactly. Faithful=2, non_triviality=2 (different lemma from Leonov's note on the same verse).

**5.8.7 (bhūtagaṇāḥ...vahanti)**: Bhūṣaṇa: "भूतगणाः गोपुरवाहका इव प्रतिमारूपेण स्थिताः । अन्यथा रावणान्तःपुरे पुरुषसञ्चारायोगात् कामगस्य विमानस्य वहनासंभवाच्च । यद्वा शिबिकावाहका इव भूतगणा अधोभागे वहन्ति । तद्वारैणैव कामगत्वमपि, चेतनप्रेरणं विना अचेतनसञ्चारस्यात्यन्तमनुचितत्वाच्च" = "the bhūta-gaṇas stand in image-form like gate-tower-bearers [gopura-vāhaka]; otherwise, since living men cannot move about in Rāvaṇa's inner apartments, and it would be impossible for the kāma-ga vimāna to be borne [by them]; or, the bhūta-gaṇas bear it below like palanquin-bearers — through this it has kāma-gatva [self-moving quality] too, since inanimate movement without a conscious mover would be entirely unfitting." This confirms the note's claim in full detail (statues at gates/gopuras, living men can't be in the harem, motion needs a mover). Faithful=2. non_triviality: Leonov's note for 5.8.7 covers "niśācarāḥ" meaning bhūtas can move day+night — different point from the statue/gopura explanation. non_triviality=2.

Anchoring: 5.8.2 bhusana/siromani match_verse=true (2) — tilaka's own pratika is content_anchor=true but matches_verse=false; since the Kataka claim is from tilaka specifically, anchoring=1 for that note. 5.8.5: tilaka matches_verse=true (2). 5.8.7: all three match_verse=true (2).

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\judgments\sarga_08.json
Now sarga 9 (6 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_09_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s09_verses.json
**5.9.3**: Bhūṣaṇa: "सर्वतः पुष्पकादन्यत्र सर्वत्र । पुष्पकारोहणस्य पश्चाद् वक्ष्यमाणत्वात्" = "'sarvataḥ' [means] everywhere except Puṣpaka; because ascending Puṣpaka will be narrated later." Matches note exactly. Faithful=2.

**5.9.10 (veśma)**: Tilaka: "वेश्म सस्त्रीकशयनगृहमिति कतकः। वेश्म पुष्पकाख्यमिति तीर्थः। अत्र तीर्थव्याख्या ज्यायसी" = "veśma = the bedroom with wife, says Kataka. Veśma = called Puṣpaka, says Tīrtha. Here Tīrtha's explanation is superior [preferred]." Confirms both named commentators AND Tilaka's own preference (for Tīrtha). Faithful=2. Excellent match.

**5.9.21**: Tilaka: "यत्तु पुष्पकस्यैव सा शाला तत इत्यस्य तदनन्तरमित्यर्थ इति, तच्चिन्त्यम्... मूलालयं दृष्ट्वा तद्बहिःस्थं पुष्पकमन्विष्य तत्स्थ एव रावणशयनगृहं तद्गृहवर्त्यनुमाय पुष्पकादवरुह्य तं प्रति स्थितस्तां ददर्शेत्येव न्याय्यमिति कतकः" — this is complex. Let me parse it carefully: it discusses that "if the hall (śālā) belongs to Puṣpaka itself, then 'tataḥ' means 'right after that'—this is questionable (cintyam)." Then it lays out Kataka's view: "having seen the main dwelling (mūla-ālaya), [Hanuman], then seeking out Puṣpaka standing outside it, having inferred Rāvaṇa's bedroom located there, having descended from Puṣpaka, stood facing it and saw that [hall]—this is proper, says Kataka." Then: "यत्त्वित्यादिनोक्ता व्याख्यैव युक्तेति मम भाति" = "the explanation stated by 'yat tu ityādi' [i.e., the view attributed just above, itself attributed to Kataka] seems to me [Tilaka] to be the correct one." Then cites later text ("avatīrya vimānāt") supporting this.

So actually it appears BOTH the "questioning of the śālā=Puṣpaka" idea AND the resolution (descend-then-see) are from **Kataka**, and Tilaka agrees with Kataka's view here — the note's phrasing "Катака полагал, что зал... часть самой виманы Пушпаки, но Тилака это отвергает" may have the attribution backwards. Let me re-read very carefully — the syntax is dense pūrvapakṣa/uttara style. Let me check this passage more carefully with fresh eyes.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\v921_tilaka.txt
Let me parse this in detail:

1. First sentence: Tilaka's own initial gloss — "having descended from Puṣpaka, [Hanuman] set out (prasthitaḥ) and saw that hall inferred by scent (as Rāvaṇa's bedroom)." This is Tilaka's OWN preliminary reading: descend from Puṣpaka first, then find the hall.

2. "यत्तु पुष्पकस्यैव सा शाला तत इत्यस्य तदनन्तरमित्यर्थ इति, तच्चिन्त्यम्" = "But the view that 'that hall belongs to Puṣpaka itself, and तत इत्यस्य means "immediately after that"' — **this [alternative view] is questionable (cintyam).**" This is presented as a view Tilaka is REJECTING (cintyam = "to be doubted/questioned").

3. "मूलालयं दृष्ट्वा ... इत्येव न्याय्यमिति कतकः" = "Having seen the main dwelling ... this alone is proper — says **Kataka**." — So Kataka's view (attributed by name here) is: descend-from-Puṣpaka-first, THEN see the hall — i.e., Kataka agrees with the "descend first" reading, NOT the "śālā=Puṣpaka" reading.

4. "यत्त्वित्यादिनोक्ता व्याख्यैव युक्तेति मम भाति" = "the explanation stated starting with 'yat tu...' [i.e., referring back to statement #2, the śālā=Puṣpaka view] seems fitting to ME [Tilaka]." 

Wait — this creates real ambiguity: does "यत्त्वित्यादिनोक्ता व्याख्या" refer back to the FIRST "yat tu" (statement #2, the rejected view) or does it just mean "the aforementioned explanation" generically referring to Kataka's view just stated? This is genuinely difficult Sanskrit commentarial cross-referencing. Given "मम भाति" (it seems to me) immediately follows Kataka's attributed view, and Sanskrit commentary convention is that the immediately preceding view is what's being endorsed unless explicitly marked otherwise, the more natural reading is that Tilaka is agreeing with **Kataka's view** just cited (descend-then-see), not reviving the earlier "cintyam" (questionable) view.

This means: the note's claim "Катака полагал, что зал... часть самой виманы Пушпаки, но Тилака это отвергает" (Kataka held that the hall was part of Puṣpaka, but Tilaka rejects this) — **may have the attribution wrong**. The текст suggests Kataka's actual explicit position is "descend-then-see" (matching, not contradicting Tilaka's preference), while the "śālā-is-part-of-Puṣpaka" view is anonymous/unattributed (marked with "yat tu" = "but some [view]") and is the one being rejected as "cintyam" — not explicitly Kataka's.

Given the genuine density and ambiguity of this passage, I should treat this as a faithfulness concern — the note asserts a specific named-authorship claim (Kataka holds the śālā=Puṣpaka view) that the text does not clearly support and may in fact contradict (Kataka is named as holding the OTHER view). This is a serious misattribution risk. I'll score faithfulness=0 for this note — it attributes a specific position to a named authority (Kataka) that the source text does not clearly assign to him, and plausibly assigns the opposite view to him instead. Verdict: reject.

Let's continue with the remaining three notes (5.9.46, 5.9.58, 5.9.68).

**5.9.46**: Tilaka: "वाहिताः किशोर्य इव कृतभारवहनाः श्रान्ताः किशोर्यो वडवा यथाध्वश्रमापनयनाय लुण्ठनेन व्यत्यस्तपल्ययनबन्धाः शेरते तद्वत्" = "'vāhitāḥ' like fillies who, having carried loads, tired, [lie down] and by rolling to relieve travel-fatigue, their harness-bindings become disarrayed — like that [these women sleep]." Matches note's claim precisely (fillies disarrange their own harness by rolling to rest, not that straps break from exhaustion per se). Faithful=2.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_s9_targets.json
Confirmed: Kostina's own note for 5.9.46 says exactly "Непонятно, почему у утомленных кобыл рвутся поводья" (unclear why exhausted mares' reins tear) — flagged as a confusion point. The candidate note's `complements_leonov` field is well-supported: it resolves exactly this confusion with Tilaka's mechanism (mares roll to relieve fatigue, thereby disarranging their own harness — not a causal "exhaustion→tearing" but "rest-behavior→disarray"). non_triviality=2, strongly justified.

5.9.10: Leonov's note is purely about "niryūha" (mattavāraṇa gloss + Goldman citation) — completely different from the candidate note's claim about "veśma" (Kataka vs Tīrtha dispute). non_triviality=2.

5.9.68: Leonov's note is about "daityāḥ"/"vipra" terms — unrelated to the candidate's claim about kāmavaśaṃ gatāḥ doctrinal defense. non_triviality=2.

Now let's verify **5.9.58** and **5.9.68** faithfulness:

**5.9.58**: Śiromaṇi: "अत्यर्थं सक्तमनस इत्यनेन रावण एव जिघ्रतीति तासामपि भ्रान्तिः सूचिता" = "By 'atyartham saktamanasaḥ' [it is] indicated that the delusion that it is Rāvaṇa himself smelling [them] is shared even by THEM [the women] too." Confirms note's claim precisely — the illusion is shared internally by the women themselves, not just an external comparison. Faithful=2.

**5.9.68**: Bhūṣaṇa: "तं कामयित्वा स्वयमेवागतास्ताः न तु तेन कामयित्वा हृता इत्यर्थः" = "having desired him, they themselves came voluntarily — not that he, having desired them, abducted them." Matches note's claim about Bhūṣaṇa (voluntary, not abducted). Śiromaṇi: "कन्या इत्युक्त्या रावणस्याधर्मसंसर्गाभावो ध्वनितः। तेन ब्रह्मराक्षसत्वादुक्तकन्याविवाहयोग्यत्वं रावणस्य ध्वनितम्" = "By saying 'kanyāḥ' [virgins/maidens], the absence of unrighteous [sexual] union by Rāvaṇa is implied. By this, due to his brahma-rākṣasa status, Rāvaṇa's eligibility to marry the said maidens is implied." Matches note's claim about Śiromaṇi (kanyāḥ implies no sin; brahma-rākṣasa status legitimizes marriage). Faithful=2 for both halves.

Now finalize contrastive/register/anchoring. Let me check Phase-1 for these six verses (already confirmed 0 hits earlier).

Anchoring: 5.9.3 bhusana matches_verse=true (2). 5.9.10 all three match_verse=true (2). 5.9.21 tilaka/bhusana matches_verse=true (2) — though the note is rejected on faithfulness anyway. 5.9.46 tilaka matches_verse=false (content_anchor=true) but note cites tilaka only for this claim → anchoring=1. 5.9.58 both siromani/bhusana matches_verse=true (2). 5.9.68 bhusana matches_verse=true, siromani matches_verse=false(content_anchor=true) — note cites both bhusana AND siromani → anchoring=1 (siromani's half unverified pratika, though plausible).

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\judgments\sarga_09.json
Now sarga 10 (9 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_10_candidates.json
9 dense notes. Let me pull the segmented bundle entries for all of them.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s10_verses.json
Let me check faithfulness one by one.

**5.10.7 (mahārajatavāsasam)**: Bhūṣaṇa: "महारजनवाससमिति पाठे कुसुम्भरागरञ्जिवस्त्रमित्यर्थः" = "in the reading mahārajanavāsasam, it means clothing dyed with kusumbha-rāga [safflower]." Matches note exactly. Faithful=2.

**5.10.12**: Tilaka: "परमोद्विग्नो ऽयं पापी देवीं हृतवानित्येतत्समीपे ऽवस्थानमनुचितमिति खिन्नचित्तो ऽपासर्पत्" = "greatly agitated [thinking] 'this sinner has abducted the goddess [Sita]', [feeling] that staying near him is improper, dejected-minded, he withdrew." This confirms Tilaka's explanation is about shame/impropriety of being near the abductor — note's characterization ("не страх, а стыд... кажется ему недостойным") is faithful, though Tilaka's actual text emphasizes moral revulsion/impropriety more than "shame" per se — a reasonable paraphrase. Now check Śiromaṇi's text — wait, this bundle only has `tilaka` and `bhusana` for this verse, NOT siromani! But the note's `source_commentary` lists `["tilaka", "siromani"]` and claims Śiromaṇi gives the compassion-based reading. Let me check carefully.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Confirmed: **no `siromani` key** in the bundle for 5.10.12 at all. The note attributes a specific compassion-based reading to Śiromaṇi ("«Широмани» же связывает волнение с тем, что Хануман... чувствует к нему сострадание"), but Śiromaṇi's text isn't present in this bundle for this verse — this is unverifiable/unfaithful, exactly analogous to the sarga-1 Tilaka case. Faithfulness=0 for this note.

**5.10.16 (vajracakrayor apy asādhyamṛtyuḥ)**: Tilaka: "वज्रचक्रयोरप्यसाध्यमृत्युरिति भावः" = "the idea is: even for vajra and cakra, [his] death is unachievable." This directly matches the note's core claim (both weapons couldn't kill him). Faithful=2.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_s10_targets.json
This is a **major** finding: **Leonov's own note for 5.10.12 ALREADY states the exact Śiromaṇi compassion reading the candidate claims to be adding as new** — "Автор «Широмани» полагает, что волнение Ханумана связано с тем, что он осознал, что величие Раваны будет уничтожено. [Е. Костина] «Мне кажется, если говорить про Широмани, то надо еще добавить, что Хануман из-за этого испытал сострадание...»" — this literally already gives BOTH the "Rāvaṇa's greatness will be destroyed" reading AND Kostina's own editorial suggestion to add "compassion" explicitly. The candidate note's claim about Śiromaṇi (compassion, foreseeing Rāvaṇa's death) is **not new** — it restates Leonov/Kostina's own note nearly verbatim, and moreover is doubly compromised because the Śiromaṇi text isn't even present in the segmented bundle for verification. This confirms both faithfulness=0 (unverifiable/unsourced attribution) AND non_triviality=0 (restates Leonov's own note, including Kostina's suggested addition). Verdict: **reject** (this is a clear case — the drafter should have caught this from Leonov's own note, which is stated as an explicit dedup baseline input per the drafting brief §3.3).

Continuing:

5.10.16: Leonov's note is trivial ("vajrollikhita — Опущено"). non_triviality=2 for the vajra/cakra-invincibility claim (genuinely new interpretive leap).

5.10.30/31: Leonov's notes are trivial omission-flags, unrelated to candidate claims. non_triviality=2 for both.

**5.10.25 (pānagandhapuraḥsaraḥ)**: Bhūṣaṇa: "निःश्वासस्य चूतादिसुरभित्वं तदधिवासितरसावल्यादिमधुसेवनात्" = "the fragrance of mango etc. in the breath [comes] from consuming honey-wine infused with those juices etc." Matches note exactly. Faithful=2.

**5.10.30 (puruṣaviśeṣaśvāsadharmaḥ)**: Tilaka: "अयं पुरुषविशेषश्वासधर्म इति कतकः। चूतादिसुरभित्वं तु तदधिवासितवस्तुसेवनात्... राक्षसत्वादेव वामाचारेण पूजाकरणान्मधुपानम्" = "this is a natural attribute of the breath of special men, says Kataka. But the mango-fragrance is [alternatively explained] from consuming that infused substance... [and] because of being a rākṣasa, wine-drinking [comes] from worship via vāma-ācāra [left-hand practice]." This confirms the note's claim precisely: Kataka's "innate quality" view vs. the wine-consumption view, PLUS the vāmācāra doctrinal framing. Faithful=2. Excellent match — note correctly attributes to Kataka (unlike 5.9.21's error), good.

**5.10.31 (amlānamālyābharaṇāḥ)**: Tilaka: "अम्लानमाल्याभरणाः देवकन्या इत्यर्थः" = "amlānamālyābharaṇāḥ means devakanyāḥ [celestial maidens]." Matches note exactly. Faithful=2.

**5.10.36 (nṛtyaśālinī... vāsanābalena)**: Tilaka: "नृत्यशालिनीति वासनाबलेन नृत्याभिनयोपेततया सुप्तवतीत्यर्थः" = "nṛtyaśālinī means: by force of vāsanā [habitual impression], being connected with dance-gesture-performance, she was sleeping [thus]." Matches note precisely. Śiromaṇi: "नृत्यशालिनी जाग्रद्वासनावशात् नृत्याश्रयीभूता प्रतीता ऽभवत्" = "nṛtyaśālinī — due to waking-vāsanā's force, she appeared as if engaged in dance." Also matches (vāsanā-based, not conscious dreaming). Bhūṣaṇa: quotes Bharataśāstra definition of aṅgahāra ("अङ्गानां योग्यदेशेषु हरणेन यथोचितम्..."), confirming the note's additional claim. Faithful=2.

**5.10.53 (na tv aucityālocanaṃ kṛtavān)**: Tilaka: "रूपयौवनसंपदा न त्वौचित्यालोचनं कृतवानिति भावः" = "by [her] endowment of beauty and youth [he thought this is Sita] — the idea is he did NOT consider propriety." Matches note exactly. Faithful=2.

**5.10.54 (sarvā apy etāś ceṣṭā upāṃśv iti bodhyam)**: Tilaka: "सर्वा अप्येताश्चेष्टा उपांश्विति बोध्यम्" = "all these actions should be understood as done softly/silently (upāṃśu)." Matches note precisely and completely (this is a direct quote). Faithful=2.

Now let's finalize non-triviality for the remaining (5.10.7, 5.10.16, 5.10.25, 5.10.36, 5.10.53, 5.10.54) and check Phase-1.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sundara_s10_targets.json
None of these Phase-1 entries overlap with the candidate's specific claims (mahārajatavāsasam variant reading; vajra/cakra invincibility). non_triviality=2 for both remaining verified ones (5.10.7 already established =2, 5.10.16 =2). No Phase-1 for 5.10.25/30/31/36/53/54, confirmed earlier all 0.

Now let's finalize contrastive_value and anchoring for all 9.

- 5.10.7: single commentator (bhusana variant reading) = 1.
- 5.10.12: rejected on faithfulness, moot but I'll still fill fields.
- 5.10.16: single commentator = 1.
- 5.10.25: single commentator = 1.
- 5.10.30: genuine 2-source contrast (Bhūṣaṇa/wine vs Kataka/innate) = 2.
- 5.10.31: single commentator = 1.
- 5.10.36: 2 commentators corroborating (not contrasting) same vāsanā point + Bhūṣaṇa's added definition = 1 (real exegetical gain, not a contrast).
- 5.10.53: single commentator = 1.
- 5.10.54: single commentator = 1.

Anchoring: 5.10.7 all match_verse=true=2. 5.10.12: tilaka matches, but siromani absent entirely (not just unmatched pratika — literally missing) — this is more severe than "unverified but plausible"; I'd actually treat this as anchoring=0 territory since there's no anchor at all for the Siromani claim, but since faithfulness already gates to reject, I'll note anchoring=0 in the reason too for completeness, matching the "misattributed/invented, no anchor available" case. 5.10.16: bhusana/siromani match, tilaka's own pratika fails (content_containment 0.0, no content_anchor flag) but the cited claim is from tilaka — anchoring=1 (weakly plausible, no content_anchor flag even, but no suggest_verse contradiction). 5.10.25: bhusana matches_verse=false, content_anchor=true — anchoring=1. 5.10.30: tilaka/bhusana both match=true — anchoring=2. 5.10.31: tilaka/bhusana match=true, siromani doesn't matter (not cited) — anchoring=2. 5.10.36: all three match=true — anchoring=2. 5.10.53: tilaka matches=true — anchoring=2. 5.10.54: tilaka matches=true — anchoring=2.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\judgments\sarga_10.json
I've now covered sargas 1-10. Let me record progress and continue with sargas 11-18. Let me mark a chapter transition since we've covered half.

- 🔧 `mcp__ccd_session__mark_chapter`
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_11_candidates.json
4 notes for sarga 11. Let me get the bundles.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s11_verses.json
**5.11.9**: Tilaka: "अन्यत्रपीत्यादिश्लोकद्वयं नव्याः प्रमादान्न पठन्ति" = "the pair of verses beginning 'anyatrāpi' — the moderns (navyāḥ), due to inattention, do not read [them]." Matches note's claim exactly (navyāḥ = "later [scholars/scribes]", pramādāt = through carelessness, na paṭhanti = don't read). Faithful=2. No Leonov note on 5.11.9 directly (Leonov's nearest is at 5.11.7). non_triviality=2.

**5.11.39**: Tilaka: "परदारपरिग्रहस्तद्वानतिपापी रावणश्च दृष्टः तादृशदर्शनमपि धर्मलोपकारीति भावः" = "the great sinner Rāvaṇa, who is the abductor-holder of another's wife, was seen — the idea is that even such seeing constitutes a dharma-violation." Matches note precisely. Śiromaṇi: "सीतापहारकः अयं रावणो मया दृष्टः एतेनैतद्दर्शनजनितपापस्य परिहारो न दृश्यते इति सूचितम्" = "'this Sītā-abductor Rāvaṇa was seen by me' — by this it is suggested that the removal of the sin born of this very seeing is not seen [i.e., no remedy is apparent]." Matches note precisely (no atonement visible). Faithful=2.

**5.11.40**: Śiromaṇi: "यत्नान्तरेण स्वामिकार्यस्यासाध्यत्वाच्चैतद्दर्शनमपि न दोषावहमिति निश्चयेन" = "and because the master's task is unachievable by another effort, by the resolve that even this seeing/viewing is not a fault-bringing (na doṣāvaham)..." Matches note exactly. Faithful=2.

**5.11.44**: Śiromaṇi: "यस्य सत्वस्य प्राणिनो या योनिः तस्यामेव तत्परिमार्ग्यते अत एव नष्टा प्रमदा मनुष्यस्त्री मृगीषु परिमार्गितुं न शक्यम्" = "whatever creature's origin/species, in that same [species] it should be searched — hence a lost woman cannot be searched for among deer." Matches note precisely (sajātīya-search principle). Faithful=2.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_s11_targets.json
Leonov's note for 5.11.40 is a different, more general gloss ("able to determine what should/shouldn't be done") than the candidate's specific claim (the "yatnāntareṇa" necessity argument that resolves the moral doubt). Genuinely distinct addition. non_triviality=2 for 5.11.40. No Leonov notes for 5.11.9, 5.11.39, 5.11.44 (confirmed, only 1 hit total). Let me verify Phase-1 hasn't a relevant hit — the `_meta.caveats` field already flags that Phase-1 verse_ids for this sarga are largely misnumbered/irrelevant, and lists which ones ARE relevant (V.11.3 tridaśa, V.11.5 klānta, V.11.30 astra, V.11.38 paradāra/dharmalopa) — none of these match our 4 candidate verse_ids (9, 39, 40, 44) except possibly V.11.38 is adjacent to 5.11.39. Let me check that specific one since it may bear on non-triviality of 5.11.39.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\v1138.json
This is at V.11.38 (a different verse, one before), which discusses Śiromaṇi's own similar text "परदारावरोधस्य दृष्टस्य निरीक्षणं धर्मलोपं करिष्यति" seen in the 5.11.40 bundle's siromani text ("परदारावरोधस्य परस्त्रीसमूहस्य निरीक्षणं धर्मलोपं करिष्यति") — this is a cross-textual Manu-citation note about the general dharmalopa concept, not the specific "seeing Rāvaṇa himself = irredeemable sin" claim of candidate note 5.11.39. Genuinely distinct — non_triviality remains 2 for 5.11.39 (the specific Tilaka/Śiromaṇi content about seeing Rāvaṇa himself, not the general paradāra-avarodha concept, is what's new).

Now let's finalize contrastive_value/anchoring: 5.11.9 single commentator=1. 5.11.39: two commentators but not really "contrasted" — they build on each other (Tilaka: seeing Rāvaṇa is a dharma-violation; Śiromaṇi: no remedy visible) — this is corroborating/extending, not contrasting; I'll call contrastive_value=1 (real exegetical gain, single line of thought advanced by two commentators). 5.11.40 single=1. 5.11.44 single (siromani primarily, bhusana just quotes verse text) =1.

Anchoring: 5.11.9 tilaka matches=true(2). 5.11.39: bhusana/tilaka match=true, siromani matches_verse=false(content_anchor=true) — note cites tilaka+siromani → anchoring=1 (siromani unverified). 5.11.40: both match=true(2). 5.11.44: both match=true(2).

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\judgments\sarga_11.json
Now sarga 12 (3 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_12_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s12_verses.json
Important discrepancy: The candidate note 5.12.4 claims Tilaka's content ("«Тилака» добавляет неявную психологическую мотивировку: если Равана и не убил её сам, то либо из влечения к ней (anurāgāt), либо из страха греха убийства женщины (strīvadhadoṣāt)"). But the bundle for 5.12.4 only has **bhusana** and **siromani** — no `tilaka` key at all! Let me check.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Confirmed: **no `tilaka` key** for 5.12.4. The note's `source_commentary: ["tilaka"]` and its entire claim about "anurāgāt / strīvadhadoṣāt" cannot be verified against the bundle — Tilaka's text is absent. Let me double check the actual bhusana/siromani text doesn't happen to contain this content under a different label — searching for "अनुराग" (anurāga) or "स्त्रीवध" (strīvadha) in the texts shown: neither bhusana nor siromani text for 5.12.4 mentions anurāga or strīvadhadoṣa at all — they discuss the physical appearance of the rākṣasī women (virūpa, vikṛta, mahānana, etc.), completely different content from the note's claim. This is a clear faithfulness violation — invented/misattributed content not entailed by the cited (or even any available) text. Faithfulness=0, verdict=reject.

**5.12.2 (aghaṭitaghaṭanāpaṭīyastvam)**: Bundle has only tilaka/bhusana for verse 2, no siromani! But the note's `source_commentary: ["siromani"]` and its entire claim attributes content to Śiromaṇi. Let me check.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Confirmed: **no `siromani` key** for 5.12.2 either. Also, "aghaṭitaghaṭanāpaṭīyastvam" is not mentioned anywhere in the tilaka/bhusana texts shown (they discuss the na dhriyate/mriyate variant reading, not this compound). This is a clear invented claim, unverifiable and seemingly fabricated. Faithfulness=0, verdict=reject.

**5.12.22 (nāgakanyā balād dhṛtāḥ)**: Bundle has only **bhusana**, no tilaka! Note's `source_commentary: ["tilaka", "bhusana"]` claims both comment independently on the wives/prisoners distinction, but Tilaka isn't in the bundle at all.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Confirmed: no `tilaka` key for 5.12.22. And the bhusana text shown ("प्रमथ्य राक्षसेन्द्रेण नागकन्या बलाद्धृताः...") is a bare verse-repetition with NO exegetical comment at all — it doesn't discuss ūḍhānām vs balād-dhṛtāḥ distinction, doesn't mention bandīkṛtānām. This note's claim is entirely unsupported by the cited text (both the Tilaka attribution is absent, and even Bhūṣaṇa's actual text doesn't contain the claimed exegesis). Faithfulness=0, verdict=reject.

This is a striking pattern for sarga 12 — all three notes appear to have fabricated or misattributed content not traceable to the bundle text. Let me double-check I'm not missing something by re-reading the raw candidates file once more to make sure I have the right verse_ids matched.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Confirmed matches. All three sarga-12 notes fail faithfulness due to either absent-commentator citations or content not traceable to the actual bundle text. Let me note this is a serious quality signal worth flagging in the summary (this sarga's notes may share a systematic drafting issue — possibly the drafter looked at a different/wider commentary source than what ended up in the segmented bundle, or hallucinated).

Non-triviality/contrastive/register/anchoring are moot for reject verdicts, but I'll fill reasonable values for completeness per the schema.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_s12_targets.json
Interesting — Kostina's own note at 5.12.22 explicitly poses exactly the two questions the candidate note purports to answer ("являются ли дочери нагов в ст. 21 и 22 разными группами" / "Ранее говорилось, что Равана никого силой не удерживал"). This confirms the drafter correctly identified a genuine open question worth answering — but the answer it supplied isn't traceable to actual cited commentary text in the bundle (Bhūṣaṇa's text is bare verse repetition with no exegesis, and Tilaka isn't present at all). This is a case where the underlying reasoning is plausible/desirable but the specific commentarial sourcing is fabricated — still a faithfulness violation per the rubric ("misattributed commentator, invented gloss... ⇒ 0").

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\judgments\sarga_12.json
Now sarga 13 (11 notes) — the largest remaining set.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_13_candidates.json
Given the sarga-12 pattern found, I'll be extra careful checking these 11 notes' commentator-key presence first before deep semantic checks.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Good news — all cited commentators are present in their respective bundles for sarga 13 (unlike sargas 1/9/12). Now let's do content-level faithfulness verification.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s13_verses_a.json
**5.13.1**: Tilaka: "प्राकारस्येन्द्रनीलकृतत्वमनेन ध्वन्यते" = "the wall's construction from indranīla [sapphire] is implied by this [comparison]." Matches note exactly. Faithful=2.

**5.13.6**: Tilaka: "पूर्वदृष्टां मन्दोदरीं सौन्दर्यादिगुणैः पुनः सीतात्वेन संभाव्य तन्निरासकवाक्यम्" = "this statement negates the possibility, previously entertained due to beauty etc., of the earlier-seen Mandodarī being Sītā." Then Tilaka's three-epithet gloss: "सा मैथिली सा सीता लाङ्गलपद्धतिजत्वेनायोनिजा। वैदेही जगत्प्रशस्तविदेहवंशसंबद्धा। जनकात्मजा ब्रह्मवित्पुत्री" — matches note's claim about the three epithets (Maithilī by conduct not by birth-from-furrow — wait, actually text says "ayonijā" = not-born-from-womb via plough-furrow, which is about Sītā's mythic origin, not "conduct" per se; let me recheck: "सा मैथिली सा सीता लाङ्गलपद्धतिजत्वेनायोनिजा" — this seems to attach "ayonijā" (not womb-born) to Sītā generally via the plough-furrow-origin myth, and doesn't clearly connect Maithilī specifically to "conduct" (ācāra). Let me check Bhūṣaṇa's parallel gloss: "मैथिली आचारप्रधानकुलोत्कर्षवती" = "Maithilī = possessing the excellence of a lineage where conduct (ācāra) is paramount." This DOES match the note's claim ("Майтхили — по роду поведения") but it's from **Bhūṣaṇa**, not explicitly Tilaka in this precise phrasing — though Tilaka's version is compressed/different structure. The note attributes all three epithet-glosses to "Тилака" specifically. Given Bhūṣaṇa's parallel text gives the cleaner three-way split (ayonijā/janmabhūmi-prayukta-atiśayavatī/ācāra-pradhāna-kula-utkarṣavatī) matching almost exactly what the note describes, while Tilaka's own phrasing is a bit different in structure ("लाङ्गलपद्धतिजत्वेनायोनिजा" = born through plough-furrow, not-womb-born — this actually explains ayonijā via the furrow myth rather than assigning it as a name-gloss)... 

This is subtle. The note says: "Тилака попутно разбирает три эпитета: Майтхили — по роду поведения (не по рождению из борозды), Вайдехи — по славе видехийского рода, дочь Джанаки — как дочь мудреца-брахмавида." Let me re-parse Tilaka's exact text once more: "सा मैथिली सा सीता लाङ्गलपद्धतिजत्वेनायोनिजा । वैदेही जगत्प्रशस्तविदेहवंशसंबद्धा । जनकात्मजा ब्रह्मवित्पुत्री" — This reads as: "she [is called] Maithilī, she [is] Sītā, [who is] ayonijā (not born from a womb) due to being born from the plough-furrow. Vaidehī [means] connected to the world-renowned Videha lineage. Janakātmajā [means] daughter of the knower-of-Brahman [Janaka]." 

So actually Tilaka's text doesn't gloss "Maithilī" as "by conduct" — it glosses **Sītā** as ayonijā (via furrow-birth), and treats Maithilī/Sītā as coreferential labels in the same clause, without an explicit "conduct" etymology for Maithilī specifically. The "conduct" (ācāra-pradhāna-kula) explanation for Maithilī is Bhūṣaṇa's, not Tilaka's, in this bundle. This means the note's attribution of "Майтхили — по роду поведения (не по рождению из борозды)" to Tilaka is **not accurately sourced** — it's conflating Tilaka's and Bhūṣaṇa's distinct glosses into one, attributed solely to Tilaka. This is a faithfulness overreach — the "не по рождению из борозды" contrastive framing (implying Tilaka explicitly rejects furrow-birth for Maithilī specifically) actually inverts Tilaka's own point (Tilaka affirms furrow-birth as the reason for ayonijā, doesn't use it to explain Maithilī specifically, and doesn't contrast it against a "conduct" reading for Maithilī).

Given `source_commentary` lists `["tilaka", "siromani"]` (not bhusana), and the specific three-epithet breakdown as described is actually a MIX of Tilaka's and Bhūṣaṇa's texts misattributed solely to Tilaka — I'll score this as a moderate overreach: faithfulness=1 (minor wording overreach: the epistemic content is *roughly* there across the bundle's commentators collectively but the specific attribution and the "не по рождению из борозды" framing for Maithilī is not accurately what Tilaka's text says).

The rest of the note (Mandodarī episode being the concrete occasion, and Śiromaṇi's "этим показано, что она не Сита") is well confirmed: Śiromaṇi: "दृष्टमन्दोदरीं सीतात्वेनाशङ्क्य निराकरोति... एतेन सा न सीतेति सूचितम्" = "having suspected the seen Mandodarī to be Sītā, [Hanuman] negates [this]... by this it is indicated that she is not Sītā." This part is faithful.

Given the overall note mixes a well-supported main claim with a partially misattributed/conflated secondary detail, I'll score faithfulness=1 → verdict `edit` (register-fixable per the rubric's framing, but here it's more a "reason overreach fixable by adjusting attribution" — the rubric says faithfulness=1 with fixable wording → edit).

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_s13_targets.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s13_verses_b.json
**5.13.8**: Bhūṣaṇa: "सागरं प्रेक्ष्य भीतं हृदयं सागरे पतितमिति मन्ये। हृदयस्य भयस्थानत्वेन तन्मूलतया तच्छरीरं लक्ष्यते" = "seeing the ocean, [her] frightened heart, I think, fell into the ocean; since the heart is the seat of fear and [her] body-root, the body is thereby signified [i.e., her death]." Confirms note's claim (metonymy — heart as fear-seat, signifying body/death). Śiromaṇi: "हृदयं मनः पतितम् उत्क्रान्तं मनउत्क्रमणस्य मरणत्वान्मृतेत्यर्थः" = "heart = mind departed/ascended-out; since departure-of-mind means death, [it means] she died." Confirms note's claim (manaḥ-utkramaṇa = death doctrine). Faithful=2.

**5.13.13**: Tilaka names Kataka explicitly: "इत्यादि श्लोकद्वयं प्रक्षिप्तमिति कतकः" = "this pair of verses [is] interpolated, says Kataka." Matches note precisely (correctly attributed this time). Faithful=2.

**5.13.15**: Śiromaṇi: "पञ्जरस्था सारिका इव भृशं लालप्यते मरणभावपरीक्षार्थं किंचित् वक्तुं प्रेर्यते" = "like a caged mynah, she wails intensely, being compelled to utter something for the purpose of testing whether death has occurred (maraṇa-bhāva-parīkṣā-artham)." Matches note exactly. Faithful=2.

**5.13.18**: Bhūṣaṇa: "दोषः स्यादनिवेदने यथावृत्तानिवेदने स्वामिवञ्चनदोषः स्यात्" = "the fault in non-reporting: if [what] actually happened is not reported, it would be the fault of deceiving the master." Śiromaṇi: "निवेद्यमाने... दोषो मिथ्यासंसर्गित्वं स्यात्। अनिवेदने ऽपि दोषः मूर्खत्वादिः स्यात्" = "in reporting... the fault would be entanglement in falsehood (unverified); in not-reporting too, the fault would be foolishness." Matches note exactly, both halves. Faithful=2.

**5.13.42**: Bhūṣaṇa: "लिङ्गिनीम्, लिङ्गं संन्यासः अनशनं तद्वती लिङ्गिनी ताम् साधयिष्यतः। लिङ्गिनमिति क्वचित्पाठः। तत्र लिङ्गं शरीरं तद्वान् लिङ्गी आत्मा तं साधयिष्यतः, शरीरादात्मानां मोचयिष्यत इत्यर्थः" = "liṅginīm — liṅga = renunciation/fasting-possessing one (liṅginī), whom [he] will accomplish. In some texts the reading is liṅginam — there liṅga = body, liṅgī possessing it = the self (ātman), whom he will accomplish, meaning he will free the self from the body." Matches note's two-reading split for Bhūṣaṇa precisely. Śiromaṇi: "लिङ्गिनम् ऊर्ध्वगतिसाधकचिह्नं सम्यक् साधयिष्यतः" = "liṅginam = the sign/mark that accomplishes upward movement [in the afterlife]." Matches note's claim about Śiromaṇi's posthumous-ascent-marker reading precisely. Faithful=2.

**5.13.44**: Bhūṣaṇa: "सुजातमूला आदौ लङ्काधिदेवताजयेन शोभनप्रारम्भा" = "sujātamūlā = having a good beginning through the earlier victory over Lanka's presiding deity." Matches note exactly. Śiromaṇi: "सुजातमूला सुजातं रामसुग्रीवसंबन्धहेतुकवार्ताहरत्वेन निष्पन्नं मूलं यस्याः... मुद्रिकादानोपलक्षितरामप्रीतिपात्रत्वहेतुकातियशोविशिष्टा" = "sujātamūlā = whose root is well-formed through being the bearer of the news that caused the Rāma-Sugrīva connection... possessing great fame due to being the object of Rāma's favor, marked by the giving of the ring." Matches note's claim (news connecting Rāma/Sugrīva, ring-token of gratitude). Faithful=2.

**5.13.50**: Bhūṣaṇa: ""इमं पशुं पशुपते ते अद्य बध्नामि अग्रे" इति श्रुतेः। अनेन सुप्रापत्वमुक्तम्" = "'this animal, O Paśupati, I now first bind for you' — per the śruti [Vedic mantra]. By this, [Rāvaṇa's] easy-attainability is stated." Matches note exactly, including the "лёгкость пленения" point. Faithful=2.

**5.13.59**: Tilaka: "अनेन रामस्य भगवदवतारत्वं सूचितम्। रूद्रादिनमस्कारेण। विराजो भगवतो नतिः" = "by this [ordering], Rāma's status as an avatar of the Lord is indicated. Through the salutation to Rudra etc. — the great gods' homage [is in fact] homage to the Lord." Matches note exactly. Faithful=2.

**5.13.62**: Tilaka: "अत्र ध्रुवं रक्षोबहुलेत्युत्प्रेक्षया चन्द्रास्तः सूचितः। अन्यथा तत्प्रकाशेन निश्चय एव स्यात्" = "here, 'certainly rākṣasa-abundant' is by poetic fancy (utprekṣā) — the moon's setting is thereby indicated; otherwise, by its [the moon's] light, it would simply be a certainty [not a guess]." Matches note precisely. Faithful=2.

Now let's check Leonov/Phase-1 baselines for non-triviality.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_s13_targets.json
Interesting for 5.13.13: Leonov/Kostina's note discusses editions (Bombay vs Gita-press), which is a DIFFERENT textological issue than the candidate note's claim (Kataka's interpolation judgment). The candidate's `why_proposed` explicitly notes this distinction ("отличное от вопроса об изданиях, поднятого Костиной"). Confirmed non-duplicative. non_triviality=2.

For 5.13.18: Leonov's note only glosses the "nivedyamāne doṣaḥ" half (why telling is bad — because it would cause Rāma's death) — a DIFFERENT explanation from the candidate's claim (svāmivañcanadoṣa = deceiving the master). This is actually a genuinely different reason for the same half of the dilemma! Both are plausible, non-duplicative. non_triviality=2, since the candidate's Bhūṣaṇa-based reason and Śiromaṇi's two-fault breakdown are distinct from Leonov's own explanation.

For the others (5.13.1, 5.13.8, 5.13.15, 5.13.42, 5.13.44, 5.13.50, 5.13.59, 5.13.62) — Leonov notes are either absent or trivial/unrelated (5.13.8 is just a term-flag placeholder, 5.13.15 is a bird-species gloss unrelated to the "self-test" claim). non_triviality=2 for all.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sundara_s13_targets.json
Different lemmas/topics (pañcatva etymology, sārikā bird lore, hriyamāṇā cross-text) — none duplicate candidate claims (heart-fall metonymy; self-check wailing). non_triviality remains 2 for all.

Now let's finalize contrastive_value and anchoring for all 11 sarga-13 notes.

- 5.13.1: single commentator = 1.
- 5.13.6: mixed edit case, contrastive: not really "≥2 genuinely contrasted" since it's Mandodarī-episode + epithet listing; I'd call this 1 (single narrative point + attribution issue).
- 5.13.8: 2 commentators, both giving compatible (not contrasting) explanations of the same figure = 1 (real exegetical gain, not opposition).
- 5.13.13: single = 1.
- 5.13.15: single = 1.
- 5.13.18: genuine 2-commentator distinct-content contrast (different reasons for each horn of dilemma) = 2.
- 5.13.42: genuine textual-variant 3-way contrast (liṅginī/liṅginam×2 readings) = 2.
- 5.13.44: genuine 2-commentator contrast (different origin stories for kīrtimālā) = 2.
- 5.13.50: single = 1.
- 5.13.59: single = 1.
- 5.13.62: single = 1.

Anchoring: 5.13.1 tilaka/bhusana match=true(2). 5.13.6 all three match=true(2) — but faithfulness issue on attribution, doesn't affect anchoring. 5.13.8 bhusana match=true, siromani matches_verse=false(content_anchor=true) → anchoring=1. 5.13.13 tilaka/bhusana match=true, siromani not cited for the Kataka claim (only tilaka is `source_commentary`, but note lists source as `["tilaka"]` only) → anchoring=2. 5.13.15 both match=true(2). 5.13.18 both match=true(2). 5.13.42 tilaka/bhusana match=true; siromani cited? source_commentary=["bhusana","siromani"] — siromani matches_verse=false(content_anchor=true) → anchoring=1. 5.13.44 all three match=true(2). 5.13.50 bhusana match=true(2). 5.13.59 tilaka match=true(2). 5.13.62 both match=true(2).

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\judgments\sarga_13.json
Now sarga 14 (5 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_14_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Good, all citations present in bundles. Let's inspect the content.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s14_verses.json
**5.14.3 (bhavyāṃś ca)**: Bhūṣaṇa: "भव्यान् शभानित्यशोकविशोषणम्। यद्वा भवं रुद्रमर्हन्तीति भव्यान् रुद्रप्रियपुष्पान् वृक्षविशेषान्" = "bhavyān — [means] 'auspicious/beautiful' — this is an epithet of aśoka; OR [alternatively], 'bhavaṃ rudram arhanti' = they are worthy of/suited to Rudra, [so] bhavyān = a particular tree species with flowers dear to Rudra." Matches note exactly. Faithful=2.

**5.14.12 (sarvāṇi bhūtāni)**: Śiromaṇi: "सर्वाणि भूतानि रक्षांसि वसन्तः कपिरूपेण समागतऋतुराजो ऽयमिति मेनिरे" = "'sarvāṇi bhūtāni' = the rākṣasas; [they] thought 'this is spring-king itself come in monkey-form'." Matches note exactly (bhūtāni specifically identified as the rākṣasa guards). Faithful=2.

**5.14.43 (aśokavanikā)**: Śiromaṇi: "सेयमशोकवनिका शोकनिवर्तिकात्वेन तदभिधा अतः इमां जानकी नूनमेष्यति। एतेनैतन्नामश्रुत्या तत्र गमने ममापि शोकविध्वंसो भवितेति निश्चयवती सीतावश्यं भवेदिति सूचितम्" = "this aśoka-vanikā [has] that name due to being 'śoka-nivartikā' [grief-averting]; therefore Jānakī will certainly come here. By this it is indicated that Sītā, being confident that hearing this name and coming there her grief too will be destroyed, will surely come [here]." Matches note's wordplay claim precisely. Tilaka: "रम्येयमशोकवनिका दुरात्मनो रावणस्यैव दृढं ध्रुवम्। राक्षसान्तरस्यैवंविधतदसंभवात्" = "this lovely aśoka-vanikā is certainly Rāvaṇa's own — since such a thing would be impossible for another rākṣasa." Matches note's claim about Tilaka. Faithful=2.

**5.14.46 (vanasyāsya vicakṣaṇā)**: Śiromaṇi: "एतेन केनचिद्रूपेण कश्चिद्रामानुचरो मदन्वेषणार्थं तत्रागच्छेदिति सीतासंभावना सूचिता" = "by this it is suggested that Sītā's expectation [is] that in some form, some follower of Rāma will come there to search for her." Matches note exactly. Faithful=2.

**5.14.49 (saṃdhyākālamanāḥ)**: Tilaka: "तत्र कर्तव्यस्नानादौ चास्त्येव स्त्रीणामप्यधिकार इति कथं स्त्रीणां सन्ध्यावन्दनमिति परास्तं वेदितव्यम्। किं च सम्यग्भगवद्ध्यानस्यैव सन्ध्यापदार्थत्वेनास्त्येव तत्र स्त्रिया अधिकारः। गायत्रीमन्त्रेण तदर्थस्मरणपूर्वकध्याने तु द्विजस्यैवाधिकार इत्यन्यत्" = "there [in] the bathing etc. to be performed, women too have a right — thus [the objection] 'how can women perform saṃdhyā-vandana' should be understood as refuted. Moreover, meditation on the Lord itself being the meaning of saṃdhyā, there too women have a right; but in meditation preceded by remembering that meaning via the Gāyatrī mantra, only the twice-born have the right — this is another matter." Matches note precisely (women can do the bathing/general meditation part; only dvija get Gāyatrī-mantra meditation). Faithful=2.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_s14_targets.json
Confirmed all Leonov notes are unrelated to candidate claims (5.14.3: champaka gloss, not bhavya; 5.14.12: Goldman citation, not "who exactly is bhūtāni"; 5.14.49: general saṃdhyā-timing gloss + śyāmā-age gloss, not the women's-right doctrinal argument). No Phase-1 for these five (already confirmed). non_triviality=2 for all 5.

Contrastive_value: 5.14.3 single=1. 5.14.12 single=1. 5.14.43: 2 commentators giving different but complementary points (Śiromaṇi=wordplay hope-basis, Tilaka=ownership certainty) — not opposing readings, so I'll call this 1 (real exegetical gain from combination). 5.14.46 single=1. 5.14.49 single=1.

Anchoring: 5.14.3 bhusana match=true(2) (tilaka not cited). 5.14.12 siromani match=true(2). 5.14.43 all three match=true(2). 5.14.46 both match=true(2). 5.14.49 both match=true(2).

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\judgments\sarga_14.json
Now sarga 15 (2 notes) — quick.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_15_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s15_verses.json
**5.15.41**: Bhūṣaṇa's actual verse text at 41 reads "गात्रशोभीनि" **replaced by** "शाखाशोभीनि" — wait, let me look carefully: the verse block shows Bhūṣaṇa's quoted verse line as "तान्याभरणजालानि शाखाशोभीन्यलक्षयत्" (śākhāśobhīny), and glosses: "शाखायां शोभन्त इति शाखाशोभीनि। भर्तृविरहकाले भूषणधारणस्यानुचितत्वत् स्वाङ्गेभ्य उन्मुच्य शाखायां न्यस्तानीत्यर्थः" = "śākhāśobhīni = shining on the branch; since wearing ornaments is improper during separation from the husband, [she] removed them from her limbs and placed them on the branch." This confirms the note's claim about Bhūṣaṇa's variant reading exactly (śākhāśobhīni, meaning ornaments hung on a branch by Sītā herself). Faithful=2.

**5.15.47**: Tilaka: ""गात्रशोभीनि" इति पाठः कतकसंमतः... तीर्थस्तु-- "शाखाशोभीनि" इति पाठं प्रकल्प्य रामविश्लेषसमये भूषणधारणस्यानुचितत्वाद्वैदेह्या भूषणानि स्वाङ्गेभ्य उन्मुच्य शाखायां न्यस्तानीति गम्यत इति व्याचख्यौ, तत्तूत्तरश्लोकयोर्हस्तेष्विति तथा श्यामानि चिरयुक्तत्वादिति पदस्वरसविरुद्धम्" = "the reading 'gātraśobhīni' is approved by Kataka... but Tīrtha, adopting the reading 'śākhāśobhīni,' explained... but this contradicts the natural sense of the words in the next two verses, [where ornaments are described as] 'on the hands' and 'darkened from long wear'." This matches the note's claim exactly — Kataka supports gātraśobhīni, Tīrtha supports śākhāśobhīni, and Tilaka rejects Tīrtha's reading citing the internal-consistency argument (darkened-from-wear, on-the-hands in subsequent verses). Faithful=2. Excellent precise match, correct attribution (Kataka/Tīrtha both explicitly named and positions correctly assigned).

Non-triviality: no Leonov notes on either verse; one Phase-1 hit — let's check it.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sundara_s15.json
Different angle (evidentiary/legal function of ornaments generally) — doesn't overlap with the specific textual variant claim. non_triviality=2 for both.

Contrastive_value: 5.15.41 single commentator variant reading = 1. 5.15.47: named two-way scholarly dispute (Kataka/Tīrtha) resolved by Tilaka = 2 (genuine named contrast with resolution). Anchoring: both all-match=true=2.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\judgments\sarga_15.json
Now sarga 16 (1 note) — quick.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_16_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s16_v5.json
This confirms the drafter's own caveat: the bundle's `bhusana` text for verse 5 is a bare verse repetition with NO commentary/gloss whatsoever — no mention of Viṣṇu-smṛti, no age-ratio numbers (16/12, 24/8), nothing about "tulyavayas" norms. The note's claim entirely fails to match the cited bundle text. The note itself flags this ("анкоринг: фрагмент сегментатора без pratika_check... атрибутировано туда, а не как отдельный стих") — acknowledging the content likely belongs elsewhere, but the content itself (Viṣṇu-smṛti citation with specific age numbers) simply isn't present anywhere in this bundle. This is an invented/unverifiable claim. Faithfulness=0.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_s16.json
This also confirms that Leonov's own note ALREADY covers exactly this ground (the age-appropriateness point, husband older, 4-year difference) — the candidate note's specific addition (Viṣṇu-smṛti citation, specific numeric ratios) would have been a genuine addition IF the underlying commentary text supported it, but since the bundle's cited text doesn't contain this citation at all, it's unverifiable. Given both the anchor issue AND the fact that Leonov's own note already substantially covers the terrain being elaborated, this note fails both the faithfulness gate and would likely fail non-triviality too since the drafter's own reasoning shows awareness this is a stretch. Verdict: reject.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\judgments\sarga_16.json
Now sarga 17 (2 notes) — quick.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_17_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s17_verses.json
**5.17.22**: Bhūṣaṇa: "चन्द्ररेखायाः स्पष्टास्पष्टत्वद्योतनायेदं विशेषणम्" = "this qualifier [śāradābhrair ivāvṛtām] is for indicating the moon-crescent's clarity-unclarity (spaṣṭa-aspaṣṭatva)." Matches note's core claim about the "visible/invisible" paradox motif exactly. But the note also claims this "prepares" a formula stated "three verses later" at 5.17.25 ("не сияет и все же сияет") — this is an added interpretive/compositional-linkage claim by the drafter that isn't explicitly stated in Bhūṣaṇa's text (Bhūṣaṇa doesn't cross-reference verse 25). Let me check if 5.17.25's content matches to see if this compositional claim, while not stated by Bhūṣaṇa, is at least accurate as an observation.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s17_v25.json
Confirmed: verse 25 does contain "vibhāti ca na bhāti ca" (shines and doesn't shine) — the exact "sияет и все же сияет" formula. The note's observation about the moon-crescent qualifier at 5.17.22 anticipating this at 5.17.25 is a genuine, verifiable compositional/thematic link that the drafter identified between two verses of the SAME bundle. This is not "invented" — it's the drafter's own inferential note about compositional structure, clearly labeled as the drafter's observation, not attributed as a direct quote from Bhūṣaṇa's text. Since the core factual claim about Bhūṣaṇa's spaṣṭāspaṣṭatva gloss IS faithful, and the added compositional link is a defensible literary observation (verifiable independently), I'll treat this as faithful=2 — the note doesn't misattribute the "3 verses later" observation to Bhūṣaṇa, it's phrased as the note's own synthesis ("Сравнение с луной здесь заранее готовит эту формулу" — presented as the note's own analytical conclusion, drawing on the bundle's own subsequent verse, not as Bhūṣaṇa's claim). This is legitimate exegetical synthesis grounded in the actual text, a strength rather than a flaw.

**5.17.32**: Bhūṣaṇa: "संवृतः राक्षस्यदर्शनाय शिंशुपापर्णैर्गूढो ऽभूत्" = "saṃvṛtaḥ = he became hidden by śiṃśupā-leaves, for [avoiding] being seen by the rākṣasīs." Śiromaṇi: "संवृतः शाखाविशेषे निलीनो ऽभवत्" = "saṃvṛtaḥ = he became concealed in a particular branch." Matches note's claims for both commentators exactly (though note frames Bhūṣaṇa's exact phrase as "скрыт листьями шимшапы" — matches precisely; and Śiromaṇi's "укрылся в одной из её ветвей" — matches "śākhā-viśeṣe" reasonably). Faithful=2.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sundara_s17.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sundara_s17b.json
Different topic (namaskāra as a formulaic ritual gesture, cross-referenced to Gita) — doesn't overlap with the candidate's specific claim about *where* Hanuman hides. non_triviality=2 for both notes.

Contrastive_value: 5.17.22 single=1. 5.17.32: 2 commentators corroborating (not contrasting) same concealment fact with slightly different phrasing = 1. Anchoring: 5.17.22 bhusana match=true(2). 5.17.32 both match=true(2).

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\judgments\sarga_17.json
Now the final sarga, 18 (7 notes).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_18_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
All citations present in bundles. Let's check content.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\s18_verses.json
**5.18.1**: Tilaka: "विचिन्वतस्तस्याः स्पष्टदर्शनाय राक्षसीनिद्रारूपमवसरमन्वेषयतः" = "seeking her out, for clear-seeing her, [he was] searching for the occasion in the form of the rākṣasīs' sleep." Matches note exactly. Faithful=2.

**5.18.11**: Tilaka: "अनेन लङ्कायां हेमन्तशिशिरयोरपि शीताभावो ध्वनितः" = "by this, the absence of cold even during hemanta and śiśira [winter seasons] in Lanka is implied." Matches note exactly. Faithful=2.

**5.18.12 (bṛsī)**: Tilaka: "बृसीरासनविशेषान् तपस्विनामिमे तृणादिना, अस्य तु स्वर्णेनेति विशेषः" = "bṛsīḥ = particular seats; for ascetics these [are made] of grass etc., but for this one [Rāvaṇa's retinue] the distinction is that they are of gold." Matches note exactly (contrast between ascetic-grass norm and gold luxury here). Faithful=2.

**5.18.18 (bahumānāc ca kāmāc ca)**: Tilaka: "बहुमानाद्भर्तृकृतसंमानात्। कामात्स्वीयात्" = "bahumānāt = from the respect done BY THE HUSBAND [Rāvaṇa]; kāmāt = from their OWN desire." This confirms the note's claim precisely — bahumāna is Rāvaṇa's act toward them, kāma is their own. Faithful=2.

**5.18.22 (dīpikābhir anekābhiḥ)**: Tilaka: "रात्रिशेषसत्त्वात् द्वादश्यां यामावशिष्टरात्रौ चन्द्रस्यास्तगमनाच्च" = "because part of the night remains, on the twelfth [tithi], during the last watch of the remaining night, and because the moon has set." Matches note exactly (twelfth night, last watch, moon already set). Faithful=2.

**5.18.29 (tad eva bhaṅgyantareṇa āha)**: Śiromaṇi: "तदेव भङ्ग्यन्तरेणाह वृत इति। ताराभिः चन्द्रमा इव नारीभिर्यो वृतः तं रावणं महाकपिर्ददर्श" = "the same thing is stated by another turn of phrase (bhaṅgyantareṇa): 'vṛtaḥ' — the one surrounded by women like the moon by stars — that Rāvaṇa, the great monkey saw." Matches note precisely — Śiromaṇi explicitly uses "bhaṅgyantareṇa" (by another turn/twist) marking this as deliberate variation, not tautology. Faithful=2.

**5.18.31 (nirdhūtas tasya tejasā)**: Tilaka: "तस्य पुरोवस्थातुमशक्नुवन्... तत्राप्यत्यल्पशरीरतया संवृतो गुप्तो ऽभवत् सर्वमायातिरस्कारकमायावतस्तस्य दृष्ट्यग्रे माययाल्पशरीरादिमत्वेन स्थातुमश्क्यत्वादेवं करणम्" = "unable to stand before him... there too, being extremely tiny in body, he remained hidden/concealed — because it was impossible to stand in the sight of that all-māyā-surpassing māyāvin [Rāvaṇa] in a state of illusion-produced tiny-body-possession, this was done thus." This confirms the note's claim precisely: Hanuman couldn't successfully deploy his own māyā/size-changing power in Rāvaṇa's overwhelming presence (Rāvaṇa's own māyā/tejas overpowers Hanuman's māyā, forcing him into a literal cramped hiding rather than a confident magical evasion). Faithful=2.

All 7 notes are faithful. Excellent sarga. Now let's check non-triviality.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\leonov_s18_targets.json
Good — Leonov's note for 5.18.1 covers the "3-6 AM timing" detail (which the candidate's `complements_leonov` field explicitly acknowledges and correctly distinguishes from), while the candidate note's own claim is about the sleep-waiting tactic, a genuinely different fact. For 5.18.12, Leonov's note covers the textual-variant dispute (maṇḍalāgra as sword vs mat), while the candidate's claim is about the ascetic-vs-gold material contrast for bṛsī specifically — a different point, and the note explicitly distinguishes this too. Both confirmed non-duplicative, non_triviality=2.

No Leonov notes for 5.18.11, 5.18.18, 5.18.22, 5.18.29, 5.18.31 — non_triviality=2 for all (let me verify Phase-1 quickly).

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\sundara_s18.json
The V.18.31 Phase-1 note is important — it directly relates to the same lemma ("nirdhūta") as the candidate note for 5.18.31. Let's compare carefully. Phase-1's note gives a general etymological/psychological reading ("this is not Hanuman's weakness but acknowledgment of Rāvaṇa's genuine might; nirdhūta = shaken from stable state; narratively important since Hanuman will return victorious"). The candidate note gives a SPECIFIC exegetical mechanism from Tilaka: Hanuman's own māyā (shape-shifting magic) was overpowered/rendered unusable in Rāvaṇa's presence — a much more concrete, textually-grounded claim about *why* he was nirdhūta (his own magic failed him specifically), which is a different angle from Phase-1's general "acknowledgment of genuine power / narrative foreshadowing" reading. These are complementary but distinct facets — the candidate's is a specific commentarial mechanism (māyā vs māyā), Phase-1's is a general lexical-thematic gloss without commentator citation. non_triviality=2 (still adds something new — the specific māyā-defeat mechanism from Tilaka, not covered by Phase-1's general etymology note).

For V.18.18 (nairṛta) — different lemma/topic entirely (cosmographic naming convention for rākṣasas), doesn't overlap with candidate's bahumāna/kāma distinction claim. non_triviality=2.

Now contrastive_value and anchoring for all 7:
- 5.18.1: single=1.
- 5.18.11: single=1.
- 5.18.12: single=1.
- 5.18.18: single (grammatical disambiguation, not a commentator-contrast)=1.
- 5.18.22: single=1.
- 5.18.29: single=1.
- 5.18.31: single=1.

Anchoring: 5.18.1 tilaka/bhusana match=true(2). 5.18.11 tilaka/bhusana match=true(2). 5.18.12 tilaka matches_verse=false(content_containment 0.091, no content_anchor flag)→anchoring=1. 5.18.18 both match=true(2). 5.18.22 both match=true(2). 5.18.29 bhusana match=true, siromani matches_verse=false(content_anchor=true) but siromani is the cited source here→anchoring=1. 5.18.31 tilaka matches_verse=false(content_anchor=true)→anchoring=1, bhusana matches=true but tilaka is the cited source for the specific māyā claim.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\judgments\sarga_18.json
All 18 sargas judged. Now let me write a script to apply all these judgments into the actual candidates JSON files in place, preserving formatting requirements (UTF-8 no BOM, ensure_ascii=False, indent=2).

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\apply_judgments.py
This is a small, task-specific script to apply already-computed judge scores into JSON files per the exact schema specified in the JUDGE_BRIEF.md I read at the start of this task — it's not a reusable helper (transcoder/parser/masker) that would exist elsewhere in the org; it's a one-off patcher for this batch's exact `_meta`/`judge` schema. Proceeding.

- 🔧 `Bash` — Apply judge objects into all 18 sarga candidate files
All applied cleanly, no warnings/mismatches. Let me verify a couple of output files for correctness (UTF-8 no BOM, structure preserved, judge object present, rejects untouched).

- 🔧 `Bash` — Verify sarga_01 output file integrity
Rejects are untouched (still just `verse_id`/`reason`, no judge object added), drafter fields preserved, meta updated correctly. Let me spot-check one more file and confirm the full note structure looks right.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_12_candidates.json
This matches the brief's exact format. `review_required` is untouched (still `true`), all drafter fields preserved, judge object correctly appended. Let me also verify the JSON is fully parseable for all 18 files and double check `review_required` was never cleared anywhere.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
All 97 notes across the 18 assigned sargas were judged, validated, and written back in place with correct schema, no BOM, `review_required` untouched, and drafter/reject fields unmodified.

## Summary

Judged all 97 notes across sargas 1–18 against their segmented bundles and the leonov_own_notes/sundara_commentary_to_add baselines, per `docs/PHASE2_METHOD.md` §3.4 and the JUDGE_BRIEF. Key finding: 8 notes rejected on the faithfulness gate — half were genuinely misattributed to commentators absent from the cited bundle (`5.1.3`, `5.9.21` reversed-attribution, `5.10.12`, `5.12.4`, `5.12.2`, `5.12.22`, `5.16.5`), one had an invented cited authority (`5.1.154`, "Kataka" not in the bhusana text), and `5.3.34` asserted a false consensus that the cited texts directly contradict. Two notes got `edit` for a partial misattribution/overreach fixable by re-pointing the citation (`5.3.44`, `5.13.6`) plus one wording overreach (`5.2.55`). Sarga 12 is a notable outlier — all 3 of its notes failed faithfulness (likely a systematic sourcing issue in that sarga's draft, worth flagging to the orchestrator).

```
sarga 01 judged: 4 notes → keep 2 / edit 0 / park 0 / reject 2 / flag_anchor 0
sarga 02 judged: 13 notes → keep 12 / edit 1 / park 0 / reject 0 / flag_anchor 0
sarga 03 judged: 10 notes → keep 8 / edit 1 / park 0 / reject 1 / flag_anchor 0
sarga 04 judged: 3 notes → keep 3 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 05 judged: 7 notes → keep 7 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 06 judged: 4 notes → keep 3 / edit 1 / park 0 / reject 0 / flag_anchor 0
sarga 07 judged: 3 notes → keep 3 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 08 judged: 3 notes → keep 3 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 09 judged: 6 notes → keep 5 / edit 0 / park 0 / reject 1 / flag_anchor 0
sarga 10 judged: 9 notes → keep 8 / edit 0 / park 0 / reject 1 / flag_anchor 0
sarga 11 judged: 4 notes → keep 4 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 12 judged: 3 notes → keep 0 / edit 0 / park 0 / reject 3 / flag_anchor 0
sarga 13 judged: 11 notes → keep 10 / edit 1 / park 0 / reject 0 / flag_anchor 0
sarga 14 judged: 5 notes → keep 5 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 15 judged: 2 notes → keep 2 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 16 judged: 1 notes → keep 0 / edit 0 / park 0 / reject 1 / flag_anchor 0
sarga 17 judged: 2 notes → keep 2 / edit 0 / park 0 / reject 0 / flag_anchor 0
sarga 18 judged: 7 notes → keep 7 / edit 0 / park 0 / reject 0 / flag_anchor 0
```

Totals: 97 notes → keep 84 / edit 3 / park 0 / reject 10 / flag_anchor 0. All 18 [`data/analysis/phase2_batch3/sarga_NN_candidates.json`](../sarga_01_candidates.json) files were rewritten in place (UTF-8, no BOM, `ensure_ascii=False, indent=2`), `_meta` updated with `judged: true` and verdict counts, `review_required` and all drafter/reject fields left untouched. No git operations were run.

