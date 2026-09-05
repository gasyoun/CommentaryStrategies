_Created: 12-07-2026 · Last updated: 05-09-2026_

# Bālakāṇḍa (I): Critical (GRETIL/Baroda) vs Gita Supersite

_Created: 12-07-2026_

> Critical vs Gita Supersite. Content-aligned via difflib LCS + fuzzy character-4gram-Jaccard
> rescue (word-boundary-robust -- Gita Supersite text does not consistently space-separate
> sandhi-joined words), canonicalized via `sanskrit_util.nfold`.
> Replaces the earlier valmikiramayan.net-based comparison (rights-cleared source now used).

## ✅ Rights status

Both sources are properly licensed: Gita Supersite text is used under the CC BY 4.0 grant
from Sudalaimuthu Palaniappan (`CommentaryStrategies/data/valmiki_PERMISSION.md`). This
supersedes the earlier valmikiramayan.net-based comparison, which had no permission on file.

## Summary

| Critical verses | Gita Supersite verses | Identical | Variant pairs | near-id (≥.9) | minor (.6-.9) | major (<.6) | Critical-only | Gita Supersite-only |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1941 | 2045 | 21 | 1759 | 1423 | 248 | 88 | 161 | 265 |

## Major differences (sim < 0.6) — 88 pairs, showing up to 60

| Critical locus | Gita Supersite locus | sim | Critical text | Gita Supersite text |
|---|---|---:|---|---|
| 1.51.5 | 1.52.10 | 0.376 | viśvāmitro mahātejā vanaspatigaṇe tathā sarvatra kuśalaṃ cāha vasiṣṭho rājasattamam | सर्वत्र कुशलं राजा वसिष्ठं प्रत्युदाहरत्। विश्वामित्रो महातेजा वसिष्ठं विनयान्वित:।।1.52.10।। |
| 1.72.17 | 1.73.25 | 0.39 | abravīj janako rājā kausalyānandavardhanam iyaṃ sītā mama sutā sahadharmacarī tava | ततस्सीतां समानीय सर्वाभरणभूषिताम्।।1.73.25।। समक्षमग्ने स्संस्थाप्य राघवाभिमुखे तदा। अब्रवीज्जनको राजा कौसल्यानन्दवर्धनम |
| 1.12.16 | 1.13.16 | 0.4 | yathoktaṃ tat kariṣyāmo na kiṃ cit parihāsyate tataḥ sumantram āhūya vasiṣṭho vākyam abravīt | ततस्सर्वे समागम्य वसिष्ठमिदमब्रुवन्।।1.13.16।। यथोक्तं तत्सुविहितं न किञ्चित्परिहीयते। यथोक्तं तत्करिष्यामो न किञ्चित्पर |
| 1.12.6 | 1.13.6 | 0.414 | sthāpatye niṣṭhitāṃś caiva vṛddhān paramadhārmikān karmāntikāñ śilpakārān vardhakīn khanakān api | ततोऽब्रवीद्विजान्वृद्धान्यज्ञकर्मसु निष्ठितान्। स्थापत्ये निष्ठितांश्चैव वृद्धान्परमधार्मिकान्।।1.13.6।। कर्मान्तिकान् श |
| 1.7.16 | 1.7.21 | 0.436 | avekṣamāṇaś cāreṇa prajā dharmeṇa rañjayan nādhyagacchad viśiṣṭaṃ vā tulyaṃ vā śatrum ātmanaḥ | नाध्यगच्छद्विशिष्टं वा तुल्यं वा शत्रुमात्मन: । मित्रवान्नतसामन्त: प्रतापहतकण्टक: ।।1.7.21।। स शशास जगद्राजा दिवं देवपति |
| 1.69.26 | 1.70.38 | 0.455 | dilīpo 'ṃśumataḥ putro dilīpasya bhagīrathaḥ bhagīrathāt kakutsthaś ca kakutsthasya raghus tathā | सगरस्यासमञ्जस्तु असमञ्जात्तथांऽशुमान्। दिलीपोंऽशुमत: पुत्रो दिलीपस्य भगीरथ:।।1.70.38।। |
| 1.43.18 | 1.44.19 | 0.457 | samṛddhārtho naraśreṣṭha svarājyaṃ praśaśāsa ha pramumoda ca lokas taṃ nṛpam āsādya rāghava | प्रमुमोद ह लोकस्तं नृपमासाद्य राघव। नष्टशोकस्समृद्धार्थो बभूव विगतज्वर:।।1.44.19।। |
| 1.6.15 | 1.6.16 | 0.462 | na dīnaḥ kṣiptacitto vā vyathito vāpi kaś cana kaś cin naro vā nārī vā nāśrīmān nāpy arūpavān | कश्चिन्नरो वा नारी वा नाश्रीमान्नाप्यरूपवान् । द्रष्टुं शक्यमयोध्यायां नापि राजन्यभक्तिमान् ।।1.6.16।। |
| 1.69.20 | 1.70.24 | 0.464 | vikukṣes tu mahātejā bāṇaḥ putraḥ pratāpavān bāṇasya tu mahātejā anaraṇyaḥ pratāpavān | बाणस्य तु महातेजा अनरण्य: प्रतापवान्। अनरण्यात्पृथुर्जज्ञे त्रिशङ्कुस्तु पृथोस्सुत:।।1.70.24।। |
| 1.12.13 | 1.13.13 | 0.466 | na cāvajñā prayoktavyā kāmakrodhavaśād api yajñakarmasu ye 'vyagrāḥ puruṣāḥ śilpinas tathā | सर्वे वर्णा यथा पूजां प्राप्नुवन्ति सुसत्कृता:। न चावज्ञा प्रयोक्तव्या कामक्रोधवशादपि।।1.13.13।। |
| 1.17.16 | 1.18.28 | 0.468 | rāmasya lokarāmasya bhrātur jyeṣṭhasya nityaśaḥ sarvapriyakaras tasya rāmasyāpi śarīrataḥ | सर्वप्रियकरस्तस्य रामस्यापि शरीरत:।।1.18.28।। लक्ष्मणो लक्ष्मिसम्पन्नो बहि:प्राण इवापर:। |
| 1.63.4 | 1.64.4 | 0.468 | tām uvāca sahasrākṣo vepamānāṃ kṛtāñjalim mā bhaiṣi rambhe bhadraṃ te kuruṣva mama śāsanam | एवमुक्तस्तया राम रम्भया भीतया तदा।।1.64.4।। तामुवाच सहस्राक्षो वेपमानां कृताञ्जलिम्। |
| 1.69.25 | 1.70.37 | 0.468 | saha tena gareṇaiva jātaḥ sa sagaro 'bhavat sagarasyāsamañjas tu asamañjād athāṃśumān | सपत्न्या तु गरस्तस्यै दत्तो गर्भजिघांसया। सह तेन गरेणैव जात: स सगरोऽभवत्।।1.70.37।। |
| 1.69.30 | 1.70.43 | 0.468 | nahuṣasya yayātis tu nābhāgas tu yayātijaḥ nābhāgasya bhabhūvāja ajād daśaratho 'bhavat | नाभागस्य बभूवाज: अजाद्दशरथोऽभवत्। अस्माद्दशरथाज्जातौ भ्रातरौ रामलक्ष्मणौ।।1.70.43।। |
| 1.12.4 | 1.13.5 | 0.469 | voḍhavyo bhavatā caiva bhāro yajñasya codyataḥ tatheti ca sa rājānam abravīd dvijasattamaḥ | तथेति च स राजानमब्रवीद्द्विजसत्तमः। करिष्ये सर्वमेवैतद्भवता यत्समर्थितम्।।1.13.5।। |
| 1.3.20 | 1.3.30 | 0.471 | āpānabhūmigamanam avarodhasya darśanam aśokavanikāyānaṃ sītāyāś cāpi darśanam | अशोकवनिकायानं सीतायाश्चपि दर्शनम् । अभिज्ञानप्रदानं च रावणस्य च दर्शनम् ।।1.3.30।। |
| 1.3.25 | 1.3.35 | 0.471 | pratāraṃ ca samudrasya rātrau laṅkāvarodhanam vibhīṣaṇena saṃsargaṃ vadhopāyanivedanam | विभीषणेन संसर्गं वधोपायनिवेदनम् । कुम्भकर्णस्य निधनं मेघनादनिबर्हणम् ।।1.3.35।। |
| 1.69.29 | 1.70.42 | 0.471 | maroḥ praśuśrukas tv āsīd ambarīṣaḥ praśuśrukāt ambarīṣasya putro 'bhūn nahuṣaḥ pṛthivīpatiḥ | अम्बरीषस्य पुत्रोऽभून्नहुष: पृथिवीपति:। नहुषस्य ययातिस्तु नाभागस्तु ययातिज:।।1.70.42।। |
| 1.13.24 | 1.14.29 | 0.472 | uragāḥ pakṣiṇaś caiva yathāśāstraṃ pracoditāḥ śāmitre tu hayas tatra tathā jala carāś ca ye | शामित्रे तु हयस्तत्र तथा जलचराश्च ये। ऋत्विग्भिस्सर्वमेवैतन्नियुक्तं शास्त्रतस्तदा।।1.14.29।। |
| 1.62.19 | 1.63.20 | 0.472 | brahmaṇaḥ sa vacaḥ śrutvā viśvāmitras tapodhanaḥ prāñjaliḥ praṇato bhūtvā pratyuvāca pitāmaham | प्राञ्जलि: प्रणतो भूत्वा सर्वलोकपितामहम्। प्रत्युवाच ततो वाचं विश्वामित्रो महामुनि:।।1.63.20।। |
| 1.44.18 | 1.45.32 | 0.474 | atha dhanvantarir nāma apsarāś ca suvarcasaḥ apsu nirmathanād eva rasāt tasmād varastriyaḥ | अप्सु निर्मथनादेव रसास्तस्माद्वरस्त्रिय:। उत्पेतुर्मनुजश्रेष्ठ तस्मादप्सरसोऽभवन्।।1.45.32।। |
| 1.72.24 | 1.73.37 | 0.474 | puṣpavṛṣṭir mahaty āsīd antarikṣāt subhāsvarā divyadundubhinirghoṣair gītavāditranisvanaiḥ | काकुत्स्थैश्च गृहीतेषु ललितेषु च पाणिषु।।1.73.37।। पुष्पवृष्टिर्महत्यासीदन्तरिक्षात्सुभास्वरा। |
| 1.26.10 | 1.27.10 | 0.475 | dadāmi cāstraṃ painākam astraṃ nārāyaṇaṃ tathā āgneyam astra dayitaṃ śikharaṃ nāma nāmataḥ | आग्नेयमस्त्रं दयितं शिखरं नाम नामतः।।1.27.10।। वायव्यं प्रथनं नाम ददामि च तवानघ । |
| 1.35.22 | 1.36.22 | 0.476 | evam uktvā surān sarvāñ śaśāpa pṛthivīm api avane naikarūpā tvaṃ bahubhāryā bhaviṣyasi | अद्यप्रभृति युष्माकमप्रजास्सन्तु पत्नय:।।1.36.22।। एवमुक्त्वासुरान् सर्वान् शशाप पृथिवीमपि। |
| 1.3.13 | 1.3.22 | 0.477 | rāghavasya vilāpaṃ ca gṛdhrarājanibarhaṇam kabandhadarśanaṃ caiva pampāyāś cāpi darśanam | कबन्धदर्शनं चापि पम्पायाश्चापि दर्शनम् । शबर्या: दर्शनं चैव हनूमद्दर्शनं तथा ।।1.3.22।। |
| 1.47.3 | 1.50.17 | 0.477 | padmapatraviśālākṣau khaḍgatūṇīdhanurdharau aśvināv iva rūpeṇa samupasthitayauvanau | इमौ कुमारौ भद्रं ते देवतुल्यपराक्रमौ।।1.50.17।। गजसिंहगती वीरौ शार्दूलवृषभोपमौ। पद्मपत्रविशालाक्षौ खड्गतूणीधनुर्धरौ।।1.5 |
| 1.1.47 | 1.1.58 | 0.478 | śabaryā pūjitaḥ samyag rāmo daśarathātmajaḥ pampātīre hanumatā saṃgato vānareṇa ha | पम्पातीरे हनुमता सङ्गतो वानरेण ह ।।1.1.58।। हनुमद्वचनाच्चैव सुग्रीवेण समागत: । |
| 1.73.7 | 1.74.8 | 0.48 | praviveśa svanilayaṃ mithilāṃ mithileśvaraḥ rājāpy ayodhyādhipatiḥ saha putrair mahātmabhiḥ | राजाऽप्ययोध्याधिपतिस्सह पुत्रैर्महात्मभि:। ऋषीन् सर्वान् पुरस्कृत्य जगाम सबलानुग:।।1.74.8।। |
| 1.47.2 | 1.48.2 | 0.481 | imau kumārau bhadraṃ te devatulyaparākramau gajasiṃhagatī vīrau śārdūlavṛṣabhopamau | इमौ कुमारौ भद्रं ते देवतुल्यपराक्रमौ। गजसिंहगती वीरौ शार्दूलवृषभोपमौ।।1.48.2।। पद्मपत्रविशालाक्षौ खड्गतूणी धनुर्धरौ। अश् |
| 1.27.12 | 1.28.14 | 0.482 | gamyatām iti tān āha yatheṣṭaṃ raghunandanaḥ mānasāḥ kāryakāleṣu sāhāyyaṃ me kariṣyatha | मानसा: कार्यकालेषु साहाय्यं मे करिष्यथ। गम्यतामिति तानाह यथेष्टं रघुनन्दन:।।1.28.14।। |
| 1.12.10 | 1.13.11 | 0.483 | bhakṣyānnapānair bahubhiḥ samupetāḥ suniṣṭhitāḥ tathā paurajanasyāpi kartavyā bahuvistarāḥ | तथा पौरजनस्यापि कर्तव्या बहुविस्तरा:। आवासा बहुभक्ष्या वै सर्वकामैरुपस्थिता:।।1.13.11।। |
| 1.12.14 | 1.13.15 | 0.483 | teṣām api viśeṣeṇa pūjā kāryā yathākramam yathā sarvaṃ suvihitaṃ na kiṃ cit parihīyate | यथा सर्वं सुविहितं न किञ्चित्परिहीयते।।1.13.15।। तथा भवन्त: कुर्वन्तु प्रीतिस्निग्धेन चेतसा। |
| 1.70.21 | 1.71.21 | 0.483 | sītāṃ rāmāya bhadraṃ te ūrmilāṃ lakṣmaṇāya ca vīryaśulkāṃ mama sutāṃ sītāṃ surasutopamām | वीर्यशुल्कां मम सुतां सीतां सुरसुतोपमाम्	।।1.71.21।। द्वितीयामूर्मिलां चैव त्रिर्ददामि न संशय:। |
| 1.71.5 | 1.72.5 | 0.483 | bhrātā yavīyān dharmajña eṣa rājā kuśadhvajaḥ asya dharmātmano rājan rūpeṇāpratimaṃ bhuvi | अस्य धर्मात्मनो राजन् रूपेणाप्रतिमं भुवि	। सुताद्वयं नरश्रेष्ठ पत्न्यर्थं वरयामहे।।1.72.5।। |
| 1.12.31 | 1.13.34 | 0.486 | mayāpi satkṛtāḥ sarve yathārhaṃ rājasattamāḥ yajñiyaṃ ca kṛtaṃ rājan puruṣaiḥ susamāhitaiḥ | यज्ञीयं च कृतं राजन् पुरुषैस्सुसमाहितै:। निर्यातु च भवान्यष्टुं यज्ञायतनमन्तिकात्।।1.13.34।। |
| 1.13.23 | 1.14.28 | 0.486 | garuḍo rukmapakṣo vai triguṇo 'ṣṭādaśātmakaḥ niyuktās tatra paśavas tat tad uddiśya daivatam | नियुक्तास्तत्र पशवस्तत्तदुद्दिश्य दैवतम्। उरगा: पक्षिणश्चैव यथाशास्त्रं प्रचोदिता:।।1.14.28।। |
| 1.26.17 | 1.27.17 | 0.486 | tāmasaṃ naraśārdūla saumanaṃ ca mahābalam saṃvartaṃ caiva durdharṣaṃ mausalaṃ ca nṛpātmaja | तामसं नरशार्दूल सौमनं च महाबल। संवर्धं चैव दुर्धर्षं मौसलं च नृपात्मज।।1.27.17।। सत्यमस्त्रं महाबाहो तथा मायाधरं परम्। घ |
| 1.69.9 | 1.70.11 | 0.486 | preṣayām āsatur vīrau mantriśreṣṭhaṃ sudāmanam gaccha mantripate śīghram aikṣvākam amitaprabham | गच्छ मन्त्रिपते शीघ्रमैक्ष्वाकुममितप्रभम्।।1.70.11।। आत्मजैस्सह दुर्धर्षमानयस्व समन्त्रिणम्। |
| 1.12.17 | 1.13.19 | 0.487 | nimantrayasya nṛpatīn pṛthivyāṃ ye ca dhārmikāḥ brāhmaṇān kṣatriyān vaiśyāñ śūdrāṃś caiva sahasraśaḥ | ब्राह्मणान्क्षत्रियान्वैश्याञ्छूद्रांश्चैव सहस्रश:। समानयस्व सत्कृत्य सर्वदेशेषु मानवान्।।1.13.19।। |
| 1.16.3 | 1.17.3 | 0.487 | māyāvidaś ca śūrāṃś ca vāyuvegasamāñjave nayajñān buddhisaṃpannān viṣṇutulyaparākramān | मायाविदश्च शूरांश्च वायुवेगसमाञ्जवे। नयज्ञान्बुद्धिसम्पन्नान्विष्णुतुल्यपराक्रमान्।।1.17.3।। असंहार्यानुपायज्ञान् दिव्यस |
| 1.58.7 | 1.59.7 | 0.488 | sarvāñ śiṣyān samāhūya vākyam etad uvāca ha | सर्वान् शिष्यान् समाहूय वाक्यमेतदुवाच ह। सर्वानृषिगणान्वत्सा आनयध्वं ममाज्ञया। सशिष्यसुहृदश्चैव सर्त्विज स्सबहुश्रुतान्। |
| 1.26.9 | 1.27.9 | 0.489 | vāruṇaṃ pāśam astraṃ ca dadāny aham anuttamam aśanī dve prayacchāmi śuṣkārdre raghunandana | अशनी द्वे प्रयच्छामि शुष्कार्द्रे रघुनन्दन।।1.27.9।। ददामि चास्त्रं पैनाकमस्त्रं नारायणं तथा। |
| 1.60.17 | 1.61.17 | 0.489 | mamāpi dayitaṃ viddhi kaniṣṭhaṃ śunakaṃ nṛpa | अविक्रेयं सुतं ज्येष्ठं भगवानाह भार्गव:।।1.61.17।। ममापि दयितं विद्धि कनिष्ठं शुनकं नृप। तस्मात्कनीयसं पुत्रं न दास्ये त |
| 1.5.21 | 1.5.20 | 0.491 | siṃhavyāghravarāhāṇāṃ mattānāṃ nadatāṃ vane hantāro niśitaiḥ śastrair balād bāhubalair api | ये च बाणैर्न विध्यन्ति विविक्तमपरापरम् । शब्दवेध्यं च विततं लघुहस्ता विशारदा: ।।1.5.20।। सिंहव्याघ्रवराहाणां मत्तानां नर |
| 1.12.12 | 1.13.12 | 0.491 | dātavyam annaṃ vidhivat satkṛtya na tu līlayā sarvavarṇā yathā pūjāṃ prāpnuvanti susatkṛtāḥ | तथा जानपदस्यापि जनस्य बहुशोभनम्। दातव्यमन्नं विधिवत्सत्कृत्य न तु लीलया।।1.13.12।। |
| 1.26.8 | 1.27.8 | 0.491 | pradīpte naraśārdūla prayacchāmi nṛpātmaja dharmapāśam ahaṃ rāma kālapāśaṃ tathaiva ca | धर्मपाशमहं राम कालपाशं तथैव च।।1.27.8।। पाशं वारुणमस्त्रं च ददाम्यहमनुत्तमम्। |
| 1.64.7 | 1.65.14 | 0.491 | sāgarāḥ kṣubhitāḥ sarve viśīryante ca parvatāḥ prakampate ca pṛthivī vāyur vāti bhṛśākulaḥ | प्रकम्पते च पृथिवी वायुर्वाति भृशाकुल:। बृह्मन्न प्रतिजानीमोनास्तिको जायते जन:।।1.65.14।। |
| 1.73.3 | 1.74.3 | 0.491 | atha rājā videhānāṃ dadau kanyādhanaṃ bahu gavāṃ śatasahasrāṇi bahūni mithileśvaraḥ | गच्छन्तं तं तु राजानमन्वगच्छन्नराधिप:।।1.74.3।। अथ राजा विदेहानां ददौ कन्याधनं बहु। |
| 1.26.6 | 1.27.4 | 0.492 | vajram astraṃ naraśreṣṭha śaivaṃ śūlavaraṃ tathā astraṃ brahmaśiraś caiva aiṣīkam api rāghava | दण्डचक्रं महद्दिव्यं तव दास्यामि राघव।।1.27.4।। धर्मचक्रं ततो वीर कालचक्रं तथैव च। विष्णुचक्रं तथात्युग्रमैन्द्रमस्त्रं  |
| 1.65.12 | 1.66.12 | 0.492 | prītiyuktaḥ sa sarveṣāṃ dadau teṣāṃ mahātmanām | प्रीतियुक्तस्स सर्वेषां ददौ तेषां महात्मनाम्। तदेतद्देवदेवस्य धनूरत्नं महात्मन:। न्यासभूतं तदा न्यस्तमस्माकं पूर्व के वि |
| 1.3.23 | 1.3.33 | 0.494 | grahaṇaṃ vāyusūnoś ca laṅkādāhābhigarjanam pratiplavanam evātha madhūnāṃ haraṇaṃ tathā | प्रतिप्लवनमेवाथ मधूनां हरणं तथा । राघवाश्वासनं चापि मणिनिर्यातनं तथा ।।1.3.33।। |
| 1.31.2 | 1.32.3 | 0.494 | kuśāmbaṃ kuśanābhaṃ ca ādhūrta rajasaṃ vasum dīptiyuktān mahotsāhān kṣatradharmacikīrṣayā | दीप्तियुक्तान् महोत्साहान् क्षत्रधर्मचिकीर्षया।।1.32.3।। तानुवाच कुश: पुत्रान् धर्मिष्ठान् सत्यवादिन:। |
| 1.26.12 | 1.27.12 | 0.497 | śakti dvayaṃ ca kākutstha dadāmi tava cānagha kaṅkālaṃ musalaṃ ghoraṃ kāpālam atha kaṅkaṇam | कङ्कालं मुसलं घोरं कापालमथ कङ्कणम्। धारयन्त्यसुरा यानि ददाम्येतानि सर्वशः।।1.27.12।। |
| 1.57.9 | 1.58.9 | 0.497 | atha rātryāṃ vyatītāyāṃ rājā caṇḍālatāṃ gataḥ nīlavastradharo nīlaḥ paruṣo dhvastamūrdhajaḥ | एवमुक्त्वा महात्मनो विविशुस्ते स्वमाश्रमम्।।1.58.9।। अथ रात्र्यां व्यतीतायां राजा चण्डालतां गत:। |
| 1.3.27 | 1.3.36 | 0.5 | bibhīṣaṇābhiṣekaṃ ca puṣpakasya ca darśanam ayodhyāyāś ca gamanaṃ bharatena samāgamam | रावणस्य विनाशं च सीतावाप्तिमरे: पुरे । विभीषणाभिषेकं च पुष्पकस्य च दर्शनम् ।।1.3.36।। |
| 1.15.25 | 1.16.27 | 0.5 | kausalyāyai narapatiḥ pāyasārdhaṃ dadau tadā ardhād ardhaṃ dadau cāpi sumitrāyai narādhipaḥ | कौसल्यायै नरपति: पायसार्धं ददौ तदा। अर्धादर्धं ददौ चापि सुमित्रायै नराधिप:।।1.16.27।। कैकेय्यै चावशिष्टार्धं ददौ पुत्रार |
| 1.3.11 | 1.3.20 | 0.503 | anasūyāsamasyāṃ ca aṅgarāgasya cārpaṇam śūrpaṇakhyāś ca saṃvādaṃ virūpakaraṇaṃ tathā | शूर्पणख्याश्च संवादं विरूपकरणं तथा । वधं खरत्रिशिरसोरुत्थानं रावणस्य च ।।1.3.20।। |
| 1.26.7 | 1.27.7 | 0.503 | dadāmi te mahābāho brāhmam astram anuttamam gade dve caiva kākutstha modakī śikharī ubhe | गदे द्वे चैव काकुत्स्थ मोदकी शिखरी उभे।।1.27.7।। प्रदीप्ते नरशार्दूल प्रयच्छामि नृपात्मज। |
| 1.42.5 | 1.43.9 | 0.503 | naiva sā nirgamaṃ lekhe jaṭāmaṇḍalamohitā tatraivābabhramad devī saṃvatsaragaṇān bahūn | तत्रैवाबम्भ्रमद्देवी संवत्सरगणान् बहून्।।1.43.9।। तामपश्यन्पुनस्तत्र तप: परममास्थित:। |
| 1.62.24 | 1.63.25 | 0.503 | evaṃ varṣasahasraṃ hi tapo ghoram upāgamat tasmin saṃtapyamāne tu viśvāmitre mahāmunau | तस्मिन् सन्तप्यमाने तु विश्वामित्रे महामुनौ।।1.63.25।। सम्भ्रमस्सुमहानासीत्सुराणां वासवस्य च। |

## Minor edits (sim 0.6–0.9) — 248 pairs, sample of 60

| Critical locus | Gita Supersite locus | sim | Critical text | Gita Supersite text |
|---|---|---:|---|---|
| 1.43.16 |  | 0.607 | ity evam uktvā deveśaḥ sarvalokapitāmahaḥ yathāgataṃ tathāgacchad devalokaṃ mahāyaśāḥ | इत्येवमुक्त्वा देवेश: सर्वलोकपितामह:। |
| 1.4.14 |  | 0.609 | tac chrutvā munayaḥ sarve bāṣpaparyākulekṣaṇāḥ sādhu sādhv ity tāv ūcatuḥ paraṃ vismayam āgatāḥ | ﻿तच्छ्रुत्वा मुनयस्सर्वे बाष्पपर्याकुलेक्षणा:। |
| 1.23.14 |  | 0.612 | dhavāśvakarṇakakubhair bilvatindukapāṭalaiḥ saṃkīrṇaṃ badarībhiś ca kiṃ nv idaṃ dāruṇaṃ vanam | धवाश्वकर्णककुभैर्बिल्वतिन्दुकपाटलै:। |
| 1.29.18 |  | 0.615 | imān api vadhiṣyāmi nirghṛṇān duṣṭacāriṇaḥ rākṣasān pāpakarmasthān yajñaghnān rudhirāśanān | इमानपि वधिष्यामि निर्घृणान् दुष्टचारिण:। |
| 1.24.18 |  | 0.619 | viṣṇunā ca purā rāma bhṛgupatnī dṛḍhavratā anindraṃ lokam icchantī kāvyamātā niṣūditā | विष्णुनापि पुरा राम भृगुपत्नी दृढव्रता। |
| 1.60.10 | 1.61.10 | 0.624 | deśāñ janapadāṃs tāṃs tān nagarāṇi vanāni ca āśramāṇi ca puṇyāni mārgamāṇo mahīpatiḥ | देशान् जनपदांस्तां स्तान्नगराणि वनानि च। आश्रमाणि च पुण्यानि मार्गमाणो महीपति: ।।1.61.10।। स पुत्रसहितं तात सभार्यं रघुन |
| 1.68.4 | 1.69.4 | 0.624 | vasiṣṭho vāmadevaś ca jābālir atha kāśyapaḥ mārkaṇḍeyaś ca dīrghāyur ṛṣiḥ kātyāyanas tathā | वसिष्ठो वामदेवश्च जाबालिरथ काश्यप:। मार्कण्डेयश्च दीर्घायु:ऋषि: कात्यायनस्तथा।।1.69.4।। एते द्विजा: प्रयान्त्वग्रे स्यन् |
| 1.1.69 | 1.1.86 | 0.626 | devatābhyo varān prāpya samutthāpya ca vānarān puṣpakaṃ tat samāruhya nandigrāmaṃ yayau tadā | देवताभ्यो वरं प्राप्य समुत्थाप्य च वानरान् । अयोध्यां प्रस्थितो राम: पुष्पकेण सुहृद्वृत: ।।1.1.86।। |
| 1.3.24 |  | 0.626 | rāghavāśvāsanaṃ caiva maṇiniryātanaṃ tathā saṃgamaṃ ca samudrasya nalasetoś ca bandhanam | ﻿सङ्गमं च समुद्रेण नलसेतोश्च बन्धनम् । |
| 1.76.11 | 1.77.14 | 0.626 | abhivādyābhivādyāṃś ca sarvā rājasutās tadā remire muditāḥ sarvā bhartṛbhiḥ sahitā rahaḥ | अभिवाद्याभिवाद्यांश्च सर्वा राजसुतास्तदा। स्वं स्वं गृहमथासाद्य कुबेरभवनोपमम्।।1.77.14।। गोभिर्धनैश्च धान्यैश्च तर्पयित् |
| 1.1.6 |  | 0.628 | śrutvā caitat trilokajño vālmīker nārado vacaḥ śrūyatām iti cāmantrya prahṛṣṭo vākyam abravīt | श्रुत्वा चैतत्ित्रलोकज्ञो वाल्मीकेर्नारदो वच: । |
| 1.17.34 | 1.18.51 | 0.628 | kaṃ ca te paramaṃ kāmaṃ karomi kim u harṣitaḥ pātrabhūto 'si me vipra diṣṭyā prāpto 'si dhārmika | कं च ते परमं कामं करोमि किमु हर्षित: ।।1.18.51।। |
| 1.25.2 |  | 0.628 | pitur vacananirdeśāt pitur vacanagauravāt vacanaṃ kauśikasyeti kartavyam aviśaṅkayā | पितुर्वचननिर्देशात्पितुर्वचनगौरवात्। |
| 1.2.39 |  | 0.632 | samākṣaraiś caturbhir yaḥ pādair gīto maharṣiṇā so 'nuvyāharaṇād bhūyaḥ śokaḥ ślokatvam āgataḥ | ﻿﻿समाक्षरैश्चतुर्भिर्य: पादैर्गीतो महर्षिणा । |
| 1.42.22 | 1.43.31 | 0.632 | devāḥ sarṣigaṇāḥ sarve daityadānavarākṣasāḥ gandharvayakṣapravarāḥ sakiṃnaramahoragāḥ | देवास्सर्षिगणा: सर्वे दैत्यदानवराक्षसा:।।1.43.31।। गन्धर्वयक्षप्रवरास्सकिन्नरमहोरगा:। सर्वाश्चाप्सरसो राम भगीरथरथानुगाम् |
| 1.3.15 |  | 0.634 | ṛṣyamūkasya gamanaṃ sugrīveṇa samāgamam pratyayotpādanaṃ sakhyaṃ vālisugrīvavigraham | ﻿ऋश्यमूकस्य गमनं सुग्रीवेण समागमम् । |
| 1.21.17 |  | 0.636 | kāmaṃ bahuguṇāḥ sarve tvayy ete nātra saṃśayaḥ tapasā saṃbhṛte caite bahurūpe bhaviṣyataḥ | कामं बहुगुणास्सर्वे त्वय्येते नात्र संशय:। |
| 1.71.10 |  | 0.636 | sadṛśaṃ kulasaṃbandhaṃ yad ājñāpayathaḥ svayam evaṃ bhavatu bhadraṃ vaḥ kuśadhvajasute ime | एवं भवतु भद्रं व: कुशध्वजसुते इमे। |
| 1.17.21 | 1.18.33 | 0.637 | te yadā jñānasaṃpannāḥ sarve samuditā guṇaiḥ hrīmantaḥ kīrtimantaś ca sarvajñā dīrghadarśinaḥ | ते यदा ज्ञानसम्पन्नास्सर्वैस्समुदिता गुणै:।।1.18.33।। ह्रीमन्त: कीर्तिमन्तश्च सर्वज्ञा दीर्घदर्शिन:। तेषामेवं प्रभावानां |
| 1.10.8 | 1.11.8 | 0.638 | taṃ ca rājā daśaratho yaṣṭukāmaḥ kṛtāñjaliḥ ṛṣyaśṛṅgaṃ dvijaśreṣṭhaṃ varayiṣyati dharmavit | तं च राजा दशरथो यष्टुकाम: कृताञ्जलि:। ऋश्यशृङ्गं द्विजश्रेष्ठं वरयिष्यति धर्मवित्।। 1.11.8।। यज्ञार्थं प्रसवार्थं च स्वर |
| 1.52.3 | 1.53.3 | 0.638 | uṣṇāḍhyasyaudanasyāpi rāśayaḥ parvatopamāḥ mṛṣṭānnāni ca sūpāś ca dadhikulyās tathaiva ca | उष्णाढ्यस्योदनस्यात्र राशय: पर्वतोपमा:। मृष्टान्नानि च सूपाश्च दधिकुल्यास्तथैव च।।1.53.3।। नानास्वादुरसानां च षाडबानां त |
| 1.54.2 | 1.55.2 | 0.638 | tasyā humbhāravāj jātāḥ kāmbojā ravisaṃnibhāḥ ūdhasas tv atha saṃjātāḥ pahlavāḥ śastrapāṇayaḥ | तस्याहुम्भारवाज्जाता: काम्भोजा रविसन्निभा:। ऊधसस्त्वथ सञ्जाता: पप्लवाश्शस्त्रपाणय:।।1.55.2।। योनिदेशाच्च यवनाश्शकृद्देशा |
| 1.62.7 | 1.63.7 | 0.638 | ity uktā sā varārohā tatrāvāsam athākarot tapaso hi mahāvighno viśvāmitram upāgataḥ | इत्युक्ता सा वरारोहा तत्र वासमथाकरोत्।।1.63.7।। तस्यां वसन्त्यां वर्षाणि पञ्च पञ्च च राघव । विश्वामित्राश्रमे राम सुखेन  |
| 1.1.61 | 1.1.76 | 0.639 | astreṇonmuham ātmānaṃ jñātvā paitāmahād varāt marṣayan rākṣasān vīro yantriṇas tān yadṛcchayā | अस्त्रेणोन्मुक्तमात्मानं ज्ञात्वा पैतामहाद्वरात् । मर्षयन्राक्षसान्वीरो यन्त्रिणस्तान्यदृच्छया ।।1.1.76।। ततो दग्ध्वा पु |
| 1.39.7 | 1.40.7 | 0.64 | parikrāntā mahī sarvā sattvavantaś ca sūditāḥ devadānavarakṣāṃsi piśācoragakiṃnarāḥ | परिक्रान्ता मही सर्वा सत्त्ववन्तश्च सूदिता:।।1.40.7।। देवदानवरक्षांसि पिशाचोरगकिन्नरा:। न च पश्यामहेऽश्वं तमश्वहर्तारमेव |
| 1.28.20 | 1.29.31 | 0.641 | kumārāv api tāṃ rātrim uṣitvā susamāhitau prabhātakāle cotthāya viśvāmitram avandatām | कुमारावपि तां रात्रिमुषित्वा सुसमाहितौ। प्रभातकाले चोत्थाय पूर्वां सन्ध्यामुपास्य च।।1.29.31।। स्पृष्टोदकौ शुची जप्यं सम |
| 1.54.5 | 1.55.5 | 0.642 | dṛṣṭvā niṣūditaṃ sainyaṃ vasiṣṭhena mahātmanā viśvāmitrasutānāṃ tu śataṃ nānāvidhāyudham | दृष्ट्वा निषूदितं सैन्यं वसिष्ठेन महात्मना। विश्वामित्रसुतानां च शतं नानाविधायुधम्।।1.55.5।। अभ्यधावत्सुसङ्कृद्धं वसिष्ठ |
| 1.47.23 | 1.48.24 | 0.643 | gautamaṃ sa dadarśātha praviśanti mahāmunim devadānavadurdharṣaṃ tapobalasamanvitam | गौतमं तं ददर्शाथ प्रविशन्तं महामुनिम्। देवदानवदुर्धर्षं तपोबलसमन्वितम्।।1.48.24।। तीर्थेंदकपरिक्लिन्नं दीप्यमानमिवानलम्। |
| 1.1.66 | 1.1.81 | 0.644 | tena gatvā purīṃ laṅkāṃ hatvā rāvaṇam āhave abhyaṣiñcat sa laṅkāyāṃ rākṣasendraṃ vibhīṣaṇam | तेन गत्वा पुरीं लङ्कां हत्वा रावणमाहवे । राम: सीतामनुप्राप्य परां व्रीडामुपागमत् ।।1.1.81।। |
| 1.69.2 | 1.70.2 | 0.644 | bhrātā mama mahātejā yavīyān atidhārmikaḥ kuśadhvaja iti khyātaḥ purīm adhyavasac chubhām | भ्राता मम महातेजा यवीयानतिधार्मिक:। कुशध्वज इति ख्यात: पुरीमध्यवसच्छुभाम्।।1.70.2।। वार्याफलकपर्यन्तां पिबन्निक्षुमतीं न |
| 1.1.25 | 1.1.28 | 0.645 | paurair anugato dūraṃ pitrā daśarathena ca śṛṅgaverapure sūtaṃ gaṅgākūle vyasarjayat | पौरैरनुगतो दूरं पित्रा दशरथेन च ।।1.1.28।। शृङ्गिबेरपुरे सूतं गङ्गाकूले व्यसर्जयत् । गुहमासाद्य धर्मात्मा निषादाधिपतिं प |
| 1.63.3 | 1.64.3 | 0.645 | ayaṃ surapate ghoro viśvāmitro mahāmuniḥ krodham utsrakṣyate ghoraṃ mayi deva na saṃśayaḥ | अयं सुरपते घोरो विश्वामित्रो महामुनि:। घोरमुत्सृजते क्रोधं मयि देव न संशय:।।1.64.3।। ततो हि मे भयं देव प्रासादं कर्तुमर् |
| 1.17.33 | 1.18.49 | 0.646 | yathāmṛtasya saṃprāptir yathā varṣam anūdake yathā sadṛśadāreṣu putrajanmāprajasya ca | यथाऽमृतस्य सम्प्राप्तिर्यथावर्षमनूदके। यथा सदृशदारेषु पुत्रजन्माऽप्रजस्य च ।।1.18.49।। प्रणष्टस्य यथालाभो यथा हर्षो महोद |
| 1.47.28 | 1.48.29 | 0.646 | tathā śaptvā sa vai śakraṃ bhāryām api ca śaptavān iha varṣasahasrāṇi bahūni tvaṃ nivatsyasi | तथा शप्त्वा स वै शक्रमहल्यामपि शप्तवान्।।1.48.29।। इह वर्षसहस्राणि बहूनि त्वं निवत्स्यसि। वायुभक्षा निराहारा तप्यन्ती भस |
| 1.71.22 | 1.72.23 | 0.646 | suvarṇaśṛṅgāḥ saṃpannāḥ savatsāḥ kāṃsyadohanāḥ gavāṃ śatasahasrāṇi catvāri puruṣarṣabhaḥ | सुवर्णश्रुङ्गा स्सम्पन्ना स्सवत्सा: कांस्यदोहना:। गवां शतसहस्राणि चत्वारि पुरुषर्षभ:।।1.72.23।। वित्तमन्यच्च सुबहुद्विजे |
| 1.1.73 | 1.1.92 | 0.647 | na vātajaṃ bhayaṃ kiṃ cin nāpsu majjanti jantavaḥ na cāgrijaṃ bhayaṃ kiṃ cid yathā kṛtayuge tathā | न चाग्निजं भयं किञ्चिन्नाप्सु मज्जन्ति जन्तव: । न वातजं भयं किञ्चिन्नापि ज्वरकृतं तथा ।।1.1.92।। न चापि क्षुद्भयं तत्र न |
| 1.5.20 |  | 0.647 | ye ca bāṇair na vidhyanti viviktam aparāparam śabdavedhyaṃ ca vitataṃ laghuhastā viśāradāḥ | ﻿ये च बाणैर्न विध्यन्ति विविक्तमपरापरम् । |
| 1.49.3 | 1.50.3 | 0.647 | bahūnīha sahasrāṇi nānādeśanivāsinām brāhmaṇānāṃ mahābhāga vedādhyayanaśālinām | बहूनीह सहस्राणि नानादेशनिवासिनाम्। ब्राह्मणानां महाभाग वेदाध्ययनशालिनाम्।।1.50.3।। ऋषिवाटाश्च दृश्यन्ते शकटीशतसङ्कुला:।  |
| 1.7.4 | 1.7.5 | 0.648 | śrīmantaś ca mahātmānaḥ śāstrajñā dṛḍhavikramāḥ kīrtimantaḥ praṇihitā yathā vacanakāriṇaḥ | विद्याविनीता ह्रीमन्त: कुशला नियतेन्द्रिया: । श्रीमन्तश्च महात्मानश्शास्त्रज्ञा दृढविक्रमा: ।।1.7.5।। कीर्तिमन्त: प्रणिह |
| 1.31.10 | 1.32.12 | 0.648 | tās tu yauvanaśālinyo rūpavatyaḥ svalaṃkṛtāḥ udyānabhūmim āgamya prāvṛṣīva śatahradāḥ | तास्तु यौवनशालिन्यो रूपवत्य स्स्वलङ्कृता:। उद्यानभूमिमागम्य प्रावृषीव शतह्रदा:।।1.32.12।। गायन्त्यो नृत्यमानाश्च वादयन्त |
| 1.51.16 | 1.52.16 | 0.648 | phalamūlena bhagavan vidyate yat tavāśrame pādyenācamanīyena bhagavaddarśanena ca | फलमूलेन भगवन् विद्यते यत्तवाश्रमे। पाद्येनाचमनीयेन भगवद्दर्शनेन च।।1.52.16।। सर्वथा च महाप्राज्ञ पूजार्हेण सुपूजित:। गमि |
| 1.1.26 | 1.1.30 | 0.649 | te vanena vanaṃ gatvā nadīs tīrtvā bahūdakāḥ citrakūṭam anuprāpya bharadvājasya śāsanāt | ते वनेन वनं गत्वा नदीस्तीर्त्वा बहूदका: ।।1.1.30।। चित्रकूटमनुप्राप्य भरद्वाजस्य शासनात् । रम्यमावसथं कृत्वा रममाणा वने  |
| 1.12.19 | 1.13.20 | 0.649 | niṣṭhitaṃ sarvaśāstreṣu tathā vedeṣu niṣṭhitam tam ānaya mahābhāgaṃ svayam eva susatkṛtam | मिथिलाधिपतिं शूरं जनकं सत्यविक्रमम्। निष्ठितं सर्वशास्त्रेषु तथा वेदेषु निष्ठितम्।।1.13.20।। तमानय महाभागं स्वयमेव सुसत् |
| 1.43.17 | 1.44.17 | 0.649 | bhagīratho 'pi rājarṣiḥ kṛtvā salilam uttamam yathākramaṃ yathānyāyaṃ sāgarāṇāṃ mahāyaśāḥ | भगीरथोऽपि राजर्षि: कृत्वा सलिलमुत्तमम्। यथाक्रमं यथान्यायं सागराणां महायशा:।।1.44.17।। कृतोदकश्शुची राजा स्वपुरं प्रविवे |
| 1.51.4 | 1.52.4 | 0.649 | pratigṛhya ca tāṃ pūjāṃ vasiṣṭhād rājasattamaḥ tapo'gnihotraśiṣyeṣu kuśalaṃ paryapṛcchata | प्रतिगृह्य तु तां पूजां वसिष्ठाद्राजसत्तम:। तपोग्निहोत्रशिष्येषु कुशलं पर्यपृच्छत।।1.52.4।। विश्वामित्रो महातेजा वनस्पति |
| 1.53.23 | 1.54.23 | 0.65 | tato 'strāṇi mahātejā viśvāmitro mumoca ha | ततोऽस्त्राणि महातेजा विश्वामित्रो मुमोच ह। तैस्तैर्यवनकाम्भोजा: पप्लवाश्चाकुलीकृता:।।1.54.23।। |
| 1.1.17 |  | 0.651 | viṣṇunā sadṛśo vīrye somavat priyadarśanaḥ kālāgnisadṛśaḥ krodhe kṣamayā pṛthivīsamaḥ | विष्णुना सदृशो वीर्ये सोमवत्प्रियदर्शनः । |
| 1.2.35 |  | 0.651 | yāvat sthāsyanti girayaḥ saritaś ca mahītale tāvad rāmāyaṇakathā lokeṣu pracariṣyati | ﻿यावत् स्थास्यन्ति गिरयस्सरितश्च महीतले । |
| 1.59.27 | 1.60.28 | 0.652 | sargo 'stu saśarīrasya triśaṅkor asya śāśvataḥ nakṣatrāṇi ca sarvāṇi māmakāni dhruvāṇy atha | स्वर्गोऽस्तु सशरीरस्य त्रिशङ्कोरस्य शाश्वत:। नक्षत्राणि च सर्वाणि मामकानि ध्रुवाण्यथ।।1.60.28।। यावल्लोका धरिष्यन्ति तिष |
| 1.1.24 | 1.1.26 | 0.653 | sarvalakṣaṇasaṃpannā nārīṇām uttamā vadhūḥ sītāpy anugatā rāmaṃ śaśinaṃ rohiṇī yathā | रामस्य दयिता भार्या नित्यं प्राणसमा हिता ।।1.1.26।। जनकस्य कुले जाता देवमायेव निर्मिता । सर्वलक्षणसम्पन्ना नारीणामुत्तमा |
| 1.39.24 | 1.40.24 | 0.653 | dadṛśuḥ kapilaṃ tatra vāsudevaṃ sanātanam hayaṃ ca tasya devasya carantam avidūrataḥ | ते तु सर्वे महात्मानो भीमवेगा महाबला:।।1.40.24।। ददृशु: कपिलं तत्र वासुदेवं सनातनम्। हयं च तस्य देवस्य चरन्तमविदूरत:।।1. |
| 1.6.16 | 1.6.17 | 0.654 | varṇeṣv agryacaturtheṣu devatātithipūjakāḥ dīrghāyuṣo narāḥ sarve dharmaṃ satyaṃ ca saṃśritāḥ | वर्णेष्वग्र्यचतुर्थेषु देवतातिथिपूजका:। कृतज्ञाश्च वदान्याश्च शूरा विक्रमसंयुता: ।।1.6.17।। दीर्घायुषो नरास्सर्वे धर्मं  |
| 1.23.24 | 1.24.25 | 0.654 | kasya cit tv atha kālasya yakṣī vai kāmarūpiṇī balaṃ nāgasahasrasya dhārayantī tadā hy abhūt | कस्यचित्त्वथ कालस्य यक्षी वै कामरूपिणी। बलं नागसहस्रस्य धारयन्ती तदा ह्यभूत्।।1.24.25।। ताटका नाम भद्रं ते भार्या सुन्दस |
| 1.39.16 | 1.40.16 | 0.654 | tataḥ pūrvāṃ diśaṃ bhittvā dakṣiṇāṃ bibhiduḥ punaḥ dakṣiṇasyām api diśi dadṛśus te mahāgajam | तत: पूर्वां दिशं भित्त्वा दक्षिणां बिभिदु: पुन:।।1.40.16।। दक्षिणस्यामपि दिशि ददृशुस्ते महागजम्। महापद्मं महात्मानं सुमह |
| 1.75.9 | 1.76.9 | 0.654 | varāyudhadharaṃ rāma draṣṭuṃ sarṣigaṇāḥ surāḥ pitāmahaṃ puraskṛtya sametās tatra saṃghaśaḥ | वरायुधधरं रामं द्रष्टुं सर्षिगणा स्सुरा:। पितामहं पुरस्कृत्य समेतास्तत्र सङ्घश:।।1.76.9।। गन्धर्वाप्सरसश्चैव सिद्धचारणकि |
| 1.3.22 |  | 0.656 | maṇipradānaṃ sītāyā vṛkṣabhaṅgaṃ tathaiva ca rākṣasīvidravaṃ caiva kiṃkarāṇāṃ nibarhaṇam | ﻿﻿﻿राक्षसीविद्रवं चैव किङ्कराणां निबर्हणम् । |
| 1.47.5 | 1.50.20 | 0.656 | bhūṣayantāv imaṃ deśaṃ candrasūryāv ivāmbaram parasparasya sadṛśau pramāṇeṅgitaceṣṭitaiḥ | वरायुधधरौ वीरौ कस्य पुत्रौ महामुने।।1.50.20।। भूषयन्ताविमं देशं चन्द्रसूर्याविवाम्बरम्। परस्परस्य सदृशौ प्रमाणेङ्गितचेष् |
| 1.50.1 | 1.51.1 | 0.656 | tasya tadvacanaṃ śrutvā viśvāmitrasya dhīmataḥ hṛṣṭaromā mahātejāḥ śatānando mahātapāḥ | तस्य तद्वचनं श्रुत्वा विश्वामित्रस्य धीमत:। हृष्टरोमा महातेजाश्शतानन्दो महातपा:।।1.51.1।। गौतमस्य सुतो ज्येष्ठस्तपसा द्य |
| 1.2.32 | 1.2.33 | 0.657 | rahasyaṃ ca prakāśaṃ ca yad vṛttaṃ tasya dhīmataḥ rāmasya saha saumitre rākṣasānāṃ ca sarvaśaḥ | रहस्यं च प्रकाशं च यद्वृत्तं तस्य धीमत: । रामस्य सहसौमित्रेः राक्षसानां च सर्वश: ।।1.2.33।। वैदेह्याश्चैव यद्वृत्तं प्रक |
| 1.47.6 | 1.48.5 | 0.657 | kimarthaṃ ca naraśreṣṭhau saṃprāptau durgame pathi varāyudhadharau vīrau śrotum icchāmi tattvataḥ | भूषयन्ताविमं देशं चन्द्रसूर्याविवाम्बरम्। परस्परस्य सदृशौ प्रमाणेङ्गितचेष्टितै:।।1.48.5।। किमर्थं च मुनिश्रेष्ठ सम्प्राप |

## Critical-only — 161, sample of 30

| Locus | Text |
|---|---|
| 1.1.18 | dhanadena samas tyāge satye dharma ivāparaḥ tam evaṃguṇasaṃpannaṃ rāmaṃ satyaparākramam |
| 1.1.27 | ramyam āvasathaṃ kṛtvā ramamāṇā vane trayaḥ devagandharvasaṃkāśās tatra te nyavasan sukham |
| 1.1.45 | kabandhaṃ nāma rūpeṇa vikṛtaṃ ghoradarśanam taṃ nihatya mahābāhur dadāha svargataś ca saḥ |
| 1.1.62 | tato dagdhvā purīṃ laṅkām ṛte sītāṃ ca maithilīm rāmāya priyam ākhyātuṃ punar āyān mahākapiḥ |
| 1.1.68 | tathā paramasaṃtuṣṭaiḥ pūjitaḥ sarvadaivataiḥ kṛtakṛtyas tadā rāmo vijvaraḥ pramumoda ha |
| 1.2.33 | vaidehyāś caiva yad vṛttaṃ prakāśaṃ yadi vā rahaḥ tac cāpy aviditaṃ sarvaṃ viditaṃ te bhaviṣyati |
| 1.3.14 | śarbaryā darśanaṃ caiva hanūmaddarśanaṃ tathā vilāpaṃ caiva pampāyāṃ rāghavasya mahātmanaḥ |
| 1.3.19 | parvatārohaṇaṃ caiva sāgarasya ca laṅghanam rātrau laṅkāpraveśaṃ ca ekasyāpi vicintanam |
| 1.3.26 | kumbhakarṇasya nidhanaṃ meghanādanibarhaṇam rāvaṇasya vināśaṃ ca sītāvāptim areḥ pure |
| 1.4.7 | pāṭhye geye ca madhuraṃ pramāṇais tribhir anvitam jātibhiḥ saptabhir yuktaṃ tantrīlayasamanvitam |
| 1.4.8 | hāsyaśṛṅgārakāruṇyaraudravīrabhayānakaiḥ bībhatsādirasair yuktaṃ kāvyam etad agāyatām |
| 1.4.9 | tau tu gāndharvatattvajñau sthāna mūrcchana kovidau bhrātarau svarasaṃpannau gandharvāv iva rūpiṇau |
| 1.4.10 | rūpalakṣaṇasaṃpannau madhurasvarabhāṣiṇau bimbād ivoddhṛtau bimbau rāmadehāt tathāparau |
| 1.4.12 | ṛṣīṇāṃ ca dvijātīnāṃ sādhūnāṃ ca samāgame yathopadeśaṃ tattvajñau jagatus tau samāhitau |
| 1.5.22 | tādṛśānāṃ sahasrais tām abhipūrṇāṃ mahārathaiḥ purīm āvāsayām āsa rājā daśarathas tadā |
| 1.6.1 | puryāṃ tasyām ayodhyāyāṃ vedavit sarvasaṃgrahaḥ dīrghadarśī mahātejāḥ paurajānapadapriyaḥ |
| 1.6.2 | ikṣvākūṇām atiratho yajvā dharmarato vaśī maharṣikalpo rājarṣis triṣu lokṛṣu viśrutaḥ |
| 1.6.3 | balavān nihatāmitro mitravān vijitendriyaḥ dhanaiś ca saṃcayaiś cānyaiḥ śakravaiśravaṇopamaḥ |
| 1.6.4 | yathā manur mahātejā lokasya parirakṣitā tathā daśaratho rājā vasañ jagad apālayat |
| 1.6.22 | añjanād api niṣkrāntair vāmanād api ca dvipaiḥ bhadramandrair bhadramṛgair mṛgamandraiś ca sā purī |
| 1.6.23 | nityamattaiḥ sadā pūrṇā nāgair acalasaṃnibhaiḥ sā yojane ca dve bhūyaḥ satyanāmā prakāśate |
| 1.7.5 | tejaḥkṣamāyaśaḥprāptāḥ smitapūrvābhibhāṣiṇaḥ krodhāt kāmārthahetor vā na brūyur anṛtaṃ vacaḥ |
| 1.8.4 | tato 'bravīd idaṃ rājā sumantraṃ mantrisattamam śīghram ānaya me sarvān gurūṃs tān sapurohitān |
| 1.9.8 | ṛṣiputrasya ghorasya nityam āśramavāsinaḥ pituḥ sa nityasaṃtuṣṭo nāticakrāma cāśramāt |
| 1.9.32 | evaṃ sa nyavasat tatra sarvakāmaiḥ supūjitaḥ ṛṣyaśṛṅgo mahātejāḥ śāntayā saha bhāryayā |
| 1.10.9 | yajñārthaṃ prasavārthaṃ ca svargārthaṃ ca nareśvaraḥ labhate ca sa taṃ kāmaṃ dvija mukhyād viśāṃ patiḥ |
| 1.11.6 | suyajñaṃ vāmadevaṃ ca jābālim atha kāśyapam purohitaṃ vasiṣṭhaṃ ca ye cānye dvijasattamāḥ |
| 1.12.1 | punaḥ prāpte vasante tu pūrṇaḥ saṃvatsaro 'bhavat abhivādya vasiṣṭhaṃ ca nyāyataḥ pratipūjya ca |
| 1.12.3 | yathā na vighnaḥ kriyate yajñāṅgeṣu vidhīyatām bhavān snigdhaḥ suhṛn mahyaṃ guruś ca paramo bhavān |
| 1.12.5 | kariṣye sarvam evaitad bhavatā yat samarthitam tato 'bravīd dvijān vṛddhān yajñakarmasu niṣṭhitān |

## Gita Supersite-only — 265, sample of 30

| Locus | Text |
|---|---|
| 1.1.13 | प्रजापतिसमश्श्रीमान् धाता रिपुनिषूदनः । रक्षिता जीवलोकस्य धर्मस्य परिरक्षिता ।।1.1.13।। |
| 1.1.30 | ते वनेन वनं गत्वा नदीस्तीर्त्वा बहूदका: ।।1.1.30।। |
| 1.1.34 | स जगाम वनं वीरो रामपादप्रसादक: ।। 1.1.34 ।। |
| 1.1.35 | गत्वा तु सुमहात्मानं रामं सत्यपराक्रमम् । अयाचद्भ्रातरं राममार्यभावपुरस्कृत: ।।1.1.35।। त्वमेव राजा धर्मज्ञ इति रामं वचोऽब्रवीत् । |
| 1.1.36 | रामोऽपि परमोदारस्सुमुखस्सुमहायशा: । न चैच्छत्पितुरादेशाद्राज्यं रामो महाबल: ।।1.1.36।। |
| 1.1.44 | स तेषां प्रतिशुश्राव राक्षसानां तथा वने ।।1.1.44।। प्रतिज्ञातश्च रामेण वधस्संयति रक्षसाम् । ऋषीणामग्निकल्पानां दण्डकारण्यवासिनाम् ।।1.1.45।। |
| 1.1.57 | सोऽभ्यगच्छन्महातेजाश्शबरीं शत्रुसूदन: ।।1.1.57।। शबर्या पूजितस्सम्यग्रामो दशरथात्मज: । |
| 1.1.60 | सुग्रीवश्चापि तत्सर्वं श्रुत्वा रामस्य वानर: ।।1.1.60।। चकार सख्यं रामेण प्रीतश्चैवाग्निसाक्षिकम् । |
| 1.1.63 | सुग्रीवश्शङ्कितश्चासीन्नित्यं वीर्येण राघवे ।।1.1.63।। राघवप्रत्ययार्थं तु दुन्दुभे: कायमुत्तमम् । दर्शयामास सुग्रीवो महापर्वतसन्निभम् ।।1.1.64।। |
| 1.1.69 | अनुमान्य तदा तारां सुग्रीवेण समागत: । निजघान च तत्रैनं शरेणैकेन राघव: ।।1.1.69।। |
| 1.1.82 | तामुवाच ततो राम: परुषं जनसंसदि । अमृष्यमाणा सा सीता विवेश ज्वलनं सती ।।1.1.82।। |
| 1.1.83 | ततोऽग्निवचनात्सीतां ज्ञात्वा विगतकल्मषाम् । बभौ रामस्सम्प्रहृष्ट: पूजितस्सर्वदैवतै: ।।1.1.83।। |
| 1.1.85 | अभिषिच्य च लङ्कायां राक्षसेन्द्रं विभीषणम् । कृतकृत्यस्तदा रामो विज्वर: प्रमुमोद ह ।।1.1.85।। |
| 1.1.87 | भरद्वाजाश्रमं गत्वा रामस्सत्यपराक्रम: । भरतस्यान्तिकं रामो हनूमन्तं व्यसर्जयत् ।।1.1.87।। |
| 1.1.88 | पुनराख्यायिकां जल्पन्सुग्रीवसहितश्च स: । पुष्पकं तत्समारुह्य नन्दिग्रामं ययौ तदा ।।1.1.88।। |
| 1.1.93 | नगराणि च राष्ट्राणि धनधान्ययुतानि च ।।1.1.93।। नित्यं प्रमुदितास्सर्वे यथा कृतयुगे तथा । |
| 1.2.43 | तदुपगतसमाससन्धियोगं सममधुरोपनतार्थवाक्यबद्धम् । रघुवरचरितं मुनिप्रणीतं दशशिरसश्च वधं निशामयध्वम् ।।1.2.43।। |
|  | ﻿रामलक्ष्मणसीताभी राज्ञा दशरथेन च । |
| 1.3.5 | स्त्रीतृतीयेन च तदा यत्प्राप्तं चरता वने । सत्यसन्धेन रामेण तत्सर्वं चान्ववेक्षितम् ।।1.3.5।। |
|  | ﻿तत: पश्यति धर्मात्मा तत्सर्वं योगमास्थित: । |
| 1.3.7 | तत्सर्वं तत्त्वतो दृष्ट्वा धर्मेण स महाद्युति: । अभिरामस्य रामस्य चरितं कर्तुमुद्यत: ।।1.3.7।। कामार्थगुणसंयुक्तं धर्मार्थगुणविस्तरम् । समुद्रमिव रत्न |
| 1.3.9 | स यथा कथितं पूर्वं नारदेन महर्षिणा । रघुवंशस्य चरितं चकार भगवानृषिः ।।1.3.9।। |
| 1.3.18 | दर्शनं शरभङ्गस्य सुतीक्ष्णेन समागमम् । अनसूयासहास्यामप्यङ्गरागस्य चार्पणम् ।।1.3.18।। |
| 1.3.19 | अगस्त्यदर्शनं चैव जटायोरभिसङ्गमम् । पञ्चवट्याश्च गमनं शूर्पणख्याश्च दर्शनम् ।।1.3.19।। |
| 1.3.27 | पर्वतारोहणं चापि सागरस्यापि लङ्घनम् । समुद्रवचनाच्चैव मैनाकस्य च दर्शनम् ।।1.3.27।। |
|  | ﻿सिंहिकायाश्च निधनं लङ्कामलयदर्शनम् । |
|  | ﻿﻿दर्शनं रावणस्यापि पुष्पकस्य च दर्शनम् । |
| 1.4.2 | चतुर्विंशत्सहस्राणि श्लोकानामुक्तवानृषि:। तथा सर्गशतान्पञ्च षट्काण्डानि तथोत्तरम् ।।1.4.2।। |
| 1.4.8 | पाठ्ये गेये च मधुरं प्रमाणैस्त्रिभिरन्वितम्। जातिभिस्सप्तभिर्बद्धं तन्त्रीलयसमन्वितम्।।1.4.8।। रसैश्शृङ्गारकारुण्यहास्यवीरभयानकै:। रौद्रादिभिश्च संयुक |
| 1.4.28 | तौ चापि मधुरं रक्तं स्वञ्चितायतनिस्वनम् । तन्त्रीलयवदत्यर्थं विश्रुतार्थमगायताम् ।।1.4.28।। |

## Full data

Complete machine-readable results alongside this file: `scratchpad/bala_gitasupersite_alignment.json`

_Dr. Mārcis Gasūns_
