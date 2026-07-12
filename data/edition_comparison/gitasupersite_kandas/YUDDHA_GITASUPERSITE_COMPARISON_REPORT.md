# Yuddhakāṇḍa: Leonov Sanskrit source vs Gita Supersite

_Created: 12-07-2026_

> Leonov vs Gita Supersite. Content-aligned via difflib LCS + fuzzy character-4gram-Jaccard
> rescue (word-boundary-robust -- Gita Supersite text does not consistently space-separate
> sandhi-joined words), canonicalized via `sanskrit_util.nfold`.
> Replaces the earlier valmikiramayan.net-based comparison (rights-cleared source now used).

## ✅ Rights status

Both sources are properly licensed: Gita Supersite text is used under the CC BY 4.0 grant
from Sudalaimuthu Palaniappan (`CommentaryStrategies/data/valmiki_PERMISSION.md`). This
supersedes the earlier valmikiramayan.net-based comparison, which had no permission on file.

## Summary

| Leonov verses | Gita Supersite verses | Identical | Variant pairs | near-id (≥.9) | minor (.6-.9) | major (<.6) | Leonov-only | Gita Supersite-only |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 5728 | 5209 | 4 | 5031 | 3353 | 1270 | 408 | 693 | 174 |

## Major differences (sim < 0.6) — 408 pairs, showing up to 60

| Leonov locus | Gita Supersite locus | sim | Leonov text | Gita Supersite text |
|---|---|---:|---|---|
| 6.123.52 | 6.126.54 | 0.217 | [nānādvijagaṇākīrṇā saṃprapuṣpitakānanā \|\|] śṛṅgaverapuraṃ caitad guho yatra sakhā mama \| [eṣā sā dṛśyate site sarayū | शृङ्गिबेरपुरंचैतद्गुहोयत्रसखामम । एषासादृश्यतेसीतेसरयूर्यूपमालिनी ।।6.126.54।। नानातरुशताकीर्णासम्प्रपुष्पितकानना । |
| 6.28.35 | 6.28.34 | 0.323 | śatam vṛndasahasrāṇām mahāvṛndamiti smṛtam \| mahāvṛndasahasrāṇām śatam padmamihocyate \|\| | शतंशङ्कुसहस्राणांमहाशङ्कु: इतिस्मृतः ।।6.28.34।। महाशङ्कुसहस्राणांशतंबृन्दमिहोच्यते । शतंबृन्दसहस्राणांमहावृन्दमितिस्मृत |
| 6.11.14 | 6.11.15 | 0.341 | asasāda mahātejāḥ sabhām viracitām tadā suvarṇarajatāstīrṇām viśuddhasphaṭikāntarām | सुवर्णरजतास्तीर्णांविशुद्धस्फटिकान्तराम् । विराजमानोवपुषारुक्मपट्टोत्तरच्छदाम् ।।6.11.15।। तांपिशाचशतै: षङ्भिरभिगुप्तांस |
| 6.74.15 | 6.74.15 | 0.367 | dṛṣṭvā samabhisaṃkramya paulastyō vākyam abravīt kaścid ārya śarais tīkṣṇair na prāṇā dhvaṃsitās tava ।। | च्चिदार्यशरैस्तीक्ष्णैर्नप्राणाध्वंसितास्तव ।।6.74.15।। विभीषणवचश्श्रुत्वाजाम्बवानृक्षपुङ्गवः । कृच्छ्रादभ्युग्दिरन्वाक् |
| 6.127.13 | 6.130.13 | 0.38 | niryayus turagākrantā rathaiś ca sumahārathāḥ \| śaktyuṛṣṭipāśahastānāṃ sadhvajānāṃ patākinām | शक्त्यृष्टिपाशहस्तानांसध्वजानांपताकिनाम् ।।6.130.13।। तुरगाणांसहस्रैश्चमुख्यैर्मुख्यतरान्वितैः । पदातीनांसहस्रैश्चवीराःप |
| 6.22.48 | 6.22.49 | 0.381 | aurasas tasya putro ‘ham sadṛśo viśvakarmaṇā\| smārito ‘asmy aham etena tattvam āha mahodadhiḥ \|\| na ca apy aham anukt | मममातुर्वरोदत्तोमन्दरेविश्वकर्मणा । औरसस्तस्यपुत्रोऽहंसदृशोविश्वकर्मणा ।।6.22.49।। नचाप्यहमनुक्तोवःप्रब्रूयामात्मनोगुणान |
| 6.26.42 | 6.26.45 | 0.388 | ṣaṣṭiḥ śatasahasrāṇi balam asya plavaṃgamāḥ \| tvām āhvayati yuddhāya krathano nāma yūthapaḥ \|\| | त्वामाह्वयतियुद्धायक्रोधनोनामयूधपः । विक्रान्ताबलवन्तश्चयथायूथानिभागशः ।।6.26.45।। |
| 6.75.68 | 6.75.70 | 0.388 | prāvartata mahāraudraṃ yuddhaṃ vānararakṣasām vānarān daśa saptēti rākṣasā jaghnur āhavē ।। | वानरान्दशसप्तेतिराक्षसाजघ्नुराहवे । राक्षसान्दशसप्तेतिवानराश्चाभ्यपातयन् ।।6.75.70।। |
| 6.67.44 | 6.67.45 | 0.389 | cikṣēpa śailaśikharaṃ kumbhakarṇasya mūrdhani sa tēnābhihatō mūrdhni śailēnēndraripus tadā ।। | स तेनाभिहतोमूर्ध्निशैलेनेन्द्ररिपुस्तदा ।।6.67.45।। कुम्भकर्णःप्रजज्वालक्रोधेनमहतातदा । सोऽभ्यधावतवेगेनवालिपुत्रममर्षणम् |
| 6.59.123 | 6.59.126 | 0.393 | viṣṇur yathā garutmantam āruhyāmaravairiṇam tac chrutvā rāghavō vākyaṃ vāyuputrēṇa bhāṣitam ।। | तच्छ्रुत्वाराघवोवाक्यंवायुपुत्रेणभाषितम् । आरुरोहमहाशूरंबलवन्तंमहाकपिम् ।।6.59.126।। रथस्थंरावणंसङ् ख्येददर्शमनुजाधिपः । |
| 6.54.12 | 6.54.12 | 0.396 | prābhajyata balaṃ sarvaṃ vajradaṃṣṭrasya paśyataḥ rākṣasān bhayavitrastān hanyamānān plavaṅgamaiḥ \|\| | राक्षसान्भयवित्रस्तान्हन्यमानान् प्लवङ्गमैः ।।6.54.12।। दृष्टवासरोषताम्राक्षोवज्रदंष्ट्रःप्रतापवान् । प्रविवेशधनुष्पाणिस |
| 6.127.30 | 6.130.30 | 0.404 | vimānaṃ puṣpakaṃ divyaṃ manasā brahmanirmitam \| rāvaṇaṃ bāndhavaiḥ sārdhaṃ hatvā labdhaṃ mahātmanā | रावणंबान्धवैःसार्थंहत्वालब्धंमहात्मना । तरुणादित्यसङ्काशंविमानंरामवाहनम् ।।6.130.30।। धनदस्यप्रसादेनदिव्यमेतन्मनोजवम् । |
| 6.89.34 | 6.90.34 | 0.409 | nirantaram ivākāśaṃ babhūva tamasā vṛtam taiḥ patadbhiś ca bahubhis tayoḥ śaraśataiḥ śitaiḥ R_6,077. | ताभामुभाभ्यांतरसाप्रसृष्टैर्विशिखैःशितैः । निरन्तरमिवाकाशंबभूवतमसावृतम् ।।6.90.34।। |
| 6.25.4 | 6.25.4 | 0.41 | bhavantau vānaram sainyam praviśyānupalakṣitau \| parimāṇam ca vīryam ca ye ca mukhyāḥ plavaṃgamāḥ \|\| | भवन्तौवानरंसैन्यंप्रविश्यानुपलक्षितौ । परिमाणंचवीर्यंचयेचमुख्याःप्लवङ्घमाः ।।6.25.4।। मन्त्रिणोयेचरामस्यसुग्रीवस्यचसम्मत |
| 6.126.45 | 6.129.46 | 0.415 | abhijñānaṃ mayā dattaṃ rāmanāmāṅgulīyakam \| abhijñānaṃ maṇiṃ labdhvā caritārtho ‘ham āgataḥ | अभिज्ञानंमणिंलब्द्वाचरितार्धो हमागतः । मया च पुनरागम्यरामस्याक्लिष्टकर्मणः ।।6.129.46।। अभिज्ञानंमयादत्तमर्चिष्मान् स मह |
| 6.89.10 | 6.126.6 | 0.423 | prahasto nihato vīro nikumbhaś ca mahābalaḥ kumbhakarṇaś ca kumbhaś ca dhūmrākṣaś ca niśācaraḥ R_6,077. | कुम्भकर्णोऽऽत्रनिहतःप्रहस्तश्चनिशाचरः । धूम्राक्षश्चात्रनिहतोवानरेणहनूमता ।।6.126.6।। |
| 6.41.44 | 6.41.43 | 0.427 | dvārē dvārē harīṇāṃ tu kōṭiṃ kōṭī nyavēśayat paścimēna tu rāmasya suṣēṇaḥ sahajāmbavān \|\| | शासनेनतुरामस्यलक्ष्मणस्सविभीषणः । द्वारेद्वारेहरीणांतुकोटिंकोटिंन्यवेशयेत् ।।6.41.43।। |
| 6.40.5 | 6.40.3 | 0.428 | nīlajīmūtasaṃkāśaṃ hemasaṃchāditāmbaram \| airāvataviṣāṇāgrair utkṛṣṭakiṇavakṣasam \|\| | तस्यांगोपुरशृङ्गस्थंराक्षसेन्द्रंदुरासदम् ।।6.40.3।। श्वेतचामरपर्यन्तंविजयच्छत्रशोभितम् । रक्तचन्दनसंलिप्तंरत्नाभरणभूषित |
| 6.26.13 | 6.41.56 | 0.429 | laṅkā pratihatā sarvā saśailavanakānanā \| sarvaśākhāmṛgendrasya sugrīvasya mahātmanaḥ \|\| | तेनशब्देनमहतासप्राकारासतोरणा ।।6.41.56।। लङ्काप्रचलितासर्वासशैलवनकानना । |
| 6.31.16 | 6.31.16 | 0.429 | vyasanenātmanaḥ sīte mama bhāryā bhaviṣyasi \| visṛjaitāṃ matiṃ mūḍhe kiṃ mṛtena kariṣyasi \|\| | विसृजेमांमतिंमूढे: किंमृतेनकरिष्यसि । भवस्वभद्रे: भार्याणांसर्वेसामीश्वरीमम ।।6.31.16।। |
| 6.117.23 | 6.120.24 | 0.429 | trīṃl lokān dhārayan rāma devagandharvadānavān \| ahaṃ te hṛdayaṃ rāma jihvā devī sarasvatī | अहंतेहृदयंरामजिह्वादेवीसरस्वती ।।6.120.24।। देवारोमाणिगात्रेषुब्रह्मणानिर्मिताःप्रभो । |
| 6.106.2 | 6.108.1 | 0.43 | yuktaṃ paramasaṃpannair vāibhir hemamālibhiḥ \| yuddhopakaraṇaiḥ pūrṇaṃ patākādhvajamālinam | स रथंसारथिःहृष्टंपरसैन्यप्रधर्षणम् । गन्धर्वनगराकारंसमुच्छ्रितपाताकिनम् ।।6.108.1।। युक्तंपरमसम्पन्नैर्वजिभिर्हेममालिभिः |
| 6.125.34 | 6.128.34 | 0.43 | balamukhyaiśca yuktaiśca kāṣāyāmbaradhāribhiḥ \| na hi te rājaputraṃ taṃ cīrakṛṣṇājināmbaram | नहितेराजपुत्रंतंचीरकृष्णाजिनाम्बरम् ।।6.128.34।। परिभोक्तुंव्यवस्यन्तिपौरावैधर्मवत्सलाः । |
| 6.26.8 | 6.26.7 | 0.432 | ālokya rāvaṇo rājā paripapracca sāraṇam \| eṣām ko vānarā mukhyāḥ ke śūrāḥ ke mahābalāḥ \|\| | तदपारमसंख्ख्येयंवानराणांमहद्बलं । अलोक्यरावणोराजापरिपप्रच्छसारणम् ।।6.26.7।। |
| 6.123.40 | 6.126.40 | 0.433 | samayaś ca kṛtaḥ sīte vadhārthaṃ vālino mayā \| eṣā sā dṛśyate pampā nalinī citrakānanā | एषासादृश्यतेपम्पानलिनीचित्रकानना ।।6.126.40 ।। त्वयाविहीनोयत्राहंविललापसुदुःखितः । |
| 6.27.46 | 6.27.46 | 0.435 | rāmapriyārtham prāṇānām dayām na kurute hariḥ \| gajo gavākṣo gavayo nalo nīlaś ca vānaraḥ \|\| | गजोगवाक्षोगवयोनलोनीलश्चवानरः । एकैकएवयोधानांकोटीभिर्दशभिर्वृतः ।।6.27.46।। |
| 6.44.34 | 6.44.35 | 0.436 | adṛśyō niśitān bāṇān mumōcāśanivarcasaḥ rāmaṃ ca lakṣmaṇaṃ caiva ghōrair nāgamayaiḥ śaraiḥ \|\| | सोऽन्तर्धानगतःपापोरावणीरणकर्कशः । अदृश्योनिशितान्बाणान्मुमोचाशनिवर्चसः ।।6.44.35।। |
| 6.65.21 | 6.65.21 | 0.437 | kumbhakarṇō mahātējā rāvaṇaṃ vākyam abravīt gamiṣyāmy aham ēkākī tiṣṭha tv iha balaṃ mahat ।। | गमिष्याम्यहमेकाकीतिष्ठत्विहबलंमम ।।6.65.21।। अद्यतान् क्षुभितान् क्रुद्धोभक्षयिष्यामिवानरान् । |
| 6.4.66 | 6.4.68 | 0.438 | mahānādān pramuñcanti kṣveḍām anye pracakrire ūruvegaiś ca mamṛdur latājālāny anekaśaḥ | ऊरुवेगैश्च ममृदुर्लताजालान्यनेकशः । जृम्भमाणाश्च विक्रान्ता विचिक्रीडुश्शिलाद्रुमै ः ।।6.4.68।। |
| 6.21.19 | 6.21.18 | 0.44 | mahābhogāni matsyānām kariṇām ca karān iha \| saśaṅkhaśuktikājālam samīnamakaram tathā \|\| | महाभोगानिमत्स्यानांकरिणांचकराह । भोगिनांपश्यनागानांमयाछिन्नानिलक्ष्मण ।।6.21.18।। |
| 6.19.5 | 6.19.5 | 0.443 | bhavantam sarvabhūtānām śaraṇyam śaraṇam gataḥ \| parityaktā mayā laṅkā mitrāṇi ca dhanāni ca \|\| | परित्यक्तामयालङ्कमित्राणिचधनानिच । भवद्गतंहिमेराज्यंजीवितंचसुखानिच ।।6.19.5।। |
| 6.54.11 | 6.54.11 | 0.443 | vānarā rākṣasaiś cāpi nipētus tatra bhūtalē tatō vānarasainyēna hanyamānaṃ niśācaram \|\| | ततोवानरसैन्येनहन्यमानंनिशाचरम् ।।6.54.11।। प्राभज्यतबलंसर्वंवज्रदंष्ट्रस्यपश्यतः । |
| 6.8.21 | 6.8.21 | 0.444 | sugrīvam sahanūmantam sarvāṃś caivātra vānarān tato vajrahanur nāma rākṣasaḥ parvatopamaḥ | ततोवज्रहनुर्नामराक्षसःपर्वतोपमः ।।6.8.21।। क्रुद्ध: परिलिहन्सृक्कांजिह्वयावाक्यमब्रवीत् । |
| 6.111.84 | 6.114.84 | 0.444 | parigho vyavakīrṇas te bāṇaiś chinnaḥ sahasradhā \| priyām ivopasaṃgṛhya kim śeṣe raṇamedinīm | अप्रियामिवोपसंगृह्यकिंशेषेरणमेदिनीम् ।।6.114.84।। अप्रियामिवकस्माच्छमांनेच्छस्यभिभाषितुम् । |
| 6.55.14 | 6.55.14 | 0.446 | babhūva sumahān nādaḥ kṣōbhayann iva sāgaram tēna śabdēna vitrastā vānarāṇāṃ mahācamūḥ \|\| | तेनशब्देनवित्रस्तावानराणांमहाचमूः ।।6.55.14।। द्रुमशैलप्रहाराणांयोद्धुंसमुपतिष्ठतं । |
| 6.69.52 | 6.69.52 | 0.446 | cēluḥ pētuś ca nēduś ca tatra rākṣasapuṃgavāḥ rākṣasāś ca śarais tīkṣṇair bibhiduḥ kapikuñjarān ।। | राक्षसाश्चशरैस्तीक्ष्णैर्बिदुःकपिकुञ्जरान् ।।6.69.52।। शूलमुद्गरखडगैश्चजघ्नुःप्रासैश्चशक्तिभिः । |
| 6.111.56 | 6.114.56 | 0.447 | sthirāsmi yā deham imaṃ dhārayāmi hatapriyā \| śayaneṣu mahārheṣu śayitvā rākṣaseśvara | शयनेषुमहार्हेषुशयित्वाराक्षसेश्वर ।।6.114.56।। इहकर्मात्प्रसुप्तोऽसिधरण्यांरेणुगुण्ठितः । |
| 6.125.36 | 6.128.35 | 0.447 | uvāca prāñjalir vākayṃ hanūmān mārutātmajaḥ \| vasantaṃ daṇḍakāraṇye yaṃ tvaṃ cīrajaṭādharam | तम्धर्ममिवधर्मज्ञंदेहवन्तमिवापरम् ।।6.128.35।। उवाचप्राञ्जलिर्वाक्यंहनूमान्मारुतात्मजः । |
| 6.4.65 | 6.4.67 | 0.448 | bhujān vikṣipya śailāṃś ca drumān anye babhañjare ārohantaś ca śṛṅgāṇi girīṇām girigocarāḥ | आरोहन्तश्च शृङ्गाणि गिरीणां गिरिगोचराः । महानादान्प्रमुञ्चन्ति क्ष्वेळ्वामन्ये प्रचक्रिरे ।।6.4.67।। |
| 6.55.11 | 6.55.11 | 0.448 | vivarṇō mukhavarṇaś ca gadgadaś cābhavat svanaḥ abhavat sudinēkālē durdinaṃ rūkṣamārutam \|\| | अभवत्सुदिनेकालेदुर्दिनंरूक्षमारुतम् ।।6.55.11।। ऊचुःखगमृगाःसर्वेवाचःक्रूराभयावहाः । |
| 6.72.2 | 6.72.2 | 0.448 | dhūmrākṣaḥ paramāmarṣī sarvaśastrabhṛtāṃ varaḥ . akampanaḥ prahastaś ca kumbhukarṇas tathaiva ca ।। | धूम्राक्षःपरमामर्षीधन्वीशस्त्रभृतांवरः । अकम्पनःप्रहस्तश्चकुम्भुकर्णस्तथैव च ।।6.72.2।। एतेमहाबलावीराराक्षसायुद्धकाङ्क्ष |
| 6.111.53 | 6.114.53 | 0.448 | dharmavyavasthābhettāraṃ māyāsraṣṭāram āhave \| devāsuranṛkanyānām āhartāraṃ tatas tataḥ | देवासुरनृकन्यानामाहर्तारंततस्ततः ।।6.114.53।। शत्रुस्त्रीशोकदातारं नेतारं स्वजनस्य च । |
| 6.112.17 | 6.115.17 | 0.448 | praharṣam atulaṃ gatvā tuṣṭuvū rāmam eva hi \| tasyāmātyā jahṛṣire bhaktā ye cāsya rākṣasāḥ | तस्यामात्याजहृषिरेभक्तायेचास्यराक्षसाः ।।6.115.17।। दृष्टवाभिषिक्तंलङ्कायांराक्षसेन्द्रंविभीषणम् । |
| 6.126.30 | 6.129.30 | 0.448 | praviveśa tadā laṅkāṃ rāvaṇo rakṣaseśvaraḥ \| tāṃ suvarṇapariṣkāre śubhe mahati veśmani | तांसुवर्णपरिष्कारेशुभेमहतिवेश्मनि ।।6.129.30।। प्रवेश्यमैथिलींवाक्यैस्सान्त्वयामासरावणः । |
| 6.55.20 | 6.55.20 | 0.449 | samvṛtāni ca bhūtāni dadṛśur na raṇājirē na dhvajō na patākā vā carma vā turagō ‘pi vā \|\| | नध्वजोनपताकावाचर्मवातुरगोऽपिवा ।।6.55.20।। आयुधंस्यन्दनोवापिददृशेतेनरेणुना । |
| 6.89.35 | 6.90.35 | 0.449 | diśaś ca pradiśaś caiva babhūvuḥ śarasaṃkulāḥ tamasā pihitaṃ sarvam āsīt pratibhayaṃ mahat R_6,077. | तैःपतभदिश्चबहुभिस्तयोःशरशतैःशितैः । दिशश्चप्रदिशश्चैवबभूवुःशरसङ्कुलाः ।।6.90.35।। |
| 6.22.74 | 6.22.77 | 0.45 | dadṛśuḥ sarvabhūtāni sāgare setubandhanam \| tāni koṭisahasrāṇi vānarāṇām mahaujasām \|\| | तानिकोटिसहस्राणिवानराणांमहौजसाम् । बध्नन्तस्सागरेसेतुंजुग्मुःपारंमहोदधेः ।।6.22.77।। |
| 6.41.43 | 6.41.42 | 0.45 | nipīḍyōpaniviṣṭāś ca sugrīvō yatra vānaraḥ śāsanēna tu rāmasya lakṣmaṇaḥ savibhīṣaṇaḥ . \|\| | वानराणांतुषटित्रंशत्कोट्यःप्रख्यातयूथपाः । निपीड्योपनिविष्टाश्चसुग्रीवोयत्रवानरः ।।6.41.42।। |
| 6.53.31 | 6.53.32 | 0.45 | rudhiraugheṇa saṃchannā bhūmir bhayakarī tadā hārakēyūravastraiś ca chatraiś ca samalaṅkṛtā \|\| | हारकेयूरवस्स्रैश्चशत्रैश्चसमलङ्कृता । भूमिर्भातिरणेतत्रशारदीवयथानिशा ।।6.53.32।। |
| 6.107.44 | 6.110.15 | 0.45 | gadāmusalavarṣeṇa rāmaṃ pratyardayad raṇe \| tatprayuktaṃ punaryuddhaṃ tumulaṃ romaharṣaṇam | रावणोऽपिततःक्रुद्धोरथस्थराक्षसेश्वरः ।।6.110.15।। गदामुसलवर्षेणरामंप्रत्यर्दयद्रणे । |
| 6.117.24 | 6.120.25 | 0.45 | devā romāṇi gātreṣu brahmaṇā nirmitāḥ prabho \| nimeṣas te smṛtā rātrir unmeṣo divasas tathā | निमेषस्तेस्मृतारात्रिरुन्मेषोदिवसस्तथा ।।6.120.25।। संस्कारास्त्वभवन्वेदानैतदस्तित्वयाविना । |
| 6.123.39 | 6.126.39 | 0.45 | ṛśyamūko girivaraḥ kāñcanair dhātubhir vṛtaḥ \| atrāhaṃ vānarendreṇa sugrīveṇa samāgataḥ | त्राहंवानरेन्द्रेणसुग्रीवेणसमागतः ।।6.126.39।। समयश्चकृतःसीतेवधार्थंवालिनोमया । |
| 6.125.37 | 6.128.37 | 0.45 | anuśocasi kākutstha sa tvāṃ kauśalam abravīt \| priyam ākhyāmi te deva śokaṃ tyaja sudāruṇam | प्रियमाख्यामितेदेवशोकंत्यजसुदारुणम् ।।6.128.37।। अस्मिन्मुहूर्तेभ्रात्रात्वंरामेणसहसङ्गतः । |
| 6.127.24 | 6.130.24 | 0.45 | kaccin cānudṛṣyante kapayaḥ kāmarūpiṇaḥ athaivam ukte vacane hanūmān idam abravīt | अथैवमुक्तेवचनेहनूमानिदमब्रवीत् । अर्थ्यंविज्ञापयन्नेवभरतंसत्यविक्रमम् ।।6.130.24।। |
| 6.44.9 | 6.44.9 | 0.451 | cakarṣuś ca dadaṃśuś ca daśanaiḥ krōdhamūrchitāḥ . lakṣmaṇaś cāpi rāmaś ca śarair āśīviṣōpamaiḥ \|\| | लक्ष्मणश्चापिरामश्चशरैराशीविषोपमैः ।।6.44.9।। दृश्यादृश्यानिरक्षांसिप्रवराणिनिजघ्नतुः । |
| 6.62.11 | 6.62.11 | 0.451 | saṃraktanayanaḥ krōdhād rāvaṇaṃ vākyam abravīt kimartham aham ādṛtya tvayā rājan vibōdhitaḥ ।। | किमर्थमहमादृत्यत्वयाराजन्विबोधितः ।।6.62.11।। शंसकस्माद्भयंतेऽत्रकोऽद्यप्रेतोभविष्यति । |
| 6.75.61 | 6.75.62 | 0.451 | rākṣasānāṃ balaṃ śrēṣṭhaṃ bhūyaḥ param aśōbhata tatrōnmattā ivōtpētur harayō ‘tha yuyutsavaḥ ।। | तत्रोन्मत्ताइवोत्पेतुर्हरयोऽथयुयुत्सवः ।।6.75.62।। तरुशैलैरभिघ्नन्तोमुष्टिभिश्चनिशाचरान् । |
| 6.89.27 | 6.90.27 | 0.451 | lakṣmaṇaṃ paravīraghnaḥ punar evābhyadhāvata tau prayuddhau tadā vīrau mṛdhe lakṣmaṇarākṣasau R_6,077. | स दत्त्वातुमुलंयुद्धंपितृव्यस्येन्द्रजत् बली । लक्ष्मणंपरवीरघ्नःपुनरेवाभ्यधावत ।।6.90.27।। |
| 6.117.22 | 6.120.23 | 0.451 | tvaṃ dhārayasi bhūtāni pṛthivīṃ sarvaparvatān \| ante pṛthivyāḥ salile dṛśyase tvaṃ mahoragaḥ | अन्तेपृथिव्याःसलिलेदृश्यसेत्वंमहोरगः ।।6.120.23।। त्रीन्लोकान्धारयन् राम देवगन्धर्वदानवान् । |
| 6.127.21 | 6.130.21 | 0.451 | śaṅkhadundubhinādena saṃcacāleva medinī \| gajānāṃ bṛhitaiś cāpi śaṅkhadundubhiniḥsvanaiḥ | अश्वानांखुरशब्दैश्चरथनेमिस्वनेन च । शङ्खदुन्दुभिनादेनसञ्चचालेवमेदिनी ।।6.130.21।। |

## Minor edits (sim 0.6–0.9) — 1270 pairs, sample of 60

| Leonov locus | Gita Supersite locus | sim | Leonov text | Gita Supersite text |
|---|---|---:|---|---|
| 6.107.53 | 6.110.25 | 0.6 | tataḥ krodhān mahābāhū raghūṇāṃ kīrtivardhanaḥ \| saṃdhāya dhanuṣā rāmaḥ śaram āśīviṣopamam | ततःक्रोधान्महाबासूरघूणांकीर्तिवर्धनः । सन्धायधनुषारामश्शरमाशीविषोपमम् ।।6.110.25।। रावणस्यशिरोऽच्छिन्दच्छ्रीमज्ज्वलितकुण |
| 6.28.12 | 6.28.12 | 0.604 | udyantam bhāskaram dṛṣṭvā bālaḥ kila bubhukṣitaḥ \| triyojanasahasram tu adhvānam avatīrya hi \|\| | उद्यन्तभास्करंदृष्टवाबालःकिलपिपासितः । त्रियोजनसहस्रंतुअध्वानमवतीर्यहि ।।6.28.12।। आदित्यमाहरिष्यामिनमेक्षुत्प्रतियास्यत |
| 6.40.14 | 6.40.14 | 0.605 | parasparaṃ svedavidigdhagātrau \| parasparam śoṇitaraktadehau \| parasparaṃ śliṣṭaniruddhaceṣṭau \| parasparaṃ śālmaliki | परस्परंस्वेदविदग्धगात्रौपरस्परंशोणितदिग्धदेहौ । परस्परंलशिष्टनिरुद्धचेष्टौपरस्परंशाल्मलिकिंशुकौयधा ।।6.40.14।। मुष्टिप्र |
| 6.78.14 | 6.78.14 | 0.605 | tē kāmarūpiṇaḥ krūrā daṃṣṭriṇaḥ piṅgalēkṣaṇāḥ . mātaṅgā iva nardantō dhvastakēśā bhayāvahāḥ ।। | तेकामरूपिणस्सरेदंष्ट्रिणःपिङ्गलेक्षणा । मातङ्गाइवनर्दन्तोध्वस्तकेशाभयावहाः ।।6.78.14।। परिवार्यमहाकायामहाकायंखरात्मजम् । |
| 6.27.33 | 6.27.32 | 0.606 | śatam śatasahasrāṇi dṛṣṭvā vai setubandhanam \| golāngūlam mahāraja gavākṣam nāma yūthapam \|\| | एतेऽसितमुखाघोरागोलाङ्गूलामहाबलाः । शतंशतहस्राणिदृष्ट्वावैसेतुबन्धनम् ।।6.27.32।। गोलाङ्गूलंमहावेगंगवाक्षंनामयूधपम् । परि |
| 6.44.38 | 6.44.38 | 0.606 | tau tēna puruṣavyāghrau kruddhēnāśīviṣaiḥ śaraiḥ \|\| | तेनतौपुरुषव्याघ्रौक्रुद्धेनाशीविषैश्शरैः ।।6.44.38।। सहसानिहतौवीरौतदाप्रैक्षन्तवानराः । |
| 6.76.55 | 6.76.55 | 0.606 | sa cichēda śitair bāṇaiḥ saptabhiḥ kāyabhēdanaiḥ ।। | सबिभेदशितैर्बाणैस्सप्तभिःकायभेदनैः ।।6.76.55।। अङ्गदोविव्यधेऽभीक्षणंससादचमुमोह च । |
| 6.111.17 | 6.114.19 | 0.606 | kharas tava hato bhrātā tadā rāmo na mānuṣaḥ \| yadaiva nagarīṃ laṅkāṃ duṣpraveṣāṃ surairapi | यदैवहिजनस्थानेराक्षसैर्भहुभिर्वृतः । खरस्तुनिहतोभ्रातातदारामो न मानुषः ।।6.114.19।। यदैवनगरींलङ्कांदुष्प्रवेशांसुरैरपि । |
| 6.121.19 | 6.124.19 | 0.606 | māṃ nivartayituṃ yo ‘sau citrakūṭam upāgataḥ \| śirasā yācato yasya vacanam na kṛtaṃ mayā | मांनिवर्तयितुंयोऽसौचित्रकूटमुपागतः । शिरसायाचतोयस्यवचनं न कृतंमया ।।6.124.19।। कौसल्यां च सुमित्रां च कैकेयीं च यशस्विनी |
| 6.72.7 | 6.72.6 | 0.607 | mōktuṃ tad bandhanaṃ ghōraṃ yakṣagandharvapannagaiḥ . tan na jānē prabhāvair vā māyayā mōhanēna vā ।। | यन्नशक्यंसुरैस्सर्वैरसुरैर्वामहाबलैः ।।6.72.6।। मोक्तुंतद्बन्धनंघोरंयक्षगन्धर्वकिन्नरैः । तन्नजानेप्रभावैर्वामाययामोहनेन |
| 6.27.2 | 6.27.2 | 0.608 | snigdhā yasya bahuvyāmā dīrghalāngūlam āśritāḥ \| tāmrāḥ pītāḥ sitāḥ śvetāḥ prakīrṇā ghorakarmaṇaḥ \|\| | स्निग्धायस्यबहुव्यामावालालाङ्गूलमाश्रिताः । ताम्राःपीतास्सिताश्श्वेताःप्रकीर्णाघोरकर्मणः ।।6.27.2।। प्रगृहीताःप्रकाशन्ते |
| 6.41.4 | 6.41.4 | 0.608 | idānīṃ mā kṛthā vīra ēvaṃvidham ariṃdama tvayi kiṃcit samāpanne kiṃ kāryaṃ sītayā mama \|\| | इदानींमाकृथावीर एवंविधमचिन्तितम् । त्वयिकिञ्चित्समापन्नेकिंकार्यंसीतयामम ।।6.41.4।। भरतेनमहाबाहो लक्ष्मणेनयवीयसा । शत्रु |
| 6.57.18 | 6.57.18 | 0.608 | samanayata mē śīghraṃ rākṣasānāṃ mahād balam madbāṇānāṃ tu vēgēna hatānāṃ tu raṇājirē \|\| | मेशीघ्रंराक्षसानांमहाद्बलम् ।।6.57.18।। मद्भाणाब्दावेगेनहतानांशनिचरणाजिरे । अद्यहृष्यन्तुमांसादाःपक्षिणःकाननौकसां ।।6.57 |
| 6.95.49 | 6.96.39 | 0.608 | teṣāṃ tu rathaghoṣeṇa rākṣasānāṃ mahātmanām vānarāṇām api camūr yuddhāyaivābhyavartata [teṣāṃ tu tumulaṃ yuddhaṃ babhūva | तेषांतुरथघोषेणराक्षसानांमहात्मनाम् । वानराणामपिचमूर्युद्धायैवाभ्यवर्तत ।।6.96.39।। |
| 6.110.12 | 6.113.12 | 0.608 | yena vitrāsitaḥ śakro yena vitrāsito yamaḥ \| yena vaiśravaṇo rājā puṣpakeṇa viyojitaḥ | येनमित्रासितःशक्रोयेनवित्रासितोयमः । येनवैश्रवणोराजापुष्पकेणवियोजितः ।।6.113.12।। गन्धर्वाणामृषीणां च सुराणां च महात्मना |
| 6.111.113 | 6.114.112 | 0.608 | citāṃ candanakāṣṭhaiś ca padmakośīracandanaiḥ \| brāhmyā saṃvartayāmāsū rāṅkavāstaraṇāvṛtām | रावणंप्रयतेदेशेस्थाप्यतेभृशदुःखिताः ।।6.114.112।। चितांचन्दनकाष्ठैश्चपद्मकोशीसंवृताम् । ब्राह्म्यासम्वर्तयामासूराङ्कवास् |
| 6.128.82 | 6.131.81 | 0.608 | tejo dhṛtir yaśo dākṣyaṃ sāmarthyaṃ vinayo nayaḥ \| pauruṣaṃ vikramo buddhir yasminn etāni nityadā | तामिङ्गितज्ञस्सम्प्रेक्ष्य बभाषे जनकात्मजाम् । प्रदेहिसुभगेहारंयस्यतुष्टासिभामिनि ।।6.131.81।। तेजोधृतिर्यशोदाक्ष्यंसामर |
| 6.45.2 | 6.45.2 | 0.609 | dvau suṣēṇasya dāyādau nīlaṃ ca plavagādhipam aṅgadaṃ vāliputraṃ ca śarabhaṃ ca tarasvinam \|\| | द्वौसुषेणस्यदायादौनीलंचप्लवगर्षपम् । अङ्गदंवालिपुत्रंचशरभंचतरस्विनम् ।।6.45.2।। विनतंजाम्बवन्तंचसानुप्रस्थंमहाबलम् । ऋषभ |
| 6.64.30 | 6.64.30 | 0.609 | tatō ‘smin bahulībhūtē kaulīnē sarvatō gatē . bhakṣitaḥ sasuhṛd rāmō rākṣasair iti viśrutē ।। | ततोऽस्मिन् बहुलीभूतेकौलीनेसर्वतोगते । भक्षितस्ससुहृद्रामोराक्षसैरितिविश्रुते ।।6.64.30।। प्रविश्याश्वास्यचापित्वंसीतांरह |
| 6.51.3 | 6.51.3 | 0.61 | yathāsau samprahṛṣṭānāṃ vānarāṇām upasthitaḥ bahūnāṃ sumahān nādō mēghanām iva garjitām \|\| | यथाऽसौसम्प्रहृष्टानांवानराणांसमुत्थितः । बहूनांसुमहान्नादोमेघनामिवगर्जिताम् ।।6.51.3।। व्यक्तंसुमहतीप्रीतिरेतेषांनात्रसं |
| 6.123.8 | 6.126.8 | 0.61 | aṅgadenātra nihato vikaṭo nāma rākṣasaḥ \| virūpākṣaśca duṣprekṣo mahāpārśvamahodarau | अङ्गदेनात्रनिहतोविकटोनामराक्षसः । विरूपाक्षश्चदुर्धर्षोमहापार्श्वमहोदरौ ।।6.126.8।। अकम्पनश्चनिहतोबलिनोऽऽन्ये च राक्षसाः |
| 6.53.4 | 6.53.4 | 0.611 | tathēty uktvā drutataraṃ māyāvī rākṣasēśvaraḥ nirjagāma balaiḥ sārdaṃ bahubhiḥ parivāritaḥ \|\| | तथेत्युक्त्वाद्रुततरंमायावीराक्षसेश्वरम् । निर्जगामबलैस्सार्दंबहुभिःपरिवारितः ।।6.53.4।। नागैरश्वैःखरैरुष्ट्रैःसंयुक्तस् |
| 6.35.33 | 6.35.34 | 0.612 | pakṣiṇaśca mṛgāḥ sarve pratyādityam rudanti te \| karālo vikalo muṇḍaḥ puruṣaḥ kṛṣṇapingalaḥ \|\| | पक्षिणश्चमृगास्सर्वेप्रत्यादित्यंरुदन्तिच । कराळोविकटोमुण्डःपुरुषःकष्णपिङ्गळः ।।6.35.34।। कालोगृहाणिसर्वेषांकालेकालेऽन्व |
| 6.38.1 | 6.38.1 | 0.612 | sa tu kṛtvā suvelasya matim ārohaṇam prati \| lakṣmaṇānugato rāmah sugrīvam idam abravīt \|\| | सतुकृत्वासुवेलस्यमतिमारोहणंप्रति । लक्ष्मणानुगतोरामःसुग्रीवमिदमब्रवीत् ।।6.38.1।। विभीषणंचधर्मज्ञमनुरक्तंनिशाचरम् । मन्त |
| 6.96.35 | 6.97.35 | 0.612 | tathā tu tau saṃyati saṃprayuktau tarasvinau vānararākṣasānām balārṇavau sasvanatuś ca bhīmau mahārṇavau dvāv iva bhinna | तथातुतौसंम्यतिसम्प्रयुक्तौ । तरस्विनौवानरराक्षसानाम् ।।6.97.35।। |
| 6.68.24 |  | 0.613 | iti bahuvidham ākulāntarātmā kṛpaṇam atīva vilapya kumbhakarṇam . nyapad api daśānanō bhṛśārtas tam anujam indraripuṃ ha | ﻿इतिबहुविधमाकुलान्तरात्माकृपणमतीवविलप्यकुम्भकर्णम् । |
| 6.100.55 | 6.101.56 | 0.613 | adya paśyantu rāmasya rāmatvaṃ mama saṃyuge trayo lokāḥ sagandharvāḥ siddhagandharvacāraṇāḥ R_6,088. | अद्यरामस्यरामत्वंपश्यन्तुममसंयुगे । त्रयोलोकास्सगन्धर्वास्सदेवास्सर्षिचारणाः ।।6.101.56।। |
| 6.5.5 |  | 0.614 | na me duḥkhaṃ priyā dūre na me duḥkhaṃ hṛteti ca etad evānuśocāmi vayo 'syā hy ativartate | ﻿नमेदुःखंप्रियादूरेनमेदुःखंहृतेतिवा । |
| 6.81.12 | 6.81.12 | 0.614 | abravīt tāṃ tu śokārtāṃ nirānandāṃ tapasvinām dṛṣṭvā rathastitāṃ dīnāṃ rākṣasendrasutāśritām R_6,068. | अब्रवीत्तांतुशोकार्तांनिरानन्दांतपस्विनीम् । दृष्टवारथोस्थितांदृष्ट्वाराक्षसेन्द्रसुतश्रिताम् ।।6.81.12।। कंसमर्थितमस्ये |
| 6.98.8 | 6.99.8 | 0.614 | tasya rkṣarājas tejasvī nīlāñjanacayopamaḥ niṣpatya sumahāvīryaḥ svayūthān meghasaṃnibhāt R_6,086. | स ऋक्षराजस्तेजस्वीनीलाञ्जनचयोपमः ।।6.99.8।। निष्पत्यसुमहावीर्यस्स्वाद्व्यूहन्मेघसन्निभात् । प्रगृह्यगिरिशृङ्गाभांक्रुद्ध |
| 6.27.8 | 6.27.8 | 0.615 | eṣām madhye sthito rājā bhīmākṣo bhīmadarśanaḥ \| parjanya iva jīmūtaiḥ samantāt parivāritaḥ \|\| | एषांमध्येस्थितोराजन्भीमाक्षोभीमदर्शनः । पर्जन्यइवजीमूतैस्समन्तात्परिवारितः ।।6.27.8।। ऋक्षवन्तंगिरिश्रेष्ठमध्यास्तेनर्मद |
| 6.38.4 | 6.38.4 | 0.615 | lankām cālokayiṣyāmo nilayam tasya rakṣasah \| yena me maraṇāntāya hṛtā bhāryā durātmanā \|\| | लङ्कांचालोकयिष्यामोनिलयंतस्यरक्षसः । येनमेमरणान्तायहृताभार्यादुरात्मना ।।6.38.4।। येनधर्मोनविज्ञातोनतद्वृत्तंनकुलंतथा ।  |
| 6.65.31 | 6.65.31 | 0.615 | sarvābharaṇasarvāṅgaḥ śūlapāṇiḥ sa rākṣasaḥ . trivikramakṛtōtsāhō nārāyaṇa ivābabhau ।। | सर्वाभरणसर्वाङ्गश्शूलपाणिस्सराक्षसः । त्रिविक्रमकृतोत्साहोनारायणइवाबभौ ।।6.65.31।। भ्रातरंसम्परिष्वज्यकृत्वाचापिप्रदक्षि |
| 6.92.18 | 6.93.18 | 0.616 | [lalāte bhrūkuṭībhiś ca saṃgatabhir vyarocata yugānte saha nakrais tu mahormibhir ivodadhiḥ] kopad vijṛbhamāṇasya vakrād | ललाटेभ्रुकुटीभिश्चसङ्गताभिर्व्यरोचत ।।6.93.18।। युगान्तेसहनक्रैस्तुमहोर्मिभिरिवोदधिः । |
| 6.47.18 | 6.47.19 | 0.617 | tataḥ sītā dadarśōbhau śayānau śaratalpagau . lakṣmaṇaṃ cāpi rāmaṃ ca visaṃjñau śarapīḍitau \|\| | ततस्सीताददर्शोभौशयानौशरतल्पगौ । लक्ष्मणंचापिरामंचविसंज्ञौशरपीडितौ ।।6.47.19।। विध्वस्तकवचौवीरौविप्रविद्धशरासनौ । सायकैचश |
| 6.51.8 | 6.51.8 | 0.617 | tathōktās tē susambhrāntāḥ prākāram adhiruhya ca . dadṛśuḥ pālitāṃ sēnāṃ sugrīvēṇa mahātmanā \|\| | तथोक्तास्तेनसम्भ्रान्ताःप्राकारमधिरुह्यच । ददृशुःपालितांसेनांसुग्रीवेणमहात्मना ।।6.51.8।। तौचमुक्तौसुघोरेणशरबन्धेनराघवौ  |
| 6.36.17 | 6.36.17 | 0.618 | vyādideśa ca pūrvasyām prahastam dvāri rākṣasam \| dakṣiṇasyām mahāvīryau mahāpārśvamahodarau \|\| | व्यादिदेशसपूर्वस्यांप्रहस्तंद्वारिराक्षसम् । दक्षिणस्यांमहावीर्यौमहापार्श्वमहादरौ ।।6.36.17।। पश्चिमायामथोद्वारिपुत्रमिन |
| 6.37.34 | 6.37.34 | 0.618 | vānarā eva viścihnam svajane asmin bhaviṣyati \| vayam tu mānuṣeṇaiva sapta yotsyāmahe parān \|\| | वानराएवनश्चिह्नंस्वजनेऽस्मिन् भविष्यति ।।6.37.34।। वयंतुमानुषेणैवसप्तयोत्प्यामहेपरान् । अहमेषममभ्रात्रालक्ष्मणेनमहौजसौ । |
| 6.65.40 | 6.65.40 | 0.618 | athānyad vapur ādāya dāruṇaṃ rōmaharṣaṇam . niṣpapāta mahātējāḥ kumbhakarṇō mahābalaḥ ।। | अथान्यद्वपुरादायदारुणंरोमहर्षणम् । निष्पपातमहातेजाःकुम्भकर्णोमहाबलः ।।6.65.40।। धनुःशतपरीणाहः स षट्छत्रसमुच्छ्रितः । रौद |
| 6.89.1 | 6.90.1 | 0.618 | yudhyamānau tato dṛṣṭvā prasaktau nararākṣasau prabhinnāv iva mātaṃgau parasparajayaiṣiṇau R_6,077. | युध्यमानौतुतौदृष्टवाप्रसक्तौनरराक्षसौ । प्रभिन्नाविवमातङ्गौपरस्परवधैषिणौ ।।6.90.1।। तौद्रष्टुकामस्सङ्ग्रामेपरस्परगतौबली  |
| 6.92.46 | 6.93.50 | 0.618 | bahuśaś codayām āsa bhartāraṃ mām anuvratām bhāryā mama bhavasveti pratyākhyāto dhruvaṃ mayā R_6,080. | बहुशश्चोदयामासभर्तारंमामनुव्रताम् । भार्याभवरमस्वेतिप्रत्याख्यातोध्रुवंमया ।।6.93.50।। सोऽयंमामनुपस्थानेव्यक्तंनैराश्यमा |
| 6.96.13 | 6.97.13 | 0.618 | atha saṃkṣīyamāṇeṣu rākṣaseṣu samantataḥ sugrīveṇa prabhagneṣu nadatsu ca patatsu ca R_6,084. | अथसंक्षीयमाणेषुराक्षसेषुसमन्ततः । सुग्रीवेणप्रभग्नेषुपतत्सुनिनदत्सु च ।।6.97.13।। विरूपाक्षस्स्वकंनामधन्वीविश्राव्यराक्ष |
| 6.102.43 | 6.104.5 | 0.618 | vimānasthās tadā devā gandharvāś ca mahoragāḥ ṛṣidānavadaityāś ca garutmantaś ca khecarāḥ R_6,091. | विमानस्थास्तदादेवागन्धर्वाश्चमहोरगाः । ऋषिदावनदैत्याश्चगरुत्मन्तश्चखेचराः ।।6.104.5।। ददृशुस्तेतदायुद्धंलोकसम्वर्तसंस्थि |
| 6.111.83 | 6.114.82 | 0.619 | vajraṃ vajradharasyeva so ‘yaṃ te satatārcitaḥ \| raṇe bahupraharaṇo hemajālapariṣkṛtaḥ | येनसूदयसेशत्रून् समरेसूर्यवर्चसा ।।6.114.82।। वज्रंवज्रधरस्येवसोऽयंतेसततार्चितः । रणेबहुप्रहरणोहेमजापरिष्कृतः ।।6.114.83 |
| 6.115.15 | 6.118.15 | 0.619 | viditaś cāstu bhadraṃ te yo ‘yaṃ raṇapariśramaḥ \| sutīrṇaḥ suhṛdāṃ vīryān na tvadarthaṃ mayā kṛtaḥ | विदितश्चास्तुभत्रंतेयोऽयंरणपरिश्रमः । सुतीर्णःसुहृदांवीर्यान्नत्वदर्थंमयाकृतः ।।6.118.15।। रक्षतातुमयावृत्तपमवादं च सर्व |
| 6.3.4 | 6.3.4 | 0.62 | balasya parimāṇaṃ ca dvāradurgakriyām api guptikarma ca laṅkāyā rakṣasāṃ sadanāni ca | बलस्यपरिमाणंचद्वारदुर्गक्रियामपि । गुप्तिकर्मचलङ्कायारक्षसांसदनानिच ।।6.3.4।। यथासुखंयथावच्छलङ्कायामसिदृष्टवान् । सर्वमा |
| 6.128.43 | 6.131.43 | 0.62 | athābravīd rājaputro bharataṃ dharmiṇāṃ varam \| arthopahitayā vācā madhuraṃ raghunandanaḥ | अथाब्रवीद्राजपुत्रोभरतंधर्मिणांवरम् ।।6.131.43।। अर्धोपहितयावाचामधुरंरघुनन्दनः । पितुर्भवनमासाद्यप्रविश्य च महात्मनः ।।6 |
| 6.27.10 | 6.27.10 | 0.621 | yavīyān asya tu bhrātā paśyainam parvatopamam bhrātrā samāno rūpeṇa viśiṣṭaś ca parākrame \|\| | यवीयानस्यतुभ्रातापश्यैनंपर्वतोपमम् । भ्रात्रासमानोरूपेणविशिष्टस्तुपराक्रमैः ।।6.27.10।। सएषजाम्बवान्नाममहायूथपयूथपः । प् |
| 6.27.31 | 6.27.30 | 0.622 | anīkamapi saṃrabdham vānarāṇām tarasvinām \| uddhūtam aruṇābhāsam pavanena samantataḥ \|\| | वातेनेवोद्धतंमेघंयमेनमनुपश्यसि । अनीकमभिसंरब्धंवानराणांतरस्विनाम् ।।6.27.30।। उद्दूतमरुणाभासंपवनेनसमन्ततः । विवर्तमानंबह |
| 6.76.80 | 6.76.82 | 0.622 | tataḥ kumbhas tu sugrīvaṃ bāhubhyāṃ jagṛhē tadā . gajāv ivāvītamadau niḥśvasantau muhur muhuḥ ।।76. | ततःकुम्भस्तुसुग्रीवंबाहुभ्यांजगृहेतदा । गजाविवाहितमदौनिश्श्वसन्तौमुहुर्मुहु 76.81।। अन्योन्यगात्रग्रथितौकर्षन्तावितरेतरम |
| 6.107.21 | 6.109.21 | 0.622 | mumoca ca daśagrīvo niḥsaṅgenāntarātmanā \| vyāyacchamānaṃ taṃ dṛṣṭvā tatparaṃ rāvaṇaṃ raṇe | मुमोच ह दशग्रीवोनिःसङ्गेनान्तरात्मना ।।6.109.21।। व्यायच्छमानंतंदृष्टवासत्वरमरावणंरणे । प्रहसन्निवकाकुत्स्थसन्दधेनिशितान |
| 6.111.65 | 6.114.64 | 0.622 | pativratā dharmaratā guruśuśrūṣaṇe ratāḥ \| tābhiḥ śokābhitaptābhiḥ śaptaḥ paravaśaṃ gataḥ | याःस्त्वयाविधवाराजन्कृतानैकाःकुलस्त्रियः ।।6.114.64।। पतिव्रताधर्मरतागुरुशुश्रूषणेरताः । ताभिश्शोकाभितप्ताभिश्शप्तःपरवशं |
| 6.128.28 | 6.131.28 | 0.622 | jagrāha bharato raśmīñ śatrughnaś chatram ādade \| lakṣmaṇo vyajanaṃ tasya mūrdhni saṃvījayaṃs tadā | जग्राहभरतोरमशीन्शत्रुघ्नश्चत्रमाददे । लक्ष्मणोव्यजनंतस्यमूर्ध्निसम्पर्यवीजयत् ।।6.131.28।। श्वेतं च वालव्यजनंजगृहेपरितस् |
| 6.71.34 | 6.71.34 | 0.623 | vajraṃ viṣṭambhitaṃ yēna bāṇair indrasya dhīmatā . pāśaḥ salilarājasya yuddhe pratihatas tathā ।। | वज्रंविष्टम्भितंयेनबाणैरिन्द्रस्यधीमतः । पाशस्सलिलराजस्यरणेप्रतिहतस्तथा ।।6.71.34।। एषोऽतिकायोबलवान्राक्षसानामथर्षभः । र |
| 6.105.29 | 6.107.29 | 0.623 | ādityaṃ prekṣya japtvedaṃ paraṃ harṣam avāptavān \| trirācamya śucirbhūtvā dhanurādāya vīryavān | आदित्यंप्रेक्ष्यजप्त्वातुपरंहर्षमवाप्तवान् । त्रिराचम्यशुचिर्भूत्वाधनुरादायवीर्यवान् ।।6.107.29।। रावणंप्रेक्ष्यहृष्टात् |
| 6.67.2 | 6.67.2 | 0.624 | samudīritavīryās tē samārōpitavikramāḥ . paryavasthāpitā vākyair aṅgadēna balīyasā ।। | समुदीरितवीर्यास्तेसमारोपितविक्रमाः । पर्यवस्थापितावाक्यैरङ्गदेनवलीमुखाः ।।6.67.2।। प्रयाताश्चगताहर्षंमरणेकृतश्चयाः । चक् |
| 6.76.32 | 6.76.32 | 0.624 | etasminn antarē maindō vīrō dvividābhyāśam āgataḥ yūpākṣaṃ tāḍayāmāsa talēnōrasi vīryavān tau śōṇitākṣyūpākṣau plavaṅgāb | तौशोणिताक्ष्यूपाक्षौप्लवङ्गाभ्यांतरस्विनौ । चक्रतुस्समरेतीव्रमाकर्षोत्पाटनंभृशम् ।।6.76.32।। |
| 6.128.62 | 6.131.62 | 0.624 | ṛtvigbhir brāhmaṇaiḥ pūrvaṃ kanyābhir mantribhis tathā \| yodhaiś caivābhyaṣiñcaṃs te samprahṛṣṭāḥ sanaigamaiḥ | ऋग्भिर्भ्राह्मणैःपूर्वंकन्याभिर्मन्त्रिभिस्तथा ।।6.131.62।। योथौश्चैवाभ्यषिञ्चंस्तेसम्प्रहृष्टास्सनैगमैः । सर्वौषधीनसैश् |
| 6.3.8 | 6.3.8 | 0.625 | rākṣasāśca yathā snigdhā rāvaṇasya ca tejasā parām samṛddhim laṅkāyāḥ sāgarasya ca bhīmatām | राक्षसाश्चयथास्निग्धारावणस्यचतेजसा । परांसमृद्धिंलङ्कायास्सागरस्यचभीमताम् ।।6.3.8।। विभागंचबलौघस्यनिर्देशंवाहनस्यच । एवम |
| 6.53.1 | 6.53.1 | 0.625 | dhūmrākṣaṃ nihataṃ śrutvā rāvaṇō rākṣasēśvaraḥ . krōdhēna mahatāviṣṭō niḥśvasann uragō yathā \|\| | धूम्राक्षंनिहतंश्रुत्वारावणोराक्षसेश्वरः । क्रोधेनमहताऽविष्टोनिश्श्वसन्नुरगोयथा ।।6.53.1।। दीर्घमुष्णंविनिश्श्वस्यक्रोधे |

## Leonov-only — 693, sample of 30

| Locus | Text |
|---|---|
| 6.2.14 | yat tu kāryaṃ manuṣyeṇa śauṭīryam avalambyatāṃ tad alaṃkaraṇāyaiva kartur bhavati satvaram |
| 6.3.5 | yathāsukhaṃ yathāvac ca laṅkāyām asi dṛṣṭavān sarvam ācakṣva tattvena sarvathā kuśalo hy asi |
| 6.3.9 | vibhāgaṃ ca balaughasya nirdeśaṃ vāhanasya ca evamuktvā kapiśreṣṭhaḥ kathayāmāsa tattvavit |
| 6.3.32 | plavamānā hi gatvā tāṃ rāvaṇasya mahāpurīm saparvatavanāṃ bhitvā sakhātāṃ ca satoraṇām saprākārāṃ sabhavanām ānayiṣyanti rāghava |
| 6.4.38 | sarāṃsi ca suphullāni taṭākāni varāṇi ca rāmasya śāsanaṃ jñātvā bhīmakopasya bhītavat |
| 6.4.40 | niḥsasarpa mahāghoraṃ bhīmaghoṣam ivārṇavam tasya dāśaratheḥ pārśve śūrās te kapikuñjarāḥ |
| 6.4.42 | mahadbhyām iva saṃspṛṣṭau grāhābhyāṃ candrabhāskarau tato vānararājena lakṣmaṇena supūjitaḥ |
| 6.4.45 | samṛddhārthaḥ samṛddhārthām ayodhyāṃ pratiyāsyasi mahānti ca nimittāni divi bhūmau ca rāghava |
| 6.4.56 | ṛkṣavānaraśārdūlair nakhadaṃṣṭrāyudhair api karāgraiś caraṇāgraiś ca vānarair uddhataṃ rajaḥ |
| 6.4.58 | chādayantī yayau bhīmā dyām ivāmbudasaṃtati uttarantyāśca senāyāḥ satatam bahuyojanam |
| 6.4.64 | kecit kilakilāṃ cakrur vānarā vanagocarāḥ prāsphoṭayaṃś ca pucchāni samnijaghnuḥ padāny api |
| 6.4.67 | jṛmbhamāṇāś ca vikrāntā vicikrīḍuḥ śilādrumaiḥ tataḥ śatasahasraiś ca koṭibhiś ca sahasraśaḥ |
| 6.4.77 | sumahadvānarānīkam cādayāmāsa sarvataḥ giriprastheṣu ramyeṣu sarvataḥ samprapuṣpitāḥ |
| 6.4.78 | ketakyaḥ sinduvārāś ca vāsantyaśca manoramāḥ mādhavyo gandhapūrṇāś ca kundagulmāśca puṣpitāḥ |
| 6.4.79 | ciribilvā madhūkāśca vañjulā vakulās tathā rañjakās tilakāś caiva nāgavṛkṣaśca puṣpitāḥ |
| 6.4.80 | cūtāḥ pāṭalikāś caiva kovidārāś ca puṣpitāḥ muculindārjunāś caiva śiṃśapāḥ kuṭajās tathā |
| 6.4.81 | hintālās tiniśāś caiva cūrṇakā nīpakās tathā nīlāśokāś ca saralā aṅkolāḥ padmakās tathā |
| 6.4.82 | prīyamāṇaiḥ plavamgais tu sarve paryākulīkṛtāḥ vāpyas tasmin girau ramyāḥ palvalāni tathaiva ca |
| 6.4.83 | cakravākānucaritāḥ kāraṇḍavaniṣevitāḥ plavaiḥ krauñcaiś ca saṃkīrṇā varāhamṛgasevitāḥ |
| 6.4.84 | ṛkṣais tarakṣubhiḥ siṃhaiḥ śārdūlaiś ca bhayāvahaiḥ vyālaiś ca bahubhir bhīmaiḥ sevyamānāḥ samantataḥ |
| 6.4.85 | padmaiḥ saugandhikaiḥ phullaiḥ kusumais cotpalais tathā vārijair vividhaiḥ puṣpai ramyās tatra jalāśayāḥ |
| 6.4.88 | babhuñjur vānarās tatra pādapānāṃ madotkaṭāḥ droṇamātrapramāṇāni lambamānāni vānarāḥ |
| 6.4.120 | dadṛśus te mahātmāno vātāhatajalāśayam aniloddhūtam ākāśe pravalgatam ivormibhiḥ |
| 6.6.8 | sahito mantrayitvā yaḥ karmārambhān pravartayet daive ca kurute yatnaṃ tam āhuḥ puruṣottamam |
| 6.7.14 | mahājvareṇa durdharṣam yamalokamahārṇavam avagāhya tvayā rājan yamasya balasāgaram |
| 6.7.15 | jayaś ca viplulaḥ prāpto mṛtyuś ca pratiṣedhitaḥ suyuddhena ca te sarve lokās tatra sutoṣitāḥ |
| 6.7.21 | rudrādityamahāgrāhaṃ marudvasumahoragam rathāśvagajatoyaughaṃ padātipulinam mahat |
| 6.7.22 | anena hi samāsādya devānām balasāgaram gṛhīto daivatapatir laṅkām cāpi praveśitaḥ |
| 6.8.14 | kākutstham upasamgamya vivṛtaṃ mānuṣam vapuḥ sarve hy asambhramā bhūtvā bruvantu raghusattamam |
| 6.8.22 | kruddhaḥ parilihan sṛkkāṃ jihvayā vākyam abravīt svairaṃ kurvantu kāryāṇi bhavanto vigatajvarāḥ |

## Gita Supersite-only — 174, sample of 30

| Locus | Text |
|---|---|
| 6.2.15 | यत्तुकार्यंमनुष्येणशौण्डीर्यमवलम्बता । अस्मिन् कालेमहाप्राज्ञसत्त्वमातिष्ठतेजसा ।।6.2.15।। |
| 6.4.41 | तस्यदाशरथे: पार्श्वे शूरास्ते कपिकुङजराः । तोर्णमापुप्लुवु स्सर्वे सदश्वा इव चोदिताः ।।6.4.41।। |
| 6.4.44 | तमङ्गदगतो रामं लक्ष्मणश्शुभया गिरा । उवाच परिपूर्णार्थ: स्मृतिमान् प्रतिभानवान् ।।6.4.44।। |
| 6.4.66 | प्रास्पोटयंश्च पुच्छानि सन्निजग्मु: पदान्यपि । भुजावनिक्षिप्य शैलांश्च द्रुमानन्ये बभञ्जिरे ।।6.4.66।। |
| 6.4.79 | गिरिप्रस्थेषु रम्येषु सर्वत सम्प्र पुष्पिताः । केतकस्सिन्दुवाराश्च वासन्त्यश्च मनोरमाः ।।6.4.79।। माधव्यो गन्धपूर्णाश्च कुन्दगुल्माश्च पुष्पिताः । चिर |
| 6.4.85 | वाप्यस्तस्मिन् गिरौ शिता: पल्वलानि तथैव च । चक्रवाकानुचरिताः कारण्डवनिषेविताः ।।6.4.85।। प्लवैः क्रौञ्चेश्च सङ्कीर्णा वराहमृग सेविताः । ऋक्षैस्तरक्षुभ |
| 6.4.91 | द्रोणमात्रप्रमाणानि लम्बमानानि वानराः । ययुः पिबन्त हृष्टास्ते मधूनि मधुपिङ्गलाः ।।6.4.91।। |
| 6.7.3 | इत्युक्ताराक्षसेन्द्रेणराक्षसास्तेमहाबलाः । ऊचुःप्रान्जलयःसर्वेरावणंराक्षसेश्वरम् ।।6.7.3।। द्विषत्पक्षमविज्ञायनीतिबाह्यास्त्वबुद्धयः । |
| 6.7.4 | राजन्परिघशक्त्यृष्टिशूलपट्टिशकुन्तलम् ।।6.7.4।। |
| 6.9.1 | ततोनिकुम्भोरभसस्सूर्यशत्रुर्महाबलः । सुप्तघ्नोयज्ञहारक्षोमहापार्श्वमहोदरौ ।।6.9.1।। अग्निकेतुश्चदुर्धर्षोरश्मिकेतुश्चराक्षस: । इन्द्रजिच्चमहातेजाबलवान |
| 6.102.10 | परंविषादमापन्नोविललापाकुलेन्द्रियः । भ्रातरंनिहतंदृष्टवालक्ष्मणंरणपांसुषु ।।6.102.10।। |
| 6.102.16 | इत्येवंविलपन्तंतंशोकविह्वलितेद्रनियम् । विवेष्टमानंकरुणमच्छवसन्तंपुनःपुनः ।।6.102.16।। राममाश्वासयनवीरसुषेनोवाक्यमब्रवीत |
| 6.102.18 | न मृथोयंमहाबाहो लक्ष्मणोलक्षमिवर्धन: । न चास्यविक्रतंवक्त्रानापिशस्वासं न निष्प्रभं ।।6.102.18।। |
| 6.102.19 | सुप्रभंसुप्रसन्नं च मुखमस्यनिरीक्ष्यताम् ।।6.102.19।। पद्मपत्रतलौहस्तौसुप्रसन्ने च लोचने । |
| 6.102.20 | ऐ वं न विद्यतेरूपंगतासूनांविशम्पते ।।6.102.20।। माविषादंमृकृथावीरसप्राणोऽयमरिन्दम । |
| 6.103.10 | ततःकाञ्चनचित्राङ्गःकिङ्किणीशतभूषितः ।।6.103.10।। तरुणादित्यसङ्काशोवैदूर्यमयकूबरः । सदश्वैःकाञ्चनापीडैर्युक्तश्श्वेतप्रकीर्णकैः ।।6.103.11।। हरिभिःसूर् |
| 6.103.33 | प्राजात्यं च नक्षत्रंरोहिणींकशशिनःप्रियाम् ।।6.103.33।। समाक्रम्यबुधस्तस्थौप्रजानामशुभावहः । |
| 6.103.35 | शस्त्रवर्णस्सुपरुषोमन्दरश्मिद्दिवाकरः ।।6.103.35।। अदृश्यतकबन्धाङ्कःसंसक्तोधूमकेतुना । |
| 6.104.9 | एतस्मिन्नन्तरेक्रोधाद्राघवस्य स रावणः । प्रहर्तुकामोदुष्टात्मास्पृशन् प्रहरणंमहत् ।।6.104.9।। वज्रसारंमहानादंसर्वशत्रुनिबर्हणम् । शैलशृङ्गनिभैःकूटैश्च |
| 6.109.16 | तेषामसम्भ्रमंदृष्टवावाजिनांरावणस्तदा ।।6.109.16।। भूयएवसुसङ्क्रुद्धश्शरवर्षंमुमोच ह । |
| 6.109.29 | प्रयुध्यमानौसमरेमहाबलौ शितैःशरैरावणलक्ष्मणाग्रजौ । ध्वजावपातेन स राक्षसाधिपो भृशंप्रचुक्रोधतदारघूत्तमे ।।6.109.29।। |
| 6.11.12 | हेममञ्जरिगर्भेचशुद्धस्फटिकविग्रहे । चामरव्यजनेतस्यरेजतुस्सव्यदक्षिणे ।।6.11.12।। |
| 6.11.14 | राक्षसैस्त्सूयमानस्सञ्जयाशीर्भिररिन्दमः । आससादमहातेजास्सभांविरचितांतदा ।।6.11.14।। |
| 6.110.4 | अर्धयन्रावणंरामोराघवंचापिरावणः ।।6.110.4।। गतिवेगंसमापन्नौप्रतिवेगप्रवर्तने । |
| 6.110.9 | सक्रोधवशमापन्नोहयानामपसर्पणे ।।6.110.9।। मुमोचनिशितान्बाणान्राघवायदशाननः । |
| 6.110.11 | चिक्षेप च पुनर्भाणान्वज्रपातसमस्वनान् ।।6.110.11।। सारथिंवज्रहस्तस्यसमुद्दिश्यदशाननः । |
| 6.110.13 | तयाधर्षणयाक्रुद्धोमातलेर्नतथात्मनः ।।6.110.13।। चकारशरजालेनराघवोविमुखंरिपुम् । |
| 6.114.9 | यदैव च जनस्थानेराक्षसैर्भहुनिर्ववृतः । खरस्तवहतोभ्रातातदैवासौ न मानुषः ।।6.114.9।। |
| 6.114.11 | यदैववानरैर्घोरैर्बद्धस्सेतुर्महार्णवे । तदैवहृदयेनाहंशङ्केरामममानुषम् ।।6.114.11।। |
| 6.114.14 | व्यक्तमेषमहायोगीपरमात्मासनातनः । अनादिमध्यनिधनोमहतंपरमोमहान् ।।6.114.14।। तमसःपरमोधाताशङ्खचक्रगदाधरः । श्रीवत्सवक्षानित्यश्रीरजय्यश्शाश्वतोध्रुवः ।।6. |

## Full data

Complete machine-readable results alongside this file: `scratchpad/yuddha_gitasupersite_alignment.json`
