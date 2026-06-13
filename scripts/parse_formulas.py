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

Запуск:
    python scripts/parse_formulas.py
"""

import json
import re
import sys
import pathlib
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "ramayana-leonov" / "ramayana-formulas_1-2.md"
OUT = ROOT / "data" / "ramayana_epithets.json"

# Грубая оценка из преамбулы файла: ~300 у нас vs. 459 в «Словаре имён» Гринцера.
GRINTSER_DICT_ENTRIES = 459

BOLD = re.compile(r"^\*\*(.+?)\*\*\s*(.*)$")


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
        elif started and cur is not None and line.strip():
            # продолжение текущей статьи (мягкий перенос внутри записи)
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
        "entries": records,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                   encoding="utf-8")

    print(f"Записано: {OUT.relative_to(ROOT)}")
    print(f"  всего статей:           {len(records)}")
    print(f"  эпитетных статей:       {len(epi)}")
    print(f"  различных персонажей:   {distinct}")
    print(f"  групповых рубрик:       {len(grp)}")
    print(f"  имён-омонимов:          {len(homonyms)}  {homonyms[:8]}")
    total_epi = sum(r["n_epithets"] for r in epi)
    print(f"  всего эпитетов:         {total_epi}")
    print(f"\n  Гринцер «Словарь имён»: {GRINTSER_DICT_ENTRIES} статей")
    print(f"  расхождение:            {GRINTSER_DICT_ENTRIES - distinct} "
          f"(см. EPITHET_LAYER.md о причинах: Шива=Рудра, сыновья не вынесены, горы)")


if __name__ == "__main__":
    main()
