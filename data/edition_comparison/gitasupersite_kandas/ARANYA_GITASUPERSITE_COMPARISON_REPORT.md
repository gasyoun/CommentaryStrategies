_Created: 12-07-2026 · Last updated: 05-09-2026_

# Araṇyakāṇḍa (III): Critical (GRETIL/Baroda) vs Gita Supersite

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
| 2060 | 2242 | 74 | 1827 | 1439 | 274 | 114 | 159 | 341 |

## Major differences (sim < 0.6) — 114 pairs, showing up to 60

| Critical locus | Gita Supersite locus | sim | Critical text | Gita Supersite text |
|---|---|---:|---|---|
| 3.33.14 | 3.35.14 | 0.39 | atyantaniyatāhāraiḥ śobhitaṃ paramarṣibhiḥ nāgaiḥ suparṇair gandharvaiḥ kiṃnaraiś ca sahasraśaḥ | नागैस्सुपर्णैर्गन्धैर्वैः किन्नरैश्च सहस्रशः। अजैर्वैखानसैर्माषैर्वालखिल्यैर्मरीचिपैः।।3.35.14।। अत्यन्तनियताहारैश्शोभित |
| 3.11.18 | 3.12.17 | 0.391 | somasthānaṃ bhagasthānaṃ sthānaṃ kauberam eva ca dhātur vidhātuḥ sthānaṃ ca vāyoḥ sthānaṃ tathaiva ca | स तत्र ब्रह्मणः स्थानमग्नेः स्थानं तथैव च।।3.12.17।। विष्णोः स्थानं महेन्द्रस्य स्थानं चैव विवस्वतः। सोमस्थानं भगस्थानं  |
| 3.16.19 | 3.17.24 | 0.391 | rāvaṇo nāma me bhrātā rākṣaso rākṣaseśvaraḥ pravṛddhanidraś ca sadā kumbhakarṇo mahābalaḥ | प्रवृद्धनिद्रश्च सदा कुम्भकर्णो महाबलः। विभीषणस्तु धर्मात्मा न तु राक्षसचेष्टितः।।3.17.24।। प्रख्यातवीर्यौ च रणे भ्रातरौ |
| 3.16.17 | 3.17.22 | 0.433 | sābravīd vacanaṃ śrutvā rākṣasī madanārditā śrūyatāṃ rāma vakṣyāmi tattvārthaṃ vacanaṃ mama | श्रूयतां राम वक्ष्यामि तत्त्वार्थं वचनं मम। 3.17.21।। अहं शूर्पणखा नाम राक्षसी कामरूपिणी। अरण्यं विचरामीदमेका सर्वभयङ्कर |
| 3.20.17 | 3.21.19 | 0.443 | apayāhi janasthānāt tvaritaḥ sahabāndhavaḥ niḥsattvasyālpavīryasya vāsas te kīdṛśas tv iha | निस्सत्वस्याल्प वीर्यस्य वासस्ते कीदृशस्त्विह।।3.21.19।। अपयाहि जनस्थानातत्वरितस्सहबान्धवः। |
| 3.50.39 | 3.52.41 | 0.443 | udvīkṣyodvīkṣya nayanair āsrapātāvilekṣaṇāḥ supravepitagātrāś ca babhūvur vanadevatāḥ | सुप्रवेपितगात्राश्च बभूवुर्वनदेवताः।।3.52.41।। विक्रोशन्तीं दृढं सीतां दृष्ट्वा दुःखं तथा गताम्। |
| 3.13.14 | 3.14.13 | 0.458 | kālakā ca mahābāho śeṣās tv amanaso 'bhavan adityāṃ jajñire devās trayastriṃśad ariṃdama | अदितिस्तन्मना राम दितिश्च मनुजर्षभ।।3.14.13।। कालिका च महाबाहो शेषास्त्वमनसोऽभवन्। |
| 3.40.26 | 3.42.28 | 0.46 | upagamya samāghrāya vidravanti diśo daśa rākṣasaḥ so 'pi tān vanyān mṛgān mṛgavadhe rataḥ | समुद्वीक्ष्य च ते सर्वे मृगा ह्यन्ये वनेचराः।।3.42.28।। उपागम्य समाघ्राय विद्रवन्ति दिशो दश। |
| 3.21.14 | 3.22.14 | 0.461 | taṃ meruśikharākāraṃ taptakāñcanabhūṣaṇam hemacakram asaṃbādhaṃ vaidūryamaya kūbaram | तं मेरुशिखराकारं तप्तकाञ्चनभूषणम्। हेमचक्रमसम्बाधं वैदूर्यमयकूबरम्।।3.22.14।। मत्स्यैः पुष्पैर्द्रुमैश्शैलैश्चन्द्रसूर्य |
| 3.61.1 | 3.65.1 | 0.461 | tapyamānaṃ tathā rāmaṃ sītāharaṇakarśitam lokānām abhave yuktaṃ sāmvartakam ivānalam | तप्यमानं तथा रामं सीताहरणकर्शितम्। लोकानामभवे युक्तं सांवर्तकमिवानलम्।।3.65.1।। वीक्षमाणं धनुस्सज्यं निश्श्वसन्तं पुनः प |
| 3.58.28 | 3.60.32 | 0.465 | nūnaṃ tac chubhadantauṣṭhaṃ mukhaṃ niṣprabhatāṃ gatam sā hi campakavarṇābhā grīvā graiveya śobhitā | सा हि चम्पकवर्णाभा ग्रीवा ग्रैवेयशोभिता। कोमला विलपन्त्यास्तु कान्ताया भक्षिता शुभा।।3.60.32।। |
| 3.36.17 | 3.38.21 | 0.471 | rāmasya śaravegena nirasto bhrāntacetanaḥ pātito 'haṃ tadā tena gambhīre sāgarāmbhasi | पातितोऽहं तदा तेन गम्भीरे सागराम्भसि। प्राप्य संज्ञां चिरात्तात लङ्कां प्रतिगतः पुरीम्।।3.38.21।। |
| 3.36.26 | 3.38.30 | 0.471 | pramadānāṃ sahasrāṇi tava rājan parigrahaḥ bhava svadāranirataḥ svakulaṃ rakṣarākṣasa | परदाराभिमर्शात्तु नान्यत्पापतरं महत्। प्रमदानां सहस्रं च तव राजन्परिग्रहः।।3.38.30।। |
| 3.38.13 | 3.40.14 | 0.471 | tasmāt sarvāsv avasthāsu mānyāḥ pūjyāś ca pārthivāḥ tvaṃ tu dharmam avijñāya kevalaṃ moham āsthitaḥ | त्वं तु धर्ममविज्ञाय केवलं मोहमास्थितः। अभ्यागतं मां दौरात्म्यात्परुषं वक्तुमिच्छसि।।3.40.14।। |
| 3.59.16 | 3.61.18 | 0.472 | tasyā hy anveṣaṇe śrīman kṣipram eva yatāvahe vanaṃ sarvaṃ vicinuvo yatra sā janakātmajā | वनं सर्वं विचिनुवो यत्र सा जनकात्मजा।।3.61.18।। मन्यसे यदि काकुत्स्थ मा स्म शोके मनः कृथाः। |
| 3.10.25 | 3.11.27 | 0.474 | trīn māsān aṣṭamāsāṃś ca rāghavo nyavasat sukham tathā saṃvasatas tasya munīnām āśrameṣu vai | तथा संवसतस्तस्य मुनीनामाश्रमेषु वै।।3.11.27।। रमतश्चानुकूल्येन ययुस्संवत्सरा दश। |
| 3.34.3 | 3.36.2 | 0.475 | triśirāś ca mahātejā rākṣasaḥ piśitāśanaḥ anye ca bahavaḥ śūrā labdhalakṣā niśācarāḥ | जानीषे त्वं जनस्थाने यथा भ्राता खरो मम। दूषणश्च महाबाहु स्वसा शूर्पणखा च मे।।3.36.2।। त्रिशिराश्च महातेजा राक्षसः पिशिता |
| 3.63.9 | 3.67.9 | 0.476 | kruddho rāmaḥ śaraṃ ghoraṃ saṃdhāya dhanuṣi kṣuram tataḥ parvatakūṭābhaṃ mahābhāgaṃ dvijottamam | ततः पर्वतकूटाभं महाभागं द्विजोत्तमम्।।3.67.9।। ददर्श पतितं भूमौ क्षतजार्द्रं जटायुषम्। |
| 3.33.28 | 3.35.28 | 0.477 | samantād yasya tāḥ śākhāḥ śatayojanam āyatāḥ yasya hastinam ādāya mahākāyaṃ ca kaccapam | यस्य हस्तिनमादाय महाकायं च कच्छपम्।।3.35.28।। भक्षार्थं गरुडश्शाखामाजगाम महाबलः। |
| 3.1.7 | 3.1.8 | 0.478 | sūryavaiśvānarābhaiś ca purāṇair munibhir vṛtam puṇyaiś a niyatāhāraiḥ śobhitaṃ paramarṣibhiḥ | पुण्यैश्च नियताहारैः शोभितं परमर्षिभिः। तद्ब्रह्मभवनप्रख्यं ब्रह्मघोषनिनादितम्।।3.1.8।। |
| 3.13.24 | 3.14.25 | 0.478 | tatas tv irāvatīṃ nāma jajñe bhadramadā sutām tasyās tv airāvataḥ putro lokanātho mahāgajaḥ | तस्यास्त्वैरावतः पुत्रो लोकनाथो महागजः। मातङ्ग्या स्त्वथ मातङ्गा अपत्यं मनुजर्षभ।।3.14.25।। |
| 3.16.16 | 3.17.20 | 0.478 | tvāṃ tu veditum icchāmi kathyatāṃ kāsi kasya vā iha vā kiṃnimittaṃ tvam āgatā brūhi tattvataḥ | इह वा किंनिमित्तं त्वमागता ब्रूहि तत्त्वत:।।3.17.20।। साब्रवीद् वचनं श्रुत्वा राक्षसी मदनार्दिता। |
| 3.53.4 | 3.55.4 | 0.478 | aśrupūrṇamukhīṃ dīnāṃ śokabhārāvapīḍitām vāyuvegair ivākrāntāṃ majjantīṃ nāvam arṇave | अश्रुपूर्णमुखीं दीनां शोकभाराभिपीडिताम्। वायुवेगैरिवाक्रान्तां मज्जन्तीं नावमर्णवे।।3.55.4।। मृगयूथपरिभ्रष्टां मृगीं श्व |
| 3.65.26 | 3.69.45 | 0.478 | imaṃ deśam anuprāptau kṣudhārtasyeha tiṣṭhataḥ sabāṇacāpakhaḍgau ca tīkṣṇaśṛṅgāv ivarṣabhau | सबाणचापखड्गौ च तीक्ष्णशृङ्गाविवर्षभौ।।3.69.45।। ममास्यमनुसम्प्राप्तौ दुर्लभं जीवितं पुनः। |
| 3.13.12 | 3.14.12 | 0.479 | tāmrāṃ krodhavaśāṃ caiva manuṃ cāpy analām api tās tu kanyās tataḥ prītaḥ kaśyapaḥ punar abravīt | तास्तु कन्यास्ततः प्रीतः काश्यपः पुनरब्रवीत्।।3.14.12।। पुत्रां स्स्रैलोक्यभर्तृ़न्वै जनयिष्यथ मत्समान्। |
| 3.13.16 | 3.14.16 | 0.479 | teṣām iyaṃ vasumatī purāsīt savanārṇavā danus tv ajanayat putram aśvagrīvam ariṃdama | दनुस्त्वजनयत्पुत्रमश्वग्रीवमरिन्दम।।3.14.16।। नरकं कालकंचैव कालिकापि व्यजायत। |
| 3.50.38 | 3.52.40 | 0.479 | iti sarvāṇi bhūtāni gaṇaśaḥ paryadevayan vitrastakā dīnamukhā rurudur mṛgapotakāḥ | वित्रस्तका दीनमुखा रुरुदुर्मृगपोतकाः।।3.52.40।। उद्वीक्ष्योद्वीक्ष्य नयनैरस्रपाताविलेक्षणाः। |
| 3.63.8 | 3.67.8 | 0.481 | āpatsu na prakampante vāyuvegair ivācalāḥ ity uktas tad vanaṃ sarvaṃ vicacāra salakṣmaṇaḥ | इत्युक्तस्तद्वनं सर्वं विचचार सलक्ष्मणः।।3.67.8।। क्रुद्धो रामश्शरं घोरं सन्धाय धनुषि क्षुरम्। |
| 3.65.25 | 3.69.44 | 0.481 | ghoraṃ deśam imaṃ prāptau mama bhakṣāv upasthitau vadataṃ kāryam iha vāṃ kimarthaṃ cāgatau yuvām | वदतं कार्यमिह वां किमर्थं चागतौ युवाम्।।3.69.44।। इमं देशमनुप्राप्तौ क्षुधार्तस्येह तिष्ठतः। |
| 3.7.13 | 3.8.13 | 0.483 | suprājyaphalamūlāni puṣpitāni vanāni ca praśāntamṛgayūthāni śāntapakṣigaṇāni ca | सप्राज्यफलमूलानि पुष्पितानि वनानि च। प्रशस्तमृगयूथानि शान्तपक्षिगणानि च।। 3.8.13।। फुल्लपङ्कजषण्डानि प्रसन्नसलिलानि च। क |
| 3.10.39 | 3.11.42 | 0.483 | tatraikāṃ rajanīm uṣya prabhāte rāma gamyatām dakṣiṇāṃ diśam āsthāya vanakhaṇḍasya pārśvataḥ | दक्षिणां दिशमास्थाय वनषण्डस्य पार्श्वतः। तत्रागस्त्याश्रमपदं गत्वा योजनमन्तरा।।3.11.42।। |
| 3.65.18 | 3.69.31 | 0.483 | mahādaṃṣṭropapannaṃ taṃ lelihānaṃ mahāmukham bhakṣayantaṃ mahāghorān ṛkṣasiṃhamṛgadvipān | भक्षयन्तं महाघोरानृक्षसिंहमृगद्विपान्। घोरौ भुजौ विकुर्वाणमुभौ योजनमायतौ।।3.69.31।। |
| 3.42.5 | 3.44.4 | 0.484 | avekṣyāvekṣya dhāvantaṃ dhanuṣpāṇir mahāvane ativṛttam iṣoḥ pātāl lobhayānaṃ kadā cana | तं स्म पश्यति रूपेण द्योतमानमिवाग्रतः।।3.44.4।। अवेक्ष्यावेक्ष्य धावन्तं धनुष्पाणिर्महावने। अतिवृत्तमिषोः पाताल्लोभयानं  |
| 3.2.13 | 3.2.12 | 0.485 | carāmi sāyudho nityam ṛṣimāṃsāni bhakṣayan iyaṃ nārī varārohā mama bharyā bhaviṣyati | अहं वनमिदं दुर्गं विराधो नाम राक्षसः। चरामि सायुधो नित्यमृषिमांसानि भक्षयन्।।3.2.12।। |
| 3.4.3 | 3.5.3 | 0.485 | āśramaṃ śarabhaṅgasya rāghavo 'bhijagāma ha | आश्रमं शरभङ्गस्य राघवोऽभिजगाम ह।।3.5.3।। तस्य देवप्रभावस्य तपसा भावितात्मनः। समीपे शरभङ्गस्य ददर्श महदद्भुतम्।।3.5.4।। |
| 3.4.26 | 3.5.30 | 0.485 | samāgamya gamiṣyāmi tridivaṃ devasevitam akṣayā naraśārdūla jitā lokā mayā śubhāḥ | त्वयाऽहं पुरुषव्याघ्र धार्मिकेण महात्मना। समागम्य गमिष्यामि त्रिदिवं देवसेवितम्।।3.5.30।। |
| 3.30.12 | 3.32.12 | 0.486 | ucchettāraṃ ca dharmāṇāṃ paradārābhimarśanam sarvadivyāstrayoktāraṃ yajñavighnakaraṃ sadā | क्षेप्तारं पर्वतेन्द्राणां सुराणां च प्रमर्दनम्। उच्छेत्तारं च धर्माणां परदाराभिमर्शनम्।।3.32.12।। |
| 3.65.6 | 3.69.6 | 0.487 | nānāmeghaghanaprakhyaṃ prahṛṣṭam iva sarvataḥ nānāvarṇaiḥ śubhaiḥ puṣpair mṛgapakṣigaṇair yutam | नानामेघघनप्रख्यं प्रहृष्टमिव सर्वतः। नानापक्षिगणैर्युक्तं नानाव्यालमृगैर्युतम्।।3.69.6।। दिदृक्षमाणौ वैदेहीं तद्वनं तौ व |
| 3.53.31 | 3.55.31 | 0.488 | śokārtaṃ tu varārohe na bhrājati varānane alaṃ vrīḍena vaidehi dharmalopa kṛtena te | वदनं पद्मसङ्काशममलं चारुदर्शनम्। शोकार्तंतु वरारोहे न भ्राजति वरानने।।3.55.31।। |
| 3.58.30 | 3.60.34 | 0.488 | bhakṣitau vepamānāgrau sahastābharaṇāṅgadau mayā virahitā bālā rakṣasāṃ bhakṣaṇāya vai | मया विरहिता बाला रक्षसां भक्षणाय वै। सार्धेनेव परित्यक्ता भक्षिता बहुबान्धवा।।3.60.34।। |
| 3.59.18 | 3.61.21 | 0.488 | nikhilena vicinvantau sītāṃ daśarathātmajau tasya śailasya sānūni guhāś ca śikharāṇi ca | तस्य शैलस्य सानूनि गुहाश्च शिखराणि च।।3.61.21।। निखिलेन विचिन्वानौ नैव तामभिजग्मतुः। |
| 3.14.16 | 3.15.16 | 0.489 | sālais tālais tamālaiś ca kharjūraiḥ panasāmrakaiḥ nīvārais timiśaiś caiva puṃnāgaiś copaśobhitāḥ | सालैस्तालैस्तमालैश्च खर्जूरपनसाम्रकैः। नीवारैस्तिमिशैश्चैव पुन्नागैश्चोपशोभिताः।।3.15.16।। चूतैरशोकैस्तिलकैश्चम्पकैः केत |
| 3.41.46 | 3.43.46 | 0.489 | yāvad gacchāmi saumitre mṛgam ānayituṃ drutam paśya lakṣmaṇa vaidehīṃ mṛgatvaci gataspṛhām | अहमेनं वधिष्यामि ग्रहीष्याम्यपि वा मृगम्।।3.43.46।। यावद्गच्छामि सौमित्रे मृगमानयितुं द्रुतम्। |
| 3.60.34 | 3.64.51 | 0.489 | vairaṃ śataguṇaṃ paśya mamedaṃ jīvitāntakam sughorahṛdayaiḥ saumya rākṣasaiḥ kāmarūpibhiḥ | पदवीपुरुषस्यैषा व्यक्तं कस्यापि रक्षसः। वैरं शतगुणं पश्य ममेदं जीवितान्तकम्।।3.64.51।। |
| 3.9.10 | 3.10.11 | 0.491 | sarvair eva samāgamya vāg iyaṃ samudāhṛtā rākṣasair daṇḍakāraṇye bahubhiḥ kāmarūpibhiḥ | राक्षसैर्दण्डकारण्ये बहुभिः कामरूपिभिः। अर्दितास्स्म दृढं राम भवान्नस्तत्र रक्षतु।।3.10.11।। |
| 3.19.24 | 3.20.22 | 0.491 | sā nadantī mahānādaṃ javāc chūrpaṇakhā punaḥ upagamya kharaṃ sā tu kiṃ cit saṃśuṣka śoṇitā | उपगम्य खरं सा तु किञ्चित्संशुष्कशोणिता।।3.20.22।। पपात पुनरेवार्ता सनिर्यासेव सल्लकी। |
| 3.35.19 | 3.37.19 | 0.491 | prāṇebhyo 'pi priyatarā bhāryā nityam anuvratā dīptasyeva hutāśasya śikhā sītā sumadhyamā | तस्य सा नरसिंहस्य सिंहोरस्कस्य भामिनी। प्राणेभ्योऽपि प्रियतरा भार्या नित्यमनुव्रता।।3.37.19।। |
| 3.58.29 | 3.60.33 | 0.491 | komalā vilapantyās tu kāntāyā bhakṣitā śubhā nūnaṃ vikṣipyamāṇau tau bāhū pallavakomalau | नूनं विक्षिप्यमाणौ तौ बाहू पल्लवकोमलौ। भक्षितौ वेपमानाग्रौ सहस्ताभरणाङ्गदौ।।3.60.33।। |
| 3.13.25 | 3.14.26 | 0.492 | haryāś ca harayo 'patyaṃ vānarāś ca tapasvinaḥ golāṅgūlāṃś ca śārdūlī vyāghrāṃś cājanayat sutān | गोलाङ्गूलांश्च शार्दूली व्याघ्रांश्चाजनयत्सुतान्। दिशागजांश्च काकुत्स्थ श्वेताप्यजनयत्सुतान्।।3.14.26।। |
| 3.42.11 | 3.44.13 | 0.492 | tam eva mṛgam uddiśya jvalantam iva pannagam mumoca jvalitaṃ dīptam astrabrahmavinirmitam | भूयस्तु शरमुद्धृत्य कुपितस्तत्र राघवः। सूर्यरश्मिप्रतीकाशं ज्वलन्तमरिमर्दनः।।3.44.13।। सन्धाय सुदृढे चापे विकृष्य बलवद्ब |
| 3.13.7 | 3.14.7 | 0.494 | kardamaḥ prathamas teṣāṃ vikṛtas tadanantaram śeṣaś ca saṃśrayaś caiva bahuputraś ca vīryavān | कर्दमः प्रथमस्तेषां विक्रीतस्तदनन्तरः। शेषश्च संश्रयश्चैव बहुपुत्रश्च वीर्यवान्।।3.14.7।। स्थाणुर्मरीचिरत्रिश्च क्रतुश्च |
| 3.38.14 | 3.40.15 | 0.494 | abhyāgataṃ māṃ daurātmyāt paruṣaṃ vadasīdṛśam guṇadoṣau na pṛcchāmi kṣamaṃ cātmani rākṣasa | गुणदोषौ न पृच्छामि क्षमं चात्मनि राक्षस। मयोक्तं तव चैतावत्संप्रत्यमितविक्रमः।।3.40.15।। |
| 3.41.47 | 3.43.47 | 0.494 | tvacā pradhānayā hy eṣa mṛgo 'dya na bhaviṣyati apramattena te bhāvyam āśramasthena sītayā | पश्य लक्ष्मण वैदेहीं मृगत्वचि गतस्पृहाम्।।3.43.47।। त्वचा प्रधानया ह्येष मृगोऽद्य न भविष्यति। |
| 3.43.5 | 3.45.5 | 0.494 | tam uvāca tatas tatra kupitā janakātmajā saumitre mitrarūpeṇa bhrātus tvam asi śatruvat | सौमित्रे मित्ररूपेण भ्रातुस्त्वमसि शत्रुवत्।।3.45.5।। यस्त्वमस्यामवस्थायां भ्रातरं नाभिपत्स्यसे। |
| 3.43.6 | 3.45.6 | 0.495 | yas tvam asyām avasthāyāṃ bhrātaraṃ nābhipadyase icchasi tvaṃ vinaśyantaṃ rāmaṃ lakṣmaṇa matkṛte | इच्छसि त्वं विनश्यन्तं रामं लक्ष्मण मत्कृते।।3.45.6।। लोभात्त्वं मत्कृते नूनं नानुगच्छसि राघवम्। |
| 3.2.9 | 3.2.9 | 0.497 | abhyadhāvat susaṃkruddhaḥ prajāḥ kāla ivāntakaḥ sa kṛtvā bhairavaṃ nādaṃ cālayann iva medinīm | स कृत्वा भैरवं नादं चालयन्निव मेदिनीम्। अङ्केनादाय वैदेहीमपक्रम्य ततोऽब्रवीत्।।3.2.9।। |
| 3.2.11 | 3.2.11 | 0.497 | praviṣṭau daṇḍakāraṇyaṃ śaracāpāsidhāriṇau kathaṃ tāpasayor vāṃ ca vāsaḥ pramadayā saha | कथं तापसयोर्वां च वासः प्रमदया सह। अधर्मचारिणौ पापौ कौ युवां मुनिदूषकौ।।3.2.11।। |
| 3.4.13 | 3.5.15 | 0.497 | urodeśeṣu sarveṣāṃ hārā jvalanasaṃnibhāḥ rūpaṃ bibhrati saumitre pañcaviṃśativārṣikam | इमे च पुरुषव्याघ्रा ये तिष्ठ्न्त्यभितो रथम्। शतं शतं कुण्डलिनो युवानः खङ्गपाणयः।।3.5.15।। विस्तीर्णविपुलोरस्काः परिघायतब |
| 3.40.16 | 3.42.18 | 0.497 | manoharasnigdhavarṇo ratnair nānāvidhair vṛtaḥ kṣaṇena rākṣaso jāto mṛgaḥ paramaśobhanaḥ | इन्द्रायुधसवर्णेन पुच्छेनोर्ध्वं विराजता।।3.42.18।। मनोहरस्स्निग्धवर्णो रत्नैर्नानाविधैर्वृतः। |
| 3.40.28 | 3.42.31 | 0.497 | kusumāpacaye vyagrā pādapān atyavartata karṇikārān aśokāṃś ca cūṭāṃś ca madirekṣaṇā | कर्णिकारानशोकांश्च चूतांश्च मदिरेक्षणा।।3.42.31।। कुसुमान्यवचिन्वन्ती चचार रुचिरानना। |

## Minor edits (sim 0.6–0.9) — 274 pairs, sample of 60

| Critical locus | Gita Supersite locus | sim | Critical text | Gita Supersite text |
|---|---|---:|---|---|
| 3.55.5 | 3.57.5 | 0.606 | mārīcena tu vijñāya svaram ālakṣya māmakam vikruṣṭaṃ mṛgarūpeṇa lakṣmaṇaḥ śṛṇuyād yadi | मारीचेन तु विज्ञाय स्वरमालम्ब्य मामकम्। विक्रुष्टं मृगरूपेण लक्ष्मणश्शृणुयाद्यदि।।3.57.5।। स सौमित्रिस्स्वरं श्रुत्वा ता |
| 3.51.22 | 3.53.23 | 0.611 | nimeṣāntaramātreṇa vinā bhrātaram āhave rākṣasā nihatā yena sahasrāṇi caturdaśa | निमेषान्तरमात्रेण विना भ्रात्रा महावने।।3.53.23।। राक्षसा निहता येन सहस्राणि चतुर्दश। स कथं राघवो वीरस्सर्वास्त्रकुशलो ब |
| 3.35.16 | 3.37.16 | 0.612 | dhanurvyāditadīptāsyaṃ śarārciṣam amarṣaṇam cāpabāṇadharaṃ vīraṃ śatrusenāpahāriṇam | धनुर्व्यादितदीप्तास्यं शरार्चिषममर्षणम्। चापबाणधरं तीक्ष्णं शत्रुसैन्यप्रहारिणम्।।3.37.16।। राज्यं सुखं च सन्त्यज्य जीवि |
| 3.44.18 | 3.46.18 | 0.615 | viśālaṃ jaghanaṃ pīnam ūrū karikaropamau etāv upacitau vṛttau sahitau saṃpragalbhitau | विशालं जघनं पीनमूरू करिकरोपमौ।।3.46.18।। एतावुपचितौ वृत्तौ संहतौ सम्प्रवल्गितौ। पीनोन्नतमुखौ कान्तौ स्निग्धौ तालफलोपमौ।। |
| 3.5.11 | 3.6.12 | 0.617 | yuñjānaḥ svān iva prāṇān prāṇair iṣṭān sutān iva nityayuktaḥ sadā rakṣan sarvān viṣayavāsinaḥ | युञ्जानस्स्वानिव प्राणान्प्राणैरिष्टान्सुतानिव। नित्ययुक्तस्सदा रक्षन्सर्वान्विषयवासिनः।।3.6.12।। प्राप्नोति शाश्वतीं रा |
| 3.10.83 | 3.11.85 | 0.617 | mārgaṃ niroddhuṃ satataṃ bhāskarasyācalottamaḥ saṃdeśaṃ pālayaṃs tasya vindhyaśaulo na vardhate | मार्गं निरोद्धुं निरतो भास्करस्याचलोत्तमः। निदेशं पालयन्यस्य विन्ध्यशैला न वर्धते।।3.11.85।। अयं दीर्घायुषस्तस्य लोके वि |
| 3.23.7 | 3.24.7 | 0.618 | saṃprahāras tu sumahān bhaviṣyati na saṃśayaḥ ayam ākhyāti me bāhuḥ sphuramāṇo muhur muhuḥ | सम्प्रहारस्तु सुमहान्भविष्यति न संशयः। अयमाख्याति मे बाहुस्स्फुरमाणो मुहुर्मुहुः।।3.24.7।। सन्निकर्षे तु न श्शूर जयं शत् |
| 3.44.22 | 3.46.23 | 0.619 | naivaṃrūpā mayā nārī dṛṣṭapūrvā mahītale iha vāsaś ca kāntāre cittam unmāthayanti me | रूपमग्र्यं च लोकेषु सौकुमार्यं वयश्चते। इह वासश्च कान्तारे चित्तमुन्मादयन्ति मे।।3.46.23।। |
| 3.71.7 | 3.75.6 | 0.621 | ṛśyamūko girir yatra nātidūre prakāśate yasmin vasati dharmātmā sugrīvo 'ṃśumataḥ sutaḥ | तदागच्छ गमिष्यामि पम्पां तां प्रियदर्शनाम्।।3.75.6।। ऋष्यमूको गिरिर्यत्र नातिदूरे प्रकाशते। यस्मिन्वसति धर्मात्मा सुग्री |
| 3.2.2 | 3.2.2 | 0.622 | nānāmṛgagaṇākīrṇaṃ śārdūlavṛkasevitam dhvastavṛkṣalatāgulmaṃ durdarśa salilāśayam | नानामृगगणाकीर्णमृक्षशार्दूल सेवितम्। ध्वस्तवृक्षलतागुल्मं दुर्दर्शसलिलाशयम्।।3.2.2।। निष्कूजनानाशकुनिझिल्लिकागणनादितम्।  |
| 3.47.8 | 3.49.8 | 0.622 | sa parivrājakacchadma mahākāyo vihāya tat pratipede svakaṃ rūpaṃ rāvaṇo rākṣasādhipaḥ | स परिव्राजकच्छद्म महाकायो विहाय तत्।।3.49.8।। प्रतिपद्य स्वकं रूपं रावणो राक्षसाधिपः। संरक्तनयनः क्रोधाज्जीमूतनिचयप्रभः। |
| 3.53.35 | 3.55.37 | 0.622 | kṛtāntavaśam āpanno mameyam iti manyate | एवमुक्त्वा दशग्रीवो मैथिलीं जनकात्मजाम्।।3.55.37।। कृतान्तवशमापन्नो ममेयमिति मन्यते। |
| 3.48.14 | 3.50.13 | 0.625 | atra brūhi yathāsatyaṃ ko rāmasya vyatikramaḥ yasya tvaṃ lokanāthasya hṛtvā bhāryāṃ gamiṣyasi | यदि शूर्पणखाहेतोर्जनस्थानगतः खरः।।3.50.13।। अतिवृत्तो हतः पूर्वं रामेणाक्लिष्टकर्मणा। अत्र ब्रूहि यथातत्त्वं को रामस्य व |
| 3.10.43 | 3.11.46 | 0.626 | paśyan vanāni citrāṇi parvapāṃś cābhrasaṃnibhān sarāṃsi saritaś caiva pathi mārgavaśānugāḥ | पश्यन्वनानि रम्याणि पर्वतांश्चाभ्रसन्निभान्।।3.11.46।। सरांसि सरितश्चैव पथि मार्गवशानुगाः। सुतीक्ष्णेनोपदिष्टेन गत्वा ते |
| 3.57.13 | 3.59.14 | 0.627 | alaṃ vaiklavyam ālambya svasthā bhava nirutsukā na cāsti triṣu lokeṣu pumān yo rāghavaṃ raṇe | अलं वैक्लब्यमालम्ब्य स्वस्था भव निरुत्सुका। न सोऽस्ति त्रिषु लोकेषु पुमान्वै राघवं रणे।।3.59.14।। जातो वा जायमानो वा संय |
| 3.10.24 | 3.11.25 | 0.628 | kva cic ca caturo māsān pañcaṣaṭ cāparān kva cit aparatrādhikān māsān adhyardham adhikaṃ kva cit | क्वचित्परिदशान्मासानेकं संवत्सरं क्वचित्।।3.11.25।। क्वचिच्छ चतुरो मासान् पञ्च षट्चापरान्क्वचित्। अपरत्राधिकं मासादप्यर् |
| 3.33.38 | 3.31.39 | 0.631 | sa rāvaṇaḥ samāgamya vidhivat tena rakṣasā tataḥ paścād idaṃ vākyam abravīd vākyakovidaḥ | एवमुक्तो महातेजा मारीचेन स रावणः। ततः पश्चादिदं वाक्यमब्रवीद्वाक्यकोविदः।।3.31.39।। |
| 3.13.28 |  | 0.632 | rohiṇy ajanayad gā vai gandharvī vājinaḥ sutān surasājanayan nāgān rāma kadrūś ca pannagān | रोहिण्यजनयद् गावो गन्धर्वी वाजिनः सुतान्। |
| 3.34.12 | 3.36.12 | 0.632 | yena vairaṃ vināraṇye sattvam āśritya kevalam karṇanāsāpahāreṇa bhaginī me virūpitā | येन वैरं विनाऽरण्ये सत्वमाश्रित्य केवलम्।।3.36.12।। कर्णनासापहरणाद्भगिनी मे विरूपिता। तस्यभार्यां जनस्थानात्सीतां सुरसुत |
| 3.70.11 | 3.74.15 | 0.632 | taiś cāham uktā dharmajñair mahābhāgair maharṣibhiḥ āgamiṣyati te rāmaḥ supuṇyam imam āśramam | तैश्चाहमुक्ता धर्मज्ञैर्महाभागैर्महर्षिभिः। आगमिष्यति ते रामस्सुपुण्यमिममाश्रमम्।।3.74.15।। स ते प्रतिग्रहीतव्यस्सौमित्र |
| 3.8.10 | 3.9.13 | 0.633 | na hi me rocate vīra gamanaṃ daṇḍakān prati kāraṇaṃ tatra vakṣyāmi vadantyāḥ śrūyatāṃ mama | त्वां चैव प्रस्थितं दृष्ट्वा राम चिन्ताकुलं मनः।।3.9.13।। सर्वतचशिन्तय्नत्या मे तव निश्श्रेयसं नृप। न हि मे रोचते वीर गम |
| 3.41.1 | 3.43.1 | 0.634 | sā taṃ saṃprekṣya suśroṇī kusumāni vicinvatī hemarājata varṇābhyāṃ pārśvābhyām upaśobhitam | सा तं सम्प्रेक्ष्य सुश्रोणी कुसुमान्यपचिन्वती। हेमराजतवर्णाभ्यां पार्श्वाभ्यामुपशोभितम्।।3.43.1।। प्रहृष्टा चानवद्याङ्गी |
| 3.10.73 | 3.11.76 | 0.635 | puṣpitān puṣpitāgrābhir latābhir anuveṣṭitān dadarśa rāmaḥ śataśas tatra kāntārapādapān | पुष्पितान्पुष्पिताग्राभिर्लताभिरनुवेष्टितान्। ददर्श रामश्शतशस्तत्र कान्तारपादपान्।।3.11.76।। हस्तिहस्तैर्विमृदितान्वानरै |
| 3.23.20 | 3.24.28 | 0.637 | siṃhanādaṃ visṛjatām anyonyam abhigarjatām cāpāni vispharayatāṃ jṛmbhatāṃ cāpy abhīkṣṇaśaḥ | सिंहनादं विसृजतामन्योन्यमभिगर्जताम्। चापानि विस्फ़ारयतां जृम्भतामप्यभीक्ष्णशः।।3.24.28।। विप्रघुष्टस्वनानां च दुन्धुभींश |
| 3.18.11 | 3.19.14 | 0.638 | taruṇau rūpasaṃpannau sukūmārau mahābalau puṇḍarīkaviśālākṣau cīrakṛṣṇājināmbarau | तरुणौ रूपसम्पन्नौ सुकुमारौ महाबलौ। पुण्डरीकविशालाक्षौ चीरकृष्णाजिनाम्बरौ।।3.19.14।। फलमूलाशनौ दान्तौ तापसौ धर्मचारिणौ। प |
| 3.4.18 | 3.5.22 | 0.639 | ihopayāty asau rāmo yāvan māṃ nābhibhāṣate niṣṭhāṃ nayata tāvat tu tato māṃ draṣṭum arhati | इहोपयात्यसौ रामो यावन्मां नाभिभाषते। निष्ठां नयतु तावत्तु ततो मा द्रष्टुमर्हति।।3.5.22।। जितवन्तं कृतार्थं हि तदाहमचिराद |
| 3.7.8 | 3.8.8 | 0.64 | aviṣahyātapo yāvat sūryo nātivirājite amārgeṇāgatāṃ lakṣmīṃ prāpyevānvayavarjitaḥ | अविषह्यातपो यावत्सूर्यो नातिविराजते। अमार्गेणागतां लक्ष्मीं प्राप्येवान्वयवर्जितः।।3.8.8।। तावदिच्छामहे गन्तुमित्युक्त्व |
| 3.10.5 | 3.11.5 | 0.64 | te gatvā dūram adhvānaṃ lambamāne divākare dadṛśuḥ sahitā ramyaṃ taṭākaṃ yojanāyatam | ते गत्वा दूरमध्वानं लम्बमाने दिवाकरे। ददृशुस्सहिता रम्यं तटाकं योजनायतम्।।3.11.5।। पद्मपुष्करसम्बाधं गजयूथैरलङ्कृतम्। सा |
| 3.42.18 | 3.44.24 | 0.64 | hā sīte lakṣmaṇety evam ākruśya tu mahāsvaram mamāra rākṣasaḥ so 'yaṃ śrutvā sītā kathaṃ bhavet | हा सीते लक्ष्मणेत्येवमाक्रुश्य च महास्वरम्। ममार राक्षसस्सोऽयं श्रुत्वा सीता कथं भवेत्।।3.44.24।। लक्ष्मणश्च महाबाहुः का |
| 3.64.29 | 3.68.29 | 0.641 | yā gatir yajñaśīlānām āhitāgneś ca yā gatiḥ aparāvartināṃ yā ca yā ca bhūmipradāyinām | या गतिर्यज्ञशीलानामाहिताग्नेश्च या गतिः।।3.68.29।। अपरावर्तिनां या च या च भूमिप्रदायिनाम्। मया त्वं समनुज्ञातो गच्छ लोका |
| 3.65.17 | 3.69.29 | 0.641 | mahāpakṣmeṇa piṅgena vipulenāyatena ca ekenorasi ghoreṇa nayanenāśudarśinā | अग्निज्वालानिकाशेन ललाटस्थेन दीप्यता। महापक्ष्मेण पिङ्गेन विपुलेनायतेन च।।3.69.29।। एकेनोरसि घोरेण नयनेनाशुदर्शिना। महाद |
| 3.69.9 | 3.73.14 | 0.642 | rohitān vakratuṇḍāṃś ca nalamīnāṃś ca rāghava pampāyām iṣubhir matsyāṃs tatra rāma varān hatān | रोहितान्वक्रतुण्डांश्च नडमीनांश्च राघव।।3.73.14।। पम्पायामिषुभिर्मत्स्यांस्तत्र राम वरान्हतान्। निस्त्वक्पक्षानयस्तप्तान |
| 3.50.41 | 3.52.42 | 0.643 | avekṣamāṇāṃ bahuṣo vaidehīṃ dharaṇītalam sa tām ākulakeśāntāṃ vipramṛṣṭaviśeṣakām | तां तु लक्ष्मण रामेति क्रोशन्तीं मधुरस्वरम्।।3.52.42।। अवेक्षमाणां बहुशो वैदेहीं धरणीतलम्। स तामाकुलकेशान्तां विप्रमृष्ट |
| 3.14.4 | 3.15.4 | 0.644 | ramate yatra vaidehī tvam ahaṃ caiva lakṣmaṇa tādṛśo dṛśyatāṃ deśaḥ saṃnikṛṣṭajalāśayaḥ | रमते यत्र वैदेही त्वमहं चैव लक्ष्मण। तादृशो दृश्यतां देशस्सन्निकृष्टजलाशयः।।3.15.4।। वनरामण्यकं यत्र स्थलरामण्यकं तथा। स |
| 3.10.22 | 3.11.23 | 0.646 | uṣitvā susukhaṃ tatra pūrjyamāno maharṣibhiḥ jagāma cāśramāṃs teṣāṃ paryāyeṇa tapasvinām | तदा तस्मिन्सकाकुत्थ्सः श्रीमत्याश्रममण्डले।।3.11.23।। उषित्वा तु सुखं तत्र पूज्यमानो महर्षिभिः। जगाम चाश्रमांस्तेषां पर् |
| 3.30.1 | 3.32.1 | 0.646 | tataḥ śūrpaṇakhā dṛṣṭvā sahasrāṇi caturdaśa hatāny ekena rāmeṇa rakṣasāṃ bhīmakarmaṇām | ततश्शूर्पणखा दृष्ट्वा सहस्राणि चतुर्दश। हतान्येकेन रामेण रक्षसां भीमकर्मणाम्।।3.32.1।। दूषणं च खरं चैव हतं त्रिशिरसा सह। |
| 3.59.1 | 3.61.1 | 0.647 | dṛṣṭāśramapadaṃ śūnyaṃ rāmo daśarathātmajaḥ rahitāṃ parṇaśālāṃ ca vidhvastāny āsanāni ca | दृष्ट्वाश्रमपदं शून्यं रामो दशरथात्मजः। रहितां पर्णशालां च विध्वस्तान्यासनानि च।।3.61.1।। अदृष्ट्वा तत्र वैदेहीं सन्निरी |
| 3.13.21 | 3.14.21 | 0.649 | daśakrodhavaśā rāma vijajñe 'py ātmasaṃbhavāḥ mṛgīṃ ca mṛgamandāṃ ca harīṃ bhadramadām api | दश क्रोधवशा राम विजज्ञे ह्यात्मसम्भवाः। मृगीं च मृगमन्दां च हरीं भद्रमदामपि।।3.14.21।। मातङ्गीमपि शार्दूलीं श्वेतां च सु |
| 3.58.6 | 3.60.6 | 0.649 | rudantam iva vṛkṣaiś ca mlānapuṣpamṛgadvijam śriyā vihīnaṃ vidhvastaṃ saṃtyaktavanadaivatam | रुदन्तमिव वृक्षैश्च म्लानपुष्पमृगद्विजम्। श्रिया विहीनं विध्वस्तं सन्त्यक्तवनदेवतम्।।3.60.6।। विप्रकीर्णाजिनकुशं विप्रवि |
| 3.63.18 | 3.67.19 | 0.649 | pariśrāntasya me pakṣau chittvā khaḍgena rāvaṇaḥ sītām ādāya vaidehīm utpapāta vihāyasaṃ | अयं तु सारथिस्तस्य मत्पक्षनिहतो युधि। परिश्रान्तस्य मे पक्षौ छित्त्वा खड्गेन रावणः।।3.67.19।। सीतामादाय वैदेहीमुत्पपात व |
| 3.69.11 | 3.73.16 | 0.649 | bhṛśaṃ te khādato matsyān pampāyāḥ puṣpasaṃcaye padmagandhi śivaṃ vāri sukhaśītam anāmayam | भृशते खादतो मत्स्यान्पम्पायाः पुष्पसञ्चये।।3.73.16।। पद्मगन्धि शिवं वारि सुखशीतमनामयम्। उद्धृत्य सतताक्लिष्टं रौप्यस्फाट |
| 3.1.4 | 3.1.4 | 0.65 | viśālair agniśaraṇaiḥ srugbhāṇḍair ajinaiḥ kuśaiḥ samidbhis toyakalaśaiḥ phalamūlaiś ca śobhitam | पूजितं च प्रनृत्तं च नित्यमप्सरसां गणैः। विशालैरग्निशरणैः स्रुग्भाण्डैरजिनैः कुशैः।।3.1.4।। समिद्भिस्तोयकलशैः फलमूलैश्च  |
| 3.33.19 | 3.35.19 | 0.65 | pāṇḍurāṇi viśālāni divyamālyayutāni ca tūryagītābhijuṣṭāni vimānāni samantataḥ | पाण्डुराणि विशालानि दिव्यमाल्ययुतानि च। तूर्यगीताभिजुष्टानि विमानानि समन्ततः।।3.35.19।। तपसा जितलोकानां कामगान्यभिसम्पतन |
| 3.47.10 | 3.49.10 | 0.651 | sa tām asitakeśāntāṃ bhāskarasya prabhām iva vasanābharaṇopetāṃ maithilīṃ rāvaṇo 'bravīt | स तामसितकेशान्तां भास्करस्य प्रभामिव।।3.49.10।। |
| 3.59.9 | 3.61.9 | 0.651 | vivaśaṃ śokasaṃtaptaṃ dīnaṃ bhagnamanoratham mām ihotsṛjya karuṇaṃ kīrtir naram ivānṛjum | विवशं शोकसन्तप्तं दीनं भग्नमनोरथम्।।3.61.9।। मामिहोत्सृज्य करुणं कीर्तिर्नरमिवानृजुम्। क्व गच्छसि वरारोहे मां नोत्सृज सु |
| 3.62.1 | 3.66.1 | 0.651 | taṃ tathā śokasaṃtaptaṃ vilapantam anāthavat mohena mahatāviṣṭaṃ paridyūnam acetanam | तं तथा शोकसन्तप्तं विलपन्तमनाथवत्। मोहेन महताविष्टं परिद्यूनमचेतनम्।।3.66.1।। ततस्सौमित्रिराश्वास्य मुहूर्तादिव लक्ष्मणः |
| 3.69.16 | 3.73.22 | 0.651 | na tāni kaś cin mālyāni tatrāropayitā naraḥ mataṅgaśiṣyās tatrāsann ṛṣayaḥ susamāhitaḥ | न तानि कश्चिन्माल्यानि तत्रारोपयिता नरः। न च वै म्लानतां यान्ति न च शीर्यन्ति राघव।।3.73.22।। |
| 3.1.6 | 3.1.6 | 0.652 | puṣpair vanyaiḥ parikṣiptaṃ padminyā ca sapadmayā phalamūlāśanair dāntaiś cīrakṛṣṇājināmbaraiḥ | बलिहोमार्चितं पुण्यं ब्रह्मघोषनिनादितम्। पुष्पैश्चान्यैः परिक्षिप्तं पद्मिन्या च सपद्मया।।3.1.6।। फलमूलाशनैर्दान्तैश्चीर |
| 3.37.19 | 3.39.18 | 0.652 | ahaṃ tasya prabhāvajño na yuddhaṃ tena te kṣamam raṇe rāmeṇa yudhyasva kṣamāṃ vā kuru rākṣasa | अहं तस्य प्रभावज्ञो न युद्धं तेन ते क्षमम्। बलिं वा नमुचिं वापि हन्याद्धि रघुनन्दनः।।3.39.18।। |
| 3.41.23 | 3.43.24 | 0.652 | paśya lakṣmaṇa vaidehyāḥ spṛhāṃ mṛgagatām imām rūpaśreṣṭhatayā hy eṣa mṛgo 'dya na bhaviṣyati | पश्य लक्ष्मण वैदेह्याः स्पृहां मृगगतामिमाम्। रूपश्रेष्ठतया ह्येष मृगोऽद्य न भविष्यति।।3.43.24।। न वने नन्दनोद्धेशे न चैत |
| 3.55.7 | 3.57.7 | 0.652 | rākṣasaiḥ sahitair nūnaṃ sītāyā īpsito vadhaḥ kāñcanaś ca mṛgo bhūtvā vyapanīyāśramāt tu mām | राक्षसैस्सहितैर्नूनं सीताया ईप्सितो वधः। काञ्चनश्च मृगो भूत्वा व्यपनीयाश्रमात्तु माम्।।3.57.7।। दूरं नीत्वा तु मारीचो रा |
| 3.43.10 | 3.45.11 | 0.653 | devi devamanuṣyeṣu gandharveṣu patatriṣu rākṣaseṣu piśāceṣu kiṃnareṣu mṛgeṣu ca | देवि देवमनुष्येषु गन्धर्वेषु पतत्रिषु।।3.45.11।। राक्षसेषु पिशाचेषु किन्नरेषु मृगेषु च। दानवेषु च घोरेषु स न विद्येत शोभ |
| 3.70.26 | 3.74.32 | 0.653 | anujñātā tu rāmeṇa hutvātmānaṃ hutāśane jvalatpāvakasaṃkāśā svargam eva jagāma sā | इत्युक्ता जटिला वृद्धा चीरकृष्णाजिनाम्बरा। तस्मिन्मुहूर्ते शबरी देहं जीर्णं जिहासती।।3.74.32।। अनुज्ञाता तु रामेण हुत्वा |
| 3.22.31 | 3.23.32 | 0.654 | śyena gāmī pṛthugrīvo yajñaśatrur vihaṃgamaḥ durjayaḥ karavīrākṣaḥ paruṣaḥ kālakārmukaḥ | श्येनगामी पृथुग्रीवो यज्ञशत्रुर्विहङ्गमः। दुर्जयः करवीराक्षः परुषः कालकार्मुकः।।3.23.32।। मेघमाली महामाली सर्वास्यो रुधि |
| 3.58.4 | 3.60.4 | 0.654 | udbhramann iva vegena vikṣipan raghunandanaḥ tatra tatroṭajasthānam abhivīkṣya samantataḥ | उद्भ्रमन्निव वेगेन विक्षिपन्रघुनन्दनः। तत्र तत्रोटजस्थानमभिवीक्षय समन्ततः।।3.60.4।। ददर्श पर्णशालां च रहितां सीतया तदा।  |
| 3.35.8 | 3.37.8 | 0.655 | na ca pitrā parityakto nāmaryādaḥ kathaṃ cana na lubdho na ca duḥśīlo na ca kṣatriyapāṃsanaḥ | न च पित्रा परित्यक्तो नामर्यादः कथञ्चन। न लुब्धो न च दुश्शीलो न च क्षत्रियपांसनः।।3.37.8।। न च धर्मगुणैर्हीनः कौसल्यानन् |
| 3.33.2 | 3.35.3 | 0.656 | tat kāryam anugamyātha yathāvad upalabhya ca doṣāṇāṃ ca guṇānāṃ ca saṃpradhārya balābalam | तत्कार्यमनुगम्याथ यथावदुपलभ्य च। दोषाणां च गुणानां च सम्प्रधार्य बलाबलम्।3.35.2।। इति कर्तव्यमित्येव कृत्वा निश्चयमात्मन |
| 3.44.11 | 3.46.11 | 0.656 | śubhāṃ ruciradantauṣṭhīṃ pūrṇacandranibhānanām āsīnāṃ parṇaśālāyāṃ bāṣpaśokābhipīḍitām | शुभां रुचिरदन्तोष्ठीं पूर्णचन्द्रनिभाननाम्।।3.46.11।। आसीनां पर्णशालायां बाष्पशोकाभिपीडिताम्। स तां पद्मपलाशाक्षीं पीतकौ |
| 3.47.13 | 3.49.14 | 0.656 | rājyāc cyutam asiddhārthaṃ rāmaṃ parimitāyuṣam kair guṇair anuraktāsi mūḍhe paṇḍitamānini | राज्याच्च्युतमसिद्धार्थं रामं परिमितायुषम्। कैर्गुणैरनुरक्तासि मूढे पण्डितमानिनि।।3.49.14।। यः स्त्रिया वचनाद्राज्यं विह |
| 3.68.6 | 3.72.6 | 0.656 | vimāne bhāsvare tiṣṭhan haṃsayukte yaśaskare prabhayā ca mahātejā diśo daśa virājayan | विमाने भास्वरे तिष्ठन्हंसयुक्ते यशस्करे। प्रभया च महातेजा दिशो दश विराजयन्।।3.72.6।। सोऽन्तरिक्षगतो रामं कबन्धो वाक्यमब् |

## Critical-only — 159, sample of 30

| Locus | Text |
|---|---|
| 3.1.3 | śaraṇyaṃ sarvabhūtānāṃ susamṛṣṭājiraṃ sadā pūjitaṃ copanṛttaṃ ca nityam apsarasāṃ gaṇaiḥ |
| 3.1.5 | āraṇyaiś ca mahāvṛkṣaiḥ puṇyaiḥ svāduphalair vṛtam balihomārcitaṃ puṇyaṃ brahmaghoṣanināditam |
| 3.1.8 | tad brahmabhavanaprakhyaṃ brahmaghoṣanināditam brahmavidbhir mahābhāgair brāhmaṇair upaśobhitam |
| 3.2.3 | niṣkūjanānāśakuni jhillikā gaṇanāditam lakṣmaṇānugato rāmo vanamadhyaṃ dadarśa ha |
| 3.2.12 | adharmacāriṇau pāpau kau yuvāṃ munidūṣakau ahaṃ vanam idaṃ durgaṃ virāgho nāma rākṣasaḥ |
| 3.3.21 | anupasthīyamāno māṃ saṃkruddho vyajahāra ha tava prasādān mukto 'ham abhiśāpāt sudāruṇāt |
| 3.3.23 | taṃ kṣipram abhigaccha tvaṃ sa te śreyo vidhāsyati avaṭe cāpi māṃ rāma nikṣipya kuśalī vraja |
| 3.4.4 | tasya devaprabhāvasya tapasā bhāvitātmanaḥ samīpe śarabhaṅgasya dadarśa mahad adbhutam |
| 3.4.6 | suprabhābharaṇaṃ devaṃ virajo 'mbaradhāriṇam tadvidhair eva bahubhiḥ pūjyamānaṃ mahātmabhiḥ |
| 3.4.8 | pāṇḍurābhraghanaprakhyaṃ candramaṇḍalasaṃnibham apaśyad vimalaṃ chatraṃ citramālyopaśobhitam |
| 3.4.12 | ime ca puruṣavyāghra ye tiṣṭhanty abhito ratham śataṃ śataṃ kuṇḍalino yuvānaḥ khaḍgapāṇayaḥ |
| 3.4.19 | jitavantaṃ kṛtārthaṃ ca draṣṭāham acirād imam karma hy anena kartavyaṃ mahad anyaiḥ suduṣkaram |
| 3.5.2 | vaikhānasā vālakhilyāḥ saṃprakṣālā marīcipāḥ aśmakuṭṭāś ca bahavaḥ patrāhārāś ca tāpasāḥ |
| 3.5.3 | dantolūkhalinaś caiva tathaivonmajjakāḥ pare munayaḥ salilāhārā vāyubhakṣās tathāpare |
| 3.5.4 | ākāśanilayāś caiva tathā sthaṇḍilaśāyinaḥ tathordhvavāsino dāntās tathārdrapaṭavāsasaḥ |
| 3.5.5 | sajapāś ca taponityās tathā pañcatapo'nvitāḥ sarve brāhmyā śriyā juṣṭā dṛḍhayogasamāhitāḥ |
| 3.5.12 | prāpnoti śāśvatīṃ rāma kīrtiṃ sa bahuvārṣikīm brahmaṇaḥ sthānam āsādya tatra cāpi mahīyate |
| 3.6.10 | citrakūṭam upādāya rājyabhraṣṭo 'si me śrutaḥ ihopayātaḥ kākutstho devarājaḥ śatakratuḥ |
| 3.7.4 | udayanntaṃ dinakaraṃ dṛṣṭvā vigatakalmaṣāḥ sutīkṣṇam abhigamyedaṃ ślakṣṇaṃ vacanam abruvan |
| 3.7.9 | tāvad icchāmahe gantum ity uktvā caraṇau muneḥ vavande sahasaumitriḥ sītayā saha rāghavaḥ |
| 3.7.14 | phullapaṅkajaṣaḍāni prasannasalilāni ca kāraṇḍavavikīrṇāni taṭākāni sarāṃsi ca |
| 3.7.15 | drakṣyase dṛṣṭiramyāṇi giriprasravaṇāni ca ramaṇīyāny araṇyāni mayūrābhirutāni ca |
| 3.8.20 | snehāc ca bahumānāc ca smāraye tvāṃ na śikṣaye na kathaṃ cana sā kāryā hṛhītadhanuṣā tvayā |
| 3.10.6 | padmapuṣkarasaṃbādhaṃ gajayūthair alaṃkṛtam sārasair haṃsakādambaiḥ saṃkulaṃ jalacāribhiḥ |
| 3.10.23 | yeṣām uṣitavān pūrvaṃ sakāśe sa mahāstravit kva cit paridaśān māsān ekaṃ saṃvatsaraṃ kva cit |
| 3.10.40 | tatrāgastyāśramapadaṃ gatvā yojanam antaram ramaṇīye vanoddeśe bahupādapa saṃvṛte |
| 3.10.44 | sutīkṣṇenopadiṣṭena gatvā tena pathā sukham idaṃ paramasaṃhṛṣṭo vākyaṃ lakṣmaṇam abravīt |
| 3.10.53 | ihaikadā kila krūro vātāpir api celvalaḥ bhrātarau sahitāv āstāṃ brāhmaṇaghnau mahāsurau |
| 3.10.74 | hastihastair vimṛditān vānarair upaśobhitān mattaiḥ śakunisaṃghaiś ca śataśaḥ pratināditān |
| 3.10.79 | nigṛhya tarasā mṛtyuṃ lokānāṃ hitakāmyayā dakṣiṇā dik kṛtā yena śaraṇyā puṇyakarmaṇā |

## Gita Supersite-only — 341, sample of 30

| Locus | Text |
|---|---|
| 3.1.3 | शरण्यं सर्वभूतानां सुसम्मृष्टाजिरं सदा। मृगैर्बहुभिराकीर्णं पक्षिसङ्घैस्समावृतम्।।3.1.3।। |
| 3.2.13 | इयं नारी वरारोहा मम भार्या भविष्यति। युवयोः पापयोश्चाहं पास्यामि रुधिरं मृधे।।3.2.13।। |
| 3.3.1 | इत्युक्त्वा लक्ष्मणश्श्रीमान्विराधे प्रहसन्निव। कोभवान्वनमभ्येत्य चरिष्यसि यथासुखम्।।3.3.1।। |
| 3.3.14 | स विद्धो न्यस्य वैदेहीं शूलमुद्यम्य राक्षसः। अभ्यद्रवत्सुसङ्कृद्धस्तदा रामं सलक्ष्मणम्।।3.3.14।। |
| 3.3.16 | अथ तौ भ्रातरौ दीप्तं शरवर्षं ववर्षतुः। विराधे राक्षसे तस्मिन् कालान्तकयमोपमे।।3.3.16।। |
| 3.3.17 | स प्रहस्य महारौद्रः स्थित्वाजृम्भत राक्षसः। जृम्भमाणस्य ते बाणाः कायान्निष्पेतुराशुगाः।।3.3.17।। |
| 3.3.18 | स्पर्शात्तु वरदानेन प्राणान्सम्रोध्य राक्षसः। विराधः शूलमुद्यम्य राघवावभ्यधावत।।3.3.18।। |
| 3.3.20 | तद्रामविशिखच्छिन्नं शूलं तस्यकराद्भुवि। पपाताशनिना छिन्नं मेरोरिव शिलातलम्।।3.3.20।। |
| 3.3.21 | तौ खड्गौ क्षिप्रमुद्यम्य कृष्णसर्पोपमौशुभौ। तूर्णमापेततुस्तस्य तदा प्रहरतां बलात्।।3.3.21।। |
| 3.3.22 | स वध्यमानः सुभृशं भुजाभ्यां परिरभ्यतौ। अप्रकम्प्यौ नरव्याघ्रौ रौद्रः प्रस्थातुमैच्छत।।3.3.22।। |
| 3.3.23 | तस्याभिप्रायमाज्ञाय रामो लक्ष्मणमब्रवीत्। वहत्वयमलं तावत्पथाऽनेन तु राक्षसः।।3.3.23।। |
| 3.3.24 | यथा चेच्छति सौमित्रे तथा वहतु राक्षसः। अयमेव हि नः पन्था येन याति निशाचरः।।3.3.24।। |
| 3.3.25 | स तु स्वबलवीर्येण समुत्क्षिप्य निशाचरः। बालाविव स्कन्धगतौ चकारातिबलोद्धतः।।3.3.25।। |
| 3.3.26 | तावारोप्य ततः स्कन्धं राघवौ रजनीचरः। विराधो विनदन्घोरं जगामाभिमुखो वनम्।।3.3.26।। |
| 3.3.27 | वनं महामेघनिभं प्रविष्टो द्रुमैर्महद्भिर्विविधैरुपेतम्। नानाविधैः पक्षिकुलैर्विचित्रं शिवायुतं व्यालमृगैर्विकीर्णम्।।3.3.27।। |
| 3.4.1 | ह्रियमाणौ तु तौ दृष्ट्वा वैदेही रामलक्ष्मणौ। उच्चैस्स्वरेण चुक्रोश प्रगृह्य सुमहाजाभुजौ।।3.4.1।। |
| 3.4.2 | एष दाशरथी रामः सत्यवान् शीलवान् शुचिः। रक्षसा रौद्ररूपेण ह्रियते सहलक्ष्मणः।।3.4.2।। |
| 3.4.3 | मामृका भक्षयिष्यन्ति शार्दूलाद्वीपिनस्तथा। मां हरोत्सृज काकुत्स्थौ नमस्ते राक्षसोत्तम।।3.4.3।। |
| 3.4.4 | तस्यास्तद्वचनं श्रुत्वा वैदेह्या रामलक्ष्मणौ। वेगं प्रचक्रतुर्वीरौ वधे तस्य दुरात्मनः।।3.4.4।। |
| 3.4.7 | मुष्टिभिर्जानुभिः पद्भिः सूदयन्तौ तु राक्षसम्। उद्यम्योद्यम्य चाप्येनं स्थण्डिले निष्पिपेषतुः।।3.4.7।। |
| 3.4.8 | स विद्धो बहुभिर्बाणैः खङ्गाभ्यां च परिक्षतः। निष्पिष्टो बहुधा भूमौ न ममार स राक्षसः।।3.4.8।। |
| 3.4.9 | तं प्रेक्ष्य रामः सुभृशमवध्यमचलोपमम्। भयेष्वभयदश्श्रीमानिदं वचनमब्रवीत्।।3.4.9।। |
| 3.4.10 | तपसा पुरुषव्याघ्र राक्षसोऽयं न शक्यते। शस्त्रेण युधि निर्जेतुं राक्षसं निखनावहे।।3.4.10।। |
| 3.4.11 | कुञ्जरस्येव रौद्रस्य राक्षसस्यास्य लक्ष्मण। वनेऽस्मिन् सुमहच्छ्वभ्रं खन्यतां रौद्रवर्चसः।।3.4.11।। |
| 3.4.12 | इत्युक्त्वा लक्ष्मणं रामः प्रदरः खन्यतामिति। तस्थौ विराधमाक्रम्य कण्ठे पादेन वीर्यवान्।।3.4.12।। |
| 3.4.13 | तच्छ्रुत्वा राघवेणोक्तं राक्षसः प्रश्रितं वचः। इदं प्रोवाच काकुत्थ्सं विराधः पुरुषर्षभम्।।3.4.13।। |
| 3.4.14 | हतोऽस्मि पुरुषव्याघ्र शक्रतुल्यबलेन वै। मया तु पूर्वं त्वं मोहान्न ज्ञातः पुरुषर्षभ।।3.4.14।। |
| 3.4.19 | तव प्रसादान्मुक्तोऽहमिहशापात्सुदारुणात्। भुवनं स्वं गमिष्यामि स्वस्ति वोऽस्तु परन्तप।।3.4.19।। |
| 3.4.24 | तच्छ्रुत्वा राघवो वाक्यं लक्ष्मणं व्यादिदेश ह। कुञ्जरस्येव रौद्रस्य राक्षसस्यास्य लक्ष्मण।।3.4.24।। वनेऽस्मिन् सुमहच्छ्वभ्रं खन्यतां रौदकर्मणः। इत्युक |
| 3.4.26 | ततः खनित्रमादाय लक्ष्मणश्श्वभ्रमुत्तमम्। अखनत्पार्श्वतस्तस्य विराधस्य महात्मनः।।3.4.26।। |

## Full data

Complete machine-readable results alongside this file: `scratchpad/aranya_gitasupersite_alignment.json`

_Dr. Mārcis Gasūns_
