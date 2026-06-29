"""
Generate Г (историко-культурологический) commentary layer for Sundarakāṇḍa chapters 21–44.

Layer Г = introductory articles on EPIC/MYTHOLOGICAL/COSMOLOGICAL BACKGROUND:
- Classes of semi-divine beings (gandharva, yakṣa, kinnara, vidyādhara, siddha, apsaras,
  dānava, daitya…)
- Cosmological concepts (yugas, Meru/cosmic geography, svarga/naraka, lokas, churning)
- Epic institutions & dharmic background (rākṣasa-marriage, vānara polity, vara/varadāna,
  śāpa/curse, vimāna, astra-as-myth, tapas→siddhi, ekapatnītva/pativratā as dharmic institution)
- Mythological events (Indra's deeds, Viṣṇu's avatāras, deva–asura conflict)

Rule: if concept introduced in Books I–III → cross-ref article only.
New-in-Book-V → fuller intro article.
Do NOT duplicate what is already in lexical layer or sundara_commentary_to_add.json.
"""
import sys
import json
import os
import re

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

JSONL_PATH = (
    r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl"
    r"\05_ramayana-sundarakanda.jsonl"
)

OUTPUT_DIR = r"C:\Users\user\Documents\GitHub\CommentaryStrategies\data\hist_cultural"
LEXICAL_DIR = r"C:\Users\user\Documents\GitHub\CommentaryStrategies\data\lexical"
EXISTING_JSON = r"C:\Users\user\Documents\GitHub\CommentaryStrategies\data\sundara_commentary_to_add.json"

TODAY = "2026-06-29"

# ---------------------------------------------------------------------------
# Load existing notes to avoid duplication
# ---------------------------------------------------------------------------
def load_existing_lemmas():
    """Return set of (chapter, lemma_iast) already noted in any layer."""
    seen = set()
    # From the big combined file
    if os.path.exists(EXISTING_JSON):
        with open(EXISTING_JSON, encoding="utf-8") as f:
            data = json.load(f)
        for item in data:
            if isinstance(item, dict) and "lemma_iast" in item and "shloka" in item:
                m = re.match(r"V\.(\d+)\.", item["shloka"] or "")
                if m:
                    seen.add((int(m.group(1)), item["lemma_iast"]))
    # From per-chapter lexical files
    for ch in range(21, 45):
        fpath = os.path.join(LEXICAL_DIR, f"ch{ch}.json")
        if os.path.exists(fpath):
            with open(fpath, encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except Exception:
                    continue
            for item in data:
                if isinstance(item, dict) and "lemma_iast" in item:
                    seen.add((ch, item["lemma_iast"]))
    return seen


# ---------------------------------------------------------------------------
# Load Sundarakanda verses
# ---------------------------------------------------------------------------
def load_verses(ch_range):
    """Return dict: chapter_int -> list of {passage, text, slp1}"""
    chapters = {ch: [] for ch in ch_range}
    with open(JSONL_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except Exception:
                continue
            ch_raw = obj.get("chapter", "")
            try:
                ch = int(ch_raw)
            except (TypeError, ValueError):
                continue
            if ch not in chapters:
                continue
            if obj.get("lang") != "sa":
                continue
            text = obj.get("text", "")
            if not text:
                continue
            chapters[ch].append({
                "passage": obj.get("passage", ""),
                "text": text,
                "slp1": obj.get("slp1", ""),
            })
    return chapters


# ---------------------------------------------------------------------------
# Knowledge base: Г-layer candidates for chapters 21–44
#
# Format: {
#   "lemma_iast": str,
#   "shloka": str,          # "V.N.M"
#   "trigger_text": str,    # Sanskrit word/phrase in verse
#   "note_ru": str,
#   "source": str,
#   "subtype": str,
#   "cross_ref": str | None,   # if introduced earlier, cite locus
#   "is_new": bool,            # True = new in Book V; False = cross-ref only
# }
#
# Methodology:
# ─ Ch 21–26: Sītā – Rāvaṇa dialogue + rākṣasī threats
#   • pativratā as dharmic institution (ch21) — first full dhārmika exposition in Bk V
#   • ekapatnīvrata / ekapatnītva (ch21) — dharmic monogamy
#   • Pulastya lineage / rākṣasa cosmogony (ch23) — genealogical frame
# ─ Ch 27: Trijaṭā's dream — already handled as В realia
# ─ Ch 28–34: Sītā's laments + Hanumān debates
#   • Brahmastra / divyāstra as mythological category (ch38) — weapon-myth
# ─ Ch 35–40: Hanumān's report on Rāma + jewel scene
#   • cāturvarṇya (ch35) — social-cosmological frame — already in А layer!
# ─ Ch 41–44: Hanumān's fire + battle with kin-kara etc.
#   • Agni as cosmic agent / lankādahana mythological parallel
#
# AFTER deduplication against existing lexical + combined layers:
# ---------------------------------------------------------------------------

KB = [
    # ── Ch 21: Sītā addresses Rāvaṇa ────────────────────────────────────────
    {
        "lemma_iast": "ekapatnīvrata",
        "shloka": "V.21.4",
        # akāryaṃ na mayā kāryam ekapatnyā vigarhitam
        "trigger_text": "ekapatnyā",
        "note_ru": (
            "Экапатнīврата — дхармическая норма верности мужу у единственной жены. "
            "В эпической традиции «единственная жена» (ekapatnī) противопоставляется "
            "многожёнству — обычному у царей, в т. ч. у Рамы (дающего обет ekapatnī "
            "только из-за Ситы). Обет ekapatnīvrata = основа pativratā-дхармы: жена "
            "получает защиту мужа и высшую религиозную заслугу (puṇya) ценой "
            "исключительной верности. Концепт введён как фоновый институт в Рам. I–II "
            "(Гринцер), здесь получает первое прямое декларативное оформление в речи "
            "Ситы: нарушение нормы = adharma, перечёркивающий легитимность сватовства "
            "Раваны."
        ),
        "source": "Rām. I–II (ekapatnīvrata как идеал); MW s.v. ekapatnikā",
        "cross_ref": "введено в Рам. I.73, II.27 (Гринцер)",
        "is_new": False,
    },
    {
        "lemma_iast": "pativratā (дхармический институт)",
        "shloka": "V.21.2",
        # cintayantī varārohā patim eva pativratā
        "trigger_text": "pativratā",
        "note_ru": (
            "Патниврата (pativratā) — в эпосе устойчивый дхармический институт «верной "
            "жены», определяющий поведение Ситы во всех эпизодах Сундараканды. В "
            "отличие от лексического объяснения термина (уже дано А-слоем), Г-слой "
            "фиксирует структурную роль: pativratā — не психологическая черта, а "
            "регулятивная норма, автоматически наделяющая женщину защитными "
            "«магическими» полномочиями (сравните: Ситы не может коснуться ни один "
            "ракшас без её согласия — следствие неповреждённого врата). Дхармическая "
            "основа pativratā восходит к ведическому ритуалу vivāha и разворачивается "
            "в Рам. I–III; здесь — первая сцена её прямого применения как «щита»."
        ),
        "source": "Manu 5.147–166 (pativratā как дхармическая категория); Rām. I.66 (Гринцер)",
        "cross_ref": "введено в Рам. I.66, III.47 (Гринцер)",
        "is_new": False,
    },

    # ── Ch 23: Rākṣasīs recount Rāvaṇa's genealogy (Pulastya line) ──────────
    {
        "lemma_iast": "ṣaṭ prajāpatayaḥ",
        "shloka": "V.23.6",
        # prajāpatīnāṃ ṣaṇṇāṃ tu caturtho 'ayaṃ prajāpati
        "trigger_text": "prajāpatīnāṃ ṣaṇṇāṃ … caturthaḥ … Pulastya",
        "note_ru": (
            "Шесть Праджапати — в брахманической космогонии класс «прародителей» "
            "(prajāpati), рождённых «умом» (mānasa) Брахмы. Согласно Рамаяне, их "
            "шесть: Маричи, Атри, Ангирас, Пуластья, Пулаха, Крату. Пуластья — "
            "четвёртый из шести (ср. Мбх. I.65.13–14). Это космогоническая рамка, "
            "объясняющая, почему Равана при всём своём злодействе обладает "
            "легитимным брахманическим происхождением (отец Вишравас — внук Брахмы): "
            "конфликт дхармы и происхождения составляет нарративный парадокс образа "
            "Раваны. Концепция mānasa-putras Брахмы введена в Рам. I (Гринцер)."
        ),
        "source": "Rām. VII.9–10 (генеалогия Раваны); Мбх. I.65.12–14",
        "cross_ref": "mānasa-putra Брахмы введено в Рам. I (Гринцер)",
        "is_new": False,
    },

    # ── Ch 26: siddha already in lexical ch26 → skip (no entry here) ──────────

    # ── Ch 27: Trijaṭā dream-vision — lokas cosmology ───────────────────────
    {
        "lemma_iast": "svapna (космологическое видение)",
        "shloka": "V.27.10",
        # śuklamālyāmbara — Trijaṭā's dream prophecy
        "trigger_text": "śuklamālyāmbara … divyaratha",
        "note_ru": (
            "Вещий сон Триджаты (гл. 27) относится к эпическому жанру «prophetic "
            "dream» (svapna-śāstra). В индийской традиции сон — не аллегория, а "
            "реальное видение (darśana) будущих событий, даруемое богами. "
            "Белые одеяния и вымазанность тёмными субстанциями = стандартная "
            "символика в эпических снах: белое → победа и рай (svarga), грязное → "
            "гибель; образы, увиденные Триджатой, имеют точные параллели в "
            "Мбх. XII.333 и Рам. VI (предсмертные знамения Раваны). "
            "Svapnaśāstra как дисциплина упоминается с АВ и разработана в "
            "Атхарваведе-париśиштax. Введено в Рам. I (Гринцер)."
        ),
        "source": "АВ-париśишты; Мбх. XII.333; Rām. VI (аналогичные сны-знамения)",
        "cross_ref": "svapna-śāstra как фоновый институт введено в Рам. I (Гринцер)",
        "is_new": False,
    },

    # ── Ch 33: varadāna already in lexical ch33 → skip ─────────────────────

    # ── Ch 35: cāturvarṇya already in lexical ch35 → skip ──────────────────

    # ── Ch 36: Hanumān shows ring — yugas/yugāntāgni ────────────────────────
    {
        "lemma_iast": "yugānta / pralaya (космологический фон)",
        "shloka": "V.36.13",
        # yugāntāgni — already in lexical ch36 as "yugāntāgni"
        # The Г-article goes one level up: not the term but the COSMOLOGICAL FRAME
        "trigger_text": "yugāntāgni … yugāntasūrya",
        "note_ru": (
            "Юга-антагни («огонь конца юги») — в эпосе устойчивый компаратив для "
            "непреодолимой разрушительной мощи. Космологический фон: согласно "
            "индийской циклической хронологии, каждая из четырёх юг завершается "
            "«растворением» (pralaya), при котором Вишну или Шива уничтожает миры "
            "огнём или потопом. Крита (satya) юга = 1 728 000 лет; трета = 1 296 000; "
            "двапара = 864 000; кали = 432 000 (сумма = одна mahāyuga = 4 320 000 лет; "
            "1000 махаюг = кальпа = «день Брахмы»). В Сундараканде yugānta-образы "
            "выполняют функцию эпической гиперболы, отсылающей к космологической "
            "памяти аудитории. Концепция четырёх юг вводится в Рам. I (Гринцер); "
            "pralaya-frame — там же и в Мбх. I.1."
        ),
        "source": "Мбх. I.1.28–36 (чатурьюга); Вишну-пурана I.3 (параметры юг)",
        "cross_ref": "четыре юги и pralaya введены в Рам. I (Гринцер); yugāntāgni как термин — А-слой V.36.13",
        "is_new": False,
    },

    # ── Ch 38: brahmastra — astra as mythological category ──────────────────
    {
        "lemma_iast": "brahmastra (астра как мифологическая категория)",
        "shloka": "V.38.37",
        # brahmastra already noted as В in combined layer
        # The Г-article is the INSTITUTION of astra-as-myth, not the named entity
        "trigger_text": "brahmastra",
        "note_ru": (
            "Астра (astra) — в эпосе мифологическая категория сверхъестественного "
            "оружия, дарованного богами (Брахмой, Индрой, Шивой) героям посредством "
            "tapas или var(ad)āna. В отличие от śastra (рукопашного оружия), астра "
            "= «оружие, посылаемое на расстоянии» плюс магическая формула (mantra). "
            "Брахмастра — высший уровень иерархии: дар Брахмы, способный уничтожить "
            "мир. Применение оружия против тех, кто не достоин его мощи, нарушает "
            "dharma (отсюда этические коллизии с Индраджитом). Институт "
            "«мифологического арсенала» введён в Рам. I (история Вишвамитры, "
            "Гринцер); здесь — первое применение brahmastra в Book V."
        ),
        "source": "Rām. I.27 (дар астр Вишвамитрой); Мбх. I.123 (категории astras)",
        "cross_ref": "категория astra как дар богов введена в Рам. I (Гринцер); brahmastra как В-реалия — В-слой V.38.37",
        "is_new": False,
    },

    # ── Ch 38–43: lankādahana / Agni → placed at ch41 in KB_ADDITIONAL ────────
]

# Now the ACTUAL fire on Lanka chapters 41-43
KB_ADDITIONAL = [
    # ── Ch 41–43: Hanumān's fire tail / lankādahana ─────────────────────────
    {
        "lemma_iast": "lankādahana (Агни как космический агент)",
        "shloka": "V.41.11",
        # dāvānala already in lexical ch41
        "trigger_text": "dāvānala … agniḥ",
        "note_ru": (
            "Ланкадахана («сожжение Ланки») — эпизод, приобретающий мифологический "
            "статус «огненного очищения» (pāvana). В эпической традиции Агни выступает "
            "не только домашним и жертвенным богом, но и агентом космической очистки: "
            "огонь, прошедший через Ланку с хвоста Ханумана, отсылает к образу "
            "Агни как свидетеля (sākṣin) и судьи. Параллель: Ситу испытывают огнём "
            "в Рам. VI (огненное испытание — agni-parīkṣā). Тот же Агни в Рам. I "
            "является свидетелем жертвоприношений. Таким образом, сожжение Ланки "
            "готовит сюжет к agni-parīkṣā: огонь «метит» Ланку как место, которое "
            "подлежит искуплению. Образ Агни как космического агента введён в "
            "Рам. I (Гринцер)."
        ),
        "source": "Rām. I.13–14 (Агни как свидетель); Rām. VI.104 (agni-parīkṣā)",
        "cross_ref": "Агни как космический агент введён в Рам. I (Гринцер); dāvānala как термин — А-слой V.41.11",
        "is_new": False,
    },

    # ── Ch 42: Vinatāsuta (Garuḍa) — Viṣṇu-mount mythology ─────────────────
    {
        "lemma_iast": "Garuḍa (мифологическая роль)",
        "shloka": "V.42.40",
        # vinatāsuta already in А-слой ch42
        "trigger_text": "vinatāsuta",
        "note_ru": (
            "Гаруда (vinatāsuta — «сын Винаты») — в эпосе и пуранах ездовая птица "
            "(vāhana) Вишну и архетипический враг нагов (змей). Его появление в "
            "сравнении для Ханумана активирует мифологический пласт: Гаруда = воплощённая "
            "способность преодолевать любые препятствия и уничтожать демонические силы "
            "(наги → ракшасы). Важнейший нарратив о Гаруде — похищение амриты из "
            "Сварги в Мбх. I.16–32 (аналог подвигу Ханумана). В Рам. III Гаруда уже "
            "упоминается как мифологический контекст; здесь — первое сравнение "
            "Ханумана с Гарудой в ситуации прямого боя. Концепт введён в Рам. III "
            "(Гринцер)."
        ),
        "source": "Мбх. I.16–32 (Гаруда и амрита); Rām. III (Гринцер)",
        "cross_ref": "Гаруда как mythological agent введён в Рам. III (Гринцер); vinatāsuta как термин — А-слой V.42.40",
        "is_new": False,
    },
]

# Flatten KB (keep only fully-formed entries with shloka + note_ru)
ALL_KB = []
for item in KB + KB_ADDITIONAL:
    if item.get("shloka") and item.get("note_ru"):
        ALL_KB.append(item)


# ---------------------------------------------------------------------------
# Deduplication
# ---------------------------------------------------------------------------
def deduplicate_kb(kb, existing_lemmas):
    """
    Remove entries whose lemma_iast (base form) is already in existing layers.
    We do a fuzzy check: strip parentheticals and normalise.
    """
    def base(lemma):
        # Take first word/token before space or '('
        return lemma.split("(")[0].strip().split()[0].lower()

    kept = []
    rejected = []
    for item in kb:
        ch_str = item["shloka"].split(".")[1]
        ch = int(ch_str)
        lemma = item["lemma_iast"]
        b = base(lemma)
        # Check against all existing lemmas for this chapter
        already = False
        for (ech, elem) in existing_lemmas:
            if ech == ch and base(elem) == b:
                already = True
                break
        if already:
            item["reject_reason"] = f"already in А/В/Б layer ch{ch}: {lemma}"
            rejected.append(item)
        else:
            kept.append(item)
    return kept, rejected


# ---------------------------------------------------------------------------
# Build output note
# ---------------------------------------------------------------------------
def make_note(item):
    note = {
        "shloka": item["shloka"],
        "lemma_iast": item["lemma_iast"],
        "note_ru": item["note_ru"],
        "type": "Г",
        "trigger": "myth_background",
        "subtype": "hist_cultural",
        "source": item.get("source", ""),
        "review_required": True,
        "cross_ref": item.get("cross_ref"),
    }
    return note


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Loading existing lemmas…")
    existing = load_existing_lemmas()
    print(f"  {len(existing)} (chapter, lemma) pairs already in А/В/Б layers")

    print("Loading Sundarakanda verses ch21–44…")
    verse_map = load_verses(range(21, 45))
    total_verses = sum(len(v) for v in verse_map.values())
    print(f"  {total_verses} Sanskrit verses loaded")

    print("Deduplicating knowledge base…")
    kept, rejected_dedup = deduplicate_kb(ALL_KB, existing)
    print(f"  {len(kept)} candidates kept, {len(rejected_dedup)} rejected (duplicates)")

    # Bucket notes by chapter
    notes_by_ch = {ch: [] for ch in range(21, 45)}
    rejected_by_ch = {ch: [] for ch in range(21, 45)}

    for item in kept:
        ch_str = item["shloka"].split(".")[1]
        ch = int(ch_str)
        notes_by_ch[ch].append(make_note(item))

    for item in rejected_dedup:
        ch_str = item["shloka"].split(".")[1]
        ch = int(ch_str)
        rej = {
            "shloka": item["shloka"],
            "lemma_iast": item["lemma_iast"],
            "reject_reason": item.get("reject_reason", "duplicate"),
        }
        rejected_by_ch[ch].append(rej)

    # Write per-chapter files
    stats = {}
    for ch in range(21, 45):
        notes = notes_by_ch[ch]
        rejected = rejected_by_ch[ch]
        n_verses = len(verse_map.get(ch, []))

        meta = {
            "_meta": {
                "description": f"Г-слой (историко-культурологический) примечаний, гл. {ch}",
                "chapter": ch,
                "layer": "hist_cultural",
                "type_code": "Г",
                "rule": (
                    "Вводные статьи по эпическому/мифологическому/космологическому фону. "
                    "Концепты из Кн. I–III → кросс-ссылка. Новые в Кн. V → полная статья. "
                    "НЕ дублирует А/В/Б-слои."
                ),
                "generated": TODAY,
                "verses_total": n_verses,
                "notes_count": len(notes),
                "density_pct": round(len(notes) / n_verses * 100, 1) if n_verses else 0.0,
            }
        }

        out_path = os.path.join(OUTPUT_DIR, f"ch{ch}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump([meta] + notes, f, ensure_ascii=False, indent=2)

        rej_path = os.path.join(OUTPUT_DIR, f"ch{ch}.rejected.json")
        with open(rej_path, "w", encoding="utf-8") as f:
            json.dump(rejected, f, ensure_ascii=False, indent=2)

        stats[ch] = {"kept": len(notes), "rejected": len(rejected), "verses": n_verses}
        status = f"ch{ch:2d}: {len(notes):2d} notes  ({len(rejected)} rejected) | {n_verses} verses"
        print(status)

    # Summary
    total_kept = sum(s["kept"] for s in stats.values())
    total_rej = sum(s["rejected"] for s in stats.values())
    cross_ref_count = sum(
        1 for item in kept if item.get("cross_ref")
    )
    new_count = sum(
        1 for item in kept if item.get("is_new", True) and not item.get("cross_ref")
    )

    print()
    print("=" * 60)
    print(f"TOTAL Г notes kept:    {total_kept}")
    print(f"  cross-ref articles:  {cross_ref_count}")
    print(f"  fuller new articles: {new_count}")
    print(f"TOTAL rejected:        {total_rej}")
    print(f"Output: {OUTPUT_DIR}")
    print("=" * 60)

    # Verify files exist
    print("\nVerifying output files…")
    missing = []
    for ch in range(21, 45):
        p1 = os.path.join(OUTPUT_DIR, f"ch{ch}.json")
        p2 = os.path.join(OUTPUT_DIR, f"ch{ch}.rejected.json")
        if not os.path.exists(p1):
            missing.append(p1)
        if not os.path.exists(p2):
            missing.append(p2)
    if missing:
        print(f"MISSING FILES: {missing}")
        sys.exit(1)
    else:
        print(f"All {(45-21)*2} files present (24 ch*.json + 24 ch*.rejected.json)")


if __name__ == "__main__":
    main()
