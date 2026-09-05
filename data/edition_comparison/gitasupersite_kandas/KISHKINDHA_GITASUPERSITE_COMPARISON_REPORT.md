_Created: 12-07-2026 · Last updated: 05-09-2026_

# Kiṣkindhākāṇḍa (IV): Critical (GRETIL/Baroda) vs Gita Supersite

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
| 1987 | 2235 | 59 | 1713 | 1423 | 222 | 68 | 215 | 463 |

## Major differences (sim < 0.6) — 68 pairs, showing up to 60

| Critical locus | Gita Supersite locus | sim | Critical text | Gita Supersite text |
|---|---|---:|---|---|
| 4.42.45 | 4.43.47 | 0.319 | nānākārāṇi vāsāṃsi phalanty anye nagottamāḥ muktāvaidūryacitrāṇi bhūṣaṇāni tathaiva ca | मुक्ता वैढूर्यचित्राणि भूषणानि तथैव च। स्त्रीणां चाप्यनुरूपाणि पुरुषाणां तथैव च।।4.43.47।। सर्वर्तुसुख सेव्यानि फलन्त्यन |
| 4.49.26 | 4.50.33 | 0.359 | kāñcanabhramarāṃś caiva madhūni ca samantataḥ maṇikāñcanacitrāṇi śayanāny āsanāni ca | मणिकाञ्चनचित्राणि शयनान्यासनानि च।।4.50.33।। महार्हाणि चयानानि ददृशुस्ते समन्ततः। हैमराजतकांस्यानां भाजनानां च संञ्चयान् |
| 4.42.42 | 4.43.44 | 0.378 | nistulābhiś ca muktābhir maṇibhiś ca mahādhanaiḥ udbhūtapulinās tatra jātarūpaiś ca nimnagāḥ | उद्भूतपुलिनास्तत्र जातरूपैश्च निम्नगाः। सर्वरत्नमयैश्चित्रैरवगाढा नगोत्तमैः।।4.43.44।। जातरूपमयैश्चापि हुताशनसमप्रभैः। |
| 4.20.2 |  | 0.396 | sā samāsādya bhartāraṃ paryaṣvajata bhāminī iṣuṇābhihataṃ dṛṣṭvā vālinaṃ kuñjaropamam | इषुणाऽभिहतं दृष्ट्वा वालिनं कुञ्जरोपमम्4.20.2।। वानरेन्द्र महेन्द्राभं शोकसन्तप्तमानसा। तारा तरुमिवोन्मूलं पर्यदेवयदातुर |
| 4.41.18 | 4.42.22 | 0.416 | nātyāsādayitavyās te vānarair bhīmavikramaiḥ nādeyaṃ ca phalaṃ tasmād deśāt kiṃ cit plavaṃgamaiḥ | नादेयं च फलं तस्माद्देशात्किञ्चित् प्लवङ्गमैः।।4.42.22।। दुरासदा हि ते वीरा स्सत्त्ववन्तो महाबलाः। फलमूलानि ते तत्र रक्ष |
| 4.38.10 | 4.39.10 | 0.426 | tato nagendrasaṃkāśais tīkṣṇa daṃṣṭrair mahābalaiḥ kṛtsnā saṃchāditā bhūmir asaṃkhyeyaiḥ plavaṃgamaiḥ | ततो नगेन्द्रसङ्काशैस्तीक्ष्णदंष्ट्रैर्महाबलैः। कृत्स्ना सञ्छादिता भूमिरसङ्ख्येयैः प्लवङ्गमैः।।4.39.10।। निमेषान्तरमात्रे |
| 4.39.20 | 4.40.20 | 0.434 | sarasvatīṃ ca sindhuṃ ca śoṇaṃ maṇinibhodakam mahīṃ kālamahīṃ caiva śailakānanaśobhitām | नदीं भागीरथीं रम्यां सरयूं कौशिकीं तथा।।4.40.20।। कालिन्दीं यमुनां रम्यां यामुनं च महागिरिम्। सरस्वतीं च सिन्धुं च शोणं  |
| 4.51.13 | 4.52.13 | 0.434 | teṣām api hi sarveṣām anumānam upāgatam gacchāmaḥ praviśāmeti bhartṛkāryatvarānvitāḥ | साध्वत्र प्रविशामेति मया तूक्ताः प्लवङ्गमाः। तेषामपि हि सर्वेषामनुमानमुपागतम्।।4.52.13।। |
| 4.65.9 | 4.66.9 | 0.453 | abhiśāpād abhūt tāta vānarī kāmarūpiṇī duhitā vānarendrasya kuñjarasya mahātmanaḥ | विख्याता त्रिषु लोकेषु रूपेणाप्रतिमा भुवि। अभिशापादभूत्तात वानरी कामरूपिणी।।4.66.9।। |
| 4.37.5 | 4.38.6 | 0.458 | evaṃ bhavatu gacchāmaḥ stheyaṃ tvacchāsane mayā tam evam uktvā sugrīvo lakṣmaṇaṃ śubhalakṣmaṇam | तमेवमुक्त्वा सुग्रीवो लक्ष्मणं शुभलक्षणम्। विसर्जयामास तदा तारामन्याश्च योषितः।।4.38.6।। |
| 4.37.24 | 4.38.24 | 0.46 | evam uktas tu sugrīvo rāmaṃ vacanam abravīt | एवमुक्तस्तु सुग्रीवो रामं वचनमब्रवीत्।।4.38.24।। प्रणष्टा श्रीश्च कीर्तिश्च कपिराज्यं च शाश्वतम्। त्वत्प्रसादान्महाबाहो  |
| 4.39.22 | 4.40.24 | 0.463 | pattanaṃ kośakārāṇāṃ bhūmiṃ ca rajatākarām sarvam etad vicetavyaṃ mṛgayadbhir tatas tataḥ | सर्वमेतद्विचेतव्यं मृगयद्भिस्ततस्ततः। रामस्य दयितां भार्यां सीतां दशरथस्नुषाम्।।4.40.24।। |
| 4.41.7 | 4.42.8 | 0.466 | pratyak srotogamāś caiva nadyaḥ śītajalāḥ śivāḥ tāpasānām araṇyāni kāntārā girayaś ca ye | प्रत्यक्स्रोतोगमाश्चैव नद्यश्शीतजलाश्शिवाः।।4.42.8।। तापसानामरण्यानि कान्तारा गिरयश्च ये। तत्रस्थलीं मरुप्रायामत्युच्चशि |
| 4.26.8 |  | 0.467 | tat samutthena śokena bāṣpopahatacetasaṃ taṃ śocamānaṃ kākutsthaṃ nityaṃ śokaparāyaṇam | आविवेश न तं निद्रा निशासु शयनं गतम्। तत्समुत्थेन शोकेन बाष्पोपहतचेतसम्4.27.32।। |
| 4.57.29 | 4.58.31 | 0.467 | asmākam api sauvarṇaṃ divyaṃ cakṣurbalaṃ tathā tasmād āhāravīryeṇa nisargeṇa ca vānarāḥ | तस्मादाहारवीर्येण निसर्गेण च वानराः। आयोजनशतात्साग्राद्वयं पश्याम नित्यशः।।4.58.31।। |
| 4.24.33 |  | 0.469 | janaṃ ca paśyasīmaṃ tvaṃ kasmāc chokābhipīḍitam prahṛṣṭam iva te vaktraṃ gatāsor api mānada | प्रहृष्टमिव ते वक्त्रं गतासोरपि मानद आस्तार्कसमवर्णं च लक्ष्यते जीवतो यथा4.25.41।। |
| 4.64.24 | 4.65.24 | 0.469 | tasmāt kalatravat tāta pratipālyaḥ sadā bhavān api caitasya kāryasya bhavān mūlam ariṃdama | अपि चैतस्य कार्यस्य भवान्मूलमरिन्दम। तस्मात्कळत्रवत्तात प्रतिपाल्यस्सदा भवान्।।4.65.24।। |
| 4.23.4 |  | 0.47 | sugrīva eva vikrānto vīra sāhasika priya ṛkṣavānaramukhyās tvāṃ balinaṃ paryupāsate | सुग्रीवस्य वशं प्राप्तो विधिरेषभवत्यहो। सुग्रीव एव विक्रान्तो वीर साहसिकप्रिय4.23.4।। |
| 4.42.27 | 4.43.29 | 0.471 | krauñcasya śikharaṃ cāpi nirīkṣya ca tatas tataḥ avṛkṣaṃ kāmaśailaṃ ca mānasaṃ vihagālayam | अवृक्षं कामशैलं च मानसं विहगालयम्। न गतिस्तत्र भूतानां देवदानव रक्षसाम्।।4.43.29।। |
| 4.32.25 | 4.33.63 | 0.473 | tataḥ sugrīvam āsīnaṃ kāñcane paramāsane mahārhāstaraṇopete dadarśādityasaṃnibham | तत स्सुग्रीवमासीनं काञ्चने परमासने। महार्हास्तरणोपेते ददर्शादित्यसन्निभम्।।4.33.63।। दिव्याभणचित्राङ्गं दिव्यरूपं यशस्वि |
| 4.42.47 | 4.43.49 | 0.473 | mahārhāṇi vicitrāṇi haimāny anye nagottamāḥ śayanāni prasūyante citrāstāraṇavanti ca | शयनानि प्रसूयन्ते चित्रास्तरणवन्ति च। मनःकान्तानि माल्यानि फलन्त्यत्रापरे द्रुमाः।।4.43.49।। |
| 4.42.49 | 4.43.50 | 0.475 | striyaś ca guṇasaṃpannā rūpayauvanalakṣitāḥ gandharvāḥ kiṃnarā siddhā nāgā vidyādharās tathā | पानानि च महार्हाणि भक्ष्याणि विविधानि च। स्त्रियश्च गुणसम्पन्ना रूपयौवनलक्षिताः।।4.43.50।। |
| 4.58.24 | 4.59.22 | 0.475 | apakṣo hi kathaṃ pakṣī karma kiṃ cid upakramet yat tu śakyaṃ mayā kartuṃ vāgbuddhiguṇavartinā | तच्छृत्वाऽपि हि मे बुद्धिर्नासीत्काचित्पराक्रमे।।4.59.22।। अपक्षो हि कथं पक्षी कर्म किञ्चिदुपक्रमे। |
| 4.18.40 | 4.18.46 | 0.478 | evam uktas tu rāmeṇa vālī pravyathito bhṛśam pratyuvāca tato rāmaṃ prāñjalir vānareśvaraḥ | प्रत्युवाच ततो रामं प्राञ्जलिर्वानरेश्वरः।।4.18.46।। यत्त्वमात्थ नरश्रेष्ठ तदेवं नात्र संशयः। |
| 4.19.24 |  | 0.482 | śārdūlenāmiṣasyārthe mṛgarājaṃ yathā hatam arcitaṃ sarvalokasya sapatākaṃ savedikam | अर्चितं सर्वलोकस्य सपताकं सवेदिकम्4.19.24।। नागहेतोस्सुपर्णेन चैत्यमुन्मथितं यथा। |
| 4.65.11 | 4.66.10 | 0.482 | acarat parvatasyāgre prāvṛḍambudasaṃnibhe vicitramālyābharaṇā mahārhakṣaumavāsinī | दुहिता वानरेन्द्रस्य कुञ्जरस्य महात्मनः। मानुषं विग्रहं कृत्वा रूपयौवनशालिनी।।4.66.10।। विचित्रमाल्याभरणा महार्हक्षौमवास |
| 4.39.31 | 4.43.25 | 0.483 | rāvaṇaḥ saha vaidehyā mārgitavyas tatas tataḥ tataḥ samudradvīpāṃś ca subhīmān draṣṭum arhatha | तस्य चन्द्रनिकाशेषु पर्वतेषु गुहासु च। रावणः सह वैदेह्या मार्गितव्यस्ततस्ततः।।4.43.25।। |
| 4.49.25 | 4.50.32 | 0.483 | dadṛśus tatra harayo gṛhamukhyāni sarvaśaḥ puṣpitān phalino vṛkṣān pravālamaṇisaṃnibhān | पुष्पितान्फलिनो वृक्षान्प्रवाळमणिसन्निभान्।।4.50.32।। काञ्चनभ्रमरांश्चैव मधूनि च समन्ततः। |
| 4.50.6 | 4.51.6 | 0.483 | puṣpitāḥ phālavantaś ca puṇyāḥ surabhigandhinaḥ ime jāmbūnadamayāḥ pādapāḥ kasya tejasā | पुष्पिताः फलवन्तश्च पुण्यास्सुरभिगन्धिनः।।4.51.6।। इमे जाम्बूनदमयाः पादपाः कस्य तेजसा। काञ्चनानि च पद्मानि जातानि विमले  |
| 4.53.3 | 4.54.3 | 0.483 | āpūryamāṇaṃ śaśvac ca tejobalaparākramaiḥ śaśinaṃ śuklapakṣādau vardhamānam iva śriyā | आपूर्यमाणं शश्वच्च तेजोबलपराक्रमैः। शशिनं शुक्लपक्षादौ वर्धमानमिव श्रिया।।4.54.3।। बृहस्पतिसमं बुद्ध्या विक्रमे सदृशं पि |
| 4.57.28 | 4.58.30 | 0.483 | garhitaṃ tu kṛtaṃ karma yena sma piśitāśanāḥ ihastho 'haṃ prapaśyāmi rāvaṇaṃ jānakīṃ tathā | इहस्थोऽहं प्रपश्यामि रावणं जानकीं तथा। अस्माकमपि सौवर्णं दिव्यं चक्षुर्बलं तथा।।4.58.30।। |
| 4.29.1 |  | 0.484 | guhāṃ praviṣṭe sugrīve vimukte gagane ghanaiḥ varṣarātroṣito rāmaḥ kāmaśokābhipīḍitaḥ | गुहं प्रविष्टे सुग्रीवे विमुक्ते गगने घनैः। वर्षरात्रोषितो रामः कामशोकाभिपीडितः4.30.1।। पाण्डुरं गगनं दृष्ट्वा विमलं चन् |
| 4.1.22 | 4.1.46 | 0.485 | nūnaṃ paravaśā sītā sāpi śocaty ahaṃ yathā śyāmā padmapalāśākṣī mṛdubhāṣā ca me priyā | वसन्तो यदि तत्रापि यत्र मे वसति प्रिया। नूनं परवशा सीता सापि शोचत्यहं यथा।।4.1.46।। |
| 4.41.2 | 4.42.2 | 0.485 | athāhūya mahātejāḥ suṣeṇaṃ nāma yūthapam tārāyāḥ pitaraṃ rājā śvaśurabhīmavikramam | तारायाः पितरं राजा श्वशुरं भीमविक्रमम्। अब्रवीत्प्राञ्जलिर्वाक्यमभिगम्य प्रणम्य च।।4.42.2।। |
| 4.10.4 |  | 0.486 | tvam eva rājā mānārhaḥ sadā cāhaṃ yathāpurā nyāsabhūtam idaṃ rājyaṃ tava niryātayāmy aham | न्यासभूतमिदं राज्यं तव निर्यातयाम्यहम्। मा च रोषं कृथास्सौम्य मयि शत्रुनिबर्हण4.10.9।। |
| 4.42.28 | 4.43.30 | 0.486 | na gatis tatra bhūtānāṃ devadānavarakṣasām sa ca sarvair vicetavyaḥ sasānuprasthabhūdharaḥ | स च सर्वैर्विचेतव्यस्ससानुप्रस्थभूधरः। क्रौञ्चं गिरिमतिक्रम्य मैनाको नाम पर्वतः।।4.43.30।। |
| 4.49.22 | 4.50.29 | 0.487 | mahadbhiḥ kāñcanair vṛkṣair vṛtaṃ bālārka saṃnibhaiḥ jātarūpamayair matsyair mahadbhiś ca sakacchapaiḥ | जातरूपमयैर्मत्स्यैर्महद्भिश्च सकच्छपैः।।4.50.29।। नळिनीस्तत्र ददृशुः प्रसन्नसलिलावृताः। |
| 4.1.40 | 4.1.81 | 0.489 | ketakoddālakāś caiva śirīṣāḥ śiṃśapā dhavāḥ śālmalyaḥ kiṃśukāś caiva raktāḥ kurabakās tathā | शाल्मल्यः किंशुकाश्चैव रक्ताः कुरवकास्तथा।।4.1.81।। त्रिनिशा नक्तमालाश्च चन्दनास्स्यन्दनास्तथा। |
| 4.19.28 |  | 0.489 | ruroda sā patiṃ dṛṣṭvā saṃditaṃ mṛtyudāmabhiḥ tām avekṣya tu sugrīvaḥ krośantīṃ kurarīm iva | तामवेक्ष्य तु सुग्रीवः क्रोशन्तीं कुररीमिव। विषादमगमत्कष्टं दृष्ट्वा चाङ्गदमागतम्4.19.28।। |
| 4.26.7 |  | 0.489 | udayābhyuditaṃ dṛṣṭvā śaśāṅkaṃ ca viśeṣataḥ āviveśa na taṃ nidrā niśāsu śayanaṃ gatam | हृतां हि भार्यां स्मरतः प्राणेभ्योऽपि गरीयसीम्। उदयाभ्युदितं दृष्ट्वा शशाङ्कं च विशेषतः4.27.31।। |
| 4.58.25 | 4.59.23 | 0.489 | śrūyatāṃ tat pravakṣyāmi bhavatāṃ pauruṣāśrayam vāṅmatibhyāṃ hi sārveṣāṃ kariṣyāmi priyaṃ hi vaḥ | यत्तु शक्यं मया कर्तुं वाग्बुद्धिगुणवर्तिना।।4.59.23।। श्रूयतां तत्प्रवक्ष्यामि भवतां पौरुषाश्रयम्। |
| 4.39.29 | 4.40.30 | 0.491 | suvarṇarūpyakaṃ caiva suvarṇākaramaṇḍitam yavadvīpam atikramya śiśiro nāma parvataḥ | रत्नवन्तं यवद्वीपं सप्तराज्योपशोभितम्। सुवर्णरूप्यकं चैव सुवर्णाकरमण्डितम्।।4.40.30।। यवद्वीपमतिक्रम्य शिशिरो नाम पर्वतः |
| 4.40.8 | 4.41.8 | 0.491 | sahasraśirasaṃ vindhyaṃ nānādrumalatāvṛtam narmadāṃ ca nadīṃ durgāṃ mahoraganiṣevitām | सहस्रशिरसं विन्ध्यं नानाद्रुमलतायुतम्। नर्मदां च नदीं रम्यां महोरगनिषेविताम्।।4.41.8।। ततो गोदावरीं रम्यां कृष्णवेणीं मह |
| 4.55.20 | 4.57.6 | 0.492 | bhrātur jaṭāyuṣas tasya janasthānanivāsinaḥ tasyaiva ca mama bhrātuḥ sakhā daśarathaḥ katham | तस्यैव च मम भ्रातुस्सखा दशरथः कथम्।।4.57.6।। यस्य रामः प्रियः पुत्रो ज्येष्ठो गुरुजनप्रियः। |
| 4.37.31 | 4.38.30 | 0.495 | arbudair arbudaśatair madhyaiś cāntaiś ca vānarāḥ samudraiś ca parārdhaiś ca harayo hariyūthapāḥ | शतैश्शतसहस्रैश्च वर्तन्ते कोटिभिश्च प्लवङ्गमाः। अयुतैश्चावृता वीराश्शङ्कुभिश्च परन्तप ।।4.38.30।। अर्बुदैरर्बुदशतैर्मध्य |
| 4.17.12 | 4.17.14 | 0.496 | sa dṛṣṭvā rāghavaṃ vālī lakṣmaṇaṃ ca mahābalam abravīt praśritaṃ vākyaṃ paruṣaṃ dharmasaṃhitam | तं दृष्ट्वा राघवं वाली लक्ष्मणं च महाबलम्। अब्रवीत्प्रश्रितं वाक्यं परुषं धर्मसंहितम्4.17.13।। त्वं नराधिपतेः पुत्रः प्र |
| 4.66.35 | 4.67.40 | 0.496 | vṛtaṃ nānāvidhair vṛkṣair mṛgasevitaśādvalam latākusumasaṃbādhaṃ nityapuṣpaphaladrumam | ततस्तं मारुतप्रख्यस्सहरिर्मारुतात्मजः।।4.67.40।। आरुरोह नगश्रेष्ठं महेन्द्रमरिमर्दनः। वृतं नानाविधैः वृक्षैर्मृगसेवितशाद |
| 4.19.26 |  | 0.5 | rāmaṃ rāmānujaṃ caiva bhartuś caivānujaṃ śubhā tān atītya samāsādya bhartāraṃ nihataṃ raṇe | अवष्टभ्य च तिष्ठन्तं ददर्श धनुरुत्तम्4.19.25।। रामं रामानुजं चैव भर्तुश्चैवानुजं शुभा। |
| 4.40.37 | 4.41.39 | 0.5 | sarparājo mahāghoro yasyāṃ vasati vāsukiḥ niryāya mārgitavyā ca sā ca bhogavatī purī | निर्याय मार्गितव्या च सा च भोगवती पुरी।।4.41.39।। तत्र चानन्तरा देशा ये केचन सुसम्वृताः। |
| 4.55.19 | 4.57.5 | 0.5 | yavīyaso guṇajñasya ślāghanīyasya vikramaiḥ tad iccheyam ahaṃ śrotuṃ vināśaṃ vānararṣabhāḥ | तदिच्छेयमहं श्रोतुं विनाशं वानरर्षभाः।।4.57.5।। भ्रातुर्जटायुषस्तस्य जनस्थाननिवासिनः। |
| 4.51.14 | 4.52.14 | 0.503 | tato gāḍhaṃ nipatitā gṛhya hastau parasparam idaṃ praviṣṭāḥ sahasā bilaṃ timirasaṃvṛtam | गच्छाम प्रविशामेति भर्तृकार्यत्वरान्विताः। ततो गाढं निपतिता गृह्य हस्तौ परस्परम्।।4.52.14।। |
| 4.58.23 | 4.59.21 | 0.503 | etam arthaṃ samagraṃ me supārśvaḥ pratyavedayat tac chrutvāpi hi me buddhir nāsīt kā cit parākrame | एष कालात्ययस्तावदिति कालविदां वरः।।4.59.21।। एतमर्थं समग्रं मे सुपार्श्वः प्रत्यवेदयत्। |
| 4.63.5 | 4.64.5 | 0.505 | sattvair mahadbhir vikṛtaiḥ krīḍadbhir vividhair jale vyāttāsyaiḥ sumahākāyair ūrmibhiś ca samākulam | सत्त्वैर्महद्भिर्विकृतैः क्रीडद्भिर्विविधैर्जले। व्यात्तास्यैस्सुमहाकायैरूर्मिभिश्च समाकुलम्।।4.64.5।। प्रसुप्तमिव चान्य |
| 4.3.17 |  | 0.508 | evaṃ māṃ paribhāṣantaṃ kasmād vai nābhibhāṣathaḥ | एवं मां परिभाषन्तं कस्माद्वै नाभिभाषथः4.3.19।। सुग्रीवो नाम धर्मात्मा कश्चिद्वानरयूथपः। वीरो विनिकृतो भ्रात्रा जगद्भ्रमत |
| 4.44.4 | 4.45.5 | 0.512 | pūrvāṃ diśaṃ prati yayau vinato hariyūthapaḥ | पूर्वां दिशं प्रतिययौ विनतो हरियूथपः।।4.45.5।। ताराङ्गदादिसहितः प्लवङ्गो  मारुतात्मजः। अगत्याचरितामाशां दक्षिणां हरियूथप |
| 4.42.10 | 4.43.11 | 0.519 | tatra mlecchān pulindāṃś ca śūrasenāṃs tathāiva ca prasthālān bharatāṃś caiva kurūṃś ca saha madrakaiḥ | तत्र म्लेच्छान्पुलिन्दांश्च शूरसेनांस्तथैव च। प्रस्थलान्भरतांश्चैव कुरूंश्च सह मद्रकैः।।4.43.11।। काम्बोजान्यवनां श्चैव  |
| 4.4.6 | 4.4.8 | 0.522 | rājā daśaratho nāma dyutimān dharmavatsalaḥ tasyāyaṃ pūrvajaḥ putro rāmo nāma janaiḥ śrutaḥ | तस्यायं पूर्वजः पुत्रो रामो नाम जनैः श्रुतः।।4.4.8।। शरण्यस्सर्वभूतानां पितुर्निर्देशपारगः। |
| 4.19.27 |  | 0.525 | samīkṣya vyathitā bhūmau saṃbhrāntā nipapāta ha supteva punar utthāya āryaputreti krośatī | तावतीत्य समासाद्य भर्तारं निहतं रणे4.19.26।। समीक्ष्य व्यथिता भूमौ सम्भ्रान्ता निपपात ह। |
| 4.38.32 | 4.39.38 | 0.54 | śarabhaḥ kumudo vahnir vānaro rambha eva ca ete cānye ca bahavo vānarāḥ kāmarūpiṇaḥ | शरभः कुमुदो वह्निर्वानरो रंह एव च। एते चान्ये च बहवो वानराः कामरूपिणः।।4.39.38।। आवृत्य पृथिवीं सर्वां पर्वतांश्च वनानि  |
| 4.40.11 | 4.41.11 | 0.543 | vidarbhān ṛṣikāṃś caiva ramyān māhiṣakān api tathā baṅgān kaliṅgāṃś ca kauśikāṃś ca samantataḥ | विदर्भानृषिकांश्चैव रम्यान्माहिषकानपि। तथा वङ्गान्कलिङ्गांश्च कौशिकांश्च समन्ततः।।4.41.11।। अन्वीक्ष्य दण्डकारण्यं सपर्व |

## Minor edits (sim 0.6–0.9) — 222 pairs, sample of 60

| Critical locus | Gita Supersite locus | sim | Critical text | Gita Supersite text |
|---|---|---:|---|---|
| 4.60.12 | 4.61.12 | 0.6 | yatnena mahatā bhūyo raviḥ samavalokitaḥ tulyaḥ pṛthvīpramāṇena bhāskaraḥ pratibhāti nau | मनश्च मे हतं भूयस्सन्निवर्त्यतु संश्रयम्। यत्नेन महता ह्यस्मिन्पुनस्सन्धाय चक्षुषी।।4.61.12।। यत्नेन महता भूयो भास्करः प |
| 4.11.42 |  | 0.602 | tān dṛṣṭvā patitāṃs tatra muniḥ śoṇitavipruṣaḥ utsasarja mahāśāpaṃ kṣeptāraṃ vālinaṃ prati | स तु विज्ञाय तपसा वानरेण कृतं हि तत्। उत्ससर्ज महाशापं क्षेप्तारं वालिनं प्रति4.11.52।। |
| 4.40.22 | 4.41.22 | 0.607 | nānāvidhair nagaiḥ phullair latābhiś copaśobhitam devarṣiyakṣapravarair apsarobhiś ca sevitam | नानाविधैर्नगै स्सर्वैलताभिश्चोपशोभितम्। देवर्षियक्षप्रवरैरप्सरोभिश्च सेवितम्।।4.41.22।। सिद्धचारणसङ्घैश्च प्रकीर्णं समनो |
| 4.32.19 | 4.33.19 | 0.609 | sa sapta kakṣyā dharmātmā yānāsanasamāvṛtāḥ praviśya sumahad guptaṃ dadarśāntaḥpuraṃ mahat | स सप्त कक्ष्या धर्मात्मा नानाजनसमाकुलाः। प्रविश्य सुमहद्गगुप्तं ददर्शान्तःपुरं महत्।।4.33.19।। हैमराजतपर्यङ्कैर्बहुभिश्च |
| 4.30.37 |  | 0.613 | athāṅgadavacaḥ śrutvā tenaiva ca samāgatau mantriṇo vānarendrasya saṃmatodāradarśinau | अथाङ्गदवचः श्रुत्वा तेनैव च समागतौ। मन्त्रिणौ वानरेन्द्रस्य सम्मतौ दारदर्शिनौ4.31.42।। प्लक्षश्चैव प्रभावश्च मन्त्रिणावर |
| 4.5.14 | 4.5.14 | 0.614 | tato hanūmān saṃtyajya bhikṣurūpam ariṃdamaḥ kāṣṭhayoḥ svena rūpeṇa janayām āsa pāvakam | ततो हनूमान्सन्त्यज्य भिक्षुरूपमरिन्दमः।।4.5.14।। काष्ठयोस्स्वेन रूपेण जनयामास पावकम्। दीप्यमानं ततो वह्निं ह्निं पुष्पैर |
| 4.40.36 | 4.41.37 | 0.614 | tatra bhogavatī nāma sarpāṇām ālayaḥ purī viśālarathyā durdharṣā sarvataḥ parirakṣitā | तत्र भोगवती नाम सर्पाणामालयः पुरी।।4.41.37।। विशालकक्ष्या दुर्धर्षा सर्वतः परिरक्षिता। रक्षिता पन्नगैर्घोरैस्तीक्ष्णदष्ट |
| 4.16.26 |  | 0.615 | vegenābhihato vālī nipapāta mahītale | ततस्तेन महातेजा वीयौटत्सिक्तः कपीश्वरः। वेगेनाभिहतो वाली निपपात महीतले4.16.36।। |
| 4.37.28 | 4.38.28 | 0.615 | ṛkṣāś cāvahitāḥ śūrā golāṅgūlāś ca rāghava kāntāra vanadurgāṇām abhijñā ghoradarśanāḥ | ऋक्षाश्चावहिताश्शूरा गोलाङ्गूलाश्च राघव। कान्तारवनदुर्गाणामभिज्ञा घोरदर्शनाः।।4.38.28।। देवगन्धर्वपुत्राश्च वानराः कामरू |
| 4.41.5 | 4.42.6 | 0.619 | surāṣṭrān saha bāhlīkāñ śūrābhīrāṃs tathaiva ca sphītāñjanapadān ramyān vipulāni purāṇi ca | सुराष्ट्रान्सहबाह्लीकान् श्चन्द्रचित्रांस्तथैव च।।4.42.6।। स्फीताञ्जनपदान्रम्यान्विपुलानि पुराणि च। पुन्नागगहनं कुक्षिं  |
| 4.37.12 | 4.38.12 | 0.621 | pāṇḍureṇātapatreṇa dhriyamāṇena mūrdhani śuklaiś ca bālavyajanair dhūyamānaiḥ samantataḥ | पाण्डुरेणातपत्रेण म्रियमाणेन मूर्धनि।।4.38.12।। शुक्लैश्च वालव्यजनैर्धूयमानैस्समन्ततः। शङ्खभेरीनिनादैश्च हरिभिश्चाभिवन्द |
| 4.38.2 | 4.39.2 | 0.622 | yad indro varṣate varṣaṃ na tac citraṃ bhaved bhuvi ādityo vā sahasrāṃśuḥ kuryād vitimiraṃ nabhaḥ | यदिन्द्रो वर्षते वर्षं न तच्चित्रं भवेत्क्वचित्। आदित्यो वा सहस्रांशुः कुर्याद्वितिमिरं नभः।।4.39.2।। चन्द्रमा रश्मिभिः  |
| 4.42.41 | 4.43.42 | 0.622 | mahārhamaṇipatraiś ca kāñcanaprabha kesaraiḥ nīlotpalavanaiś citraiḥ sa deśaḥ sarvatovṛtaḥ | तरुणादित्यसङ्काशैर्भान्ति तत्र जलाशयाः।।4.43.42।। महार्हमणिरत्नैश्च काञ्चनप्रभकेसरैः। निलोत्पलवनैश्चित्रै स्स देश स्सर्व |
| 4.17.20 |  | 0.624 | viṣaye vā pure vā te yadā nāpakaromy aham na ca tvāṃ pratijāne 'haṃ kasmāt tvaṃ haṃsy akilbiṣam | विषये वा पुरे वा ते यदा पापं करोम्यहम्। न च त्वामवजाने च कस्मात्त्वं हंस्यकिल्बिषम्4.17.23।। फलमूलाशनं नित्यं वानरं वनगो |
| 4.41.33 | 4.42.39 | 0.624 | tenaivam uktaḥ śailendraḥ sarva eva tvadāśrayāḥ matprasādād bhaviṣyanti divārātrau ca kāñcanāḥ | तेनैव मुक्तश्शैलेन्द्रस्सर्व एव त्वदाश्रयाः। मत्प्रसादाद्भविष्यन्ति दिवा रात्रं च काञ्चनाः।।4.42.39।। त्वयि ये चापि वत्स |
| 4.11.50 |  | 0.626 | tasya tadvacanaṃ śrutvā sugrīvasya mahātmanaḥ rāghavo dundubheḥ kāyaṃ pādāṅguṣṭhena līlayā | तस्य तद्वचनं श्रुत्वा राघवस्य महात्मनः। गच्छन्नेवाचचक्षेऽथ सुग्रीवस्तन्महद्वनम्4.13.16।। |
| 4.7.10 |  | 0.628 | bāliśas tu naro nityaṃ vaiklavyaṃ yo 'nuvartate sa majjaty avaśaḥ śoke bhārākrānteva naur jale | बालिशस्तु नरो नित्यं वैक्लब्यं योऽनुवर्तते। |
| 4.11.43 |  | 0.63 | sa maharṣiṃ samāsādya yācate sma kṛtāñjaliḥ | एतच्छ्रुत्वा तदा वाली वचनं वानरेरितम्। स महर्षिंतदाऽसाद्य याचते स्म कृताञ्जलिः4.11.62।। |
| 4.51.4 | 4.52.4 | 0.631 | rājā sarvasya lokasya mahendravaruṇopamaḥ rāmo dāśarathiḥ śrīmān praviṣṭo daṇḍakāvanam | राजा सर्वस्य लोकस्य महेन्द्रवरुणोपमः। रामो दाशरथिश्शीमान्प्रविष्टो दण्डकावनम्।।4.52.4।। लक्ष्मणेन सह भ्रात्रा वैदेह्या च |
| 4.51.7 | 4.52.7 | 0.631 | agastyacaritām āśāṃ dakṣiṇāṃ yamarakṣitām sahaibhir vānarair mukhyair aṅgadapramukhair vayam | अगस्त्यचरितामाशां दक्षिणां यमरक्षिताम्। सहैभिर्वानरैर्घोरैरङ्गदप्रमुखैर्वयम्।।4.52.7।। रावणं सहितास्सर्वे राक्षसं कामरूप |
| 4.54.19 | 4.55.19 | 0.631 | mataṃ tad vāliputrasya vijñāya plavagarṣabhāḥ upaspṛśyodakaṃ sarve prāṅmukhāḥ samupāviśan | मतं तद्वालिपुत्रस्य विज्ञाय प्लवगर्षभाः।।4.55.19।। उपस्पृश्योदकं तत्र प्राङ्मुखास्समुपाविशन्। दक्षिणाग्रेषु दर्भेषु उदक् |
| 4.42.39 | 4.43.40 | 0.632 | tataḥ kāñcanapadmābhiḥ padminībhiḥ kṛtodakāḥ nīlavaidūryapatrāḍhyā nadyas tatra sahasraśaḥ | उत्तराः कुरवस्तत्र कृतपुण्यप्रतिश्रयाः।।4.43.40।। ततः काञ्चनपद्माभिः पद्भिनीभिः कृतोदकाः। नीलवैडूर्यपत्राभिर्नद्यस्तत्र  |
| 4.8.21 |  | 0.634 | ime hi me mahāvegāḥ patriṇas tigmatejasaḥ kārtikeyavanodbhūtāḥ śarā hemavibhūṣitāḥ | इमे हि मे महावेगा पत्रिणस्तिग्मतेजसः। कार्तिकेयवनोद्भूताश्शरा हेमविभूषिताः4.8.22।। कङ्कपत्रपरिच्छन्ना महेन्द्राशनिसन्निभ |
| 4.26.10 |  | 0.634 | bhavān kriyāparo loke bhavān devaparāyaṇaḥ āstiko dharmaśīlaś ca vyavasāyī ca rāghava | भवान्क्रियापरो लोके भवान् देवपरायणः। आस्तिको धर्मशीलश्च व्यवसायी च राघव4.27.35।। न ह्यव्यवसितश्शत्रुं राक्षसं तं विशेषतः |
| 4.60.5 |  | 0.634 | athāvāṃ yugapat prāptāv apaśyāva mahītale rathacakrapramāṇāni nagarāṇi pṛthak pṛthak | अथाऽवां युगपत्प्राप्तावपश्याव महीतले। |
| 4.63.24 | 4.64.24 | 0.634 | bruvadhvaṃ yasya yā śaktir gamane plavagarṣabhāḥ | न हि वो गमने सङ्गः कदाचित्कस्यचित्क्वचित्। ब्रुवध्वं यस्य या शक्तिः प्लवने प्लवगर्षभाः।।4.64.24।। |
| 4.54.20 | 4.55.23 | 0.636 | sa saṃviśadbhir bahubhir mahīdharo; mahādrikūṭapramitaiḥ plavaṃgamaiḥ | स संविशद्भिबहुभिर्महीधरो महाद्रिकूटप्रतिमैः प्लवङ्गमैः। बभूव सन्नादितनिर्दरान्तरो भृशं नदद्भिर्जलदैरिवोल्बणैः।।4.55.23।। |
| 4.11.14 |  | 0.638 | taṃ bhītam iti vijñāya samudram asurottamaḥ himavadvanam āgacchac charaś cāpād iva cyutaḥ | तं भीत इति विज्ञाय समुद्रमसुरोत्तमः। हिमवद्वनमागच्छच्छरश्चापादिव च्युतः4.11.14।। ततस्तस्य गिरेश्श्वेता गजेन्द्रविप्रलाश् |
| 4.39.46 | 4.40.50 | 0.638 | āsīnaṃ parvatasyāgre sarvabhūtanamaskṛtam sahasraśirasaṃ devam anantaṃ nīlavāsasaṃ | तत्र चन्द्रप्रतीकाशं पन्नगं धरणीधरम्।।4.40.50।। पद्मपत्रविशालाक्षं ततो द्रक्ष्यथ वानराः। आसीनं पर्वतस्याग्रे सर्वभूतनमस् |
| 4.5.5 |  | 0.639 | rājasūyāśvamedhaiś ca vahnir yenābhitarpitaḥ dakṣiṇāś ca tathotsṛṣṭā gāvaḥ śatasahasraśaḥ | राजसूयाश्वमेधैश्च वह्निर्येनाभितर्पितः। दक्षिणाश्च तथोत्सृष्टा गावश्शतसहस्रशः4.5.5।। तपसा सत्यवाक्येन वसुधा येन पालिता।  |
| 4.52.19 | 4.53.19 | 0.639 | sa tu siṃharṣabha skandhaḥ pīnāyatabhujaḥ kapiḥ yuvarājo mahāprājña aṅgado vākyam abravīt | ततस्तान्कपिवृद्धांस्तु शिष्टांश्चैव वनौकसः। वाचा मधुरयाऽभाष्य यथावदनुमान्य च।।4.53.19।। स तु सिंहवृषस्कन्धः पीनायतभुजः क |
| 4.57.33 | 4.58.36 | 0.639 | tato nītvā tu taṃ deśaṃ tīre nadanadīpateḥ nirdagdhapakṣaṃ saṃpātiṃ vānarāḥ sumahaujasaḥ | ततो नीत्वा तु तं देशं तीरं नदनदीपतेः। निर्दग्धपक्षं सम्पातिं वानरास्सुमहौजसः।।4.58.36।। पुनः प्रत्यानयित्वा च तं देशं पत |
| 4.2.24 |  | 0.64 | lakṣayasva tayor bhāvaṃ prahṛṣṭamanasau yadi viśvāsayan praśaṃsābhir iṅgitaiś ca punaḥ punaḥ | लक्षयस्व तयोर्भावं प्रहृष्टमनसौ यदि। विश्वासयन्प्रशंसाभिरिङ्गितैश्च पुनः पुनः4.2.25।। ममैवाभिमुखं स्थित्वा पृच्छ त्वं हर |
| 4.32.23 | 4.33.23 | 0.64 | dṛṣṭvābhijanasaṃpannāś citramālyakṛtasrajaḥ varamālyakṛtavyagrā bhūṣaṇottamabhūṣitāḥ | दृष्ट्वाऽभिजनसम्पन्नाश्चित्रमाल्यकृतस्रजः। फलमाल्यकृतव्यग्रा भूषणोत्तमभूषिताः।।4.33.23।। नातृप्तान्नापि चाव्यग्रान्नानुद |
| 4.48.2 | 4.49.2 | 0.64 | vanāni girayo nadyo durgāṇi gahanāni ca daryo giriguhāś caiva vicitā naḥ samantataḥ | वनानि गिरयो नद्यो दुर्गाणि गहनानि च। दर्यो गिरिगुहाश्चैव विचितानि समन्ततः।।4.49.2।। तत्र तत्र सहास्माभिर्जानकी न च दृश्य |
| 4.52.3 | 4.53.3 | 0.64 | sā tvam asmād bilād ghorād uttārayitum arhasi | सा त्वमस्माद्बिलाद्घोरादुत्तारयितुमर्हसि।।4.53.3।। तस्मात्सुग्रीववचनादतिक्रान्तान्गतायुषः। |
| 4.57.23 | 4.58.24 | 0.64 | saṃprāpya sāgarasyāntaṃ saṃpūrṇaṃ śatayojanam āsādya dakṣiṇaṃ kūlaṃ tato drakṣyatha rāvaṇam | लङ्कायामथ गुप्तायां सागरेण समन्ततः। सम्प्राप्य सागरस्यान्तं सम्पूर्णं शतयोजनम्।।4.58.24।। आसाद्य दक्षिणं तीरं ततो द्रक्ष |
| 4.30.14 |  | 0.641 | sālatālāśvakarṇāṃś ca tarasā pātayan bahūn paryasyan girikūṭāni drumān anyāṃś ca vegataḥ | सालतालाश्वकर्णांश्च तरसा पातयन्बहून्। पर्यस्यन्गिरिकूटानि द्रुमानन्यांश्च वेगतः4.31.14।। शिलाश्च शकलीकुर्वन्पद्भ्यां गज  |
| 4.39.33 | 4.40.37 | 0.641 | taṃ kālameghapratimaṃ mahoraganiṣevitam abhigamya mahānādaṃ tīrthenaiva mahodadhim | तं कालमेघप्रतिमं महोरगनिषेवितम्। अभिगम्य महानादं तीर्थेनैव महोदधिम्।।4.40.37।। ततो रक्तजलं भीमं लोहितं नाम सागरम्। गत्वा |
| 4.6.6 |  | 0.642 | idaṃ tathyaṃ mama vacas tvam avehi ca rāghava tyaja śokaṃ mahābāho tāṃ kāntām ānayāmi te | इदं तथ्यं मम वचस्त्वमवेहि च राघव। न शक्या सा जरयितुं सेन्द्रैरपि स्सुरासुरैः4.6.7।। तव भार्या महाबाहो भक्ष्यं विषकृतं यथ |
| 4.66.40 | 4.67.46 | 0.643 | nānāgandharvamithunaiḥ pānasaṃsargakarkaśaiḥ utpatadbhir vihaṃgaiś ca vidyādharagaṇair api | नानागन्धर्वमिथुनैः पानसंसर्गकर्कशैः।।4.67.46।। उत्पतद्भिश्च विहगैर्विद्याधरगणैरपि। त्यज्यमानमहासानुस्सन्निलीनमहोरगः।।4.6 |
| 4.11.25 |  | 0.644 | dhārayan māhiṣaṃ rūpaṃ tīkṣṇaśṛṅgo bhayāvahaḥ prāvṛṣīva mahāmeghas toyapūrṇo nabhastale | धारयन्माहिषं रूपं तीक्ष्णशृङ्गो भयावहः। प्रावृषीव महामेघस्तोयपूर्णो नभस्स्थले4.11.25।। ततस्तु द्वारमागम्य किष्किन्धाया म |
| 4.30.12 |  | 0.644 | yathoktakārī vacanam uttaraṃ caiva sottaram bṛhaspatisamo buddhyā mattvā rāmānujas tadā | यथोक्तकारी वचनमुत्तरं चैव सोत्तरम्। बृहस्पतिसमो बुद्ध्या मत्वा रामानुजस्तदा4.31.12।। कामक्रोधसमुत्थेन भ्रातुः कोपाग्निना |
| 4.30.33 |  | 0.644 | eṣa rāmānujaḥ prāptas tvatsakāśam ariṃdamaḥ bhrātur vyasanasaṃtapto dvāri tiṣṭhati lakṣmaṇaḥ | एष रामानुजः प्राप्तस्वत्सकाशमरिन्दम4.31.33।। भ्रातुर्व्यसनसन्तप्तो द्वारि तिष्ठति लक्ष्मणः। तस्य वाक्यं यदि रुचिः क्रियत |
| 4.45.14 | 4.46.21 | 0.644 | idānīṃ me smṛtaṃ rājan yathā vālī harīśvaraḥ mataṅgena tadā śapto hy asminn āśramamaṇḍale | इदानीं मे स्मृतं राजन्यथा वाली हरीश्वरः।।4.46.21।। मतङ्गेन तदा शप्तो ह्यस्मिन्नाश्रममण्डले। प्रविशेद्यदि वै वाली मूर्धाऽ |
| 4.13.15 |  | 0.645 | tasya tadvacanaṃ śrutvā rāghavasya mahātmanaḥ gacchann evācacakṣe 'tha sugrīvas tan mahad vanam | तस्य तद्वचनं श्रुत्वा सुग्रीवस्य महात्मनः। स्मितपूर्वमथो रामः प्रत्युवाच हरिं प्रभुः4.11.82।। |
| 4.38.16 | 4.39.17 | 0.645 | padmakesarasaṃkāśas taruṇārkanibhānanaḥ buddhimān vānaraśreṣṭhaḥ sarvavānarasattamaḥ | पद्मकेसरसङ्काशस्तरुणार्कनिभाननः। बुद्धिमान्वानरश्रेष्ठस्सर्ववानरसत्तमः।।4.39.17।। अनेकैर्बहुसाहस्रैर्वानराणां समन्वितः।  |
| 4.39.39 | 4.40.43 | 0.645 | tasya madhye mahāśveta ṛṣabho nāma parvataḥ divyagandhaiḥ kusumitai rajataiś ca nagair vṛtaḥ | तस्य मध्ये महान् श्वेतो ऋषभो नाम पर्वतः।।4.40.43।। दिव्यगन्धैः कुसुमितै राजितैश्च नगैर्वृतः। सरश्च राजतैः पद्मैर्ज्वलितै |
| 4.47.18 | 4.48.20 | 0.645 | tam āpatantaṃ sahasā vāliputro 'ṅgadas tadā | तमापतन्तं सहसा वालिपुत्रोऽङ्गदस्तदा। रावणोऽयमिति ज्ञात्वा तलेनाभिजघान ह।।4.48.20।। |
| 4.57.15 | 4.58.15 | 0.645 | taruṇī rūpasaṃpannā sarvābharaṇabhūṣitā hriyamāṇā mayā dṛṣṭā rāvaṇena durātmanā | तरुणी रूपसम्पन्ना सर्वाभरणभूषिता। ह्रियमाणा मया दृष्टा रावणेन दुरात्मना।।4.58.15।। क्रोशन्ती राम रामेति लक्ष्मणेति च भाम |
| 4.1.39 | 4.1.79 | 0.646 | cūtāḥ pāṭalayaś caiva kovidārāś ca puṣpitāḥ mucukundārjunāś caiva dṛśyante girisānuṣu | अङ्कोलाश्च कुरण्टाश्च चूर्णकाः पारिभद्रकाः। चूताः पाटलयश्चैव कोविदाराश्च पुष्पिताः।।4.1.79।। मुचुकुन्दार्जुनाश्चैव दृश्य |
| 4.4.10 |  | 0.646 | sukhārhasya mahārhasya sarvabhūtahitātmanaḥ aiśvaryeṇa vihīnasya vanavāsāśritasya ca | सुखार्हस्य महार्हस्य सर्वभूतहितात्मनः। ऐश्वर्येण च हीनस्य वनवासाश्रितस्य च4.4.13।। रक्षसाऽपहृता भार्या रहिते कामरूपिणा।  |
| 4.6.7 |  | 0.646 | anumānāt tu jānāmi maithilī sā na saṃśayaḥ hriyamāṇā mayā dṛṣṭā rakṣasā krūrakarmaṇā | अनुमानात्तु जानामि मैथिली सा न संशयः। ह्रियमाणा मया दृष्टा रक्षसा क्रूरकर्मणा4.6.9।। क्रोशन्ती राम रामेति लक्ष्मणेति च व |
| 4.18.52 |  | 0.646 | sa tam āśvāsayad rāmo vālinaṃ vyaktadarśanam | स तमाश्वासयद्रामो वालिनं व्यक्तदर्शनम्4.18.60।। सामसम्पन्नया वाचा धर्मतत्त्वार्थयुक्तया। |
| 4.48.16 | 4.49.16 | 0.646 | te śāradābhrapratimaṃ śrīmadrajataparvatam śṛṅgavantaṃ darīvantam adhiruhya ca vānarāḥ | ते शारदाभ्रप्रतिमं श्रीमद्रजतपर्वतम्। शृङ्गवन्तं दरीमन्तमधिरुह्य च वानराः।।4.49.16।। तत्र लोध्रवनं रम्यं सप्तपर्णवनानि च |
| 4.55.14 | 4.56.15 | 0.646 | rāmalakṣmaṇayor vāsām araṇye saha sītayā rāghavasya ca bāṇena vālinaś ca tathā vadhaḥ | रामलक्ष्मणयोर्वासश्च अरण्ये सह सीतया।।4.56.15।। राघवस्य च बाणेन वालिनश्च तथा वधः। रामकोपादशेषाणां रक्षसानां तथा वधः।।4.5 |
| 4.11.52 |  | 0.648 | ārdraḥ samāṃsapratyagraḥ kṣiptaḥ kāyaḥ purā sakhe laghuḥ saṃprati nirmāṃsas tṛṇabhūtaś ca rāghava | आर्द्रस्समांसः प्रत्यग्रः क्षिप्तः कायः पुरा सखे4.11.87।। लघुस्सम्प्रति निर्मांस स्तृणभूतश्च राघव। परिश्रान्तेन मत्तेन भ |
| 4.5.8 | 4.5.8 | 0.649 | śrutvā hanumato vākyaṃ sugrīvo hṛṣṭamānasaḥ bhayaṃ sa rāghavād ghoraṃ prajahau vigatajvaraḥ | श्रुत्वा हनुमतो वाक्यं सुग्रीवो हृष्टमानसः। भयं चराघवाद्घोरं प्रजहौ विगतज्वरः।।4.5.8।। सकृत्वा मानुषं रूपं सुग्रीवः प्लव |
| 4.11.39 |  | 0.649 | yuddhe prāṇahare tasmin niṣpiṣṭo dundubhis tadā śrotrābhyām atha raktaṃ tu tasya susrāva pātyataḥ | वाली व्यापातयाञ्चक्रे ननर्द च महास्वनम्। श्रोत्राभ्यामथ रक्तं तु तस्य सुस्राव पात्यतः4.11.41।। |
| 4.18.2 |  | 0.649 | taṃ niṣprabham ivādityaṃ muktatoyam ivāmbudam uktavākyaṃ hariśreṣṭham upaśāntam ivānalam | तं निष्प्रभमिवादित्यं मुक्ततोयमिवाम्बुदम्। उक्तवाक्यं हरिश्रेष्ठमुपशान्तमिवानलम्4.18.2।। धर्मार्थगुणसम्पन्नं हरीश्वरमनुत |

## Critical-only — 215, sample of 30

| Locus | Text |
|---|---|
| 4.1.9 | mārutaḥ sukhaṃ saṃsparśe vāti candanaśītalaḥ ṣaṭpadair anukūjadbhir vaneṣu madhugandhiṣu |
| 4.1.38 | nīpāś ca varaṇāś caiva kharjūrāś ca supuṣpitāḥ aṅkolāś ca kuraṇṭāś ca cūrṇakāḥ pāribhadrakāḥ |
| 4.1.44 | adhikaṃ śobhate pampāvikūjadbhir vihaṃgamaiḥ |
| 4.1.47 | evaṃ sa vilapaṃs tatra śokopahatacetanaḥ avekṣata śivāṃ pampāṃ ramyavārivahāṃ śubhām |
| 4.2.25 | mamaivābhimukhaṃ sthitvā pṛccha tvaṃ haripuṃgava prayojanaṃ praveśasya vanasyāsya dhanurdharau |
| 4.3.2 | sa tatra gatvā hanumān balavān vānarottamaḥ upacakrāma tau vāgbhir mṛdvībhiḥ satyavikramaḥ |
| 4.3.3 | svakaṃ rūpaṃ parityajya bhikṣurūpeṇa vānaraḥ ābabhāṣe ca tau vīrau yathāvat praśaśaṃsa ca |
| 4.3.5 | trāsayantau mṛgagaṇān anyāṃś ca vanacāriṇaḥ pampātīraruhān vṛkṣān vīkṣamāṇau samantataḥ |
| 4.3.7 | siṃhaviprekṣitau vīrau siṃhātibalavikramau śakracāpanibhe cāpe pragṛhya vipulair bhujaiḥ |
| 4.3.11 | yadṛcchayeva saṃprāptau candrasūryau vasuṃdharām viśālavakṣasau vīrau mānuṣau devarūpiṇau |
| 4.3.12 | siṃhaskandhau mahāsattvau samadāv iva govṛṣau āyatāś ca suvṛttāś ca bāhavaḥ parighottamāḥ |
| 4.3.18 | sugrīvo nāma dharmātmā kaś cid vānarayūthapaḥ vīro vinikṛto bhrātrā jagad bhramati duḥkhitaḥ |
| 4.3.21 | bhikṣurūpapraticchannaṃ sugrīvapriyakāmyayā ṛśyamūkād iha prāptaṃ kāmagaṃ kāmarūpiṇam |
| 4.4.7 | śaraṇyaḥ sarvabhūtānāṃ pitur nirdeśapāragaḥ vīro daśarathasyāyaṃ putrāṇāṃ guṇavattaraḥ |
| 4.4.8 | rājyād bhraṣṭo vane vastuṃ mayā sārdham ihāgataḥ bhāryayā ca mahātejāḥ sītayānugato vaśī |
| 4.4.11 | rakṣasāpahṛtā bhāryā rahite kāmarūpiṇā tac ca na jñāyate rakṣaḥ patnī yenāsya sā hṛtā |
| 4.5.6 | tapasā satyavākyena vasudhā yena pālitā strīhetos tasya putro 'yaṃ rāmas tvāṃ śaraṇaṃ gataḥ |
| 4.5.9 | sa kṛtvā mānuṣaṃ rūpaṃ sugrīvaḥ plavagādhipaḥ darśanīyatamo bhūtvā prītyā provāca rāghavam |
| 4.5.15 | dīpyamānaṃ tato vahniṃ puṣpair abhyarcya satkṛtam tayor madhye tu suprīto nidadhe susamāhitaḥ |
| 4.5.18 | tataḥ sarvārthavidvāṃsaṃ rāmaṃ daśarathātmajam sugrīvaḥ prāha tejasvī vākyam ekamanās tadā |
| 4.6.1 | ayam ākhyāti me rāma sacivo mantrisattamaḥ hanumān yannimittaṃ tvaṃ nirjanaṃ vanam āgataḥ |
| 4.6.2 | lakṣmaṇena saha bhrātrā vasataś ca vane tava rakṣasāpahṛtā bhāryā maithilī janakātmajā |
| 4.6.3 | tvayā viyuktā rudatī lakṣmaṇena ca dhīmatā antaraṃ prepsunā tena hatvā gṛdhraṃ jaṭāyuṣam |
| 4.6.8 | krośantī rāma rāmeti lakṣmaṇeti ca visvaram sphurantī rāvaṇasyāṅke pannagendravadhūr yathā |
| 4.9.20 | gūhamānasya me tattvaṃ yatnato mantribhiḥ śrutam tato 'haṃ taiḥ samāgamya sametair abhiṣecitaḥ |
| 4.10.5 | mā ca roṣaṃ kṛthāḥ saumya mayi śatrunibarhaṇa yāce tvāṃ śirasā rājan mayā baddho 'yam añjaliḥ |
| 4.11.13 | guhā prasravaṇopeto bahukandaranirjharaḥ sa samarthas tava prītim atulāṃ kartum āhave |
| 4.11.15 | tatas tasya gireḥ śvetā gajendravipulāḥ śilāḥ cikṣepa bahudhā bhūmau dundubhir vinanāda ca |
| 4.11.26 | tatas tu dvāram āgamya kiṣkindhāyā mahābalaḥ nanarda kampayan bhūmiṃ dundubhir dundubhir yathā |
| 4.11.31 | tasya tadvacanaṃ śrutvā vānarendrasya dhīmataḥ uvāca dundubhir vākyaṃ krodhāt saṃraktalocanaḥ |

## Gita Supersite-only — 463, sample of 30

| Locus | Text |
|---|---|
| 4.1.3 | सौमित्रे शोभते पम्पा वैदूर्यविमलोदका। फुल्लपद्मोत्पलवती शोभिता विविधैर्द्रुमैः।।4.1.3।। |
| 4.1.6 | शोकार्तस्यापि मे पम्पा शोभते चित्रकानना। व्यवकीर्णा बहुविधैः पुष्पैश्शीतोदका शिवा।।4.1.6।। |
| 4.1.7 | नलिनैरपि सञ्छन्ना ह्यत्यर्थशुभदर्शना। सर्पव्यालानुचरिता मृगद्विजसमाकुला।।4.1.7।। |
| 4.1.9 | पुष्पभारसमृद्धानि शिखराणि समन्ततः। लताभिः पुष्पिताग्राभिरुपगूढानि सर्वशः।।4.1.9।। |
|  | पतितैः पतमानैश्च पादपस्थैश्च मारुतः। |
|  | विक्षिपन्विविधाश्शाखा नगानां कुसुमोत्कचाः। |
|  | मत्तकोकिलसन्नादैर्नर्तयन्निव पादपान्। |
|  | तेन विक्षिपताऽत्यर्थं पवनेन समन्ततः। |
| 4.1.17 | स एष सुखसंस्पर्शो वाति चन्दनशीतलः। गन्धमभ्यवहन्पुण्यं श्रमापनयनोऽनिलः।।4.1.17।। |
| 4.1.18 | अमी पवनविक्षिप्ता विनदन्तीव पादपाः। षट्पदैरनुकूजन्तो वनेषु मधुगन्धिषु।।4.1.18।। |
| 4.1.20 | पुष्पसञ्छन्नशिखरा मारुतोत्क्षेपचञ्चलाः। अमी मधुकरोत्तंसाः प्रगीता इव पादपाः।।4.1.20।। |
| 4.1.25 | श्रुत्वैतस्य पुरा शब्दमाश्रमस्था मम प्रिया। मामाहूय प्रमुदिताः परमं प्रत्यनन्दत।।4.1.25।। |
| 4.1.26 | एवं विचित्राः पतगा नानारावविराविणः। वृक्षगुल्मलताः पश्य सम्पतन्ति समन्ततः।।4.1.26।। |
| 4.1.28 | दात्यूहरतिविक्रन्दैः पुंस्कोकिलरुतैरपि। स्वनन्ति पादपाश्चेमे ममानङ्गप्रदीपनाः।।4.1.28।। |
| 4.1.29 | अशोकस्तबकाङ्गारष्षट्पदस्वननिःस्वनः। मां हि पल्लवताम्रार्चिर्वसन्ताग्निः प्रधक्ष्यति।।4.1.29।। |
| 4.1.30 | न हि तां सूक्ष्मपक्ष्माक्षीं सुकेशीं मृदुभाषिणीम्। अपश्यतो मे सौमित्रे जीवितेऽस्ति प्रयोजनम्।।4.1.30।। |
| 4.1.31 | अयं हि दयितस्तस्याः कालो रुचिरकाननः। कोकिलाकुलसीमान्तो दयिताया ममानघ।।4.1.31।। |
| 4.1.32 | मन्मथाऽयाससम्भूतो वसन्तगुणवर्धितः। अयं मां धक्ष्यति क्षिप्रं शोकाग्निर्नचिरादिव।।4.1.32।। |
| 4.1.33 | अपश्यतस्तां दयितां पश्यतो रुचिरद्रुमान्। ममायमात्मप्रभवो भूयस्त्वमुपयास्यति।।4.1.33।। |
| 4.1.34 | अदृश्यमाना वैदेही शोकं वर्धयते मम। दृश्यमानो वसन्तश्च स्वेदसंसर्गदूषकः।।4.1.34।। |
| 4.1.36 | अमी मयूराश्शोभन्ते प्रनृत्यन्तस्ततस्ततः। स्वैः पक्षैः पवनोद्धूतैर्गवाक्षैः स्फाटिकैरिव।।4.1.36।। |
| 4.1.39 | तामेव मन्मथाविष्टो मयूरोऽप्युपधावति। वितत्य रुचिरौ पक्षौ रुतैरुपहसन्निव।।4.1.39।। |
| 4.1.41 | मम त्वयं विना वासः पुष्पमासे सुदुस्सहः। पश्य लक्ष्मण संरागः तिर्यग्योनिगतेष्वपि। यदेषा शिखिनी कामाद्भर्तारं रमतेऽन्तिके।।4.1.41।। |
| 4.1.42 | मामप्येवं विशालाक्षी जानकी जातसम्भ्रमा। मदनेनाभिवर्तेत यदि नाऽपहृता भवेत्।।4.1.42।। |
| 4.1.44 | रुचिराण्यपि पुष्पाणि पादपानामतिश्रिया। निष्फलानि महीं यान्ति समं मधुकरोत्करैः।।4.1.44।। |
| 4.1.47 | नूनं न तु वसन्तोऽतं देशं स्पृशति यत्र सा। कथं ह्यसितपद्माक्षी वर्तयेत्सा मया विना।।4.1.47।। |
| 4.1.48 | अथवा वर्तते तत्र वसन्तो यत्र मे प्रिया। किं करिष्यति सुश्रोणी सा तु निर्भर्त्सिता परैः।।4.1.48।। |
| 4.1.49 | श्यामा पद्मपलाशाक्षी मृदुपूर्वाभिभाषिणी। नूनं वसन्तमासाद्य परित्यक्ष्यति जीवितम्।।4.1.49।। |
| 4.1.50 | दृढं हि हृदये बुद्धिर्मम सम्परिवर्तते। नालं वर्तयितुं सीता साध्वी मद्विरहं गता।।4.1.50।। |
| 4.1.51 | मयि भावस्तु वैदेह्यास्तत्त्वतो विनिवेशितः। ममापि भावस्सीतायां सर्वथा विनिवेशितः।।4.1.51।। |

## Full data

Complete machine-readable results alongside this file: `scratchpad/kishkindha_gitasupersite_alignment.json`

_Dr. Mārcis Gasūns_
