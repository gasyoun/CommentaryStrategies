#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Структурирование формульно-эпитетного слоя Рамаяны (шаг C2 дорожной карты).

Преобразует рукописный перечень ramayana-leonov/ramayana-formulas_1-2.md
(жирное имя — эпитеты через «;») в структурированный JSON: лемма, список
эпитетов, число эпитетов, наличие квадратных уточнений составителей, индекс
омонима. Групповые рубрики (имя оканчивается на «:») выделяются отдельно.

Формульный слой нужен при любой модели комментария Сундараканды (он питает
ярус-2 / цифровой аппарат и систематическую обработку эпитетов де Йонга), поэтому
шаг не зависит от решения D2.

Кросоволок с IAST (26-08-2026, H3558). Перечень книг 1–2 сам по себе НЕ несёт
построфных адресов — ни в источнике, ни в разобранном виде, поэтому собственный
CTS-URN эпитетной статье приписать неоткуда. Что здесь делается вместо этого:
леммы эпитетов из sources/leonov_notes.json (кн. V, IAST + shloka_addr) сводятся
с русскими эпитетами книг 1–2 по нормализованному глоссу, и совпадение пишется
в поле iast_crosswalk как ЗАСВИДЕТЕЛЬСТВОВАННОЕ УПОТРЕБЛЕНИЕ ЛЕММЫ в книге V —
не как адрес самой статьи. Связь лемматическая, не референтная: dhīmān засвиде-
тельствован в 5.1.3 о Ханумане, а «мудрый» в книгах 1–2 стоит при Бхарате,
Вишвамитре, Куше и Ману. Поле отвечает на вопрос «как этот русский эпитет звучит
в санскрите и где это видно», а не «где стоит этот эпитет в книгах 1–2».

Запуск:
    python scripts/parse_formulas.py
"""

import json
import re
import sys
import pathlib
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from derive_urn import derive  # noqa: E402  (CTS-URN из shloka_addr, шаг B2)

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "ramayana-leonov" / "ramayana-formulas_1-2.md"
NOTES = ROOT / "sources" / "leonov_notes.json"
OUT = ROOT / "data" / "ramayana_epithets.json"

# Грубая оценка из преамбулы файла: ~300 у нас vs. 459 в «Словаре имён» Гринцера.
GRINTSER_DICT_ENTRIES = 459

BOLD = re.compile(r"^\*\*(.+?)\*\*\s*(.*)$")

# Лемма в примечании Костиной стоит в скобках после русского глосса:
# «О губитель врагов (śatrukarśana) — букв. …» → глосс «О губитель врагов»,
# лемма «śatrukarśana». Скобку без диакритики отбрасываем (это не IAST).
IAST_PAREN = re.compile(r"\(([^()]{2,60})\)")
IAST_DIACRITIC = re.compile(r"[āīūṛṝḷḹṅñṭḍṇśṣḥṁṃ]")


def norm_gloss(s):
    """Нормализовать русский глосс для сопоставления: регистр, ё, скобочные
    уточнения составителей, ведущее звательное «О »."""
    s = s.lower().replace("ё", "е")
    s = re.sub(r"\[[^\]]*\]", " ", s)
    s = re.sub(r"[^а-я\s-]", " ", s)
    s = re.sub(r"^\s*о\s+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def load_crosswalk():
    """sources/leonov_notes.json → [{lemma, gloss_ru, urn, shloka_addr}].

    Порядок исходного файла сохраняется; повторы (лемма, urn) снимаются.
    Адрес переводится в CTS-URN тем же derive(), что и золотая выборка.
    """
    if not NOTES.is_file():
        return []
    notes = json.loads(NOTES.read_text(encoding="utf-8"))
    out, seen = [], set()
    for n in notes:
        m = IAST_PAREN.search(n.get("raw_text", ""))
        if not m:
            continue
        lemma = m.group(1).strip()
        if not IAST_DIACRITIC.search(lemma):
            continue
        gloss = n["raw_text"][: m.start()].strip()
        urn, ok, _ = derive(n.get("shloka_addr", ""))
        if not ok:
            continue
        key = (lemma, urn)
        if key in seen:
            continue
        seen.add(key)
        out.append({"lemma": lemma, "gloss_ru": gloss,
                    "urn": urn, "shloka_addr": n["shloka_addr"]})
    return out


def attach_crosswalk(records, cross):
    """Приписать эпитетным статьям поле iast_crosswalk по совпадению глосса.

    Совпадение лемматическое: лемма засвидетельствована в книге V по указанному
    адресу — это НЕ адрес самой статьи и НЕ утверждение, что в 5.x.y эпитет
    отнесён к тому же персонажу. См. докстринг модуля.
    """
    by_gloss = {}
    for c in cross:
        by_gloss.setdefault(norm_gloss(c["gloss_ru"]), []).append(c)
    matched = 0
    attestations = 0
    for rec in records:
        if rec["type"] != "epithet":
            continue
        links, seen = [], set()
        for epi in rec["epithets"]:
            for c in by_gloss.get(norm_gloss(epi), []):
                key = (epi, c["lemma"], c["urn"])
                if key in seen:
                    continue
                seen.add(key)
                links.append({
                    "epithet": epi,
                    "lemma": c["lemma"],
                    "gloss_ru": c["gloss_ru"],
                    "attested_urn": c["urn"],
                    "attested_addr": c["shloka_addr"],
                    "source": "sources/leonov_notes.json",
                })
        if links:
            rec["iast_crosswalk"] = links
            matched += 1
            attestations += len(links)
    return matched, attestations


def clean_name(raw):
    """Снять обрамляющие пробелы, экранированный/обычный дефис, двоеточие."""
    name = raw.strip()
    is_group = name.endswith(":")
    name = re.sub(r"[\s:]*\\?-?\s*$", "", name).strip()
    name = name.rstrip(":").strip()
    return name, is_group


def unescape_md(s):
    """Снять markdown-экранирование: \\[ \\] \\- \\( \\) → [ ] - ( )."""
    return re.sub(r"\\([\[\]\-()])", r"\1", s)


def clean_rest(rest):
    """Снять ведущий дефис (если он стоял после жирного имени)."""
    return re.sub(r"^\s*\\?-\s*", "", rest).strip()


def parse(text):
    entries = []
    cur = None
    started = False
    for line in text.splitlines():
        m = BOLD.match(line)
        if m:
            started = True
            if cur:
                entries.append(cur)
            name, is_group = clean_name(m.group(1))
            cur = {"name": name, "is_group": is_group,
                   "content": clean_rest(m.group(2))}
        elif not line.strip():
            # Пустая строка = граница абзаца (markdown): закрываем текущую статью.
            # Без этого хвостовая редакторская проза (стр./«кто это?»/заметки),
            # отделённая пустой строкой, прилипала к последней статье.
            if cur:
                entries.append(cur)
                cur = None
        elif started and cur is not None:
            # Мягкий перенос ВНУТРИ статьи (непрерывные строки без пустой между).
            cur["content"] += " " + line.strip()
    if cur:
        entries.append(cur)
    return entries


def finalize(entries):
    name_counts = Counter(e["name"] for e in entries)
    seen = Counter()
    out = []
    for e in entries:
        content = unescape_md(e["content"].strip())
        has_bracket = bool(re.search(r"\[[^\]]+\]", content))
        rec = {"name": e["name"]}
        if name_counts[e["name"]] > 1:
            seen[e["name"]] += 1
            rec["homonym_index"] = seen[e["name"]]
        if e["is_group"]:
            rec["type"] = "group"
            members = [m.strip() for m in re.split(r"[;\n]", content) if m.strip()]
            rec["members"] = members
            rec["n_members"] = len(members)
        else:
            rec["type"] = "epithet"
            epithets = [p.strip() for p in content.split(";") if p.strip()]
            rec["epithets"] = epithets
            rec["n_epithets"] = len(epithets)
            rec["has_bracket_note"] = has_bracket
        out.append(rec)
    return out


def main():
    text = SRC.read_text(encoding="utf-8")
    records = finalize(parse(text))
    cross = load_crosswalk()
    matched, attestations = attach_crosswalk(records, cross)
    epi = [r for r in records if r["type"] == "epithet"]
    grp = [r for r in records if r["type"] == "group"]
    distinct = len({r["name"] for r in epi})
    homonyms = sorted({r["name"] for r in epi if r.get("homonym_index")})

    payload = {
        "source": "ramayana-leonov/ramayana-formulas_1-2.md",
        "books": "1-2 (Bāla, Ayodhyā)",
        "generated_by": "scripts/parse_formulas.py",
        "entry_count": len(records),
        "epithet_entries": len(epi),
        "distinct_named_characters": distinct,
        "group_entries": len(grp),
        "homonym_names": homonyms,
        "grintser_dictionary_entries": GRINTSER_DICT_ENTRIES,
        "iast_crosswalk_source": "sources/leonov_notes.json",
        "iast_crosswalk_note": (
            "Поле iast_crosswalk у статьи — засвидетельствованные употребления "
            "санскритской леммы в книге V (Сундараканда) с CTS-URN, а НЕ адрес "
            "самой статьи: перечень книг 1–2 построфных адресов не несёт. "
            "Связь лемматическая, не референтная — dhīmān засвидетельствован в "
            "5.1.3 о Ханумане, тогда как русский эпитет «мудрый» в книгах 1–2 "
            "стоит при Бхарате, Вишвамитре, Куше и Ману. Сопоставление идёт по "
            "нормализованному русскому глоссу примечания."
        ),
        "iast_crosswalk_lemmas": len({c["lemma"] for c in cross}),
        "iast_crosswalk_matched_entries": matched,
        "iast_crosswalk_attestations": attestations,
        "entries": records,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                   encoding="utf-8", newline="\n")

    print(f"Записано: {OUT.relative_to(ROOT)}")
    print(f"  всего статей:           {len(records)}")
    print(f"  эпитетных статей:       {len(epi)}")
    print(f"  различных персонажей:   {distinct}")
    print(f"  групповых рубрик:       {len(grp)}")
    print(f"  имён-омонимов:          {len(homonyms)}  {homonyms[:8]}")
    total_epi = sum(r["n_epithets"] for r in epi)
    print(f"  всего эпитетов:         {total_epi}")
    print(f"  IAST-лемм из кн. V:     {len({c['lemma'] for c in cross})} "
          f"(из {len(cross)} пар лемма↔адрес)")
    print(f"  статей с кросоволоком:  {matched}  (засвидетельствований: {attestations})")
    print(f"\n  Гринцер «Словарь имён»: {GRINTSER_DICT_ENTRIES} статей")
    print(f"  расхождение:            {GRINTSER_DICT_ENTRIES - distinct} "
          f"(см. EPITHET_LAYER.md о причинах: Шива=Рудра, сыновья не вынесены, горы)")


if __name__ == "__main__":
    main()
