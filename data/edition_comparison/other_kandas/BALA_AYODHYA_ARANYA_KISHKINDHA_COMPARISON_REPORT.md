# Critical (GRETIL/Baroda) vs Southern (valmikiramayan.net) — Bāla / Ayodhyā / Araṇya / Kiṣkindhā

_Created: 12-07-2026_

> Method: same content-alignment pipeline as the Yuddhakāṇḍa comparison (`YUDDHA_COMPARISON_REPORT.md`)
> — difflib LCS + fuzzy token-Jaccard rescue, canonicalized via `sanskrit_util.nfold`
> (`CommentaryStrategies/scripts/sa_align.py`). Sources: GRETIL critical edition
> (`SamudraManthanam/GRETIL-1_sanskr/2_epic/ramayana/ram_0{1,2,3,4}_u.htm`, Tokunaga/Smith/Neill)
> vs valmikiramayan.net (K.M.K. Murthy Southern-recension text, Devanāgarī), all sargas per book.
> Unlike the Yuddhakāṇḍa comparison, there is no "Leonov-edited" third text here — no analogous
> source exists for these 4 books (Grintser/Serebryany translated them, not Leonov; see chat).
> **Uttarakāṇḍa (VII) is not included: valmikiramayan.net does not publish it at all.**

## ⚠️ Rights caveat

This comparison reproduces excerpts of valmikiramayan.net's copyrighted Devanāgarī text at scale
(the `*_only` and `variants` tables below). The only rights clearance on file in this project
(`CommentaryStrategies/data/valmiki_PERMISSION.md`) covers a *different* Gita Supersite editor's
grant for Vālmīki commentaries specifically for Sundarakāṇḍa — it does NOT cover valmikiramayan.net
or these 4 books. **Do not publish/commit this report or its JSON as-is without a rights check**
(`/publish-safety-check`) — treat as a private working document until cleared.

## Summary across all 4 books

| Kāṇḍa | Critical verses | Southern verses | Δ | Identical | Variant pairs | — near-id (≥.9) | — minor (.6–.9) | — major (<.6) | Critical-only | Southern-only |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bālakāṇḍa (I) | 1941 | 2164 | +223 | 102 | 1370 | 1124 | 193 | 53 | 469 | 692 |
| Ayodhyākāṇḍa (II) | 3160 | 4105 | +945 | 91 | 2389 | 2239 | 121 | 29 | 680 | 1625 |
| Araṇyakāṇḍa (III) | 2060 | 2312 | +252 | 24 | 1475 | 1247 | 191 | 37 | 561 | 813 |
| Kiṣkindhākāṇḍa (IV) | 1987 | 2312 | +325 | 34 | 1379 | 1196 | 162 | 21 | 574 | 899 |
| **Total (4 books)** | 9148 | 10893 | +1745 | 251 | 6613 | 5806 | 667 | 140 | 2284 | 4029 |

All 4 books show the southern recension running noticeably longer than the critical edition
(+12% to +30%), consistent with the known pattern already established for Sundarakāṇḍa (+15%,
`CommentaryStrategies/data/edition_comparison/README.md`) and Yuddhakāṇḍa.

## Bālakāṇḍa (I)

Critical 1941 verses vs Southern 2164 verses. 102 identical, 1370 aligned-but-different, 469 critical-only, 548 southern-only.

### Major differences (sim < 0.6) — 53 pairs, showing up to 60

| Critical locus | Southern locus | sim | Critical text | Southern text |
|---|---|---:|---|---|
| 1.51.5 | 1.52.10 | 0.386 | viśvāmitro mahātejā vanaspatigaṇe tathā sarvatra kuśalaṃ cāha vasiṣṭho rājasattamam | सर्वत्र कुशलं राजा वसिष्ठं प्रत्युदाहरत् \| विश्वामित्रो महातेजा वसिष्ठं विनयान्वितम् |
| 1.70.21 | 1.71.21 | 0.387 | sītāṃ rāmāya bhadraṃ te ūrmilāṃ lakṣmaṇāya ca vīryaśulkāṃ mama sutāṃ sītāṃ surasutopamām | वीर्यशुल्कां मम सुतां सीतां सुरसुतोपमाम्  द्वितीयामूर्मिलां चैव त्रिर्वदामि न संशयः \| ददामि परमप्रीतो वध्वौ ते मुनिपुंग |
| 1.48.17 | 1.49.18 | 0.395 | rāghavau tu tatas tasyāḥ pādau jagṛhatus tadā smarantī gautamavacaḥ pratijagrāha sā ca tau | स्मरन्ती गौतमवचः प्रतिजग्राह सा च तौ \|\| पाद्यमर्घ्यं तथातिथ्यं चकार सुसमाहिता \| प्रतिजग्राह काकुत्स्थो विधिदृष्टेन कर |
| 1.59.6 | 1.60.7 | 0.412 | agnikalpo hi bhagavāñ śāpaṃ dāsyati roṣitaḥ tasmāt pravartyatāṃ yajñaḥ saśarīro yathā divam | तस्मात् प्रवर्त्यतां यज्ञः सशरीरो यथा दिवम् \| गच्छेदिक्ष्वाकुदायादो विश्वामित्रस्य तेजसा  ततः प्रवर्त्यतां यज्ञः सर्वे  |
| 1.63.4 | 1.64.5 | 0.43 | tām uvāca sahasrākṣo vepamānāṃ kṛtāñjalim mā bhaiṣi rambhe bhadraṃ te kuruṣva mama śāsanam | मा भैषि रंभे भद्रं ते कुरुष्व मम शासनम्  कोकिलो हृदयग्राही माधवे रुचिरद्रुमे \| अहं कंदर्पसहितः स्थास्यामि तव पार्श्वतः |
| 1.72.17 | 1.73.26 | 0.456 | abravīj janako rājā kausalyānandavardhanam iyaṃ sītā mama sutā sahadharmacarī tava | इयं सीता मम सुता सहधर्मचरी तव  प्रतीच्छ चैनां भद्रं ते पाणिं गृह्णीष्व पाणिना \| |
| 1.73.8 | 1.74.7 | 0.458 | ṛṣīn sarvān puraskṛtya jagāma sabalānugaḥ gacchantaṃ tu naravyāghraṃ sarṣisaṃghaṃ sarāghavam | राजाप्ययोध्याधिपतिः सह पुत्रैर्महात्मभिः  ऋषीन् सर्वान् पुरस्कृत्य जगाम सबलानुगः \| |
| 1.3.14 | 1.3.22 | 0.463 | śarbaryā darśanaṃ caiva hanūmaddarśanaṃ tathā vilāpaṃ caiva pampāyāṃ rāghavasya mahātmanaḥ | शबरीदर्शनं चैव फलमूलाशनं तथा \| प्रलापं चैव पम्पायां हनुमद्दर्शनं तथा |
| 1.1.47 | 1.1.58 | 0.475 | śabaryā pūjitaḥ samyag rāmo daśarathātmajaḥ pampātīre hanumatā saṃgato vānareṇa ha | पम्पातीरे हनुमता सङ्गतो वानरेण ह  हनुमद्वचनाच्चैव सुग्रीवेण समागतः \| |
| 1.13.25 | 1.14.32 | 0.475 | ṛtvigbhiḥ sarvam evaitan niyuktaṃ śāstratas tadā paśūnāṃ triśataṃ tatra yūpeṣu niyataṃ tadā | पशूनां त्रिशतं तत्र यूपेषु नियतं तदा \| अश्वरत्नोत्तमं तस्य राज्ञो दशरथस्य च |
| 1.71.10 | 1.72.11 | 0.475 | sadṛśaṃ kulasaṃbandhaṃ yad ājñāpayathaḥ svayam evaṃ bhavatu bhadraṃ vaḥ kuśadhvajasute ime | एवं भवतु भद्रं वः कुशध्वजसुते इमे \| पत्न्यौ भजेतां सहितौ शत्रुघ्नभरतावुभौ |
| 1.55.13 | 1.56.13 | 0.476 | vasiṣṭhe japatāṃ śreṣṭhe tad adbhutam ivābhavat tāni sarvāṇi daṇḍena grasate brahmaṇaḥ sutaḥ | तानि सर्वाणि दण्डेन ग्रसते ब्रह्मणः सुतः  तेषु शांतेषु ब्रह्मास्त्रं क्षिप्तवान् गाधिनंदनः \| |
| 1.12.31 | 1.13.37 | 0.478 | mayāpi satkṛtāḥ sarve yathārhaṃ rājasattamāḥ yajñiyaṃ ca kṛtaṃ rājan puruṣaiḥ susamāhitaiḥ | यज्ञीयं च कृतं सर्वं पुरुषैः सुसमाहितैः \| निर्यातु च भवान्यष्टुं यज्ञायतनमन्तिकात् |
| 1.12.1 | 1.13.2 | 0.479 | punaḥ prāpte vasante tu pūrṇaḥ saṃvatsaro 'bhavat abhivādya vasiṣṭhaṃ ca nyāyataḥ pratipūjya ca | अभिवाद्य वसिष्ठं च न्यायतः प्रतिपूज्य च \| अब्रवीत्प्रश्रितं वाक्यं प्रसवार्थं द्विजोत्तमम् |
| 1.12.3 | 1.13.3 | 0.479 | yathā na vighnaḥ kriyate yajñāṅgeṣu vidhīyatām bhavān snigdhaḥ suhṛn mahyaṃ guruś ca paramo bhavān | यज्ञो मे क्रियतां ब्रह्मन् यथोक्तं मुनिपुङ्गव \| यथा न विघ्नः क्रियते यज्ञांगेषु विधीयताम् |
| 1.47.2 | 1.48.2 | 0.483 | imau kumārau bhadraṃ te devatulyaparākramau gajasiṃhagatī vīrau śārdūlavṛṣabhopamau | इमौ कुमारौ भद्रं ते देवतुल्यपराक्रमौ \| गजसिंहगती वीरौ शार्दूलवृषभोपमौ  पद्मपत्रविशालाक्षौ खड्गतूणीधनुर्धरौ \| अश्विनावि |
| 1.49.17 | 1.50.17 | 0.483 | imau kumārau bhadraṃ te devatulyaparākramau gajasiṃhagatī vīrau śārdūlavṛṣabhopamau | इमौ कुमारौ भद्रं ते देवतुल्यपराक्रमौ  गजसिंहगती वीरौ शार्दूलवृषभोपमौ \| पद्मपत्रविशालाक्षौ खड्गतूणीधनुर्धरौ \| अश्विनावि |
| 1.71.5 | 1.72.5 | 0.483 | bhrātā yavīyān dharmajña eṣa rājā kuśadhvajaḥ asya dharmātmano rājan rūpeṇāpratimaṃ bhuvi | अस्य धर्मात्मनो राजन् रूपेणाप्रतिमं भुवि \| सुताद्वयं नरश्रेष्ठ पत्न्यर्थं वरयामहे |
| 1.61.6 | 1.62.7 | 0.484 | svargalokam upāśnīyāṃ tapas taptvā hy anuttamam sa me nātho hy anāthasya bhava bhavyena cetasā | स मे नाथो ह्यनाथस्य भव भव्येन चेतसा \| पितेव पुत्रं धर्मात्मंस्त्रातुमर्हसि किल्बिषात् |
| 1.3.19 | 1.3.29 | 0.485 | parvatārohaṇaṃ caiva sāgarasya ca laṅghanam rātrau laṅkāpraveśaṃ ca ekasyāpi vicintanam | रात्रौ लङ्काप्रवेशं च एकस्याथ विचिन्तनम् \| आपानभूमिगमनमवरोधस्य दर्शनम् |
| 1.6.23 | 1.6.26 | 0.491 | nityamattaiḥ sadā pūrṇā nāgair acalasaṃnibhaiḥ sā yojane ca dve bhūyaḥ satyanāmā prakāśate | सा योजने च द्वे भूयः सत्यनामा प्रकाशते \| यस्यां दशरथो राजा वसन् जगदपालयत् |
| 1.13.40 | 1.14.48 | 0.492 | na bhūmyā kāryam asmākaṃ na hi śaktāḥ sma pālane ratāḥ svādhyāyakaraṇe vayaṃ nityaṃ hi bhūmipa | रताः स्वाध्यायकरणे वयं नित्यं हि भूमिप \| निष्क्रयं किंचिदेवेह प्रयच्छतु भवानिति |
| 1.57.9 | 1.58.9 | 0.492 | atha rātryāṃ vyatītāyāṃ rājā caṇḍālatāṃ gataḥ nīlavastradharo nīlaḥ paruṣo dhvastamūrdhajaḥ | इत्युक्त्वा ते महात्मानो विविशुः स्वं स्वमाश्रमम्  अथ रात्र्यां व्यतीतायां राजा चण्डालतां गतः \| |
| 1.48.13 | 1.49.13 | 0.493 | dadarśa ca mahābhāgāṃ tapasā dyotitaprabhām lokair api samāgamya durnirīkṣyāṃ surāsuraiḥ | ददर्श च महाभागां तपसा द्योतितप्रभाम् \| लोकैरपि समागम्य दुर्निरीक्ष्यां सुरासुरैः  प्रयत्नान्निर्मितां धात्रा दिव्यां मा |
| 1.8.9 | 1.9.6 | 0.495 | dvaividhyaṃ brahmacaryasya bhaviṣyati mahātmanaḥ lokeṣu prathitaṃ rājan vipraiś ca kathitaṃ sadā | लोकेषु प्रथितं राजन् विप्रैश्च कथितं सदा \| तस्यैवं वर्तमानस्य कालः समभिवर्तत |
| 1.27.11 | 1.28.11 | 0.499 | rāmaṃ prāñjalayo bhūtvābruvan madhurabhāṣiṇaḥ ime sma naraśārdūla śādhi kiṃ karavāma te | बाढमित्येव काकुत्स्थ प्रहृष्टेनान्तरात्मना \| दिव्यभास्वरदेहाश्च मूर्तिमन्तः सुखप्रदाः  केचिदङ्गारसदृशाः केचिद् धूमोपमास |
| 1.8.8 | 1.9.5 | 0.5 | sa vane nityasaṃvṛddho munir vanacaraḥ sadā nānyaṃ jānāti viprendro nityaṃ pitranuvartanāt | नान्यं जानाति विप्रेन्द्रो नित्यं पित्रनुवर्तनात् \| द्वैविध्यं ब्रहचर्यस्य भविष्यति महात्मनः |
| 1.12.4 | 1.13.4 | 0.5 | voḍhavyo bhavatā caiva bhāro yajñasya codyataḥ tatheti ca sa rājānam abravīd dvijasattamaḥ | भवान्स्निग्धः सुहृन्मह्यं गुरुश्च परमो महान् \| वोढव्यो भवता चैव भारो यज्ञस्य चोद्यतः |
| 1.26.7 | 1.27.7 | 0.5 | dadāmi te mahābāho brāhmam astram anuttamam gade dve caiva kākutstha modakī śikharī ubhe | गदे द्वे चैव काकुत्स्थ मोदकी शिखरी शुभे  प्रदीप्ते नरशार्दूल प्रयच्छामि नृपात्मज \| |
| 1.15.25 | 1.16.27 | 0.501 | kausalyāyai narapatiḥ pāyasārdhaṃ dadau tadā ardhād ardhaṃ dadau cāpi sumitrāyai narādhipaḥ | कौसल्यायै नरपतिः पायसार्धं ददौ तदा \| अर्धादर्धं ददौ चापि सुमित्रायै नराधिपः  कैकेय्यै चावशिष्टार्धं ददौ पुत्रार्थकारणात |
| 1.17.17 | 1.18.30 | 0.503 | lakṣmaṇo lakṣmisaṃpanno bahiḥprāṇa ivāparaḥ na ca tena vinā nidrāṃ labhate puruṣottamaḥ | न च तेन विना निद्रां लभते पुरुषोत्तमः  मृष्टमन्नमुपानीतमश्नाति न हि तं विना \| |
| 1.19.21 | 1.20.22 | 0.503 | na śaktā rāvaṇaṃ soḍhuṃ kiṃ punar mānavā yudhi sa hi vīryavatāṃ vīryam ādatte yudhi rākṣasaḥ | देवदानवगंधर्वा यक्षाः पतगपन्नगाः\| न शक्ता रावणं सोढुं किं पुनर्मानवा युधि |
| 1.26.17 | 1.27.18 | 0.503 | tāmasaṃ naraśārdūla saumanaṃ ca mahābalam saṃvartaṃ caiva durdharṣaṃ mausalaṃ ca nṛpātmaja | तामसं नरशार्दूल सौमनं च महाबलम् \| संवर्तं चैव दुर्धर्षं मौसलं च नृपात्मज  सत्यमस्त्रं महाबाहो तथा मायामयं परम् \| सौरं  |
| 1.62.24 | 1.63.25 | 0.503 | evaṃ varṣasahasraṃ hi tapo ghoram upāgamat tasmin saṃtapyamāne tu viśvāmitre mahāmunau | तस्मिन् संतप्यमाने तु विश्वामित्रे महामुनौ \| संतापः सुमहानासीत् सुराणां वासवस्य च |
| 1.73.5 | 1.74.5 | 0.503 | dadau kanyā pitā tāsāṃ dāsīdāsam anuttamam hiraṇyasya suvarṇasya muktānāṃ vidrumasya ca | हिरण्यस्य सुवर्णस्य मुक्तानां विद्रुमस्य च  ददौ राजा सुसंहृष्टः कन्याधनमनुत्तमम् \| |
| 1.64.7 | 1.65.13 | 0.505 | sāgarāḥ kṣubhitāḥ sarve viśīryante ca parvatāḥ prakampate ca pṛthivī vāyur vāti bhṛśākulaḥ | व्याकुलाश्च दिशः सर्वा न च किंचित् प्रकाशते  सागराः क्षुभिताः सर्वे विशीर्यन्ते च पर्वताः \| |
| 1.6.15 | 1.6.15 | 0.506 | na dīnaḥ kṣiptacitto vā vyathito vāpi kaś cana kaś cin naro vā nārī vā nāśrīmān nāpy arūpavān | नाषडङ्गविदत्रासीन्नाव्रतो नासहस्रदः \| न दीनः क्षिप्तचित्तो वा व्यथितो वापि कश्चन |
| 1.5.2 | 1.5.1 | 0.507 | yeṣāṃ sa sagaro nāma sāgaro yena khānitaḥ ṣaṣṭiḥ putrasahasrāṇi yaṃ yāntaṃ paryavārayan | सर्वा पूर्वमियं येषामासीत्कृत्स्ना वसुंधरा \| प्रजापतिमुपादाय नृपाणां जयशालिनाम्  येषां स सगरो नाम सागरो येन खानितः \| ष |
| 1.14.16 | 1.15.18 | 0.508 | etasminn antare viṣṇur upayāto mahādyutiḥ brahmaṇā ca samāgamya tatra tasthau samāhitaḥ | ब्रह्मणा च समागम्य तत्र तस्थौ समाहितः \| तमब्रुवन् सुराः सर्वे समभिष्टूय संनताः |
| 1.26.11 | 1.27.11 | 0.511 | vāyavyaṃ prathamaṃ nāma dadāmi tava rāghava astraṃ hayaśiro nāma krauñcam astraṃ tathaiva ca | अस्त्रं हयशिरो नाम क्रौञ्चमस्त्रं तथैव च  शक्तिद्वयं च काकुत्स्थ ददामि तव राघव \| |
| 1.32.9 | 1.33.8 | 0.513 | kṣamā yaśaḥ kṣamā dharmaḥ kṣamāyāṃ viṣṭhitaṃ jagat visṛjya kanyāḥ kākutstha rājā tridaśavikramaḥ | क्षमा दानं क्षमा सत्यं क्षमा यज्ञश्च पुत्रिकाः  क्षमा यशः क्षमा धर्मः क्षमायां विष्ठितं जगत् \| |
| 1.26.5 | 1.56.10 | 0.516 | dharmacakraṃ tato vīra kālacakraṃ tathaiva ca viṣṇucakraṃ tathātyugram aindraṃ cakraṃ tathaiva ca | धर्मचक्रं कालचक्रं विष्णुचक्रं तथैव च \| वायव्यं मथनं चैव अस्त्रं हयशिरस्तथा |
| 1.6.16 | 1.6.18 | 0.518 | varṇeṣv agryacaturtheṣu devatātithipūjakāḥ dīrghāyuṣo narāḥ sarve dharmaṃ satyaṃ ca saṃśritāḥ | दीर्घायुषो नराः सर्वे धर्मं सत्यं च संश्रिताः \| सहिताः पुत्रपौत्रैश्च नित्यं स्त्रीभिः पुरोत्तमे |
| 1.64.25 | 1.65.34 | 0.522 | sadasyaiḥ prāpya ca sadaḥ śrutās te bahavo guṇāḥ | सदस्यैः प्राप्य च सदः श्रुतास्ते बहवो गुणाः  अप्रमेया तपस्तुभ्यमप्रमेयं च ते बलम् \| अप्रमेया गुणाश्चैव नित्यं ते कुशिका |
| 1.56.13 | 1.57.13 | 0.53 | pratyākhyāto vasiṣṭhena sa yayau dakṣiṇāṃ diśam vasiṣṭhā dīrgha tapasas tapo yatra hi tepire | अशक्यमिति चाप्युक्तो वसिष्ठेन महात्मना \| प्रत्याख्यातो वसिष्ठेन स ययौ दक्षिणां दिशम्  ततस्तत्कर्मसिद्ध्यर्थं पुत्रांस्त |
| 1.17.15 | 1.18.28 | 0.532 | teṣām api mahātejā rāmaḥ satyaparākramaḥ bālyāt prabhṛti susnigdho lakṣmaṇo lakṣmivardhanaḥ | बाल्यात् प्रभृति सुस्निग्धो लक्ष्मणो लक्ष्मिवर्धनः  रामस्य लोकरामस्य भ्रातुर्ज्येष्ठस्य नित्यशः \| |
| 1.26.13 | 1.27.13 | 0.534 | dhārayanty asurā yāni dadāmy etāni sarvaśaḥ vaidyādharaṃ mahāstraṃ ca nandanaṃ nāma nāmataḥ | वैद्याधरं महास्त्रं च नन्दनं नाम नामतः  असिरत्नं महाबाहो ददामि नृवरात्मज \| |
| 1.73.3 | 1.74.3 | 0.551 | atha rājā videhānāṃ dadau kanyādhanaṃ bahu gavāṃ śatasahasrāṇi bahūni mithileśvaraḥ | अथ राजा विदेहानां ददौ कन्याधनं बहु \| गवां शतसहस्राणि बहूनि मिथिलेश्वरः  कंबलानां च मुख्यानां क्षौमान् कोट्यंबराणि च \|  |
| 1.56.2 | 1.57.1 | 0.576 | sa dakṣiṇāṃ diśaṃ gatvā mahiṣyā saha rāghava tatāpa paramaṃ ghoraṃ viśvāmitro mahātapāḥ | ततः संतप्तहृदयः स्मरन्निग्रहमात्मनः \| विनिःश्वस्य विनिःश्वस्य कृतवैरो महात्मना  सदक्षिणां दिशं गत्वा महिष्या सह राघव \| |
| 1.74.25 | 1.75.24 | 0.579 | pṛthivīṃ cākhilāṃ prāpya kāśyapāya mahātmane yajñasyānte tadā rāma dakṣiṇāṃ puṇyakarmaṇe | वधमप्रतिरूपं तु पितुः श्रुत्वा सुदारुणम् \| क्षत्रमुत्सादयन् रोषाज्जातं जातमनेकशः  पृथिवीं चाखिलां प्राप्य काश्यपाय महात |
| 1.26.16 | 1.27.15 | 0.581 | madanaṃ caiva durdharṣaṃ kandarpadayitaṃ tathā paiśācam astraṃ dayitaṃ mohanaṃ nāma nāmataḥ | वर्षणं शोषणं चैव संतापनविलापने  मादनं चैव दुर्धर्षं कन्दर्पदयितं तथा \| गान्धर्वमस्त्रं दयितं मानवं नाम नामतः  पैशाचमस्त |
| 1.34.8 | 1.35.9 | 0.589 | tataḥ snātvā yathānyāyaṃ saṃtarpya pitṛdevatāḥ hutvā caivāgnihotrāṇi prāśya cāmṛtavad dhaviḥ | तस्यास्तीरे तदा सर्वे चक्रुर्वासपरिग्रहम् \| ततः स्नात्वा यथान्यायं संतर्प्य पितृदेवताः  हुत्वा चैवाग्निहोत्राणि प्राश्य |
| 1.51.17 | 1.52.16 | 0.591 | sarvathā ca mahāprājña pūjārheṇa supūjitaḥ gamiṣyāmi namas te 'stu maitreṇekṣasva cakṣuṣā | फलमूलेन भगवन्विद्यते यत्तवाश्रमे \| पाद्येनाचमनीयेन भगवद्दर्शनेन च  सर्वथा च महाप्राज्ञ पूजार्हेण सुपूजितः \| नमस्तेऽस्त |

### Minor edits (sim 0.6–0.9) — 193 pairs, sample of 40

| Critical locus | Southern locus | sim | Critical text | Southern text |
|---|---|---:|---|---|
| 1.62.26 | 1.63.26 | 0.62 | uvācātmahitaṃ vākyam ahitaṃ kauśikasya ca | रंभामप्सरसं शक्रः सह सर्वैर्मरुद्गणैः \| उवाचात्महितं वाक्यमहितं कौशिकस्य च |
| 1.52.3 | 1.53.3 | 0.624 | uṣṇāḍhyasyaudanasyāpi rāśayaḥ parvatopamāḥ mṛṣṭānnāni ca sūpāś ca dadhikulyās tathaiva ca | उष्णाढ्यस्यौदनस्यापि राशयः पर्वतोपमाः \| मृष्टान्नानि च सूपाश्च दधिकुल्यास्तथैव च  नानास्वादुरसानां च खाण्डवानां [षाडवान |
| 1.69.6 | 1.70.8 | 0.626 | ājñayā tu narendrasya ājagāma kuśadhvajaḥ | तद्वृत्तं नृपतिः श्रुत्वा दूतश्रेष्ठैर्महाजवैः \| आज्ञया तु नरेन्द्रस्य आजगाम कुशध्वजः |
| 1.1.69 | 1.1.86 | 0.627 | devatābhyo varān prāpya samutthāpya ca vānarān puṣpakaṃ tat samāruhya nandigrāmaṃ yayau tadā | देवताभ्यो वरं प्राप्य समुत्थाप्य च वानरान् \| अयोध्यां प्रस्थितो रामः पुष्पकेण सुहृद् वृतः |
| 1.15.12 | 1.16.14 | 0.632 | divākarasamākāraṃ dīptānalaśikhopamam taptajāmbūnadamayīṃ rājatāntaparicchadām | दिवाकरसमाकारं दीप्तानलशिखोपमम् \| तप्तजाम्बूनदमयीं राजतान्तपरिच्छदाम्  दिव्यपायससंपूर्णां पात्रीं पत्नीमिव प्रियाम् \| प |
| 1.49.3 | 1.50.3 | 0.634 | bahūnīha sahasrāṇi nānādeśanivāsinām brāhmaṇānāṃ mahābhāga vedādhyayanaśālinām | बहूनीह सहस्राणि नानादेशनिवासिनाम् \| ब्राह्मणानां महाभाग वेदाध्ययनशालिनाम्  ऋषि ऋषिवाटाश्च दृश्यन्ते शकटीशतसंकुलाः \| दे |
| 1.27.15 | 1.28.17 | 0.636 | kiṃ nv etan meghasaṃkāśaṃ parvatasyāvidūrataḥ vṛkṣaṣaṇḍam ito bhāti paraṃ kautūhalaṃ hi me | किं न्वेतन्मेघसंकाशं पर्वतस्याविदूरतः \| वृक्षखण्डमिवाभाति परं कौतूहलं हि मे  दर्शनीयं मृगाकीर्णं मनोहरमतीव च \| नानाप्र |
| 1.30.15 | 1.31.16 | 0.637 | pradakṣiṇaṃ tataḥ kṛtvā siddhāśramam anuttamam uttarāṃ diśam uddiśya prasthātum upacakrame | इति उक्त्वा मुनिशार्दूलः कौशिकः स तपोधनः \| उत्तराम् दिशम् उद्दिश्य प्रस्थातुम् उपचक्रमे |
| 1.75.9 | 1.76.9 | 0.642 | varāyudhadharaṃ rāma draṣṭuṃ sarṣigaṇāḥ surāḥ pitāmahaṃ puraskṛtya sametās tatra saṃghaśaḥ | वरायुधधरं रामं द्रष्टुं सर्षिगणाः सुराः \| पितामहं पुरस्कृत्य समेतास्तत्र सर्वशः  गंधर्वाप्सरसश्चैव सिद्धचारणकिन्नराः \| |
| 1.10.8 | 1.11.8 | 0.643 | taṃ ca rājā daśaratho yaṣṭukāmaḥ kṛtāñjaliḥ ṛṣyaśṛṅgaṃ dvijaśreṣṭhaṃ varayiṣyati dharmavit | तं च राजा दशरथो यष्टुकामः कृतांजलिः \| ऋष्यशृङ्गं द्विजश्रेष्ठं वरयिष्यति धर्मवित्  यज्ञार्थं प्रसवार्थं च स्वर्गार्थं च |
| 1.39.7 | 1.40.8 | 0.643 | parikrāntā mahī sarvā sattvavantaś ca sūditāḥ devadānavarakṣāṃsi piśācoragakiṃnarāḥ | परिक्रांता मही सर्वा सत्त्ववन्तश्च सूदिताः \| देवदानवरक्षांसि पिशाचोरगपन्नगाः  न च पश्यामहेऽश्वं तमश्वहर्तारमेव च \| किं |
| 1.1.25 | 1.1.28 | 0.645 | paurair anugato dūraṃ pitrā daśarathena ca śṛṅgaverapure sūtaṃ gaṅgākūle vyasarjayat | पौरैरनुगतो दूरं पित्रा दशरथेन च  शृङ्गिबेरपुरे सूतं गङ्गाकूले व्यसर्जयत् \| गुहमासाद्य धर्मात्मा निषादाधिपतिं प्रियम्  ग |
| 1.53.23 | 1.54.23 | 0.645 | tato 'strāṇi mahātejā viśvāmitro mumoca ha | ततोऽस्त्राणि महातेजा विश्वामित्रो मुमोच ह \| तैस्तैर्यवनकांभोजा बर्बराश्चाकुलीकृताः |
| 1.43.10 | 1.44.10 | 0.648 | rājarṣiṇā guṇavatā maharṣisamatejasā mattulyatapasā caiva kṣatradharmasthitena ca | राजर्षिणा गुणवता महर्षिसमतेजसा \| मत्तुल्यतपसा चैव क्षत्रधर्मे स्थितेन च  दिलीपेन महाभाग तव पित्रातितेजसा \| पुनर्न शङ्क |
| 1.60.10 | 1.61.10 | 0.648 | deśāñ janapadāṃs tāṃs tān nagarāṇi vanāni ca āśramāṇi ca puṇyāni mārgamāṇo mahīpatiḥ | देशान् जनपदांस्तांस्तान्नगराणि वनानि च \| आश्रमाणि च पुण्यानि मार्गमाणो महीपतिः  स पुत्रसहितं तात सभार्यं रघुनंदन \| भृग |
| 1.54.2 | 1.55.2 | 0.649 | tasyā humbhāravāj jātāḥ kāmbojā ravisaṃnibhāḥ ūdhasas tv atha saṃjātāḥ pahlavāḥ śastrapāṇayaḥ | तस्या हुंकारतो जाताः कांबोजा रविसन्निभाः \| ऊधसस्त्वथ संजाताः पह्लवाः शस्त्रपाणयः  योनिदेशाच्च यवनाः शकृदेशाच्छकास्तथा \ |
| 1.1.26 | 1.1.30 | 0.651 | te vanena vanaṃ gatvā nadīs tīrtvā bahūdakāḥ citrakūṭam anuprāpya bharadvājasya śāsanāt | ते वनेन वनं गत्वा नदीस्तीर्त्वा बहूदकाः  चित्रकूटमनुप्राप्य भरद्वाजस्य शासनात् \| रम्यमावसथं कृत्वा रममाणा वने त्रयः  दे |
| 1.39.24 | 1.40.25 | 0.651 | dadṛśuḥ kapilaṃ tatra vāsudevaṃ sanātanam hayaṃ ca tasya devasya carantam avidūrataḥ | ते तु सर्वे महत्मानो भीमवेगा महबलाः \| ददृशुः कपिलं तत्र वासुदेवं सनातनम्  हयं च तस्य देवस्य चरन्तमविदूरतः \| प्रहर्षमतु |
| 1.54.5 | 1.55.5 | 0.652 | dṛṣṭvā niṣūditaṃ sainyaṃ vasiṣṭhena mahātmanā viśvāmitrasutānāṃ tu śataṃ nānāvidhāyudham | दृष्ट्वा निषूदितं सैन्यं वसिष्ठेन महात्मना \| विश्वामित्रसुतानां तु शतं नानाविधायुधम्  अभ्यधावत् सुसंक्रद्धं वसिष्ठं जपत |
| 1.71.4 | 1.72.4 | 0.652 | vaktavyaṃ na naraśreṣṭha śrūyatāṃ vacanaṃ mama | वक्तव्यं च नरश्रेष्ठ श्रूयतां वचनं मम \| भ्राता यवीयान् धर्मज्ञ एष राजा कुशध्वजः |
| 1.60.21 | 1.61.22 | 0.653 | gavāṃ śatasahasreṇa śunaḥśepaṃ nareśvaraḥ gṛhītvā paramaprīto jagāma raghunandana | अथ राजा महाबाहो वाक्यान्ते ब्रह्मवादिनः \| हिरण्यस्य सुवर्णस्य कोटिभी रत्नराशिभिः  गवां शतसहस्रेण शुनःशेपं नरेश्वरः \| ग |
| 1.1.67 | 1.1.83 | 0.654 | karmaṇā tena mahatā trailokyaṃ sacarācaram sadevarṣigaṇaṃ tuṣṭaṃ rāghavasya mahātmanaḥ | ततोऽग्निवचनात्सीतां ज्ञात्वा विगतकल्मषाम् \| कर्मणा तेन महता त्रैलोक्यं सचराचरम्  सदेवर्षिगणं तुष्टं राघवस्य महात्मनः \| |
| 1.51.4 | 1.52.4 | 0.654 | pratigṛhya ca tāṃ pūjāṃ vasiṣṭhād rājasattamaḥ tapo'gnihotraśiṣyeṣu kuśalaṃ paryapṛcchata | प्रतिगृह्य तु तां पूजां वसिष्ठाद्राजसत्तमः \| तपोऽग्निहोत्रशिष्येषु कुशलं पर्यपृच्छत  विश्वामित्रो महातेजा वनस्पतिगणे तथ |
| 1.55.20 | 1.56.20 | 0.654 | tato 'stuvan munigaṇā vasiṣṭhaṃ japatāṃ varam amoghaṃ te balaṃ brahmaṃs tejo dhāraya tejasā | ततोऽस्तुवन् मुनिगणा वसिष्ठं जपतां वरम् \| अमोघं ते बलं ब्रह्मंस्तेजो धारय तेजसा  निगृहीतस्त्वया ब्रह्मन् विश्वामित्रो मह |
| 1.47.23 | 1.48.23 | 0.656 | gautamaṃ sa dadarśātha praviśanti mahāmunim devadānavadurdharṣaṃ tapobalasamanvitam | गौतमं स ददर्शाथ प्रविशन्तं महामुनिम्  देवदानवदुर्धर्षं तपोबलसमन्वितम् \| तीर्थोदकपरिक्लिन्नं दीप्यमानमिवानलम्  गृहीतसमिध |
| 1.49.20 | 1.50.20 | 0.657 | varāyudhadharau vīrau kasya putrau mahāmune bhūṣayantāv imaṃ deśaṃ candrasūryāv ivāmbaram | वरायुधधरौ वीरौ कस्य पुत्रौ महामुने \| भूषयन्ताविमं देशं चन्द्रसूर्याविवाम्बरम्  परस्परस्य सदृशौ प्रमाणेङ्गितचेष्टितैः \| |
| 1.11.6 | 1.12.4 | 0.659 | suyajñaṃ vāmadevaṃ ca jābālim atha kāśyapam purohitaṃ vasiṣṭhaṃ ca ye cānye dvijasattamāḥ | ततो नृपोऽब्रवीद्वाक्यं सुमन्त्रं मन्त्रिसत्तमम्  सुमंत्रावाहय क्षिप्रमृत्विजो ब्रह्मवादिनः \| सुयज्ञं वामदेवं च जाबालिमथ |
| 1.46.9 | 1.47.8 | 0.659 | evaṃ tau niścayaṃ kṛtvā mātāputrau tapovane jagmatus tridivaṃ rāma kṛtārthāv iti naḥ śrutam | सर्वमेतद्यथोक्तं ते भविष्यति न संशयः  विचरिष्यन्ति भद्रं ते देवरूपास्तवात्मजाः \| एवं तौ निश्चयं कृत्वा मातापुत्रौ तपोवन |
| 1.59.20 | 1.60.20 | 0.659 | ṛṣimadhye sa tejasvī prajāpatir ivāparaḥ sṛjan dakṣiṇamārgasthān saptarṣīn aparān punaḥ | ऋषिमध्ये स तेजस्वी प्रजापतिरिवापरः  सृजन् दक्षिणमार्गस्थान् सप्तर्षीनपरान् पुनः \| नक्षत्रमालामपरामसृजत् क्रोधमूर्च्छितः |
| 1.69.31 | 1.70.44 | 0.659 | ādivaṃśaviśuddhānāṃ rājñāṃ paramadharmiṇām ikṣvākukulajātānāṃ vīrāṇāṃ satyavādinām | आदिवंशविशुद्धानां राज्ञां परमधर्मिणाम् \| इक्ष्वाकुकुलजातानां वीराणां सत्यवादिनाम्  रामलक्ष्मणयोरर्थे त्वत्सुते वरये नृप |
| 1.35.10 | 1.36.10 | 0.661 | na lokā dhārayiṣyanti tava tejaḥ surottama brāhmeṇa tapasā yukto devyā saha tapaś cara | न लोका धारयिष्यन्ति तव तेजः सुरोत्तम \| ब्राह्मेण तपसा युक्तो देव्या सह तपश्चर  त्रैलोक्यहितकामार्थं तेजस्तेजसि धारय \|  |
| 1.8.3 | 1.8.3 | 0.662 | sa niścitāṃ matiṃ kṛtvā yaṣṭavyam iti buddhimān mantribhiḥ saha dharmātmā sarvair eva kṛtātmabhiḥ | स निश्चितां मतिं कृत्वा यष्टव्यमिति बुद्धिमान् \| मंत्रिभिः सह धर्मात्मा सर्वैरपि कृतात्मभिः  ततोऽब्रवीदिदं राजा सुमन्त् |
| 1.22.11 | 1.23.10 | 0.662 | tapasyantam iha sthāṇuṃ niyamena samāhitam kṛtodvāhaṃ tu deveśaṃ gacchantaṃ samarudgaṇam | कन्दर्पो मूर्तिमानासीत् काम इत्युच्यते बुधैः \| तपस्यन्तमिह स्थाणुं नियमेन समाहितम्  कृतोद्वाहं तु देवेशं गच्छन्तं समरुद |
| 1.2.32 | 1.2.33 | 0.664 | rahasyaṃ ca prakāśaṃ ca yad vṛttaṃ tasya dhīmataḥ rāmasya saha saumitre rākṣasānāṃ ca sarvaśaḥ | रहस्यं च प्रकाशं च यद् वृत्तं तस्य धीमतः \| रामस्य सहसौमित्रे राक्षसानां च सर्वशः  वैदेह्याश्चापि यद् वृत्तं प्रकाशं यदि |
| 1.9.29 | 1.10.30 | 0.664 | varṣeṇaivāgataṃ vipraṃ viṣayaṃ svaṃ narādhipaḥ pratyudgamya muniṃ prahvaḥ śirasā ca mahīṃ gataḥ | वर्षेणैवागतं विप्रं विषयं स्वं नराधिपः \| प्रत्युद्गम्य मुनिं प्रह्वः शिरसा च महीं गतः  अर्घ्यं च प्रददौ तस्मै न्यायतः स |
| 1.21.19 | 1.22.21 | 0.664 | gurukāryāṇi sarvāṇi niyujya kuśikātmaje ūṣus tāṃ rajanīṃ tatra sarayvāṃ susukhaṃ trayaḥ | विद्यासमुदितो रामः शुशुभे भूरिविक्रमः  सहस्ररश्मिर्भगवान् शरदीव दिवाकरः \| गुरुकार्याणि सर्वाणि नियुज्य कुशिकात्मजे \| ऊ |
| 1.42.22 | 1.43.31 | 0.664 | devāḥ sarṣigaṇāḥ sarve daityadānavarākṣasāḥ gandharvayakṣapravarāḥ sakiṃnaramahoragāḥ | देवाः सर्षिगणाः सर्वे दैत्यदानवराक्षसाः  गन्धर्वयक्षप्रवराः सकिंनरमहोरगाः \| सर्पाश्चाप्सरसो राम भगीरथरथानुगाः  गंगामन्व |
| 1.21.2 | 1.22.2 | 0.667 | kṛtasvastyayanaṃ mātrā pitrā daśarathena ca purodhasā vasiṣṭhena maṅgalair abhimantritam | कृतस्वस्त्ययनं मात्रा पित्रा दशरथेन च \| पुरोधसा वसिष्ठेन मङ्गलैरभिमंत्रितम्  सपुत्रं मूर्ध्न्युपाघ्राय राजा दशरथस्तदा \ |
| 1.23.8 | 1.24.9 | 0.667 | tasmāt susrāva sarasaḥ sāyodhyām upagūhate saraḥpravṛttā sarayūḥ puṇyā brahmasaraścyutā | तस्मात् सुस्राव सरसः सायोध्यामुपगूहते  सरः प्रवृत्ता सरयूः पुण्या ब्रह्मसरश्च्युता \| तस्यायमतुलः शब्दो जाह्नवीमभिवर्तते |
| 1.39.16 | 1.40.17 | 0.667 | tataḥ pūrvāṃ diśaṃ bhittvā dakṣiṇāṃ bibhiduḥ punaḥ dakṣiṇasyām api diśi dadṛśus te mahāgajam | ततः पूर्वां दिशं भित्त्वा दक्षिणां बिभिदुः पुनः \| दक्षिणस्यामपि दिशि ददृशुस्ते महागजम्  महापद्मं महात्मानं सुमहत्पर्वतो |

### Critical-only verses — 469, sample of 30 (present in Baroda critical, absent from Southern)

| Locus | Text |
|---|---|
| 1.1.6 | śrutvā caitat trilokajño vālmīker nārado vacaḥ śrūyatām iti cāmantrya prahṛṣṭo vākyam abravīt |
| 1.1.18 | dhanadena samas tyāge satye dharma ivāparaḥ tam evaṃguṇasaṃpannaṃ rāmaṃ satyaparākramam |
| 1.1.19 | jyeṣṭhaṃ śreṣṭhaguṇair yuktaṃ priyaṃ daśarathaḥ sutam yauvarājyena saṃyoktum aicchat prītyā mahīpatiḥ |
| 1.1.24 | sarvalakṣaṇasaṃpannā nārīṇām uttamā vadhūḥ sītāpy anugatā rāmaṃ śaśinaṃ rohiṇī yathā |
| 1.1.27 | ramyam āvasathaṃ kṛtvā ramamāṇā vane trayaḥ devagandharvasaṃkāśās tatra te nyavasan sukham |
| 1.1.31 | sa kāmam anavāpyaiva rāmapādāv upaspṛśan nandigrāme 'karod rājyaṃ rāmāgamanakāṅkṣayā |
| 1.1.32 | rāmas tu punar ālakṣya nāgarasya janasya ca tatrāgamanam ekāgre daṇḍakān praviveśa ha |
| 1.1.38 | nijaghāna raṇe rāmas teṣāṃ caiva padānugān rakṣasāṃ nihatāny āsan sahasrāṇi caturdaśa |
| 1.1.45 | kabandhaṃ nāma rūpeṇa vikṛtaṃ ghoradarśanam taṃ nihatya mahābāhur dadāha svargataś ca saḥ |
| 1.1.48 | hanumadvacanāc caiva sugrīveṇa samāgataḥ sugrīvāya ca tat sarvaṃ śaṃsad rāmo mahābalaḥ |
| 1.1.51 | rāghavaḥ pratyayārthaṃ tu dundubheḥ kāyam uttamam pādāṅguṣṭhena cikṣepa saṃpūrṇaṃ daśayojanam |
| 1.1.55 | tataḥ sugrīvavacanād dhatvā vālinam āhave sugrīvam eva tad rājye rāghavaḥ pratyapādayat |
| 1.1.61 | astreṇonmuham ātmānaṃ jñātvā paitāmahād varāt marṣayan rākṣasān vīro yantriṇas tān yadṛcchayā |
| 1.1.62 | tato dagdhvā purīṃ laṅkām ṛte sītāṃ ca maithilīm rāmāya priyam ākhyātuṃ punar āyān mahākapiḥ |
| 1.1.66 | tena gatvā purīṃ laṅkāṃ hatvā rāvaṇam āhave abhyaṣiñcat sa laṅkāyāṃ rākṣasendraṃ vibhīṣaṇam |
| 1.1.68 | tathā paramasaṃtuṣṭaiḥ pūjitaḥ sarvadaivataiḥ kṛtakṛtyas tadā rāmo vijvaraḥ pramumoda ha |
| 1.1.73 | na vātajaṃ bhayaṃ kiṃ cin nāpsu majjanti jantavaḥ na cāgrijaṃ bhayaṃ kiṃ cid yathā kṛtayuge tathā |
| 1.1.79 | paṭhan dvijo vāgṛṣabhatvam īyāt; syāt kṣatriyo bhūmipatitvam īyāt vaṇigjanaḥ paṇyaphalatvam īyāj; janaś ca śūdro 'pi mahattvam īyāt |
| 1.2.2 | yathāvat pūjitas tena devarṣir nāradas tadā āpṛṣṭvaivābhyanujñātaḥ sa jagāma vihāyasaṃ |
| 1.2.3 | sa muhūtaṃ gate tasmin devalokaṃ munis tadā jagāma tamasātīraṃ jāhnavyās tv avidūrataḥ |
| 1.2.13 | tataḥ karuṇaveditvād adharmo 'yam iti dvijaḥ niśāmya rudatīṃ krauñcīm idaṃ vacanam abravīt |
| 1.2.16 | cintayan sa mahāprājñaś cakāra matimān matim śiṣyaṃ caivābravīd vākyam idaṃ sa munipuṃgavaḥ |
| 1.2.18 | śiṣyas tu tasya bruvato muner vākyam anuttamam pratijagrāha saṃhṛṣṭas tasya tuṣṭo 'bhavad guruḥ |
| 1.2.26 | upaviṣṭe tadā tasmin sākṣāl lokapitāmahe tad gatenaiva manasā vālmīkir dhyānam āsthitaḥ |
| 1.2.28 | śocann eva muhuḥ krauñcīm upaślokam imaṃ punaḥ jagāv antargatamanā bhūtvā śokaparāyaṇaḥ |
| 1.2.33 | vaidehyāś caiva yad vṛttaṃ prakāśaṃ yadi vā rahaḥ tac cāpy aviditaṃ sarvaṃ viditaṃ te bhaviṣyati |
| 1.2.39 | samākṣaraiś caturbhir yaḥ pādair gīto maharṣiṇā so 'nuvyāharaṇād bhūyaḥ śokaḥ ślokatvam āgataḥ |
| 1.2.40 | tasya buddhir iyaṃ jātā vālmīker bhāvitātmanaḥ kṛtsnaṃ rāmāyaṇaṃ kāvyam īdṛśaiḥ karavāṇy aham |
| 1.3.4 | nānācitrāḥ kathāś cānyā viśvāmitrasahāyane jānakyāś ca vivāhaṃ ca dhanuṣaś ca vibhedanam |
| 1.3.8 | gaṅgāyāś cābhisaṃtāraṃ bharadvājasya darśanam bharadvājābhyanujñānāc citrakūṭasya darśanam |

### Southern-only verses — 548, sample of 30 (in the vulgate, absent from critical)

| Locus | Text (Devanāgarī) |
|---|---|
| 1.1.6 | श्रुत्वा चैतत्त्रिलोकज्ञो वाल्मीकेर्नारदो वचः \| श्रूयतामिति चामन्त्र्य प्रहृष्टो वाक्यमब्रवीत् |
| 1.1.13 | प्रजापतिसमः श्रीमान् धाता रिपुनिषूदनः \| रक्षिता जीवलोकस्य धर्मस्य परिरक्षिता |
| 1.1.19 | तमेवं गुणसम्पन्नं रामं सत्यपराक्रमम्  ज्येष्ठं श्रेष्ठगुणैर्युक्तं प्रियं दशरथस्सुतम् \| प्रकृतीनां हितैर्युक्तं प्रकृतिप्रियकाम्यया  यौवराज्येन संयोक् |
| 1.1.26 | रामस्य दयिता भार्या नित्यं प्राणसमा हिता  जनकस्य कुले जाता देवमायेव निर्मिता \| सर्वलक्षणसम्पन्ना नारीणामुत्तमा वधूः  सीताप्यनुगता रामं शशिनं रोहिणी यथ |
| 1.1.35 | गत्वा तु स महात्मानं रामं सत्यपराक्रमम् \| अयाचद्भ्रातरं राममार्यभावपुरस्कृतः  त्वमेव राजा धर्मज्ञ इति रामं वचोऽब्रवीत् \| |
| 1.1.36 | रामोऽपि परमोदारः सुमुखः सुमहायशाः  न चैच्छत्पितुरादेशाद्राज्यं रामो महाबलः \| |
| 1.1.38 | स काममनवाप्यैव रामपादावुपस्पृशन्  नन्दिग्रामेऽकरोद्राज्यं रामागमनकाङ्क्षया \| |
| 1.1.39 | गते तु भरते श्रीमान् सत्यसन्धो जितेन्द्रियः  रामस्तु पुनरालक्ष्य नागरस्य जनस्य च \| तत्रागमनमेकाग्रो दण्डकान्प्रविवेश ह \|१-१-४० |
| 1.1.44 | स तेषां प्रतिशुश्राव राक्षसानां तथा वने  प्रतिज्ञातश्च रामेण वधः संयति रक्षसाम् \| ऋषीणामग्निकल्पानां दण्डकारण्यवासिनाम् |
| 1.1.48 | वने तस्मिन्निवसता जनस्थाननिवासिनाम्  रक्षसां निहतान्यासन् सहस्राणि चतुर्दश \| |
| 1.1.57 | सोऽभ्यगच्छन्महातेजाः शबरीं शत्रुसूदनः  शबर्या पूजितः सम्यग्रामो दशरथात्मजः \| |
| 1.1.59 | सुग्रीवाय च तत्सर्वं शंसद्रामो महाबलः  आदितस्तद्यथावृत्तं सीतायाश्च विशेषतः \| |
| 1.1.60 | सुग्रीवश्चापि तत्सर्वं श्रुत्वा रामस्य वानरः  चकार सख्यं रामेण प्रीतश्चैवाग्निसाक्षिकम् \| |
| 1.1.63 | सुग्रीवः शङ्कितश्चासीन्नित्यं वीर्येण राघवे  राघवप्रत्ययार्थं तु दुन्दुभेः कायमुत्तमम् \| दर्शयामास सुग्रीवो महापर्वतसन्निभम् |
| 1.1.65 | उत्स्मयित्वा महाबाहुः प्रेक्ष्य चास्थि महाबलः \| पादाङ्गुष्ठेन चिक्षेप सम्पूर्णं दशयोजनम् |
| 1.1.69 | अनुमान्य तदा तारां सुग्रीवेण समागतः \| निजघान च तत्रैनं शरेणैकेन राघवः |
| 1.1.70 | ततः सुग्रीववचनाद्धत्वा वालिनमाहवे \| सुग्रीवमेव तद्राज्ये राघवः प्रत्यपादयत् |
| 1.1.76 | अस्त्रेणोन्मुक्तमात्मानं ज्ञात्वा पैतामहाद्वरात् \| मर्षयन् राक्षसान् वीरो यन्त्रिणस्तान्यदृच्छया  ततो दग्ध्वा पुरीं लङ्कामृते सीतां च मैथिलीम् \| रामाय |
| 1.1.81 | तेन गत्वा पुरीं लङ्कां हत्वा रावणमाहवे \| रामः सीतामनुप्राप्य परां व्रीडामुपागमत् |
| 1.1.82 | तामुवाच ततो रामः परुषं जनसंसदि \| अमृष्यमाणा सा सीता विवेश ज्वलनं सती |
| 1.1.85 | अभिषिच्य च लङ्कायां राक्षसेन्द्रं विभीषणम् \| कृतकृत्यस्ततो रामो विज्वरः प्रमुमोद ह |
| 1.1.87 | भरद्वाजाश्रमं गत्वा रामः सत्यपराक्रमः \| भरतस्यान्तिकं रामो हनुमन्तं व्यसर्जयत् |
| 1.1.88 | पुनराख्यायिकां जल्पन् सुग्रीवसहितश्च सः \| पुष्पकं तत्समारुह्य नन्दिग्रामं ययौ तदा |
| 1.1.92 | न चाग्निजं भयं किञ्चिन्नाप्सु मज्जन्ति जन्तवः \| न वातजं भयं किञ्चिन्नापि ज्वरकृतं तथा  न चापि क्षुद्भयं तत्र न तस्करभयं तथा \| |
| 1.1.93 | नगराणि च राष्ट्राणि धनधान्ययुतानि च  नित्यं प्रमुदिताः सर्वे यथा कृतयुगे तथा \| |
| 1.1.100 | पठन् द्विजो वागृषभत्वमीयात् \| स्यात् क्षत्रियो भूमिपतित्वमीयात् \|\| वणिग्जनः पण्यफलत्वमीयात् \| जनश्च शूद्रोऽपि महत्त्वमीयात् |
| 1.1.1 | श्लोकेन प्रति साहस्रं प्रथमे क्रमात् \| गायत्र्यक्षरमेकैकं स्थापयामास वै मुनिः \|\| १. त - तपः स्वाध्यायनिरतं तपस्वी वाग्विदां वरम् \| नारदं परिपप्रच्छ वा |
| 1.2.2 | यथावत्पूजितस्तेन देवर्षिर्नारदस्तथा \| आपृच्छैवाभ्यनुज्ञातः स जगाम विहायसम् |
| 1.2.3 | स मुहूर्तं गते तस्मिन्देवलोकं मुनिस्तदा \| जगाम तमसातीरं जाह्नव्यास्त्वविदूरतः |
| 1.2.14 | ततः करुणवेदित्वादधर्मोऽयमिति द्विजः \| निशाम्य रुदतीं क्रौञ्चीमिदं वचनमब्रवीत् |

## Ayodhyākāṇḍa (II)

Critical 3160 verses vs Southern 4105 verses. 91 identical, 2389 aligned-but-different, 680 critical-only, 1491 southern-only.

### Major differences (sim < 0.6) — 29 pairs, showing up to 60

| Critical locus | Southern locus | sim | Critical text | Southern text |
|---|---|---:|---|---|
| 2.9.13 | 2.2.17 | 0.4 | tatrāpi vikṣataḥ śastraiḥ patis te rakṣitas tvayā tuṣṭena tena dattau te dvau varau śubhadarśane | तुष्टेन तेन दत्तौ ते द्वौ वरौ शुभदर्शने \| सत्वयोक्तः पतिर्देवि यदेच्छेयं तदा वरौ  गृह्णीयामिति तत्तन तधेत्युक्तं महात्म |
| 2.1.24 | 2.1.29 | 0.45 | abhiyātā prahartā ca senānayaviśāradaḥ apradhṛṣyaś ca saṃgrāme kruddhair api surāsuraiḥ | धनुर्वेदविदां श्रेष्ठो लोकेऽतिरथसम्मतः \| अभियाता प्रहर्ता च सेनानयविशारदः |
| 2.1.23 | 2.1.28 | 0.461 | ārohe vinaye caiva yukto vāraṇavājinām dhanurvedavidāṃ śreṣṭho loke 'tirathasaṃmataḥ | वैहारिकाणां शिल्पानां विज्ञातार्थविभागवित् \| आरोहे विनये चैव युक्तो वारणवाजिनाम् |
| 2.19.21 | 2.22.25 | 0.461 | vyāhate 'py abhiṣeke me paritāpo na vidyate tasmād aparitāpaḥ saṃs tvam apy anuvidhāya mām | एतया तत्त्वया बुद्ध्या संस्तभ्यात्मानमात्मना \| व्याहते अपि अभिषेके मे परितापो न विद्यते |
| 2.66.28 | 2.72.34 | 0.475 | ārye kim abravīd rājā pitā me satyavikramaḥ paścimaṃ sādhusaṃdeśam icchāmi śrotum ātmanaḥ | धर्मविद्धर्मनित्यश्च सत्यसन्धो दृढव्रतः \| आर्ये किम् अब्रवीद् राजा पिता मे सत्य विक्रमः |
| 2.20.8 | 2.23.7 | 0.479 | pāpayos tu kathaṃ nāma tayoḥ śaṅkā na vidyate santi dharmopadhāḥ ślakṣṇā dharmātman kiṃ na budhyase | किम् नाम कृपणम् दैवम् अशक्तम् अभिशंसति \| पापयोस् तु कथम् नाम तयोह् शन्का न विद्यते |
| 2.49.2 | 2.55.3 | 0.486 | prasthitāṃś caiva tān prekṣya pitā putrān ivānvagāt tataḥ pracakrame vaktuṃ vacanaṃ sa mahāmuniḥ | ततः प्रचक्रमे वक्तुम् वचनम् स महामुनिः \| भर्द्वाजो महातेजा रामम् सत्यपराक्रमम् |
| 2.84.19 | 2.90.19 | 0.489 | uvāca taṃ bharadvājaḥ prasādād bharataṃ vacaḥ tvayy etat puruṣavyāghraṃ yuktaṃ rāghavavaṃśaje | वशिष्ठादिभि ऋत्विग्भि र्याचितो भगवांस्ततः \| उवाच तम् भरद्वाजः प्रसादाद् भरतम् वचः |
| 2.63.11 | 2.69.11 | 0.495 | svapne 'pi sāgaraṃ śuṣkaṃ candraṃ ca patitaṃ bhuvi sahasā cāpi saṃśantaṃ jvalitaṃ jātavedasaṃ | स्वप्ने अपि सागरम् शुष्कम् चन्द्रम् च पतितम् भुवि \| सहसा च अपि संशन्तम् ज्वलितम् जात वेदसम्  औपवाह्यस्य नागस्य विषाणम्  |
| 2.2.32 | 2.2.52 | 0.497 | sarvān devān namasyanti rāmasyārthe yaśasvinaḥ teṣām āyācitaṃ deva tvatprasādāt samṛdhyatām | स्त्रियो वृद्धास्तरुण्यश्च सायं प्रातः समाहिताः \| सर्वान् देवान् नमस्यन्ति रामस्यार्थे यशस्विनः |
| 2.98.9 | 2.105.8 | 0.497 | sa yadā puṣpito bhūtvā phalāni na vidarśayet sa tāṃ nānubhavet prītiṃ yasya hetoḥ prabhāvitaḥ | यथा तु रोपितो वृक्षः पुरुषेण विवर्धितः \| ह्रस्वकेन दुरारोहो रूढ स्कन्धो महा द्रुमः  स यदा पुष्पितो भूत्वा फलानि न विदर् |
| 2.13.27 | 2.15.42 | 0.498 | sa vājiyuktena rathena sārathir; narākulaṃ rājakulaṃ vilokayan tataḥ samāsādya mahādhanaṃ mahat; prahṛṣṭaromā sa babhūva | ततस्समासाद्य महाधनं महत् \| प्रहृष्टरोमा स बभूव सारथिः \| मृगैर्मयूरैश्च समाकुलोल्बणं \| गृहं वरार्हस्य शचीपतेरिव |
| 2.42.11 | 2.48.13 | 0.5 | vicitrakusumāpīḍā bahumañjaridhāriṇaḥ akāle cāpi mukhyāni puṣpāṇi ca phalāni ca | अकाले चापि मुख्यानि पुष्पाणि च फलानि च \| दर्शयिष्यन्ति अनुक्रोशात् गिरयो रामम् आगतम् |
| 2.63.17 | 2.69.19 | 0.5 | śuṣyatīva ca me kaṇṭho na svastham iva me manaḥ jugupsann iva cātmānaṃ na ca paśyāmi kāraṇam | एतन् निमित्तम् दीनो अहम् तन् न वः प्रतिपूजये \| शुष्यति इव च मे कण्ठो न स्वस्थम् इव मे मनः |
| 2.11.5 | 2.12.94 | 0.502 | mṛte mayi gate rāme vanaṃ manujapuṃgave hantānārye mamāmitre rāmaḥ pravrājito vanam | हन्तानार्ये ममामित्रे सकामा भव कैकयि  मृते मयि गते रामे वनम् पुरुषपुङ्गवे \| सेदानीम् विधवा राज्यम् सपुत्रा कारयिष्यसि |
| 2.1.22 | 2.1.27 | 0.503 | arthadharmau ca saṃgṛhya sukhatantro na cālasaḥ vaihārikāṇāṃ śilpānāṃ vijñātārthavibhāgavit | श्रैष्ठ्यं शास्त्रसमूहेषु प्राप्तो व्यामिश्रकेषु च \| अर्थधर्मौ च संगृह्य सुखतन्त्रो न चालसः |
| 2.3.13 | 2.3.27 | 0.506 | gharmābhitaptāḥ parjanyaṃ hlādayantam iva prajāḥ na tatarpa samāyāntaṃ paśyamāno narādhipaḥ | गन्धर्वराजप्रतिमं लोके विख्यातपौरुषम्  दीर्घ बाहुं महसत्त्वं मत्तमातङ्गगामिनम् \| चन्द्रकान्ताननं राममतीव प्रियदर्शनम्   |
| 2.50.15 | 2.56.22 | 0.506 | śuśrūṣamāṇam ekāgram idaṃ vacanam abravīt aiṇeyaṃ māṃsam āhṛtya śālāṃ yakṣyāmahe vayam | ऐणेयम् मांसम् आहृत्य शालाम् यक्ष्यामहे वयम् \| कर्त्व्यम् वास्तुशमनम् सौमित्रे चिरजीवभिः |
| 2.95.35 | 2.103.34 | 0.506 | vijñāya tumulaṃ śabdaṃ trastā bharatasainikāḥ abruvaṃś cāpi rāmeṇa bharataḥ saṃgato dhruvam | महाबलानाम् रुदताअं कुर्वतामुदकं पितुः \| विज्ञाय तुमुलं शब्दम् त्रस्ता भरतसैनिकाः |
| 2.9.42 | 2.2.55 | 0.509 | tathā protsāhitā devī gatvā mantharayā saha krodhāgāraṃ viśālākṣī saubhāgyamadagarvitā | तथा प्रोत्साहिता देवी गता मन्थरया सह \| क्रोधागारं विशालाक्षी सौभाग्यमदगर्विता  अनेकशतसाहस्रं मुक्ताहारं वराङ्गना \| अवम |
| 2.102.17 | 2.110.21 | 0.509 | sa tām abhyavadad vipro varepsuṃ putrajanmani tataḥ sā gṛham āgamya devī putraṃ vyajāyata | कृत्वाप्रदक्षिणं हृष्टा मुनिं तमनुमान्य च  पद्मपत्रसमानाक्षं पद्मगर्भसमप्रभम् \| ततः सा गृहम् आगम्य देवी पुत्रम् व्यजायत |
| 2.10.7 | 2.10.29 | 0.514 | yad idaṃ mama duḥkhāya śeṣe kalyāṇi pāṃsuṣu bhūmau śeṣe kimarthaṃ tvaṃ mayi kalyāṇa cetasi | भूमौ शेषे किमर्थं त्वं मयि कल्याणचेतसि \| भूतोपहतचित्तेव मम चित्तप्रमाथिनी |
| 2.7.5 | None | 0.516 | rāmamātā dhanaṃ kiṃ nu janebhyaḥ saṃprayacchati atimātraṃ praharṣo 'yaṃ kiṃ janasya ca śaṃsa me | उत्तमेनाभिसंयुक्ता हर्षेणार्थपरा सती \| राममाता धनं किं नु जनेभ्यः संप्रयच्छति \| २-७-८ |
| 2.21.5 | 2.24.6 | 0.52 | tvayā vihīnām iha māṃ śokāgnir atulo mahān pradhakṣyati yathā kakṣaṃ citrabhānur himātyaye | अयम् तु मामात्मभवस्तवादर्शनमारुतः \| विलापदुःखसमिधो रुदिताश्रुहुताहुतिः  चिन्ताबाष्पमहाधूस्तवागमनचिन्तजः \| कर्शयित्वा भ |
| 2.37.27 | 2.42.33 | 0.528 | na tvāṃ paśyāmi kausalye sādhu māṃ pāṇinā spṛśa rāmaṃ me 'nugatā dṛṣṭir adyāpi na nivartate | रामम् मेऽनुगता दृष्टिरद्यापि न निवर्तते \| न त्वाम् पश्यामि कौसल्ये साधु माम् पाणिना स्पृश |
| 2.7.4 | 2.7.7 | 0.536 | avidūre sthitāṃ dṛṣṭvā dhātrīṃ papraccha mantharā uttamenābhisaṃyuktā harṣeṇārthaparā satī | प्रहर्षोत्फुल्लनयनां पाण्डुरक्षौमवासिनीम् \| अविदूरे स्थितां दृष्ट्वा धात्रीं पप्रच्छ मन्थरा |
| 2.84.9 | 2.112.26 | 0.539 | tatheti ca pratijñāya bharadvājo mahātapāḥ bharataṃ pratyuvācedaṃ rāghavasnehabandhanāt | तथेति च प्रतिज्ञाय तं परिष्वज्य सादरम्  शत्रुघ्नम् च परिष्वज्य भरतं चेदमब्रवीत् \| |
| 2.43.6 | 2.49.4 | 0.56 | yā putram īdṛśaṃ rājñaḥ pravāsayati dhārmikam vana vāse mahāprājñaṃ sānukrośam atandritam | राजानम् धिग् दशरथम् कामस्य वशम् आगतम्  हा नृशंस अद्य कैकेयी पापा पाप अनुबन्धिनी \| तीक्ष्णा सम्भिन्न मर्यादा तीक्ष्णे कर |
| 2.14.20 | 2.16.29 | 0.572 | hariyuktaṃ sahasrākṣo ratham indra ivāśugam prayayau tūrṇam āsthāya rāghavo jvalitaḥ śriyā | मेघनादमसम्बाधं मणिहेमविभूशितम् \| मुष्णन्तम् इव चक्षूंषि प्रभया मेरुवर्चसम्  करेणुशिशुकल्पैश्च युक्तं परमवाजिभिः \| हरिय |

### Minor edits (sim 0.6–0.9) — 121 pairs, sample of 40

| Critical locus | Southern locus | sim | Critical text | Southern text |
|---|---|---:|---|---|
| 2.78.4 | 2.84.4 | 0.621 | atha dāśarathiṃ rāmaṃ pitrā rājyād vivāsitam bharataḥ kaikeyīputro hantuṃ samadhigacchati | बन्धयिष्यति वा दाशान् अथ वा अस्मान् वधिष्यति \| अथ दाशरथिम् रामम् पित्रा राज्यात् विवासितम्  सम्पन्नाम् श्रियमन्विच्चंस् |
| 2.82.2 | 2.88.1 | 0.621 | abravīj jananīḥ sarvā iha tena mahātmanā śarvarī śayitā bhūmāv idam asya vimarditam | तत् श्रुत्वा निपुणम् सर्वम् भरतः सह मन्त्रिभिः \| इन्गुदी मूलम् आगम्य राम शय्याम् अवेक्ष्य ताम्  अब्रवीद् जननीः सर्वा इह |
| 2.98.43 | 2.106.5 | 0.622 | yasyaiṣa buddhilābhaḥ syāt paritapyeta kena saḥ sa evaṃ vyasanaṃ prāpya na viṣīditum arhati | परावरज्ञो यश्च स्यात् यथा त्वं मनुजाधिप \| स एवम् व्यसनम् प्राप्य न विषीदितुम् अर्हति |
| 2.20.23 | 2.23.27 | 0.623 | pratijāne ca te vīra mā bhūvaṃ vīralokabhāk rājyaṃ ca tava rakṣeyam ahaṃ veleva sāgaram | स चेद् राजनि अनेक अग्रे राज्य विभ्रम शन्कया \| न एवम् इच्चसि धर्मात्मन् राज्यम् राम त्वम् आत्मनि  प्रतिजाने च ते वीर मा  |
| 2.100.6 | 2.108.5 | 0.623 | evam eva manuṣyāṇāṃ pitā mātā gṛhaṃ vasu āvāsamātraṃ kākutstha sajjante nātra sajjanāḥ | यथा ग्राम अन्तरम् गग्च्छन् नरः कश्चिद् क्वचिद् वसेत् \| उत्सृज्य च तम् आवासम् प्रतिष्ठेत अपरे अहनि  एवम् एव मनुष्याणाम्  |
| 2.2.20 | 2.2.29 | 0.624 | rāmaḥ satpuruṣo loke satyadharmaparāyaṇaḥ dharmajñaḥ satyasaṃdhaś ca śīlavān anasūyakaḥ | रामः सत्पुरुषो लोके सत्यधर्मपरायणः \| साक्षाद्रामाद्विनिर्वृत्तो धर्मश्चापि श्रिया सह |
| 2.4.2 | 2.4.1 | 0.63 | śva eva puṣyo bhavitā śvo 'bhiṣecyeta me sutaḥ rāmo rājīvatāmrākṣo yauvarājya iti prabhuḥ | गतेष्वथ नृपो भूयः पौरेषु सह मन्त्रिभिः \| मन्त्रयुत्वा ततश्चक्रे निश्चयज्ञः स निश्चयम्  श्व एव पुष्यो भविता श्वोऽभिषेच्य |
| 2.34.1 | 2.39.1 | 0.631 | rāmasya tu vacaḥ śrutvā muniveṣadharaṃ ca tam samīkṣya saha bhāryābhī rājā vigatacetanaḥ | रामस्य तु वचः श्रुत्वा मुनि वेष धरम् च तम् \| समीक्ष्य सह भार्याभी राजा विगत चेतनः  न एनम् दुह्खेन सम्तप्तः प्रत्यवैक्षत |
| 2.58.40 | 2.64.49 | 0.633 | sa tu divyena rūpeṇa muniputraḥ svakarmabhiḥ āśvāsya ca muhūrtaṃ tu pitarau vākyam abravīt | आबभाषे च वृद्धौ तौ सह शक्रेण तापसः \| आश्वास्य च मुहूर्तम् तु पितरौ वाक्यम् अब्रवीत् |
| 2.1.34 | 2.1.40 | 0.635 | taṃ samīkṣya mahārājo yuktaṃ samuditair guṇaiḥ niścitya sacivaiḥ sārdhaṃ yuvarājam amanyata | इत्येतैर्विविधैस्तैस्तैरन्यपार्थिवदुर्लभैः  शिष्टैरपरिमेयैश्च लोके लोकोत्तरैर्गुणैः \| तं समीक्ष्य महाराजो युक्तं समुदित |
| 2.99.5 | 2.107.5 | 0.637 | tataḥ sā saṃpratiśrāvya tava mātā yaśasvinī ayācata naraśreṣṭhaṃ dvau varau varavarṇinī | ततः सा सम्प्रतिश्राव्य तव माता यशस्विनी \| अयाचत नर श्रेष्ठम् द्वौ वरौ वर वर्णिनी  तव राज्यम् नर व्याघ्र मम प्रव्राजनम्  |
| 2.68.10 | 2.74.9 | 0.641 | yat tvayā dhārmiko rāmo nityaṃ satyaparāyaṇaḥ vanaṃ prasthāpito duḥkhāt pitā ca tridivaṃ gataḥ | न त्वम् अश्व पतेः कन्या धर्म राजस्य धीमतः \| राक्षसी तत्र जाता असि कुल प्रध्वंसिनी पितुः  यत् त्वया धार्मिको रामः नित्यम |
| 2.45.12 | 2.51.11 | 0.642 | asmin pravrajito rājā na ciraṃ vartayiṣyati vidhavā medinī nūnaṃ kṣipram eva bhaviṣyati | यो मन्त्र तपसा लब्धो विविधैः च परिश्रमैः \| एको दशरथस्य एष पुत्रः सदृश लक्षणः  अस्मिन् प्रव्रजितः राजा न चिरम् वर्तयिष्य |
| 2.26.15 | 2.29.17 | 0.643 | pretyabhāve 'pi kalyāṇaḥ saṃgamo me saha tvayā śrutir hi śrūyate puṇyā brāhmaṇānāṃ yaśasvinām | प्रेत्य भावे अपि कल्याणः सम्गमः मे सह त्वया \| श्रुतिर् हि श्रूयते पुण्या ब्राह्मणानाम् यशस्विनाम्  इह लोके च पितृभिर् य |
| 2.64.2 | 2.70.1 | 0.643 | samāgamya tu rājñā ca rājaputreṇa cārcitāḥ rājñaḥ pādau gṛhītvā tu tam ūcur bharataṃ vacaḥ | भरते ब्रुवति स्वप्नम् दूताः ते क्लान्त वाहनाः \| प्रविश्य असह्य परिखम् रम्यम् राज गृहम् पुरम्  समागम्य तु राज्ञा च राज प |
| 2.85.67 | 2.91.73 | 0.643 | hradāḥ pūrṇā rasālasya dadhnaḥ śvetasya cāpare babhūvuḥ pāyasasyānte śarkarāyāś ca saṃcayāḥ | ह्रदाः पूर्णा रसालस्य दध्नः श्वेतस्य च अपरे \| बभूवुः पायसस्य अन्ते शर्करायाः च संचयाः  कल्कामः चूर्ण कषायामः च स्नानानि |
| 2.98.25 | 2.105.26 | 0.643 | yathā kāṣṭhaṃ ca kāṣṭhaṃ ca sameyātāṃ mahārṇave sametya ca vyapeyātāṃ kālam āsādya kaṃ cana | यथा काष्ठम् च काष्ठम् च समेयाताम् महा अर्णवे \| समेत्य च व्यपेयाताम् कालम् आसाद्य कंचन  एवम् भार्याः च पुत्राः च ज्नातयः |
| 2.34.5 | 2.39.5 | 0.644 | na tv evānāgate kāle dehāc cyavati jīvitam kaikeyyā kliśyamānasya mṛtyur mama na vidyate | न तु एव अनागते काले देहाच् च्यवति जीवितम् \| कैकेय्या क्लिश्यमानस्य मृत्युर् मम न विद्यते  मो अहम् पावक सम्काशम् पश्यामि |
| 2.109.19 | 2.117.17 | 0.644 | tāṃ tu sītā mahābhāgām anasūyāṃ pativratām abhyavādayad avyagrā svaṃ nāma samudāharat | शिथिलाम् वलिताम् वृद्धाम् जरा पाण्डुर मूर्धजाम् \| सततम् वेपमान अन्गीम् प्रवाते कदली यथा  ताम् तु सीता महा भागाम् अनसूया |
| 2.13.5 | 2.15.5 | 0.645 | gaṅgāyamunayoḥ puṇyāt saṃgamād āhṛtaṃ jalam yāś cānyāḥ saritaḥ puṇyā hradāḥ kūpāḥ sarāṃsi ca | गङ्गायमुनयोः पुण्यात्सङ्गमादाहृतं जलम्  याश्चान्याः सरितः पुण्या ह्रदाः कूपाः सरांसि च \| प्राग्वाहाश्चोर्ध्ववाहाश्च तिर |
| 2.35.32 | 2.40.44 | 0.645 | tathā rudantīṃ kausalyāṃ rathaṃ tam anudhāvatīm krośantīṃ rāma rāmeti hā sīte lakṣmaṇeti ca | तथा रुदन्तीम् कौसल्याम् रथम् तम् अनुधावतीम् \| क्रोशन्तीम् राम राम इति हा सीते लक्ष्मण इति च  रामलक्ष्मणसीतार्थम् स्रवन् |
| 2.35.14 | 2.40.16 | 0.647 | sītātṛtīyān ārūḍhān dṛṣṭvā dhṛṣṭam acodayat sumantraḥ saṃmatān aśvān vāyuvegasamāñ jave | तथैवायुधजालानि भ्रातृभ्याम् कवचानि च \| रथोपस्थे प्रतिन्यस्य सचर्म कठिनम् च तत्  सीता तृतीयान् आरूढान् दृष्ट्वा धृष्टम्  |
| 2.48.2 | 2.54.2 | 0.647 | yatra bhāgīrathī gaṅgā yamunām abhivartate jagmus taṃ deśam uddiśya vigāhya sumahad vanam | यत्र भागीरथी गन्गा यमुनाम् अभिवर्तते \| जग्मुस् तम् देशम् उद्दिश्य विगाह्य सुमहद् वनम्  ते भूमिम् आगान् विविधान् देशामः  |
| 2.19.2 | 2.22.1 | 0.648 | āsādya rāmaḥ saumitriṃ suhṛdaṃ bhrātaraṃ priyam uvācedaṃ sa dhairyeṇa dhārayan sattvam ātmavān | अथ तम् व्यथया दीनम् सविशेषम् अमर्षितम् \| श्वसन्तम् इव नाग इन्द्रम् रोष विस्फारित ईक्षणम्  आसद्य रामः सौमित्रिम् सुह्ऱ्द |
| 2.85.15 | 2.91.17 | 0.648 | ghṛtācīm atha viśvācīṃ miśrakeśīm alambusām śakraṃ yāś copatiṣṭhanti brahmāṇaṃ yāś ca bhāminīḥ | घृताचीम् अथ विश्वाचीम् मिश्र केशीम् अलम्बुसाम् \| नागदन्तां च हेमां च हिमामद्रिकृतस्थलाम् |
| 2.14.18 | 2.16.27 | 0.649 | sa sarvān arthino dṛṣṭvā sametya pratinandya ca tataḥ pāvakasaṃkāśam āruroha rathottamam | अथ मध्यमकक्ष्यायां समागच्छत् सुहृज्जनैः \| स सर्वानर्थिनो दृष्ट्वा समेत्य प्रतिनन्द्य च  ततः पावकसंकाशमारुरोह रथोत्तमम्  |
| 2.33.10 | 2.37.10 | 0.649 | sā vyapatrapamāṇeva pratigṛhya ca durmanāḥ gandharvarājapratimaṃ bhartāram idam abravīt | सा व्यपत्रपमाणा इव प्रतिगृह्य च दुर्मनाः \| गन्धर्व राज प्रतिमम् भर्तारम् इदम् अब्रवीत्  अश्रुसंपूर्ण्नेत्रा च धर्मज्ञा  |
| 2.54.12 | 2.60.12 | 0.649 | pathi pṛcchati vaidehī grāmāṃś ca nagarāṇi ca gatiṃ dṛṣṭvā nadīnāṃ ca pādapān vividhān api | परि पृच्चति वैदेही ग्रामामः च नगराणि च \| गतिम् दृष्ट्वा नदीनाम् च पादपान् विविधान् अपि  रामम् हि लक्ष्मनम् वापि पृष्ट्व |
| 2.66.18 | 2.72.22 | 0.649 | tam ārtaṃ devasaṃkāśaṃ samīkṣya patitaṃ bhuvi utthāpayitvā śokārtaṃ vacanaṃ cedam abravīt | तम् आर्तम् देव सम्काशम् समीक्ष्य पतितम् भुवि \| निकृत्तमिव सालस्य स्कन्धम् परशुना वने  मत्तमातङ्गसम्काशम् चन्द्रार्कसदृश |
| 2.41.25 | 2.46.30 | 0.65 | muhūrtaṃ tvaritaṃ gatvā nirgataya rathaṃ punaḥ yathā na vidyuḥ paurā māṃ tathā kuru samāhitaḥ | मोहन अर्थम् तु पौराणाम् सूतम् रामः अब्रवीद् वचः \| उदन् मुखः प्रयाहि त्वम् रथम् आस्थाय सारथे  मुहूर्तम् त्वरितम् गत्वा न |
| 2.58.22 | 2.64.27 | 0.65 | naya nau nṛpa taṃ deśam iti māṃ cābhyabhāṣata adya taṃ draṣṭum icchāvaḥ putraṃ paścimadarśanam | नय नौ नृप तम् देशम् इति माम् च अभ्यभाषत \| अद्य तम् द्रष्टुम् इच्चावः पुत्रम् पश्चिम दर्शनम्  रुधिरेण अवसित अन्गम् प्रकी |
| 2.14.4 | 2.16.4 | 0.651 | te samīkṣya samāyāntaṃ rāmapriyacikīrṣavaḥ sahabhāryāya rāmāya kṣipram evācacakṣire | ते समीक्ष्य समायान्तं रामप्रियचिकीर्षवः \| सहसोत्पतिताः सर्वे ह्यसनेभ्यः ससम्भ्रमाः |
| 2.20.34 | 2.23.38 | 0.651 | anurūpāv imau bāhū rāma karma kariṣyataḥ abhiṣecanavighnasya kartṝṇāṃ te nivāraṇe | अद्य चन्दन सारस्य केयूरा मोक्षणस्य च \| वसूनाम् च विमोक्षस्य सुह्ऱ्दाम् पालनस्य च  अनुरूपाव् इमौ बाहू राम कर्म करिष्यतः  |
| 2.46.72 | 2.52.87 | 0.652 | sā tvāṃ devi namasyāmi praśaṃsāmi ca śobhane prāpta rājye naravyāghra śivena punar āgate | सा त्वाम् देवि नमस्यामि प्रशंसामि च शोभने \| प्राप्त राज्ये नर व्याघ्र शिवेन पुनर् आगते  गवाम् शत सहस्राणि वस्त्राणि अन् |
| 2.86.20 | 2.92.20 | 0.652 | yām imāṃ bhagavan dīnāṃ śokān aśanakarśitām pitur hi mahiṣīṃ devīṃ devatām iva paśyasi | याम् इमाम् भगवन् दीनाम् शोकान् अशन कर्शिताम् \| पितुर् हि महिषीम् देवीम् देवताम् इव पश्यसि  एषा तम् पुरुष व्याघ्रम् सिम् |
| 2.96.23 | 2.104.25 | 0.652 | mukhaṃ te prekṣya māṃ śoko dahaty agnir ivāśrayam bhṛśaṃ manasi vaidehi vyasanāraṇisaṃbhavaḥ | पद्ममातपसन्तप्तं परिक्लिष्टमिवोत्पलम् \| काञ्चनं रजसा ध्वस्तम् क्स्लिष्टं चन्द्रमिवाम्बुदैः  मुखम् ते प्रेक्ष्य माम् शोक |
| 2.46.23 | 2.52.30 | 0.655 | evam uktvā tu rājānaṃ mātaraṃ ca sumantra me anyāś ca devīḥ sahitāḥ kaikeyīṃ ca punaḥ punaḥ | एवम् उक्त्वा तु राजानम् मातरम् च सुमन्त्र मे \| अन्याः च देवीः सहिताः कैकेयीम् च पुनः पुनः  आरोग्यम् ब्रूहि कौसल्याम् अथ |
| 2.81.3 | 2.87.2 | 0.655 | pratyāśvasya muhūrtaṃ tu kālaṃ paramadurmanāḥ papāta sahasā totrair hṛdi viddha iva dvipaḥ | सुकुमारो महा सत्त्वः सिम्ह स्कन्धो महा भुजः \| पुण्डरीक विशाल अक्षः तरुणः प्रिय दर्शनः  प्रत्याश्वस्य मुहूर्तम् तु कालम् |
| 2.84.1 | 2.90.1 | 0.655 | bharadvājāśramaṃ dṛṣṭvā krośād eva nararṣabhaḥ balaṃ sarvam avasthāpya jagāma saha mantribhiḥ | द्भरद्वाज आश्रमम् दृष्ट्वा क्रोशाद् एव नर ऋषभः \| बलम् सर्वम् अवस्थाप्य जगाम सह मन्त्रिभिः  पद्भ्याम् एव हि धर्मज्नो न्य |
| 2.98.28 | 2.105.29 | 0.658 | yathā hi sārthaṃ gacchantaṃ brūyāt kaś cit pathi sthitaḥ aham apy āgamiṣyāmi pṛṣṭhato bhavatām iti | यथा हि सार्थम् गग्च्छन्तम् ब्रूयात् कश्चित् पथि स्थितः \| अहम् अप्य् आगमिष्यामि पृष्ठतो भवताम् इति  एवम् पूर्वैर् गतो मा |

### Critical-only verses — 680, sample of 30 (present in Baroda critical, absent from Southern)

| Locus | Text |
|---|---|
| 2.1.1 | kasya cit tv atha kālasya rājā daśarathaḥ sutam bharataṃ kekayīputram abravīd raghunandanaḥ |
| 2.1.2 | ayaṃ kekayarājasya putro vasati putraka tvāṃ netum āgato vīra yudhājin mātulas tava |
| 2.1.3 | śrutvā daśarathasyaitad bharataḥ kekayīsutaḥ gamanāyābhicakrāma śatrughnasahitas tadā |
| 2.1.4 | āpṛcchya pitaraṃ śūro rāmaṃ cākliṣṭakāriṇam mātṝṃś cāpi naraśreṣṭhaḥ śatrughnasahito yayau |
| 2.1.5 | yudhājit prāpya bharataṃ saśatrughnaṃ praharṣitaḥ svapuraṃ prāviśad vīraḥ pitā tasya tutoṣa ha |
| 2.1.11 | gate ca bharate rāmo lakṣmaṇaś ca mahābalaḥ pitaraṃ devasaṃkāśaṃ pūjayām āsatus tadā |
| 2.1.12 | pitur ājñāṃ puraskṛtya paurakāryāṇi sarvaśaḥ cakāra rāmo dharmātmā priyāṇi ca hitāni ca |
| 2.1.13 | mātṛbhyo mātṛkāryāṇi kṛtvā paramayantritaḥ gurūṇāṃ gurukāryāṇi kāle kāle 'nvavaikṣata |
| 2.1.14 | evaṃ daśarathaḥ prīto brāhmaṇā naigamās tathā rāmasya śīlavṛttena sarve viṣayavāsinaḥ |
| 2.1.16 | kathaṃ cid upakāreṇa kṛtenaikena tuṣyati na smaraty apakārāṇāṃ śatam apy ātmavattayā |
| 2.1.17 | śīlavṛddhair jñānavṛddhair vayovṛddhaiś ca sajjanaiḥ kathayann āsta vai nityam astrayogyāntareṣv api |
| 2.1.18 | kalyāṇābhijanaḥ sādhur adīnaḥ satyavāg ṛjuḥ vṛddhair abhivinītaś ca dvijair dharmārthadarśibhiḥ |
| 2.1.20 | śāstrajñaś ca kṛtajñaś ca puruṣāntarakovidaḥ yaḥ pragrahānugrahayor yathānyāyaṃ vicakṣaṇaḥ |
| 2.1.21 | āyakarmaṇy upāyajñaḥ saṃdṛṣṭavyayakarmavit śraiṣṭhyaṃ śāstrasamūheṣu prāpto vyāmiśrakeṣv api |
| 2.1.28 | tam evaṃvṛttasaṃpannam apradhṛṣya parākramam lokapālopamaṃ nātham akāmayata medinī |
| 2.1.33 | mahīm aham imāṃ kṛtsnām adhitiṣṭhantam ātmajam anena vayasā dṛṣṭvā yathā svargam avāpnuyām |
| 2.1.37 | sa labdhamānair vinayānvitair nṛpaiḥ; purālayair jānapadaiś ca mānavaiḥ upopaviṣṭair nṛpatir vṛto babhau; sahasracakṣur bhagavān ivāmaraiḥ |
| 2.2.1 | tataḥ pariṣadaṃ sarvām āmantrya vasudhādhipaḥ hitam uddharṣaṇaṃ cedam uvācāpratimaṃ vacaḥ |
| 2.2.3 | so 'ham ikṣvākubhiḥ pūrvair narendraiḥ paripālitam śreyasā yoktukāmo 'smi sukhārham akhilaṃ jagat |
| 2.2.4 | mayāpy ācaritaṃ pūrvaiḥ panthānam anugacchatā prajā nityam atandreṇa yathāśakty abhirakṣatā |
| 2.2.6 | prāpya varṣasahasrāṇi bahūny āyūṃṣi jīvitaḥ jīrṇasyāsya śarīrasya viśrāntim abhirocaye |
| 2.2.8 | so 'haṃ viśramam icchāmi putraṃ kṛtvā prajāhite saṃnikṛṣṭān imān sarvān anumānya dvijarṣabhān |
| 2.2.21 | kṣāntaḥ sāntvayitā ślakṣṇaḥ kṛtajño vijitendriyaḥ mṛduś ca sthiracittaś ca sadā bhavyo 'nasūyakaḥ |
| 2.2.23 | tenāsyehātulā kīrtir yaśas tejaś ca vardhate devāsuramanuṣyāṇāṃ sarvāstreṣu viśāradaḥ |
| 2.2.26 | putreṣv agniṣu dāreṣu preṣyaśiṣyagaṇeṣu ca nikhilenānupūrvyā ca pitā putrān ivaurasān |
| 2.2.29 | satyavādī maheṣvāso vṛddhasevī jitendriyaḥ vatsaḥ śreyasi jātas te diṣṭyāsau tava rāghavaḥ |
| 2.2.31 | abhyantaraś ca bāhyaś ca paurajānapado janaḥ striyo vṛddhās taruṇyaś ca sāyaṃprātaḥ samāhitāḥ |
| 2.3.2 | aho 'smi paramaprītaḥ prabhāvaś cātulo mama yan me jyeṣṭhaṃ priyaṃ putraṃ yauvarājyastham icchatha |
| 2.3.8 | atha tatra samāsīnās tadā daśarathaṃ nṛpam prācyodīcyāḥ pratīcyāś ca dākṣiṇātyāś ca bhūmipāḥ |
| 2.3.9 | mlecchāś cāryāś ca ye cānye vanaśailāntavāsinaḥ upāsāṃ cakrire sarve taṃ devā iva vāsavam |

### Southern-only verses — 1491, sample of 30 (in the vulgate, absent from critical)

| Locus | Text (Devanāgarī) |
|---|---|
| 2.1.1 | गच्छता मातुलकुलं भरतेन तदाऽनघः \| शत्रुघ्नो नित्यशत्रुघ्नो नीतः प्रीतिपुरस्कृतः |
| 2.1.7 | स हि देवैरुदीर्णस्य रावणस्य वधार्थिभिः \| अर्थितो मानुषे लोके जज्ञे विष्णुः सनातनः |
| 2.1.8 | कौसल्या शुशुभे तेन पुत्रेणामिततेजसा \| यथा वरेण देवानामदितिर्वज्रपाणिना |
| 2.1.9 | स हि रूपोपपन्नश्च वीर्यवाननसूयकः \| भूमावनुपमः सूनुर्गुणैर्दशरथोपमः |
| 2.1.11 | कथञ्चिदुपकारेण कृतेनैकेन तुष्यति \| न स्मरत्यपकाराणां शतमप्यात्मवत्तया |
| 2.1.12 | शीलवृद्धैर्ज्ञानवृद्धैर्वयोवृद्धैश्च सज्जनैः \| कथयन्नास्त वै नित्यमस्त्रयोग्यान्तरेष्वपि |
| 2.1.13 | बुद्धिमान्मधुराभाषी पूर्वभाषी प्रियंवदः \| वीर्यवान्न च वीर्येण महता स्वेन विस्मितः |
| 2.1.14 | न चानृतकथो विद्वान् वृद्धानां प्रतिपूजकः \| अनुरक्तः प्रजाभिश्च प्रजाश्चाप्यनुरज्यते |
| 2.1.15 | सानुक्रोशो जितक्रोधो ब्राह्मणप्रतिपूजकः \| दीनानुकम्पी धर्मज्ञो नित्यं प्रग्रहवाञ्शुचिः |
| 2.1.16 | कुलोचितमतिः क्षात्रं धर्मं स्वं बहुमन्यते \| मन्यते परया कीर्त्या महत्स्वर्गफलं ततः |
| 2.1.17 | नाश्रेयसि रतो विद्वान्न विरुद्धकथारुचिः \| उत्तरोत्तरयुक्तीनां वक्ता वाचस्पतिर्यथा |
| 2.1.18 | अरोगस्तरुणो वाग्मी वपुष्मान्देशकालवित् \| लोके पुरुषसारज्ञस्साधुरेको विनिर्मितः |
| 2.1.19 | स तु श्रेष्ठैर्गुणैर्युक्तः प्रजानां पार्थिवात्मजः \| बहिश्चर इव प्राणो बभूव गुणतः प्रियः |
| 2.1.20 | सम्यग्विद्याव्रतस्नातो यथावत्साङ्गवेदवित् \| इष्वस्त्रे च पितुः श्रेष्ठो बभूव भरताग्रजः |
| 2.1.21 | कल्याणाभिजनः साधुरदीनः सत्यवागृजुः \| वृद्धैरभिविनीतश्च द्विजैर्धर्मार्थदर्शिभिः |
| 2.1.23 | निभृतः संवृताकारो गुप्तमन्त्रः सहायवान् \| अमोघक्रोधहर्षश्च त्यागसंयमकालवित् |
| 2.1.24 | दृढभक्तिः स्थिरप्रज्ञो नासद्ग्राही न दुर्वचाः \| निस्तन्द्रिरप्रमत्तश्च स्वदोषपरदोषवित् |
| 2.1.25 | शास्त्रज्ञश्च कृतज्ञश्च पुरुषान्तरकोविदः \| यः प्रग्रहानुग्रहयोर्यथान्यायं विचक्षणः |
| 2.1.26 | सत्संग्रहप्रग्रहणे स्थानविन्निग्रहस्य च \| आयकर्मण्युपायज्ञः संदृष्टव्ययकर्मवित् |
| 2.1.33 | तमेवं व्रत्तसंपन्नमप्रधृष्यपराक्रमम्  लोकपालोपमं नाथमकामयत मेदिनी \| |
| 2.1.35 | अथ राज्ञो बभूवैवं वृद्धस्य चिरजीविनः  प्रीतिरेषा कथं रामो राजा स्यान्मयि जीवति \| |
| 2.1.39 | महीमहमिमां कृत्स्नामधितिष्ठन्तमात्मजम्  अनेन वयसा दृष्ट्वा यथा स्वर्गमवाप्नुयाम् \| |
| 2.1.42 | दिव्यन्तरिक्षे भूमौ च घोरमुत्पातजं भयम्  संचचक्षेऽथ मेधावी शरीरे चात्मनो जराम् \| |
| 2.1.43 | पूर्णचन्द्राननस्याथ शोकापनुदमात्मनः  लोके रामस्य बुबुधे सम्प्रियत्वं महात्मनः \| |
| 2.1.44 | आत्मनश्च प्रजानां च श्रेयसे च प्रियेण च  प्राप्तकालेन धर्मात्मा भक्त्या त्वरितवान् नृपः \| |
| 2.1.46 | न तु केकयराजानं जनकं वा नराधिपः  त्वरया चानयामास पश्चात्तौ श्रोष्यतः प्रियम् \| |
| 2.1.47 | तान्वेश्मनानाभरणैर्यथार्हं प्रतिपूजितान्  ददर्शालंकृतो राजा प्रजापतिरिव प्रजाः \| |
| 2.1.48 | अथोपविष्टे नृपतौ तस्मिन्परबलार्दने  ततः प्रविविशुः शेषा राजानो लोकसम्मताः \| |
| 2.1.50 | स लब्धमानैर्विनयान्वितैर्नृपैः \| पुरालयैर्जानपदैश्च मानवैः \| उपोपविष्टैर्नृपतिर्वृतो बभौ \| सहस्रचक्षुर्भगवानिवामरैः |
| 2.2.1 | ततः परिषदं सर्वामामन्त्र्य वसुधाधिपः \| हितमुद्धर्षणं चैवमुवाच प्रथितं वचः |

## Araṇyakāṇḍa (III)

Critical 2060 verses vs Southern 2312 verses. 24 identical, 1475 aligned-but-different, 561 critical-only, 726 southern-only.

### Major differences (sim < 0.6) — 37 pairs, showing up to 60

| Critical locus | Southern locus | sim | Critical text | Southern text |
|---|---|---:|---|---|
| 3.59.18 | 3.61.21 | 0.364 | nikhilena vicinvantau sītāṃ daśarathātmajau tasya śailasya sānūni guhāś ca śikharāṇi ca | तस्य शैलस्य सानूनि शिलाः च शिखराणि च \| निखिलेन विचिन्वन्तौ न एव ताम् अभिजग्मतुः |
| 3.10.21 | 3.11.21 | 0.39 | praviśya saha vaidehyā lakṣmaṇena ca rāghavaḥ tadā tasmin sa kākutsthaḥ śrīmaty āśramamaṇḍale | एवम् कथयमानः स ददर्श आश्रम मण्डलम् \| कुश चीर परिक्षिप्तम् ब्राह्म्या लक्ष्म्या समावृतम्  प्रविश्य सह वैदेह्या लक्ष्मणेन |
| 3.11.17 | 3.12.17 | 0.414 | sa tatra brahmaṇaḥ sthānam agneḥ sthānaṃ tathaiva ca viṣṇoḥ sthānaṃ mahendrasya sthānaṃ caiva vivasvataḥ | स तत्र ब्रह्मणः स्थानम् अग्नेः स्थानम् तथैव च  विष्णोः स्थानम् महेन्द्रस्य स्थानम् चैव विवस्वतः \| सोम स्थानम् भग स्थानम |
| 3.16.17 | 3.17.20 | 0.425 | sābravīd vacanaṃ śrutvā rākṣasī madanārditā śrūyatāṃ rāma vakṣyāmi tattvārthaṃ vacanaṃ mama | श्रूयताम् राम वक्ष्यामि तत्त्वार्थम् वचनम् मम \| अहम् शूर्पणखा नाम राक्षसी कामरूपिणी  अरण्यम् विचरामि इदम् एका सर्व भयंक |
| 3.13.15 | 3.14.14 | 0.455 | ādityā vasavo rudrā aśvinau ca paraṃtapa ditis tv ajanayat putrān daityāṃs tāta yaśasvinaḥ | अदित्याम् जज्ञिरे देवाः त्रयः त्रिंशत् अरिंदम  आदित्या वसवो रुद्रा अश्विनौ च परंतप \| |
| 3.1.5 | 3.1.6 | 0.457 | āraṇyaiś ca mahāvṛkṣaiḥ puṇyaiḥ svāduphalair vṛtam balihomārcitaṃ puṇyaṃ brahmaghoṣanināditam | बलिहोमार्चितं पुण्यं ब्रह्मघोषनिनादितम् \| पुष्पैश्चान्यैः परिक्षिप्तं पद्मिन्या च सपद्मया |
| 3.65.25 | 3.69.44 | 0.469 | ghoraṃ deśam imaṃ prāptau mama bhakṣāv upasthitau vadataṃ kāryam iha vāṃ kimarthaṃ cāgatau yuvām | वदतम् कार्यम् इह वाम् किम् अर्थम् च आगतौ युवाम्  इमम् देशम् अनुप्राप्तौ क्षुधा आर्तस्य इह तिष्ठतः \| |
| 3.43.4 | 3.45.3 | 0.47 | rakṣasāṃ vaśam āpannaṃ siṃhānām iva govṛṣam na jagāma tathoktas tu bhrātur ājñāya śāsanam | तम् क्षिप्रम् अभिधाव त्वम् भ्रातरम् शरण एषिणम्  रक्षसाम् वशम् आपन्नम् सिंहानाम् इव गोवृषम् \| |
| 3.2.13 | 3.2.13 | 0.477 | carāmi sāyudho nityam ṛṣimāṃsāni bhakṣayan iyaṃ nārī varārohā mama bharyā bhaviṣyati | इयम् नारी वरारोहा मम भार्या भविष्यति  युवयोः पापयोः च अहम् पास्यामि रुधिरम् मृधे \| |
| 3.58.30 | 3.60.34 | 0.48 | bhakṣitau vepamānāgrau sahastābharaṇāṅgadau mayā virahitā bālā rakṣasāṃ bhakṣaṇāya vai | मया विरहिता बाला रक्षसाम् भक्षणाय वै \| सार्थेन इव परित्यक्ता भक्षिता बहु बांधवा |
| 3.55.18 | 3.57.20 | 0.483 | aśubhāny eva bhūyiṣṭhaṃ yathā prādurbhavanti me api lakṣmaṇa sītāyāḥ sāmagryaṃ prāpnuyāvahe | अपि लक्ष्मण सीतायाः सामग्र्यम् प्राप्नुयावहे \| जीवन्त्याः पुरुषव्याघ्र सुताया जनक्स्य वै |
| 3.2.9 | 3.2.9 | 0.484 | abhyadhāvat susaṃkruddhaḥ prajāḥ kāla ivāntakaḥ sa kṛtvā bhairavaṃ nādaṃ cālayann iva medinīm | स कृत्वा भैरवम् नादम् चालयन् इव मेदिनीम्  अङ्केन आदाय वैदेहीम् अपक्रंय तदा अब्रवीत् \| |
| 3.38.19 | 3.40.25 | 0.484 | gaccha saumya śivaṃ mārgaṃ kāryasyāsya vivṛddhaye prāpya sītām ayuddhena vañcayitvā tu rāghavam | प्राप्य सीताम् अयुद्धेन वंचयित्वा तु राघवम् \| लंकाम् प्रति गमिष्यामि कृत कार्यः सह त्वया |
| 3.65.19 | 3.69.31 | 0.484 | ghorau bhujau vikurvāṇam ubhau yojanam āyatau karābhyāṃ vividhān gṛhya ṛṣkān pakṣigaṇān mṛgān | भक्षयंतम् महा घोरान् ऋक्ष सिम्ह मृग द्विपान् \| घोरौ भुजौ विकुर्वाणम् उभौ योजनम् आयतौ |
| 3.22.22 | 3.23.22 | 0.489 | sakāmā bhaginī me 'stu pītvā tu rudhiraṃ tayoḥ yannimittaṃ tu rāmasya lakṣmaṇasya viparyayaḥ | यन् निमित्तम् तु रामस्य लक्ष्मणस्य विपर्ययः  सकामा भगिनी मे अस्तु पीत्वा तु रुधिरम् तयोः \| |
| 3.58.31 | 3.60.35 | 0.489 | sārtheneva parityaktā bhakṣitā bahubāndhavā hā lakṣmaṇa mahābāho paśyasi tvaṃ priyāṃ kva cit | हा लक्ष्मण महाबाहो पश्यसे त्वम् प्रियाम् क्वचित् \| हा प्रिये क्व गता भद्रे हा सीते इति पुनः पुनः |
| 3.34.2 | 3.36.2 | 0.494 | jānīṣe tvaṃ janasthānaṃ bhrātā yatra kharo mama dūṣaṇaś ca mahābāhuḥ svasā śūrpaṇakhā ca me | जानीषे त्वम् जनस्थाने भ्राता यत्र खरो मम \| दूषणः च महाबाहुः स्वसा शूर्पणखा च मे  त्रिशिराः च महातेजा राक्षसः पिशित अशनः |
| 3.12.17 | 3.13.17 | 0.495 | ataś ca tvām ahaṃ brūmi gaccha pañcavaṭīm iti sa hi ramyo vanoddeśo maithilī tatra raṃsyate | स हि रम्यो वनोद्देशो मैथिली तत्र रंस्यते  स देशः श्लाघनीयः च न अतिदूरे च राघव \| |
| 3.59.19 | 3.61.22 | 0.497 | nikhilena vicinvantau naiva tām abhijagmatuḥ vicitya sarvataḥ śailaṃ rāmo lakṣmaṇam abravīt | विचित्य सर्वतः शैलम् रामो लक्ष्मणम् अब्रवीत् \| न इह पश्यामि सौमित्रे वैदेहीम् पर्वते शुभाम् |
| 3.30.21 | 3.32.21 | 0.5 | rākṣasī bhrātaraṃ krūraṃ sā dadarśa mahābalam taṃ divyavastrābharaṇaṃ divyamālyopaśobhitam | रावणम् सर्व भूतानाम् सर्व लोक भयावहम्  राक्षसी भ्रातरम् क्रूरम् सा ददर्श महाबलम् \| |
| 3.2.12 | 3.2.12 | 0.503 | adharmacāriṇau pāpau kau yuvāṃ munidūṣakau ahaṃ vanam idaṃ durgaṃ virāgho nāma rākṣasaḥ | अहम् वनम् इदम् दुर्गम् विराघो नाम राक्षसः  चरामि सायुधो नित्यम् ऋषि मांसानि भक्षयन् \| |
| 3.40.26 | 3.42.29 | 0.505 | upagamya samāghrāya vidravanti diśo daśa rākṣasaḥ so 'pi tān vanyān mṛgān mṛgavadhe rataḥ | राक्षसः सो अपि तान् वन्यान् मृगान् मृगवधे रतः  प्रच्छादनार्थम् भावस्य न भक्षयति संस्पृशन् \| |
| 3.2.8 | 3.2.8 | 0.508 | avasajyāyase śūle vinadantaṃ mahāsvanam sa rāmo lakṣmaṇaṃ caiva sītāṃ dṛṣṭvā ca maithilīm | स रामम् लक्ष्मणम् चैव सीताम् दृष्ट्वा च मैथिलीम्  अभ्य धावत् सुसंक्रुद्धो प्रजाः काल इव अन्तकः \| |
| 3.53.33 | 3.55.35 | 0.508 | prasādaṃ kuru me kṣipraṃ vaśyo dāso 'ham asmi te nemāḥ śūnyā mayā vācaḥ śuṣyamāṇena bhāṣitāḥ | एतौ पादौ मया स्निग्धौ शिरोभिः परिपीडितौ  प्रसादम् कुरु मे क्षिप्रम् वश्यो दासो अहम् अस्मि ते \| |
| 3.63.9 | 3.67.8 | 0.515 | kruddho rāmaḥ śaraṃ ghoraṃ saṃdhāya dhanuṣi kṣuram tataḥ parvatakūṭābhaṃ mahābhāgaṃ dvijottamam | इति उक्तः तत् वनम् सर्वम् विचचार स लक्ष्मणः  क्रुद्धो रामः शरम् घोरम् संधाय धनुषि क्षुरम् \| |
| 3.41.44 | 3.43.46 | 0.516 | bhaved dhato 'yaṃ vātāpir agastyeneva mā gatiḥ iha tvaṃ bhava saṃnaddho yantrito rakṣa maithilīm | इह त्वम् भव संनद्धो यंत्रितो रक्ष मैथिलीम्  अस्याम् आयत्तम् अस्माकम् यत् कृत्यम् रघुनंदन \| |
| 3.40.25 | 3.42.28 | 0.523 | paribhramati citrāṇi maṇḍalāni viniṣpatan samudvīkṣya ca sarve taṃ mṛgā ye 'nye vanecarāḥ | समुद्वीक्ष्य च सर्वे तम् मृगा ये अन्ये वनेचराः  उपगम्य समाघ्राय विद्रवन्ति दिशो दश \| |
| 3.71.12 | 3.75.11 | 0.526 | sa rāmo vidhivān vṛkṣān sarāṃsi vividhāni ca paśyan kāmābhisaṃtapto jagāma paramaṃ hradam | समीक्षमाणः पुष्प आढ्यम् सर्वतो विपुल द्रुमम्  कोयष्टिभिः च अर्जुनकैः शत पत्रैः च कीरकैः \| एतैः च अन्यैः च बहुभिः नादितम |
| 3.44.21 | 3.46.22 | 0.528 | karāntamitamadhyāsi sukeśī saṃhatastanī naiva devī na gandharvī na yakṣī na ca kiṃnarī | न एव देवी न गन्धर्वी न यक्षी न च किंनरी  न एवम् रूपा मया नारी दृष्ट पूर्वा मही तले \| |
| 3.50.40 | 3.52.41 | 0.528 | vikrośantīṃ dṛḍhaṃ sītāṃ dṛṣṭvā duḥkhaṃ tathā gatām tāṃ tu lakṣmaṇa rāmeti krośantīṃ madhurasvarām | सुप्रवेपित गात्राः च बभूवुः वन देवताः  विक्रोशन्तीम् दृढम् सीताम् दृष्ट्वा दुःखम् तथा गताम् \| |
| 3.10.41 | 3.11.43 | 0.533 | sa hi ramyo vanoddeśo bahupādapasaṃkulaḥ yadi buddhiḥ kṛtā draṣṭum agastyaṃ taṃ mahāmunim | यदि बुद्धिः कृता द्रष्टुम् अगस्त्यम् तम् महामुनिम् \| अद्य एव गमने बुद्धिम् रोचयस्व महामते |
| 3.70.7 | 3.74.8 | 0.535 | tām uvāca tato rāmaḥ śramaṇīṃ saṃśitavratām kaccit te nirjitā vighnāḥ kaccit te vardhate tapaḥ | कच्चित् ते निर्जिता विघ्नाः कच्चित् ते वर्धते तपः \| कच्चित् ते नियतः कोप आहारः च तपोधने |
| 3.70.8 | 3.74.9 | 0.535 | kaccit te niyataḥ kopa āhāraś ca tapodhane kaccit te niyamāḥ prāptāḥ kaccit te manasaḥ sukham | कच्चित् ते नियमाः प्राप्ताः कच्चित् ते मनसः सुखम् \| कच्चित् ते गुरु शुश्रूषा सफला चारु भाषिणि |
| 3.42.11 | 3.44.13 | 0.547 | tam eva mṛgam uddiśya jvalantam iva pannagam mumoca jvalitaṃ dīptam astrabrahmavinirmitam | भूयः तु शरम् उद्धृत्य कुपितः तत्र राघवः \| सूर्य रश्मि प्रतीकाशम् ज्वलंतम् अरि मर्दनम्  संधाय सुदृढे चापे विकृष्य बलवत्  |
| 3.13.17 | 3.14.17 | 0.549 | narakaṃ kālakaṃ caiva kālakāpi vyajāyata krauñcīṃ bhāsīṃ tathā śyenīṃ dhṛtarāṣṭrīṃ tathā śukīm | क्रौन्चीम् भासीम् तथा श्येनीम् धृतराष्ट्रीम् तथा शुकीम्  ताम्रा तु सुषुवे कन्याः पंच एता लोकविश्रुताः \| |
| 3.35.21 | 3.37.23 | 0.577 | sa sarvaiḥ sacivaiḥ sārdhaṃ vibhīṣaṇapuraskṛtaiḥ mantrayitvā tu dharmiṣṭhaiḥ kṛtvā niścayam ātmanaḥ | स सर्वैः सचिवैः सार्धम् विभीषण पुरस्कृतैः \| मंत्रयित्वा तु धर्मिष्ठैः कृत्वा निश्चयम् आत्मनः \| दोषाणाम् च गुणानाम् च स |
| 3.58.5 | 3.60.4 | 0.595 | dadarśa parṇaśālāṃ ca rahitāṃ sītayā tadā śriyā virahitāṃ dhvastāṃ hemante padminīm iva | उद् भ्रमन् इव वेगेन विक्षिपन् रघु नन्दनः \| तत्र तत्र उटज स्थानम् अभिवीक्ष्य समंततः  ददर्श पर्ण शालाम् च सीतया रहिताम् त |

### Minor edits (sim 0.6–0.9) — 191 pairs, sample of 40

| Critical locus | Southern locus | sim | Critical text | Southern text |
|---|---|---:|---|---|
| 3.45.9 | 3.47.8 | 0.604 | iti bruvāṇāṃ kaikeyīṃ śvaśuro me sa mānadaḥ ayācatārthair anvarthair na ca yācñāṃ cakāra sā | न अद्य भोक्ष्ये न च स्वप्स्ये न पास्ये कदाचन  एष मे जीवितस्य अन्तो रामो यदि अभिषिच्यते \| इति ब्रुवाणाम् कैकेयीम् श्वशुर |
| 3.55.5 | 3.57.5 | 0.614 | mārīcena tu vijñāya svaram ālakṣya māmakam vikruṣṭaṃ mṛgarūpeṇa lakṣmaṇaḥ śṛṇuyād yadi | मारीचेन तु विज्ञाय स्वरम् आलक्ष्य मामकम् \| विक्रुष्टम् मृग रूपेण लक्ष्मणः शृणुयात् यदि  स सौमित्रिः स्वरम् श्रुत्वा ताम |
| 3.32.9 | 3.36.8 | 0.615 | rakṣasāṃ bhīmavīryāṇāṃ sahasrāṇi caturdaśa nihatāni śarais tīkṣṇais tenaikena padātinā | चतुर्दश सहस्राणि रक्षसाम् उग्र तेजसाम्  निहतानि शरैः दीप्तैः मानुषेण पदातिना \| |
| 3.9.8 | 3.10.7 | 0.623 | mayā tu vacanaṃ śrutvā teṣām evaṃ mukhāc cyutam kṛtvā caraṇaśuśrūṣāṃ vākyam etad udāhṛtam | मया तु वचनम् श्रुत्वा तेषाम् एवम् मुखात् च्युतम्  कृत्वा वचन शुश्रुषाम् वाक्यम् एतत् उदाहृतम् \| प्रसीदन्तु भवन्तो मे ह् |
| 3.4.18 | 3.5.22 | 0.626 | ihopayāty asau rāmo yāvan māṃ nābhibhāṣate niṣṭhāṃ nayata tāvat tu tato māṃ draṣṭum arhati | इह उपयाति असौ रामो यावन् माम् न अभिभाषते \| निष्ठाम् नयत तावत् तु ततो मा द्रष्टुम् अर्हति  जितवन्तम् कृतार्थम् हि तदा अह |
| 3.10.5 | 3.11.5 | 0.626 | te gatvā dūram adhvānaṃ lambamāne divākare dadṛśuḥ sahitā ramyaṃ taṭākaṃ yojanāyatam | ते गत्वा दूरम् अध्वानम् लंबमाने दिवाकरे \| ददृशुः सहिता रंयम् तटाकम् योजन आयुतम्  पद्म पुष्कर संबाधम् गज यूथैः अलंकृतम्  |
| 3.16.3 | 3.1.7 | 0.627 | sa rāmaḥ parṇaśālāyām āsīnaḥ saha sītayā virarāja mahābāhuś citrayā candramā iva | उवास सुखितः तत्र पूज्यमानो महर्षभः\| स रामः पर्ण शालायाम् आसीनः सह सीतया -३ विरराज महा बाहुः चित्रया चन्द्रमा इव \| लक्ष |
| 3.27.6 | 3.28.6 | 0.627 | sa sarvāś ca diśo bāṇaiḥ pradiśaś ca mahārathaḥ pūrayām āsa taṃ dṛṣṭvā rāmo 'pi sumahad dhanuḥ | स सर्वाः च दिशो बाणैः प्रदिशः च महारथः \| पूरयामास तम् दृष्ट्वा रामो अपि सुमहत् धनुः  स सायकैः दुर्विषहैः स स्फुलिन्गैः  |
| 3.57.13 | 3.59.14 | 0.628 | alaṃ vaiklavyam ālambya svasthā bhava nirutsukā na cāsti triṣu lokeṣu pumān yo rāghavaṃ raṇe | अलम् वैक्लवताम् गंतुम् स्वस्था भव निर् उत्सुका \| न च अस्ति त्रिषु लोकेषु पुमान् यो राघवम् रणे  जातो वा जायमानो वा संयुग |
| 3.33.38 | 3.35.39 | 0.632 | sa rāvaṇaḥ samāgamya vidhivat tena rakṣasā tataḥ paścād idaṃ vākyam abravīd vākyakovidaḥ | स रावणः समागम्य विधिवत् तेन रक्षसा \| मारीचेन अर्चितो राजा सर्व कामैः अमानुषैः |
| 3.35.9 | 3.37.8 | 0.632 | na ca dharmaguṇair hīnaiḥ kausalyānandavardhanaḥ na ca tīkṣṇo hi bhūtānāṃ sarveṣāṃ ca hite rataḥ | न च पित्रा परित्यक्तो न अमर्यादः कथंचन \| न लुब्धो न च दुःशीलो न च क्षत्रिय पांसनः  न च धर्म गुणैर् हीनैः कौसल्या आनंद व |
| 3.10.22 | 3.11.22 | 0.635 | uṣitvā susukhaṃ tatra pūrjyamāno maharṣibhiḥ jagāma cāśramāṃs teṣāṃ paryāyeṇa tapasvinām | तदा तस्मिन् स काकुत्स्थः श्रीमति आश्रम मण्डले  उषित्वा स सुखम् तत्र पूर्ज्यमानो महर्षिभिः \| जगाम च आश्रमान् तेषाम् पर्य |
| 3.55.7 | 3.57.7 | 0.636 | rākṣasaiḥ sahitair nūnaṃ sītāyā īpsito vadhaḥ kāñcanaś ca mṛgo bhūtvā vyapanīyāśramāt tu mām | राक्षसैः सहितैर् नूनम् सीताया ईप्सितो वधः \| कांचनः च मृगो भूत्वा व्यपनीय आश्रमात् तु माम्  दूरम् नीत्वा अथ मारीचो राक्ष |
| 3.7.9 | 3.8.8 | 0.637 | tāvad icchāmahe gantum ity uktvā caraṇau muneḥ vavande sahasaumitriḥ sītayā saha rāghavaḥ | अविषह्य आतपो यावत् सूर्यो न अति विराजते \| अमार्गेण आगताम् लक्ष्मीम् प्राप्य इव अन्वय वर्जितः  तावत् इच्छामहे गन्तुम् इत |
| 3.53.29 | 3.55.29 | 0.637 | puṣpakaṃ nāma suśroṇi bhrātur vaiśravaṇasya me vimānaṃ ramaṇīyaṃ ca tad vimānaṃ manojavam | पुष्पकम् नाम सुश्रोणि भ्रातुः वैश्रवणस्य मे  विमानम् सूर्य संकाशम् तरसा निर्जितम् रणे \| |
| 3.27.2 | 3.28.2 | 0.639 | sa dṛṣṭvā rākṣasaṃ sainyam aviṣahyaṃ mahābalam hatam ekena rāmeṇa dūṣaṇas triśirā api | स दृष्ट्वा राक्षसम् सैन्यम् अविषह्यम् महाबलम् \| हतम् एकेन रामेण दूषणः त्रिशिरा अपि  तद् बलम् हत भूयिष्ठम् विमनाः प्रेक् |
| 3.42.18 | 3.44.24 | 0.639 | hā sīte lakṣmaṇety evam ākruśya tu mahāsvaram mamāra rākṣasaḥ so 'yaṃ śrutvā sītā kathaṃ bhavet | हा सीते लक्ष्मण इति एवम् आक्रुश्य तु महा स्वनम् \| ममार राक्षसः सो अयम् श्रुत्वा सीता कथम् भवेत्  लक्ष्मणः च महाबाहुः का |
| 3.33.3 | 3.35.2 | 0.64 | iti kartavyam ity eva kṛtvā niścayam ātmanaḥ sthirabuddhis tato ramyāṃ yānaśālāṃ jagāma ha | तत् कार्यम् अनुगम्यांतर् यथावत् उपलभ्य च \| दोषाणाम् च गुणानाम् च सम्प्रधार्य बल अबलम्  इति कर्तव्यम् इति एव कृत्वा निश् |
| 3.13.21 | 3.14.21 | 0.642 | daśakrodhavaśā rāma vijajñe 'py ātmasaṃbhavāḥ mṛgīṃ ca mṛgamandāṃ ca harīṃ bhadramadām api | दश क्रोधवशा राम विजज्ञे अपि आत्मसंभवाः \| मृगीम् च मृगमंदाम् च हरीम् भद्रमदाम् अपि  मात.ंगीम् अथ शार्दूलीम् श्वेताम् च स |
| 3.34.13 | 3.36.12 | 0.642 | tasya bhāryāṃ janasthānāt sītāṃ surasutopamām ānayiṣyāmi vikramya sahāyas tatra me bhava | येन वैरम् विना अरण्ये सत्त्वम् आश्रित्य केवलम्  कर्ण नास अपहारेण भगिनी मे विरूपिता \| तस्य भार्याम् जनस्थानात् सीताम् सु |
| 3.23.7 | 3.24.7 | 0.643 | saṃprahāras tu sumahān bhaviṣyati na saṃśayaḥ ayam ākhyāti me bāhuḥ sphuramāṇo muhur muhuḥ | संप्रहारः तु सुमहान् भविष्यति न संशयः \| अयम् आख्याति मे बाहुः स्फुरमाणो मुहुर् मुहुः  संनिकर्षे तु नः शूर जयम् शत्रोः प |
| 3.5.12 | 3.6.12 | 0.645 | prāpnoti śāśvatīṃ rāma kīrtiṃ sa bahuvārṣikīm brahmaṇaḥ sthānam āsādya tatra cāpi mahīyate | युंजानः स्वान् इव प्राणान् प्राणैः इष्टान् सुतान् इव \| नित्य युक्तः सदा रक्षन् सर्वान् विषय वासिनः  प्राप्नोति शाश्वतीम |
| 3.43.10 | 3.45.11 | 0.645 | devi devamanuṣyeṣu gandharveṣu patatriṣu rākṣaseṣu piśāceṣu kiṃnareṣu mṛgeṣu ca | देवि देव मनुष्येषु गन्धर्वेषु पतत्रिषु  राक्षसेषु पिशाचेषु किन्नरेषु मृगेषु च \| दानवेषु च घोरेषु न स विद्येत शोभने  यो  |
| 3.60.22 | 3.64.35 | 0.645 | evaṃ sa ruṣito rāmo didhakṣann iva cakṣuṣā dadarśa bhūmau niṣkrāntaṃ rākṣasasya padaṃ mahat | एवम् प्ररुषितो रामो दिधक्षन् इव चक्षुषा  ददर्श भूमौ निष्क्रांतम् राक्षसस्य पदम् महत् \| त्रस्तया राम काङ्क्षिण्याः प्रधा |
| 3.60.39 | 3.64.56 | 0.645 | māṃ prāpya hi guṇo doṣaḥ saṃvṛttaḥ paśya lakṣmaṇa adyaiva sarvabhūtānāṃ rakṣasām abhavāya ca | माम् प्राप्य हि गुणो दोषः संवृत्तः पश्य लक्ष्मण \| अद्य एव सर्व भूतानाम् रक्षसाम् अभवाय च  संहृत्य एव शशि ज्योत्स्नाम् म |
| 3.37.19 | 3.39.19 | 0.646 | ahaṃ tasya prabhāvajño na yuddhaṃ tena te kṣamam raṇe rāmeṇa yudhyasva kṣamāṃ vā kuru rākṣasa | अहम् तस्य प्रभावज्ञो न युद्धम् तेन ते क्षमम् \| बलिम् वा नमुचिं वा अपि हन्यद्धि रघुन्ंअंदन |
| 3.63.18 | 3.67.19 | 0.647 | pariśrāntasya me pakṣau chittvā khaḍgena rāvaṇaḥ sītām ādāya vaidehīm utpapāta vihāyasaṃ | अयम् तु सारथिः तस्य मत् पक्ष निहतो भुविः \| परिश्रान्तस्य मे पक्षौ छित्त्वा खड्गेन रावणः  सीताम् आदाय वैदेहीम् उत्पपात व |
| 3.14.4 | 3.15.4 | 0.649 | ramate yatra vaidehī tvam ahaṃ caiva lakṣmaṇa tādṛśo dṛśyatāṃ deśaḥ saṃnikṛṣṭajalāśayaḥ | रमते यत्र वैदेही त्वम् अहम् चैव लक्ष्मण \| तादृशो दृश्यताम् देशः संनिकृष्ट जलाशयः  वन रामण्यकम् यत्र जल रामण्यकम् तथा \| |
| 3.30.1 | 3.32.1 | 0.649 | tataḥ śūrpaṇakhā dṛṣṭvā sahasrāṇi caturdaśa hatāny ekena rāmeṇa rakṣasāṃ bhīmakarmaṇām | ततः शूर्पणखा दृष्ट्वा सहस्राणि चतुर्दश \| हतानि एकेन रामेण रक्षसाम् भीम कर्मणाम्  दूषणम् च खरम् चैव हतम् त्रिशिरसम् रणे  |
| 3.48.14 | 3.50.14 | 0.65 | atra brūhi yathāsatyaṃ ko rāmasya vyatikramaḥ yasya tvaṃ lokanāthasya hṛtvā bhāryāṃ gamiṣyasi | यदि शूर्पणखा हेतोः जनस्थान गतः खरः \| अतिवृत्तो हतः पूर्वम् रामेण अक्लिष्ट कर्मणा  अत्र ब्रूहि यथा तत्त्वम् को रामस्य व् |
| 3.50.7 | 3.52.7 | 0.65 | tāṃ latām iva veṣṭantīm āliṅgantīṃ mahādrumān muñca muñceti bahuśaḥ pravadan rākṣasādhipaḥ | ताम् लताम् इव वेष्टन्तीम् आलिंगन्तीम् महाद्रुमान् \| मुंच मुंच इति बहुशः प्रवदन् राक्षस अधिपः  क्रोशन्तीम् राम राम इति र |
| 3.41.1 | 3.43.1 | 0.652 | sā taṃ saṃprekṣya suśroṇī kusumāni vicinvatī hemarājata varṇābhyāṃ pārśvābhyām upaśobhitam | सा तम् संप्रेक्ष्य सुश्रोणी कुसुमानि विचिन्वती \| हेम राजत वर्णाभ्याम् पार्श्वाभ्याम् उपशोभितम्  प्रहृष्टा च अनवद्यान्गी |
| 3.41.24 | 3.43.25 | 0.655 | na vane nandanoddeśe na caitrarathasaṃśraye kutaḥ pṛthivyāṃ saumitre yo 'sya kaś cit samo mṛgaḥ | पश्य लक्ष्मण वैदेह्याः स्पृहाम् उल्लसिताम् इमाम् \| रूप श्रेष्ठतया हि एष मृगो अद्य न भविष्यति  न वने नंदनोद्देशे न चैत्र |
| 3.44.22 | 3.46.23 | 0.655 | naivaṃrūpā mayā nārī dṛṣṭapūrvā mahītale iha vāsaś ca kāntāre cittam unmāthayanti me | रूपम् अग्र्यम् च लोकेषु सौकुमार्यम् वयः च ते  इह वासः च कांतारे चित्तम् उन्मथयन्ति मे \| |
| 3.59.8 | 3.61.7 | 0.655 | kāmavṛttam anāryaṃ māṃ mṛṣāvādinam eva ca dhik tvām iti pare loke vyaktaṃ vakṣyati me pitā | कथम् प्रतिज्ञाम् संश्रुत्य मया त्वम् अभियोजितः  अपूरयित्वा तम् कालम् मत् सकाशम् इह आगतः \| काम वृत्तम् अनार्यम् माम् मृष |
| 3.59.2 | 3.61.1 | 0.659 | adṛṣṭvā tatra vaidehīṃ saṃnirīkṣya ca sarvaśaḥ uvāca rāmaḥ prākruśya pragṛhya rucirau bhujau | दृष्ट्वा आश्रम पदम् शून्यम् रामो दशरथ आत्मजः \| रहिताम् पर्णशालाम् च प्रविद्धानि आसनानि च  अदृष्ट्वा तत्र वैदेहीम् संनिर |
| 3.15.29 | 3.16.31 | 0.662 | padmapatrekṣaṇaḥ śyāmaḥ śrīmān nirudaro mahān dharmajñaḥ satyavādī ca hrī niṣedho jitendriyaḥ | पद्मपत्रेक्षणः श्यामः श्रीमान् निरुदरो महान् \| धर्मज्ञः सत्यवादी च ह्री निषेधो जितेन्द्रियः  प्रियाभिभाषी मधुरो दीर्घबा |
| 3.23.17 | 3.24.19 | 0.67 | tato devāḥ sagandharvāḥ siddhāś ca saha cāraṇaiḥ ūcuḥ paramasaṃtrastā guhyakāś ca parasparam | ततो देवाः सगन्धर्वाः सिद्धाः च सह चारणैः \| समेयुः च महात्मनो युद्ध दर्शन कांक्षया |
| 3.32.3 | 3.34.3 | 0.695 | āyudhaṃ kiṃ ca rāmasya nihatā yena rākṣasāḥ kharaś ca nihataṃ saṃkhye dūṣaṇas triśirās tathā | आयुधम् किम् च रामस्य येन ते राक्षसाः हता \| खरः च निहतः संख्ये दूषणः त्रिशिराः तथा  तत् त्वम् ब्रूहि मनोज्ञान्गी केन त्व |
| 3.41.23 | 3.43.48 | 0.706 | paśya lakṣmaṇa vaidehyāḥ spṛhāṃ mṛgagatām imām rūpaśreṣṭhatayā hy eṣa mṛgo 'dya na bhaviṣyati | पश्य लक्ष्मण वैदेहीम् मृग त्वचि गताम् स्पृहाम्  त्वचा प्रधानया हि एष मृगो अद्य न भविष्यति \| |

### Critical-only verses — 561, sample of 30 (present in Baroda critical, absent from Southern)

| Locus | Text |
|---|---|
| 3.1.3 | śaraṇyaṃ sarvabhūtānāṃ susamṛṣṭājiraṃ sadā pūjitaṃ copanṛttaṃ ca nityam apsarasāṃ gaṇaiḥ |
| 3.1.4 | viśālair agniśaraṇaiḥ srugbhāṇḍair ajinaiḥ kuśaiḥ samidbhis toyakalaśaiḥ phalamūlaiś ca śobhitam |
| 3.1.6 | puṣpair vanyaiḥ parikṣiptaṃ padminyā ca sapadmayā phalamūlāśanair dāntaiś cīrakṛṣṇājināmbaraiḥ |
| 3.1.7 | sūryavaiśvānarābhaiś ca purāṇair munibhir vṛtam puṇyaiś a niyatāhāraiḥ śobhitaṃ paramarṣibhiḥ |
| 3.1.8 | tad brahmabhavanaprakhyaṃ brahmaghoṣanināditam brahmavidbhir mahābhāgair brāhmaṇair upaśobhitam |
| 3.1.9 | tad dṛṣṭvā rāghavaḥ śrīmāṃs tāpasāśramamaṇḍalam abhyagacchan mahātejā vijyaṃ kṛtvā mahad dhanuḥ |
| 3.1.11 | te taṃ somam ivodyantaṃ dṛṣṭvā vai dharmacāriṇaḥ maṅgalāni prayuñjānāḥ pratyagṛhṇan dṛḍhavratāḥ |
| 3.1.16 | mūlaṃ puṣpaṃ phalaṃ vanyam āśramaṃ ca mahātmanaḥ nivedayītvā dharmajñās tataḥ prāñjalayo 'bruvan |
| 3.1.20 | nyastadaṇḍā vayaṃ rājañ jitakrodhā jitendriyāḥ rakṣitavyās tvayā śaśvad garbhabhūtās tapodhanāḥ |
| 3.1.21 | evam uktvā phalair mūlaiḥ puṣpair vanyaiś ca rāghavam anyaiś ca vividhāhāraiḥ salakṣmaṇam apūjayan |
| 3.2.2 | nānāmṛgagaṇākīrṇaṃ śārdūlavṛkasevitam dhvastavṛkṣalatāgulmaṃ durdarśa salilāśayam |
| 3.2.3 | niṣkūjanānāśakuni jhillikā gaṇanāditam lakṣmaṇānugato rāmo vanamadhyaṃ dadarśa ha |
| 3.2.4 | vanamadhye tu kākutsthas tasmin ghoramṛgāyute dadarśa giriśṛṅgābhaṃ puruṣādaṃ mahāsvanam |
| 3.2.6 | vasānaṃ carmavaiyāghraṃ vasārdraṃ rudhirokṣitam trāsanaṃ sarvabhūtānāṃ vyāditāsyam ivāntakam |
| 3.2.10 | aṅgenādāya vaidehīm apakramya tato 'bravīt yuvāṃ jaṭācīradharau sabhāryau kṣīṇajīvitau |
| 3.2.11 | praviṣṭau daṇḍakāraṇyaṃ śaracāpāsidhāriṇau kathaṃ tāpasayor vāṃ ca vāsaḥ pramadayā saha |
| 3.3.8 | taṃ rāmaḥ pratyuvācedaṃ kopasaṃraktalocanaḥ rākṣasaṃ vikṛtākāraṃ virādhaṃ pāpacetasaṃ |
| 3.3.11 | dhanuṣā jyāguṇavatā saptabāṇān mumoca ha rukmapuṅkhān mahāvegān suparṇānilatulyagān |
| 3.3.16 | sa bhagnabāhuḥ saṃvigno nipapātāśu rākṣasaḥ dharaṇyāṃ meghasaṃkāśo vajrabhinna ivācalaḥ |
| 3.3.20 | tadā prakṛtim āpanno bhavān svargaṃ gamiṣyati iti vaiśravaṇo rājā rambhāsaktam uvāca ha |
| 3.3.21 | anupasthīyamāno māṃ saṃkruddho vyajahāra ha tava prasādān mukto 'ham abhiśāpāt sudāruṇāt |
| 3.3.22 | ito vasati dharmātmā śarabhaṅgaḥ pratāpavān adhyardhayojane tāta maharṣiḥ sūryasaṃnibhaḥ |
| 3.3.23 | taṃ kṣipram abhigaccha tvaṃ sa te śreyo vidhāsyati avaṭe cāpi māṃ rāma nikṣipya kuśalī vraja |
| 3.3.26 | taṃ muktakaṇṭham utkṣipya śaṅkukarṇaṃ mahāsvanam virādhaṃ prākṣipac chvabhre nadantaṃ bhairavasvanam |
| 3.4.3 | āśramaṃ śarabhaṅgasya rāghavo 'bhijagāma ha |
| 3.4.5 | vibhrājamānaṃ vapuṣā sūryavaiśvānaropamam asaṃspṛśantaṃ vasudhāṃ dadarśa vibudheśvaram |
| 3.4.6 | suprabhābharaṇaṃ devaṃ virajo 'mbaradhāriṇam tadvidhair eva bahubhiḥ pūjyamānaṃ mahātmabhiḥ |
| 3.4.7 | haribhir vājibhir yuktam antarikṣagataṃ ratham dadarśādūratas tasya taruṇādityasaṃnibham |
| 3.4.8 | pāṇḍurābhraghanaprakhyaṃ candramaṇḍalasaṃnibham apaśyad vimalaṃ chatraṃ citramālyopaśobhitam |
| 3.4.9 | cāmaravyajane cāgrye rukmadaṇḍe mahādhane gṛhīte vananārībhyāṃ dhūyamāne ca mūrdhani |

### Southern-only verses — 726, sample of 30 (in the vulgate, absent from critical)

| Locus | Text (Devanāgarī) |
|---|---|
| 3.1.3 | शरण्यं सर्वभूतानां सुसंमृष्टाजिरं सद \| मृगैर्बहुभिराकीर्णं पक्षिसंमैः समातम् |
| 3.1.4 | पूजितं चोपनृत्तं च नित्यमप्सरसाम् गणैः \| विशालैरग्निशरणैः स्रुग्भाण्डैरजिनैः कुशैः  समिद्भिस्तोयकलशैः फलमूलश्च शोभितम् \| आरण्यैः च महा वृक्षैः पुण्यैः |
| 3.1.7 | फलमूलाशनैर्दान्तैस्चीरकृष्णाजिनाम्बरैः \| सूर्यवैश्वानराभश्च पुराणैर्मुनिभिर्युतम् |
| 3.1.8 | पुण्यैश्च नियताहारैः शोभितं परमर्षिभिः \| तद् ब्रह्मभवनप्रख्यां ब्रह्मघोषनिनादितम् |
| 3.1.9 | ब्रह्मविर्भिर्महाभागैर्ब्राह्मणैरुपशोभितम् \| तद्दृष्ट्वा राघवः श्रीमांस्तापसाश्रममण्डलम्  अभ्यगच्छन्महातेजा विज्यं कृत्वा महद्धनुः \| |
| 3.1.11 | ते तु सोममिवोद्यन्तं द्इष्ट्वा वै धर्मचारिणम्  लक्ष्मणं चैव दृष्ट्वातु वैदेहीं च यशस्विनीम् \| मङ्गलानि प्रयञ्जानाः प्रत्यगृह्णान् दृढव्रताः |
| 3.1.17 | मङ्गलानि प्रयुञ्जना मुदा परमया युताः \| मूलं पुष्पं फलं सर्वमाश्रमं च महात्मनः  निवेदयित्वा ध्र्मज्ञास्ते तु प्राञ्जलयोऽब्रुवन् \| |
| 3.1.21 | न्यस्तदण्डा वयं राजञ्जितक्रोधा जित्रेन्द्रियाः \| रक्षणीयास्त्वया श्श्वद्गर्भभूतास्तपोधनाः |
| 3.1.22 | एवमुक्त्वा फलैर्मुलैह् पुष्पैरन्यैश्च राघवम् \| वन्यैश्च विविधाहारैः सलक्ष्मणमपूजयन् |
| 3.2.2 | नाना मृग गण आकीर्णम् ऋक्ष शार्दूल सेवितम् \| ध्वस्त वृक्ष लता गुल्मम् दुर्दर्श सलिलाशयम्  निष्कूजमाना शकुनि झिल्लिका गण नादितम् \| लक्ष्मण अनुचरोओ रामो  |
| 3.2.4 | सीताया सह काकुत्स्थः तस्मिन् घोर मृग आयुते \| ददर्श गिरि शृङ्ग आभम् पुरुषादम् महास्वनम् |
| 3.2.6 | वसानम् चर्म वैयाघ्रम् वस आर्द्रम् रुधिरोक्षितम् \| त्रासनम् सर्व भूतानाम् व्यादितास्यम् इव अन्तकम् |
| 3.2.10 | युवाम् जटा चीर धरौ सभार्यौ क्षीण जीवितौ  प्रविष्टौ दण्डकारण्यम् शर चाप असि पाणिनौ \| |
| 3.2.11 | कथम् तापसयोः युवाम् च वासः प्रमदया सह  अधर्म चारिणौ पापौ कौ युवाम् मुनि दूषकौ \| |
| 3.3.8 | तम् रामः प्रति उवाच इदम् कोप संरक्त लोचनः \| राक्षसम् विकृत आकारम् विराधम् पाप चेतसम् |
| 3.3.11 | धनुषा ज्या गुणवता सप्त बाणान् मुमोच ह \| रुक्म पुंखान् महावेगान् सुपर्ण अनिल तुल्य गान् |
| 3.3.13 | स विद्धो न्यस्य वैदेहीम् शूलम् उद्यंय राक्षसः \| अभ्यद्रवत् सुसंक्रुद्धः तदा रामम् स लक्ष्मणम् |
| 3.3.15 | अथ तौ भ्रातरौ दीप्तम् शर वर्षम् ववर्षतुः \| विराधे राक्षसे तस्मिन् कालांतक अयम् उपमे |
| 3.3.16 | स प्रहस्य महा रौद्रः स्थित्वा अजृम्भत राक्षसः \| जृंभमाणस्य ते बाणाः कायात् निष्पेतुर् अशुगाः |
| 3.3.17 | स्पर्शात् तु वर दानेन प्राणान् संरोध्य राक्षसः \| विराधः शूलम् उद्यंय राघवौ अभ्यधावत |
| 3.3.19 | तत् राम विशिखैः छिन्नम् शूलम् तस्य आपतत् भुविः \| पपात अशनिना चिन्नम् मेरोर् इव शिला तलम् |
| 3.3.20 | तौ खड्गौ क्षिप्रम् उद्यंय कृष्ण सर्पौ इव उद्यतौ \| तूर्णम् आपेततुः तस्य तदा प्रहारताम् बलात् |
| 3.3.21 | स वध्यमान सुभृशम् भुजाभ्याम् परिगृह्य तौ \| अप्रकंप्यौ नरव्याघ्रौ रौद्रः प्रस्थातुम् ऐच्छत |
| 3.3.22 | तस्य अभिप्रायम् अज्ञाय रामो लक्ष्मणम् अब्रवीत् \| वहतु अयम् अलम् तावत् पथानेन तु राक्षसः |
| 3.3.23 | यथा च इच्छति सौमित्रे तथा वहतु राक्षसः \| अयम् एव हि नः पन्था येन याति निशाचरः |
| 3.3.24 | स तु स्व बल वीर्येण समुत्क्षिप्य निशाचरः \| बालाः इव स्कन्ध गतौ चकार अति बलोद्धतः |
| 3.3.25 | तौ आरोप्य ततः स्कन्धम् राघवो रजनी चरः \| विराधो विनदन् घोरम् जगाम अभिमुखो वनम् |
| 3.3.26 | वनम् महा मेघ निभम् प्रविष्टो द्रुमैः महद्भिः विविधैः उपेतम् \| नाना विधैः पक्षि कुलैः विचित्रम् शिव आयुतम् व्याल मृगैः विकीर्णम् |
| 3.4.1 | ह्रियमाणौ तु काकुत्स्थौ दृष्ट्वा सीता रघूत्तमौ \| उच्चैः स्वरेण चुक्रोश प्रगृह्य सु महाभुजौ |
| 3.4.2 | एष दाशरथी रामः सत्यवान् शीलवान् शुचिः \| रक्षसा रौद्र रूपेण ह्रियते सह लक्ष्मणः |

## Kiṣkindhākāṇḍa (IV)

Critical 1987 verses vs Southern 2312 verses. 34 identical, 1379 aligned-but-different, 574 critical-only, 820 southern-only.

### Major differences (sim < 0.6) — 21 pairs, showing up to 60

| Critical locus | Southern locus | sim | Critical text | Southern text |
|---|---|---:|---|---|
| 4.20.2 | 4.20.1 | 0.4 | sā samāsādya bhartāraṃ paryaṣvajata bhāminī iṣuṇābhihataṃ dṛṣṭvā vālinaṃ kuñjaropamam | राम चाप विसृष्टेन शरेण अंतकरेण तम् \| दृष्ट्वा विनिहतम् भूमौ तारा ताराधिप आनना  सा समासाद्य भर्तारम् पर्यष्वजत भामिनी \| |
| 4.51.13 | 4.52.13 | 0.448 | teṣām api hi sarveṣām anumānam upāgatam gacchāmaḥ praviśāmeti bhartṛkāryatvarānvitāḥ | साधु अत्र प्रविशाम इति मया तु उक्ताः प्लवंगमाः \| तेषाम् अपि हि सर्वेषाम् अनुमानम् उपागतम् |
| 4.23.4 | 4.23.4 | 0.468 | sugrīva eva vikrānto vīra sāhasika priya ṛkṣavānaramukhyās tvāṃ balinaṃ paryupāsate | सुग्रीवस्य वशम् प्राप्तो विधिः एष भवत्य अहो \| सुग्रीव एव विक्रांतो वीर साहसिक प्रिय |
| 4.1.22 | 4.1.47 | 0.469 | nūnaṃ paravaśā sītā sāpi śocaty ahaṃ yathā śyāmā padmapalāśākṣī mṛdubhāṣā ca me priyā | वसन्तो यदि तत्र अपि यत्र मे वसति प्रिया \| नूनम् परवशा सीता सा अपि शोच्यति अहम् यथा |
| 4.19.26 | 4.19.26 | 0.475 | rāmaṃ rāmānujaṃ caiva bhartuś caivānujaṃ śubhā tān atītya samāsādya bhartāraṃ nihataṃ raṇe | तान् अतीत्य समासाद्य भर्तारम् निहतम् रणे \| समीक्ष्य व्यथिता भूमौ संभ्रांता निपपात ह |
| 4.26.7 | 4.27.32 | 0.482 | udayābhyuditaṃ dṛṣṭvā śaśāṅkaṃ ca viśeṣataḥ āviveśa na taṃ nidrā niśāsu śayanaṃ gatam | आविवेश न तम् निद्रा निशासु शयनम् गतम् \| तत् समुत्थेन शोकेन बाष्प उपहत चेतसम् |
| 4.42.29 | 4.43.29 | 0.487 | krauñcaṃ girim atikramya maināko nāma parvataḥ mayasya bhavanaṃ tatra dānavasya svayaṃ kṛtam | स च सर्वैः विचेतव्यः स सानु प्रस्थ भूधरः \| क्रौन्चम् गिरिम् अतिक्रम्य मैनाको नाम पर्वतः |
| 4.39.23 | 4.40.24 | 0.489 | rāmasya dayitāṃ bhāryāṃ sītāṃ daśarataḥ snuṣām samudram avagāḍhāṃś ca parvatān pattanāni ca | सर्वम् च तत् विचेतव्यम् मार्गयद्भिः ततः ततः \| रामस्य दयिताम् भार्याम् सीताम् दशरथः स्नुषाम् |
| 4.51.14 | 4.52.14 | 0.489 | tato gāḍhaṃ nipatitā gṛhya hastau parasparam idaṃ praviṣṭāḥ sahasā bilaṃ timirasaṃvṛtam | अस्मिन् निपतिताः सर्वे अपि अथ कार्य त्वरान्विताः \| ततो गाढम् निपतिता गृह्य हस्तौ परस्परम् |
| 4.19.28 | 4.19.28 | 0.492 | ruroda sā patiṃ dṛṣṭvā saṃditaṃ mṛtyudāmabhiḥ tām avekṣya tu sugrīvaḥ krośantīṃ kurarīm iva | ताम् अवेक्ष्य तु सुग्रीवः क्रोशन्तीम् कुररीम् इव \| विषादम् अगमत् कष्टम् दृष्ट्वा च अंगदम् आगतम् |
| 4.58.25 | 4.59.24 | 0.5 | śrūyatāṃ tat pravakṣyāmi bhavatāṃ pauruṣāśrayam vāṅmatibhyāṃ hi sārveṣāṃ kariṣyāmi priyaṃ hi vaḥ | वाक् मतिभ्याम् हि सार्वेषाम् करिष्यामि प्रियम् हि वः  यत् हि दाशरथेः कार्यम् मम तत् न अत्र संशयः \| |
| 4.6.3 | 4.6.4 | 0.503 | tvayā viyuktā rudatī lakṣmaṇena ca dhīmatā antaraṃ prepsunā tena hatvā gṛdhraṃ jaṭāyuṣam | अन्तरम् प्रेप्सुना तेन हत्वा गृध्रम् जटायुषम् \| भार्या वियोगजम् दुःखम् प्रापितः तेन रक्ष्सा |
| 4.40.37 | 4.41.38 | 0.503 | sarparājo mahāghoro yasyāṃ vasati vāsukiḥ niryāya mārgitavyā ca sā ca bhogavatī purī | निर्याय मार्गितव्या च सा च भोगवती पुरी  तत्र च अंतरोद्देशा ये केचन समावृताः \| |
| 4.55.20 | 4.56.23 | 0.503 | bhrātur jaṭāyuṣas tasya janasthānanivāsinaḥ tasyaiva ca mama bhrātuḥ sakhā daśarathaḥ katham | तस्य एव च मम भ्रातुः सखा दशरथः कथम्  यस्य रामः प्रियः पुत्रो ज्येष्ठो गुरु जन प्रियः \| |
| 4.64.24 | 4.65.24 | 0.503 | tasmāt kalatravat tāta pratipālyaḥ sadā bhavān api caitasya kāryasya bhavān mūlam ariṃdama | अपि वै एतस्य कार्यस्य भवान् मूलम् अरिम् दम \| तस्मात् कलत्रवत् तात प्रतिपाल्यः सदा भवान् |
| 4.6.7 | 4.6.9 | 0.526 | anumānāt tu jānāmi maithilī sā na saṃśayaḥ hriyamāṇā mayā dṛṣṭā rakṣasā krūrakarmaṇā | त्यज शोकम् महाबाहो ताम् कान्ताम् आनयामि ते \| ४-६-८ अनुमानात् तु जानामि मैथिली सा न संशयः \| ह्रियमाणा मया दृष्टा रक्षसा |
| 4.51.8 | 4.52.7 | 0.534 | rāvaṇaṃ sahitāḥ sarve rākṣasaṃ kāmarūpiṇam sītayā saha vaidehyā mārgadhvam iti coditāḥ | अगस्त्य चरिताम् आशाम् दक्षिणाम् यम रक्षिताम् \| सहैभिर्वानरैमुख्यैरङ्गदप्रमुखैर्वयम् - यद्वा - सह एभिः वानरैः मुख्यैः अं |
| 4.58.20 | 4.59.19 | 0.553 | evam uktas tato 'haṃ taiḥ siddhaiḥ paramaśobhanaiḥ sa ca me rāvaṇo rājā rakṣasāṃ prativeditaḥ | एवम् उक्तः ततो अहम् तैः सिद्धैः परम शोभनैः \| स च मे रावणो राजा रक्षसाम् प्रतिवेदितः  पश्यन् दाशरथेः भार्याम् रामस्य जनक |
| 4.3.3 | 4.3.3 | 0.557 | svakaṃ rūpaṃ parityajya bhikṣurūpeṇa vānaraḥ ābabhāṣe ca tau vīrau yathāvat praśaśaṃsa ca | ततः च हनुमान् वाचा श्लक्ष्णया सुमनोज्ञया \| विनीतवत् उपागम्य राघवौ प्रणिपत्य च  अबभाषे च तौ वीरौ यथावत् प्रशशंस च \| |
| 4.38.2 | 4.39.2 | 0.585 | yad indro varṣate varṣaṃ na tac citraṃ bhaved bhuvi ādityo vā sahasrāṃśuḥ kuryād vitimiraṃ nabhaḥ | यत् इन्द्रो वर्षते वर्षम् न तत् चित्रम् भविष्यति \| आदित्यो असौ सहस्रांशुः कुर्यात् वितिमिरम् नभः  चन्द्रमा रजनीम् कुर्य |
| 4.37.24 | 4.11.73 | 0.599 | evam uktas tu sugrīvo rāmaṃ vacanam abravīt | एवम् उक्त्वा तु सुग्रीवो रामम् रक्तान्त लोचनम् \| ध्यत्वा मुहूर्तम् काकुत्स्थम् पुनरेव वचो अब्रवीत् |

### Minor edits (sim 0.6–0.9) — 162 pairs, sample of 40

| Critical locus | Southern locus | sim | Critical text | Southern text |
|---|---|---:|---|---|
| 4.4.13 | 4.4.15 | 0.606 | sa jñāsyati mahāvīryas tava bhāryāpahāriṇam evam uktvā danuḥ svargaṃ bhrājamāno gataḥ sukham | दनुः नाम दितेः पुत्रः शापात् राक्षसताम् गतः \| आख्यातः तेन सुग्रीवः समर्थो वानराधिपः  स ज्ञास्यति महावीर्यः तव भार्या अप |
| 4.63.24 | 4.64.22 | 0.608 | bruvadhvaṃ yasya yā śaktir gamane plavagarṣabhāḥ | न हि वो गमने संगः कदाचित् अपि कस्यचित् भवेत् \| ब्रुवध्वम् यस्य या शक्तिः प्लवने प्लवगर्षभाः |
| 4.11.14 | 4.11.14 | 0.61 | taṃ bhītam iti vijñāya samudram asurottamaḥ himavadvanam āgacchac charaś cāpād iva cyutaḥ | तम् भीतम् इति विज्ञाय समुद्रम् असुरोत्तमः \| हिमवद् वनम् आगम्य शरः चापाद् इव च्युतः  ततः तस्य गिरेः श्वेता गजेन्द्र प्रत |
| 4.48.2 | 4.49.2 | 0.615 | vanāni girayo nadyo durgāṇi gahanāni ca daryo giriguhāś caiva vicitā naḥ samantataḥ | वनानि गिरयो नद्यो दुर्गाणि गहनानि च \| दरी गिरि गुहाः चैव विचिता नः समंततः  तत्र तत्र सह अस्माभिः जानकी न च दृश्यते \| त |
| 4.49.14 | 4.50.15 | 0.62 | nūnaṃ salilavān atra kūpo vā yadi vā hradaḥ tathā ceme biladvāre snigdhās tiṣṭhanti pādapāḥ | अस्मात् च अपि बिलात् हंसाः क्रौन्चाः च सह सारसैः  जल आर्द्राः चक्रवाकाः च निष्पतन्ति स्म सर्वशः \| नूनम् सलिलवान् अत्र क |
| 4.17.20 | 4.17.24 | 0.621 | viṣaye vā pure vā te yadā nāpakaromy aham na ca tvāṃ pratijāne 'haṃ kasmāt tvaṃ haṃsy akilbiṣam | विषये वा पुरे वा ते यदा पापम् करोमि अहम् \| न च त्वाम् अवजाने अहं कस्मात् त्वम् हंसि अकिल्बिषम्  फल मूल अशनम् नित्यम् वा |
| 4.64.2 | 4.65.1 | 0.626 | gajo gavākṣo gavayaḥ śarabho gandhamādanaḥ maindaś ca dvividaś caiva suṣeṇo jāmbavāṃs tathā | अथ अंगद वचः श्रुत्वा सर्वे ते वानर उत्तमाः \| स्वम् स्वम् गतौ समुत्साहम् ऊचुः तत्र यथा क्रमम्  गजो गवाक्षो गवयः शरभो गंध |
| 4.42.13 | 4.40.65 | 0.628 | lodhrapadmakaṣaṇḍeṣu devadāruvaneṣu ca rāvaṇaḥ saha vaidehya mārgitavyas tatas tataḥ | तस्य शलस्य पृष्ठेषु निर्झरेषु गुहासु च \| रावणः सह वैदेह्या मार्गतव्या ततः ततः |
| 4.40.23 | 4.41.21 | 0.629 | siddhacāraṇasaṃghaiś ca prakīrṇaṃ sumanoharam tam upaiti sahasrākṣaḥ sadā parvasu parvasu | नाना विधैः नगैः फुल्लैः लताभिः च उपशोभितम्  देव ऋषि यक्ष प्रवरैः अप्सरोभिः च सेवितम् \| सिद्ध चारण संघैः च प्रकीर्णम् सु |
| 4.17.12 | 4.17.14 | 0.63 | sa dṛṣṭvā rāghavaṃ vālī lakṣmaṇaṃ ca mahābalam abravīt praśritaṃ vākyaṃ paruṣaṃ dharmasaṃhitam | तम् दृष्ट्वा राघवम् वाली लक्ष्मणम् च महाबलम् \| अब्रवीत् परुषम् वाक्यम् प्रश्रितम् धर्म संहितम्  स भूमौ अल्पतेजोसुः निहत |
| 4.45.14 | 4.46.21 | 0.63 | idānīṃ me smṛtaṃ rājan yathā vālī harīśvaraḥ mataṅgena tadā śapto hy asminn āśramamaṇḍale | इदानीम् मे स्मृतम् राजन् यथा वाली हरीश्वरः  मतंगेन तदा शप्तो हि अस्मिन् आश्रम मण्डले \| प्रविशेत् यदि वै वाली मूर्धा अस् |
| 4.4.6 | 4.4.8 | 0.631 | rājā daśaratho nāma dyutimān dharmavatsalaḥ tasyāyaṃ pūrvajaḥ putro rāmo nāma janaiḥ śrutaḥ | अग्निष्टोमादिभिः यज्ञैः इष्टवान् आप्त दक्षिणैः \| तस्य अयम् पूर्वजः पुत्रो रामो नाम जनैः श्रुतः |
| 4.40.36 | 4.41.36 | 0.632 | tatra bhogavatī nāma sarpāṇām ālayaḥ purī viśālarathyā durdharṣā sarvataḥ parirakṣitā | तत्र भोगवती नाम सर्पाणाम् आलयः पुरी  विशाल रथ्या दुर्धर्षा सर्वतः परिरक्षिता \| रक्षिता पन्नगैः घोरैः तीष्क्ण दम्ष्ट्रैः |
| 4.42.46 | 4.43.45 | 0.633 | strīṇāṃ yāny anurūpāṇi puruṣāṇāṃ tathaiva ca sarvartusukhasevyāni phalanty anye nagottamāḥ | मुक्ता वैदूर्य चित्राणि भूषणानि तथैव च \| स्त्रीणाम् यानि अनुरूपाणि पुरुषाणाम् तथैव च  सर्व ऋतु सुख सेव्यानि फलन्ति अन्य |
| 4.52.29 | 4.53.21 | 0.634 | tīkṣṇaḥ prakṛtyā sugrīvaḥ priyāsaktaś ca rāghavaḥ adṛṣṭāyāṃ ca vaidehyāṃ dṛṣṭvāsmāṃś ca samāgatān | तीक्ष्णः प्रकृत्या सुग्रीवः प्रिया रक्तः च राघवः \| समीक्ष्य अकृत कार्यान् तु तस्मिन् च समये गते  अदृष्टायाम् च वैदेह्या |
| 4.57.34 | 4.58.36 | 0.636 | punaḥ pratyānayitvā vai taṃ deśaṃ patageśvaram babhūvur vānarā hṛṣṭāḥ pravṛttim upalabhya te | ततो नीत्वा तु तम् देशम् तीरे नद नदी पतेः \| निर्दग्ध पक्षम् संपातिम् वानराः सुमहौओजसः  तम् पुनः प्रत्यानयित्वा वै तम् दे |
| 4.5.14 | 4.5.13 | 0.639 | tato hanūmān saṃtyajya bhikṣurūpam ariṃdamaḥ kāṣṭhayoḥ svena rūpeṇa janayām āsa pāvakam | ततो हनूमान् संत्यज्य भिक्षु रूपम् अरिन्दमः  काष्ठयोः स्वेन रूपेण जनयामास पावकम् \| दीप्यमानम् ततो वह्निम् पुष्पैः अभ्यर् |
| 4.55.1 | 4.56.1 | 0.64 | upaviṣṭās tu te sarve yasmin prāyaṃ giristhale harayo gṛdhrarājaś ca taṃ deśam upacakrame | उपविष्टाः तु ते सर्वे यस्मिन् प्रायम् गिरि स्थले \| हरयो गृध्र राजः च तम् देशम् उपचक्रमे  सांपातिः नाम नाम्ना तु चिर जीव |
| 4.17.15 | 4.17.17 | 0.641 | sānukrośo mahotsāhaḥ samayajño dṛḍhavrataḥ iti te sarvabhūtāni kathayanti yaśo bhuvi | कुलीनः सत्त्व संपन्नः तेजस्वी चरितव्रतः \| रामः करुणवेदी च प्रजानाम् च हितेरतः  सानुक्रोशो महोत्साहः समयज्ञो दृढव्रतः \| |
| 4.55.14 | 4.56.15 | 0.641 | rāmalakṣmaṇayor vāsām araṇye saha sītayā rāghavasya ca bāṇena vālinaś ca tathā vadhaḥ | राम लक्ष्मणयोः वासाम् अरण्ये सह सीतया \| राघवस्य च बाणेन वालिनः च तथा वधः  राम कोपात् अशेषाणाम् राक्षसाम् च तथा वधम् \|  |
| 4.49.3 | 4.5.3 | 0.642 | teṣāṃ tatraiva vasatāṃ sa kālo vyatyavartata | आसेदुः तस्य शैलस्य कोटिम् दक्षिण पस्चिमाम् \| तेषाम् तत्र एव वसताम् स कालो व्यत्यवर्तत |
| 4.56.12 | 4.57.12 | 0.644 | tato mama pitṛvyeṇa sugrīveṇa mahātmanā cakāra rāghavaḥ sakhyaṃ so 'vadhīt pitaraṃ mama | ततो मम पितृव्येण सुग्रीवेण महात्मना \| चकार राघवः सख्यम् सः अवधीत् पितरम् मम  मम पित्रा विरुद्धो हि सुग्रीवः सचिवैः सह \ |
| 4.52.19 | 4.53.6 | 0.645 | sa tu siṃharṣabha skandhaḥ pīnāyatabhujaḥ kapiḥ yuvarājo mahāprājña aṅgado vākyam abravīt | ततः तान् कपि वृद्धान् च शिष्टान् चैव वनौकसः \| वाचा मधुरया अभाष्य यथावत् अनुमान्य च  स तु सिंह ऋषभ स्कंधः पीन आयत भुजः क |
| 4.56.7 | 4.57.7 | 0.645 | rājā kṛtsnasya jagata ikṣvākūṇāṃ mahārathaḥ rāmo dāśarathiḥ śrīmān praviṣṭo daṇḍakāvanam | राजा कृत्स्नस्य जगतः इक्ष्वाकूणाम् महारथः \| रामो दाशरथिः श्रीमान् प्रविष्टो दण्डका वनम्  लक्ष्मणेन सह भ्रात्रा वैदेह्या |
| 4.45.16 | 4.46.23 | 0.646 | tataḥ parvatam āsādya ṛśyamūkaṃ nṛpātmaja na viveśa tadā vālī mataṅgasya bhayāt tadā | ततः पर्वतम् आसाद्य ऋश्यमूकम् नृपात्मज  न विवेश तदा वाली मतंगस्य भयात् तदा \| एवम् मया तदा राजन् प्रत्यक्षम् उपलक्षितम् \ |
| 4.54.14 | 4.55.14 | 0.646 | ārogyapūrvaṃ kuśalaṃ vācyā mātā rumā ca me mātaraṃ caiva me tārām āśvāsayitum arhatha | आरोग्य पूर्वम् कुशलम् वाच्या माता रुमा च मे  मातरम् चैव मे ताराम् आश्वासयितुम् अर्हथ \| प्रकृत्या प्रिय पुत्रा सा सानुक् |
| 4.25.11 | 4.26.11 | 0.648 | evam uktvā hanūmantaṃ rāmaḥ sugrīvam abravīt imam apy aṅgadaṃ vīra yauvarājye 'bhiṣecaya | एवम् उक्त्वा हनूमन्तम् रामः सुग्रीवम् अब्रवीत्  वृत्तज्ञो वृत्त संपन्नम् उदार बल विक्रमम् \| |
| 4.11.43 | 4.11.62 | 0.652 | sa maharṣiṃ samāsādya yācate sma kṛtāñjaliḥ | एतत् श्रुत्वा तदा वाली वचनम् वनर ईरितम् \| स महर्षिम् समासाद्य याचते स्म कृत अंजलिः |
| 4.52.13 | 4.52.31 | 0.653 | svasti vo 'stu gamiṣyāmi bhavanaṃ vānararṣabhāḥ ity uktvā tad bilaṃ śrīmat praviveśa svayaṃprabhā | एष विन्ध्यो गिरिः श्रीमान् नाना द्रुम लता आयुतः  एष प्रसवणः शैलः सागरो अयम् महा उदधिः \| स्वस्ति वो अस्तु गमिष्यामि भवनम |
| 4.45.3 | 4.46.3 | 0.654 | yadā tu dundubhiṃ nāma dānavaṃ mahiṣākṛtim parikālayate vālī malayaṃ prati parvatam | यदा तु दुंदुभिम् नाम दानवम् महिष आकृतिम् \| परिकालयते वाली मलयम् प्रति पर्वतम्  तदा विवेश महिषो मलयस्य गुहाम् प्रति \| व |
| 4.41.36 | 4.42.41 | 0.655 | ādityam upatiṣṭhanti taiś ca sūryo 'bhipūjitaḥ adṛśyaḥ sarvabhūtānām astaṃ gacchati parvatam | विश्वेदेवाः च वसवो मरुतः च दिव ओकसः \| आगत्य पश्चिमाम् संध्याम् मेरुम् उत्तम पर्वतम्  आदित्यम् उपतिष्ठन्ति तैः च सूर्यो  |
| 4.51.5 | 4.52.4 | 0.655 | lakṣmaṇena saha bhrātrā vaidehyā cāpi bhāryayā tasya bhāryā janasthānād rāvaṇena hṛtā balāt | राजा सर्वस्य लोकस्य महेन्द्र वरुण उपमः \| रामो दाशरथिः श्रीमान् प्रविष्टो दण्डका वनम्  लक्ष्मणेन सह भ्रात्रा वैदेह्या च  |
| 4.3.6 | 4.3.7 | 0.657 | imāṃ nadīṃ śubhajalāṃ śobhayantau tarasvinau dhairyavantau suvarṇābhau kau yuvāṃ cīravāsasau | पम्पा तीर रुहान् वृक्षान् वीक्षमाणौ समंततः \| इमाम् नदीम् शुभ जलाम् शोभयन्तौ तरस्विनौ  धैर्यवन्तौ सुवर्णाभौ कौ युवाम् ची |
| 4.54.3 | 4.55.3 | 0.657 | bhrātur jyeṣṭhasya yo bhāryāṃ jīvito mahiṣīṃ priyām dharmeṇa mātaraṃ yas tu svīkaroti jugupsitaḥ | भ्रातुः ज्येष्ठस्य यो भार्याम् जीवितो महिषीम् प्रियाम् \| धर्मेण मातरम् यः तु स्वीकरोति जुगुप्सितः  कथम् स धर्मम् जानीते |
| 4.11.26 | 4.11.25 | 0.662 | tatas tu dvāram āgamya kiṣkindhāyā mahābalaḥ nanarda kampayan bhūmiṃ dundubhir dundubhir yathā | धारयन् माहिषम् रूपम् तीक्ष्ण शृङ्गो भयावहः \| प्रावृषि इव महा मेघः तोय पूर्णो नभस्तले  ततः तु द्वारम् आगम्य किष्किन्धाया |
| 4.30.10 | 4.31.10 | 0.662 | tataḥ śubhamatiḥ prājño bhrātuḥ priyahite rataḥ lakṣmaṇaḥ pratisaṃrabdho jagāma bhavanaṃ kapeḥ | ततः शुभ मतिः प्राज्ञो भ्रातुः प्रियहितेरतः \| लक्ष्मणः प्रतिसंरब्धो जगाम भवनम् कपेः  शक्र बाणासन प्रख्यम् धनुः कालांतक उ |
| 4.11.39 | 4.11.41 | 0.663 | yuddhe prāṇahare tasmin niṣpiṣṭo dundubhis tadā śrotrābhyām atha raktaṃ tu tasya susrāva pātyataḥ | वाली व्यापादयाम् चक्रे ननर्द च महास्वनम् \| श्रोत्राभ्याम् अथ रक्तम् तु तस्य सुस्राव पात्यतः |
| 4.3.20 | 4.3.22 | 0.667 | yuvābhyāṃ saha dharmātmā sugrīvaḥ sakhyam icchati tasya māṃ sacivaṃ vittaṃ vānaraṃ pavanātmajam | युवाभ्याम् स हि धर्मात्मा सुग्रीवः सख्यम् इच्छति \| तस्य माम् सचिवम् वित्तम् वानरम् पवनात्मजम्  भिक्षु रूप प्रति च्छन्नम |
| 4.33.2 | 4.34.2 | 0.669 | kruddhaṃ niḥśvasamānaṃ taṃ pradīptam iva tejasā bhrātur vyasanasaṃtaptaṃ dṛṣṭvā daśarathātmajam | क्रुद्धम् निःश्वसमानम् तम् प्रदीप्तम् इव तेजसा \| भ्रातुर् व्यसन संतप्तम् दृष्ट्वा दशरथ आत्मजम्  उत्पपात हरिश्रेष्ठो हित |
| 4.9.21 | 4.9.21 | 0.67 | rājyaṃ praśāsatas tasya nyāyato mama rāghava ājagāma ripuṃ hatvā vālī tam asurottamam | ततः अहम् तैः समागम्य समेतैः अभिषेचितः \| राज्यम् प्रशासतः तस्य न्यायतो मम राघव  आजगाम रिपुम् हत्वा दानवम् स तु वानरः \| |

### Critical-only verses — 574, sample of 30 (present in Baroda critical, absent from Southern)

| Locus | Text |
|---|---|
| 4.1.6 | sukhānilo 'yaṃ saumitre kālaḥ pracuramanmathaḥ gandhavān surabhir māso jātapuṣpaphaladrumaḥ |
| 4.1.9 | mārutaḥ sukhaṃ saṃsparśe vāti candanaśītalaḥ ṣaṭpadair anukūjadbhir vaneṣu madhugandhiṣu |
| 4.1.15 | vimiśrā vihagāḥ pumbhir ātmavyūhābhinanditāḥ bhṛṅgarājapramuditāḥ saumitre madhurasvarāḥ |
| 4.1.17 | śikhinībhiḥ parivṛtā mayūrā girisānuṣu manmathābhiparītasya mama manmathavardhanāḥ |
| 4.1.21 | vadanti rāvaṃ muditāḥ śakunāḥ saṃghaśaḥ kalam āhvayanta ivānyonyaṃ kāmonmādakarā mama |
| 4.1.27 | saumitre paśya pampāyāś citrāsu vanarājiṣu nalināni prakāśante jale taruṇasūryavat |
| 4.1.28 | eṣā prasannasalilā padmanīlotpalāyatā haṃsakāraṇḍavākīrṇā pampā saugandhikāyutā |
| 4.1.29 | cakravākayutā nityaṃ citraprasthavanāntarā mātaṅgamṛgayūthaiś ca śobhate salilārthibhiḥ |
| 4.1.35 | pampātīraruhāś ceme saṃsaktā madhugandhinaḥ mālatīmallikāṣaṇḍāḥ karavīrāś ca puṣpitāḥ |
| 4.1.37 | ciribilvā madhūkāś ca vañjulā bakulās tathā campakās tilakāś caiva nāgavṛkṣāś ca puṣpitāḥ |
| 4.1.38 | nīpāś ca varaṇāś caiva kharjūrāś ca supuṣpitāḥ aṅkolāś ca kuraṇṭāś ca cūrṇakāḥ pāribhadrakāḥ |
| 4.1.39 | cūtāḥ pāṭalayaś caiva kovidārāś ca puṣpitāḥ mucukundārjunāś caiva dṛśyante girisānuṣu |
| 4.1.40 | ketakoddālakāś caiva śirīṣāḥ śiṃśapā dhavāḥ śālmalyaḥ kiṃśukāś caiva raktāḥ kurabakās tathā |
| 4.1.43 | paśya śītajalāṃ cemāṃ saumitre puṣkarāyutām cakravākānucaritāṃ kāraṇḍavaniṣevitām |
| 4.1.44 | adhikaṃ śobhate pampāvikūjadbhir vihaṃgamaiḥ |
| 4.1.47 | evaṃ sa vilapaṃs tatra śokopahatacetanaḥ avekṣata śivāṃ pampāṃ ramyavārivahāṃ śubhām |
| 4.1.49 | tāv ṛṣyamūkaṃ sahitau prayātau; sugrīvaśākhāmṛgasevitaṃ tam trastās tu dṛṣṭvā harayo babhūvur; mahaujasau rāghavalakṣmaṇau tau |
| 4.2.7 | tataḥ sugrīvasacivā dṛṣṭvā paramadhanvinau jagmur giritaṭāt tasmād anyac chikharam uttamam |
| 4.2.13 | tatas taṃ bhayasaṃtrastaṃ vālikilbiṣaśaṅkitam uvāca hanumān vākyaṃ sugrīvaṃ vākyakovidaḥ |
| 4.2.19 | dīrghabāhū viśālākṣau śaracāpāsidhāriṇau kasya na syād bhayaṃ dṛṣṭvā etau surasutopamau |
| 4.2.24 | lakṣayasva tayor bhāvaṃ prahṛṣṭamanasau yadi viśvāsayan praśaṃsābhir iṅgitaiś ca punaḥ punaḥ |
| 4.2.25 | mamaivābhimukhaṃ sthitvā pṛccha tvaṃ haripuṃgava prayojanaṃ praveśasya vanasyāsya dhanurdharau |
| 4.3.2 | sa tatra gatvā hanumān balavān vānarottamaḥ upacakrāma tau vāgbhir mṛdvībhiḥ satyavikramaḥ |
| 4.3.4 | rājarṣidevapratimau tāpasau saṃśitavratau deśaṃ katham imaṃ prāptau bhavantau varavarṇinau |
| 4.3.5 | trāsayantau mṛgagaṇān anyāṃś ca vanacāriṇaḥ pampātīraruhān vṛkṣān vīkṣamāṇau samantataḥ |
| 4.3.7 | siṃhaviprekṣitau vīrau siṃhātibalavikramau śakracāpanibhe cāpe pragṛhya vipulair bhujaiḥ |
| 4.3.8 | śrīmantau rūpasaṃpannau vṛṣabhaśreṣṭhavikramau hastihastopamabhujau dyutimantau nararṣabhau |
| 4.3.9 | prabhayā parvatendro 'yaṃ yuvayor avabhāsitaḥ rājyārhāv amaraprakhyau kathaṃ deśam ihāgatau |
| 4.3.10 | padmapatrekṣaṇau vīrau jaṭāmaṇḍaladhāriṇau anyonyasadṛśau vīrau devalokād ivāgatau |
| 4.3.11 | yadṛcchayeva saṃprāptau candrasūryau vasuṃdharām viśālavakṣasau vīrau mānuṣau devarūpiṇau |

### Southern-only verses — 820, sample of 30 (in the vulgate, absent from critical)

| Locus | Text (Devanāgarī) |
|---|---|
| 4.1.3 | सौमित्रे शोभते पम्पा वैदूर्य विमल उदका \| फुल्ल पद्म उत्पलवती शोभिता विविधैः द्रुमैः |
| 4.1.6 | शोकार्तस्य अपि मे पम्पा शोभते चित्र कानना \| व्यवकीर्णा बहु विधैः पुष्पैः शीतोदका शिवा |
| 4.1.7 | नलिनैः अपि संछन्ना हि अत्यर्थ शुभ दर्शना \| सर्प व्याल अनुचरिता मृग द्विज समाकुला |
| 4.1.9 | पुष्प भार समृद्धानि शिखराणि समन्ततः \| लताभिः पुष्पित अग्राभिः उपगूढानि सर्वतः |
| 4.1.10 | सुख अनिलोऽयम् सौमित्रे कालः प्रचुर मन्मथः \| गन्धवान् सुरभिर् मासो जात पुष्प फल द्रुमः |
| 4.1.13 | पतितैः पतमानैः च पादपस्थैः च मारुतः \| कुसुमैः पश्य सौमित्रे क्रीडतीव समन्ततः |
| 4.1.14 | विक्षिपन् विविधाः शाखा नगानाम् कुसुमोत्कटाः \| मारुतः चलित स्थानैः षट्पदैः अनुगीयते |
| 4.1.15 | मत्त कोकिल सन्नादैः नर्तयन् इव पादपान् \| शैल कन्दर निष्क्रान्तः प्रगीत इव च अनिलः |
| 4.1.16 | तेन विक्षिपता अत्यर्थम् पवनेन समन्ततः \| अमी संसक्त शाखाग्रा ग्रथिता इव पादपाः |
| 4.1.17 | स एव सुख संस्पर्शो वाति चन्दन शीतलः \| गन्धम् अभ्यवहन् पुण्यम् श्रम अपनयो अनिलः |
| 4.1.18 | अमी पवन विक्षिप्ता विनन्दन्ती इव पादपाः \|षट्पदैः अनुकूजद्भिः वनेषु मधु गन्धिषु |
| 4.1.20 | पुष्प संछन्न शिखरा मारुतः उत्क्षेप चंचला \| अमी मधुकरोत्तंसाः प्रगीत इव पादपाः |
| 4.1.25 | श्रुत्वा एतस्य पुरा शब्दम् आश्रमस्था मम प्रिया \| माम् आहूय प्रमुदिता परमम् प्रत्यनन्दत |
| 4.1.26 | एवम् विचित्राः पतगा नाना राव विराविणः \| वृक्ष गुल्म लताः पश्य संपतन्ति समन्ततः |
| 4.1.27 | विमिश्रा विहगाः पुंभिः आत्म व्यूह अभिनन्दिताः \| भृङ्गराज प्रमुदिताः सौमित्रे मधुर स्वराः |
| 4.1.29 | अशोक स्तबक अङ्गारः षट्पद स्वन निस्वनः  माम् हि पल्लव ताम्रार्चिः वसन्ताग्निः प्रधक्ष्यति \| |
| 4.1.30 | न हि ताम् सूक्ष्मपक्ष्माक्षीम् सुकेशीम् मृदु भाषिणीम्  अपश्यतो मे सौउमित्रे जीवितेऽस्ति प्रयोजनम् \| |
| 4.1.31 | अयम् हि रुचिरः तस्याः कालो रुचिर काननः  कोकिलाकुल सीमान्तः दयिताया मम अनघः \| |
| 4.1.32 | मन्मध आयास संभूतो वसन्त गुण वर्धितः  अयम् माम् धक्ष्यति क्षिप्रम् शोकाग्निः न चिरादिव \| |
| 4.1.33 | अपश्यत ताम् वनिताम् पश्यतो रुचिर द्रुमान्  मम अयम् आत्मप्रभवो भूयस्त्वम् उपयास्यति \| |
| 4.1.34 | अदृश्यमाना वैदेही शोकम् वर्धयती इह मे  दृश्यमानो वसन्तः च स्वेद संसर्ग दूषकः \| |
| 4.1.36 | अमी मयूराः शोभन्ते प्रनृत्यन्तः ततः ततः  स्त्वैः पक्षैः पवन उद्धूतैः गवाक्षैः स्फाटिकैः इव \| |
| 4.1.37 | शिखिनीभिः परिवृतास्त एते मद मूर्छिताः  मन्मथ अभिपरीतस्य मम मन्मथ वर्धनाः \| |
| 4.1.39 | ताम् एव मनसा रामाम् मयुरोऽपि अनुधावति  वितत्य रुचिरौ पक्षौ रुतैः उपहसन् इव \| |
| 4.1.41 | मम त्वयम् विना वासः पुष्पमासे सुदुःसहः  पश्य लक्ष्मण संरागः तिर्यक् योनिगतेषु अपि \| यदेषा शिखिनी कामात् भर्तारम् अभिवर्तते |
| 4.1.43 | माम् अपि एवम् विशालाक्षी जानकी जात संभ्रमा \| मदनेन अभिवर्तेत यदि न अपहृता भवेत् |
| 4.1.45 | रुचिराणि अपि पुष्पाणि पादपानाम् अतिश्रिया \| निष्फलानि महीम् यान्ति समम् मधुकरोत्करैः |
| 4.1.46 | नदन्ति कावम् मुदिताः शकुना सङ्घशः कलम् \| आह्वयन्त इव अन्योन्यम् काम उन्मादकरा मम |
| 4.1.48 | नूनम् न तु वसन्तः तम् देशम् स्पृशति यत्र सा \| कथम् हि असित पद्माक्षी वर्तयेत् सा मया विना |
| 4.1.49 | अथवा वर्तते तत्र वसन्तो यत्र मे प्रिया \| किम् करिष्यति सुश्रोणी सा तु निर् भर्त्सिता परैः |

## Full data

Complete machine-readable results per book: `bala_alignment.json`, `ayodhya_alignment.json`, `aranya_alignment.json`, `kishkindha_alignment.json` (alongside this file).
