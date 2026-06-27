"""
crosstext_mbh_battle_build.py

Build the curated cross-text note set linking the MBh battle parvans
(Bhīṣma/Droṇa/Karṇa/Śalya/Sauptika) to the Sundarakāṇḍa, focus = military realia.

Every (source_addr, sundara_addr) pairing below was located by mining shared
SLP1 militaria stems (see crosstext_mbh_battle.py) and then hand-verified.
Here we re-pull the EXACT #sa + #ru of both ends from the corpus so the quoted
text is faithful, and assemble the note objects.

Output: data/crosstext/mbh_battle.json
"""
import sys, json, os
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CS_DIR     = Path(r"C:\Users\user\Documents\GitHub\CommentaryStrategies")
OUT_DIR    = CS_DIR / "data" / "crosstext"
CORPUS_DIR = Path(r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl")

FILES = {
    "Bhīṣmaparva":   "06_mahabharata-bhishmaparva.jsonl",
    "Droṇaparva":    "07_mahabharata-dronaparva.jsonl",
    "Karṇaparva":    "08_mahabharata-karnaparva.jsonl",
    "Śalyaparva":    "09_mahabharata-shalyaparva.jsonl",
    "Sauptikaparva": "10_mahabharata-sauptikaparva.jsonl",
    "Sundara":       "05_ramayana-sundarakanda.jsonl",
}

def load(fn):
    out = {}
    with open(CORPUS_DIR / fn, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            o = json.loads(line)
            r = out.setdefault(o["passage"], {})
            if o["seg"] == "sa":
                r["sa"] = o.get("text", "")
            elif o["seg"] == "ru":
                r["ru"] = o.get("text", "")
    return out

CORP = {k: load(v) for k, v in FILES.items()}

def sa(work, p):  return CORP[work].get(p, {}).get("sa", "")
def ru(work, p):  return CORP[work].get(p, {}).get("ru", "")

# ── curated parallels ────────────────────────────────────────────────────────
# Each entry: sundara passage, source work+passage, shared stem, lemma, type,
# and the Russian commentary frame (the source #sa/#ru is injected verbatim).
SPECS = [
    # ---- weapon catalogue / arsenal of the rākṣasa guards ----
    dict(snd="42.28", work="Śalyaparva", src="9.59.1-2", stem="gadA", lemma="gadā",
         typ="А",
         frame="«Палица» (gadā) — главное ударное оружие эпического богатыря и фокус целой парвы: "
               "Шальяпарва кульминирует в поединке на палицах (gadāyuddha) Бхимы и Дурьодханы. "
               "В МБх Баладева назван «знатоком и искушённым в бою на палицах» (gadāyuddhaviśeṣajño "
               "gadāyuddhaviśāradaḥ). Стих Сундараканды, где ракшасы идут на Ханумана «с разнообразными "
               "палицами», помещает обезьяньего героя в ту же воинскую парадигму, где gadā — оружие "
               "первого ранга. Параллель — локус классикус технического термина."),
    dict(snd="42.28", work="Bhīṣmaparva", src="6.50.1-2", stem="gadA", lemma="gadā",
         typ="Б",
         frame="Формула «герой с палицей, словно [бог смерти] Антака с жезлом» (carantaṃ gadayā vīraṃ "
               "daṇḍapāṇim ivāntakam) прилагается в Бхишмапарве к Бхимасене. Тот же образный регистр — "
               "палиценосец как воплощение смерти — стоит за катологом палиц, обрушенных на Ханумана. "
               "Общая воинская формула, прилагаемая к сопоставимой фигуре богатыря."),
    dict(snd="42.29", work="Karṇaparva", src="8.54.15-16", stem="nArAc", lemma="nārāca",
         typ="А",
         frame="Перечень метательного оружия в руках ракшасов (дубины, трезубцы, копья, дротики, пики) "
               "типологически совпадает с эпическими «арсенальными» каталогами МБх. В Карнапарве Кришна "
               "поимённо считает запас стрел Карны — маргана, кшура, бхалла, нарача, прадарана, — что даёт "
               "локус классикус для номенклатуры наконечников. Сундараканда в 44.7 прямо называет nārāca "
               "(цельножелезную стрелу); МБх-инвентарь раскрывает её место в системе типов."),
    dict(snd="43.13", work="Karṇaparva", src="8.27.28-29", stem="paraSv", lemma="paraśvadha",
         typ="А",
         frame="«Боевой топор» (paraśvadha) в перечне оружия храмовых стражей (прасы, мечи, топоры) — "
               "часть стандартного эпического набора рукопашного оружия. Параллельные батальные парваны "
               "МБх дают тот же ассортимент в сценах, где воин «всецело полагается на свою мощь и доблесть» "
               "(svavīrye … parāśvasya), и paraśvadha регулярно соседствует с asi и prāsa. Свидетельство "
               "общей оружейной номенклатуры."),
    dict(snd="44.7", work="Karṇaparva", src="8.12.50-51", stem="nArAc", lemma="nārāca",
         typ="Б",
         frame="Ровно тот же приём — поражение врага железной стрелой nārāca в лицо / между бровей — "
               "формульно повторяется в Карнапарве: «Арджуна с силой вонзил железную стрелу между бровей "
               "(Ашваттхамана); и с этой стрелой воссиял сын Дроны, словно солнце с устремлённым ввысь "
               "лучом». Сундара 44.7 («одной стрелой, подобной полумесяцу, в лицо … десятью стрелами "
               "[поразил]») — кавья-вариация той же батальной формулы прицельного выстрела нарача."),
    # ---- army formation / vyūha ----
    dict(snd="42.27", work="Bhīṣmaparva", src="6.19.1-2", stem="vyUh", lemma="vyūha",
         typ="А",
         frame="«Боевой строй» (vyūha) — центральное понятие военной науки МБх: Бхишмапарва открывается "
               "вопросом, как Юдхиштхира «меньшим войском построился (pratyavyūhata)» против одиннадцати "
               "акшаухини, и характеризует Бхишму как «знатока человеческого, божественного, гандхарвского "
               "и асурского строя» (mānuṣaṃ … daivaṃ gāndharvam āsuram vyūham). В Сундараканде ракшасы "
               "не строятся в vyūha, а толпой окружают одинокого Ханумана — контраст, который МБх-локус "
               "помогает увидеть: Хануман сражается вне регулярной армейской тактики."),
    # ---- warrior epithets ----
    dict(snd="42.4", work="Droṇaparva", src="7.56.40-41", stem="vyAGra", lemma="puruṣavyāghra",
         typ="Б",
         frame="Эпитет «тигр среди мужей» (puruṣavyāghra / naravyāghra) — устойчивая героическая формула "
               "батальных парван, прилагаемая к Кришне-вознице («Победа всегда несомненна у того, чьим "
               "возницей стал ты, о тигр среди людей»). Тот же зооморфный регистр воинского величия "
               "лежит в основе характеристик Ханумана (mahābāhu, mahāsattva, mahābala) и его львино-"
               "тигриных сравнений. Общая эпическая формула доблести."),
    dict(snd="45.4", work="Śalyaparva", src="9.7.34-35", stem="parAkram", lemma="parākrama",
         typ="Б",
         frame="«Неизмеримой мощи» (amitavikrama) лучники Сундараканды, натягивающие золочёные луки "
               "«подобно тучам с молниями», описаны в том же формульном ключе, что и герои МБх, "
               "«яростно ринувшиеся, преисполненные доблести» (susaṃrabdheṣu … parākrānteṣu) после гибели "
               "Бхишмы, Дроны и Карны. Параллель — общий героико-батальный словарь vikrama/parākrama, "
               "прилагаемый к сопоставимым воинам."),
    # ---- mahāratha / great chariot-warrior ----
    dict(snd="46.27", work="Bhīṣmaparva", src="6.87.1", stem="mahAraT", lemma="mahāratha",
         typ="А",
         frame="«Великий колесничный воин» (mahāratha) — высший воинский разряд эпоса; в Бхишмапарве так "
               "названы Партхи, отреагировавшие на гибель Иравана в бою. Сундара 46.27, где Хануман "
               "обрушивается на колесницу (ratha) Дурдхары «словно молния на гору», вписывает обезьяньего "
               "героя в мир колесничного боя МБх: он уничтожает именно mahāratha-противников. Локус "
               "технического термина воинской иерархии."),
    # ---- combat fury formula ----
    dict(snd="42.4", work="Droṇaparva", src="7.73.1-2", stem="amarZa", lemma="amarṣa",
         typ="Б",
         frame="«Боевая ярость» (amarṣa) как пусковой механизм подвига — формула батальных парван: в "
               "Дронапарве «разъярённый великий лучник, лучший из всех носящих оружие, тигр среди мужей» "
               "(amarṣito maheṣvāsaḥ … naravyāghraḥ) бросается в бой. Сундара 42.4, где Хануман, увидев "
               "ракшаси, «принял огромный облик, пугающий [их]», передаёт ту же эпическую динамику "
               "ярость → преображение → атака. Общая боевая формула."),
    # ---- batch 2: combat-frenzy, deva-asura simile, invincibility, vega, tejas ----
    dict(snd="46.18", work="Karṇaparva", src="8.21.1", stem="samar", lemma="devāsuropama",
         typ="Б",
         frame="Сравнение боя с «битвой богов и асуров» (devāsuropama saṃgrāma) — высшая формула эпической "
               "гиперболы батальных парван: в Карнапарве сыновья Дхритараштры «опьяняемые битвой "
               "(yuddhadurmada), возобновили сражение, подобное схватке богов с асурами». Сундараканда "
               "пронизана тем же кодом: ракшаское войско, ринувшееся на Ханумана «стремительное, "
               "пышущее жаром огня» (46.18), а сам он бьёт врагов «словно тысячеокий [Индра] — дайтьев» "
               "(42.41). Локус формулы deva-asura, на которой строится всё батальное величие Сундары."),
    dict(snd="42.25", work="Karṇaparva", src="8.24.147", stem="yudDa", lemma="yuddhadurmada",
         typ="А",
         frame="Эпитет «опьянённые битвой» (yuddhadurmada) — техническая формула воинского исступления "
               "батальных парван; в Карнапарве данавы названы «великолепно вооружёнными, опьяняющимися "
               "битвой» (kṛtāstrān yuddhadurmadān). Восемьдесят тысяч киṅкаров Сундараканды, что "
               "«вышли из чертога с дубинами и молотами в руках» (42.25), — функциональный аналог "
               "этой исступлённой ратной массы. Локус классикус термина боевого неистовства."),
    dict(snd="51.42", work="Bhīṣmaparva", src="6.103.68-69", stem="durjay", lemma="durjaya",
         typ="Б",
         frame="Формула непобедимости через перечень богов: в Бхишмапарве сказано, что «можно одолеть "
               "Держателя ваджры [Индру], Варуну, а равно Яму …» — но не Бхишму, «гневного в бою, словно "
               "сам бог смерти с жезлом» (daṇḍapāṇim ivāntakam). Тот же приём — превосходство героя над "
               "богами — стоит за Сундара 51.42, где о Раме сказано: тот, «кто вступил бы в бой с Рамой, "
               "чья доблесть равна Вишну (viṣṇutulyaparākrama)…». Общая формула сверхбожественной "
               "неодолимости, прилагаемая к сопоставимой фигуре."),
    dict(snd="46.27", work="Droṇaparva", src="7.134.3", stem="vegena", lemma="vega",
         typ="Б",
         frame="«Стремительный налёт» (vegena utpatya / abhipatya) — устойчивая формула атаки батальных "
               "парван: в Дронапарве воин «стремительно обрушивался» (utpatantaṃ vegena), и его пришлось "
               "удерживать. Сундара 46.27, где Хануман «высоко вдруг взлетев (sahasotpatya), на колесницу "
               "Дурдхары обрушился, стремительный (mahāvega), словно молния на гору», — кавья-вариация "
               "той же кинетической формулы прыжка-атаки. Общий батальный словарь движения."),
    dict(snd="42.30", work="Karṇaparva", src="8.63.1-2", stem="tejas", lemma="tejasvin",
         typ="Б",
         frame="«Пылающий [ратным] жаром» (tejasvin) — стандартный эпитет богатыря в гуще боя: в "
               "Карнапарве «пылкий (tejasvī) Карна на колеснице двинулся на врагов», преисполненный "
               "скорби и ярости. Сундара 42.30, где «пылкий (tejasvī), осиянный Хануман, подобный горе, "
               "взмахнул хвостом по земле и взревел великим рыком», прилагает тот же эпитет tejas к "
               "обезьяньему герою на пике боевого подъёма. Общая героическая формула."),
    dict(snd="44.3", work="Karṇaparva", src="8.27.28-29", stem="cAp", lemma="cāpa",
         typ="Б",
         frame="Натягиваемый с громовым звоном лук — кульминационный жест воина-лучника. Сундара 44.3 "
               "(«лук, подобный луку Индры, … натягивая стремительно, [издающий] звук, подобный грому "
               "ваджры») передаёт ту же формулу, что и вызовы на поединок лучников МБх, где боец "
               "«всецело полагается на свою мощь и доблесть» (svavīrye), готовясь к стрельбе. Общий "
               "образ воина-cāpadhara батальных парван."),
]

def build():
    notes = []
    for sp in SPECS:
        snd_p = sp["snd"]; work = sp["work"]; src_p = sp["src"]
        s_sa, s_ru = sa(work, src_p), ru(work, src_p)
        u_sa, u_ru = sa("Sundara", snd_p), ru("Sundara", snd_p)
        if not s_sa or not u_sa:
            print(f"  WARN missing text: {work} {src_p} / Sundara {snd_p}", file=sys.stderr)
            continue
        note_ru = (
            sp["frame"]
            + "\n\nПараллель — " + work + " " + src_p + ":\n"
            + "СА: " + s_sa + "\n"
            + "РУ: " + s_ru
            + "\n\nСвидетельство: уровень шлоки (мягкое, корпусное); требуется проверка."
        )
        ch = snd_p.split(".")[0]
        notes.append({
            "shloka": "V." + snd_p,
            "lemma_iast": sp["lemma"],
            "note_ru": note_ru,
            "type": sp["typ"],
            "trigger": "crosstext",
            "subtype": "cross_text",
            "source": "Mahābhārata, " + work + " " + src_p,
            "stem": sp["stem"],
            "parallel_addr": "MBh " + work + " " + src_p,
            "parallel_sa_iast": s_sa,
            "parallel_ru": s_ru,
            "cluster": "mbh_battle",
            "chapter": ch,
            "review_required": True,
        })
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / "mbh_battle.json"
    out.write_text(json.dumps(notes, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {len(notes)} notes -> {out}")
    return notes

if __name__ == "__main__":
    build()
