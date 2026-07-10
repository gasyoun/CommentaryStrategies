# Lexicon of Conceptual False Friends in Sanskrit–Russian Academic Translation

**CommentaryStrategies · M. Gasūns · 2026**  
Dual-purpose document: (1) scholarly framework for ВЯ article, (2) pipeline configuration for automated annotation.

---

## Theoretical Preamble

### Two kinds of false friend

**European false friends** (Kazansky's type): formal similarity between source and target terms masks semantic divergence. Example: Latin *magnanimitas* rendered as Russian «великодушие» — the forms rhyme but the cultural semantics diverge. The error is lexical: a translator who knows both languages can detect and correct it.

**Sanskrit false friends** (the type documented here): conceptual incommensurability — the Sanskrit term refers to a concept for which Russian provides no adequate structural slot. Any Russian rendering is a partial domestication. The error is ontological: it persists even for expert translators because the gap is in the conceptual systems, not in the individual translator's competence. Multiple contradictory Russian equivalents co-exist in the corpus for the same term, all partially correct, none fully adequate.

This distinction is the core argument of the ВЯ article: Sanskrit–Russian translation confronts a *qualitatively different* problem from what Kazansky describes for Latin–Russian translation, and Russian academic translators developed specific systematic responses to it.

### Three translation strategies (analytical framework for ВЯ article)

| Code | Name | Definition | Signal in notes |
|---|---|---|---|
| **T** | Transliterate + gloss | Sanskrit term kept (transliterated) in the translation itself; note explains the term | Note contains IAST or Russian transliteration + extended explanation |
| **C** | Contextual calque | Term translated differently depending on context; note acknowledges the variation or the inadequacy of any single rendering | Note contains phrase like «в данном контексте», «букв.», «точнее», or compares two Russian renderings |
| **D** | Domesticate | Single Russian equivalent used consistently; no note or a very short note (≤80 chars) | No note, or note that treats the Russian word as self-explanatory |

**Note — two frameworks, one argument.** T/C/D is the *analytical* taxonomy built for the ВЯ argument. The corpus (17,863 notes) encodes a related but distinct axis — **axis_4_paribok** — with three values from Paribok's original classification:

| Paribok code | Meaning | Relationship to T/C/D |
|---|---|---|
| **P** | Понятие — basic factual gloss or transliteration | ≈ T (simple) |
| **K** | Кодификатор — term treated as a key technical/conceptual node | ≈ T (extended) or C |
| **D** | Дискурсивное — term elaborated discursively; domesticated Russian used | ≈ C or D |

Each entry below has a **Corpus sample** line reporting actual Paribok P/K/D hits from the 50-note samples (300 notes total: Kalyanov / Vasilkov / Erman / Grintser / Syrkin / Leonov). The T/C/D assignments in the **Strategies** sections are analytical claims inferred from those hits and from scholarly assessment of the full translation practice; they are *hypotheses pending full-corpus extraction* for translators not yet in the sample (Sementsov, Burba, Petrov, Elizarenkova).

### Incommensurability scale (for ВЯ article)

- **Level I** — Partial equivalence: Russian equivalent captures 70–80% of semantic content; domestication is feasible with a short note (e.g., *mantra*, *āśrama* sense 1)
- **Level II** — Contextual divergence: term requires different Russian words in different textual contexts; calque is necessary; single equivalent misleads (e.g., *dharma*, *yoga*, *tapas*)
- **Level III** — Structural incommensurability: Russian conceptual apparatus lacks the distinction the Sanskrit term encodes; even transliteration + gloss fails to convey the full concept (e.g., *brahman* n. vs. *Brahmā* m., *ātman* as simultaneously individual and universal)

---

## Lexicon (25 Terms)

Organized in five conceptual groups. Each entry contains:
- Sanskrit term (IAST) + Russian transliteration standard
- Incommensurability level (I / II / III)
- The false friend (the obvious but misleading Russian rendering)
- Conceptual gap (why it misleads)
- **Strategies (analytical):** T/C/D assignment per translator — analytical claims, with "hypothesized" for translators not yet in the 50-note sample
- **Corpus sample (n=50/translator):** actual Paribok P/K/D hits from the annotation sample — verified data
- **Inferred strategy:** T/C/D translation from sample hits
- Corpus frequency estimate
- Pipeline search strings

---

### GROUP A: Metaphysical–Ontological Terms (7 terms)

---

#### 1. dharma — дхарма

**Level:** III  
**False friend:** «закон», «долг», «добродетель», «религия»  
**Conceptual gap:** *Dharma* simultaneously encodes cosmic order, social obligation, personal duty, moral law, and religious observance as aspects of a single concept — aspects that Russian and European languages assign to distinct, non-overlapping terms (law / duty / virtue / religion). No Russian word covers even two of these aspects simultaneously. The term is additionally context-dependent: the *dharma* of a king is not the *dharma* of a brahmin, and neither is identical with the cosmic *dharma* (= Vedic *ṛta*). Any consistent single rendering creates systematic misleading: «закон» implies legislative authority; «долг» implies Kantian moral duty; «добродетель» implies a virtue ethics; «религия» implies a confessional system.

**Strategies:**
- **T (transliterate):** Note explains *dharma* as Sanskrit term with extended semantic analysis. Kalyanov, Syrkin, Burba.
- **C (calque):** Different Russian words in different passages; note acknowledges the variation. Vasilkov/Neveleva («закон справедливости», «правило», «нравственный долг» by context). Erman.
- **D (domesticate):** Consistent «закон» or «долг» with minimal or no note. Petrov 1788 (inherited from Wilkins's English «duty»). Grinnser (partial — uses «закон» in epic context but «долг» in Gita-adjacent passages).

**Corpus frequency:** HIGH — present in ~15–20% of all notes across corpus; the single most-discussed term.  
**Corpus sample (n=50/translator, Paribok P/K/D):** Kalyanov K×2 | Vasilkov P×2+K×2+D×2 | Erman D×1 | Grintser — | Syrkin K×1 | Leonov K×2 | Elizarenkova (samskrtam.ru, pending)  
**Inferred strategy:** Kalyanov T/C (K dominant) | Vasilkov mixed (all three strategies) | Erman C/D | Grintser — (not in sample) | Syrkin T/C | Leonov T | Sementsov T+theor. | Burba T | Petrov D  

**Pipeline search strings (Russian):**
- Transliteration: `дхарм` (covers дхарма, дхарме, дхармы, дхармой, дхарман)
- False friend flags: `\bзакон\b`, `\bдолг\b`, `\bдобродетел` (when appearing in note discussing Sanskrit original)
- IAST: `dharm`

---

#### 2. ātman — атман

**Level:** III  
**False friend:** «душа», «дух», «я», «самость»  
**Conceptual gap:** *Ātman* denotes the individual self AND, in Advaita Vedānta, the universal absolute self identical with *brahman*. Russian «душа» (soul) imports Christian dualist ontology: a created spiritual substance distinct from God and body. «Я» (I/self) imports Kantian/Fichtean subjectivity. «Самость» imports Jungian psychology (introduced by translators of Jung in the 1990s–2000s, creating retroactive confusion). None of these captures the non-dual Vedāntic meaning where individual ātman and universal Ātman are not two. Additionally, in non-Advaita systems (Viśiṣṭādvaita, Dvaita) *ātman* has a different ontological status — the same term, different philosophy. A note that explains *ātman* through the lens of one system silently excludes the others.

**Strategies:**
- **T:** «атман» + extended philosophical note. Syrkin (most systematic — his upanishadic corpus makes this unavoidable), Erman.
- **C:** «я», «душа», «личность» by context, with comparative note. Vasilkov/Neveleva.
- **D:** «душа» consistently, short or no note. Petrov 1788, Smirrnov (partially — uses «душа» in literary translation, explains in separate glossary).

**Corpus frequency:** HIGH — particularly dense in Syrkin (upanishads) and Erman (Gita).  
**Corpus sample (n=50/translator, Paribok P/K/D):** Kalyanov — | Vasilkov — | Erman D×1 | Grintser — | Syrkin P×1+K×1+D×7 | Leonov K×1 | Elizarenkova (samskrtam.ru, pending)  
**Inferred strategy:** Kalyanov C/T (not in sample) | Vasilkov C (not in sample) | Erman D | Grintser C (not in sample) | Syrkin T+D (complex: 7D but also K — discursive elaboration within T framework) | Leonov T | Sementsov T+theor. | Burba T | Petrov D  

**Pipeline search strings:**
- Transliteration: `атман`
- False friend flags: `\bдуш[аеуой]\b`, `\bсамост`
- IAST: `ātman`, `atman`

---

#### 3. brahman (n.) / Brahmā (m.) — Брахман / Брахма

**Level:** III (the n./m. distinction makes this worse than ātman)  
**False friend:** «Бог», «Абсолют», «Брахман» (collapsing both)  
**Conceptual gap:** Sanskrit distinguishes two terms homophonous in some forms: *brahman* (neuter) — the impersonal absolute, the ground of being, identified with ātman in Advaita — and *Brahmā* (masculine) — the creator god, one of the trimūrti, a personal deity who is himself a created being within larger cosmic time. Russian «Брахман» typically renders both, which conflates (a) the impersonal absolute and (b) a personal deity who is not that absolute. Additionally, «Бог» imports monotheistic concepts (omnipotence, creation ex nihilo, personal relationship) none of which apply to either brahman (n.) or Brahmā (m.). The collapse becomes especially damaging in philosophical passages of the Gita or Upanishads.

**Strategies:**
- **T:** «Брахман» (n.) vs. «Брахма» (m.) maintained as distinct, with a note on the n./m. distinction. Syrkin (systematic), Erman, Burba.
- **C:** «Абсолют» / «Мировой дух» / «Высший Брахман» for (n.), «Брахма» for (m.). Vasilkov/Neveleva.
- **D:** «Брахман» for both, or «Бог»/«Господь» in theistic contexts. Petrov 1788 (via Wilkins, who uses «the Supreme Being»).

**Corpus frequency:** HIGH  
**Corpus sample (n=50/translator, Paribok P/K/D):** Kalyanov P×1 | Vasilkov — | Erman D×2 | Grintser — | Syrkin P×2+K×1+D×3 | Leonov — | Elizarenkova (samskrtam.ru, pending)  
**Inferred strategy:** Kalyanov C (P in sample — basic gloss) | Vasilkov C (not in sample) | Erman T/D (distinguishes n./m. but D-heavy) | Grintser — | Syrkin T+D (K+D: treats as key concept with discursive elaboration) | Sementsov T+theor. | Burba T | Petrov D  

**Pipeline search strings:**
- Transliteration: `[Бб]рахман`, `[Бб]рахм[аеу]`
- False friend flags: `\bБог\b`, `\bАбсолют\b`, `Мировой дух`
- IAST: `brahman`, `Brahmā`, `brahm`
- Note: pipeline must flag when «Брахман» and «Брахма» are used interchangeably (no distinction in note)

---

#### 4. māyā — майя

**Level:** III  
**False friend:** «иллюзия», «обман», «видимость», «магия», «чары»  
**Conceptual gap:** *Māyā* has two distinct semantic layers that Russian «иллюзия» collapses: (1) in Advaita, the cosmic power by which *brahman* appears as the multiplicity of the world — not "illusion" in the sense of "unreal" but in the sense of "not ultimately real" (like a dream that is real while dreamed); (2) in theistic Śākta traditions, the creative power of the goddess, entirely positive. «Иллюзия» in modern Russian carries a purely negative epistemological connotation (a false belief), which misleads on both counts. «Магия» reduces it to folk magic. The philosophical content of *māyā* as a theodicy (why does the absolute appear as world?) is lost in all domesticating translations.

**Strategies:**
- **T:** «майя» + note distinguishing Advaita usage from folk usage. Syrkin, Erman, Sementsov.
- **C:** «иллюзия» in Advaita contexts, «сила/мощь» in Śākta contexts, with note. Vasilkov/Neveleva.
- **D:** «иллюзия», «обман», «волшебство» without note or with very short note. Petrov 1788, Grinnser (partial).

**Corpus frequency:** MEDIUM (less frequent than dharma/ātman but crucial in philosophical contexts)  
**Corpus sample (n=50/translator, Paribok P/K/D):** Kalyanov P×1 | Vasilkov K×1 | Erman P×1+D×1 | Grintser — | Syrkin — | Leonov — | Elizarenkova (samskrtam.ru, pending)  
**Inferred strategy:** Kalyanov P/C (basic gloss) | Vasilkov K→C (treats as key concept) | Erman mixed (P and D) | Grintser D/C (not in sample) | Syrkin T (not in sample, upanishadic context) | Sementsov T | Petrov D  

**Pipeline search strings:**
- Transliteration: `\bмай[яею]\b`
- False friend flags: `\bиллюзи`, `\bобман\b`, `\bволшебств`
- IAST: `māyā`, `maya`

---

#### 5. puruṣa — пуруша

**Level:** II–III  
**False friend:** «человек», «дух», «душа», «личность», «мужчина»  
**Conceptual gap:** In the Ṛgveda, *puruṣa* is the cosmic man whose sacrifice creates the world (RV 10.90 — Puruṣasūkta). In Sāṃkhya philosophy, *puruṣa* is the pure consciousness principle — passive, unchanging, witness — opposed to *prakṛti* (active matter). In the Mahābhārata/Gita, *puruṣa* oscillates between these meanings and also simply means "man/person." Russian «человек» captures only the last usage; «дух» imports Christian pneumatology; «личность» imports modern personalism. In Sāṃkhya contexts, rendering *puruṣa* as «дух» is particularly damaging because *puruṣa* is consciousness without qualities, which is nothing like the European concept of spirit.

**Strategies:**
- **T:** «пуруша» + note distinguishing Ṛgvedic, Sāṃkhya, and epic usages. Elizarenkova, Syrkin, Erman.
- **C:** «дух» in philosophical contexts, «человек» in epic narrative. Kalyanov, Vasilkov.
- **D:** «дух», «душа», «человек» without noting the shift. Petrov 1788.

**Corpus frequency:** MEDIUM  
**Corpus sample (n=50/translator, Paribok P/K/D):** Kalyanov — | Vasilkov K×1 | Erman D×1 | Grintser — | Syrkin — | Leonov — | Elizarenkova (samskrtam.ru, pending — Ṛgvedic puruṣasūkta is her specialty)  
**Inferred strategy:** Elizarenkova T | Syrkin T (not in sample) | Erman D (Puraṣottama treated discursively) | Kalyanov C (not in sample) | Vasilkov K→C (treats as Sāṃkhya concept) | Sementsov T | Petrov D  

**Pipeline search strings:**
- Transliteration: `[Пп]уруш`
- False friend flags: `\bдух[аеуи]?\b` (when in note about this term), `\bличност`
- IAST: `puruṣa`, `purusa`

---

#### 6. prakṛti — пракрити

**Level:** II  
**False friend:** «природа», «первовещество», «материя»  
**Conceptual gap:** In Sāṃkhya, *prakṛti* is the active material principle of the universe, containing and evolving through the three *guṇa*s. Russian «природа» imports Romantic/Enlightenment nature-philosophy (creative but non-conscious nature); «материя» imports Marxist dialectical materialism. Neither captures *prakṛti*'s constitutive role: it is not the physical world but the principle from which the physical world evolves when in contact with *puruṣa*. The *puruṣa/prakṛti* pair requires paired translation — translating *puruṣa* as «дух» and *prakṛti* as «природа» creates a misleading echo of German Idealism (Geist/Natur).

**Strategies:**
- **T:** «пракрити» as a pair with «пуруша», with note on Sāṃkhya. Elizarenkova, Syrkin, Sementsov.
- **C:** «природа», «первоматерия» by context. Erman, Vasilkov.
- **D:** «природа» consistently. Kalyanov (in non-philosophical passages).

**Corpus frequency:** LOW–MEDIUM (dense in upanishadic and Gita-philosophical notes)  
**Corpus sample (n=50/translator, Paribok P/K/D):** Kalyanov — | Vasilkov K×1 | Erman K×1 | Grintser — | Syrkin — | Leonov — | Elizarenkova (samskrtam.ru, pending)  
**Inferred strategy:** Elizarenkova T | Syrkin T (not in sample) | Erman K→T (treats as Sāṃkhya concept) | Vasilkov K→C | Kalyanov D (not in sample, non-philosophical passages)  

**Pipeline search strings:**
- Transliteration: `[Пп]ракрит`
- False friend flags: `\bприрод[аеуы]\b` (when in note distinguishing from *puruṣa*)
- IAST: `prakṛti`, `prakriti`

---

#### 7. ākāśa — акаша

**Level:** II  
**False friend:** «небо», «воздух», «эфир», «пространство»  
**Conceptual gap:** *Ākāśa* is the fifth and subtlest of the five classical Indian elements (*pañcamahābhūta*), often translated as "ether" after the Greek *aithēr*. But the Greek ether is a fifth element of celestial matter; *ākāśa* is the element of space itself, the medium through which sound travels, without mass. Russian «небо» (sky) adds spatial restriction (above); «воздух» (air) confuses it with *vāyu* (wind/air, the fourth element); «пространство» (space) is closest but lacks the elemental/physical-theory connotation. The false friend is compounded by the fact that in some contexts *ākāśa* is indeed "sky" (epic poetry) while in others it is a technical term of cosmology.

**Strategies:**
- **T:** «акаша» + note distinguishing cosmological from poetic usage. Elizarenkova, Syrkin.
- **C:** «эфир» in cosmological passages, «небо» in epic. Kalyanov, Vasilkov.
- **D:** «небо» or «воздух» consistently. Petrov 1788, Grinnser.

**Corpus frequency:** LOW (more frequent in Elizarenkova Rigveda than in epic corpus)  

**Pipeline search strings:**
- Transliteration: `[Аа]каш`
- False friend flags: `\bнеб[оеу]\b`, `\bэфир`
- IAST: `ākāśa`, `akasa`

---

### GROUP B: Soteriological–Ethical Terms (5 terms)

---

#### 8. karma — карма

**Level:** II  
**False friend:** «судьба», «рок», «участь», «возмездие», «воздаяние»  
**Conceptual gap:** *Karma* is the law of action-and-consequence operating across rebirths: every intentional action leaves a trace (*saṃskāra*) that conditions future experience. Russian «судьба» (fate) implies an external power determining outcomes (cf. the Moirai, Norns); *karma* is strictly causal and self-generated — there is no fate-giver, only the agent's own accumulated actions. «Возмездие» (retribution) implies punishment by an external moral authority. «Участь» (lot/portion) is too passive. The most common modern Russian usage of «карма» (from popular spirituality, strongly colored by the «возмездие» connotation — "what goes around comes around") is itself a false friend for translators trying to convey the technical philosophical concept.

**Strategies:**
- **T:** «карма» + note explaining the causal (not retributive, not fatalistic) mechanism. Syrkin, Erman, Sementsov.
- **C:** «деяние», «деяние и его последствия» in technical passages; «судьба», «участь» in narrative. Kalyanov, Vasilkov.
- **D:** «судьба», «рок», «воздаяние» without distinguishing the mechanism. Petrov 1788 (via Wilkins's «works»).

**Corpus frequency:** HIGH  
**Corpus sample (n=50/translator, Paribok P/K/D):** Kalyanov — | Vasilkov — | Erman D×1 | Grintser — | Syrkin K×1 | Leonov — | Elizarenkova (samskrtam.ru, pending)  
**Inferred strategy:** Kalyanov C (not in sample) | Vasilkov C (not in sample) | Erman D (nishkama-karma elaborated) | Grintser — | Syrkin T/C (K in sample) | Sementsov T | Burba T | Petrov D  

**Pipeline search strings:**
- Transliteration: `\bкарм[аеуы]\b`
- False friend flags: `\bсудьб`, `\bрок\b`, `\bвозмезди`
- IAST: `karma`, `karman`

---

#### 9. mokṣa — мокша

**Level:** II  
**False friend:** «спасение», «освобождение», «нирвана»  
**Conceptual gap:** *Mokṣa* is liberation from the cycle of rebirth (*saṃsāra*) — the soteriological goal of most Indian philosophical systems. Russian «спасение» (salvation) imports Christian soteriology: a sinner saved by divine grace from eternal damnation. *Mokṣa* involves no savior, no original sin, no grace in the Christian sense, and the "from what" is saṃsāra (not damnation). «Освобождение» (liberation, emancipation) is the most neutral and widely used, but it carries Soviet-era connotations of political liberation. «Нирвана» creates a cross-tradition confusion: *mokṣa* is the Hindu term; *nirvāṇa* is the Buddhist term; they are related but not identical.

**Strategies:**
- **T:** «мокша» + note distinguishing from Christian salvation and Buddhist nirvāṇa. Syrkin, Erman, Sementsov.
- **C:** «освобождение» as neutral calque, with a note acknowledging inadequacy. Vasilkov/Neveleva, Grinnser.
- **D:** «спасение» or «освобождение» without note. Kalyanov (uses «освобождение» consistently), Petrov.

**Corpus frequency:** MEDIUM  
**Corpus sample (n=50/translator, Paribok P/K/D):** Kalyanov D×1 | Vasilkov D×1 | Erman — | Grintser — | Syrkin — | Leonov — | Elizarenkova (samskrtam.ru, pending)  
**Inferred strategy:** Kalyanov D (confirmed in sample — «освобождение» without note) | Vasilkov D (confirmed — D in sample) | Erman T (not in sample, Gita context) | Grintser C (not in sample) | Syrkin T (not in sample) | Sementsov T | Petrov D  

**Pipeline search strings:**
- Transliteration: `\bмокш`
- False friend flags: `\bспасени`, `\bнирван` (when used as equivalent of mokṣa)
- IAST: `mokṣa`, `moksa`

---

#### 10. nirvāṇa — нирвана

**Level:** III  
**False friend:** «небытие», «уничтожение», «угасание», «блаженство», «рай»  
**Conceptual gap:** *Nirvāṇa* (Sanskrit/Pali) literally means "blowing out" (of the fires of craving, hatred, delusion). Western interpreters from Schopenhauer onward systematically read it as annihilation of consciousness — «небытие» (non-being). Buddhist doctrine explicitly rejects this: the Buddha refused to state whether the liberated being "exists" or "does not exist" after *nirvāṇa* (the question is "undeclared," *avyākata*). The annihilationist reading is the most common false friend. The opposite error is to render *nirvāṇa* as «блаженство» (bliss) or «рай» (paradise) — a positive-theology overcorrection. For the Sanskrit corpus (as opposed to Pali), *nirvāṇa* appears primarily in the Gita (BhG 2.72, 5.24–26, 6.15) with a specifically Vedāntic coloring — "nirvāṇa of brahman" (*brahmanirviṇa*) — which is not the same as the Buddhist concept. Toporov handles this distinction specifically; Russian Gita translators mostly collapse it.

**Strategies:**
- **T:** «нирвана» + note specifying the Gita usage vs. Buddhist usage. Erman (most careful), Sementsov.
- **C:** «угасание», «успокоение», «покой» — neutral calques that avoid both errors. Syrkin.
- **D:** «небытие», «уничтожение» (annihilationist) or «блаженство» (positive). Petrov 1788.

**Corpus frequency:** MEDIUM (dense in Gita and Toporov's Dhammapada)  
**Corpus sample (n=50/translator, Paribok P/K/D):** Kalyanov — | Vasilkov — | Erman D×1 | Grintser — | Syrkin — | Leonov — | Elizarenkova (samskrtam.ru, pending)  
**Inferred strategy:** Erman T/D (confirmed D: «Брахма-нирвана» elaborated with Buddhist parallel note) | Sementsov T | Syrkin C (not in sample) | Petrov D  

**Pipeline search strings:**
- Transliteration: `\bнирван`
- False friend flags: `\bнебыти`, `\bуничтожени`, `\bблаженств`
- IAST: `nirvāṇa`, `nirvana`

---

#### 11. saṃsāra — сансара

**Level:** I–II  
**False friend:** «круговорот», «переселение душ», «перерождение»  
**Conceptual gap:** The transliteration «сансара» is widely used and partially adequate. The false friends appear in two forms: (1) «переселение душ» (transmigration of souls) imports Greek metempsychosis with its Pythagorean/Platonic coloring — in Indian thought the "soul" that transmigrates is not identical across births (in Buddhism there is no *ātman* to transmigrate at all, only a causal stream); (2) «круговорот» (cycle/rotation) emphasizes the cyclic structure but loses the soteriological negative valence — in Indian thought saṃsāra is what one wants to *escape from*, not a neutral natural phenomenon.

**Strategies:**
- **T:** «сансара» as standard transliteration, short note on etymology. Most translators use this.
- **C:** «круговорот бытия», «колесо рождений» — extended calques. Vasilkov/Neveleva occasionally.
- **D:** «переселение душ» without qualification. Older translations, popular usage.

**Corpus frequency:** MEDIUM  

**Pipeline search strings:**
- Transliteration: `[Сс]ансар`
- False friend flags: `переселение душ`, `\bкруговорот\b`
- IAST: `saṃsāra`, `samsara`

---

#### 12. yoga — йога

**Level:** II  
**False friend:** «соединение», «единение», «путь», «метод», «система»  
**Conceptual gap:** The etymology (*yuj* = yoke, join) suggests «соединение» (union), but this is the most misleading rendering in non-technical contexts. In the Gita, *yoga* means a *path* or *discipline* (Karma Yoga, Jñāna Yoga, Bhakti Yoga) — «соединение» with what? is never specified. In Patañjali's Yoga Sūtras, *yoga* is defined as «chitta-vṛtti-nirodha» (cessation of mental fluctuations) — nothing to do with "union." In epic narrative, *yoga* often simply means "method," "skill," or "application." The modern popularized meaning (physical postures, āsana practice) is absent from classical Sanskrit except as one minor component of Patañjali's aṣṭāṅga yoga. The single Russian word «йога» carries all these connotations simultaneously and none precisely.

**Strategies:**
- **T:** «йога» + note specifying which of the distinct meanings applies. Erman (most careful — the Gita's three-yoga structure demands this), Sementsov.
- **C:** «путь», «метод», «дисциплина» by context, with note. Vasilkov/Neveleva.
- **D:** «йога», «соединение», «единение» without contextual specification. Kalyanov (partially), Petrov, Grinnser.

**Corpus frequency:** HIGH (especially dense in Gita commentary)  
**Corpus sample (n=50/translator, Paribok P/K/D):** Kalyanov — | Vasilkov D×1 | Erman K×1+D×1 | Grintser — | Syrkin P×1 | Leonov — | Elizarenkova (samskrtam.ru, pending)  
**Inferred strategy:** Kalyanov D/C (not in sample) | Vasilkov D→C (domesticates in epic context) | Erman T/D (K = technical elaboration; D = Sāṃkhya/yoga contrast) | Grintser D (not in sample) | Syrkin P→T (basic term recognition) | Sementsov T | Burba T | Petrov D  

**Pipeline search strings:**
- Transliteration: `\bйог[аеуи]\b`, `\bйогин`
- False friend flags: `\bсоединени`, `\bединени`
- IAST: `\byoga\b`
- Note: high false-positive rate — «йога» in the source text is not always a term being explained; filter for notes that define or explain the term

---

### GROUP C: Devotional–Ritual Terms (5 terms)

---

#### 13. bhakti — бхакти

**Level:** II  
**False friend:** «вера», «преданность», «набожность», «любовь к Богу»  
**Conceptual gap:** *Bhakti* is a specific soteriological practice: devotional relationship to a personal deity (especially Viṣṇu/Kṛṣṇa or Śiva) as a means of *mokṣa*. Russian «вера» (faith) imports Protestant/Orthodox connotations of cognitive assent to doctrine — *bhakti* involves no doctrinal assent requirement; it is relational and affective. «Преданность» (devotion/loyalty) is closest but loses the theological content: *bhakti* is not mere loyalty but a specific soteriological path equal in standing to Jñāna Yoga and Karma Yoga. In the Gita context (Bhakti Yoga, BhG 12), rendering *bhakti* as «любовь к Богу» conflates it with Christian agape/caritas.

**Strategies:**
- **T:** «бхакти» + note on soteriological standing. Erman, Sementsov, Syrkin.
- **C:** «преданность» as close approximation, note on theological content. Vasilkov/Neveleva.
- **D:** «вера», «набожность», «любовь к Богу». Petrov 1788, Blinderman (who however handles this within the tika framework).

**Corpus frequency:** MEDIUM  
**Corpus sample (n=50/translator, Paribok P/K/D):** Kalyanov — | Vasilkov — | Erman D×2 | Grintser P×1 | Syrkin — | Leonov — | Elizarenkova (samskrtam.ru, pending)  
**Inferred strategy:** Erman D→T (both bhakti notes D-coded: discursive elaboration of theological content) | Grintser P (basic realia note) | Sementsov T | Syrkin T (not in sample) | Petrov D  

**Pipeline search strings:**
- Transliteration: `\bбхакт`
- False friend flags: `\bвер[аеуы]\b` (in definitional context), `\bнабожност`
- IAST: `bhakti`

---

#### 14. yajña — яджня / жертвоприношение

**Level:** II–III  
**False friend:** «жертвоприношение», «жертва», «обряд»  
**Conceptual gap:** *Yajña* is the Vedic sacrificial ritual — but the term carries theological weight absent from Russian «жертвоприношение» (sacrifice): in the Ṛgveda and Brāhmaṇas, *yajña* is not merely a religious ceremony but the cosmological act that sustains the universe. The gods eat the sacrifice, the sacrifice feeds the gods, the gods send rain, the rain grows grain, the grain is offered — the world runs on *yajña*. In BhG 3.10–15, Kṛṣṇa explicitly describes the universe as operating through *yajña*. None of this is in «жертвоприношение». Additionally, in the Gita, *yajña* is metaphorized: action itself, knowledge, breath are all described as *yajña* (BhG 4.24–33). The false friend is most damaging here — "offering one's senses as sacrifice" sounds bizarre if *yajña* = «жертвоприношение».

**Strategies:**
- **T:** «яджня» + note on cosmological and metaphorical extensions. Elizarenkova, Sementsov (who is the most systematic on the ritual reading of the Gita).
- **C:** «жертвоприношение» in ritual contexts, «жертва», «служение», «деяние» in metaphorical contexts. Erman, Vasilkov.
- **D:** «жертвоприношение» consistently. Kalyanov, Petrov.

**Corpus frequency:** MEDIUM (high in Elizarenkova Rigveda, medium in Gita)  
**Corpus sample (n=50/translator, Paribok P/K/D):** Kalyanov P×1 | Vasilkov — | Erman — | Grintser — | Syrkin P×2+D×1 | Leonov — | Elizarenkova (samskrtam.ru, pending — central Rigvedic term)  
**Inferred strategy:** Kalyanov P→D (basic realia transliteration, no deeper elaboration) | Syrkin mixed (P for proper-noun uses, D for philosophical elaboration of sacrifice concept) | Elizarenkova T | Sementsov T | Petrov D  

**Pipeline search strings:**
- Transliteration: `[Яя]джн`
- False friend flags: `\bжертвоприношени`, `\bжертв[аеу]\b` (when in definitional note)
- IAST: `yajña`, `yajna`

---

#### 15. tapas — тапас

**Level:** II  
**False friend:** «аскеза», «подвижничество», «умерщвление плоти»  
**Conceptual gap:** *Tapas* derives from the root *tap* (heat, burn). Its primary meaning is the "heat" generated by ascetic practice — but this "heat" is cosmologically active: in the Ṛgveda, *tapas* is the power by which the creator god generates the universe. «Аскеза» (asceticism) captures the behavioral dimension (fasting, bodily mortification) but loses the creative/cosmological dimension: a ṛṣi's *tapas* can compel the gods, create new beings, and even threaten the cosmic order. «Умерщвление плоти» (mortification of the flesh) imports Christian ascetic theology (the body as sinful obstacle) — in Indian tradition the body is not sinful but is a vehicle and instrument of *tapas*. The range is also wider than physical practice: mental concentration, brahmacarya (celibacy), truth-telling are all *tapas*.

**Strategies:**
- **T:** «тапас» + note specifying cosmological and creative dimensions. Elizarenkova, Syrkin.
- **C:** «подвижничество», «аскеза» in practice contexts; «жар», «внутренний огонь» in cosmological contexts. Vasilkov/Neveleva.
- **D:** «аскеза», «умерщвление плоти». Kalyanov, Grinnser.

**Corpus frequency:** MEDIUM  
**Corpus sample (n=50/translator, Paribok P/K/D):** Kalyanov K×1 | Vasilkov — | Erman — | Grintser — | Syrkin P×1 | Leonov — | Elizarenkova (samskrtam.ru, pending — cosmological dimension is her focus)  
**Inferred strategy:** Kalyanov K→T (treats as key technical concept: «тапас — аскетическое подвижничество, порождающее магическую силу») | Syrkin P→T (basic transliteration) | Elizarenkova T | Vasilkov C (not in sample) | Grintser D (not in sample)  

**Pipeline search strings:**
- Transliteration: `\bтапас`, `\bтапа\b`
- False friend flags: `\bумерщвлени`, `\bаскез[аеуы]\b` (in definitional note)
- IAST: `tapas`

---

#### 16. mantra — мантра

**Level:** I  
**False friend:** «молитвенная формула», «заклинание», «гимн»  
**Conceptual gap:** *Mantra* is a Vedic verse, a sacred formula, or a sound-sequence regarded as having inherent sonic power. «Молитвенная формула» (prayer formula) imports petitionary-prayer theology (mantra is not a request to a deity but an efficacious sonic act). «Заклинание» (incantation/spell) implies folk magic and a belief in supernatural manipulation — in Mīmāṃsā philosophy, mantra works through the inherent power of sound (śabda), not through any supernatural agent. «Гимн» (hymn) captures the Ṛgvedic meaning (where many mantras are indeed hymns to gods) but loses the technical-sonic dimension. The modern popular usage of «мантра» in Russian (a phrase repeated for self-improvement) is a false friend for all academic contexts.

**Strategies:**
- **T:** «мантра» + short note. Almost universal among academic translators — Level I incommensurability means transliteration is viable.
- **C:** «формула», «стих», «гимн» by genre context. Elizarenkova (who distinguishes RV hymn from AV magical formula carefully).
- **D:** «заклинание», «молитва». Petrov 1788, popular translations.

**Corpus frequency:** MEDIUM  

**Pipeline search strings:**
- Transliteration: `\bмантр`
- False friend flags: `\bзаклинани`, `\bмолитвенн` (in definitional context)
- IAST: `mantra`

---

#### 17. āśrama — ашрам

**Level:** I (sense 1) / II (sense 2)  
**False friend:** Sense 1: «обитель» (adequate); Sense 2: «стадия жизни» (calque, acceptable)  
**Conceptual gap:** *Āśrama* has two distinct meanings: (1) a hermitage or forest retreat (the «ашрам» of popular usage — Level I, transliteration viable); (2) one of the four stages of life (*caturāśrama*): *brahmacarya* (student), *gṛhastha* (householder), *vānaprastha* (forest dweller), *saṃnyāsa* (renunciant). Sense 2 has no Russian equivalent whatsoever — «стадия жизни» (stage of life) is a calque that works only with explanation. The false friend is assuming that when a Sanskrit text mentions *āśrama*, it means sense 1 (a place) rather than sense 2 (a social institution) — the two are related but distinct.

**Strategies:**
- **T (sense 2):** «ашрам» (for the institution) + note specifying caturāśrama. Syrkin (unavoidable in upanishadic context), Vasilkov.
- **C (sense 2):** «жизненная стадия», «уклад жизни». Erman.
- **D (sense 1):** «ашрам», «обитель», «скит» without distinguishing senses. Kalyanov, Grinnser.

**Corpus frequency:** MEDIUM (higher in Syrkin upanishads)  
**Corpus sample (n=50/translator, Paribok P/K/D):** Kalyanov — | Vasilkov K×1 | Erman — | Grintser P×1 | Syrkin — | Leonov — | Elizarenkova (samskrtam.ru, pending)  
**Inferred strategy:** Vasilkov K→T (ванапрастха — caturāśrama treated as key concept) | Grintser P→D (sense 1: ашрам as hermitage, basic realia gloss) | Syrkin T (not in sample — unavoidable in upanishadic context) | Kalyanov D (not in sample, sense 1 dominant)  

**Pipeline search strings:**
- Transliteration: `[Аа]шрам`
- Flag note: pipeline should flag when «ашрам» appears in a note that also contains the words «стадия», «уклад», «домохозяин», «брахмачарья», «отшельник» — these signal sense 2 usage
- IAST: `āśrama`, `asrama`

---

### GROUP D: Cosmological–Social Terms (4 terms)

---

#### 18. guṇa — гуна

**Level:** II  
**False friend:** «качество», «свойство», «нить», «элемент»  
**Conceptual gap:** In Sāṃkhya, the three *guṇa*s (*sattva*, *rajas*, *tamas*) are the three constitutive strands or modes of *prakṛti* — not qualities in the Aristotelian sense (accidental properties of a substance) but the very fabric of material existence. «Качество» (quality) suggests an Aristotelian reading. «Свойство» (property/attribute) is similarly misleading. «Нить» (thread) — the literal meaning of *guṇa* — is sometimes used but sounds odd in philosophical context. In the Gita (BhG 14–18) the *guṇa* theory structures the entire ethics: *sattva* (lucidity/goodness), *rajas* (passion/activity), *tamas* (inertia/darkness). «Начало» (principle) is occasionally used and is closest to the philosophical meaning.

**Strategies:**
- **T:** «гуна» (pl. «гуны») + note on Sāṃkhya framework. Erman (most careful in Gita context), Sementsov, Syrkin.
- **C:** «начало», «стихия», «составляющая». Vasilkov/Neveleva.
- **D:** «качество», «свойство». Kalyanov (in non-Sāṃkhya epic passages).

**Corpus frequency:** MEDIUM  

**Pipeline search strings:**
- Transliteration: `\bгун[аы]\b`, `\bгуна\b`
- False friend flags: `\bкачеств`, `\bсвойств` (in definitional context)
- IAST: `guṇa`, `guna`

---

#### 19. varṇa — варна (vs. jāti — джати)

**Level:** III (as a pair)  
**False friend:** «каста»  
**Conceptual gap:** The word «каста» (from Portuguese *casta*) refers to the empirical reality of birth-groups (*jāti*) in Indian society — of which there are thousands. *Varṇa* refers to the theoretical four-class system of the Sanskrit texts: *brāhmaṇa*, *kṣatriya*, *vaiśya*, *śūdra* — which maps imperfectly onto *jāti* reality. Using «каста» for *varṇa* collapses the distinction between ideological model and social fact, which is precisely what much of critical scholarship (Dumont, Olivelle, Pollock) has worked to maintain. The false friend is compounded by the fact that *varṇa* literally means "color" — a dimension most Russian translators suppress or relegate to a brief etymological note.

**Strategies:**
- **T:** «варна» + note distinguishing from *jāti* and from «каста». Vasilkov/Neveleva (most consistent — their corpus has the highest cultural-commentary density), Erman.
- **C:** «сословие» (estate/class, sociologically closer than «каста»). Syrkin.
- **D:** «каста». Kalyanov (largely), Petrov 1788, Grinnser (partially).

**Corpus frequency:** MEDIUM–HIGH  
**Corpus sample (n=50/translator, Paribok P/K/D):** Kalyanov — | Vasilkov — | Erman — | Grintser — | Syrkin — | Leonov — | Elizarenkova (samskrtam.ru, pending)  
**Note:** Not detected in 50-note sample for any translator — frequency too low for sample detection; full-corpus extraction required.  
**Inferred strategy:** Vasilkov T (distinguishes varṇa/jāti) | Erman T | Syrkin C («сословие») | Kalyanov D («каста») | Grintser D/C | Petrov D  

**Pipeline search strings:**
- Transliteration: `\bварн[аы]\b`
- False friend flags: `\bкаст[аеуы]\b`
- IAST: `varṇa`, `varna`
- Note: pipeline should also flag the *varṇa/jāti* pair — notes that distinguish the two are T-strategy signals

---

#### 20. deva / asura — дева / асура

**Level:** I–II (each individually), II (as a pair)  
**False friend:** *deva* → «бог»; *asura* → «демон»  
**Conceptual gap:** *Deva* (divine being) and *asura* are not equivalent to God/Devil or angel/demon. In the Ṛgveda, *asura* means "powerful lord" (cognate with Avestan *ahura*) and is a positive title — the same being can be called *deva* and *asura*. The negative connotation develops later. «Демон» imports Christian demonology (fallen angel, servant of Satan); an *asura* is not fallen, not evil by nature, and not ontologically subordinate to a supreme deity. «Бог» for *deva* imports monotheistic attributes (omnipotence, omniscience, creator status) that no *deva* possesses — the *deva*s are powerful beings within a larger cosmological system, themselves subject to *karma* and rebirth.

**Strategies:**
- **T:** «дева» (or «дэва») for *deva*, «асура» for *asura* + note on historical semantics. Elizarenkova (systematic — the Rigvedic shift from positive to negative *asura* is documented in her notes).
- **C:** «боги» for *deva* in narrative contexts (pragmatic), «асуры» for *asura* as transliteration. Kalyanov, Vasilkov.
- **D:** «боги» and «демоны/ракшасы» — conflating *asura*, *rākṣasa*, *dānava*. Petrov 1788.

**Corpus frequency:** HIGH in epic corpus (Kalyanov, Vasilkov — epic is dense with deva/asura conflict)  
**Corpus sample (n=50/translator, Paribok P/K/D):** Kalyanov P×6 | Vasilkov P×1 | Erman — | Grintser — | Syrkin — | Leonov — | Elizarenkova (samskrtam.ru, pending — asura positive→negative shift is her documented specialty)  
**Inferred strategy:** Kalyanov P→C (6 P-coded hits: transliterates «асуры» in epic narrative without deep note; the Rigvedic semantic shift is not his focus) | Vasilkov P→C (same pattern) | Elizarenkova T (systematic: documents the asura valence shift) | Petrov D  

**Pipeline search strings:**
- Transliteration: `[Аа]сур`, `[Дд]ев[аы]\b`
- False friend flags: `\bдемон`, `\bбог\b` (when in definitional note about *asura*/*deva*)
- IAST: `deva`, `asura`

---

#### 21. ṛta — **[held for Elizarenkova/Rigveda article]**

*Ṛta* (Vedic cosmic order, predecessor of dharma) is not widespread in post-Vedic Sanskrit and does not appear in the current epic/upanishadic corpus. Full treatment is reserved for the planned Elizarenkova (Rigveda) annotation layer. Pipeline search: `\bṛta\b`, `\brita\b` (high false-positive rate — filter by context).

---

### GROUP E: Philosophical–Psychological Terms (4 terms)

---

#### 22. ahaṃkāra — ахамкара

**Level:** II  
**False friend:** «эго», «самосознание», «личность», «самость», «я-делатель»  
**Conceptual gap:** *Ahaṃkāra* (lit. "I-maker") is the Sāṃkhya principle by which *prakṛti* produces the sense of individual selfhood — the faculty that takes the universal consciousness (*puruṣa*) to be a particular individual. «Эго» imports Freudian psychoanalysis (the ego as the realistic principle between id and superego). «Самость» imports Jungian psychology. Neither maps onto the Sāṃkhya ontological role of *ahaṃkāra* as a cosmological *tattva* (principle), not a psychological agency. The literal rendering «я-делатель» is sometimes used (Burba) as a transparent calque; it is clumsy but accurate.

**Strategies:**
- **T:** «ахамкара» + note on Sāṃkhya place. Syrkin, Erman.
- **C:** «я-делатель», «самость», «чувство я». Burba (literal), Sementsov.
- **D:** «эго», «самосознание». Popular translations, Petrov 1788 (has no equivalent).

**Corpus frequency:** LOW–MEDIUM (dense in Syrkin upanishads and Erman/Sementsov Gita)  

**Pipeline search strings:**
- Transliteration: `[Аа]хамкар`, `я-делател`
- False friend flags: `\bэго\b`, `\bсамост` (in definitional context)
- IAST: `ahaṃkāra`, `ahamkara`

---

#### 23. buddhi — буддхи

**Level:** II  
**False friend:** «разум», «рассудок», «интеллект», «мудрость»  
**Conceptual gap:** In Sāṃkhya, *buddhi* (also called *mahat*, the "great one") is the first evolute of *prakṛti* — the faculty of discrimination (*viveka*) between *puruṣa* and *prakṛti*. «Разум» (reason/rationality) imports Kantian theoretical reason. «Интеллект» imports cognitive psychology. The Sāṃkhya *buddhi* is not a cognitive faculty in the modern sense but a cosmological principle, the subtle seat of consciousness through which *puruṣa* appears to have qualities it doesn't actually have. In the Gita, *buddhi-yoga* (the yoga of disciplined intellect) requires a precise rendering; «разум» works in casual usage but misleads in the philosophical passages of BhG 2–3.

**Strategies:**
- **T:** «буддхи» + note on Sāṃkhya role. Syrkin, Erman, Burba.
- **C:** «различающий разум», «интеллект» in philosophical contexts, «разум» elsewhere. Vasilkov.
- **D:** «разум», «рассудок». Kalyanov (in non-philosophical passages), Petrov.

**Corpus frequency:** LOW–MEDIUM  

**Pipeline search strings:**
- Transliteration: `[Бб]уддх`
- False friend flags: `\bразум\b`, `\bинтеллект\b` (in definitional note)
- IAST: `buddhi`

---

#### 24. śūnya / śūnyatā — шунья / шуньята

**Level:** III  
**False friend:** «пустота», «ничто», «небытие»  
**Conceptual gap:** *Śūnya* (zero, empty) and *śūnyatā* (emptiness, voidness) are core Buddhist Madhyamaka concepts: all phenomena lack inherent self-existence (*svabhāva*); they exist only in dependence on other phenomena. This is not nihilism: Nāgārjuna explicitly states that *śūnyatā* does not mean things don't exist, but that they don't exist *inherently*. Russian «пустота» (emptiness/void) in ordinary usage implies that "there is nothing there" — the nihilist reading Nāgārjuna argued against. «Небытие» (non-being) is even more misleading — importing Parmenidean/Hegelian ontology. For the Sanskrit corpus specifically (as opposed to Pali), *śūnya* appears in the Gita (BhG 6.13 — *śūnyavat*) with a much simpler meaning; the false friend is reading the simple usage through the Madhyamaka lens.

**Strategies:**
- **T:** «шуньята» + note on Madhyamaka reading vs. nihilist misreading. Toporov (Dhammapada — planned corpus); Erchenkov.
- **C:** «незначительность», «пустотность», «лишенность самобытия». Occasional in philosophical translations.
- **D:** «пустота», «небытие». Popular usage, Petrov 1788 (N/A for Gita context).

**Corpus frequency:** LOW in current corpus (Erchenkov only); will rise when Toporov annotated  

**Pipeline search strings:**
- Transliteration: `[Шш]унь`, `\bшунята\b`
- False friend flags: `\bпустот`, `\bнебыти`
- IAST: `śūnya`, `śūnyatā`, `sunyata`

---

#### 25. satya — сатья / истина / правда

**Level:** I–II  
**False friend:** «правда», «истина», «правдивость»  
**Conceptual gap:** *Satya* derives from *sat* (being, existent) — it is literally "that which is" and therefore "truth." Russian «правда» carries ethical-social connotations (justice, fairness in a community); «истина» is closer to philosophical truth but import European epistemological categories. The gap is widest in cosmological contexts: *satyaloka* (the realm of truth/being) is not "the realm of correct propositions" but "the realm of that which truly exists" — an ontological, not epistemological, truth. In ethics, *satya* (truthfulness) as one of the *yama*s of yoga philosophy is straightforward — Level I. In cosmology it is Level II.

**Strategies:**
- **T:** «сатья» + note on *sat*/*satya* relationship. Syrkin, Elizarenkova.
- **C:** «истина» in philosophical, «правда», «правдивость» in ethical contexts, with note. Vasilkov/Neveleva.
- **D:** «правда», «истина» consistently. Kalyanov, Grinnser, Petrov.

**Corpus frequency:** MEDIUM  

**Pipeline search strings:**
- Transliteration: `\bсатья\b`, `\bсатьям\b`
- False friend flags: `\bправд`, `\bистин` (in definitional note)
- IAST: `satya`

---

## Summary Table (Pipeline Configuration)

Columns: **Paribok K hits** and **Paribok D hits** are from the 50-note sample (n=300 total); "—" = not detected in sample. **Inferred T-dominant** lists translators assessed as T-strategy users (pending full-corpus extraction for Sementsov, Burba, Petrov, Elizarenkova).

| # | Term (IAST) | Level | False friend (RU) | Freq. | Paribok K (sample) | Paribok D (sample) | Inferred T-dominant |
|---|---|---|---|---|---|---|---|
| 1 | dharma | III | закон, долг | HIGH | Kal×2, Vas×2, Syr×1, Leo×2 | Vas×2, Erm×1 | Kalyanov, Syrkin, Leonov, Burba |
| 2 | ātman | III | душа, самость | HIGH | Syr×1, Leo×1 | Erm×1, Syr×7 | Syrkin, Erman, Sementsov, Burba |
| 3 | brahman/Brahmā | III | Бог, Абсолют | HIGH | Syr×1 | Erm×2, Syr×3 | Syrkin, Erman, Burba |
| 4 | māyā | III | иллюзия, обман | MEDIUM | Vas×1 | Erm×1 | Syrkin, Erman, Sementsov |
| 5 | puruṣa | II–III | человек, дух, душа | MEDIUM | Vas×1 | Erm×1 | Elizarenkova, Syrkin, Sementsov |
| 6 | prakṛti | II | природа, материя | LOW–MED | Vas×1, Erm×1 | — | Elizarenkova, Syrkin, Sementsov |
| 7 | ākāśa | II | небо, воздух, эфир | LOW | — | — | Elizarenkova, Syrkin |
| 8 | karma | II | судьба, рок | HIGH | Syr×1 | Erm×1 | Syrkin, Erman, Sementsov, Burba |
| 9 | mokṣa | II | спасение, освобождение | MEDIUM | — | Kal×1, Vas×1 | Syrkin, Erman, Sementsov |
| 10 | nirvāṇa | III | небытие, угасание | MEDIUM | — | Erm×1 | Erman, Sementsov |
| 11 | saṃsāra | I–II | переселение душ | MEDIUM | — | — | most (transliterate) |
| 12 | yoga | II | соединение | HIGH | Erm×1 | Vas×1, Erm×1 | Erman, Sementsov, Burba |
| 13 | bhakti | II | вера, преданность | MEDIUM | — | Erm×2 | Erman, Sementsov |
| 14 | yajña | II–III | жертвоприношение | MEDIUM | — | Syr×1 | Elizarenkova, Sementsov |
| 15 | tapas | II | аскеза, умерщвление | MEDIUM | Kal×1 | — | Elizarenkova, Syrkin, Kalyanov |
| 16 | mantra | I | заклинание, молитва | MEDIUM | — | — | most (transliterate) |
| 17 | āśrama | I/II | обитель / стадия | MEDIUM | Vas×1 | — | Syrkin, Vasilkov |
| 18 | guṇa | II | качество, свойство | MEDIUM | — | — | Erman, Sementsov, Syrkin |
| 19 | varṇa | III (pair) | каста | MED–HIGH | — | — | Vasilkov, Erman |
| 20 | deva/asura | I–II | бог/демон | HIGH | — | — | Elizarenkova (P×6 in Kal, P×1 in Vas — all transliterate) |
| 21 | ṛta | II–III | закон, правда | — | — | — | *held for Elizarenkova article* |
| 22 | ahaṃkāra | II | эго, самость | LOW–MED | — | — | Syrkin, Erman |
| 23 | buddhi | II | разум, рассудок | LOW–MED | — | — | Syrkin, Erman, Burba |
| 24 | śūnya/tā | III | пустота, небытие | LOW† | — | — | Toporov (planned), Erchenkov |
| 25 | satya | I–II | правда, истина | MEDIUM | — | — | Syrkin, Elizarenkova |

*Abbreviations: Kal=Kalyanov, Vas=Vasilkov, Erm=Erman, Gri=Grintser, Syr=Syrkin, Leo=Leonov.*  
† LOW in current corpus — will rise when Elizarenkova/Toporov layers annotated.  
*Elizarenkova (samskrtam.ru) not yet in annotation sample; strategy inferred from scholarly profile.*

---

## ВЯ Article Argument — How the Lexicon Maps to the Argument

### The five-point argument structure (sketch for article)

1. **European false friends ≠ Sanskrit false friends.** Kazansky's formulation (*magnanimitas* → «великодушие») describes a *lexical* problem: formal similarity masks semantic divergence. The 25 Sanskrit terms above describe an *ontological* problem: the Russian conceptual apparatus lacks the category the Sanskrit term encodes. This is a qualitatively different kind of translation obstacle.

2. **Three measurable strategies, not a continuum.** The T/C/D taxonomy is falsifiable: corpus search identifies the strategy for each translator on each term. The distribution of strategies is non-random: it correlates with reader-contract (philological → T; humanist → C; philosophical → T+theoretical note; popularizing → D).

3. **The "false friends" are a fingerprint of theoretical position.** How a translator handles *dharma* is a statement about their theory of commensurability: T-strategy assumes the reader should confront the incommensurability directly; D-strategy assumes the reader needs a bridge. Neither is an error — they are different reader-contracts made explicit.

4. **Diachronic shift (quantifiable).** From Petrov 1788 (D dominant) to Burba 2009 and Erchenkov 2008 (T dominant), Russian academic translation shows a measurable shift toward higher tolerance for incommensurability — more transliteration, longer notes, more explicit acknowledgment of the term's untranslatability. This is an empirical claim checkable from corpus data.

5. **The Gita case as proof of concept.** Six translators, same 25 terms, measurable divergence. Table from the ВФ article (Article 2) can be cross-referenced here, with the false-friend lexicon as the analytical key.

---

*Document version: 2026-05-15 · Next step: pipeline architecture for automated extraction*
