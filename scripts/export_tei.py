#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Экспорт размеченного корпуса в TEI P5 (шаг B3 дорожной карты).

Каждый файл data/<translator>_markup_50.json конвертируется в tei/<translator>.xml:
четырёхосная сетка объявляется как <taxonomy> в teiHeader, каждое примечание —
<note> с @target на CTS-URN стиха и @ana, ссылающимся на категории таксономий.

Полнотекстовая публикация авторизована (data/RIGHTS.md), поэтому raw_text
включается целиком.

Валидация: xmllint локально недоступен (см. CLAUDE.md), поэтому сигналом
корректности служит успешный разбор через ElementTree — той же конвенции
придерживается проект для XML-проверки csl.

Запуск:
    python scripts/export_tei.py
"""

import json
import re
import sys
import pathlib
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from taxonomy import (  # noqa: E402
    AXIS1_TOPICS, AXIS2_KAZANSKY, AXIS3_LAKSHANA, AXIS4_PARIBOK, assert_covers)

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "tei"

# Подписи категорий (TEI <catDesc>) — стиль «полное описание». КОДЫ берутся из
# схемы (taxonomy.py); assert_covers ниже падает, если подписи разойдутся со схемой.
AXIS2 = {
    "A": "филологический комментарий (язык, грамматика)",
    "B": "текстологический комментарий (варианты, источники)",
    "V": "историко-культурный комментарий (реалии, мифология)",
    "G": "культурологический / интерпретационный комментарий",
}
AXIS3 = {
    "L1": "именование (nāmadheya)", "L2": "толкование (vivaraṇa)",
    "L3": "связь (vākyayojanā)", "L4": "возражение (ākṣepa)",
    "L5": "контекст / смысл целого (samanvaya)",
}
AXIS4 = {
    "P": "понятие (translatable concept)",
    "K": "кодификатор направления деятельности (Парибок)",
    "D": "концепт-расхождение (несоизмеримость)",
}
# Список тем axis_1 — напрямую из схемы (без хардкод-копии).
AXIS1 = list(AXIS1_TOPICS)

# Защита от дрейфа: подписи обязаны покрывать ровно коды схемы.
assert_covers(AXIS2, AXIS2_KAZANSKY, "export_tei.AXIS2")
assert_covers(AXIS3, AXIS3_LAKSHANA, "export_tei.AXIS3")
assert_covers(AXIS4, AXIS4_PARIBOK, "export_tei.AXIS4")


def ncname(s):
    """comment_id → валидный xml:id (NCName): слэши→подчёркивания."""
    out = re.sub(r"[^\w.-]", "_", s)
    # NCName должен начинаться с буквы/подчёркивания; пустой → не упасть на out[0].
    return out if out and (out[0].isalpha() or out[0] == "_") else "x" + out


def cat(cid, desc):
    return f'        <category xml:id="{cid}"><catDesc>{escape(desc)}</catDesc></category>'


def build_header(translator, n):
    taxos = []
    taxos.append('      <taxonomy xml:id="axis2_kazansky">')
    taxos.append('        <desc>Ось 2 — тип комментария (номенклатура Н. Н. Казанского)</desc>')
    taxos += [cat(f"a2_{k}", v) for k, v in AXIS2.items()]
    taxos.append('      </taxonomy>')
    taxos.append('      <taxonomy xml:id="axis3_lakshana">')
    taxos.append('        <desc>Ось 3 — пять lakṣaṇa комментаторской традиции</desc>')
    taxos += [cat(f"lak_{k}", v) for k, v in AXIS3.items()]
    taxos.append('      </taxonomy>')
    taxos.append('      <taxonomy xml:id="axis4_paribok">')
    taxos.append('        <desc>Ось 4 — категориальный статус термина (модель А. В. Парибка)</desc>')
    taxos += [cat(f"par_{k}", v) for k, v in AXIS4.items()]
    taxos.append('      </taxonomy>')
    taxos.append('      <taxonomy xml:id="axis1_topic">')
    taxos.append('        <desc>Ось 1 — тематическая рубрика примечания</desc>')
    taxos += [cat(f"top_{t}", t) for t in AXIS1]
    taxos.append('      </taxonomy>')
    taxo_block = "\n".join(taxos)
    return f"""  <teiHeader>
    <fileDesc>
      <titleStmt>
        <title>Комментаторский аппарат: {escape(translator)} (золотая выборка, {n} примечаний)</title>
        <respStmt><resp>разметка</resp><name>CommentaryStrategies</name></respStmt>
      </titleStmt>
      <publicationStmt>
        <p>Корпус CommentaryStrategies. Полнотекстовая публикация авторизована
           2026-06-12 (см. data/RIGHTS.md). Лицензия данных — отдельно от лицензии кода.</p>
      </publicationStmt>
      <sourceDesc>
        <p>Размеченная выборка примечаний переводчика «{escape(translator)}»;
           адресация стихов — CTS-URN (scripts/derive_urn.py).</p>
      </sourceDesc>
    </fileDesc>
    <encodingDesc>
      <classDecl>
{taxo_block}
      </classDecl>
    </encodingDesc>
  </teiHeader>"""


def build_note(rec):
    xmlid = ncname(rec["comment_id"])
    urn = rec.get("urn", "")
    ana = [f"#a2_{rec['axis_2_kazansky']}", f"#par_{rec['axis_4_paribok']}"]
    ana += [f"#lak_{l}" for l in rec.get("axis_3_lakshana", [])]
    ana += [f"#top_{t}" for t in rec.get("axis_1_topic", [])]
    rend = ' rend="iast"' if rec.get("has_iast") else ""
    attrs = (f'xml:id="{xmlid}" target="{escape(urn)}" '
             f'type="{rec["axis_2_kazansky"]}" ana="{" ".join(ana)}" '
             f'n="{escape(rec["shloka_addr"])}"{rend}')
    body = escape(rec.get("raw_text", ""))
    bibls = ""
    for src in rec.get("cited_indian_commentators", []):
        bibls += f'\n        <bibl type="indian_commentator">{escape(src)}</bibl>'
    for src in rec.get("cited_western_sources", []):
        bibls += f'\n        <bibl type="western_source">{escape(src)}</bibl>'
    return f"      <note {attrs}>{body}{bibls}</note>"


def build_tei(translator, records):
    # Уникальность xml:id: разные comment_id могут схлопнуться в один ncname
    # (слэш/двоеточие/пробел → «_»). Дубль xml:id = невалидный XML, который
    # ET.fromstring НЕ ловит, — проверяем явно.
    ids = [ncname(r.get("comment_id", "")) for r in records]
    dupes = sorted({x for x in ids if ids.count(x) > 1})
    if dupes:
        raise ValueError(f"export_tei[{translator}]: дублирующиеся xml:id {dupes}")
    notes = "\n".join(build_note(r) for r in records)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
{build_header(translator, len(records))}
  <text>
    <body>
      <listAnnotation>
{notes}
      </listAnnotation>
    </body>
  </text>
</TEI>
"""


def main():
    OUT.mkdir(exist_ok=True)
    files = sorted(DATA.glob("*_markup_50.json"))
    total = 0
    for path in files:
        records = json.loads(path.read_text(encoding="utf-8"))
        translator = records[0]["translator"]
        xml = build_tei(translator, records)
        # Валидация: разбор через ElementTree
        try:
            ET.fromstring(xml)
        except ET.ParseError as e:
            print(f"✗ {path.name}: ОШИБКА разбора TEI — {e}")
            continue
        dest = OUT / f"{translator}.xml"
        dest.write_text(xml, encoding="utf-8", newline="\n")
        total += len(records)
        print(f"✓ {dest.relative_to(ROOT)}  ({len(records)} note, ET parse OK)")
    print(f"\nЭкспортировано {total} примечаний в TEI P5. Валидация: ET parse OK.")


if __name__ == "__main__":
    main()
