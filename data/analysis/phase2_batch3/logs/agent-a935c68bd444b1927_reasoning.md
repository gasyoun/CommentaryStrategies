_Created: 07-07-2026 · Last updated: 05-09-2026_

# Agent log agent-a935c68bd444b1927

_Model: `claude-sonnet-5`; extracted by scripts/export_agent_logs.py; raw transcript alongside (.jsonl) holds the full record incl. tool results._


I'll start by reading the drafting brief to understand the exact contract I need to follow.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\DRAFTING_BRIEF.md
Now let me check the canonical method doc and look at the input files for sarga 46.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\docs\PHASE2_METHOD.md
- 🔧 `Bash` — List segmented inputs and check size of note files
Good, the brief and method are clear. Now let me set up the scratch directory and slice the dedup baselines for sarga 46 first.

- 🔧 `Bash` — mkdir -p "C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Need to write to files instead of printing to console (console encoding issue). Let me write a script to slice both dedup sources for sarga 46 to scratch files.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\slice_sarga.py
That's a new file — the error must be transient. Let me retry.

- 🔧 `Bash` — Check scratch directory contents
The directory already exists with unrelated files from other sessions. Let me write my script under a distinct name.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_slice_sarga.py
This is a trivial one-off scratch slicing script (5 lines, dict filtering by a key), not a reusable helper — no prior-art check warranted. Proceeding.

- 🔧 `Bash` — Slice dedup baselines for sargas 46-49
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_slice_report.txt
Now let's look at the segmented input for sarga 46, and the dedup slices.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Redirecting to a file still goes through console encoding when using `print`. Let me write directly to a file with proper encoding instead.

- 🔧 `Write` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_peek.py
Trivial scratch peek script — no prior-art check needed.

- 🔧 `Bash` — Peek at sarga 46 segmented structure
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_s46_peek.txt
Good, now I understand the schema. Let me read the full sarga 46 file and the dedup slices in full.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_46_segmented.json
Now let me look at the Leonov and Phase-1 dedup slices for sarga 46.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_leonov_sarga_46.json
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_phase1_sarga_46.json
Now I have full context for sarga 46: the segmented commentary bundles, Leonov's own 19 notes, and Phase-1's 13 notes. Let me analyze verse-by-verse for contrastive/single-commentator opportunities not already covered.

Let me now go through each verse bundle systematically:

**5.46.1** — Leonov's own note already covers saṃvṛtākāraḥ (Tilaka: nigṛhītāntargatabhayaḥ; Bhūṣaṇa: gloss differs — antarmanāḥ) extensively, including the contrastive Tilaka vs Bhūṣaṇa split. Checking bundle: bhusana gloss is "saṃvṛtākāraḥ = antarmanāḥ" (withdrawn-minded), siromani explains saṃvṛtaḥ=ācchāditaḥ ākāraḥ. Leonov's note already states Tilaka says "hidden fear" and Bhūṣaṇa says "anger" — but bundle only has bhusana+siromani (no tilaka in verse 1 itself — tilaka commentary is in the *preamble* 46.pre, covering vv1-2 combined). The siromani reading adds a nuance not in Leonov's note: siromani gives TWO glosses — "concealed appearance = fear-marked appearance" AND "assumed appearance = decision to fight again" (उत्तमां मतिं पुनर्युद्धनिश्चयम्). This second gloss (uttamāṃ matim = decision to renew battle) is a distinct facet not in Leonov's note (which only discusses saṃvṛtākāraḥ and separately notes Tilaka/Tattvadipika on "resolute course of action" for uttamāṃ matim, but doesn't have Śiromaṇi's specific "decision to renew the war" reading). This is a plausible complements_leonov candidate. Let me check further verses first before drafting to keep pace.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Now I have the full lay of the land: 41 real verses (1-41, missing 16 which has no commentary bundle apparently — checking), plus 10 ambiguous-marker merged-range tokens (67, 910, 1216, 1619, 1819, 2022, 2628, 2729, 2938, 3133, 3640) that are non-independent and reject by rule (e), plus verse 67 which despite showing `ambiguous_marker: false` has empty sanskrit_iast/leonov_ru — a data artifact (verse 67 doesn't exist in a 41-verse sarga; this is clearly a mis-tagged marker). Let me verify verse 16 is genuinely absent and confirm verse 67's status.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
Confirmed: verse 16 is genuinely absent from the bundle set (no commentary aligned to it), and "5.46.67" is a merged-range-style artifact token (empty sanskrit_iast/leonov_ru, despite `ambiguous_marker: false` — the segmenter mis-flagged it, but its content is clearly non-independent bhusana fragment). I'll treat it as reject-with-reason like the other merged markers since it carries no verifiable anchor. Total verse bundles to consider = 51 (as stated in `verse_count`). Let me now draft carefully, verse by verse.

**5.46.1**: siromani gives a distinct second gloss — uttamāṃ matiṃ = "decision to renew battle" (पुनर्युद्धनिश्चय), which Leonov's note doesn't carry (Leonov only covers saṃvṛtākāraḥ contrast + Tilaka/Tattvadipika's generic "decisive course of action" for uttamāṃ matim). This is a genuine additional facet — Śiromaṇi specifies it's a decision to *resume war*, narratively significant (sets up the whole battle sequence). Draft with `complements_leonov`.

**5.46.2**: bhusana just glosses names/numbers, restates подстрочник. Reject.

**5.46.3**: Leonov/Kostina flag `nayaviśāradān` themselves (needs commentary on "искусные в политике"), and Phase-1 already has a full lexical note on `nayaviśārada`. Tilaka+bhusana here only restate the verse words (`saṃdideśa`, gloss same). Reject — duplicates Phase-1 tier-2 + Kostina's own flagged point, no new commentator content beyond what's captured.

**5.46.4**: tilaka: yāta=gaccata (trivial). bhusana: restates. siromani: glosses `sa` = kṛtapunaryuddhaniścayo rāvaṇaḥ... — again ties back to "renewed war decision" but this duplicates what I'm capturing in 46.1. Actually wait — let me check: Kostina's own note on v.4 already extensively discusses `sa kapiḥ śāsyatām` via Śiromaṇi's gloss (nigṛhyatām)! That's the same commentator+point already in Leonov's note. Reject — duplicates Leonov/Kostina's own note.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
I already have verses 5-12 from the earlier full read. Let me re-examine them carefully now, verse by verse, plus continue through the rest.

**5.46.5** (deśakāla): Phase-1 already has a full lexical note on `deśakāla` covering exactly this compound's artha-śāstra register. Tilaka/Bhūṣaṇa/Śiromaṇi here diverge on whether "yatta/yattaiḥ" (samādheyaṃ) is to be *done* or *avoided* — actually Bhūṣaṇa glosses samādheyam = parihartavyam ("to be avoided") while the verse's plain sense (and подстрочник) says "должно соблюдать" — that's an interesting reading (Bhūṣaṇa reverses the polarity: samādheyaṃ = "must be given up/avoided" not "undertaken"). Let me check: Tilaka says "yattaiḥ sāvasānaiḥ" and doesn't gloss samādheya's polarity explicitly ("samādheyaṃ kāryam" = to be done — same as literal). Śiromaṇi: "yatnaiḥ...bhāvyaṃ syāt...karma samādheyaṃ ca" — also "to be done." So Bhūṣaṇa alone reads समाधेयं = परिहर्तव्यम् (something to be *renounced*/avoided), diverging from Tilaka (kāryam = to be done) and from Leonov's own translation ("действия... должны быть предприняты"). This is a genuine contrastive-worthy divergence not covered by the Phase-1 lexical note (which is about deśakāla's semantics, not about the samādheya reversal). This is draftable — contrastive.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && e
Let me verify my reading of Bhūṣaṇa's gloss on samādheyam more carefully by re-checking the exact text.

Looking back at verse 5: `bhusana: "...समाधेयं परिहर्तव्यम्..."` — yes, samādheyam glossed as parihartavyam ("to be renounced/set aside"), which is the OPPOSITE polarity from the verse's own plain sense ("karma cāpi samādheyam" = "action too must be undertaken/attended to"). Tilaka's gloss: "samādheyaṃ kāryam" = "to be done" (matches plain sense). This is a genuine Tilaka/Bhūṣaṇa split on the polarity of a key verb, worth a contrastive note.

Now let's continue through verses 6-15.

**5.46.6**: Tilaka explains logical connection (hetu) across verses, cross-references v.8's "bhaved" — mostly structural bridging, restates подстрочник's content. Bhūṣaṇa/Śiromaṇi restate. Kostina's own note flags a textual variant (v.7 absent in Goldman). No independent gloss beyond подстрочник here from the three ṭīkās for this specific verse. Reject.

**5.46.7**: Śiromaṇi is a long structural passage bridging several verses (7-15), explaining Rāvaṇa's reasoning chain but not adding a specific gloss to verse 7's own words. It's essentially connective tissue, restates the подстрочник's logic. Reject — pure structural/logical bridging, not exegesis of a specific term (rule c-adjacent, no independent gloss for reader).

**5.46.8**: Phase-1 already has `tapobalā` lexical note fully covering this. Leonov's own note ALSO covers `asmadartham` (Tattvadipika) and `indreṇa vā` (Bhūṣaṇa: "Indra or someone else"). Bundle only shows bhusana with a gloss restating verse text (sanāgayakṣagandharvā devāsuramaharṣayaḥ — just repeats compound, no new content). Reject — duplicates tier-1+Phase-1.

**5.46.9**: Bhūṣaṇa glosses vyalīkam = apriyam (trivial synonym, subsumed by подстрочник "неприятное"). Tilaka restates. No new content. Reject.

**5.46.10**: Tilaka: "parigṛhyatām = baddhvā ānīyatām" (seize = having bound, bring) — trivial gloss matching подстрочник. Reject.

**5.46.11**: Leonov's own note ALREADY covers this exact verse — the dhīraparākramaḥ epithet — wait, checking: Leonov's own note for 5.46.11 is just "[Kostina] «11» Сверка" (a collation flag, not a substantive note). Phase-1 already has a full crosstext note on `dhīra` for this verse citing BhG 2.15. Bhūṣaṇa here (in bundle) is actually a longer passage that seems to belong to verse 12 (offset issue — the text starting "नावमान्यो भवद्भिश्च हरिर्धीरपराक्रमः" runs through what should be vv 9-16 as one big chunk with embedded verse markers). Tilaka: "sa-vāji-ratha ityādi punarvacanaṃ sthairyārtham" — a real gloss: explains WHY the verse repeats phrases from v.4 (savājirathamātaṅgāḥ sa kapiḥ śāsyatām) — Tilaka says this repetition is "for the sake of firmness/emphasis" (sthairyārtham). This is a genuine rhetorical-narrative observation not in подстрочник nor Phase-1's dhīra note (which is about the dhīra epithet, not about the repetition device). Draftable — single-commentator gloss on a narrative/rhetorical device (repetition for emphasis).

Let me continue through the rest before finalizing drafts.

**5.46.12**: Bhūṣaṇa here is actually the continuation of the big block (spans into future verses – "tathāpi tu nayajñena jayamākāṅkṣatā raṇe..."), matches подстрочник content once properly attributed to verse ~16 by content but assigned here per marker. It restates verse content, no independent gloss for v.12's own words (dṛṣṭā hi harayaḥ pūrve...). Reject — this is a content/marker misalignment; the chunk doesn't gloss v.12 itself.

**5.46.13**: Bhūṣaṇa glosses gatiḥ=vegaḥ ("pace"="speed") and rūpaparikalpanam = yatheṣṭarūpagrahaṇam ("assuming any form at will") — this second gloss adds something: it specifies that rūpaparikalpanam refers to shape-shifting ability (not explicit in подстрочник's "способности менять облик" — actually подстрочник already says "способности менять облик", so this gloss just confirms/restates. The first gloss gatiḥ=vegaḥ is trivial. Reject — both glosses restate подстрочник.

**5.46.14**: Tilaka glosses rūpaparikalpanam = yathepsitarūpaparigrahaḥ (same idea, restates) and sattvam=cittam ("sattva"="mind/consciousness") — this is interesting: sattva could be read as "essence/being" (great being) OR specifically "citta" (mind/consciousness) per Tilaka. The подстрочник translates "великое существо" (great being) for mahat sattvam. Tilaka's गloss sattvam=cittam is a plausible alternate/technical reading worth noting — but does it change the sense enough? "mahat sattvam idaṃ jñeyam" = "this should be known as a great being" vs if sattva=citta, "this should be known as a great mind/consciousness" — a real interpretive divergence in what exactly Hanuman's revealed nature is (physical/ontological "being" vs "mind/citta", touching Sāṃkhya terminology). This is a genuine single-commentator gloss with translation-choice implications (Leonov follows the "being" reading against Tilaka's "citta" reading). Draftable.

Let me verify this reading is solid — `sattvam` glossed as `cittam` by Tilaka is a real Sāṃkhya-adjacent technical move worth flagging.

- 🔧 `Bash` — echo "checking verse 14 commentary text again"
Verse 14 commentary (tilaka): `"रूपपरिकल्पनं यथेप्सितरूपपरिग्रहः\nसत्त्वं चित्तम्"` — confirmed, two glosses, second is `sattvaṃ cittam`. This is solid: draftable as single-commentator (Tilaka), kazansky **Б** (textological/meaning), since it resolves what "sattva" means in this specific compound against the plain "being" reading.

Continuing:

**5.46.15**: Bhūṣaṇa restates verse (kāmaṃ lokāstrayaḥ...). Leonov's own note already covers this exact verse (kāmaṃ = "хотя"). Tilaka glosses kāmam = "yadyapi" ("although" — concessive) and prayatnam = "iti ārṣam klībatvam" (this is a grammatical note about a masculine/neuter irregularity — Ārṣa usage). Since Leonov's own note ALREADY explains kāmam = "хотя" (matching Tilaka exactly), Tilaka's kāmam gloss duplicates tier-1. The grammatical note about ārṣa klībatvam is pure Sanskrit grammar invisible to a Russian reader (rule c). Reject.

**5.46.17**: Bhūṣaṇa restates verse content (te svāmivacanaṃ...) and extends into next verses; no independent gloss of this verse's specific words beyond подстрочник. Phase-1 already covers `yuddhasiddhi` for this verse fully. Reject.

**5.46.18**: Bhūṣaṇa restates. Kostina's own note flags "Агни" (fire) reference already. Reject — duplicates tier-1 flag + restates подстрочник.

**5.46.19**: Bhūṣaṇa glosses svatejoraśmimālinam = svatejasā sūryam, and notes a rhetorical distinction: raśmimantam iva = upamā (simile) vs (next verse's) svatejoraśmimālinam = rūpakam (metaphor) — "atra upamā, atra rūpakam iti bhidā" (this is a simile, that is a metaphor — that's the distinction). This is a genuine rhetorical/figurative-language observation (upamā vs rūpaka distinction), a real literary-critical point about how the verse constructs its comparison, which the подстрочник flattens (both translated as "подобно"/"облаченную в"). Kazansky type — this is about figurative reading, Śiromaṇi's domain per citation hierarchy but here it's Bhūṣaṇa making the alaṃkāra distinction. Draftable — single-commentator, kazansky Б (textological — rhetorical device distinction affecting how to read the image), genuine facet not in Leonov (v.20's note only covers the literal meaning, not the upamā/rūpaka rhetorical shift).

Wait, let me check — this Bhūṣaṇa comment appears attached to v.19's bundle but the actual content ("स्वतेजोरश्मिमालिनं स्वतेजसा सूर्यम् । रश्मिमन्तमिवेत्यत्र उपमा, अत्र रूपकमिति भिदा") is glossing the *transition* between "raśmimantam ivodyantam" (v.20, simile) and "svatejoraśmimālinam" (also v.20) — actually both phrases are in verse 20 itself! Let me re-check.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_v19_20.txt
Confirmed: the alaṃkāra observation (upamā vs rūpaka) is Bhūṣaṇa's gloss quoting v.20's own phrase "raśmimantam ivodyantaṃ" (v.20) vs "svatejoraśmimālinam" (also v.20), but the chunk is attached to v.19's bundle (marker offset — the pratīka check shows it matches v.19's own words though, since it quotes "tatas taṃ dadṛśur vīrā dīpyamānaṃ mahākapim" first which IS v.19). Actually the full bhusana chunk covers BOTH the v.19 line and the v.20 line (it's one continuous quote spanning the verse boundary print convention). Given `pratika_check` verified true for v.19's own pratīka, and the alaṃkāra note specifically concerns the second half of the quoted material (which is v.20's text appearing within the v.19-attached chunk), I should note in `why_proposed` that this attaches to the v.19/v.20 boundary and is anchored per the segmenter to v.19. Since this is a genuine and verified-anchored point, I'll attach it to 5.46.19 (verified anchor) and note it comments on the imagery carried into v.20.

Continuing through remaining verses:

**5.46.20**: Śiromaṇi bridges bookkeeping (śloka-dvayam ekānvayi for 19-20, structural) then jumps to explaining v.22's pañcaśarāḥ (pītamukhāḥ = svarṇapuṅkhāḥ, golden-shafted) — this duplicates Phase-1's already-drafted content? No, Phase-1 doesn't have this verse. But wait — this Śiromaṇi content is actually about verse 22 (pītamukhāḥ glossed as golden), attached here due to marker misalignment. Leonov's own note on v.22 ALREADY covers exactly this (Tilaka says gold-covered, Tattvadipika agrees but adds blood-color alt reading). Śiromaṇi's specific "svarṇapuṅkhāḥ" synonym doesn't add beyond what's in Leonov's v.22 note (which already says "покрыты золотом" per Tilaka). Bhūṣaṇa's chunk here restates verse 20's compounds mechanically (mahotsāhaṃ, mahāsattvaṃ...) — no glosses, just repetition variant of the verse itself. Reject both — duplicates tier-1 (Śiromaṇi content is content-anchored to v.22 already covered) and restates подстрочник (Bhūṣaṇa).

**5.46.21**: Tilaka: "dikṣu sarvāsvavasthitāḥ" gloss = "drāk tat-samīpam āgantuṃ cakitā iti bhāvaḥ" (they stood all around — the sense is that they were too frightened to approach him quickly). This is a genuine interpretive addition: Tilaka reads the rakṣasas' positioning ("stood on all sides") as revealing their *fear/hesitation* to approach Hanuman directly, not just tactical positioning. The подстрочник just says "they all stood around" without this psychological nuance. Draftable — single-commentator (Б, textological/psychological subtext). Śiromaṇi's content here is a long structural bridge (bookkeeping across vv 12-17), no new gloss for v.21 itself. 

**5.46.22**: Leonov's own note is extremely thorough here (covers tīkṣṇāḥ, pītamukhāḥ, utpalapatrābhāḥ with Tilaka/Bhūṣaṇa/Tattvadipika all cited). Bundle's bhusana ("tasya pañcāyasāḥ...") restates verse. Tilaka ("tīkṣṇā marmacchidaḥ, pītamukhāḥ phalabhāge svarṇarūṣitāḥ. utpalapatrābhā eva, na tu tatpīḍārhā ityarthaḥ") — checking against Leonov's note: Leonov's note says "по мнению Тилаки, эти стрелы не могли причинить вреда Хануману" for utpalapatrābhāḥ — this exactly matches "utpalapatrābhā eva, na tu tatpīḍārhā ityarthaḥ" (they only LOOK like lotus petals, but aren't actually capable of hurting him). Also Tilaka's "tīkṣṇāḥ = marmacchidaḥ" (sharp = organ/vital-point-cutting) isn't explicitly in Leonov's note (Leonov only covers Bhūṣaṇa's tīkṣṇāḥ=krūrāḥ gloss). This is a minor additional nuance but likely too thin — marmacchidaḥ vs krūrāḥ are near-synonymous ("cutting vital points" vs "cruel/sharp"), not really a divergent facet. Reject — duplicates tier-1 (Leonov's note already captures the substantive Tilaka point about utpalapatrābhāḥ being deceptive).

**5.46.23**: Śiromaṇi structural bridge, restates. Tilaka: "svayaṃ nadan. tena nādena diśo nādayann ityarthaḥ. utpapāta toraṇād iti śeṣaḥ" — adds an ellipsis-supplement: "utpapāta" implies "from the archway" (toraṇāt) as unstated but implied. This is a genuine supplied-ellipsis note (rule: draftable per brief's "supplied ellipsis" criterion) — the подстрочник just says "взлетела" without specifying *from where*. Bhūṣaṇa here (sa kapir vārayām āsa...) belongs to v.25, restates, already used. Draftable — single-commentator, Tilaka, Б (supplied ellipsis).

**5.46.24**: Tilaka: "abhipede = prāptaḥ" (trivial synonym). Śiromaṇi: structural bridge. Reject.

**5.46.25**: Leonov's own note already covers this exact simile (vārayām āsa... payodānte payodam iva mārutaḥ). Bhūṣaṇa's chunk here is actually v.29's content (taṃ virūpākṣayūpākṣau dṛṣṭvā...) — marker misalignment, restates. Reject — duplicates tier-1 / restates.

**5.46.26**: Śiromaṇi: "ardyamānaḥ iti. durdhareṇa ardyamānaḥ anilātmajaḥ ninadaṃ cakāra vyavardhata ca" — pure restatement/paraphrase of verse. Reject.

**5.46.27**: Leonov's own note covers vidyudrāśir girāv iva already. Phase-1 has a full lexical note on vidyudrāśi. Bhūṣaṇa here restates + extra content (belongs to v.30, tāv ubhau... mudgarābhyāṃ — anticipating next verses). Śiromaṇi restates. Reject.

**5.46.28**: Bhūṣaṇa/Śiromaṇi restate verse mechanically (mathitāṣṭāśvam, bhagnākṣakūbaram — Śiromaṇi glosses mathitāḥ=hiṃsitāḥ, trivial synonym). Reject.

**5.46.29**: Leonov's own note covers jātaroṣau durdharṣāv utpetatur ariṃdamau. Bhūṣaṇa's chunk here belongs to v.32 (sa sālavṛkṣam āsādya...). Śiromaṇi restates. Reject.

**5.46.30**: Tilaka: "tābhyāṃ kartṛbhyāṃ mudgarābhyāṃ karaṇābhyām abhihataḥ" — clarifies grammatical roles (the two rakshasas as agents, the maces as instruments) — this is grammar-adjacent, arguably invisible/trivial to a Russian reader (rule c). Śiromaṇi restates (structural). Reject.

**5.46.31**: Leonov's own note ALREADY covers this exact point (Tilaka: vajra-vakṣas, "diamond chest" making the blows harmless). Bhūṣaṇa/Śiromaṇi restate. Reject — duplicates tier-1.

**5.46.32**: Śiromaṇi restates (sa bhūmiṃ prāpto hanūmān śālavṛkṣam āsādya...). Reject.

**5.46.33**: Bhūṣaṇa restates. Śiromaṇi structural bridge + notes "ekataḥ...ekataḥ" division of labor (Praghasa attacks from one side, Bhāsakarṇa from the other) — this is present in подстрочник already ("вместе они напали"/"с одной стороны"). Reject — restates.

**5.46.34, 35**: Bhūṣaṇa restates mechanically. Reject both.

**5.46.36**: Bhūṣaṇa restates. Śiromaṇi restates (glosses compound parts mechanically, matches подстрочник exactly). Reject.

**5.46.37**: Bhūṣaṇa restates. Śiromaṇi structural + notes "ardham pṛthak" (half-verse treated separately) and gives a small addition later (tataḥ...on to v.38 setup) — restates. Reject.

**5.46.38**: Bhūṣaṇa restates. Reject.

**5.46.39**: Bhūṣaṇa restates. Śiromaṇi: "vināśanaprakāram āha" (explains the manner/method of destruction) — trivial. Reject (also flagged content_containment 0.071, weak anchor).

**5.46.40**: Bhūṣaṇa restates. Śiromaṇi: "hataiḥ iti. hatair nāgādibhir bhagnākṣair mahārathaiś ca ruddhamārgā bhūmir abhavad iti śeṣaḥ" — supplies the elided verb (abhavat, "became") — this is a genuine supplied-ellipsis note per the brief's criteria. But is it substantive enough for a Russian reader? The подстрочник already conveys "were blocked" implicitly. This ellipsis-supply is minor grammatical bookkeeping, not exegetically meaningful (doesn't change interpretation). Reject — restates/pure grammar, no interpretive gain.

**5.46.41**: Leonov's own note covers kṛtakṣaṇaḥ kāla iva prajākṣaye extensively (Kostina notes Gita Press differs: "готовящаяся истреблять" vs "после гибели"). Phase-1 has a full lexical note on kṛtakṣaṇa. Tilaka: "kṛtakṣaṇaḥ = labdhāvasaraḥ" (obtained-the-opportunity) — this actually supports the "awaiting/ready" reading (matches Leonov's main translation, NOT the Gita-Press alternate). Bhūṣaṇa here includes the sarga colophon (iti ārṣe...) plus a repeat gloss "kṛtakṣaṇaḥ = dattāvasaraḥ, abhūd iti śeṣaḥ" — Bhūṣaṇa's supplied ellipsis "abhūt" (was/became) is minor grammar. Given Leonov/Kostina's note ALREADY flags the translation-choice ambiguity (kāla iva prajākṣaye = "Time awaiting" vs "Death having prepared to destroy") citing Gita-Press's divergent reading, and Tilaka+Bhūṣaṇa BOTH confirm the "labdhāvasaraḥ/dattāvasaraḥ" (=opportunity granted/obtained, i.e., "awaiting") reading — this actually RESOLVES which side of Kostina's flagged ambiguity the ṭīkā tradition supports! That's a genuine complements_leonov: the commentators unanimously back Leonov's own main translation against the Gita-Press alternative Kostina flagged. Draftable — contrastive is not needed (Tilaka/Bhūṣaṇa agree), single-commentator-consensus resolving Kostina's flagged doubt. I'll cite Tilaka (primary per hierarchy) with complements_leonov noting it confirms against Gita-Press.

Now let me also reconsider verse 1's siromani gloss and verse 4 more carefully, then also check verse 67 (empty anchor) which I'll reject as merged-range-equivalent.

Let me double check verse 1's exact wording once more and finalize the draft set.

- 🔧 `Bash` — echo "reviewing final list before writing output"
Let me finalize my decisions. Draftable set for sarga 46:

1. **5.46.1** — Śiromaṇi's second gloss: uttamāṃ matim = decision to resume war (complements Leonov)
2. **5.46.5** — Tilaka vs Bhūṣaṇa contrastive on samādheyam polarity
3. **5.46.11** — Tilaka: repetition of v.4's phrasing is for emphasis (sthairyārtham)
4. **5.46.14** — Tilaka: sattvam = cittam (alternate technical reading)
5. **5.46.19** — Bhūṣaṇa: upamā vs rūpaka rhetorical distinction
6. **5.46.21** — Tilaka: positioning reveals fear/hesitation to approach
7. **5.46.23** — Tilaka: supplied ellipsis "from the archway" (utpapāta toraṇāt)
8. **5.46.41** — Tilaka/Bhūṣaṇa confirm "awaiting" reading against Kostina's flagged Gita-Press alternative

That's 8 drafts out of 51 considered (≈15.7%) — a bit high vs the 5-10% target. Let me be more conservative and re-scrutinize the weaker ones (14, 21, 23) against the reject discipline more strictly.

Re-examining #4 (v.14, sattvam=cittam): this is a real but thin technical gloss — is it "invisible/pure grammar" or genuinely meaningful? Sattva vs citta touches a real interpretive question (is Hanuman revealed as a "great being" or as "a great mind/intelligence"?), which does affect how a reader understands what's being revealed. I'll keep it but make sure `why_proposed` earns its place clearly.

Re-examining #6 (v.21, Tilaka "cakitāḥ"/hesitation reading): this is a real interpretive add (fear-subtext vs neutral positioning) - keep.

Re-examining #7 (v.23, supplied ellipsis "toraṇāt"): minor but per brief, supplied ellipsis is an explicit allowed category. It's thin but genuine — I'll keep but note it's a minor supply. Given accept rate should trend low, let me cut the weakest one. Comparing all 8, the thinnest is arguably #7 (just supplies "from the arch," barely changes reading) vs #4 (real semantic divergence) vs #6 (real psychological subtext). Let me cut #7 to reject, bringing total to 7/51 ≈ 13.7% — still a bit high but the brief says "~5-10%... do not pad" as a guideline not a hard cap. Given batch-2 achieved 10.9%, I'll keep discipline tight and cut one more borderline one.

Reconsidering #1 (v.1 Śiromaṇi "renewed war" gloss): Leonov's note already discusses "uttamāṃ matim" via Tilaka/Tattvadipika as "decisive course of action" — Śiromaṇi's specific narrative content (punaryuddhaniścaya, decision to resume war) is a genuine narrative-function fact (sets up why Rāvaṇa musters generals next) — this matches the brief's explicitly valued "narrative-function observations." Keep.

I'll cut #7 (v.23 ellipsis) as the weakest, keeping 7 drafts / 51 = 13.7%. Let me reconsider once more — actually let me check the accept-rate guidance again: it's a target not hard rule, and batch-2 was 10.9%. Given sarga 46 is unusually battle-heavy with genuine contrastive divergences, I'll keep it evidence-driven rather than force-fit to a percentage. I'll finalize with 7 drafts, rejecting v.23.

Now let me write the output file for sarga 46.

- 🔧 `Write` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_46_candidates.json
Let me verify the counts reconcile and the JSON is valid (no BOM, correct encoding).

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_s46_check.txt
Sarga 46 reconciles perfectly (7 drafted + 44 rejected = 51 considered), no BOM (`7b` = `{`). Now moving to sarga 47.

- 🔧 `Bash` — Peek sarga 47 meta
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_47_segmented.json
Let me continue reading the rest of sarga 47.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_47_segmented.json
Now I have the full sarga 47 bundle (38 real verses + 4 merged-range markers = 42 total, matching `verse_count: 42`). Let me get the dedup slices.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_leonov_sarga_47.json
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_phase1_sarga_47.json
Now I have the complete picture for sarga 47. Let me go through verse by verse.

**5.47.1**: Tilaka/Bhūṣaṇa/Śiromaṇi all essentially restate the verse mechanically (pramāpitān=māritān, samīkṣya=vijñāya — trivial synonyms). Phase-1 already has a note on akṣa itself. Leonov's own note covers sānucarān and akṣatam already. Reject.

**5.47.2**: Bhūṣaṇa restates. Śiromaṇi glosses dṛṣṭyarpaṇena = dṛṣṭipracālanena eva ("merely by the movement/turn of his glance") and specifies sadasi = yāgaśālāyām ("in the sacrificial hall") — this actually answers Kostina's own flagged question! Kostina asks "что за собрание" (what assembly?) for "sadasi" — and Śiromaṇi explicitly glosses sadasi as yāgaśālā (sacrificial ritual-hall), resolving her open question with a real place-reference. This is draftable, complements_leonov (directly answers Kostina's flagged gap), kazansky В (realia — a specific ritual venue).

**5.47.3**: Tilaka/Bhūṣaṇa restate word order (mahān sa ityanvayaḥ — syntax note) and repeat compound. No new content; Phase-1's note doesn't cover this verse but Leonov's own note (Claude.AI flag) already notes "vṛṣabha = bull, epithet of excellence." Bundle doesn't add anything beyond that. Reject — restates подстрочник, no new commentator content.

**5.47.4**: Tilaka/Bhūṣaṇa/Śiromaṇi all restate mechanically (tapaḥsaṃgraha compound already fully covered by Phase-1 lexical note). Reject.

**5.47.5**: Bhūṣaṇa gives an unusually rich note: on aṣṭāsinibaddhabandhuram he offers THREE alternate parsings/meanings for "bandhura" — (1) beautiful chariot-boards fastened with eight swords, (2) some say bandhura = phalaka-saṅghāta (assemblage of boards), (3) others say = ghaṇṭā (bells) — a genuine textual-interpretive crux with multiple traditional glosses recorded by name ("anye... āhuḥ"). This kind of explicit multi-reading crux (Bhūṣaṇa citing "some say X, others say Y") is a strong candidate — draftable, single-commentator (though internally contrastive), kazansky Б (textological — ambiguous compound with recorded alternate readings). Also Tilaka reads asaṅgacārin differently: "parvatādiṣv api" (i.e., it moves unobstructed even over mountains) — a specific gloss not in подстrочник's generic "не знающей препятствий." I'll focus the note on the bandhura crux since it's the richer/more citable point (multiple named alternatives = genuine textual crux, more valuable than the parvata gloss). Given IAST budget, I'll keep it single-topic.

**5.47.6**: Bhūṣaṇa gives a genuinely rich variant-reading discussion: notes an alternate reading "pratipūrṇam astinā" (variant pāṭha) glossed differently, AND explains a rhetorical resolution of apparent redundancy between "śaśisūryavarcasā" here and "raviprabham" (used earlier, v.5's variant) — "ataḥ na raviprabham ity anena punaruktiḥ. tacchabdadvayaṃ ca pūrvānusmaraṇārtham" (so this doesn't repeat "ravi-prabham"; the repetition of "tat" [in the verse] serves to recall the earlier reference). This is a genuine textual-variant + poetic-technique note addressing a real redundancy concern in the received text. This is solid — draftable, single-commentator (Bhūṣaṇa), kazansky Б (textual variant / avoiding redundancy).

Given the density of good material, let me be selective — I need to keep the accept rate reasonable. Let me continue scanning the rest first before finalizing which of 5/6 to keep.

**5.47.7**: Tilaka: bāṇāsanam eva śakrakārmukam yasya (his bow, only mentioned generically, glossed via a formula meaning "bow like Indra's" — actually wait, checking: this tilaka fragment "bāṇāsanam eva śakrakārmukaṃ yasya saḥ" seems to be a mis-anchored gloss belonging to v.18's bāṇāsanaśakrakārmukaḥ, not v.7's own content) — restates подстрочник (toraṇasthitam = toraṇāśrayam, āsīnam = upaviṣṭam, trivial synonyms). Reject.

**5.47.8**: Leonov's own note ALREADY covers harīkṣaṇaḥ (Tilaka: siṃhavat krūra dṛṣṭiḥ) and yugāntakālāgnim iva prajākṣaye. Phase-1 also has a full lexical note on yugāntakālāgni. Tilaka here ALSO adds: "bālo 'yaṃ māṃ yoddhum icchatīti vismayaḥ rāvaṇaputratvāc ca tatra jātādaratvam" — explains WHY Akṣa feels surprise/respect: because Hanuman (an adult in his eyes) wants to fight "this mere boy" (Akṣa), and because Akṣa is Rāvaṇa's son, there's an added element of due respect. This is a psychological/narrative motivation not in Leonov's note (which only covers the two glosses already flagged) nor in Phase-1. This is a genuine additional facet — complements_leonov. Draftable.

**5.47.9**: Leonov's own note covers yugakṣaye sūrya variant (himakṣaye) and abhivardhata=tejasā (Tilaka, already flagged). Bundle Tilaka repeats exactly "abhivardhata tejasā 'bhyavardhata ity arthaḥ" — same content, duplicate. Reject.

**5.47.10**: Bhūṣaṇa/Śiromaṇi restate. No new content. Reject.

**5.47.11**: Tilaka glosses niṣkam = uro-bhūṣaṇam ("a chest ornament" — but wait, niṣka doesn't appear in v.11's text; checking — actually this looks misplaced, belongs to v.12's hemaniṣkāṅgada). Also "āśupārākramaḥ" and "saṃgrama... saṃbhramaprada = bhayaprada" — these are all trivial synonym glosses restating подстрочник or misaligned to v.12. Reject.

**5.47.12**: Bhūṣaṇa/Śiromaṇi restate (niṣkam uro-bhūṣaṇam = "a breast-ornament" — a real gloss of a rare word niṣka, but подстrochnik already translates it as "ожерелье" so this doesn't add new information for a Russian reader, just confirms the translation choice). Reject — restates.

**5.47.13**: Leonov's own note covers "rarāsa bhūmiḥ" already (Tilaka: refers to земные существа). Bhūṣaṇa adds something distinct: "na tatāpa bhānumān. sūryodayaḥ pūrvaṃ sūcitaḥ saḥ na tatāpety ucyate" — this explains an implicit narrative-continuity point: the sun (mentioned as having risen earlier in the text) is now said to NOT scorch — Bhūṣaṇa flags this as making sense only because sunrise was already established earlier in the story, i.e., it's not a new sunrise. This is a subtle continuity/craft observation. It's fairly thin though — is it independent enough? I think this borders on grammar-invisible technicality. Let me weigh against reject discipline: it does explain something a Russian reader wouldn't get from "не жгло солнце" alone — WHY mention sun not scorching at all, i.e. this confirms it was already day (not a fresh dawn point) — actually this is fairly niche and doesn't change reading meaningfully. I'll reject — duplicates tier-1's coverage of the same verse and the additional point is too thin/technical.

**5.47.14**: Leonov's own note + Phase-1 lexical note both cover samādhisaṃyogavimokṣatattvavid fully. Bundle just restates. Reject.

**5.47.15**: Tilaka offers a real variant-reading + gloss: notes alternate pāṭha "vivṛttalocanaḥ" and glosses it as "avasarocitacakṣuḥ" (eyes fitting to the occasion) instead of literally "rolling/wide eyes" — also glosses "navoditādityasaṃnibhaḥ" = "raktavarṇaḥ" (blood-red colored, i.e., not just "like the rising sun" generically but specifically red-hued). Bhūṣaṇa separately explains the double simile structure: "raktasiktatve dṛṣṭāntaḥ navodita iti. śarācitatve dṛṣṭāntaḥ āditya ivāṃśumālika iti" — i.e., he explicitly identifies which simile matches which vehicle (bloodied → "newly-risen sun" red color; arrow-covered → "sun with a garland of rays"). This is a genuine rhetorical-structure clarification (disentangling a double simile), which the подстрочник doesn't make explicit (it just presents both images sequentially without clarifying which maps to what). Draftable — single-commentator (Bhūṣaṇa), kazansky Б.

Given the accumulating density again, let me keep tracking candidates and evaluate at the end. Continuing:

**5.47.16**: Tilaka trivial (āpūryata=vyavardhata). Leonov's own note flags "лучшего из царей" (rājavarātmajam) as Kostina's open question (uncertain epithet for Rāvaṇa). Bundle doesn't resolve this — no ṭīkā comments on rājavara itself specifically. Reject.

**5.47.17**: Tilaka: "mandarāgrasthatvena madhyandinasthatvaṃ lakṣyate" (being on the summit of Mandara indicates being at noon/zenith) — this reads the simile as encoding TIME OF DAY (noon), a genuine interpretive addition beyond the plain image of "like the sun on Mandara's peak." Bhūṣaṇa confirms/extends: "mandarāgrasthaḥ mandaro nāma bhūmadhyaparvataḥ. tadagre madhyāhne vartata ity aughryoktiḥ" (Mandara is the central mountain of the earth; being at its peak at midday is a hyperbolic/intensifying expression — aughryokti). Both commentators converge on reading this as a temporal marker (noon) AND a rhetorical device (hyperbole) — this is a genuine contrastive-adjacent (actually convergent) reading not visible in Leonov's note (no note exists for this verse) nor подстрочник (which just says "стоящему на вершине Мандары"). Draftable — single-commentator-consensus (both agree), citing Tilaka primary + Bhūṣaṇa confirming, kazansky Б (figurative reading — but actually this is more realia/temporal-symbolic — let's call it Б since it's about textual/figurative meaning, not customs).

I'm accumulating quite a few strong candidates for sarga 47. Let me push through the remainder and then make final cuts to keep density reasonable.

**5.47.18**: Śiromaṇi restates. Tilaka: "śarān vimokṣayan vyarthīkurvan" — this exactly duplicates Leonov's own note (which already cites Tilaka's vimokṣayan=vyarthīkurvan AND Bhūṣaṇa's śarīre asaṃyojayan) for verse 23 — but wait, this Tilaka fragment is attached to v.18's bundle while Leonov's note is for v.23. Let me check — the pratika_check shows tilaka's pratika "śarān vimokṣayan vyarthīkurvan" matches_verse: true for v.18?? That seems like a marker/content mismatch since "vimokṣayan" is v.23's verb. This is a segmenter misalignment — the content actually belongs to v.23, already covered by Leonov's note. Reject — duplicates tier-1 (content belongs to v.23, already noted).

**5.47.19**: Tilaka: "tejaādi sāyakāntāḥ pravṛddhā yasya" — trivial paraphrase of compound. Reject.

**5.47.20**: Leonov's own note ALREADY covers gajo mahākūpam ivāvṛtaṃ tṛṇaiḥ (medieval commentators note it's an elephant-trap). Bundle: Tilaka: "tṛṇair āvṛtaṃ mahākūpaṃ gajapātanārthakṛtagartam" — this IS the exact source of Leonov's note (elephant-trap pit) — duplicate. Reject.

**5.47.21**: Tilaka: "samutsahena samutsāhena hrasva ārṣaḥ" (grammatical note on a short-vowel Ārṣa irregularity) — pure grammar, invisible to Russian reader. Reject.

**5.47.22-25**: mostly restating verse content via trivial synonyms (samabhidravat=abhyadravat, etc.) or structural bridging. Let me check v.23 specifically since Leonov's own note already covers vimokṣayan there (Tilaka+Bhūṣaṇa both cited) — bundle repeats same content. Reject 22-25 as restating/duplicating.

**5.47.26**: Tilaka offers a genuine variant-reading note: "'pramāpaṇe mārutir atra jāyate' iti pāṭhe 'ayaṃ janaḥ' iti-vat svasyaiva hanumatā mārutir iti nirdeśaḥ" — this explains an alternate manuscript reading where the text says "mārutiḥ" (Hanuman's own name) instead of "me matiḥ" (my resolve), and explains it as Hanuman referring to himself in third person (like "ayaṃ janaḥ" = "this person" for "I"). This is a genuine, citable textual variant with real interpretive consequence (whose thought is being reported, and a self-referential naming convention) — solidly draftable. Kazansky Б (textual variant).

**5.47.27**: restates via trivial synonyms. Reject.

**5.47.28**: restates. Reject.

**5.47.29**: Leonov's own note ALREADY covers pramāpaṇaṃ hy asya mamādya rocate (citing Goldman's "no choice but to kill him"). Śiromaṇi here: "yato 'sya raṇe parākramo vivardhate ata upekṣito 'yaṃ māṃ nābhibhavet abhibhaved evety arthaḥ" — this clarifies the double-negative logic (nābhibhaved... = "would definitely overcome," reading the double negation as emphatic affirmation) — could be seen as grammar-adjacent but it does resolve a genuine logical/translation ambiguity (na khalv ayaṃ nābhibhaved = literally "would not not-overcome" = "would certainly overcome"). This affects how the verse's logic reads. Thin though, and duplicates territory already covered by Leonov's note on the same verse's broader point (Hanuman resolving to kill). I'll reject as too thin/duplicative — the core interpretive point (Hanuman feels he must kill Akṣa) is already fully covered by tier-1.

**5.47.30-38**: Let me scan for anything new. V.30: restates. V.31: Tilaka repeats v.29's content (misaligned), restates. V.32: Tilaka trivial (nīḍam=rathyadhiṣṭhānasthānam, minor technical term gloss for chariot-seat — thin). Leonov's own note covers piṅgādhipamantrinirjitaḥ already. Reject all as restating/duplicating.

**5.47.33**: Leonov's own note (with Kostina's flagged ambiguity about who exactly "left the body" — Akṣa or a sage) ALREADY covers marutām ivālayam via Śiromaṇi (devānām ālayam). Bundle: Tilaka "marutām ālayaṃ svargam utpatan ṛṣir iva" — restates the same simile, no new content beyond tier-1. Reject.

**5.47.34-38**: mostly restating verse content mechanically. V.35: Bhūṣaṇa notes "gṛhya iva ity atra guṇābhāva ārṣaḥ" — pure grammar (a vowel-gradation irregularity, Ārṣa usage) — invisible to reader. Reject. V.36: restates. V.37: restates (structural bridging). V.38: Tilaka: "kṛtakṣaṇaḥ punaryuddhe kṛtotsāhaḥ" — interesting: this is a THIRD reading of kṛtakṣaṇa (cf. my sarga-46 note where Tilaka/Bhūṣaṇa agreed on "awaiting the moment" for 46.41's kṛtakṣaṇaḥ) — here in 47.38, Tilaka glosses kṛtakṣaṇaḥ as "kṛta-utsāhaḥ punar-yuddhe" = "one who has readied himself/gathered enthusiasm for renewed battle" — a notably DIFFERENT reading from 46.41's "awaiting/having obtained the opportunity" sense! This is the same exact phrase "kṛtakṣaṇaḥ kāla iva prajākṣaye" recurring (formulaic repetition across the sarga boundary), and Tilaka glosses it differently here than the parallel passage. Given Leonov/Kostina's own note on 47.38 flags this connection explicitly ("нужна ссылка на 46.41 или комм"), this is exactly the kind of cross-reference gap that deserves a note: Tilaka's shift from "awaiting the moment" (46.41, consensus with Bhūṣaṇa) to "readied himself for renewed battle" (47.38) shows the tradition reads the repeated formula with a different nuance each time it recurs. This is a strong candidate — complements_leonov (directly answers Kostina's flagged cross-reference need), contrastive-ish (differs from the reading at 46.41 within the same commentator's own tradition). Draftable.

Now let me finalize my selection for sarga 47. Candidates identified:
1. v.2 — sadasi=yāgaśālāyām (Śiromaṇi) — answers Kostina's flagged question
2. v.5 — Bhūṣaṇa's bandhura crux (multiple named alternate readings)
3. v.6 — Bhūṣaṇa's variant-reading/redundancy resolution
4. v.8 — Tilaka's psychological motivation (complements Leonov)
5. v.15 — Bhūṣaṇa's double-simile disentangling
6. v.17 — Tilaka+Bhūṣaṇa's noon/hyperbole reading
7. v.26 — Tilaka's variant reading (mārutiḥ self-reference)
8. v.38 — Tilaka's kṛtakṣaṇaḥ reading vs 46.41, answering Kostina's cross-ref flag

That's 8 out of 38 real verses (+ 4 merged markers rejected) = 42 considered, 8 drafted ≈ 19%. That's too high vs the target. I need to cut to the strongest ~4-5. Let me rank by strength:

**Strongest** (clear, unambiguous value, directly resolves a flagged gap or genuine textual crux):
- v.2 (answers Kostina's explicit question) — KEEP
- v.38 (answers Kostina's explicit cross-reference request) — KEEP
- v.26 (genuine named textual variant with real interpretive consequence) — KEEP
- v.5 (genuine multi-reading crux, Bhūṣaṇa cites named alternatives) — KEEP

**Weaker/more marginal** (real but thinner, more ornamental):
- v.6 (redundancy-avoidance technical note — thinner)
- v.8 (psychological motivation — plausible but soft, and Leonov's note already covers the two main glosses on this verse)
- v.15 (double-simile disentangling — genuine but somewhat technical/rhetorical, lower reader impact)
- v.17 (noon/hyperbole reading — nice but ornamental, doesn't change core meaning)

I'll cut to 5 total, keeping the 4 strongest plus v.17 (since it's a clear contrastive-adjacent consensus reading that changes how a reader perceives the image, matching the brief's valued "narrative-function/doctrinal" register). That gives 5/42 ≈ 11.9%, closer to target range. Let me finalize.

- 🔧 `Bash` — echo "finalizing sarga 47 selection: v2, v5, v17, v26, v38 = 5 drafts"
Now let me write the sarga 47 output file with all 38 verses + 4 merged markers accounted for (5 drafted + 37 rejected = 42).

- 🔧 `Write` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_47_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_s47_check.txt
Sarga 47 reconciles (5 + 37 = 42), no BOM. Now let's move to sarga 48.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_48_segmented.json
This is a big sarga (74 verses). Let me continue reading.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_48_segmented.json
Let me continue reading the remaining verses.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_48_segmented.json
Now I have the full sarga 48 (74 verses stated, 62 real verse bundles [1-61 + one v.62/68 which are empty-content artifacts] + 12 merged-range markers). Let me get the dedup slices.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_leonov_sarga_48.json
This is a substantial dedup list (24 entries). Let me get the Phase-1 notes too.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_phase1_sarga_48.json
Now I have all context for sarga 48 (74 verse_count per meta, but let me verify actual count of verse entries in the list).

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_s48_counts.txt
Confirmed: 74 total bundles = 60 real numbered verses (1-61, missing v.18 as standalone but it's covered — wait, 1-61 is 61 verses, but v.18 is missing from the ids list since it appears merged into others; actually checking: ids has 1-17, then 19-61 = 60 real verses) + verse 62 and 68 (empty-content artifacts, `ambiguous_marker:false` but empty) + 12 true ambiguous-range markers = 74 total. Let me go through this large sarga systematically.

**5.48.1**: Leonov's own note ALREADY covers manaḥ samādhāya extensively (medieval commentators: hidden fear; Śiromaṇi: grief over son's loss). Bundle confirms exactly this (Tilaka: putranāśakhinnam api cetaḥ dhīratayā 'prakāśitabhayaṃ pratiṣṭhāpya = fear; Śiromaṇi via preamble: śokaṃ vimucya = grief). Duplicate. Reject.

**5.48.2**: Bhūṣaṇa/Śiromaṇi restate mechanically (astravit=brahmāstravit). Phase-1 has pitāmahārādhana note. Reject.

**5.48.3**: Leonov's own note covers sureśvarasamāśritāḥ. Bundle restates. Reject.

**5.48.4**: restates via trivial synonym chains + Phase-1 covers deśakālapradhāna already. Reject.

**5.48.5**: Tilaka gives a genuine textual-variant note: "'karmaṇā' ity eva pāṭhaḥ sāṃpradāyikaḥ iti katakaḥ" — cites the named scholar/commentator "Katakaḥ" (a recognized authority, likely referring to Kataka Mādhava Yogīndra, an alternate/earlier commentator) confirming a specific reading is "traditional" (sāṃpradāyika). This is a genuine citation of an authority validating a textual reading — but this is thin/technical (just validates a reading choice with no semantic consequence for a Russian reader). Reject — too technical, no interpretive payoff.

**5.48.6**: Leonov's own note covers this exactly. Reject.

**5.48.7**: Tilaka has an oddly extensive passage that seems misaligned (quoting "samāhitātmā... smaran vraja akṣataṃ..." — this is actually v.12's content, a marker/content misalignment). Reject — restates/misaligned.

**5.48.8**: Bhūṣaṇa/Śiromaṇi restate + Śiromaṇi adds an implicit logical point: "nanu tarhi mama api vadhaḥ syād ity ata āha na iti" (if so, wouldn't I too be killed? [Rāvaṇa] answers: no) and "etena atiprabalatvāt tava vadho na bhaviṣyati iti dhvanitam" (this implies/suggests that due to Indrajit's superior strength, HE won't be killed [unlike Akṣa]) — this is a genuine dramatic-irony/foreshadowing observation: Śiromaṇi reads Rāvaṇa's assurance as an implicit prophecy (which will of course be falsified — spoiler: Indrajit does eventually die, but not to Hanuman). Actually, thinking about this more, this reading emphasizes Rāvaṇa's parental anxiety/reassurance as containing a dramatic irony the подстрочник doesn't flag. This is a decent narrative-function observation. Let me hold it as a candidate.

**5.48.9-14**: Let me scan quickly — mostly trivial synonym glosses (bhusana glossing prabhāvam=antaḥśaktim, parākramam=pauruṣam — restates). V.13's Leonov note doesn't exist but Phase-1 covers rājadharma. Tilaka/Bhūṣaṇa/Śiromaṇi mostly restate the verse. Reject 9-14 (v.14's Leonov note already covers nānāśāstreṣu with variant nānāśastreṣu, Tilaka in bundle confirms same content as tier-1 — duplicate).

**5.48.15**: Kostina's own note flags "обошел почтительно повелителя" as needing a realia comment (пояснение по реалиям — i.e., about pradakṣiṇa, circumambulation). Śiromaṇi/Tilaka/Bhūṣaṇa all just restate "pradakṣiṇaṃ cakāra" mechanically without actually explaining the custom's significance — EXCEPT Bhūṣaṇa quotes Viṣṇu Purāṇa on dakṣasutāḥ (a genuine cross-textual citation: "manasā tv eva bhūtāni pūrvaṃ dakṣo 'sṛjat tathā / devān ṛṣīn sagandharvān uragān pakṣiṇas tathā" — Dakṣa created beings by mind, including gods, sages, gandharvas, serpents, birds). This IS a real citation with content (naming the Purāṇic source for the dakṣasuta epithet), which Phase-1's note on dakṣasuta doesn't include (Phase-1 mentions Dakṣa's daughters as mothers of gods generically, but doesn't cite this specific Viṣṇu Purāṇa verse). This is draftable — a genuine cited cross-text source (kazansky В, realia, citing named Purāṇic verse) that complements Phase-1's dakṣasuta note with a textual citation. But does it answer Kostina's specific pradakṣiṇa question? Not directly — her question was about circumambulation ritual, not about dakṣasuta. Let me treat this as its own candidate on dakṣasuta (complements Phase-1), separate from Kostina's still-unanswered pradakṣiṇa question (which remains unresolved — reject that angle).

**5.48.16**: Tilaka: "svagaṇair anyaiḥ sabhā-sthai rākṣasaiḥ" (clarifies "his own troops" = the other rakshasas present in the assembly) — minor. Reject — restates.

**5.48.17**: Leonov's own note covers samudra iva parvaṇi. Śiromaṇi/Tilaka restate ("vardhamāna iti śeṣaḥ" - trivial). Reject.

Given the accumulating pattern, let me push forward through the remaining verses more efficiently, focusing only on genuinely new content.

- 🔧 `Bash` — echo "continuing scan v18-61"
**v.18 doesn't exist as own bundle** (merged into markers 1820/1920). **v.19-25**: mostly restate. **v.19**: restates. **v.20**: Bhūṣaṇa notes a grammatical/textual ellipsis point about "jyāsvanam" (compound parsing, thin, invisible). Reject. **v.21**: Tilaka trivial gloss. Reject. **v.22**: Tilaka: "diśaś ca ity utpātavarṇanam" (identifies this as an utpāta-varṇana, an "omen description" — a recognized narrative convention/genre marker) — this labels the verse as belonging to a specific epic convention (bad omens preceding battle), which the подстрочник doesn't flag as such. This is a modest but real generic/narrative-convention observation. Let me keep as a soft candidate.

**v.23**: Leonov's own note flags "чакрачары и" needing commentary (Kostina notes Goldman links cakracarāḥ to ṛṣis, Gita-Press to siddhas). Bundle: Tilaka says "cakracarā grahāḥ" (= "wandering in a circle" = planets/celestial bodies, "grahāḥ")! This is a THIRD distinct reading (not ṛṣis, not siddhas, but "planets/grahas that move in circuits") that directly answers Kostina's flagged question with a genuine new option from the ṭīkā tradition. This is strongly draftable — complements_leonov, resolves an open flagged question with new information. 

**v.24-27**: restate mechanically. Reject.

**v.28**: Leonov's own note ALREADY covers susaṃtatān (Tilaka: avirātān; Śiromaṇi: atidṛḍhān; Goldman: "long"). Bundle confirms same. Reject — duplicate.

**v.29**: Leonov's own note covers mṛdaṅgabherīpaṭahasvanam. Bundle restates. Reject.

**v.30-33**: restate. v.33: Kostina flags "Индраджита" needing an epithet comment (devasamānavikramau — "equal in valor to the gods" applied to both Hanuman and Indrajit) — bundle Bhūṣaṇa just glosses antaram=chidram (trivial). Reject.

**v.34**: Leonov's own note covers amogheṣu (arrows didn't harm his life). Tilaka/Bhūṣaṇa/Śiromaṇi restate the same point almost verbatim to Leonov's note. Reject — duplicate.

**v.35-38**: restate. Reject.

**v.39**: Leonov's own note covers prabhoḥ prabhāvāt (majority: Brahma; but Śiromaṇi: Rāma!) and pitāmaha (Brahma), plus Kostina's flagged open methodological question about "силы"/vega interpretation. Let me check bundle's Śiromaṇi content carefully: `"tataḥ...prabho rāmasya prabhāvāt vigato nivṛtto 'lpavego yasmāt mahāvega ity arthaḥ"` — wait, this appears in v.40's bundle (Śiromaṇi content there, mislabeled/shifted) — actually checking again: the v.39 bundle's Tilaka/Bhūṣaṇa don't mention Rāma; it's v.40's Śiromaṇi entry that reads "prabhoḥ" as Rāma (`prabho rāmasya prabhāvāt`)! This confirms Leonov's own note's claim precisely (Śiromaṇi reads prabhu = Rāma against the majority Brahma reading) — this is ALREADY in Leonov's note. Duplicate, but let me check if the bundle's specific location/anchor adds anything Leonov's note doesn't: Leonov's note says "автор комментария Широмани полагает, что речь здесь идет о Раме" — that's exactly what I found. Reject — duplicate.

**v.40**: Kostina's own note flags "даре" (dāna) needing comment, citing Gita-Press explanation. Bundle: does any commentator explain WHAT the specific vara (boon) from Brahma actually consists of? Checking Tilaka's content in v.40: "svāyaṃbhuvaiḥ svayaṃbhū-daivatyair anekavidhair mantrair abhimantritaṃ tat siddhaṃ bhavati tādṛśaṃ brahmāstraṃ tat-kṛta-nirodhaṃ buddhā pitāmahāt labdhaṃ vara-rūpaṃ dānaṃ prāg-ukta-rūpaṃ cintayāmāsa" — this just says "he thought of the boon previously mentioned" (referring back to something in an earlier sarga, not explaining it here). Doesn't resolve Kostina's flagged gap. Reject.

**v.41**: Leonov's own note covers lokaguroḥ, mayā anuvartitavyaḥ (Tilaka: muhūrtamātram, brief duration), AND Kostina's flagged open questions about voluntary submission and "ity evam evam." Phase-1 also covers lokaguru fully. Bundle restates same content. Reject — duplicate.

**v.42-44**: restate (v.44's guṇadarśanam already covered by Phase-1). Reject.

**v.45**: Leonov's own note covers samīkṣyakārī vinivṛttaceṣṭaḥ. Bundle restates. Reject.

**v.46-47**: v.47's Leonov note covers abhigarhaṇaṃ variant (abhigrahaṇa). Bundle (Tilaka/Śiromaṇi) restates without mentioning the variant. Reject both.

**v.48**: Phase-1 has a full note on astrabandha. Bundle restates the same logical point (astra-bond doesn't tolerate another bond) already fully covered. Reject.

**v.49**: Kostina's own note flags "смирным" wanting a comment ("as if still under the brahmastra's influence"). Bundle: Tilaka gives an EXTENSIVE alternate-reading discussion: "nānyena bandhe hy anuvartate 'stram" pāṭha (variant reading) with a totally different chintā (Indrajit's worry) — Tilaka's alternate interpretation: Indrajit worries that HIS OWN great deed (binding Hanuman with the astra) was rendered "meaningless" (nirarthakam) because the rakshasas didn't understand mantra-gati (this is exactly what v.50 says, but Tilaka is noting a variant that shifts WHOSE realization this is and what triggers Indrajit's concern one verse earlier than the "standard" reading). This is genuinely complex — but does it add real value for a Russian reader beyond what's already conveyed? The подстрочник translation of v.49 already conveys "though bound by another, [Hanuman] seemed to still obey the weapon" — and Kostina's flag asks for a comment on exactly this. Tilaka's gloss doesn't directly explain the "as if still bound" phrase's implication though — it discusses a textual variant for the NEXT clause. Let me look more carefully: is there a comment specifically on "anyena baddho 'py anuvartate 'stram" (though bound by another [tie], [he seems to] still obey/follow the [previous] weapon)? 

Actually, re-reading Śiromaṇi's note for v.49: "anyena baddho 'yam astram anuvartate atha iti hetoś cintāṃ jagāma" — this explains: BECAUSE Hanuman (bound now by ropes) still SEEMS to behave as if under the astra's compulsion, THAT'S WHY Indrajit becomes worried/thoughtful (i.e., Indrajit reads Hanuman's continued stillness as a possible ongoing effect of the astra, not just rope-compliance) — this is genuinely the interpretive key to why Indrajit "becomes anxious," which directly resolves Kostina's flagged question about what "смирным" (submissive-seeming) means and why it matters narratively. This is solid — draftable, complements_leonov (answers Kostina's flagged need directly).

**v.50**: Kostina's own note flags the "great deed made futile" / "we didn't think" contrast (Indrajit vs the rakshasas). Bundle restates the same contrast Kostina already identified via Goldman/Gita-Press comparison — no new content beyond what she's already flagged and resolved herself. Reject — duplicates her own already-resolved point.

**v.51**: Leonov's own note covers astreṇa hanumān mukto nātmānam avabudhyate (Tilaka: nāvabodhayati sma = didn't let it show; Śiromaṇi: didn't know himself). Bundle restates exactly. Reject — duplicate.

**v.52**: Leonov's own note covers kālamuṣṭibhiḥ variant (kāṣṭhamuṣṭibhiḥ). Bundle restates same variant. Reject — duplicate.

**v.53-54**: restate. Reject.

**v.55**: Leonov's own note covers ko 'bhyupāśrayaḥ (Tilaka: "by whose help is he so fearless"). Bundle: Tilaka ALSO adds distinguishing content: "kāryaṃ kartavyam arthas tat-prayojanaṃ ca. samāhāra-dvandvaḥ arthasya mūlam ukta-prayojana-pravartakam. uttarāśayas tu dūtyaṃ kṛtyam, prerakaḥ sugrīva iti" — this is a genuinely interesting note: Tilaka explicitly states the "answer" implied by the narrative structure — "the underlying purport [of these questions] is: his task is a diplomatic mission (dūtya), and his sender is Sugrīva" — i.e., Tilaka is glossing the rhetorical questions posed by the rakshasas with the ANSWER the reader/audience already knows (dramatic irony: we know Hanuman is Sugrīva's envoy, though the rakshasas don't). This is a genuine dramatic-irony observation not in Leonov's note (which only covers ko'bhyupāśrayaḥ) nor подстрочник. Draftable — complements_leonov.

**v.56**: restates. Reject. Though note: Tilaka's fragment here is oddly a long discussion of nānāśāstreṣu again (misaligned/duplicated content from elsewhere, likely a segmenter glitch pulling in v.14 material) — reject as restating/misaligned.

**v.57-61**: mostly restate mechanically. Reject all.

Now let me also check v.8's Śiromaṇi content once more and v.22's utpāta-varṇana more carefully, then finalize my candidate list.

Candidates identified for sarga 48:
1. v.8 — Śiromaṇi's dramatic-irony reading (implicit foreshadowing that Indrajit alone, unlike Akṣa, will survive)
2. v.15 — Bhūṣaṇa's cited Viṣṇu Purāṇa verse on Dakṣa's creation (complements Phase-1's dakṣasuta note)
3. v.22 — Tilaka's utpāta-varṇana genre-label (soft)
4. v.23 — Tilaka's third reading of cakracarāḥ = grahāḥ (planets) — resolves Kostina's flagged question
5. v.49 — Śiromaṇi's explanation of why Indrajit grows anxious (answers Kostina's flagged "смирным" question)
6. v.55 — Tilaka's dramatic-irony gloss (the implied answer: Hanuman is Sugrīva's envoy)

That's 6 candidates. Given this is a 74-bundle sarga (62 real considered + 12 merged markers), 6/74 ≈ 8.1% — right in the target range. Let me weigh strength: v.22 is the weakest (thin genre-label, no real interpretive content change) — I'll cut it. That gives 5/74 ≈ 6.8%, solidly in range. Let me finalize with 5: v.8, v.15, v.23, v.49, v.55.

- 🔧 `Bash` — echo "finalizing sarga 48: v8, v15, v23, v49, v55 = 5 drafts; 69 rejects; 74 considered"
Now let me write the sarga 48 output file. I need reject entries for all 69 remaining verses (62 real + 12 markers - 5 drafted = 69).

- 🔧 `Write` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_48_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_s48_check.txt
Sarga 48 reconciles (5 + 69 = 74). Now let's move to sarga 49, the final one, and a much shorter sarga (only 6 dedup notes on each side, suggesting fewer verses).

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\segmented\sarga_49_segmented.json
Now sarga 49 (27 verses total: 19 real numbered verses 1-19, 2 empty-content artifacts at 23/46, and 6 merged-range markers). Let me check the dedup files, which I already have.

- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_leonov_sarga_49.json
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_phase1_sarga_49.json
Now let me work through sarga 49 verse by verse.

**5.49.1**: Leonov's own note ALREADY covers this fully and explicitly — including Tilaka's unusual minority reading (rakṣo'dhipam = Indrajit, not Rāvaṇa!) and Gita-Press's blended interpretation. Bundle: Tilaka's fragment (in preamble/v.1) confirms exactly this: "tasyendrajitaḥ. yat tu rāvaṇasyeti tan na, tena hanūmati kasyāpi karmaṇo 'kṛtatvād iti katakaḥ. putradvārā svabandhanakarmaṇety artha iti tīrthaḥ" — this is EXACTLY the content already in Leonov's note (Tilaka says it's Indrajit not Rāvaṇa, citing named authorities Kataka and Tīrtha for the reasoning). Reject — duplicate, already fully covered.

**5.49.2**: Phase-1 has a full note on mukuṭa. Bundle (Bhūṣaṇa) restates verse mechanically. Reject.

**5.49.3**: Phase-1 has a full note on vajrasaṃyoga. Bundle restates. Reject.

**5.49.4**: Tilaka glosses bhaktibhiḥ = "śaiva-tripuṇḍra-vad racanā-viśeṣaiḥ" ("like the Shaiva three-line forehead marks" — i.e., the decorative lines on Rāvaṇa's body are compared to Shaiva sectarian tilaka markings). This is a genuine realia note: identifying the specific decorative convention (Shaiva tripuṇḍra) behind "vicitrābhir vividhābhiś ca bhaktibhiḥ" (variegated lines/patterns), which the подстрочник renders generically as "разноцветными разнообразными линиями (орнаментами)." This is a real addition — a specific religious-iconographic identification not otherwise given. Draftable — kazansky В (realia, sectarian marking convention), single-commentator (Tilaka).

**5.49.5**: Tilaka/Bhūṣaṇa/Śiromaṇi restate mechanically (описание внешности Раваны, glossed synonymously). Reject.

**5.49.6**: Leonov's own note ALREADY covers śirobhir daśabhiḥ (Tilaka: normally one head, but ten-headed form assumed for this encounter/battle). Bundle confirms: Tilaka here says "śirobhir daśabhir iti hanūmato darśana-kāle raṇe iva bhīṣaṇa-rūpa-karaṇād iti bodhyam" — exactly matches Leonov's note. Reject — duplicate.

**5.49.7**: Leonov's own note covers pūrṇacandrābhavaktreṇa and the sabālārkam/sabalākam variant (citing Jhala's critical edition) AND Kostina's flag about Goldman linking the moon-simile to a gem in the necklace. Bundle: Bhūṣaṇa actually explains EXACTLY that Goldman-point already: "pūrṇacandrābhavaktreṇa pūrṇacandra-tulya-nāyaka-ratnena. vaktraṃ nāyakaratnam abhito-lagna-muktā-maṇi-maṇḍalam" — Bhūṣaṇa glosses "vaktra" (face) here NOT as Rāvaṇa's literal face, but as the "chief gem" (nāyaka-ratna) of the necklace, surrounded by a ring of pearls! This is the EXACT source of what Kostina flagged as "Goldman's interpretation" — this is the primary ṭīkā source Goldman must have drawn from. This directly resolves/traces Kostina's flagged comment to its ṭīkā origin. This is strongly draftable — complements_leonov (traces the exact commentarial source behind the flagged Goldman note), contrastive-ish (offers an alternate reading of "vaktra" against the plain "face" reading the подстрочник takes). Kazansky Б.

**5.49.8**: Leonov's own note covers keyūra/aṅgada terminology already. Bundle restates. Reject.

**5.49.9-14**: mostly restate mechanically (descriptions of throne, attendants, ministers). Let me check for anything genuinely new. V.9: restates. V.10: restates. V.11: restates (names of ministers, matches подстрочник). V.12: Tilaka glosses "catur-bhiḥ sāgaraiḥ parivṛtaṃ taṃ kṛtsnaṃ lokaṃ bhūmaṇḍalam iva ity arthaḥ" — trivial confirmation of simile. Reject. V.13: restates. V.14: restates.

**5.49.15**: restates (Hanuman's astonishment despite being tormented). Reject.

**5.49.16**: restates (Hanuman dazzled by Rāvaṇa's brilliance, begins to think). Reject.

**5.49.17**: Kostina's own note flags "благими знаками" (sarvalakṣaṇayuktatā, "possessed of all auspicious marks") as needing a comment later. Bundle: Śiromaṇi just restates "rāṣakṣasarājasya rūpādi-sarva-lakṣaṇa-yuktatā ca aho āścaryam" — doesn't explain WHAT the specific lakṣaṇas are (no enumeration of the 32/108 auspicious marks tradition). Doesn't resolve Kostina's flagged gap with anything concrete. Reject.

**5.49.18**: Kostina's own note flags several open points (saśakrasyāpi omitted, "закону следовал" antonymic translation issue, nṛśaṃsaiḥ omitted). Bundle: Tilaka offers a genuinely rich double-reading here: "yadvā dharma ity ārṣād yajantam ayaṃ balavān rākṣaseśvaro yady adharmavān na syāt tadā śakrasya ity ādi prāgvat. adharma-hatatvāt tu sva-prajānām api nāśaka eva iti bhāvaḥ" — Tilaka proposes an alternate grammatical parsing (ārṣa/irregular form) AND adds a crucial extra clause: "but because he is ruined by adharma, he is a destroyer even of his OWN subjects" — this is a genuine extra interpretive point (not just protector-if-not-for-adharma, but actively harmful to his own people BECAUSE of adharma) that goes beyond what подстрочник conveys (which only states the hypothetical "would have been protector of heaven"). This adds a real facet: adharma doesn't just disqualify Rāvaṇa from cosmic protectorship — it makes him a destroyer of his own kingdom. This is a genuine additional facet, though it may verge into "Kostina already opened this can of worms" territory. Let me check if it resolves anything she flagged: her flags are about elliptical omissions (saśakrasyāpi, nṛśaṃsaiḥ) and translation choice for "закону следовал" (not clear which exact phrase this refers to — likely `adharma` construal). Tilaka's additional point about destroying his own subjects is a genuinely NEW facet not addressed by Kostina's flags directly, but it does relate to the same verse's core interpretive crux (dharma/adharma logic). I'll draft this — single-commentator, kazansky Б (textological — supplies an implied further consequence of the conditional).

**5.49.19**: restates (fear of Rāvaṇa, ekārṇavaṃ jagat). Phase-1 has a note on kāla for v.19-adjacent (though that lemma appears to be from a further verse not in this bundle — checking, Phase-1's V.49.19 note is about "kāla" but the actual verse content here doesn't mention kāla — let me check: this bundle's v.19 text is about Rāvaṇa's cruel deeds and his power to make the world one ocean, no "kāla" mention. So Phase-1's V.49.19 lemma may refer to a differently-numbered verse in the full sarga (this segmented bundle only goes to v.19; the sarga apparently has more verses beyond, referenced in Phase-1's V.49.20 lemma too, but those aren't in this segmented file). This confirms the segmented file only covers up to v.19 for this batch's dedup purposes — nothing to add for v.19 itself here. Reject — restates.

Now let me check v.23 and v.46 (empty-content artifacts) and the merged-range markers — these are non-independent, reject per rule (e)/artifact.

Let me finalize sarga 49 candidates: v.4 (Tilaka, Shaiva tripuṇḍra), v.7 (Bhūṣaṇa, vaktra=necklace gem), v.18 (Tilaka, adharma destroys own subjects). That's 3 drafts.

- 🔧 `Bash` — echo "finalizing sarga 49: v4, v7, v18 = 3 drafts; verses considered = 27"
3/27 ≈ 11.1%, within reasonable range for this shorter sarga. Now let me write the sarga 49 output file. I need to list all 24 rejects (27 - 3 = 24): verses 1,2,3,5,6,8,9,10,11,12,13,14,15,16,17,19 (16 real verses) + 2 empty artifacts (23,46) + 6 merged markers = 24.

- 🔧 `Write` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_49_candidates.json
- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_s49_check.txt
All four sargas reconcile with no BOM issues. Let me do a final sanity check across all four output files to confirm valid JSON and the hard style rules (no "М.: Наука 2022", correct Парибка form if mentioned, no Devanagari in note_ru).

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_final_check.txt
Good catch — let me check these three flagged notes. Per the brief, `contrastive: true` should list ≥2 commentators. Let me review each: 5.47.38 (kṛtakṣaṇaḥ vs 46.41) cites only Tilaka but contrasts against a prior verse's reading — this is cross-verse contrast, not same-verse multi-commentator, so `contrastive: false` is more accurate. Same logic for 5.48.23 (cakracarāḥ — contrasts against Western translators, not a second commentator in the bundle) and 5.49.7 (vaktra — contrasts against Goldman's interpretation, not a second ṭīkā). Let me fix all three to `contrastive: false`.

- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_47_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_47_candidates.json
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_48_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_48_candidates.json
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_49_candidates.json
- 🔧 `Read` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_49_candidates.json
- 🔧 `Edit` — C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready\data\analysis\phase2_batch3\sarga_49_candidates.json
Now let me re-run the validation check to confirm all issues are resolved and files are still well-formed.

- 🔧 `Bash` — cd "C:\Users\user\Documents\GitHub\CommentaryStrategies\.claude\worktrees\h268-lp-camera-ready" && p
- 🔧 `Read` — C:\Users\user\AppData\Local\Temp\claude\C--Users-user-Documents-GitHub\3c92a91d-16fd-4adf-abae-9346e856701a\scratchpad\h268_final_check2.txt
All four sarga files are clean: valid JSON, no BOM, counts reconcile exactly, no forbidden citations, no Devanagari in note text, and the contrastive flag now correctly requires ≥2 commentators only for genuine same-verse divergences.

Summary of all four sargas:

sarga 46: 51 considered / 7 drafted / 44 rejected / 1 contrastive
sarga 47: 42 considered / 5 drafted / 37 rejected / 0 contrastive
sarga 48: 74 considered / 5 drafted / 69 rejected / 0 contrastive
sarga 49: 27 considered / 3 drafted / 24 rejected / 0 contrastive

Output files (all in [data/analysis/phase2_batch3/](data/analysis/phase2_batch3/)):
- [sarga_46_candidates.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch3/sarga_46_candidates.json)
- [sarga_47_candidates.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch3/sarga_47_candidates.json)
- [sarga_48_candidates.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch3/sarga_48_candidates.json)
- [sarga_49_candidates.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/phase2_batch3/sarga_49_candidates.json)

No git commands were run. Every bundle across all four sargas was considered in verse order, dedup-checked against both `data/leonov_own_notes.json` and `data/sundara_commentary_to_add.json`, with per-verse reject entries (no ranges) so counts reconcile exactly against `verses_considered` in each file's `_meta`.

_Dr. Mārcis Gasūns_
