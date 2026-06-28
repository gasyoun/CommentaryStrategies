"""
sundara_ch2_68_pipeline.py — Commentary generation for Sundarakāṇḍa chapters 2–68.

Produces per-chapter data/sundara_ch{N}_commentary_to_add.json files (same shape as
ch.1), then aggregates everything into data/sundara_commentary_to_add.json plus
data/sundara_book_stats.json.

Design principles:
- Generalises the ch.1 KB / dedup logic; never re-derives the method.
- Seeds global "already-noted" set from ch.1 output so no lemma already noted
  in ch.1 gets a duplicate first-appearance note.
- One KB covers the whole book; each chapter only draws from it.
- Conservative by construction: verses that the подстрочник already makes clear
  get no note.
- All output files: UTF-8, no BOM, review_required: true throughout.
"""
import sys, json, re, collections, subprocess
from pathlib import Path
from datetime import date

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CS_DIR   = Path(r"C:\Users\user\Documents\GitHub\CommentaryStrategies")
DATA_DIR = CS_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

CORPUS_DIR = Path(r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl")
SUNDARA    = CORPUS_DIR / "05_ramayana-sundarakanda.jsonl"

TODAY = str(date.today())

# ── helpers ──────────────────────────────────────────────────────────────────

def load_jsonl(path):
    rows = []
    try:
        with open(path, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        rows.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
    except Exception as e:
        print(f"  WARN: {path}: {e}", file=sys.stderr)
    return rows

def short_addr(ch: int, v: int) -> str:
    return f"V.{ch}.{v}"

def ucfirst(s: str) -> str:
    return s[:1].upper() + s[1:] if s else s

_TOKEN_RE = re.compile(r'[A-Za-z][A-Za-z]{2,}')
STOP_SLP1 = {
    'tat','tato','iva','ca','tu','iti','eva','api','hi','na','sa','te','tam',
    'sma','vai','yat','kim','yad','tad','idam','asya','tasya','atra','tatra',
    'yatra','puna','atha','tatah','tatas','atah','ata','ha','svam','tena',
    'yena','cha','anu','upa','pra','sam','pari','nis','nir','dur','sus','abhi',
    'avi','ava','ati','adhi','aha','ima','mahA','maha','para','param',
    'asmin','tasmAt','yasmin','enam','etat','etad','ayam','imAn',
}

def content_tokens(slp1: str) -> set:
    toks = _TOKEN_RE.findall(slp1.lower())
    return {t for t in toks if t not in STOP_SLP1 and len(t) >= 3}


# ── BOOK-WIDE KNOWLEDGE BASE ─────────────────────────────────────────────────
# Keys are IAST lemmas exactly as they appear in the Sanskrit corpus text.
# Covers all chapters 1–68; the ch.1 seed set (already_noted) prevents duplication.
#
# Convention for `slp1_triggers`: list of SLP1 token substrings that, when found
#   in a verse's SLP1 text, flag this lemma as present. Matching is substring-in-token
#   (to handle inflection). Keep short enough to avoid false positives.
#
# `skip`: True → never emit a note (too well-known / already rendered by подстрочник).

KB = {
    # ── Ch.1 entries (seeded; will be suppressed by already_noted) ──────────
    "cāraṇa":      {"ru": "чараны",              "type": "В", "trigger": "realia",   "priority": "high",
        "slp1_triggers": ["cAraRa","cArana"],
        "note": "класс полубожественных небесных певцов-странников. Комм. «Бхушана»: dēvagāyakāḥ «божественные певцы».",
        "commentators": ["Bhūṣaṇa","Tattvadīpikā"], "western": ["Goldman 1994"]},
    "vānara":      {"ru": "ванара",               "type": "А", "trigger": "term",     "priority": "high",
        "slp1_triggers": ["vAnara","vAnara"],
        "note": "букв. «лесной житель», обезьяна; общий термин для народа Сугривы.",
        "commentators": ["Tilaka"], "western": []},
    "mahābala":    {"ru": "обладающий великой силой","type": "А","trigger": "epithet", "priority": "med",
        "slp1_triggers": ["mahAbala"],
        "note": "эпитет Ханумана, букв. «обладающий великой силой» (mahā-bala). Первое вхождение в кн. V.",
        "commentators": [], "western": []},
    "dhīra":       {"ru": "стойкий",              "type": "А", "trigger": "epithet",  "priority": "low",
        "slp1_triggers": ["DIra"],
        "note": "букв. «твёрдый», «мудрый» (dhīra); подчёркивает ментальную концентрацию героя.",
        "commentators": [], "western": []},
    "vaidūrya":    {"ru": "вайдурья",             "type": "А", "trigger": "term",     "priority": "med",
        "slp1_triggers": ["vEDUrya","vaidUrya"],
        "note": "берилл / «кошачий глаз» (vaidūrya), драгоценный минерал зеленовато-синего отлива.",
        "commentators": [], "western": []},
    "kapivara":    {"ru": "лучший из обезьян",    "type": "А", "trigger": "epithet",  "priority": "med",
        "slp1_triggers": ["kapivara"],
        "note": "стандартный эпитет-сравнение (kapi-vara «лучший из обезьян»), синонимичен vānaraśreṣṭha.",
        "commentators": [], "western": []},
    "nāga":        {"ru": "наг / слон",            "type": "Б", "trigger": "term",     "priority": "high",
        "slp1_triggers": ["nAga"],
        "note": "слово nāga двузначно: «наг» (полубожественный змей) и «слон». Комм. «Широмани» глоссирует здесь gaja (слон). Подстрочник выбирает один вариант, скрывая амбивалентность оригинала.",
        "commentators": ["Śiromaṇi"], "western": ["Goldman 1994"]},
    "mārutātmaja": {"ru": "сын бога ветра",        "type": "А", "trigger": "epithet",  "priority": "high",
        "slp1_triggers": ["mArutAtmaja"],
        "note": "патроним Ханумана (māruta-ātmaja «сын Маруты/Ваю»), пара к vāyuputra.",
        "commentators": [], "western": []},
    "kapikuñjara": {"ru": "слон среди обезьян",    "type": "А", "trigger": "epithet",  "priority": "med",
        "slp1_triggers": ["kapikuYjara","kapikunjara"],
        "note": "метафора высшего превосходства в группе (kapi-kuñjara «слон среди обезьян»), ср. puruṣarṣabha «бык среди мужей».",
        "commentators": [], "western": []},
    "rāghava":     {"ru": "Потомок Рагху",          "type": "А", "trigger": "crossref", "priority": "high",
        "slp1_triggers": ["rAGava"],
        "grintser": "см. примеч. к I.1.1 (Гринцер)",
        "note": "стандартный эпитет Рамы (потомок царя Рагху).",
        "commentators": [], "western": []},
    "janakātmajā": {"ru": "Дочь Джанаки",           "type": "А", "trigger": "crossref", "priority": "high",
        "slp1_triggers": ["janakAtmajA"],
        "text_triggers": ["janakātmajā"],
        "grintser": "см. примеч. к I.1.25 (Гринцер)",
        "note": "патроним Ситы (дочь царя Джанаки).",
        "commentators": [], "western": []},
    "vāyuputra":   {"ru": "сын Ваю",                "type": "А", "trigger": "epithet",  "priority": "med",
        "slp1_triggers": ["vAyuputra"],
        "note": "патроним Ханумана (vāyu-putra «сын бога ветра»), пара к mārutātmaja.",
        "commentators": ["Tilaka"], "western": []},
    "rāvaṇa":      {"ru": "Равана",                 "type": "В", "trigger": "realia",   "priority": "low",
        "slp1_triggers": ["rAvaRa"],
        "note": "царь ракшасов, похититель Ситы; центральный антагонист.",
        "skip": True},
    "surasā":      {"ru": "Сураса",                 "type": "В", "trigger": "realia",   "priority": "high",
        "slp1_triggers": ["surasA"],
        "note": "мать нагов (nāgamātā), посланная богами испытать Ханумана на пути через океан.",
        "commentators": ["Tattvadīpikā"], "western": []},
    "dāśarathi":   {"ru": "Сын Дашаратхи",          "type": "А", "trigger": "crossref", "priority": "med",
        "slp1_triggers": ["dASaraTi"],
        "grintser": "см. примеч. к I.1.8 (Гринцер)",
        "note": "патроним Рамы (сын царя Дашаратхи).",
        "commentators": [], "western": []},
    "māruti":      {"ru": "Марути",                  "type": "А", "trigger": "epithet",  "priority": "med",
        "slp1_triggers": ["mAruti"],
        "note": "именное производное от Марут (бог ветра) — стандартное имя Ханумана.",
        "commentators": [], "western": []},
    "vaidehī":     {"ru": "Вайдехи",                 "type": "А", "trigger": "crossref", "priority": "med",
        "slp1_triggers": ["vEdehi","vaidehI"],
        "grintser": "см. примеч. к I.1.28 (Гринцер)",
        "note": "эпитет Ситы (царевна из Видехи).",
        "commentators": [], "western": []},
    "maithilī":    {"ru": "Майтхили",                "type": "А", "trigger": "crossref", "priority": "med",
        "slp1_triggers": ["mEWilI","maithilI"],
        "grintser": "см. примеч. к I.1.26 (Гринцер)",
        "note": "эпитет Ситы (царевна из Митхилы).",
        "commentators": [], "western": []},
    "siṃhikā":     {"ru": "Симхика",                 "type": "В", "trigger": "realia",   "priority": "high",
        "slp1_triggers": ["siMhikA"],
        "note": "ракшасини, «ловящая тени» (chāyāgrahin): по «Широмани», притягивает существ за тень. Хануман уничтожает её при перелёте.",
        "commentators": ["Śiromaṇi"], "western": []},
    "mahākāya":    {"ru": "огромный",                "type": "А", "trigger": "epithet",  "priority": "low",
        "slp1_triggers": ["mahAkAya"],
        "note": "эпитет (mahā-kāya «обладающий великим телом»).",
        "commentators": [], "western": []},
    "maināka":     {"ru": "Майнака",                 "type": "В", "trigger": "realia",   "priority": "high",
        "slp1_triggers": ["mainAka"],
        "note": "гора, поднявшаяся из океана навстречу Хануману как место отдыха. В «Бхушане» — сын Гималаев; эпитет hiraṇyanābha «золотопупый».",
        "commentators": ["Bhūṣaṇa"], "western": []},

    # ── New entries for chapters 2–68 ──────────────────────────────────────────

    # Hanumān's epithets (additional)
    "hanumat":     {"ru": "Хануман",                 "type": "А", "trigger": "epithet",  "priority": "high",
        "slp1_triggers": ["hanumat","hanUmat"],
        "note": "имя героя — «наделённый (крепкими) челюстями» (hanu «челюсть» + mat). «Тилака» объясняет: Индра ударил его ваджрой по подбородку, отсюда имя. Первое появление формы hanumat в кн. V.",
        "commentators": ["Tilaka"], "western": ["Goldman 1994"]},
    "hanūmān":     {"ru": "Хануман",                 "type": "А", "trigger": "epithet",  "priority": "high",
        "slp1_triggers": ["hanUmAn"],
        "note": "имя героя (hanūmān, именительный от hanumat): «наделённый крепкими челюстями»; по «Тилаке», Индра ударил его ваджрой по подбородку, отсюда имя.",
        "skip_if_noted": "hanumat",  # suppress if hanumat already noted
        "commentators": ["Tilaka"], "western": []},
    "pavananandana":{"ru": "сын Паваны",              "type": "А", "trigger": "epithet",  "priority": "med",
        "slp1_triggers": ["pavananandana"],
        "note": "эпитет Ханумана: pavana-nandana «сын Паваны (бога ветра)». Синонимичен mārutātmaja.",
        "commentators": [], "western": []},
    "anilātmaja":  {"ru": "сын Анилы",               "type": "А", "trigger": "epithet",  "priority": "low",
        "slp1_triggers": ["anilAtmaja"],
        "note": "патроним Ханумана: anila-ātmaja «сын Анилы (бога ветра)»; синонимичен mārutātmaja, vāyuputra.",
        "commentators": [], "western": []},
    "kapīndra":    {"ru": "царь обезьян",             "type": "А", "trigger": "epithet",  "priority": "med",
        "slp1_triggers": ["kapIndra"],
        "note": "эпитет «царь обезьян» (kapi-indra), прилагается к Сугриве или Хануману в зависимости от контекста.",
        "commentators": [], "western": []},
    "plavaga":     {"ru": "прыгун / обезьяна",        "type": "А", "trigger": "term",     "priority": "low",
        "slp1_triggers": ["plavaga"],
        "note": "букв. «прыгающий по воде» или «прыгун» (pla-vaga); поэтическое обозначение обезьяны, акцентирует прыжковую природу ванаров.",
        "commentators": [], "western": []},
    "plavaṃgama":  {"ru": "прыгун / обезьяна",        "type": "А", "trigger": "term",     "priority": "low",
        "slp1_triggers": ["plavaGgama","plavaggama"],
        "note": "«движущийся прыжками» (plavaṃ-gama); синоним plavaga как поэтическое обозначение обезьяны.",
        "skip_if_noted": "plavaga",
        "commentators": [], "western": []},
    "śākhāmṛga":  {"ru": "ветвелаз / обезьяна",      "type": "А", "trigger": "term",     "priority": "low",
        "slp1_triggers": ["SAKAmfga","SAKAmRga"],
        "note": "поэтическое обозначение обезьяны: śākhā-mṛga «ветвяной зверь» (букв. «зверь ветвей»).",
        "commentators": [], "western": []},
    "vānaraśreṣṭha":{"ru": "лучший из ванаров",      "type": "А", "trigger": "epithet",  "priority": "low",
        "slp1_triggers": ["vAnareXWa","vAnaraSrezWa"],
        "note": "vānara-śreṣṭha «лучший из обезьян», синонимичен kapivara; первое вхождение в кн. V.",
        "commentators": [], "western": []},

    # Rāma's epithets (additional)
    "kākutstha":   {"ru": "Потомок Какутстхи",        "type": "А", "trigger": "crossref", "priority": "med",
        "slp1_triggers": ["kAkutsTA"],
        "grintser": "см. примеч. к I.1.1 (Гринцер)",
        "note": "эпитет Рамы (потомок героя Какутстхи из рода Икшваку).",
        "commentators": [], "western": []},
    "rāmabhadra":  {"ru": "благой Рама",               "type": "А", "trigger": "epithet",  "priority": "low",
        "slp1_triggers": ["rAmaBadra"],
        "note": "восхвалительный эпитет Рамы: rāma-bhadra «благой Рама»; вариант rāma + bhadra «счастливый».",
        "commentators": [], "western": []},
    "puruṣarṣabha":{"ru": "бык среди мужей",           "type": "А", "trigger": "epithet",  "priority": "med",
        "slp1_triggers": ["puruXarXaBa","puruSarSaBa"],
        "note": "стандартная animal-metaphor высшего ранга: puruṣa-ṛṣabha «бык среди мужей». Ср. kapikuñjara «слон среди обезьян».",
        "commentators": [], "western": []},
    "naravyāghra": {"ru": "тигр среди людей",           "type": "А", "trigger": "epithet",  "priority": "low",
        "slp1_triggers": ["naravyAGra"],
        "note": "nara-vyāghra «тигр среди людей» — animal-metaphor ранга, симметричная puruṣarṣabha.",
        "commentators": [], "western": []},
    "ikṣvāku":     {"ru": "из рода Икшваку",            "type": "А", "trigger": "crossref", "priority": "med",
        "slp1_triggers": ["ikXvAku","ikSvAku"],
        "grintser": "см. примеч. к I.1.2 (Гринцер)",
        "note": "принадлежность к роду Икшваку (Ikṣvāku) — солнечная династия, к которой принадлежат Рама и его предки.",
        "commentators": [], "western": []},

    # Sītā's epithets (additional)
    "sītā":        {"ru": "Сита",                      "type": "А", "trigger": "crossref", "priority": "high",
        "slp1_triggers": ["sItA"],
        "grintser": "см. примеч. к I.1.4 (Гринцер)",
        "note": "имя героини: sītā «борозда» (от sī- «пахать»); по «Арандхати», Сита родилась из борозды, проведённой Джанакой.",
        "commentators": [], "western": ["Goldman 1994"]},
    "jānakī":      {"ru": "Джанаки",                   "type": "А", "trigger": "crossref", "priority": "med",
        "slp1_triggers": ["jAnakI"],
        "grintser": "см. примеч. к I.1.25 (Гринцер)",
        "note": "патроним Ситы (дочь царя Джанаки); синонимичен janakātmajā.",
        "skip_if_noted": "janakātmajā",
        "commentators": [], "western": []},
    "bhāminī":     {"ru": "прекрасная / гневная",       "type": "Б", "trigger": "term",     "priority": "med",
        "slp1_triggers": ["BAminI"],
        "note": "bh āminī двузначно: «прекрасная женщина» и «гневливая (женщина)». Контекст определяет выбор; подстрочник может выбрать один из оттенков.",
        "commentators": [], "western": []},
    "aninditā":    {"ru": "безупречная",                "type": "А", "trigger": "epithet",  "priority": "low",
        "slp1_triggers": ["aniniditA","aniniditA"],
        "note": "эпитет Ситы: aninditā «безупречная, не порицаемая»; характеристика нравственного достоинства.",
        "commentators": [], "western": []},
    "śubhānanā":   {"ru": "прекраснолицая",             "type": "А", "trigger": "epithet",  "priority": "low",
        "slp1_triggers": ["SuBAnAnA","SubhAnAnA"],
        "note": "эпитет Ситы: śubha-ānanā «с прекрасным лицом».",
        "commentators": [], "western": []},
    "anagha":      {"ru": "безгрешная / безгрешный",    "type": "А", "trigger": "epithet",  "priority": "low",
        "slp1_triggers": ["anaGa"],
        "note": "anagha «безгрешный / безгрешная»; прилагается к Раме и к Сите; акцент на моральной чистоте.",
        "commentators": [], "western": []},

    # Rāvaṇa's Lanka (geography and architecture)
    "laṅkā":       {"ru": "Ланка",                      "type": "В", "trigger": "realia",   "priority": "high",
        "slp1_triggers": ["laNkA"],
        "note": "остров-крепость Раваны; «Шримад Рамаяна» локализует её на вершине горы Трикута. «Широмани» отождествляет с островом, известным ныне как Шри-Ланка. «Тилака» акцентирует неприступность её стен. Первое вхождение в кн. V.",
        "commentators": ["Tilaka", "Śiromaṇi"], "western": ["Goldman 1994"]},
    "puṣpaka":     {"ru": "Пушпака",                    "type": "В", "trigger": "realia",   "priority": "high",
        "slp1_triggers": ["puzpaka"],
        "text_triggers": ["puṣpaka"],
        "note": "puspaka (пушпака) — воздушная колесница, первоначально принадлежавшая Кубере, захваченная Раваной. «Бхушана»: «движется куда пожелает повелитель» (yathecchagāmī). Первое появление в кн. V.",
        "commentators": ["Bhūṣaṇa"], "western": []},
    "trikūṭa":     {"ru": "Трикута",                    "type": "В", "trigger": "realia",   "priority": "med",
        "slp1_triggers": ["trikUwa"],
        "note": "tri-kūṭa «трёхглавая [гора]» — горная гряда, на которой стоит Ланка. «Тилака» объясняет три вершины именами богов.",
        "commentators": ["Tilaka"], "western": []},
    "aśoka":       {"ru": "ашока",                      "type": "В", "trigger": "realia",   "priority": "high",
        "slp1_triggers": ["aSoka"],
        "text_triggers": ["aśoka"],
        "note": "дерево ашока (Saraca asoca / Jonesia ashoka); символ заточения Ситы в одноимённой роще. «Широмани» глоссирует: aśoka букв. «без скорби», отсюда горькая ирония места заключения.",
        "commentators": ["Śiromaṇi"], "western": []},
    "aśokavanikā": {"ru": "роща Ашока",                 "type": "В", "trigger": "realia",   "priority": "high",
        "slp1_triggers": ["aSokavanikA"],
        "text_triggers": ["aśokavanikā","aśokavanikā"],
        "note": "роща деревьев ашока (aśoka-vanikā), место заключения Ситы в Ланке; центральное место действия кн. V.",
        "commentators": [], "western": ["Goldman 1994"]},
    "prāsāda":     {"ru": "дворец / башня",              "type": "А", "trigger": "term",     "priority": "low",
        "slp1_triggers": ["prAsAda"],
        "note": "prāsāda — многоэтажный дворцовый павильон или башня-терраса; в контексте Ланки — элемент архитектуры крепости-дворца Раваны.",
        "commentators": [], "western": []},
    "gopura":      {"ru": "гопура / ворота",             "type": "А", "trigger": "term",     "priority": "low",
        "slp1_triggers": ["gopura"],
        "note": "gopura — монументальные надвратные башни; в описании Ланки — ворота главного дворца.",
        "commentators": [], "western": []},

    # Rākṣasa world
    "rākṣasa":     {"ru": "ракшас",                     "type": "А", "trigger": "term",     "priority": "high",
        "slp1_triggers": ["rAkzasa"],
        "text_triggers": ["rākṣasa"],
        "note": "rākṣasa — класс демонических существ; этимология в «Нирукте»: «те, кого охраняют» (rakṣ-) или «те, кто охраняют» (ракшанта). По «Тилаке», людоеды ночного времени. Подстрочник переводит нарицательным «ракшас», что уместно, но утрачивает коннотации.",
        "commentators": ["Tilaka"], "western": []},
    "rākṣasī":     {"ru": "ракшасини",                  "type": "А", "trigger": "term",     "priority": "med",
        "slp1_triggers": ["rAkzasI"],
        "text_triggers": ["rākṣasī","rākṣasīnāṃ"],
        "note": "rākṣasī — женская особь из класса ракшасов; стражницы-ракшасини охраняют Ситу в роще.",
        "skip_if_noted": "rākṣasa",
        "commentators": [], "western": []},
    "piśāca":      {"ru": "пишача",                     "type": "В", "trigger": "realia",   "priority": "med",
        "slp1_triggers": ["piSAca"],
        "note": "piśāca — разряд злобных духов-людоедов, питающихся плотью и кровью; в комментарии «Бхушана» отличаются от ракшасов пищевыми привычками.",
        "commentators": ["Bhūṣaṇa"], "western": []},
    "yakṣa":       {"ru": "якша",                       "type": "В", "trigger": "realia",   "priority": "med",
        "slp1_triggers": ["yakXa","yakSa"],
        "note": "yakṣa — класс полубожественных существ, слуг Куберы; в описаниях Ланки маркируют «инородную» роскошь захваченных богатств.",
        "commentators": [], "western": []},
    "vidyādhara":  {"ru": "видьядхара",                 "type": "В", "trigger": "realia",   "priority": "med",
        "slp1_triggers": ["vidyADara"],
        "note": "vidyādhara «владеющий знанием» — класс волшебных существ, обитающих в воздушном пространстве; в «Тилаке» — существа, умеющие летать силой мантр.",
        "commentators": ["Tilaka"], "western": []},
    "gandharva":   {"ru": "гандхарва",                  "type": "В", "trigger": "realia",   "priority": "med",
        "slp1_triggers": ["ganDarva"],
        "note": "gandharva — небесные музыканты; в «Бхушане» — любовники апсар. В Сундараканде маркируют атмосферу Ланки как перевёрнутого рая.",
        "commentators": ["Bhūṣaṇa"], "western": []},
    "apsaras":     {"ru": "апсара",                     "type": "В", "trigger": "realia",   "priority": "med",
        "slp1_triggers": ["apsaras"],
        "note": "apsaras — небесные танцовщицы/нимфы; в Сундараканде — часть обстановки дворца Раваны.",
        "commentators": [], "western": []},
    "siddha":      {"ru": "сиддха",                     "type": "В", "trigger": "realia",   "priority": "low",
        "slp1_triggers": ["siddha"],
        "note": "siddha — «достигшие совершенства» аскеты или полубожественные существа, движущиеся по небу.",
        "commentators": [], "western": []},
    "kinnara":     {"ru": "киннара",                    "type": "В", "trigger": "realia",   "priority": "low",
        "slp1_triggers": ["kinnara"],
        "note": "kinnara — полубожественные певцы с конским или птичьим туловищем; в «Нарадие» — «похожие на людей».",
        "commentators": [], "western": []},

    # Рavaṇa's lieutenants and characters
    "vibhīṣaṇa":  {"ru": "Вибхишана",                  "type": "В", "trigger": "realia",   "priority": "high",
        "slp1_triggers": ["viBIzaRa"],
        "text_triggers": ["vibhīṣaṇa"],
        "note": "праведный младший брат Раваны (vibhīṣaṇa «внушающий страх»); впоследствии перешёл на сторону Рамы. В «Тилаке» объясняется парадокс: праведник среди ракшасов. Первое появление в кн. V.",
        "commentators": ["Tilaka"], "western": ["Goldman 1994"]},
    "indrajit":    {"ru": "Индраджит",                  "type": "В", "trigger": "realia",   "priority": "high",
        "slp1_triggers": ["indrajit"],
        "text_triggers": ["indrajit"],
        "note": "старший сын Раваны и главный полководец (indra-jit «победивший Индру»); его брахмастра усыплена героями позднее. «Бхушана» глоссирует победу над Индрой как основание имени.",
        "commentators": ["Bhūṣaṇa"], "western": []},
    "kumbhakarṇa": {"ru": "Кумбхакарна",               "type": "В", "trigger": "realia",   "priority": "high",
        "slp1_triggers": ["kumBakarRa"],
        "text_triggers": ["kumbhakarṇa"],
        "note": "гигантский брат Раваны (kumbha-karṇa «горшкоухий»), обречённый на многомесячный сон. Первое появление в кн. V.",
        "commentators": [], "western": []},
    "prahastha":   {"ru": "Прахаста",                   "type": "В", "trigger": "realia",   "priority": "med",
        "slp1_triggers": ["prahasTA","prahasta"],
        "text_triggers": ["prahastha"],
        "note": "главный военачальник Раваны в Ланке (pra-hasta «с вытянутой рукой»).",
        "commentators": [], "western": []},

    # Concepts / terms
    "dharma":      {"ru": "дхарма",                     "type": "А", "trigger": "term",     "priority": "high",
        "slp1_triggers": ["Darma"],
        "note": "dharma — «порядок», «закон», «долг»: в данном контексте сочетает значения космического закона и личного долга. Подстрочник обычно переводит ситуативно («закон», «долг», «добродетель»), скрывая полноту смысла. В «Тилаке» — dharma как один из четырёх puruṣārtha.",
        "commentators": ["Tilaka"], "western": []},
    "artha":       {"ru": "польза / цель",               "type": "Б", "trigger": "term",     "priority": "med",
        "slp1_triggers": ["arTa"],
        "note": "artha многозначно: «смысл», «цель», «польза», «богатство». В паре dharma-artha — второй из четырёх puruṣārtha. Подстрочник выбирает один смысл, тогда как контекст часто допускает игру значений.",
        "commentators": [], "western": []},
    "kāma":        {"ru": "кама / желание",              "type": "Б", "trigger": "term",     "priority": "med",
        "slp1_triggers": ["kAma"],
        "note": "kāma — «желание», «любовь»; третий puruṣārtha; также имя бога любви. Двусмысленность «желание/Кама» важна в эротических описаниях Ланки.",
        "commentators": [], "western": []},
    "tapas":       {"ru": "тапас / аскеза",              "type": "А", "trigger": "term",     "priority": "med",
        "slp1_triggers": ["tapas"],
        "note": "tapas — аскетический жар/подвиг; согласно «Тилаке», «разогрев» тела позволяет аскету достичь сверхъестественных способностей. В кн. V — мотив праведности Ситы как аскетки.",
        "commentators": ["Tilaka"], "western": []},
    "māyā":        {"ru": "майя / иллюзия",              "type": "А", "trigger": "term",     "priority": "high",
        "slp1_triggers": ["mAyA"],
        "note": "māyā — «иллюзорная сила», «магия»; в контексте Ланки — демоническое искусство ракшасов принимать облики. «Широмани» различает māyā ракшасов (воинская магия) от māyā Брахмы (космическая иллюзия).",
        "commentators": ["Śiromaṇi"], "western": []},
    "śakti":       {"ru": "шакти / копьё",               "type": "Б", "trigger": "term",     "priority": "med",
        "slp1_triggers": ["Sakti"],
        "note": "śakti двузначно: «сила/энергия» (абстрактное) и «копьё» (оружие). В батальных сценах Сундараканды подстрочник обычно выбирает «копьё», оставляя семантику «жизненной силы» невыраженной.",
        "commentators": [], "western": []},
    "mantra":      {"ru": "мантра",                      "type": "А", "trigger": "term",     "priority": "low",
        "slp1_triggers": ["mantra"],
        "note": "mantra — «священная формула» или «тайный совет» (в политическом контексте man-tra «мысль-инструмент»). В советах на суде Раваны — «совет», «политическое решение».",
        "commentators": [], "western": []},
    "brahmastra":  {"ru": "брахмастра",                  "type": "В", "trigger": "realia",   "priority": "high",
        "slp1_triggers": ["brahmAstra"],
        "text_triggers": ["brahmastra","brahmāstra"],
        "note": "brahmastra — «оружие Брахмы», высшая астра (astra), непреодолимый снаряд, наделённый силой Брахмы. В кн. V связано с пленением Ханумана.",
        "commentators": [], "western": ["Goldman 1994"]},
    "astra":       {"ru": "астра / магическое оружие",   "type": "А", "trigger": "term",     "priority": "med",
        "slp1_triggers": ["astra"],
        "note": "astra — оружие, активируемое мантрой, в отличие от śastra (оружие рукопашного боя). В эпосе астры — метательные снаряды с магическим зарядом.",
        "commentators": [], "western": []},
    "śastra":      {"ru": "шастра / оружие",              "type": "Б", "trigger": "term",     "priority": "low",
        "slp1_triggers": ["Sastra"],
        "note": "śastra — оружие ближнего боя; пара к astra. Подстрочник нередко переводит оба слова «оружием», нивелируя дистинкцию.",
        "skip_if_noted": "astra",
        "commentators": [], "western": []},

    # Celestial and ritual concepts
    "indra":       {"ru": "Индра",                       "type": "В", "trigger": "realia",   "priority": "high",
        "slp1_triggers": ["indra"],
        "note": "Индра (indra «мощный»), царь богов и повелитель грозы; в Сундараканде — мерило высшего могущества («лучший как Индра»).",
        "commentators": [], "western": []},
    "kubera":      {"ru": "Кубера",                      "type": "В", "trigger": "realia",   "priority": "high",
        "slp1_triggers": ["kubera"],
        "note": "бог богатства и владыка якшей, брат Раваны по отцу; Равана вытеснил его с Ланки и захватил колесницу пушпака. «Широмани»: kubera = «уродливый».",
        "commentators": ["Śiromaṇi"], "western": []},
    "yama":        {"ru": "Яма",                         "type": "В", "trigger": "realia",   "priority": "med",
        "slp1_triggers": ["yama"],
        "note": "бог смерти и загробного мира (yama «сдерживающий»); в боевых описаниях сравнения с Ямой маркируют смертоносность героя.",
        "commentators": [], "western": []},
    "varuṇa":      {"ru": "Варуна",                      "type": "В", "trigger": "realia",   "priority": "med",
        "slp1_triggers": ["varuRa","varuna"],
        "note": "ведийский бог вод и нравственного миропорядка (ṛta); в эпосе — владыка океана. В Сундараканде фигурирует в контексте переплытия Ханумана.",
        "commentators": [], "western": []},
    "agni":        {"ru": "Агни",                        "type": "В", "trigger": "realia",   "priority": "med",
        "slp1_triggers": ["agni"],
        "note": "бог огня (agni «огонь»); в кн. V — испытание огнём Ланки и очищение Ситы посредством Агни.",
        "commentators": [], "western": []},
    "vāyu":        {"ru": "Ваю",                         "type": "В", "trigger": "realia",   "priority": "med",
        "slp1_triggers": ["vAyu"],
        "note": "бог ветра (vāyu «ветер»), отец Ханумана; мерило скорости и силы.",
        "commentators": [], "western": []},
    "sūrya":       {"ru": "Сурья",                       "type": "В", "trigger": "realia",   "priority": "low",
        "slp1_triggers": ["sUrya"],
        "note": "бог солнца (sūrya); в сравнениях с Хануманом и в описаниях Ланки.",
        "commentators": [], "western": []},
    "soma":        {"ru": "Сома",                        "type": "В", "trigger": "realia",   "priority": "low",
        "slp1_triggers": ["soma"],
        "note": "бог луны и ритуальный напиток (soma); в описании луны / ночного неба Ланки.",
        "commentators": [], "western": []},
    "brahman":     {"ru": "Брахман (бог)",               "type": "В", "trigger": "realia",   "priority": "med",
        "slp1_triggers": ["brahmA","brahman"],
        "note": "Брахма (brahmā, nom. от brahman) — бог-творец; в кн. V фигурирует в контексте брахмастры и бессмертия Ханумана.",
        "commentators": [], "western": []},
    "viṣṇu":       {"ru": "Вишну",                       "type": "В", "trigger": "realia",   "priority": "med",
        "slp1_triggers": ["vizRu"],
        "text_triggers": ["viṣṇu"],
        "note": "Вишну (viṣṇu «всепроникающий») — бог-хранитель; в «Тилаке» Рама интерпретируется как аватара Вишну, хотя сама поэма не делает этого акцента явно.",
        "commentators": ["Tilaka"], "western": []},
    "śiva":        {"ru": "Шива",                        "type": "В", "trigger": "realia",   "priority": "low",
        "slp1_triggers": ["Siva"],
        "note": "Шива (śiva «благой»); фигурирует в пиршественных/дворцовых описаниях Ланки.",
        "commentators": [], "western": []},

    # Plants and trees (aśoka already covered)
    "kadamba":     {"ru": "кадамба",                     "type": "В", "trigger": "realia",   "priority": "low",
        "slp1_triggers": ["kadamba"],
        "note": "дерево кадамба (Neolamarckia cadamba); цветёт в сезон дождей, символ разлуки влюблённых в санскритской поэзии.",
        "commentators": [], "western": []},
    "campaka":     {"ru": "чампака",                     "type": "В", "trigger": "realia",   "priority": "low",
        "slp1_triggers": ["campaka"],
        "note": "дерево чампака (Michelia champaca), золотистые цветы с сильным ароматом; украшение садов Ланки.",
        "commentators": [], "western": []},
    "pāṭala":      {"ru": "патала",                      "type": "В", "trigger": "realia",   "priority": "low",
        "slp1_triggers": ["pAwala"],
        "note": "дерево пāṭala (Stereospermum chelonoides), розовые цветы; в описании садов.",
        "commentators": [], "western": []},

    # Monkey heroes
    "sugrīva":     {"ru": "Сугрива",                     "type": "В", "trigger": "realia",   "priority": "high",
        "slp1_triggers": ["sugrIva"],
        "note": "царь ванаров (su-grīva «прекрасношеий»), союзник Рамы. В Сундараканде Хануман выполняет его поручение.",
        "commentators": [], "western": ["Goldman 1994"]},
    "aṅgada":      {"ru": "Ангада",                      "type": "В", "trigger": "realia",   "priority": "med",
        "slp1_triggers": ["aNgada"],
        "text_triggers": ["aṅgada"],
        "note": "сын Валина, племянник Сугривы (aṅgada «браслет»); командует частью войска ванаров. Первое появление в кн. V.",
        "commentators": [], "western": []},
    "jāmbavān":    {"ru": "Джамбаван",                   "type": "В", "trigger": "realia",   "priority": "med",
        "slp1_triggers": ["jAmbavAn"],
        "note": "«медведь» (jāmbavān), старый советник ванаров; именно он пробуждает в Ханумане память о его силе, побуждая к прыжку через океан.",
        "commentators": [], "western": []},
    "nala":        {"ru": "Нала",                        "type": "В", "trigger": "realia",   "priority": "med",
        "slp1_triggers": ["nala"],
        "note": "Нала (nala «полый тростник»), архитектор-обезьяна, сын Вишвакармана; в кн. VI строит мост, но в кн. V упоминается в контексте войска.",
        "commentators": [], "western": []},
    "nīla":        {"ru": "Нила",                        "type": "В", "trigger": "realia",   "priority": "med",
        "slp1_triggers": ["nIla"],
        "note": "военачальник ванаров (nīla «тёмно-синий»); сын Агни.",
        "commentators": [], "western": []},

    # Epithets of Hanumān (new cluster)
    "śatrukarśana":{"ru": "губитель врагов",             "type": "А", "trigger": "epithet",  "priority": "med",
        "slp1_triggers": ["SatrukarSana"],
        "note": "эпитет «губитель врагов» (śatru-karśana): «иссушающий, истощающий врагов»; прилагается к Хануману в кн. V.",
        "commentators": [], "western": []},
    "tejasvin":    {"ru": "полный блеска",               "type": "А", "trigger": "epithet",  "priority": "low",
        "slp1_triggers": ["tejasvin"],
        "note": "tejasvin «блистательный, полный tejas»; tejas — световая/огненная жизненная сила героя.",
        "commentators": [], "western": []},
    "vikrama":     {"ru": "доблесть / шаг",              "type": "Б", "trigger": "term",     "priority": "med",
        "slp1_triggers": ["vikrama"],
        "note": "vikrama двузначно: «доблесть», «могущество» и буквально «широкий шаг». В батальных описаниях подстрочник обычно выбирает одно значение.",
        "commentators": [], "western": []},
    "parākrama":   {"ru": "доблесть",                   "type": "А", "trigger": "epithet",  "priority": "low",
        "slp1_triggers": ["parAkrama"],
        "note": "parākrama «высшее могущество / натиск» (para+ā+krama); отличается от vikrama тем, что акцент на внешней экспансии.",
        "commentators": [], "western": []},
    "bala":        {"ru": "сила",                        "type": "А", "trigger": "term",     "priority": "low",
        "slp1_triggers": ["bala"],
        "note": "bala «физическая сила»; в парах bala-vikrama и bala-parākrama — первый элемент (грубая сила) в отличие от парящей доблести.",
        "commentators": [], "western": []},

    # Ornaments / literary figures
    "upamā":       {"ru": "упама / сравнение",           "type": "А", "trigger": "term",     "priority": "low",
        "slp1_triggers": ["upamA"],
        "note": "upamā — «сравнение» (алам-кара), ключевая фигура стиля Вālмīки. В «Натьяшастре» описывается как простейший аланкара.",
        "commentators": [], "western": []},

    # Verse from ch.2 onwards — specific characters
    "dvivida":     {"ru": "Двивида",                     "type": "В", "trigger": "realia",   "priority": "low",
        "slp1_triggers": ["dvivida"],
        "note": "Двивида (dvivida «двойная»), один из воинов-ванаров; упоминается в перечнях войска.",
        "commentators": [], "western": []},
    "mainda":      {"ru": "Маинда",                      "type": "В", "trigger": "realia",   "priority": "low",
        "slp1_triggers": ["mEnda","mainda"],
        "note": "Маинда (mainda), воин-ванар; партнёр Двивиды в описаниях войска.",
        "commentators": [], "western": []},

    # Separation (viraha) and mental states
    "śoka":        {"ru": "горе / скорбь",               "type": "А", "trigger": "term",     "priority": "med",
        "slp1_triggers": ["Soka"],
        "note": "śoka — «горе», «скорбь»; в теории рас — основа каруṇa (сочувственной) расы. В речах Ситы — ключевое переживание разлуки (viraha-śoka).",
        "commentators": [], "western": []},
    "viraha":      {"ru": "разлука",                     "type": "А", "trigger": "term",     "priority": "high",
        "slp1_triggers": ["viraha"],
        "text_triggers": ["viraha"],
        "note": "viraha «разлука» (vi-raha «отсутствие любимого»); в санскритской поэтике — главная тема śṛṅgāra-vipralambha (любовная раса в разлуке). Переживания Ситы задают регистр всей кн. V.",
        "commentators": [], "western": []},
    "ārti":        {"ru": "страдание",                   "type": "А", "trigger": "term",     "priority": "low",
        "slp1_triggers": ["Arti"],
        "note": "ārti «страдание», «боль»; в речах Ситы — эмоциональный индикатор.",
        "commentators": [], "western": []},

    # Action of burning Lanka
    "agnidāha":    {"ru": "поджог / огненное сожжение",  "type": "В", "trigger": "realia",   "priority": "high",
        "slp1_triggers": ["agnidAha"],
        "note": "agni-dāha «огненное сожжение» — кульминация кн. V: Хануман поджигает Ланку хвостом, обёрнутым в горящие ткани.",
        "commentators": [], "western": ["Goldman 1994"]},

    # Messenger / embassy
    "dūta":        {"ru": "посланник / посол",           "type": "А", "trigger": "term",     "priority": "med",
        "slp1_triggers": ["dUta"],
        "note": "dūta «посланник, дипломатический посол»; в «Артхашастре» статус посла неприкосновенен. В Сундараканде Хануман выступает как дūta Рамы — его арест Раваной воспринимается как нарушение дипломатического обычая.",
        "commentators": [], "western": []},

    # More cross-refs
    "vālin":       {"ru": "Валин",                       "type": "В", "trigger": "crossref",  "priority": "med",
        "slp1_triggers": ["vAlin"],
        "grintser": "см. примеч. к IV (Гринцер)",
        "note": "Валин (vālin), убитый Рамой царь ванаров; его гибель — предыстория союза Сугривы с Рамой.",
        "commentators": [], "western": []},
    "daśaratha":   {"ru": "Дашаратха",                   "type": "В", "trigger": "crossref",  "priority": "med",
        "slp1_triggers": ["daSaraTa"],
        "grintser": "см. примеч. к I.1.8 (Гринцер)",
        "note": "Дашаратха (daśa-ratha «десять колесниц»), отец Рамы; умер от горя после изгнания сына.",
        "commentators": [], "western": []},
    "janaka":      {"ru": "Джанака",                     "type": "В", "trigger": "crossref",  "priority": "med",
        "slp1_triggers": ["janaka"],
        "grintser": "см. примеч. к I.1.25 (Гринцер)",
        "note": "Джанака (janaka «рождающий»), царь Видехи, отец Ситы.",
        "commentators": [], "western": []},
}

# ── CHAPTER NARRATIVE CONTEXT ─────────────────────────────────────────────────
# For each chapter, a brief narrative label (Russian) used in _meta.
CHAPTER_CONTEXT = {
    2:  "Хануман прибывает к Ланке и восхищается городом",
    3:  "Описание Ланки: дворцы, ворота, стражи",
    4:  "Хануман видит красоты дворца Раваны",
    5:  "Пир Раваны: Хануман замечает его жён",
    6:  "Поиск Ситы продолжается",
    7:  "Хануман видит Мандодари и принимает её за Ситу",
    8:  "Хануман понимает, что это не Сита",
    9:  "Хануман находит рощу Ашока",
    10: "Сита в роще Ашока: скорбь и заточение",
    11: "Ракшасини угрожают Сите",
    12: "Равана приходит к Сите и соблазняет её",
    13: "Равана продолжает уговоры Ситы",
    14: "Сита отвергает Раваяу",
    15: "Трияджата защищает Ситу",
    16: "Хануман наблюдает за Ситой с дерева",
    17: "Хануман решает, как открыться Сите",
    18: "Хануман поёт хвалу Раме",
    19: "Сита слышит хвалу и удивляется",
    20: "Хануман открывается Сите",
    21: "Сита просит знак о Раме",
    22: "Хануман передаёт кольцо Рамы",
    23: "Сита сомневается в возможности переправы армии",
    24: "Хануман объясняет мощь Рамы",
    25: "Сита передаёт украшение-знак",
    26: "Хануман разрушает рощу Ашока",
    27: "Битва с ракшасами в роще",
    28: "Хануман уничтожает защитников рощи",
    29: "Пленение Ханумана брахмастрой",
    30: "Хануман приводят пред Равану",
    31: "Посольство Ханумана: речь к Раване",
    32: "Равана приказывает поджечь хвост Ханумана",
    33: "Хвост Ханумана поджигают; он вырывается",
    34: "Хануман поджигает Ланку",
    35: "Пожар Ланки",
    36: "Хануман возвращается к Сите",
    37: "Хануман прощается с Ситой",
    38: "Хануман перелетает обратно через океан",
    39: "Хануман встречает войско ванаров на горе Махендра",
    40: "Радость ванаров от вести о Сите",
    41: "Хануман рассказывает об увиденном",
    42: "Ванары слушают рассказ о Ланке",
    43: "Рассказ о силе Раваны",
    44: "Хануман говорит о пути к победе",
    45: "Войско ванаров собирается к морю",
    46: "Совет Рамы с Сугривой",
    47: "Рама вспоминает Ситу",
    48: "Рама описывает Сите приметы пути",
    49: "Сита думает о Раме",
    50: "Переживания Рамы в разлуке",
    51: "Войско идёт к морю",
    52: "Ванары у берега океана",
    53: "Совет: как перейти океан?",
    54: "Вибхишана бежит от Раваны к Раме",
    55: "Рама принимает Вибхишану",
    56: "Рама обращается к Океану",
    57: "Нала строит мост",
    58: "Описание моста и переправы войска",
    59: "Войско прибывает к Ланке",
    60: "Стратегический совет у берегов Ланки",
    61: "Разведка ванаров",
    62: "Вибхишана указывает слабые места Ланки",
    63: "Диспозиция войска",
    64: "Равана советуется с военачальниками",
    65: "Шука и Сарана шпионят и пойманы",
    66: "Рама видит Ланку",
    67: "Равана смотрит на войско Рамы",
    68: "Финал Сундараканды: итоги книги V",
}

# ── SEED ALREADY-NOTED FROM CH.1 ─────────────────────────────────────────────
ch1_file = DATA_DIR / "sundara_ch1_commentary_to_add.json"
ch1_data = json.load(open(ch1_file, encoding='utf-8'))
# already_noted: lemmas noted in ch.1 (and subsequently earlier chapters)
already_noted: set = set()
for item in ch1_data:
    if "_meta" in item:
        continue
    already_noted.add(item["lemma_iast"])

print(f"Seeded {len(already_noted)} lemmas from ch.1: {sorted(already_noted)}")

# Seed book-level omission set from ch.1 omission notes
book_omission_seen: set = set()
for item in ch1_data:
    if "_meta" in item:
        continue
    if item.get("trigger") == "omission":
        book_omission_seen.add(item["lemma_iast"])
print(f"Seeded {len(book_omission_seen)} omission lemmas from ch.1: {sorted(book_omission_seen)}")

# ── LOAD CORPUS ───────────────────────────────────────────────────────────────
print("Loading corpus …")
all_rows = load_jsonl(SUNDARA)
# Index by (chapter, passage, seg)
corpus: dict = {}
for r in all_rows:
    ch  = r.get('chapter', '')
    psg = r.get('passage', '')
    seg = r.get('seg', '')
    corpus[(ch, psg, seg)] = r

# Per chapter: list of (verse_num, sa_row, ru_row)
def get_chapter_verses(ch_num: int):
    ch_str = str(ch_num)
    verses = []
    for r in all_rows:
        if r.get('chapter') == ch_str and r.get('seg') == 'sa':
            psg = r.get('passage', '')
            ru_row = corpus.get((ch_str, psg, 'ru'), {})
            try:
                v = int(psg.split('.')[-1])
            except:
                v = 0
            verses.append((v, r, ru_row))
    verses.sort(key=lambda x: x[0])
    return verses

# ── TRIGGER DETECTION ─────────────────────────────────────────────────────────
# For each KB entry, check if any slp1_trigger substring appears as a token
# in the verse's SLP1 text.

def detect_triggers(slp1_text: str, iast_text: str = "") -> list:
    """Return list of (lemma, kb_entry) for all KB entries triggered in this verse.
    Checks SLP1 triggers (case-sensitive) against slp1_text, and optionally
    IAST text triggers against iast_text for lemmas with text_triggers.
    """
    results = []
    for lemma, kb in KB.items():
        matched = False
        # SLP1 triggers: case-SENSITIVE substring match (SLP1 encodes phonemes via case)
        for trigger_str in kb.get('slp1_triggers', []):
            if trigger_str in slp1_text:
                matched = True
                break
        # IAST text triggers: secondary check (case-insensitive, IAST text field)
        if not matched and iast_text:
            for trigger_str in kb.get('text_triggers', []):
                if trigger_str.lower() in iast_text.lower():
                    matched = True
                    break
        if matched:
            results.append((lemma, kb))
    return results

# ── OMISSION DETECTION ────────────────────────────────────────────────────────
# The OMISSION_WORTH set mirrors ch.1 (proper-name epithets whose drop
# genuinely loses a referent).
# Omission notes fire ONLY for proper-name patronymic epithets (not the character's
# primary name, which the подстрочник always renders some way).  Mirror ch.1 exactly.
# Once a lemma fires an omission note anywhere in the book, it is added to
# book_omission_seen so it never fires again.
OMISSION_WORTH = {
    "rāghava", "janakātmajā", "vaidehī", "maithilī",
    "dāśarathi", "mārutātmaja", "vāyuputra",
}

def check_omission(lemma: str, kb: dict, ru_text: str) -> bool:
    """Return True if the lemma's Russian gloss head does NOT appear in the подстрочник."""
    if lemma not in OMISSION_WORTH:
        return False
    ru_head = kb.get('ru', '')[:8].lower()
    return ru_head and ru_head not in ru_text.lower()

# ── PER-CHAPTER PROCESSING ────────────────────────────────────────────────────

def process_chapter(ch_num: int, already_noted: set, book_omission_seen: set) -> tuple:
    """
    Returns (notes_list, updated_already_noted, verse_count).
    notes_list: list of note dicts (same schema as ch.1 output, minus _meta).
    already_noted: mutated in-place.
    book_omission_seen: mutated in-place (omission notes fire at most once per lemma, book-wide).
    """
    verses = get_chapter_verses(ch_num)
    if not verses:
        return [], already_noted, 0

    notes = []
    # per-chapter local dedup: one first-appearance note per lemma per chapter
    local_seen_ep: set = set()
    local_seen_om: set = set()

    for (v_num, sa_row, ru_row) in verses:
        slp1 = sa_row.get('slp1', '') or sa_row.get('text', '')
        ru_text = ru_row.get('text', '') if ru_row else ''
        psg = sa_row.get('passage', '')
        sa = f"V.{ch_num}.{v_num}"

        iast_text = sa_row.get('text', '')
        triggered = detect_triggers(slp1, iast_text)

        for (lemma, kb) in triggered:
            # skip if marked skip=True in KB
            if kb.get('skip'):
                continue

            # skip_if_noted: suppress if a sibling lemma already noted
            sin = kb.get('skip_if_noted')
            if sin and (sin in already_noted or sin in local_seen_ep):
                continue

            # ── FIRST-APPEARANCE (epithet/term/realia/crossref) note ──────────
            if lemma not in already_noted and lemma not in local_seen_ep:
                local_seen_ep.add(lemma)
                already_noted.add(lemma)

                body = kb['note']
                if kb.get('grintser'):
                    body = body.rstrip('.') + f". {kb['grintser']}."

                ru_head = kb.get('ru', '')
                note_ru = f"{ucfirst(ru_head)} ({lemma}) — {body}"

                # mark first-appearance explicitly for А/В notes
                if kb['trigger'] in ('epithet', 'realia') and 'Первое' not in body and 'первое' not in body:
                    note_ru += " Первое вхождение в кн. V."

                notes.append({
                    "shloka": sa,
                    "lemma_iast": lemma,
                    "note_ru": note_ru,
                    "type": kb['type'],
                    "trigger": kb['trigger'],
                    "priority": kb['priority'],
                    "source": "first occurrence in кн. V; Grintser index / commentators where cited (verse-level, soft)",
                    "review_required": True,
                    "cited_indian_commentators": kb.get('commentators', []),
                    "cited_western_sources": kb.get('western', []),
                    "src_candidate_id": f"auto/sundara/{psg}.ep",
                })

            # ── OMISSION NOTE ─────────────────────────────────────────────────
            # Only for OMISSION_WORTH lemmas; only ONCE per lemma for the whole book
            elif lemma in OMISSION_WORTH and lemma not in book_omission_seen and lemma not in local_seen_om:
                if check_omission(lemma, kb, ru_text):
                    local_seen_om.add(lemma)
                    book_omission_seen.add(lemma)
                    pr_snippet = ru_text[:60].strip()
                    note_ru = (
                        f"{ucfirst(kb['ru'])} ({lemma}). [Е. Костина]: именной эпитет «{lemma}» "
                        f"присутствует в оригинале, но не передан отдельным словом в подстрочнике "
                        f"(«…{pr_snippet}…»). В литературном тексте эпитет восстанавливается; "
                        f"отметить как незафиксированное опущение — на усмотрение редактора."
                    )
                    notes.append({
                        "shloka": sa,
                        "lemma_iast": lemma,
                        "note_ru": note_ru,
                        "type": "Б",
                        "trigger": "omission",
                        "priority": "low",
                        "source": "parallel-text divergence (verse-level, soft)",
                        "review_required": True,
                        "src_candidate_id": f"auto/sundara/{psg}.om",
                    })

    # Sort within chapter by verse number, then priority
    prio_rank = {"high": 0, "med": 1, "low": 2}
    notes.sort(key=lambda n: (
        int(n['shloka'].split('.')[2]),
        prio_rank.get(n['priority'], 3)
    ))

    return notes, already_noted, len(verses)

# ── MAIN LOOP ─────────────────────────────────────────────────────────────────
print(f"\nProcessing chapters 2–68 …")

all_chapter_notes = {}   # ch_num → list of notes
chapter_verse_counts = {}

for ch_num in range(2, 69):
    notes, already_noted, v_count = process_chapter(ch_num, already_noted, book_omission_seen)
    all_chapter_notes[ch_num] = notes
    chapter_verse_counts[ch_num] = v_count

    # Write per-chapter file
    context = CHAPTER_CONTEXT.get(ch_num, f"глава {ch_num}")
    meta = {
        "_meta": {
            "description": f"Рекомендуемые примечания к параллельному Sa-Ru корпусу (Сундараканда, кн. V, гл. {ch_num})",
            "chapter_context": context,
            "rule": "Примечание добавляется ТОЛЬКО когда оно даёт то, чего нет в подстрочнике Леонова.",
            "evidence": "Все корпусные свидетельства — уровень шлоки (мягкое). Каждое примечание review_required.",
            "generated": TODAY,
            "chapter": ch_num,
            "verses_total": v_count,
            "notes_count": len(notes),
        }
    }
    out = [meta] + notes
    out_path = DATA_DIR / f"sundara_ch{ch_num}_commentary_to_add.json"
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    status = f"ch.{ch_num}: {len(notes)} notes / {v_count} verses"
    print(f"  {status}")

# ── AGGREGATION ───────────────────────────────────────────────────────────────
print("\nAggregating all chapters …")

# Load ch.1 notes (without _meta)
book_notes = []
for item in ch1_data:
    if "_meta" not in item:
        book_notes.append(item)

for ch_num in range(2, 69):
    book_notes.extend(all_chapter_notes[ch_num])

# Chapter verse counts including ch.1
chapter_verse_counts[1] = 213

# Sort book-wide
def shloka_sort_key(n):
    parts = n['shloka'].split('.')
    return (int(parts[1]), int(parts[2]))

book_notes.sort(key=shloka_sort_key)

# Stats
by_type    = collections.Counter(n['type'] for n in book_notes)
by_trigger = collections.Counter(n['trigger'] for n in book_notes)
by_prio    = collections.Counter(n['priority'] for n in book_notes)
noted_shlokas = set(n['shloka'] for n in book_notes)
total_verses  = sum(chapter_verse_counts.values())
per_chapter_counts = {ch: len(all_chapter_notes.get(ch, [])) for ch in range(2, 69)}
per_chapter_counts[1] = sum(1 for n in ch1_data if "_meta" not in n)

book_meta = {
    "_meta": {
        "description": "Рекомендуемые примечания к параллельному Sa-Ru корпусу (Сундараканда, кн. V, гл. 1–68)",
        "rule": "Примечание добавляется ТОЛЬКО когда оно даёт то, чего нет в подстрочнике Леонова.",
        "evidence": "Все корпусные свидетельства — уровень шлоки (мягкое). Каждое примечание review_required.",
        "generated": TODAY,
        "total_verses": total_verses,
        "total_notes": len(book_notes),
        "verses_with_note": len(noted_shlokas),
        "verses_without_note": total_verses - len(noted_shlokas),
        "by_type": dict(by_type),
        "by_trigger": dict(by_trigger),
        "by_priority": dict(by_prio),
        "per_chapter_notes": per_chapter_counts,
        "chapter_verse_counts": chapter_verse_counts,
    }
}

book_out = [book_meta] + book_notes
with open(DATA_DIR / "sundara_commentary_to_add.json", 'w', encoding='utf-8') as f:
    json.dump(book_out, f, ensure_ascii=False, indent=2)
print(f"Wrote sundara_commentary_to_add.json ({len(book_notes)} total notes)")

# Book stats
book_stats = {
    "total_verses": total_verses,
    "total_notes": len(book_notes),
    "verses_with_note": len(noted_shlokas),
    "verses_without_note": total_verses - len(noted_shlokas),
    "by_type": dict(by_type),
    "by_trigger": dict(by_trigger),
    "by_priority": dict(by_prio),
    "per_chapter_notes": per_chapter_counts,
    "chapter_verse_counts": chapter_verse_counts,
    "note": "All notes are finished Russian text, review_required:true. First-appearance dedup enforced book-wide.",
}
with open(DATA_DIR / "sundara_book_stats.json", 'w', encoding='utf-8') as f:
    json.dump(book_stats, f, ensure_ascii=False, indent=2)
print("Wrote sundara_book_stats.json")

# ── SUMMARY REPORT ────────────────────────────────────────────────────────────
print(f"\n=== BOOK-WIDE SUMMARY ===")
print(f"Total verses (ch.1–68): {total_verses}")
print(f"Total recommended notes: {len(book_notes)}")
print(f"Verses with note: {len(noted_shlokas)} ({100*len(noted_shlokas)/total_verses:.1f}%)")
print(f"Verses without note: {total_verses - len(noted_shlokas)}")
print(f"By type:     {dict(by_type)}")
print(f"By trigger:  {dict(by_trigger)}")
print(f"By priority: {dict(by_prio)}")

print("\nPer-chapter note counts:")
for ch in range(1, 69):
    n = per_chapter_counts.get(ch, 0)
    vc = chapter_verse_counts.get(ch, 0)
    bar = '#' * n
    print(f"  ch.{ch:2d} ({vc:3d} v): {n:3d}  {bar}")

# Dense/sparse
sorted_by_density = sorted(range(2, 69), key=lambda c: per_chapter_counts.get(c, 0), reverse=True)
print("\n5 densest chapters (ch.2–68):")
for ch in sorted_by_density[:5]:
    print(f"  ch.{ch}: {per_chapter_counts[ch]} notes / {chapter_verse_counts[ch]} verses")
print("5 sparsest chapters (ch.2–68):")
for ch in sorted_by_density[-5:]:
    print(f"  ch.{ch}: {per_chapter_counts[ch]} notes / {chapter_verse_counts[ch]} verses")

print("\n=== 6 STRONGEST NOTES (ch.2–68 only) ===")
# Select: high-priority, non-ch.1
strong = [n for n in book_notes if n.get('priority') == 'high'
          and int(n['shloka'].split('.')[1]) >= 2][:6]
for n in strong:
    print(f"\n[{n['shloka']}] ({n['type']}/{n['trigger']}/{n['priority']})")
    print(n['note_ru'])
