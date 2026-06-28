"""
sundara_gazetteer_supplement.py — correction pass.

The book run (sundara_ch2_68_pipeline.py) under-covered named-entity
first-appearances because its trigger gazetteer was ch.1-centric. This pass uses
the AUTHORITATIVE entity gazetteer from leonov_kostina_commentary_analysis.html
§09б (id="formulas") + ramayana-leonov/ramayana-formulas_1-2.md, which list every
named character / divine being / place with their exact first-appearance shloka
in кн. V.

For each gazetteer entity whose FIRST book appearance has NO note yet, it adds a
Type В realia note (proper names are only transliterated by the подстрочник —
the identity/realia is exactly what to add) anchored to that first shloka, with
the same quality/format as the ch.1 Siṃhikā/Vibhīṣaṇa notes. Flagged unusual
epithets (e.g. padmapalāśākṣa) get a Type А epithet note.

Global first-appearance dedup is preserved: each entity noted ONCE, at first
occurrence. Entities already noted by the main pipeline are skipped.

It then:
  - appends the new notes into the affected per-chapter files
    (data/sundara_ch{N}_commentary_to_add.json)
  - regenerates data/sundara_commentary_to_add.json + data/sundara_book_stats.json

All output UTF-8 no BOM, review_required:true.
"""
import sys, json, collections
from pathlib import Path
from datetime import date

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CS_DIR   = Path(r"C:\Users\user\Documents\GitHub\CommentaryStrategies")
DATA_DIR = CS_DIR / "data"
CORPUS   = Path(r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl\05_ramayana-sundarakanda.jsonl")
TODAY    = str(date.today())

def ucfirst(s): return s[:1].upper() + s[1:] if s else s

# ── GAZETTEER ENTITIES (corpus-verified first-appearance shlokas) ─────────────
# shloka = exact corpus passage where the NAME/epithet first occurs (verified by
#   grepping the corpus text, not the ±1 table anchor). chapter is derived.
# These are the named-entity / flagged-epithet first appearances the main run
# missed.  Each note ≈ ch.1 Siṃhikā / Vibhīṣaṇa register.
GAZETTEER = [
    # ── ch.1 misses (кн. V realia, same class as Siṃhikā/Surasā that WERE noted) ──
    {"lemma": "samudra", "shloka": "V.1.29", "type": "В", "trigger": "realia", "priority": "med",
     "ru": "океан",
     "note": "великий океан (samudra), отделяющий материк от Ланки; эпитеты varuṇālaya «обитель Варуны», mahodadhi «великий водоём». Его переплытие в один прыжок — центральный подвиг кн. V. Подстрочник передаёт нарицательным «океан», не отмечая его как мифологизированную водную преграду — обитель Варуны.",
     "commentators": [], "western": ["Goldman 1994"]},
    {"lemma": "maināka", "shloka": "V.1.91", "type": "В", "trigger": "realia", "priority": "high",
     "ru": "Майнака",
     "note": "золотая гора (maināka), поднявшаяся из океана навстречу Хануману как место отдыха по просьбе Самудры (океана). В «Бхушане» — сын Гималаев и Мены; эпитеты hiraṇyanābha «золотопупый», girisattama «лучшая из гор». Хануман из учтивости касается её и летит дальше. Первое появление персонажа.",
     "commentators": ["Bhūṣaṇa"], "western": []},

    # ── ch.3: Lankini, the city-goddess / gate-guardian rākṣasī ──
    {"lemma": "laṅkinī", "shloka": "V.3.21", "type": "В", "trigger": "realia", "priority": "high",
     "ru": "Ланкини",
     "note": "хранительница-божество города Ланки (laṅkinī), ракшаси, персонифицирующая саму крепость; преграждает Хануману вход и сражена его ударом. По комментаторам, её поражение — предзнаменование падения Ланки (древнее пророчество о гибели города при появлении обезьяны). Подстрочник передаёт «Ланка… сама предстала», сохраняя двусмысленность «город / его богиня». Первое появление персонажа.",
     "commentators": ["Tilaka"], "western": ["Goldman 1994"]},

    # ── ch.10: Mandodari, chief queen of Ravana ──
    {"lemma": "mandodarī", "shloka": "V.10.52", "type": "В", "trigger": "realia", "priority": "high",
     "ru": "Мандодари",
     "note": "главная супруга Раваны (mandodarī «тонкостанная»), спящую красоту которой Хануман сперва принимает за Ситу. Дочь асура Майи; в традиции — образец добродетельной жены при злом муже. Подстрочник лишь транслитерирует имя; узнавание-ошибка Ханумана — важный сюжетный мотив. Первое появление персонажа.",
     "commentators": ["Bhūṣaṇa"], "western": []},

    # ── ch.13: Daśagrīva, "ten-necked" epithet of Ravana, FIRST in кн. V ──
    {"lemma": "daśagrīva", "shloka": "V.13.49", "type": "А", "trigger": "epithet", "priority": "med",
     "ru": "Десятишеий",
     "note": "эпитет Раваны daśa-grīva «десятишеий» (пара к daśānana «десятиликий»); указывает на его десять голов — знак чудовищной мощи, полученной аскезой. Леонов: «Мощношеий Равана». Первое вхождение формы в кн. V.",
     "commentators": [], "western": []},

    # ── ch.27: Trijaṭā, the compassionate rākṣasī ──
    {"lemma": "trijaṭā", "shloka": "V.27.4", "type": "В", "trigger": "realia", "priority": "high",
     "ru": "Триджата",
     "note": "старая ракшаси (trijaṭā «с тремя косицами»), стражница Ситы, которая удерживает прочих ракшасини от расправы, рассказав свой вещий сон о победе Рамы. Эпитеты dharmajñā «знающая дхарму», dayāpara «сострадательная». Её сон — структурный пророческий узел кн. V. Первое появление персонажа.",
     "commentators": ["Tattvadīpikā"], "western": ["Goldman 1994"]},

    # ── ch.41: Daśānana, "ten-faced" epithet of Ravana, FIRST in кн. V ──
    {"lemma": "daśānana", "shloka": "V.41.8", "type": "А", "trigger": "epithet", "priority": "med",
     "ru": "Десятиликий",
     "note": "эпитет Раваны daśa-ānana «десятиликий» (пара к daśagrīva); подчёркивает его десятиглавый облик. Леонов: «Десятиликий Равана». Первое вхождение формы в кн. V.",
     "commentators": [], "western": []},

    # ── ch.44: Jambumālin, Prahasta's son, first rākṣasa warrior killed ──
    {"lemma": "jambumālin", "shloka": "V.44.19", "type": "В", "trigger": "realia", "priority": "med",
     "ru": "Джамбумалин",
     "note": "сын Прахасты, ракшаса-воин (jambu-mālin «в гирлянде из роз»), первый полководец, посланный против Ханумана и им убитый; эпитет raṇakovida «искусный в бою». Его гибель открывает череду поединков в роще. Первое появление персонажа.",
     "commentators": [], "western": []},

    # ── ch.47: Akṣa, son of Ravana ──
    {"lemma": "akṣa", "shloka": "V.47.1", "type": "В", "trigger": "realia", "priority": "high",
     "ru": "Акша",
     "note": "юный сын Раваны (akṣa), царевич (kumāra), отправленный против Ханумана после гибели пяти полководцев и убитый им; описан эпитетом mahābala «многомощный». Гибель сына — поворот, вынуждающий Равану послать Индраджита. Подстрочник называет его «царевич», имя вводит ниже. Первое появление персонажа.",
     "commentators": [], "western": ["Goldman 1994"]},

    # ── ch.48: padmapalāśākṣa, unusual epithet of Indrajit ──
    {"lemma": "padmapalāśākṣa", "shloka": "V.48.17", "type": "А", "trigger": "epithet", "priority": "med",
     "ru": "лотосоокий",
     "note": "эпитет Индраджита padma-palāśa-akṣa «с глазами-лепестками лотоса» — неожиданная «лирическая» формула красоты, приложенная к грозному воину-ракшасу. Леонов: «блистательный, лотосоокий». Контраст между нежным эпитетом и боевой ролью отмечается комментаторами как намеренный. Первое вхождение в кн. V.",
     "commentators": ["Bhūṣaṇa"], "western": []},

    # ── ch.61: Dadhimukha, guardian of Madhuvana, uncle of Angada ──
    {"lemma": "dadhimukha", "shloka": "V.61.9", "type": "В", "trigger": "realia", "priority": "med",
     "ru": "Дадхимукха",
     "note": "обезьяна-страж медового сада Сугривы (dadhimukha «творожноликий», вар. dadhivaktra), дядя (mātula) Ангады; жалуется Сугриве на разорение сада вернувшимися ванарами — комический эпизод, косвенно сообщающий об успехе миссии. Первое появление персонажа.",
     "commentators": [], "western": []},
]

def chap_of(shloka):
    return int(shloka.split('.')[1])

# ── load merged notes to know what's already noted ───────────────────────────
merged = json.load(open(DATA_DIR / "sundara_commentary_to_add.json", encoding='utf-8'))
existing_lemmas = set(n['lemma_iast'] for n in merged if '_meta' not in n)
# also treat 'prahastha' (misspelled key already used) as covering 'prahasta'
existing_lemmas.add('prahasta')

added = []
skipped = []
for ent in GAZETTEER:
    if ent['lemma'] in existing_lemmas:
        skipped.append(ent['lemma'])
        continue
    added.append(ent)
    existing_lemmas.add(ent['lemma'])

print(f"Gazetteer entities: {len(GAZETTEER)}; already noted (skip): {len(skipped)} {skipped}")
print(f"Missing → adding {len(added)} notes:")

# ── build note dicts + append into per-chapter files ─────────────────────────
def make_note(ent):
    body = ent['note']
    note_ru = f"{ucfirst(ent['ru'])} ({ent['lemma']}) — {body}"
    return {
        "shloka": ent['shloka'],
        "lemma_iast": ent['lemma'],
        "note_ru": note_ru,
        "type": ent['type'],
        "trigger": ent['trigger'],
        "priority": ent['priority'],
        "source": "gazetteer (analysis §09б / formulas tt.1-2) — first occurrence in кн. V (verse-level, soft)",
        "review_required": True,
        "cited_indian_commentators": ent.get('commentators', []),
        "cited_western_sources": ent.get('western', []),
        "src_candidate_id": f"gazetteer/sundara/{ent['shloka'].replace('V.','')}",
    }

prio_rank = {"high": 0, "med": 1, "low": 2}
by_chapter = collections.defaultdict(list)
for ent in added:
    note = make_note(ent)
    by_chapter[chap_of(ent['shloka'])].append(note)
    print(f"  [{note['shloka']}] {note['type']}/{note['trigger']}/{note['priority']}: {ent['lemma']}")

affected_chapters = sorted(by_chapter.keys())
for ch in affected_chapters:
    path = DATA_DIR / f"sundara_ch{ch}_commentary_to_add.json"
    data = json.load(open(path, encoding='utf-8'))
    meta = data[0]
    notes = [x for x in data if '_meta' not in x]
    notes.extend(by_chapter[ch])
    # re-sort by verse, then priority
    notes.sort(key=lambda n: (int(n['shloka'].split('.')[2]), prio_rank.get(n['priority'], 3)))
    # update meta count
    if '_meta' in meta:
        meta['_meta']['notes_count'] = len(notes)
        meta['_meta']['gazetteer_supplement'] = TODAY
    out = [meta] + notes
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"  → ch.{ch}: +{len(by_chapter[ch])} → {len(notes)} total")

# ── regenerate merged book file + stats from per-chapter files ───────────────
print("\nRegenerating merged file + stats from per-chapter files …")

# ch.1 lives in its own file
all_notes = []
chapter_counts = {}
for ch in range(1, 69):
    path = DATA_DIR / f"sundara_ch{ch}_commentary_to_add.json"
    data = json.load(open(path, encoding='utf-8'))
    notes = [x for x in data if '_meta' not in x]
    all_notes.extend(notes)
    chapter_counts[ch] = len(notes)

# verse counts from corpus
corpus = [json.loads(l) for l in open(CORPUS, encoding='utf-8')]
verse_counts = collections.Counter()
for r in corpus:
    if r.get('seg') == 'sa':
        verse_counts[int(r['chapter'])] += 1
chapter_verse_counts = {ch: verse_counts.get(ch, 0) for ch in range(1, 69)}

all_notes.sort(key=lambda n: (int(n['shloka'].split('.')[1]), int(n['shloka'].split('.')[2])))

by_type    = collections.Counter(n['type'] for n in all_notes)
by_trigger = collections.Counter(n['trigger'] for n in all_notes)
by_prio    = collections.Counter(n['priority'] for n in all_notes)
noted_shlokas = set(n['shloka'] for n in all_notes)
total_verses  = sum(chapter_verse_counts.values())

book_meta = {
    "_meta": {
        "description": "Рекомендуемые примечания к параллельному Sa-Ru корпусу (Сундараканда, кн. V, гл. 1–68)",
        "rule": "Примечание добавляется ТОЛЬКО когда оно даёт то, чего нет в подстрочнике Леонова.",
        "evidence": "Все корпусные свидетельства — уровень шлоки (мягкое). Каждое примечание review_required.",
        "generated": TODAY,
        "gazetteer_supplement": f"{TODAY}: добавлены пропущенные именованные сущности (§09б formulas) — {len(added)} примечаний",
        "total_verses": total_verses,
        "total_notes": len(all_notes),
        "verses_with_note": len(noted_shlokas),
        "verses_without_note": total_verses - len(noted_shlokas),
        "by_type": dict(by_type),
        "by_trigger": dict(by_trigger),
        "by_priority": dict(by_prio),
        "per_chapter_notes": chapter_counts,
        "chapter_verse_counts": chapter_verse_counts,
    }
}
with open(DATA_DIR / "sundara_commentary_to_add.json", 'w', encoding='utf-8') as f:
    json.dump([book_meta] + all_notes, f, ensure_ascii=False, indent=2)

book_stats = {
    "total_verses": total_verses,
    "total_notes": len(all_notes),
    "verses_with_note": len(noted_shlokas),
    "verses_without_note": total_verses - len(noted_shlokas),
    "by_type": dict(by_type),
    "by_trigger": dict(by_trigger),
    "by_priority": dict(by_prio),
    "per_chapter_notes": chapter_counts,
    "chapter_verse_counts": chapter_verse_counts,
    "note": "All notes finished Russian text, review_required:true. First-appearance dedup book-wide. Includes gazetteer named-entity supplement.",
}
with open(DATA_DIR / "sundara_book_stats.json", 'w', encoding='utf-8') as f:
    json.dump(book_stats, f, ensure_ascii=False, indent=2)

# ── report ───────────────────────────────────────────────────────────────────
print(f"\n=== AFTER SUPPLEMENT ===")
print(f"Total notes: {len(all_notes)} (+{len(added)})")
print(f"Verses with note: {len(noted_shlokas)} / {total_verses}")
print(f"By type: {dict(by_type)}  By trigger: {dict(by_trigger)}  By priority: {dict(by_prio)}")
print(f"\nPer-chapter counts ch.17–68 (the previously near-empty range):")
for ch in range(17, 69):
    n = chapter_counts.get(ch, 0)
    vc = chapter_verse_counts.get(ch, 0)
    star = " *" if ch in affected_chapters else ""
    if n > 0:
        print(f"  ch.{ch:2d} ({vc:3d} v): {n}{star}")
