"""
sundara_mbh_narrative_notes.py — emit the final cross-text note layer for the
cluster 'mbh_narrative' (Mahābhārata Ādi/Sabhā/Āraṇyaka/Virāṭa/Udyoga parvas).

Each note was hand-judged by the LLM from machine-mined rare shared SLP1 stems
(see sundara_mbh_narrative_mine.py + sundara_mbh_inspect.py). The parallel verse
(IAST + Leonov-style Russian подстрочник from the corpus) is quoted inside note_ru.

Output: data/crosstext/mbh_narrative.json  (UTF-8, no BOM).
Never touches Leonov's text; every note review_required:true (verse-level/soft).
"""
import sys, json
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

OUT = Path(r"C:\Users\user\Documents\GitHub\CommentaryStrategies\data\crosstext\mbh_narrative.json")

# type codes: А = термин/локус-классикус; Б = формула/эпитет/сравнение (упамана);
#             В = мифологический/этический/ритуальный фон.
NOTES = [
 {
  "shloka": "V.1.34", "lemma_iast": "garuḍa / mahoraga", "type": "Б",
  "stem": "mahorag", "source": "Mahābhārata, Ādiparva 1.114.60",
  "parallel_addr": "01_mahabharata-adiparva:1.114.36-62",
  "note_ru": "Сравнение изогнутого хвоста летящего Ханумана с «огромной змеёй (mahoraga), которую уносит Гаруда» (V.1.34: garuḍeneva hriyamāṇo mahoragaḥ) опирается на устойчивую эпическую антитезу Гаруда↔наги. В Махабхарате термины mahoraga и takṣaka mahoragaḥ стоят рядом в каталоге змеев, явившихся к рождению Арджуны: Ādi 1.114.60 «karkoṭako'tha śeṣaśca vāsukiśca bhujaṅgamaḥ / kacchapaścāpakuṇḍaśca takṣakaśca mahoragaḥ» — «Также Каркотака и Шеша, змей Васуки и Каччхапа, Кунда и великий змей Такшака». Сундараканда переводит эту космологическую вражду в план кавья-сравнения: Хануман — Гаруда, его хвост — обречённая змея. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.1.56", "lemma_iast": "pañcāsya pannaga", "type": "Б",
  "stem": "pannaga", "source": "Mahābhārata, Sabhāparva 2.19.9",
  "parallel_addr": "02_mahabharata-sabhaparva:2.19.1-11",
  "note_ru": "Руки Ханумана, простёртые в небе, сравниваются с «пятиглавыми змеями (pañcāsyāv pannagau), вздымающимися с вершины горы» (V.1.56). Лексема pannaga в эпосе закреплена за змеями-нагами полубожественного ранга, обитателями гор и вод: ср. Sabhā 2.19.9 «arbudaḥ śakravāpī ca pannagau śatrutāpanau» — «Здесь (жили) змеи Арбуда и Шакравапин, каратели врагов». Сравнение работает не на простом сходстве формы, а на коннотации грозной, поднявшейся из горы змеиной мощи. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.1.65", "lemma_iast": "ulkā", "type": "В",
  "stem": "ulkA", "source": "Mahābhārata, Sabhāparva 2.71.26",
  "parallel_addr": "02_mahabharata-sabhaparva:2.71.21-28",
  "note_ru": "Образ Ханумана-метеора (ulkā), падающего по небу из дальних пределов (V.1.65 «khe yathā nipataty ulkā»), у Леонова нейтрален. Но в эпической поэтике ulkā — прежде всего зловещее знамение (utpāta). Канонический локус — Sabhā 2.71.26, знамения при изгнании Пандавов: «rāhuragrasadādityamaparvaṇi viśāṃ pate / ulkā cāpyapasavyaṃ tu puraṃ kṛtvā vyaśīryata» — «(Демон) Раху стал проглатывать Солнце, хотя это и не был день противостояния; начали рассыпаться метеоры, кружась над городом слева направо». Сопоставление высвечивает амбивалентность сравнения: красота полёта несёт обертон грозного предвестия для Ланки. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.1.74", "lemma_iast": "timi-nakra-jhaṣa-kūrma", "type": "Б",
  "stem": "kUrm", "source": "Mahābhārata, Ādiparva 1.25.18-25",
  "parallel_addr": "01_mahabharata-adiparva:1.25.18-25",
  "note_ru": "Обнажившиеся при полёте Ханумана морские твари — «киты, крокодилы, рыбы и черепахи» (timi-nakra-jhaṣāḥ kūrmāḥ, V.1.74) — образуют стандартный эпический список обитателей вод. Тот же набор крупных водяных существ структурирует знаменитую притчу о слоне и черепахе (gaja-kūrma) в Ādi 1.25.18-25, где kūrma «triyojanotsedho daśayojanamaṇḍalaḥ» («черепаха в три йоджаны вышиной, в десять йоджан в окружности») воплощает гигантизм водного мира. Параллель показывает, что сундараканда оперирует готовым эпическим бестиарием океана. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.1.75", "lemma_iast": "bhujaṅga / suparṇa", "type": "Б",
  "stem": "BujaNg", "source": "Mahābhārata, Ādiparva 1.46.16",
  "parallel_addr": "01_mahabharata-adiparva:1.46.16-17",
  "note_ru": "«Змеи, живущие в океане (bhujaṅgāḥ sāgaraṃgamāḥ), решили, что это Супарна (Гаруда)» (V.1.75) — снова формульная пара змей↔Гаруда, на сей раз с термином bhujaṅga. В Махабхарате bhujaṅga часто равно «змей-губитель»: Ādi 1.46.16 «takṣakeṇa bhujaṅgena dhakṣyate» — «(царь) должен быть сожжён змеем (bhujaṅga) Такшакой». Ужас морских змеев перед мнимым Гарудой-Хануманом черпает силу из общеэпического представления о Гаруде как природном истребителе нагов. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.1.86", "lemma_iast": "nāga-yakṣa-rakṣas", "type": "В",
  "stem": "nAga", "source": "Mahābhārata, Udyogaparva 5.99.9-16",
  "parallel_addr": "05_mahabharata-udyogaparva:5.99.9-16",
  "note_ru": "Радость «нагов, якшей и разнообразных ракшасов» при виде неутомимого Ханумана (V.1.86) предполагает населённый полубожественными существами космос, типичный для эпоса. Ср. развёрнутый каталог нагов — «сыновей Гаруды» — в Udyoga 5.99.9-16 (Suvarṇacūḍa, Nāgāśin, Dāruṇa…), где наги предстают могущественным, славным («prādhānyato'tha yaśasā kīrtitāḥ») разрядом существ. Сундараканда кратко вызывает тот же ярус мироздания как зрителей подвига. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.1.97", "lemma_iast": "manyu", "type": "А",
  "stem": "manyu", "source": "Mahābhārata, Udyogaparva 5.21.8",
  "parallel_addr": "05_mahabharata-udyogaparva:5.21.8-15",
  "note_ru": "Гномическая строка горы Майнаки «Неисполнение долга вызывает гнев праведных» (kartavyam akṛtaṃ kāryaṃ satāṃ manyum udīrayet, V.1.97) использует manyu в его этико-эпическом значении — праведный гнев, гнев как нравственная санкция. Тот же концепт manyu как движущая сила героя у Удьйогапарвы: 5.21.8 «bhīṣme bruvati tadvākyaṃ dhṛṣṭamākṣipya manyumān / …karṇo vacanamabravīt» — «Карна, исполненный гнева (manyumān), резко прервал речь Бхишмы». Параллель помогает читателю-индологу увидеть, что manyu здесь — технический термин эпической этики, а не бытовая «злость». Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.1.106", "lemma_iast": "jātarūpamaya", "type": "Б",
  "stem": "jAtarUpamay", "source": "Mahābhārata, Āraṇyakaparva 3.151.5",
  "parallel_addr": "03_mahabharata-aranyakaparva:3.151.1-8",
  "note_ru": "Эпитет jātarūpamaya «из чистого золота» (V.1.106, о золотых пиках горы Майнаки) — устойчивая формула описания дивных, кубероподобных мест. Ср. Āraṇyaka 3.151.5, описание лотосового озера Куберы на Кайласе: «jātarūpamayaiḥ padmaiśchannāṃ paramagandhibhiḥ» — «(озеро,) усеянное ароматнейшими золотыми лотосами (jātarūpamaya)». В обоих случаях золото маркирует принадлежность ландшафта к сфере якшей/богов. Сундараканда наделяет Майнаку той же сакрально-золотой топикой. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.1.118", "lemma_iast": "mārutātmaja", "type": "Б",
  "stem": "mArutAtmaja", "source": "Mahābhārata, Āraṇyakaparva 3.149.16",
  "parallel_addr": "03_mahabharata-aranyakaparva:3.149.2-16",
  "note_ru": "Эпитет mārutātmaja «сын Ветра» (V.1.118) применён к Хануману. Тот же эпитет того же персонажа — в ключевом эпизоде встречи Ханумана и Бхимы (оба сыновья Ваю!): Āraṇyaka 3.149.16 «na hi te kiñcidaprāpyaṃ mārutātmaja vidyate» — «Воистину, для тебя нет ничего недостижимого, о сын Ветра (mārutātmaja)!». Этот локус — лучший внешний комментарий к сундараканде: там Хануман демонстрирует Бхиме свой облик «прыжка через океан» (sāgaralaṅghana), а Бхима признаёт, что Хануман один мог бы уничтожить Ланку. Прямая мифологическая перекличка двух эпосов через общего отца-Ваю. Свидетельство: уровень шлоки (мягкое, но сильное по содержанию).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.1.119", "lemma_iast": "atithiḥ pūjārhaḥ", "type": "В",
  "stem": "pUjArh", "source": "Mahābhārata, Ādiparva 1.157.4",
  "parallel_addr": "01_mahabharata-adiparva:1.157.1-5",
  "note_ru": "Гнома Майнаки «гость заслуживает почёта, даже заурядный» (atithiḥ kila pūjārhaḥ prākṛto 'pi, V.1.119) — формульное выражение дхармы гостеприимства (atithi-pūjā). Ср. Ādi 1.157.4, где Вьяса, придя к скрывающимся Пандавам, спрашивает: «api vipreṣu vaḥ pūjā pūjārheṣu na hīyate» — «не лишаются ли почестей те, кто заслуживает их (pūjārha)?». Один и тот же корень pūjā-arha закрепляет общеэпический кодекс приёма достойного гостя; Майнака прилагает его к Хануману, чтобы оправдать своё желание дать ему отдых. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.1.119", "lemma_iast": "atithi", "type": "В",
  "stem": "atiTi", "source": "Mahābhārata, Āraṇyakaparva 3.154.33",
  "parallel_addr": "03_mahabharata-aranyakaparva:3.154.32-39",
  "note_ru": "К той же строке о госте (V.1.119): термин atithi в эпосе несёт сакральную неприкосновенность. Ср. Āraṇyaka 3.154.33, где ракшаса оправдывает, почему не убил переодетого брахманом Бхиму: «atithiṃ brahmarūpaṃ ca kathaṃ hanyāmanāgasam / …yo hanyānnarakaṃ vrajet» — «Как мог я погубить невиновного, (бывшего нашим) гостем (atithi) в облике брахмана?.. Тот, кто убьёт такого, попадёт в Нараку». Параллель проясняет: почёт гостю у Майнаки — не вежливость, а религиозная норма, нарушение которой ведёт в ад. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.1.125", "lemma_iast": "devarāṭ / vajram udyamya", "type": "В",
  "stem": "devarAw", "source": "Mahābhārata, Udyogaparva 5.18.4",
  "parallel_addr": "05_mahabharata-udyogaparva:5.18.1-9",
  "note_ru": "Майнака вспоминает, как «владыка богов (devarāṭ), разгневанный, подняв ваджру (vajram udyamya), приблизился ко мне» (V.1.125) — отсылка к мифу о подрезании Индрой крыльев гор. Титул devarāṭ «царь богов» — стандартное эпическое именование Индры; ср. Udyoga 5.18.4 «sa sametya mahendrāṇyā devarājaḥ śatakratuḥ / …pālayāmāsa devarāṭ» — «И царь богов (devarāṭ), совершитель ста жертвоприношений, стал охранять (миры)». Параллель закрепляет, что в V.1.125 действует именно Индра-вседержитель с его атрибутом-ваджрой, а Майнака — один из немногих уцелевших крылатых гор, спасённый Ваю. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.1.141", "lemma_iast": "satkriyā", "type": "В",
  "stem": "satkriyA", "source": "Mahābhārata, Āraṇyakaparva 3.182.10",
  "parallel_addr": "03_mahabharata-aranyakaparva:3.182.1-10",
  "note_ru": "Похвала Сурасы Хануману «доволен я тобой, сумевшей оказать ему гостеприимство (satkriyā)» (V.1.141) использует satkriyā в техническом значении ритуального приёма-почитания. Ср. Āraṇyaka 3.182.10, где Хайхаи говорят отшельнику: «na vayaṃ satkriyāṃ mune tvatto'rhāḥ karmadoṣeṇa» — «Мы недостойны, мудрец, твоего гостеприимства (satkriyā): грех на нас». Один и тот же термин satkriyā связывает эпизод испытания Ханумана Сурасой с общеэпической этикой почётного приёма. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.1.182", "lemma_iast": "kṛṣyamāṇa megha", "type": "Б",
  "stem": "kfzyamAR", "source": "Mahābhārata, Āraṇyakaparva 3.48.34",
  "parallel_addr": "03_mahabharata-aranyakaparva:3.48.30-35",
  "note_ru": "Облака, «которые тянула за собой обезьяна» (kapinā kṛṣyamāṇāni mahābhrāṇi, V.1.182), — редкое причастие kṛṣyamāṇa «влекомый». В Махабхарате тот же страдательный образ применён к телам павших, влекомым хищниками: Āraṇyaka 3.48.34 «teṣāṃ drakṣyasi… gātrāṇi… kravyādaiḥ kṛṣyamāṇāni bhakṣyamāṇāni ca» — «Ты увидишь, как их тела хищные звери будут таскать (kṛṣyamāṇāni) и пожирать». Контраст употреблений (величавые облака у Ханумана ↔ зловещее влечение трупов в МБх) — характерный пример того, как один эпический глагол обслуживает противоположные регистры. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.2.2", "lemma_iast": "puṣpavarṣa", "type": "В",
  "stem": "puzpavarz", "source": "Mahābhārata, Virāṭaparva 4.59.39",
  "parallel_addr": "04_mahabharata-virataparva:4.59.39-44",
  "note_ru": "«Цветочный дождь, облетевший с деревьев» (puṣpavarṣa, V.2.2), которым осыпан Хануман, — формула божественного одобрения подвига. Ср. Virāṭa 4.59.39, где Индра чествует поединок Арджуны и Бхишмы: «devarājastu pārthabhīṣmasamāgamam / pūjayāmāsa divyena puṣpavarṣeṇa» — «царь богов почтил (встречу Партхи и Бхишмы) ливнем небесных цветов (puṣpavarṣa)». В обоих эпосах цветочный дождь — небесная санкция героического деяния; Хануман, «казавшийся сделанным из цветов», получает ту же небесную награду. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.7.1", "lemma_iast": "meghajāla", "type": "Б",
  "stem": "meGajAl", "source": "Mahābhārata, Āraṇyakaparva 3.39.15",
  "parallel_addr": "03_mahabharata-aranyakaparva:3.39.14-20",
  "note_ru": "Дворцовый комплекс Ланки сравнивается с «огромной грядой облаков в пору дождей, с молниями» (meghajālaṃ vidyutpinaddham, V.7.1). Сложное слово meghajāla «сеть/гряда облаков» — общий поэтический штамп; ср. Āraṇyaka 3.39.15 при уходе Арджуны в Гималаи: «meghajālaṃ ca vitataṃ chādayāmāsa sarvataḥ» — «бескрайние скопища облаков (meghajāla) всё вокруг покрыли тенью». Параллель показывает, что зодческая роскошь Ланки описана через тот же арсенал «облачных» сравнений, что и грозовой пейзаж эпоса. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.12.3", "lemma_iast": "āryapathe sthitā", "type": "В",
  "stem": "pravar", "source": "Mahābhārata, Āraṇyakaparva 3.250.1-9",
  "parallel_addr": "03_mahabharata-aranyakaparva:3.250.1-9",
  "note_ru": "Хануман размышляет о Сите как «стоящей на наилучшем пути благородных (āryapathe sthitā), сосредоточенной на сохранении добродетели (svaśīlasaṃrakṣaṇa)», которую погубил «предводитель ракшасов (rākṣasānāṃ pravara)» (V.12.3). Ситуация дословно рифмуется с эпизодом домогательства Джаядратхи к Драупади (Āraṇyaka 3.250 сл.): там «śibīnāṃ pravara» (Котикашья) подступает к одинокой верной жене в лесу, а Драупади защищает свою дхарму («niratā svadharme»). Обе сцены — испытание pativratā наедине перед лицом похитителя; параллель высвечивает типовой эпический мотив «одинокая добродетельная жена и насильник-pravara». Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.13.8", "lemma_iast": "hriyamāṇā", "type": "Б",
  "stem": "hriyamAR", "source": "Mahābhārata, Udyogaparva 5.176.41",
  "parallel_addr": "05_mahabharata-udyogaparva:5.176.35-42",
  "note_ru": "Хануман воображает Ситу «когда её несли (hriyamāṇāyāḥ) по пути сиддхов» (V.13.8) — причастие от hṛ «похищать», эпический термин насильственного увоза женщины. Тот же глагол в рассказе Амбы (Udyoga 5.176.41): «eṣa me hriyamāṇāyā… abhavaddhṛdi saṅkalpaḥ» — «Когда меня увозили насильно (hriyamāṇā), у меня в сердце зародилось желание (отомстить)». Параллель ставит похищение Ситы в один типологический ряд с похищением Амбы Бхишмой — оба запускают сюжет мести/войны. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.13.53", "lemma_iast": "nirdahet / sāgaralaṅghana", "type": "В",
  "stem": "sarvavAnar", "source": "Mahābhārata, Āraṇyakaparva 3.267.27",
  "parallel_addr": "03_mahabharata-aranyakaparva:3.267.22-32",
  "note_ru": "Опасение Ханумана, что Рама, не найдя Ситу, «уничтожит всех обезьян (nirdahet sarvavānarān)» (V.13.53), отсылает к узловой проблеме всего эпоса — переправе войска через стойойджанный океан. Рамопакхьяна Махабхараты прямо излагает её устами Рамы: Āraṇyaka 3.267.27 «śatayojanavistāraṃ na śaktāḥ sarvavānarāḥ / krāntuṃ toyanidhiṃ» — «Вы, обезьяны (sarvavānarāḥ), не сможете все вместе пересечь водный простор шириной в сотню йоджан». Эта параллель — компактный эпический пересказ той самой повествовательной рамки, в которой действует Хануман-разведчик. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.15.20", "lemma_iast": "śikhām iva vibhāvasoḥ pinaddhāṃ dhūmajālena", "type": "Б",
  "stem": "mandapraKyAyamAn", "source": "Mahābhārata, Āraṇyakaparva 3.65.7",
  "parallel_addr": "03_mahabharata-aranyakaparva:3.65.6-8",
  "note_ru": "Сита в ашоковой роще «с трудноузнаваемым обликом (mandaprakhyāyamānena rūpeṇa), сияющая подобно пламени огня, скрытому клубами дыма» (V.15.20) — это почти дословно стих о найденной Дамаянти в Нала-упакхьяне: Āraṇyaka 3.65.7 «mandaprakhyāyamānena rūpeṇāpratimena tām / pinaddhāṃ dhūmajālena prabhāmiva vibhāvasoḥ» — «Несравненная красота её пряталась от взоров, словно солнце за облёкшею его завесой дыма». Совпадение целого полустишия (формула «mandaprakhyāyamānena rūpeṇa … pinaddhāṃ dhūmajālena») — яркий случай общего эпического клише для покинутой, измождённой тоской верной жены. Свидетельство: уровень шлоки (сильная формульная параллель).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.19.17", "lemma_iast": "ratnagarbhagṛhocitā mṛṇālī aciroddhṛtā", "type": "Б",
  "stem": "ratnagarBagfhocit", "source": "Mahābhārata, Āraṇyakaparva 3.65.15",
  "parallel_addr": "03_mahabharata-aranyakaparva:3.65.9-16",
  "note_ru": "Стих о Сите «нежную, с прекрасным телом, привыкшую жить во дворце, полном самоцветов (ratnagarbhagṛhocitā), подобную сжигаемому зноем недавно вырванному лотосовому стеблю (mṛṇālīm aciroddhṛtām)» (V.19.17) совпадает практически слово-в-слово с описанием Дамаянти: Āraṇyaka 3.65.15 «sukumārīṃ sujātāṅgīṃ ratnagarbhagṛhocitām / dahyamānāmivoṣṇena mṛṇālīmaciroddhṛtām». Это вторая (после V.15.20) общая формула из того же пассажа Нала-упакхьяны: образ «дворцовой неженки, ставшей вырванным лотосовым стеблем» — устойчивый троп для героини в изгнании/плену. Сильное свидетельство прямого формульного родства Сита↔Дамаянти. Свидетельство: уровень шлоки (сильная формульная параллель).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.20.29", "lemma_iast": "suparṇaḥ pannagaṃ yathā", "type": "Б",
  "stem": "pannag", "source": "Mahābhārata, Āraṇyakaparva 3.176.2",
  "parallel_addr": "03_mahabharata-aranyakaparva:3.176.1-11",
  "note_ru": "Равана льстит Сите: «ты похищаешь мою душу, словно Супарна — змею (suparṇaḥ pannagaṃ yathā)» (V.20.29). Сравнение перекодирует уже знакомую формулу Гаруда↔наг (ср. V.1.34, V.1.75) в любовно-кавья регистр: похищающий Гаруда теперь — метафора пленяющей красоты. Эпический фон термина pannaga как жертвы более сильного — Āraṇyaka 3.176.2, где Бхима, схваченный змеем, обращается: «kāmayā brūhi pannaga… kastvaṃ» — «Поведай мне милостиво, о змей (pannaga)». Параллель помогает увидеть, что комплимент Раваны построен на инверсии хищной формулы. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.22.20", "lemma_iast": "bhasma … tejasā", "type": "В",
  "stem": "kurmi", "source": "Mahābhārata, Udyogaparva 5.180.24",
  "parallel_addr": "05_mahabharata-udyogaparva:5.180.18-26",
  "note_ru": "Угроза-несовершение Ситы Раване: «не будь повеления Рамы и сохранения мной тапаса, я обратила бы тебя в пепел своей мощью (bhasma … tejasā), Дашагрива» (V.22.20). Здесь действует общеэпическое представление о tapas как накопленной испепеляющей энергии. Ср. Udyoga 5.180.24, где Рама Джамадагнья объясняет Бхишме, по чему он не ударит: «ye te vedāḥ śarīrasthā… tapaśca sumahattaptaṃ na tebhyaḥ praharāmyaham» — «Веды, что в теле твоём, и аскетические заслуги, накопленные суровым покаянием (tapas), — по ним я не ударю». В обоих местах tapas мыслится как реальная боевая сила, которую носитель добровольно сдерживает. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.24.12", "lemma_iast": "damayantī … sagara … saudāsa", "type": "В",
  "stem": "sagara", "source": "Mahābhārata, Āraṇyakaparva 3.106.10-17 (Sagara) и 3.50-78 (Nala–Damayantī)",
  "parallel_addr": "03_mahabharata-aranyakaparva:3.106.10-17",
  "note_ru": "Хануман ободряет Ситу списком образцовых верных жён: «как Мадаянти к Саудасе, как Кешини к Сагаре, как Дамаянти, дочь Бхимы, верная мужу — к Нишадцу (Нале)» (V.24.12). Все три pativratā-пары — герои именно Араньякапарвы. Сагара — герой кумулятивного сказания Āraṇyaka 3.106 сл. («etatte sarvamākhyātaṃ… sagareṇa vivāsitaḥ»), а Дамаянти, дочь Бхимы (bhaimī) — героиня Нала-упакхьяны (Āraṇyaka 3.50-78), откуда уже извлечены формульные параллели V.15.20 и V.19.17. Таким образом, перечень эталонных жён у Ханумана опирается на тот же повествовательный фонд Vana-parvan, что и описания самой Ситы. Свидетельство: уровень шлоки (мягкое; связь по корпусу имён).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.25.8", "lemma_iast": "vivarṇavadanābhavat / kadalī pravāte", "type": "Б",
  "stem": "vivarRavadanABavat", "source": "Mahābhārata, Āraṇyakaparva 3.61.95",
  "parallel_addr": "03_mahabharata-aranyakaparva:3.61.95-97",
  "note_ru": "Сита перед ракшаси «трепещущая, словно подорожник (банан) на ветру (kadalī pravāte), … побледневшая лицом (vivarṇavadanābhavat)» (V.25.8). Глагольная формула pāda «vivarṇavadanābhavat» дословно совпадает с описанием покинутой Дамаянти: Āraṇyaka 3.61.95 «bhartṛśokaparā dīnā vivarṇavadanābhavat» — «была она бледна и печальна, поглощена тоской о супруге (vivarṇavadanābhavat)»; а в следующих стихах Дамаянти, как и Сита, ищет утешения у дерева aśoka. Третья общая формула из Нала-упакхьяны (ср. V.15.20, V.19.17) подтверждает, что портрет страдающей Ситы систематически собран из клише, отработанных на образе Дамаянти. Свидетельство: уровень шлоки (сильная формульная параллель).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
 {
  "shloka": "V.6.32", "lemma_iast": "airāvatasama gaja", "type": "Б",
  "stem": "gaja", "source": "Mahābhārata, Sabhāparva 2.48.25",
  "parallel_addr": "02_mahabharata-sabhaparva:2.48.22-33",
  "note_ru": "Описание боевых слонов Ланки «в битве подобных Айравате (airāvatasamān yudhi)» (V.6.32) использует слона Индры Айравату как эталон. Ср. каталог даров на rājasūya Юдхиштхиры (Sabhā 2.48.25): «virāṭena tu matsyena… kuñjarāṇāṃ sahasre dve mattānāṃ samupāhṛte» — «Виратой, царём матсьев, были доставлены две тысячи возбуждённых слонов (kuñjara)». Перечни породистых, «опьянённых» боевых слонов — общий эпический топос царской/военной роскоши; сундараканда применяет его к могуществу Раваны. Свидетельство: уровень шлоки (мягкое).",
  "trigger": "crosstext", "subtype": "cross_text", "cluster": "mbh_narrative", "review_required": True
 },
]

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(NOTES, f, ensure_ascii=False, indent=1)
    # BOM guard
    with open(OUT, 'rb') as f:
        head = f.read(3)
    assert head[:3].hex() != 'efbbbf', "BOM written!"
    print(f"wrote {len(NOTES)} notes -> {OUT}")
    chapters = sorted({n['shloka'].split('.')[1] for n in NOTES}, key=int)
    print("chapters covered:", ", ".join(chapters))

if __name__ == '__main__':
    main()
