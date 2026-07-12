# Ayodhyākāṇḍa (II): Critical (GRETIL/Baroda) vs Gita Supersite

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
| 3160 | 4053 | 89 | 2898 | 2516 | 297 | 85 | 173 | 1066 |

## Major differences (sim < 0.6) — 85 pairs, showing up to 60

| Critical locus | Gita Supersite locus | sim | Critical text | Gita Supersite text |
|---|---|---:|---|---|
| 2.71.2 | 2.77.3 | 0.248 | brāhmaṇebhyo dadau ratnaṃ dhanam annaṃ ca puṣkalam bāstikaṃ bahuśuklaṃ ca gāś cāpi śataśas tathā | बास्तिकं बहु शुक्लं च गाश्चापि शतशस्तथा। दासीदासं च यानं च वेश्मानि सुमहान्ति च।।2.77.3।। ब्राह्मणेभ्यो ददौ पुत्रो राज्ञ |
| 2.102.27 | 2.110.30 | 0.389 | ambarīṣasya putro 'bhūn nahuṣaḥ satyavikramaḥ nahuṣasya ca nābhāgaḥ putraḥ paramadhārmikaḥ | शङ्खणस्य च पुत्रोऽभूच्छूर श्रीमान्सुदर्शनः। सुदर्शनस्याग्निवर्णः अग्निवर्णस्य शीघ्रगः।।2.110.30।। शीघ्रगस्य मरुः पुत्रो  |
| 2.109.10 | 2.117.9 | 0.429 | yayā mūlaphale sṛṣṭe jāhnavī ca pravartitā ugreṇa tapasā yuktā niyamaiś cāpy alaṃkṛtā | दश वर्षाण्यनावृष्ट्या दग्धे लोके निरन्तरम्।।2.117.9।। यया मूलफले सृष्टे जाह्नवी च प्रवर्तिता। उग्रेण तपसा युक्ता नियमैश् |
| 2.20.7 | 2.23.7 | 0.452 | yathā daivam aśauṇḍīraṃ śauṇḍīraḥ kṣatriyarṣabhaḥ kiṃ nāma kṛpaṇaṃ daivam aśaktam abhiśaṃsasi | किन्नाम कृपणं दैवमशक्तमभिशंससि।।2.23.7।। पापयोस्ते कथं नाम तयोश्शङ्का न विद्यते। |
| 2.45.20 | 2.86.19 | 0.453 | rathāśvagajasaṃbādhāṃ tūryanādavināditām sarvakalyāṇasaṃpūrṇāṃ hṛṣṭapuṣṭajanākulām | रम्यचत्वरसंस्थानां सुविभक्तमहापथाम्। हर्म्यप्रासादम्पन्नां सर्वरत्नविभूषिताम्।।2.86.19।। गजाश्वरथसंबाधां तूर्यनादविनादित |
| 2.19.21 | 2.22.25 | 0.457 | vyāhate 'py abhiṣeke me paritāpo na vidyate tasmād aparitāpaḥ saṃs tvam apy anuvidhāya mām | एतया तत्त्वया बुद्ध्या संस्तभ्यात्मानमात्मना। व्याहतेऽप्यभिषेके मे परितापो न विद्यते।।2.22.25।। |
| 2.37.23 | 2.42.28 | 0.457 | kausalyāyā gṛhaṃ śīghraṃ rāma mātur nayantu mām iti bruvantaṃ rājānam anayan dvāradarśitaḥ | इति ब्रुवन्तं राजानमनयन् द्वारदर्शिनः। कौशल्याया गृहं तत्र न्यवेश्यत विनीतवत्।।2.42.28।। |
| 2.10.16 | 2.11.4 | 0.462 | evam uktas tayā rājā priyayā strīvaśaṃ gataḥ tām uvāca mahātejāḥ kaikeyīm īṣadutsmitaḥ | तामुवाच महातेजाः कैकेयीमीषदुत्स्मितः। कामी हस्तेन संगृह्य मूर्धजेषु शुचिस्मिताम्।।2.11.4।। |
| 2.78.3 | 2.84.3 | 0.462 | sa eṣa hi mahākāyaḥ kovidāradhvajo rathe bandhayiṣyati vā dāśān atha vāsmān vadhiṣyati | यथा तु खलु दुर्बुद्धिर्भरत स्स्वयमागतः। स एष हि महाकायः कोविदारध्वजो रथे।।2.84.3।। |
| 2.85.30 | 2.91.33 | 0.463 | sitameghanibhaṃ cāpi rājaveśma sutoraṇam śuklamālyakṛtākāraṃ divyagandhasamukṣitam | सितमेघनिभं चापि राजवेश्म सुतोरणम्। दिव्यमाल्यकृताकारं दिव्यगन्धसमुक्षितम्।।2.91.33।। चतुरश्रमसंबाधं शयनासनयानवत्। दिव्यै |
| 2.93.25 | 2.99.26 | 0.468 | taṃ tu kṛṣṇājinadharaṃ cīravalkalavāsasaṃ dadarśa rāmam āsīnam abhitaḥ pāvakopamam | तं तु कृष्णाजिनधरं चीरवल्कलवाससम्। ददर्श राममासीनमभितः पावकोपमम्।।2.99.26।। सिंहस्कन्धं महाबाहुं पुण्डरीकनिभेक्षणम्। पृथ |
| 2.17.13 | 2.20.26 | 0.469 | mātaraṃ rāghavaḥ kiṃ cit prasāryāñjalim abravīt sa svabhāvavinītaś ca gauravāc ca tadānataḥ | स स्वभावविनीतश्च गौरवाच्च तदा नतः। प्रस्थितो दण्डकारण्यमाप्रष्टुमुपचक्रमे।।2.20.26।। |
| 2.58.48 | 2.64.63 | 0.469 | yadi māṃ saṃspṛśed rāmaḥ sakṛd adyālabheta vā na tan me sadṛśaṃ devi yan mayā rāghave kṛtam | एतन्मे सदृशं देवि यन्मया राघवे कृतम्। सदृशं तत्तु तस्यैव यदनेन कृतं मयि।।2.64.63।। |
| 2.9.12 | 2.9.16 | 0.471 | tasmin mahati saṃgrāme rājā daśarathas tadā apavāhya tvayā devi saṃgrāmān naṣṭacetanaḥ | अपवाह्य त्वया देवि सङ्ग्रामान्नष्टचेतनः। तत्रापि विक्षतश्शस्त्रैः पतिस्ते रक्षितस्त्वया।।2.9.16।। |
| 2.36.9 | 2.41.9 | 0.471 | nāgnihotrāṇy ahūyanta sūryaś cāntaradhīyata vyasṛjan kavalān nāgā gāvo vatsān na pāyayan | नाग्निहोत्राण्यहूयन्त नापचन् गृहमेधिनः अकुर्वन्न प्रजाः कार्यं सूर्यश्चान्तरधीयत।।2.41.9।। |
| 2.2.31 | 2.2.52 | 0.473 | abhyantaraś ca bāhyaś ca paurajānapado janaḥ striyo vṛddhās taruṇyaś ca sāyaṃprātaḥ samāhitāḥ | स्त्रियो वृद्धास्तरुण्यश्च सायं प्रातस्समाहिताः। सर्वान् देवान् नमस्यन्ति रामस्यार्थे यशस्विनः।।2.2.52।। |
| 2.31.32 | 2.34.48 | 0.473 | naivāhaṃ rājyam icchāmi na sukhaṃ na ca maithilīm tvām ahaṃ satyam icchāmi nānṛtaṃ puruṣarṣabha | त्वामहं सत्यमिच्छामि नानृतं पुरुषर्षभ। प्रत्यक्षं तव सत्येन सुकृतेन च ते शपे।।2.34.48।। |
| 2.16.12 | 2.18.13 | 0.479 | vivarṇavadano dīno na hi mām abhibhāṣate śārīro mānaso vāpi kaccid enaṃ na bādhate | शरीरो मानसो वापि कच्चिदेनं न बाधते। सन्तापोवाऽभितापो वा दुर्लभं हि सदा सुखम्।।2.18.13।। |
| 2.72.6 | 2.78.7 | 0.48 | liptā candanasāreṇa rājavastrāṇi bibhratī mekhalā dāmabhiś citrai rajjubaddheva vānarī | मेखलादामभिश्चित्रैरन्यैश्च शुभभूषणैः। बभासे बहुभिर्बद्धा रज्जुबद्धेव वानरी।।2.78.7।। |
| 2.74.1 | 2.80.1 | 0.48 | atha bhūmipradeśajñāḥ sūtrakarmaviśāradāḥ svakarmābhiratāḥ śūrāḥ khanakā yantrakās tathā | अथ भूमिप्रदेशज्ञास्सूत्रकर्मविशारदाः। स्वकर्माभिरताश्शूराः खनका यन्त्रकास्तथा।।2.80.1।। कर्मान्तिकाः स्थपतयः पुरुष यन्त् |
| 2.32.12 | 2.36.16 | 0.483 | kaikeyī dviguṇaṃ kruddhā rājānam idam abravīt tavaiva vaṃśe sagaro jyeṣṭhaṃ putram upārudhat | वैव वंशे सगरो ज्येष्ठं पुत्रमुपारुधत्। असमञ्ज इति ख्यातं तथायं गन्तुमर्हति।।2.36.16।। |
| 2.66.28 | 2.72.35 | 0.483 | ārye kim abravīd rājā pitā me satyavikramaḥ paścimaṃ sādhusaṃdeśam icchāmi śrotum ātmanaḥ | पश्चिमं साधु सन्देशमिच्छामि श्रोतुमात्मनः। इति पृष्टा यथातत्त्वं कैकेयी वाक्यमब्रवीत्।।2.72.35।। |
| 2.6.11 | 2.6.11 | 0.485 | sitābhraśikharābheṣu devatāyataneṣu ca catuṣpatheṣu rathyāsu caityeṣv aṭṭālakeṣu ca | सिताभ्रशिखराभेषु देवतायतनेषु च। चतुष्पथेषु रथ्यासु चैत्येष्वट्टालकेषु च।।2.6.11।। नानापण्यसमृद्धेषु वणिजामापणेषु च। कुटु |
| 2.21.22 | 2.24.29 | 0.485 | pūjyās te matkṛte devi brāhmaṇāś caiva suvratāḥ evaṃ kālaṃ pratīkṣasva mamāgamanakāṅkṣiṇī | एवं कालं प्रतीक्षस्व ममागमनकाङ्क्षिणी। नियता नियताहारा भर्तृशुश्रूषणे रता।।2.24.29।। |
| 2.74.17 | 2.80.18 | 0.485 | bahupāṃsucayāś cāpi parikhāparivāritāḥ tatrendrakīlapratimāḥ pratolīvaraśobhitāḥ | बहुपांसुचयाश्चापि परिखापरिवारिताः। तत्रेन्द्रकीलप्रतिमाः प्रतोलीवरशोभिताः।।2.80.18।। प्रासादमालावितता स्सौधप्राकारसंवृता |
| 2.11.10 | 2.13.17 | 0.486 | na prabhātaṃ tvayecchāmi mayāyaṃ racito 'ñjaliḥ atha vā gamyatāṃ śīghraṃ nāham icchāmi nirghṛṇām | न प्रभातं त्वयेच्छामि निशे नक्षत्रभूषणे।।2.13.17।। क्रियतां मे दया भद्रे मयाऽयं रचितोऽञ्जलिः। |
| 2.46.68 | 2.52.83 | 0.486 | putro daśarathasyāyaṃ mahārājasya dhīmataḥ nideśaṃ pālayatv enaṃ gaṅge tvadabhirakṣitaḥ | पुत्रो दशरथस्यायं महाराजस्य धीमतः। निदेशं पारयित्वेमं गङ्गे त्वदभिरक्षितः।।2.52.83।। चतुर्दश हि वर्षाणि समग्राण्युष्य का |
| 2.110.44 | 2.118.45 | 0.486 | lakṣmaṇena saha bhrātrā rāmaḥ satyaparākramaḥ viśvāmitras tu dharmātmā mama pitrā supūjitaḥ | विश्वामित्रस्तु धर्मात्मा मम पित्रा सुपूजितः।।2.118.45।। प्रोवाच पितरं तत्र भ्रातरौ रामलक्ष्मणौ। |
| 2.24.15 | 2.27.18 | 0.488 | saha tvayā viśālākṣa raṃsye paramanandinī evaṃ varṣasahasrāṇāṃ śataṃ vāhaṃ tvayā saha | अभिषेकं करिष्यामि तासु नित्यं यतव्रता। सह त्वया विशालाक्ष रंस्ये परमनन्दिनी ।।2.27.18।। |
| 2.42.13 | 2.48.16 | 0.488 | yatra rāmo bhayaṃ nātra nāsti tatra parābhavaḥ sa hi śūro mahābāhuḥ putro daśarathasya ca | स हि शूरो महाबाहुः पुत्रो दशरथस्य च। पुरा भवति नोदूरादनुगच्छाम राघवम्।।2.48.16।। |
| 2.91.11 | 2.97.23 | 0.488 | vanavāsam anudhyāya gṛhāya pratineṣyati imāṃ vāpy eśa vaidehīm atyantasukhasevinīm | इमां वाप्येष वैदेहीमत्यन्तसुखसेविनीम्। पिता मे राघव श्श्रीमान्वनादादाय यास्यति।।2.97.23।। |
| 2.110.45 | 2.118.46 | 0.488 | provāca pitaraṃ tatra rāghavo rāmalakṣmaṇau sutau daśarathasyemau dhanurdarśanakāṅkṣiṇau | सुतौ दशरथस्येमौ धनुर्दर्शकाङ्क्षिणौ। धनुर्दर्शय रामाय राजपुत्राय दैविकम्।।2.118.46।। |
| 2.7.5 | 2.7.8 | 0.489 | rāmamātā dhanaṃ kiṃ nu janebhyaḥ saṃprayacchati atimātraṃ praharṣo 'yaṃ kiṃ janasya ca śaṃsa me | उत्तमेनाभिसंयुक्ता हर्षेणार्थपरा सती। राममाता धनं किन्नु जनेभ्यस्सम्प्रयच्छति।।2.7.8।। |
| 2.13.7 | 2.15.7 | 0.489 | kṣaudraṃ dadhighṛtaṃ lājā dharbhāḥ sumanasaḥ payaḥ salājāḥ kṣīribhiś channā ghaṭāḥ kāñcanarājatāḥ | सलाजाः क्षीरिभिश्छन्ना घटाः काञ्चनराजताः।।2.15.7।। पद्मोत्पलयुता भान्ति पूर्णाः परमवारिणा। |
| 2.86.24 | 2.92.24 | 0.489 | yasyāḥ kṛte narayāghrau jīvanāśam ito gatau rājā putravihīnaś ca svargaṃ daśaratho gataḥ | यस्याः कृते नरव्याघ्रौ जीवनाशमितो गतौ। राजपुत्रविहीनश्च स्वर्गं दशरथो गतः।।2.92.24।। क्रोधनामकृतप्रज्ञां दृप्तां सुभगमान |
| 2.98.8 | 2.105.8 | 0.49 | yathā tu ropito vṛkṣaḥ puruṣeṇa vivardhitaḥ hrasvakena durāroho rūḍhaskandho mahādrumaḥ | यथा तु रोपितो वृक्षः पुरुषेण विवर्धितः। ह्रस्वकेण दुरारोहो रूढस्कन्धो महाद्रुमः।।2.105.8।। स यदा पुष्पितो भूत्वा फलानि न |
| 2.1.21 | 2.1.27 | 0.492 | āyakarmaṇy upāyajñaḥ saṃdṛṣṭavyayakarmavit śraiṣṭhyaṃ śāstrasamūheṣu prāpto vyāmiśrakeṣv api | श्रैष्ठ्यं शास्त्रसमूहेषु प्राप्तो व्यामिश्रकेषु च। अर्थधमौ च सङ्गृह्य सुखतन्त्रो न चालसः।।2.1.27।। |
| 2.11.6 | 2.12.66 | 0.492 | yadi satyaṃ bravīmy etat tad asatyaṃ bhaviṣyati akīrtir atulā loke dhruvaṃ paribhavaś ca me | कैकेय्या क्लिश्यमानेन रामः प्रव्राजितो मया।।2.12.66।। यदि सत्यं ब्रवीम्येतत्तदसत्यं भविष्यति। |
| 2.13.12 | 2.15.13 | 0.492 | ikṣvākūṇāṃ yathā rājye saṃbhriyetābhiṣecanam tathā jātīyām ādāya rājaputrābhiṣecanam | इक्ष्वाकूणां यथा राज्ये संभ्रियेताभिषेचनम्।।2.15.13।। तथाजातीयमादाय राजपुत्राभिषेचनम्। ते राजवचनात्तत्र समवेतामहीपतिम्।। |
| 2.94.34 | 2.100.40 | 0.492 | vīrair adhyuṣitāṃ pūrvam asmākaṃ tāta pūrvakaiḥ satyanāmāṃ dṛḍhadvārāṃ hastyaśvarathasaṃkulām | वीरैरध्युषितां पूर्वमस्माकं तात पूर्वकैः। सत्यनामां दृढ द्वारां हस्त्यश्वरथसङ्कुलाम्।।2.100.40।। ब्राह्मणैः क्षत्रियैर्व |
| 2.94.43 | 2.100.51 | 0.492 | kaccin nāga vanaṃ guptaṃ kuñjarāṇaṃ ca tṛpyasi kaccid darśayase nityaṃ manuṣyāṇāṃ vibhūṣitam | कच्चिद्दर्शयसे नित्यं मनुष्याणां विभूषितम्। उत्थायोत्थाय पूर्वाह्णे राजपुत्र महापथे।।2.100.51।। |
| 2.2.29 | 2.2.49 | 0.494 | satyavādī maheṣvāso vṛddhasevī jitendriyaḥ vatsaḥ śreyasi jātas te diṣṭyāsau tava rāghavaḥ | वत्सश्श्रेयसि जातस्ते दिष्ट्याऽसौ तव राघव। दिष्ट्या पुत्रगुणैर्युक्तो मारीच इव काश्यपः।।2.2.49।। |
| 2.50.15 | 2.56.22 | 0.494 | śuśrūṣamāṇam ekāgram idaṃ vacanam abravīt aiṇeyaṃ māṃsam āhṛtya śālāṃ yakṣyāmahe vayam | ऐणेयं मांसमाहृत्य शालां यक्ष्यामहे वयम्। कर्तव्यं वास्तुशमनं सौमित्रे चिरजीविभिः।।2.56.22।। |
| 2.63.11 | 2.69.11 | 0.494 | svapne 'pi sāgaraṃ śuṣkaṃ candraṃ ca patitaṃ bhuvi sahasā cāpi saṃśantaṃ jvalitaṃ jātavedasaṃ | स्वप्नेऽपि सागरं शुष्कं चन्द्रं च पतितं भवि। उपरुद्धां च जगतीं तमसेव समावृताम्।।2.69.11।। औपवाह्यस्य नागस्य विषाणं शकलीक |
| 2.3.11 | 2.3.27 | 0.496 | gandharvarājapratimaṃ loke vikhyātapauruṣam dīrghabāhuṃ mahāsattvaṃ mattamātaṅgagāminam | गन्धर्वराजप्रतिमं लोके विख्यातपौरुषम्।।2.3.27।। दीर्घबाहुं महासत्त्वं मत्तमातङ्गगामिनम्। चन्द्रकान्ताननं राममतीव प्रियदर |
| 2.1.22 | 2.1.28 | 0.497 | arthadharmau ca saṃgṛhya sukhatantro na cālasaḥ vaihārikāṇāṃ śilpānāṃ vijñātārthavibhāgavit | वैहारिकाणां शिल्पानां विज्ञाताऽऽर्थविभागवित्। आरोहे विनये चैव युक्तो वारणवाजिनाम्।।2.1.28।। |
| 2.13.23 | 2.15.30 | 0.497 | prapanno rājamārgaṃ ca patākā dhvajaśobhitam sa sūtas tatra śuśrāva rāmādhikaraṇāḥ kathāḥ | स सूतस्तत्र शुश्राव रामाधिकरणाः कथाः।।2.15.30।। अभिषेचनसंयुक्तास्सर्वलोकस्य हृष्टवत्। |
| 2.63.17 | 2.69.19 | 0.497 | śuṣyatīva ca me kaṇṭho na svastham iva me manaḥ jugupsann iva cātmānaṃ na ca paśyāmi kāraṇam | एतन्निमित्तं दीनोऽहं तन्नवः प्रतिपूजये। शुष्यतीव च मे कण्ठः न स्वस्थमिव मे मनः।।2.69.19।। |
| 2.94.56 | 2.100.65 | 0.497 | nāstikyam anṛtaṃ krodhaṃ pramādaṃ dīrghasūtratām adarśanaṃ jñānavatām ālasyaṃ pañcavṛttitām | नास्तिक्यमनृतं क्रोधं प्रमादं दीर्घसूत्रताम्। अदर्शनं ज्ञानवतामालस्यं पञ्चवृत्तिताम्।।2.100.65।। एकचिन्तनमर्थानामनर्थज्ञ |
| 2.98.43 | 2.106.4 | 0.497 | yasyaiṣa buddhilābhaḥ syāt paritapyeta kena saḥ sa evaṃ vyasanaṃ prāpya na viṣīditum arhati | यथा मृत स्तथा जीवन्यथाऽसति तथा सति। यस्यैष बुद्धिलाभ स्स्यात्परितप्येत केन सः।।2.106.4।। |
| 2.85.66 | 2.91.72 | 0.499 | pātrīṇāṃ ca sahasrāṇi śātakumbhamayāni ca sthālyaḥ kumbhyaḥ karambhyaś ca dadhipūrṇāḥ susaṃskṛtāḥ | पात्रीणां च सहस्राणि स्थालीनां नियुतानि च। न्यर्बुधानि च पात्राणि शातकुम्भमयानि च।।2.91.72।। स्थाल्यः कुम्भ्य करम्भ्य श् |
| 2.42.14 | 2.48.17 | 0.5 | purā bhavati no dūrād anugacchāma rāghavam pādacchāyā sukhā bhartus tādṛśasya mahātmanaḥ | पादच्छाया सुखा भर्तुस्तादृशस्य महात्मनः। स हि नाथो जनस्यास्य स गति स्सपरायणम्।।2.48.17।। |
| 2.84.19 | 2.90.20 | 0.5 | uvāca taṃ bharadvājaḥ prasādād bharataṃ vacaḥ tvayy etat puruṣavyāghraṃ yuktaṃ rāghavavaṃśaje | त्वय्येतत्पुरुषव्याघ्र युक्तं राघववंशजे। गुरुवृत्तिर्दमश्चैव साधूनामनुयायिता।।2.90.20।। |
| 2.101.6 | 2.109.5 | 0.5 | adharmaṃ dharmaveṣeṇa yadīmaṃ lokasaṃkaram abhipatsye śubhaṃ hitvā kriyāvidhivivarjitam | अनार्यस्त्वार्यसङ्काश श्शौचाद्दीनस्ताथाऽशुचिः। लक्षण्यवदलक्षण्यो दुश्शीलश्शीलवानिव।।2.109.5।। अधर्मं धर्मवेशेण यदीमं लोक |
| 2.49.2 | 2.55.2 | 0.503 | prasthitāṃś caiva tān prekṣya pitā putrān ivānvagāt tataḥ pracakrame vaktuṃ vacanaṃ sa mahāmuniḥ | तेषां चैव स्वस्त्ययनं महर्षि स्स चकार ह। प्रस्थितांश्चैव तान्प्रेक्ष्य पिता पुत्रानिवान्वगात्।।2.55.2।। |
| 2.14.6 | 2.16.8 | 0.504 | taṃ vaiśravaṇasaṃkāśam upaviṣṭaṃ svalaṃkṛtam dādarśa sūtaḥ paryaṅke sauvaṇo sottaracchade | तं वैश्रवणसङ्काशमुपविष्टं स्वलङ्कृतम्। ददर्श सूतः पर्य्यङ्के सौवर्णे सोत्तरच्छदे।।2.16.8।। वराहरुधिराभेण शुचिना च सुगन्ध |
| 2.88.8 | 2.94.8 | 0.504 | āmrajambvasanair lodhraiḥ priyālaiḥ panasair dhavaiḥ aṅkolair bhavyatiniśair bilvatindukaveṇubhiḥ | आम्रजम्ब्वसनैर्लोध्रैः प्रियालैः पनसैर्धवैः। अङ्कोलैर्भव्यतिनिशैर्बिल्वतिन्दुक वेणुभिः।।2.94.8।। काश्मर्यरिष्टवरुणैर्मधू |
| 2.74.2 | 2.80.1 | 0.506 | karmāntikāḥ sthapatayaḥ puruṣā yantrakovidāḥ tathā vardhakayaś caiva mārgiṇo vṛkṣatakṣakāḥ | अथ भूमिप्रदेशज्ञास्सूत्रकर्मविशारदाः। स्वकर्माभिरताश्शूराः खनका यन्त्रकास्तथा।।2.80.1।। कर्मान्तिकाः स्थपतयः पुरुष यन्त् |
| 2.28.12 | 2.31.27 | 0.507 | ye ca rājño dadau divye mahātmā varuṇaḥ svayam janakasya mahāyajñe dhanuṣī raudradarśane | ये च राज्ञो ददौ दिव्ये महात्मा वरुण स्स्वयम्। जनकस्य महायज्ञे धनुषी रौद्रदर्शने।।2.31.27।। अभेद्यकवचे दिव्ये तूणी चाक्षय |
| 2.45.19 | 2.51.21 | 0.509 | ramyacatvarasaṃsthānāṃ suvibhaktamahāpathām harmyaprāsādasaṃpannāṃ gaṇikāvaraśobhitām | रम्यचत्वरसंस्थानां सुविभक्तमहापथाम्। हर्म्यप्रासादसम्पन्नाम् गणिकावरशोभिताम्।।2.51.21।। रथाश्वगजसम्बाधां तूर्यनादविनादित |

## Minor edits (sim 0.6–0.9) — 297 pairs, sample of 60

| Critical locus | Gita Supersite locus | sim | Critical text | Gita Supersite text |
|---|---|---:|---|---|
| 2.18.32 | 2.21.37 | 0.601 | tām evam uktvā jananīṃ lakṣmaṇaṃ punar abravīt tava lakṣmaṇa jānāmi mayi sneham anuttamam | तामेवमुक्त्वा जननीं लक्ष्मणं पुनरब्रवीत्। वाक्यं वाक्यविदां श्रेष्ठश्श्रेष्ठस्सर्वधनुष्मताम्।।2.21.37।। |
| 2.97.3 |  | 0.603 | yannimittam imaṃ deśaṃ kṛṣṇājinajaṭādharaḥ hitvā rājyaṃ praviṣṭas tvaṃ tat sarvaṃ vaktum arhasi | यन्निमित्तमिमं देशं कृष्णाजिनजटाधरः। |
| 2.97.14 |  | 0.603 | evam uktvā mahābāhuḥ sabāṣpaḥ kekayīsutaḥ rāmasya śirasā pādau jagrāha bharataḥ punaḥ | एवमुक्त्वा महाबाहु स्सबाष्पः कैकयीसुतः। |
| 2.57.17 | 2.63.25 | 0.607 | tato 'haṃ śaram uddhṛtya dīptam āśīviṣopamam amuñcaṃ niśitaṃ bāṇam aham āśīviṣopamam | ततोऽहं शरमुधृत्य दीप्तमाशीविषोपमम्। शब्दं प्रति गजप्रेप्सुरभिलक्ष्य त्वपातयम्।।2.63.25।। |
| 2.68.27 |  | 0.607 | ānāyayitvā tanayaṃ kausalyāyā mahādyutim svayam eva pravekṣyāmi vanaṃ muniniṣevitam | ﻿अनाययित्वा तनयं कौसल्याया महाबलम्। |
| 2.104.7 |  | 0.609 | etāvad uktvā vacanaṃ gandharvāḥ samaharṣayaḥ rājarṣayaś caiva tathā sarve svāṃ svāṃ gatiṃ gatāḥ | एतावदुक्त्वा वचनं गन्धर्वा: स‌महर्षयः। |
| 2.95.23 |  | 0.611 | tato nityānugas teṣāṃ viditātmā mahāmatiḥ mṛdur dāntaś ca śāntaś ca rāme ca dṛḍha bhaktimān | ततो नित्यानुगस्तेषां विदितात्मा महामतिः। |
| 2.18.30 | 2.21.34 | 0.612 | na khalv etan mayaikena kriyate pitṛśāsanam pūrvair ayam abhipreto gato mārgo 'nugamyate | न खल्वेतन्मयैकेन क्रियते पितृशासनम्। एतैरपि कृतं देवि ये मया तव कीर्तिताः।।2.21.34।। |
| 2.97.12 |  | 0.612 | ebhiś ca sacivaiḥ sārdhaṃ śirasā yācito mayā bhrātuḥ śiṣyasya dāsasya prasādaṃ kartum arhasi | एभिश्च सचिवैस्सार्धं शिरसा याचितो मया। |
| 2.23.2 | 2.26.1 | 0.613 | virājayan rājasuto rājamārgaṃ narair vṛtam hṛdayāny āmamantheva janasya guṇavattayā | अभिवाद्य च कौसल्यां राम स्संप्रस्थितो वनम्। कृतस्वस्त्ययनो मात्रा धर्मिष्ठे वर्त्मनि स्थितः।।2.26.1।। विराजयन्राजसुतो रा |
| 2.60.1 | 2.66.1 | 0.613 | tam agnim iva saṃśāntam ambuhīnam ivārṇavam hataprabham ivādityaṃ svargathaṃ prekṣya bhūmipam | तमग्निमिव संशान्तमम्बुहीनमिवार्णवम्। हतप्रभमिवाऽऽदित्यं स्वर्गस्थं प्रेक्ष्य पार्थिवम्।।2.66.1।। कौसल्या बाष्पपूर्णाक्षी |
| 2.43.4 | 2.49.9 | 0.615 | śṛṇvan vāco manuṣyāṇāṃ grāmasaṃvāsavāsinām rājānaṃ dhig daśarathaṃ kāmasya vaśam āgatam | एता वाचो मनुष्याणां ग्रामसंवासवासिनाम्। शृण्वन्नतिययौ वीरः कोसलान् कोसलेश्वरः।।2.49.9।। |
| 2.66.12 |  | 0.615 | rājā bhavati bhūyiṣṭhgam ihāmbāyā niveśane tam ahaṃ nādya paśyāmi draṣṭum icchann ihāgataḥ | ﻿राजा भवति भूयिष्ठमिहाम्बाया निवेशने। |
| 2.105.23 | 2.113.23 | 0.616 | śṛṅgaverapurād bhūya ayodhyāṃ saṃdadarśa ha bharato duḥkhasaṃtaptaḥ sārathiṃ cedam abravīt | अयोध्यां च ततो दृष्ट्वा पित्रा भ्रात्रा विवर्जिताम्। भरतो दुःख सन्तप्त स्सारथिं चेदमब्रवीत्।।2.113.23।। |
| 2.1.34 | 2.1.40 | 0.618 | taṃ samīkṣya mahārājo yuktaṃ samuditair guṇaiḥ niścitya sacivaiḥ sārdhaṃ yuvarājam amanyata | इत्येतैर्विविधैस्तैस्तैरन्यपार्थिवदुर्लभैः।।2.1.40।। शिष्टैरपरिमेयैश्च लोके लोकोत्तरैर्गुणैः। तं समीक्ष्य महाराजो युक्तं |
| 2.58.40 | 2.64.49 | 0.618 | sa tu divyena rūpeṇa muniputraḥ svakarmabhiḥ āśvāsya ca muhūrtaṃ tu pitarau vākyam abravīt | आबभाषे च वृद्धौ तौ सह शक्रेण तापसः। आश्वास्यच मुहूर्तं तु पितरौ वाक्यमब्रवीत्।।2.64.49।। |
| 2.98.23 |  | 0.62 | nandanty udita āditye nandanty astam ite ravau ātmano nāvabudhyante manuṣyā jīvitakṣayam | नन्दन्त्युदित आदित्ये नन्दन्त्यस्तमितेऽहनि। |
| 2.104.6 |  | 0.62 | sadānṛṇam imaṃ rāmaṃ vayam icchāmahe pituḥ anṛṇatvāc ca kaikeyyāḥ svargaṃ daśaratho gataḥ | सदाऽनृणमिमं रामं वयमिच्छामहे पितुः। |
| 2.88.2 | 2.94.1 | 0.621 | atha dāśarathiś citraṃ citrakūṭam adarśayat bhāryām amarasaṃkāśaḥ śacīm iva puraṃdaraḥ | दीर्घकालोषित स्तस्मिन्गिरौ गिरिवनप्रियः। वैदेह्याः प्रियमाकाङ्क्षन्स्वं च चित्तं विलोभयन्।।2.94.1।। अथ दाशरथिश्चित्रं चि |
| 2.1.35 | 2.1.45 | 0.622 | nānānagaravāstavyān pṛthagjānapadān api samānināya medinyāḥ pradhānān pṛthivīpatiḥ | नानानगरवास्तव्यान्पृथग्जानपदानपि।।2.1.45।। |
| 2.82.2 | 2.88.1 | 0.622 | abravīj jananīḥ sarvā iha tena mahātmanā śarvarī śayitā bhūmāv idam asya vimarditam | तच्छ्रुत्वा निपुणं सर्वं भरत स्सह मन्त्रिभिः। इङ्गुदीमूलमागम्य रामशय्यामवेक्ष्य ताम्।।2.88.1।। अब्रवीज्जननी स्सर्वा इह त |
| 2.98.36 |  | 0.622 | ete bahuvidhāḥ śokā vilāpa rudite tathā varjanīyā hi dhīreṇa sarvāvasthāsu dhīmatā | एते बहुविधा शोका विलापरुदिते तथा। |
| 2.48.2 | 2.54.2 | 0.624 | yatra bhāgīrathī gaṅgā yamunām abhivartate jagmus taṃ deśam uddiśya vigāhya sumahad vanam | यत्र भागीरथीं गङ्गां यमुनाभिप्रवर्तते। जग्मुस्तं देशमुद्दिश्य विगाह्य सुमहद्वनम्।।2.54.2।। ते भूमिभागान्विविधान् देशांश् |
| 2.83.15 |  | 0.624 | āvāsam ādīpayatāṃ tīrthaṃ cāpy avagāhatām bhāṇḍāni cādadānānāṃ ghoṣas tridivam aspṛśat | आवासमादीपयतां तीर्थं चाप्यवगाहताम्। |
| 2.102.12 | 2.110.13 | 0.625 | yuvanāśva sutaḥ śrīmān māndhātā samapadyata māndhātus tu mahātejāḥ susaṃdhir udapadyata | युवनाश्वसुत श्श्रीमान्मान्धाता समपद्यत।।2.110.13।। |
| 2.102.19 |  | 0.625 | sa rājā sagaro nāma yaḥ samudram akhānayat iṣṭvā parvaṇi vegena trāsayantam imāḥ prajāḥ | स राजा सगरो नाम य: स‌मुद्रमखानयत्। |
| 2.31.27 | 2.34.33 | 0.626 | adya tv idānīṃ rajanīṃ putra mā gaccha sarvathā mātaraṃ māṃ ca saṃpaśyan vasemām adya śarvarīm | अद्य त्विदानीं रजनीं पुत्र मा गच्छ सर्वथा। एकाहदर्शनेनापि साधु तावच्चराम्यहम्।।2.34.33।। |
| 2.57.9 | 2.63.13 | 0.626 | saṃmohād iha bālena yathā syād bhakṣitaṃ viṣam evaṃ mamāpy avijñātaṃ śabdavedhyamayaṃ phalam | यथान्यः पुरुषः कश्चित्पलाशैर्मोहितो भवेत्। एवं ममाऽप्यविज्ञातं शब्दवेध्यमयं फलम्।।2.63.13।। |
| 2.95.32 |  | 0.626 | tatas tenaiva mārgeṇa pratyuttīrya nadītaṭāt āruroha naravyāghro ramyasānuṃ mahīdharam | तत स्तेनैव मार्गेण प्रत्युत्तीर्य सरित्तटात्। |
| 2.4.22 |  | 0.627 | tatra puṣye 'bhiṣiñcasva manas tvarayatīva mām śvas tvāham abhiṣekṣyāmi yauvarājye paraṃtapa | ﻿﻿ततः पुष्येऽभिषिञ्चस्व मनस्त्वरयतीव माम्। |
| 2.13.17 | 2.15.21 | 0.627 | ity uktvāntaḥpuradvāram ājagāma purāṇavit āśīrbhir guṇayuktābhir abhituṣṭāva rāghavam | सोऽत्यासाद्य तु तद्वेश्म तिरस्करणिमन्तरा।।2.15.21।। आशीर्भिर्गुणयुक्ताभि रभितुष्टाव राघवम्। |
| 2.13.5 | 2.15.5 | 0.628 | gaṅgāyamunayoḥ puṇyāt saṃgamād āhṛtaṃ jalam yāś cānyāḥ saritaḥ puṇyā hradāḥ kūpāḥ sarāṃsi ca | गङ्गायमुनयोःपुण्यात्सङ्गमादाहृतं जलम्।।2.15.5।। याश्चान्या स्सरितः पुण्या ह्रदाः कूपा स्सरांसि च। प्राग्वाहाश्चोर्ध्ववाह |
| 2.14.1 | 2.16.1 | 0.628 | sa tad antaḥpuradvāraṃ samatītya janākulam praviviktāṃ tataḥ kakṣyām āsasāda purāṇavit | तदन्तःपुरद्वारं समतीत्य जनाकुलम्। प्रविविक्तां ततः कक्ष्यामाससाद पुराणवित्।।2.16.1।। प्रासकार्मुकबिभ्रद्भिर्युवभिर्मृष्ट |
| 2.68.20 |  | 0.628 | evam uktā tu surabhiḥ surarājena dhīmatā patyuvāca tato dhīrā vākyaṃ vākyaviśāradā | ﻿एवमुक्ता तु सुरभि स्सुरराजेन धीमता। |
| 2.97.18 |  | 0.628 | yāvat pitari dharmajña gauravaṃ lokasatkṛte tāvad dharmabhṛtāṃ śreṣṭha jananyām api gauravam | यावत पितरि धर्मज्ञे गौरवं लोकसत्कृतम्। |
| 2.2.30 |  | 0.629 | balam ārogyam āyuś ca rāmasya viditātmanaḥ āśaṃsate janaḥ sarvo rāṣṭre puravare tathā | ﻿बलमारोग्यमायुश्च रामस्य विदितात्मनः। |
| 2.4.2 | 2.4.1 | 0.629 | śva eva puṣyo bhavitā śvo 'bhiṣecyeta me sutaḥ rāmo rājīvatāmrākṣo yauvarājya iti prabhuḥ | गतेष्वथ नृपो भूयः पौरेषु सह मन्त्रिभिः। मन्त्रयित्वा ततश्चक्रे निश्चयज्ञस्सनिश्चयम्।।2.4.1।। श्व एव पुष्यो भविताश्वोऽभिष |
| 2.16.60 | 2.19.34 | 0.629 | dhārayan manasā duḥkham indriyāṇi nigṛhya ca praviveśātmavān veśma māturapriyaśaṃsivān | प्रतिषिध्य शुभं छत्रं व्यजने च स्वलङ्कृते। विसर्जयित्वा स्वजनं रथं पौरांस्तथा जनान्।।2.19.34।। धारयन् मनसा दुःखमिन्द्रिय |
| 2.23.23 | 2.26.24 | 0.629 | bharatasya samīpe te nāhaṃ kathyaḥ kadā cana ṛddhiyuktā hi puruṣā na sahante parastavam | सोऽहं त्वामागतो द्रष्टुं प्रस्थितो विजनं वनम्। भरतस्य समीपे तु नाहं कथ्यः कदाचन।।2.26.24।। बुद्धियुक्ता हि पुरुषा न सहन् |
| 2.98.39 |  | 0.629 | na mayā śāsanaṃ tasya tyaktuṃ nyāyyam ariṃdama tat tvayāpi sadā mānyaṃ sa vai bandhuḥ sa naḥ pitā | न मया शासनं तस्य त्यक्तुं न्याय्य मरिन्दम। |
| 2.68.21 | 2.74.23 | 0.63 | śāntaṃ pātaṃ na vaḥ kiṃ cit kutaś cid amarādhipa ahaṃ tu magnau śocāmi svaputrau viṣame sthitau | शान्तं पापं न वः किञ्चित्कुतश्चिदमराधिपः। अहं मग्नौ तु शोचामि स्वपुत्रौ विषमे स्थितौ।।2.74.23।। एतौ दृष्ट्वा कृशौ दीनौ स |
| 2.9.9 | 2.9.11 | 0.631 | tava devāsure yuddhe saha rājarṣibhiḥ patiḥ agacchat tvām upādāya devarājasya sāhyakṛt | तव दैवासुरे युद्धे सह राजर्षिभिः पतिः। अगच्छत्त्वामुपादाय देवराजस्य साह्यकृत्।।2.9.11।। दिशमास्थाय वै देवि दक्षिणां दण्ड |
| 2.95.9 | 2.102.2 | 0.631 | vāgvajraṃ bharatenoktam amanojñaṃ paraṃtapaḥ pragṛhya bāhū rāmo vai puṣpitāgro yathā drumaḥ | तं तु वज्रमिवोत्सृष्टमाहवे दानवारिणा वाग्वज्रंभरते नोक्त ममनोज्ञं परन्तपः।।2.102.2।। प्रगृह्य रामो बाहू वैपुष्पिताग्रो य |
| 2.97.16 |  | 0.632 | kulīnaḥ sattvasaṃpannas tejasvī caritavrataḥ rājyahetoḥ kathaṃ pāpam ācaret tvadvidho janaḥ | कुलीन:सत्त्वसम्पन्नस्तेजस्वी चरितव्रतः। |
| 2.3.29 | 2.3.46 | 0.633 | tac chrutvā suhṛdas tasya rāmasya priyakāriṇaḥ tvaritāḥ śīghram abhyetya kausalyāyai nyavedayan | ﻿तच्छ्रुत्वा सुहृदस्तस्य रामस्य प्रियकारिणः।।2.3.46।। |
| 2.66.25 |  | 0.633 | kva sa pāṇiḥ sukhasparśas tātasyākliṣṭakarmaṇaḥ yena māṃ rajasā dhvastam abhīkṣṇaṃ parimārjati | ﻿क्व स पाणिस्सुखस्पर्शस्तातस्याक्लिष्टकर्मणः। |
| 2.70.4 | 2.76.4 | 0.633 | uddhṛtaṃ tailasaṃkledāt sa tu bhūmau niveśitam āpītavarṇavadanaṃ prasuptam iva bhūmipam | उद्धृतं तैलसंरोधात्सतु भूमौ निवेशितम्। आपीतवर्णवदनं प्रसुप्तमिव भूमिपम्।।2.76.4।। संवेश्य शयने चाग्य्रे नानारत्नपरिष्कृत |
| 2.95.43 |  | 0.633 | rathāṅgasāhvā natyūhā haṃsāḥ kāraṇḍavāḥ plavāḥ tathā puṃskokilāḥ krauñcā visaṃjñā bhejire diśaḥ | रथाङ्गसाह्वा नत्यूहा हंसाः कारण्डवाः परे। |
| 2.3.14 | 2.3.30 | 0.634 | avatārya sumantras taṃ rāghavaṃ syandanottamāt pituḥ samīpaṃ gacchantaṃ prāñjaliḥ pṛṣṭhato 'nvagāt | ﻿अवतार्य सुमन्त्रस्तं राघवं स्यन्दनोत्तमात्।।2.3.30।। |
| 2.81.2 | 2.87.2 | 0.634 | sukumāro mahāsattvaḥ siṃhaskandho mahābhujaḥ puṇḍarīka viśālākṣas taruṇaḥ priyadarśanaḥ | सुकुमारो महासत्त्वस्सिंहस्कन्धो महाभुजः। पुण्डरीकविशालाक्ष स्तरुणः प्रियदर्शनः।।2.87.2।। प्रत्याश्वस्य मुहूर्तं तु कालं  |
| 2.5.13 |  | 0.635 | hṛṣṭanārī narayutaṃ rāmaveśma tadā babhau yathā mattadvijagaṇaṃ praphullanalinaṃ saraḥ | ﻿हृष्टनारीनरयुतं रामवेश्म तदा बभौ। |
| 2.102.10 |  | 0.635 | anaraṇyān mahābāhuḥ pṛthū rājā babhūva ha tasmāt pṛthor mahārājas triśaṅkur udapadyata | अनरण्यान्महाबाहुः पृथु राजा बभूव ह। |
| 2.5.18 |  | 0.636 | tadā hy ayodhyā nilayaḥ sastrībālābalo janaḥ rāmābhiṣekam ākāṅkṣann ākāṅkṣann udayaṃ raveḥ | ﻿तदा ह्ययोध्यानिलयः सस्त्रीबालाबलो जनः। |
| 2.59.12 | 2.65.27 | 0.636 | tat samuttrastasaṃbhrāntaṃ paryutsukajanākulam sarvatas tumulākrandaṃ paritāpārtabāndhavam | तत् परित्रस्तन्त्रसम्भ्रान्त पर्युत्सुकजनाकुलम्। सर्वतस्तुमुलाक्रन्दं परितापार्तबान्धवम्।।2.65.27।। सद्यो निपतितानन्दं द |
| 2.57.27 | 2.63.38 | 0.637 | taṃ deśam aham āgamya dīnasattvaḥ sudurmanāḥ apaśyam iṣuṇā tīre sarayvās tāpasaṃ hatam | तं देशमहमागम्य दीनसत्त्वस्सुदुर्मनाः। अपश्यमिषुणा तीरे सरय्वास्तापसं हतम्।।2.63.38।। अवकीर्ण जटाभारं प्रविद्धकलशोदकम्। प |
| 2.85.15 | 2.91.17 | 0.637 | ghṛtācīm atha viśvācīṃ miśrakeśīm alambusām śakraṃ yāś copatiṣṭhanti brahmāṇaṃ yāś ca bhāminīḥ | घृताचीमथ विश्वाचीं मिश्रकेशीमलंबुसाम्। नागदन्तां च हेमां च हिमामद्रिकृतस्थलाम्।।2.91.17।। |
| 2.101.31 |  | 0.637 | dharme ratāḥ satpuruṣaiḥ sametās; tejasvino dānaguṇapradhānāḥ ahiṃsakā vītamalāś ca loke; bhavanti pūjyā munayaḥ pradhān | धर्मे रता: स‌त्पुरुषै: स‌मेतास्तेजस्विनो दानगुणप्रधानाः। |
| 2.103.6 |  | 0.637 | vṛddhāyā dharmaśīlāyā mātur nārhasy avartitum asyās tu vacanaṃ kurvan nātivarteḥ satāṃ gatim | वृद्धाया धर्मशीलाया मातुर्नार्हस्यवर्तितुम्। |
| 2.48.25 | 2.54.28 | 0.638 | daśakrośa itas tāta girir yasmin nivatsyasi maharṣisevitaḥ puṇyaḥ sarvataḥ sukha darśanaḥ | दशक्रोश इतस्तात गिरिर्यत्रनिवत्स्यसि। महर्षिसेवितः पुण्यः सर्वतः सुखदर्शनः।।2.54.28।। गोलाङ्गूलानुचरितो वानरर्क्षनिषेवित |
| 2.53.12 | 2.59.19 | 0.638 | aprahṛṣṭamanuṣyā ca dīnanāgaturaṃgamā ārtasvaraparimlānā viniḥśvasitaniḥsvanā | अप्रहृष्टमनुष्या च दीननागतुरङ्गमा। आर्तस्वरपरिम्लाना विनिश्श्वसितनिस्स्वना।।2.59.19।। निरानन्दा महाराज रामप्रव्राजनातुरा |

## Critical-only — 173, sample of 30

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
| 2.1.25 | anasūyo jitakrodho na dṛpto na ca matsarī na cāvamantā bhūtānāṃ na ca kālavaśānugaḥ |
| 2.2.21 | kṣāntaḥ sāntvayitā ślakṣṇaḥ kṛtajño vijitendriyaḥ mṛduś ca sthiracittaś ca sadā bhavyo 'nasūyakaḥ |
| 2.2.23 | tenāsyehātulā kīrtir yaśas tejaś ca vardhate devāsuramanuṣyāṇāṃ sarvāstreṣu viśāradaḥ |
| 2.2.26 | putreṣv agniṣu dāreṣu preṣyaśiṣyagaṇeṣu ca nikhilenānupūrvyā ca pitā putrān ivaurasān |
| 2.2.32 | sarvān devān namasyanti rāmasyārthe yaśasvinaḥ teṣām āyācitaṃ deva tvatprasādāt samṛdhyatām |
| 2.3.9 | mlecchāś cāryāś ca ye cānye vanaśailāntavāsinaḥ upāsāṃ cakrire sarve taṃ devā iva vāsavam |
| 2.3.12 | candrakāntānanaṃ rāmam atīva priyadarśanam rūpaudāryaguṇaiḥ puṃsāṃ dṛṣṭicittāpahāriṇam |
| 2.3.13 | gharmābhitaptāḥ parjanyaṃ hlādayantam iva prajāḥ na tatarpa samāyāntaṃ paśyamāno narādhipaḥ |
| 2.6.4 | vāgyataḥ saha vaidehyā bhūtvā niyatamānasaḥ śrīmaty āyatane viṣṇoḥ śiśye naravarātmajaḥ |
| 2.6.12 | nānāpaṇyasamṛddheṣu vaṇijām āpaṇeṣu ca kuṭumbināṃ samṛddheṣu śrīmatsu bhavaneṣu ca |
| 2.6.13 | sabhāsu caiva sarvāsu vṛkṣeṣv ālakṣiteṣu ca dhvajāḥ samucchritāś citrāḥ patākāś cābhavaṃs tadā |
| 2.6.20 | sametya saṃghaśaḥ sarve catvareṣu sabhāsu ca kathayanto mithas tatra praśaśaṃsur janādhipam |
| 2.7.3 | patākābhir varārhābhir dhvajaiś ca samalaṃkṛtām siktāṃ candanatoyaiś ca śiraḥsnātajanair vṛtām |
| 2.9.10 | diśam āsthāya kaikeyi dakṣiṇāṃ daṇḍakān prati vaijayantam iti khyātaṃ puraṃ yatra timidhvajaḥ |
| 2.9.13 | tatrāpi vikṣataḥ śastraiḥ patis te rakṣitas tvayā tuṣṭena tena dattau te dvau varau śubhadarśane |
| 2.9.43 | anekaśatasāhasraṃ muktāhāraṃ varāṅganā avamucya varārhāṇi śubhāny ābharaṇāni ca |
| 2.9.44 | tato hemopamā tatra kubjā vākyaṃ vaśaṃ gatā saṃviśya bhūmau kaikeyī mantharām idam abravīt |
| 2.10.12 | ātmano jīvitenāpi brūhi yan manasecchasi yāvad āvartate cakraṃ tāvatī me vasuṃdharā |
| 2.10.23 | niśācarāṇi bhūtāni gṛheṣu gṛhadevatāḥ yāni cānyāni bhūtāni jānīyur bhāṣitaṃ tava |
| 2.10.30 | tataḥ śrutvā mahārāja kaikeyyā dāruṇaṃ vacaḥ vyathito vilavaś caiva vyāghrīṃ dṛṣṭvā yathā mṛgaḥ |
| 2.10.31 | asaṃvṛtāyām āsīno jagatyāṃ dīrgham ucchvasan aho dhig iti sāmarṣo vācam uktvā narādhipaḥ |

## Gita Supersite-only — 1066, sample of 30

| Locus | Text |
|---|---|
| 2.1.1 | गच्छता मातुलकुलं भरतेन तदाऽनघ। शत्रुघ्नो नित्यशत्रुघ्नो नीतः प्रीतिपुरस्कृतः।।2.1.1।। |
| 2.1.7 | स हि देवैरुदीर्णस्य रावणस्य वधार्थिभिः। अर्थितो मानुषे लोके जज्ञे विष्णुस्सनातनः।।2.1.7।। |
| 2.1.8 | कौशल्या शुशुभे तेन पुत्रेणामिततेजसा। यथा वरेण देवानामदितिर्वज्रपाणिना।।2.1.8।। |
| 2.1.9 | स हि रूपोपपन्नश्च वीर्यवाननसूयकः। भूमौवनुपमस्सूनुर्गुणैर्दशरथोपमः।।2.1.9।। |
| 2.1.13 | बुद्धिमान्मधुराभाषी पूर्वभाषी प्रियंवदः। वीर्यवान्न च वीर्येण महता स्वेन विस्मितः।।2.1.13।। |
| 2.1.14 | नचानृतकथो विद्वान् वृद्धानां प्रतिपूजकः। अनुरक्तः प्रजाभिश्च प्रजाश्चाप्यनुरञ्जते।।2.1.14।। |
| 2.1.15 | सानुक्रोशो जितक्रोधो ब्राह्मणप्रतिपूजकः। दीनानुकम्पी धर्मज्ञो नित्यं प्रग्रहवांश्चुचिः।।2.1.15।। |
| 2.1.16 | कुलोचितमतिः क्षात्रं धर्मं स्वं बहुमन्यते। मन्यते परया कीर्त्या महत्स्वर्गफलं ततः।।2.1.16।। |
| 2.1.17 | नाऽऽश्रेयसि रतो विद्वान्नविरुद्धकथारुचिः। उत्तरोत्तरयुक्तौ च वक्ता वाचस्पतिर्यथा।।2.1.17।। |
|  | ﻿अरोगस्तरुणो वाग्मी वपुष्मान्देशकालवित्। |
| 2.1.19 | स तु श्रेष्ठैर्गुणैर्युक्तः प्रजानां पार्थिवात्मजः। बहिश्चर इव प्राणो बभूव गुणतः प्रियः।।2.1.19।। |
| 2.1.20 | सम्यग्विद्याव्रतस्नातो यथावत्साङ्गवेदवित्। इष्वस्त्रे च पितु श्श्रेष्ठो बभूव भरताग्रजः।।2.1.20।। |
| 2.1.23 | निभृत स्संवृताकारो गुप्तमन्त्र स्सहायवान्। अमोघक्रोधहर्षश्च त्यागसंयमकालवित्।।2.1.23।। |
|  | ﻿दृढभक्ति स्स्थिरप्रज्ञो नासद्ग्राही न दुर्वचाः। |
| 2.1.26 | सत्सङ्ग्रहप्रग्रहणे स्थानविन्निग्रहस्य च। आयकर्मण्युपायज्ञ स्सन्दृष्टव्ययकर्मवित्।।2.1.26।। |
| 2.1.35 | अथ राज्ञो बभूवैवं वृद्धस्य चिरजीविनः।।2.1.35।। |
| 2.1.42 | दिव्यन्तरिक्षे भूमौ च घोरमुत्पातजं भयम्।।2.1.42।। स़ञ्चचक्षेऽथ मेधावी शरीरे चात्मनो जराम्। |
| 2.1.43 | पूर्णचन्द्राननस्याथ शोकापनुदमात्मनः।।2.1.43।। लोके रामस्य बुबुधे सम्प्रियत्वं महात्मनः। |
| 2.1.44 | आत्मनश्च प्रजानां च श्रेयसे च प्रियेण च।।2.1.44।। प्राप्तकालेन धर्मात्मा भक्त्या त्वरितवान् नृपः। |
| 2.1.46 | न तु केकयराजानं जनकं वा नराधिपः।।2.1.46।। त्वरया चानयामास पश्चात्तौ श्रोष्यतः प्रियम्। |
| 2.1.47 | तान्वेश्मनानाभरणैर्यथाऽर्हं प्रतिपूजितान्।।2.1.47।। ददर्शालङ्कृतो राजा प्रजापतिरिव प्रजाः। |
| 2.1.48 | अथोपविष्टे नृपतौ तस्मिन्परबलार्दने।।2.1.48।। ततः प्रविविशु श्शेषा राजानो लोकसम्मताः। |
| 2.2.4 | विदितं भवतामेतद्यथा मे राज्यमुत्तमम्। पूर्वकैर्मम राजेन्द्रैस्सुतवत्परिपालितम्।।2.2.4।। |
| 2.2.15 | यदिदं मेऽनुरूपार्थं मया साधु सुमन्त्रितम्। भवन्तो मेऽनुमन्यन्तां कथं वा करवाण्यहम्।।2.2.15।। |
| 2.2.16 | यद्यप्येषा मम प्रीतिर्हितमन्यद्विचिन्त्यताम्। अन्या मध्यस्थचिन्ता हि विमर्दाभ्यधिकोदया।।2.2.16।। |
| 2.2.18 | स्निग्धोऽनुनादी संजज्ञे तत्र हर्षसमीरितः। जनौघोद्घुष्टसन्नादो विमानं कम्पयन्निव।।2.2.18।। |
| 2.2.22 | इच्छामो हि महाबाहुं रघुवीरं महाबलम्। गजेन महताऽयान्तं रामं छत्रावृताननम्।।2.2.22।। |
| 2.2.24 | श्रुत्वैव वचनं यन्मे राघवं पतिमिच्छथ। राजान स्संशयोऽयं मे किमिदं ब्रूत तत्त्वतः।।2.2.24।। |
| 2.2.27 | गुणान् गुणवतो देव देवकल्पस्य धीमतः। प्रियानानन्दनान्कृत्स्नान्प्रवक्ष्यामोऽद्य तान् शृणु।।2.2.27।। |
| 2.2.29 | राम स्सत्पुरुषो लोके सत्यधर्मपरायणः। साक्षाद्रामाद्विनिर्वृत्तो धर्मश्चापि श्रिया सह।।2.2.29।। |

## Full data

Complete machine-readable results alongside this file: `scratchpad/ayodhya_gitasupersite_alignment.json`
