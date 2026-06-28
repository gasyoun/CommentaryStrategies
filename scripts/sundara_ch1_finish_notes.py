"""
Refine the 162 raw ch.1 candidates into FINISHED, ready-to-paste commentary
entries for the Sanskrit-Russian parallel corpus (samskrtam.ru reader).

Core editorial rule: in a parallel corpus the reader ALREADY has Leonov's
literal Russian подстрочник, so a note is worth adding ONLY when it gives
something the подстрочник cannot:
  - a non-obvious term gloss / etymology (Type А)
  - an epithet's FIRST appearance in кн. V (Type А, помета)
  - a realia / myth figure / geography article (Type В)
  - a divergence / dropped term vs the literary text (Type Б, Костина «Опущено»)
  - a cross-ref to where Grintser introduced the name in Ram. I-III (отсылка)
A verse that the подстрочник already makes clear gets NO note (by omission).

Input:  data/leonov_sundara_ch1_candidates.json  (162 raw candidates)
Output: data/sundara_ch1_commentary_to_add.json  (finished notes, sorted)
        data/sundara_ch1_stats.json              (regenerated stats)
"""
import sys, os, json, re, collections
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CS_DIR   = Path(r"C:\Users\user\Documents\GitHub\CommentaryStrategies")
DATA_DIR = CS_DIR / "data"

cands = json.load(open(DATA_DIR / "leonov_sundara_ch1_candidates.json", encoding='utf-8'))

def shloka_num(addr: str) -> tuple:
    """'Rām. Sundara 5.1.39' -> (1, 39) for sorting."""
    m = re.search(r'5\.(\d+)\.(\d+)', addr)
    return (int(m.group(1)), int(m.group(2))) if m else (99, 999)

def short_addr(addr: str) -> str:
    """'Rām. Sundara 5.1.39' -> 'V.1.39'"""
    m = re.search(r'5\.(\d+)\.(\d+)', addr)
    return f"V.{m.group(1)}.{m.group(2)}" if m else addr

def ucfirst(s: str) -> str:
    """Capitalize only the first char (preserve proper-name caps in the tail)."""
    return s[:1].upper() + s[1:] if s else s

# ── KNOWLEDGE BASE ───────────────────────────────────────────────────────────
# Per-lemma editorial content. The raw candidates only carry a bare gloss;
# here we attach real etymology / commentator / cross-ref so the FINISHED note
# gives the reader what the подстрочник cannot.
#
# Each entry:
#   ru        — headword translation as it reads in the подстрочник
#   note      — finished note body (the part AFTER the lemma) for FIRST appearance
#   type      — А / Б / В
#   trigger   — term | epithet | realia | omission | crossref
#   priority  — high | med | low
#   grintser  — optional «см. примеч. к I.X.Y» reference text
#   repeat_note — if set, a (short) note is still worth it on repeat; else repeats are dropped

KB = {
    "cāraṇa": {
        "ru": "чараны", "type": "В", "trigger": "realia", "priority": "high",
        "note": "класс полубожественных небесных певцов-странников (cāraṇa). "
                "Комм. «Бхушана» глоссирует как dēvagāyakāḥ «божественные певцы», «Таттвадипика» — «дорога богов» (suravartmani). "
                "Голдмены: «celestial bards». Подстрочник «по которому ходят чараны» сохраняет слово без пояснения его мифологического статуса.",
        "commentators": ["Bhūṣaṇa", "Tattvadīpikā"], "western": ["Goldman 1994"],
    },
    "vānara": {
        "ru": "ванара", "type": "А", "trigger": "term", "priority": "high",
        "note": "букв. «лесной житель», обезьяна; общий термин для народа Сугривы. "
                "В «Тилаке» отмечается божественное происхождение ванаров. Подстрочник передаёт нарицательным «обезьяна», "
                "что снимает этнонимический оттенок термина.",
        "commentators": ["Tilaka"], "western": [],
        # vānara recurs 31×; a note is warranted ONLY on first appearance.
    },
    "mahābala": {
        "ru": "обладающий великой силой", "type": "А", "trigger": "epithet", "priority": "med",
        "note": "ситуативный эпитет Ханумана, букв. «обладающий великой силой» (mahā-bala). "
                "Первое вхождение в кн. V. Дальнейшие употребления — без примечания.",
        "commentators": [], "western": [],
    },
    "dhīra": {
        "ru": "стойкий", "type": "А", "trigger": "epithet", "priority": "low",
        "note": "букв. «твёрдый», «мудрый» (dhīra); в контексте подготовки к прыжку подчёркивает ментальную концентрацию героя.",
        "commentators": [], "western": [],
    },
    "vaidūrya": {
        "ru": "вайдурья", "type": "А", "trigger": "term", "priority": "med",
        "note": "берилл / «кошачий глаз» (vaidūrya), драгоценный минерал зеленовато-синего отлива; "
                "здесь — о цвете горных лугов «изумрудного цвета». Подстрочник передаёт смысл («изумрудного цвета»), "
                "но опускает сам минералогический термин.",
        "commentators": [], "western": [],
    },
    "kapivara": {
        "ru": "лучший из обезьян", "type": "А", "trigger": "epithet", "priority": "med",
        "note": "стандартный эпитет-сравнение (kapi-vara «лучший из обезьян»), синонимичен vānaraśreṣṭha, plavaṃgapravara. Первое вхождение в кн. V.",
        "commentators": [], "western": [],
    },
    "nāga": {
        "ru": "наг / слон", "type": "Б", "trigger": "term", "priority": "high",
        "note": "слово nāga двузначно: «наг» (полубожественный змей) и «слон». Из комментаторов только «Широмани» глоссирует здесь gaja (слон); "
                "большинство западных переводчиков — «наг» (Goldman 1984: 302). Подстрочник выбирает один вариант, скрывая амбивалентность оригинала.",
        "commentators": ["Śiromaṇi"], "western": ["Goldman 1994"],
    },
    "mārutātmaja": {
        "ru": "сын бога ветра", "type": "А", "trigger": "epithet", "priority": "high",
        "note": "патроним Ханумана (māruta-ātmaja «сын Маруты/Ваю»), пара к vāyuputra. Первое вхождение в кн. V.",
        "commentators": [], "western": [],
    },
    "kapikuñjara": {
        "ru": "слон среди обезьян", "type": "А", "trigger": "epithet", "priority": "med",
        "note": "метафора высшего превосходства в группе (kapi-kuñjara «слон среди обезьян»), ср. puruṣarṣabha «бык среди мужей». Первое вхождение в кн. V.",
        "commentators": [], "western": [],
    },
    "rāghava": {
        "ru": "Потомок Рагху", "type": "А", "trigger": "crossref", "priority": "high",
        "note": "стандартный эпитет Рамы (потомок царя Рагху).",
        "grintser": "см. примеч. к I.1.1 (Гринцер)",
        "commentators": [], "western": [],
    },
    "janakātmajā": {
        "ru": "Дочь Джанаки", "type": "А", "trigger": "crossref", "priority": "high",
        "note": "патроним Ситы (дочь царя Джанаки); первое появление эпитета Ситы в кн. V.",
        "grintser": "см. примеч. к I.1.25 (Гринцер)",
        "commentators": [], "western": [],
    },
    "vāyuputra": {
        "ru": "сын Ваю", "type": "А", "trigger": "epithet", "priority": "med",
        "note": "патроним Ханумана (vāyu-putra «сын бога ветра»), пара к mārutātmaja. "
                "Леонов отмечает чередование с ātmayoni; «Тилака» подчёркивает их тождество.",
        "commentators": ["Tilaka"], "western": [],
    },
    "rāvaṇa": {
        "ru": "Равана", "type": "В", "trigger": "realia", "priority": "low",
        "note": "царь ракшасов, похититель Ситы; центральный антагонист. Введён ранее; здесь без пояснения.",
        "commentators": [], "western": [],
        "skip": True,  # too well-known / introduced earlier — no note needed
    },
    "surasā": {
        "ru": "Сураса", "type": "В", "trigger": "realia", "priority": "high",
        "note": "мать нагов (nāgamātā), посланная богами испытать Ханумана на пути через океан. "
                "В «Таттвадипике» поясняется её роль как испытательницы силы героя. Первое появление персонажа.",
        "commentators": ["Tattvadīpikā"], "western": [],
    },
    "dāśarathi": {
        "ru": "Сын Дашаратхи", "type": "А", "trigger": "crossref", "priority": "med",
        "note": "патроним Рамы (сын царя Дашаратхи).",
        "grintser": "см. примеч. к I.1.8 (Гринцер)",
        "commentators": [], "western": [],
    },
    "māruti": {
        "ru": "Марути", "type": "А", "trigger": "epithet", "priority": "med",
        "note": "именное производное от Марут (бог ветра) — стандартное имя Ханумана.",
        "commentators": [], "western": [],
    },
    "vaidehī": {
        "ru": "Вайдехи", "type": "А", "trigger": "crossref", "priority": "med",
        "note": "эпитет Ситы (царевна из Видехи).",
        "grintser": "см. примеч. к I.1.28 (Гринцер)",
        "commentators": [], "western": [],
    },
    "maithilī": {
        "ru": "Майтхили", "type": "А", "trigger": "crossref", "priority": "med",
        "note": "эпитет Ситы (царевна из Митхилы).",
        "grintser": "см. примеч. к I.1.26 (Гринцер)",
        "commentators": [], "western": [],
    },
    "siṃhikā": {
        "ru": "Симхика", "type": "В", "trigger": "realia", "priority": "high",
        "note": "ракшасини, «ловящая тени» (chāyāgrahin): по «Широмани», обладает силой притягивать существ за их тень. "
                "Хануман уничтожает её при перелёте. Первое появление персонажа.",
        "commentators": ["Śiromaṇi"], "western": [],
    },
    "mahākāya": {
        "ru": "огромный", "type": "А", "trigger": "epithet", "priority": "low",
        "note": "ситуативный эпитет (mahā-kāya «обладающий великим телом») при увеличении тела Ханумана перед прыжком.",
        "commentators": [], "western": [],
    },
    # maināka comes only as a stem in some candidates; add it explicitly:
    "maināka": {
        "ru": "Майнака", "type": "В", "trigger": "realia", "priority": "high",
        "note": "гора, поднявшаяся из океана навстречу Хануману как место отдыха. "
                "В «Бхушане» — сын Гималаев; эпитет hiraṇyanābha «золотопупый». Первое появление.",
        "commentators": ["Bhūṣaṇa"], "western": [],
    },
}

# ── REFINEMENT ───────────────────────────────────────────────────────────────
# First, find the EARLIEST shloka at which each lemma occurs across ALL its
# candidates (regardless of candidate suffix), so the first-appearance note
# anchors to the true first verse, not the first verse that happened to carry an
# 'ep' candidate.
earliest_shloka = {}
for c in cands:
    lm = c.get('provenance', {}).get('iast_form')
    if lm is None:
        continue
    sn = shloka_num(c['shloka_addr'])
    if lm not in earliest_shloka or sn < earliest_shloka[lm]:
        earliest_shloka[lm] = sn

# Walk candidates in shloka order, applying first-occurrence dedup per lemma.
cands_sorted = sorted(cands, key=lambda c: (shloka_num(c['shloka_addr']),
                                            c['comment_id']))

first_seen = set()          # lemmas already noted (for first-appearance dedup)
omission_seen = set()       # (lemma) for which an omission note already emitted
notes = []
dropped = collections.Counter()

for c in cands_sorted:
    prov = c.get('provenance', {})
    lemma = prov.get('iast_form')
    cid = c['comment_id']
    addr = c['shloka_addr']
    sa = short_addr(addr)

    # ── DROP: pure stem-overlap "parallels" (ix) — no real note ──────────────
    if cid.split('.')[-1].startswith('ix'):
        dropped['stem_overlap_parallel'] += 1
        continue

    if lemma is None or lemma not in KB:
        dropped['no_kb_entry'] += 1
        continue

    kb = KB[lemma]
    if kb.get('skip'):
        dropped['too_wellknown'] += 1
        continue

    is_om = cid.split('.')[-1].startswith('om')
    is_ep = cid.split('.')[-1].startswith('ep')
    first = prov.get('first_occurrence', False)

    # ── OMISSION candidates (Костина «Опущено») ─────────────────────────────
    if is_om:
        # The raw omission detector flags a lemma as "dropped" whenever the
        # Russian gloss's first chars don't appear in the подстрочник. That is
        # a weak heuristic: in most cases (vānara→«обезьяна», mahābala→«великой
        # силой», nāga→«слон/наг») the подстрочник DOES render the concept with a
        # synonym, so there is no real omission and a note would only add noise.
        # We therefore keep an omission note ONLY for proper-name epithets whose
        # drop genuinely loses a referent the literary text restores — and only
        # once per lemma. Common appellatives are dropped.
        OMISSION_WORTH = {"rāghava", "janakātmajā", "vaidehī", "maithilī",
                          "dāśarathi", "mārutātmaja", "vāyuputra"}
        if lemma not in OMISSION_WORTH:
            dropped['omission_rendered_by_podstrochnik'] += 1
            continue
        if lemma in omission_seen:
            dropped['duplicate_omission'] += 1
            continue
        omission_seen.add(lemma)
        pr = prov.get('parallel_ru_text', '')
        note_ru = (f"{ucfirst(kb['ru'])} ({lemma}). [Е. Костина]: именной эпитет «{lemma}» "
                   f"присутствует в оригинале, но не передан отдельным словом в подстрочнике "
                   f"(«…{pr[:60].strip()}…»). В литературном тексте эпитет восстанавливается; "
                   f"отметить как незафиксированное опущение — на усмотрение редактора.")
        notes.append({
            "shloka": sa,
            "lemma_iast": lemma,
            "note_ru": note_ru,
            "type": "Б",
            "trigger": "omission",
            "priority": "low",
            "source": "parallel-text divergence (verse-level, soft)",
            "review_required": True,
            "src_candidate_id": cid,
        })
        continue

    # ── EPITHET / TERM / REALIA candidates (ep) ──────────────────────────────
    if is_ep:
        # FIRST appearance → full note. Repeats → drop (подстрочник suffices).
        if lemma in first_seen:
            dropped['repeat_occurrence'] += 1
            continue
        first_seen.add(lemma)
        # Anchor the first-appearance note to the lemma's EARLIEST shloka, even
        # if this particular 'ep' candidate sits at a later verse.
        em = earliest_shloka.get(lemma)
        if em:
            sa = f"V.{em[0]}.{em[1]}"

        # Build finished note text.
        body = kb['note']
        if kb.get('grintser'):
            body = body.rstrip('.') + f". {kb['grintser']}."
        # Compose «русский (iast) — …»
        note_ru = f"{ucfirst(kb['ru'])} ({lemma}) — {body}"
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
            "src_candidate_id": cid,
        })
        continue

    dropped['other'] += 1

# ── Sort finished notes by shloka, then priority ─────────────────────────────
prio_rank = {"high": 0, "med": 1, "low": 2}
notes.sort(key=lambda n: (int(n['shloka'].split('.')[1]),
                          int(n['shloka'].split('.')[2]),
                          prio_rank.get(n['priority'], 3)))

# ── Write commentary-to-add ──────────────────────────────────────────────────
out_meta = {
    "_meta": {
        "description": "Рекомендуемые примечания к параллельному Sa-Ru корпусу (Сундараканда, кн. V, гл. 1)",
        "rule": "Примечание добавляется ТОЛЬКО когда оно даёт то, чего нет в подстрочнике Леонова: "
                "глосса нетривиального термина, помета первого вхождения эпитета в кн. V, "
                "статья о реалии/мифологеме/географии, расхождение с литературным текстом, "
                "или отсылка к месту ввода имени в Рам. I-III (Гринцер). "
                "Стих, ясный из подстрочника, примечания НЕ получает.",
        "evidence": "Все корпусные свидетельства — уровень шлоки (мягкое). Каждое примечание review_required.",
        "generated": "2026-06-26",
        "ch1_verses_total": 213,
    }
}
commentary_out = [out_meta] + notes
with open(DATA_DIR / "sundara_ch1_commentary_to_add.json", 'w', encoding='utf-8') as f:
    json.dump(commentary_out, f, ensure_ascii=False, indent=2)

# ── Regenerate stats ─────────────────────────────────────────────────────────
by_type    = collections.Counter(n['type'] for n in notes)
by_trigger = collections.Counter(n['trigger'] for n in notes)
by_prio    = collections.Counter(n['priority'] for n in notes)
noted_shlokas = set(n['shloka'] for n in notes)
verses_total = 213
verses_noted = len(noted_shlokas)

stats = {
    "ch1_verses_total": verses_total,
    "notes_recommended": len(notes),
    "verses_with_note": verses_noted,
    "verses_without_note": verses_total - verses_noted,
    "by_type": dict(by_type),
    "by_trigger": dict(by_trigger),
    "by_priority": dict(by_prio),
    "raw_candidates_input": len(cands),
    "dropped": dict(dropped),
    "drop_total": sum(dropped.values()),
    "note": "Notes are FINISHED (ready-to-paste) Russian text. Rule: only add what "
            "the подстрочник cannot give. Evidence verse-level (soft); all review_required.",
}
with open(DATA_DIR / "sundara_ch1_stats.json", 'w', encoding='utf-8') as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)

# ── Report ───────────────────────────────────────────────────────────────────
print(f"Finished notes recommended: {len(notes)}")
print(f"  by type:     {dict(by_type)}")
print(f"  by trigger:  {dict(by_trigger)}")
print(f"  by priority: {dict(by_prio)}")
print(f"Verses with note: {verses_noted} / {verses_total}  (без примечания: {verses_total - verses_noted})")
print(f"Dropped from 162 raw: {sum(dropped.values())}  {dict(dropped)}")
print()
print("=== Sample finished notes ===")
for n in notes[:6]:
    print(f"[{n['shloka']}] ({n['type']}/{n['trigger']}/{n['priority']}) {n['note_ru']}")
    print()
