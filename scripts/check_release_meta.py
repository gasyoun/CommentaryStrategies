#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Паритет релизных метаданных: CITATION.cff ↔ .zenodo.json ↔ git-теги (шаг B6).

Ловит класс дрифта, найденный drain-проходом A05 (29-08-2026): .zenodo.json
нес версию «1.2.0» (это был номер cff-version, а не релиза), тогда как
CITATION.cff и git-теги жили на 1.26.1. Zenodo-интеграция берёт версию из
тега GitHub-релиза, но рукописные поля в двух файлах обязаны совпадать между
собой — иначе цитирование (CITATION.cff) и депозитные метаданные (Zenodo)
расходятся незаметно.

Проверки:
  1. Оба файла существуют и разбираются (JSON / ключи CFF 1.2.0).
  2. Структурный минимум: title, license, version в обоих; creators с ORCID
     в .zenodo.json; date-released формата YYYY-MM-DD в CITATION.cff.
  3. Жёсткий паритет: version в .zenodo.json == version в CITATION.cff.
  4. Мягкий паритет с тегами: если git-теги видны (неглубокий checkout в CI
     их не несёт — тогда SKIP), последний тег vX.Y.Z сверяется с версией;
     расхождение — WARNING, не отказ (легальный интервал между release-
     коммитом и постановкой тега).

Запуск (в CI — шаг «Release metadata parity» job'а Corpus integrity):
    python scripts/check_release_meta.py [--check]

--check — принят как алиас дефолта (конвенция --emit/--check в репо);
проверка ничего не пишет и не чинит, только диагностирует.
"""

import json
import pathlib
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
CFF = ROOT / "CITATION.cff"
ZENODO = ROOT / ".zenodo.json"

REQUIRED_CFF = ("cff-version", "title", "version", "license", "date-released")
REQUIRED_ZENODO = ("title", "upload_type", "license", "version", "creators")


def parse_cff(path):
    """Минимальный разбор CFF: 'ключ: значение' верхнего уровня."""
    fields = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^([a-z][a-z0-9-]*):\s*(.*)$", line)
        if m and m.group(1) not in fields:
            fields[m.group(1)] = m.group(2).strip().strip('"')
    return fields


def latest_tag():
    """Последний релизный тег vX.Y.Z по semver; None, если тегов нет/недоступны.

    git describe не подходит: репо несёт служебные теги (reserve-*, …),
    и по дистанции графа он выберет их, а не релиз. Сортируем версионно
    сами и берём только v-теги с цифровой старшей частью.
    """
    try:
        proc = subprocess.run(
            ["git", "for-each-ref", "--sort=-v:refname",
             "--format=%(refname:short)", "refs/tags/v[0-9]*"],
            cwd=ROOT, capture_output=True, text=True, timeout=10,
        )
        if proc.returncode != 0:
            return None
        for tag in proc.stdout.splitlines():
            tag = tag.strip()
            if re.fullmatch(r"v\d+\.\d+\.\d+", tag):
                return tag
        return None
    except (OSError, subprocess.TimeoutExpired):
        return None


def main():
    # --check — алиас дефолта (конвенция --emit/--check в репо): проверка
    # ничего не пишет и не чинит, только диагностирует.
    defects, warnings = [], []

    if not CFF.is_file():
        defects.append(f"нет файла {CFF.relative_to(ROOT)}")
    if not ZENODO.is_file():
        defects.append(f"нет файла {ZENODO.relative_to(ROOT)}")
    if defects:
        print("FAIL: " + "; ".join(defects))
        return 1

    try:
        zen = json.loads(ZENODO.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        print(f"FAIL: {ZENODO.relative_to(ROOT)} не разбирается как JSON: {e}")
        return 1
    cff = parse_cff(CFF)

    missing_cff = [k for k in REQUIRED_CFF if k not in cff or not cff[k]]
    if missing_cff:
        defects.append(f"CITATION.cff: нет ключей {', '.join(missing_cff)}")
    missing_zen = [k for k in REQUIRED_ZENODO if not zen.get(k)]
    if missing_zen:
        defects.append(f".zenodo.json: нет ключей {', '.join(missing_zen)}")
    if "creators" in zen and not any(c.get("orcid") for c in zen["creators"]):
        defects.append(".zenodo.json: у creators нет ни одного orcid")
    if cff.get("date-released") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", cff["date-released"]):
        defects.append(f"CITATION.cff: date-released не YYYY-MM-DD ({cff['date-released']!r})")

    cff_ver, zen_ver = cff.get("version"), str(zen.get("version", ""))
    if cff_ver and zen_ver and cff_ver != zen_ver:
        defects.append(
            f"дрифт версии: CITATION.cff {cff_ver} != .zenodo.json {zen_ver}"
            " (класс ловушки: в .zenodo.json стоял cff-version вместо релиза)"
        )

    tag = latest_tag()
    if tag is None:
        print("SKIP: git-теги недоступны (неглубокий checkout) — сверены только файлы.")
    else:
        tag_ver = tag.lstrip("v")
        if cff_ver and tag_ver != cff_ver:
            warnings.append(
                f"последний тег {tag} != CITATION.cff {cff_ver}"
                " — легально между release-коммитом и тегом, иначе синхронизируйте"
            )

    for w in warnings:
        print(f"WARNING: {w}")
    if defects:
        for d in defects:
            print(f"FAIL: {d}")
        print(f"\nПроверка релизных метаданных: дефектов {len(defects)}.")
        return 1

    print(f"✓ CITATION.cff {cff_ver} ↔ .zenodo.json {zen_ver} — версии в паритете")
    print(f"✓ структурный минимум обоих файлов присутствует"
          f"{f'; последний тег {tag}' if tag else ''}")
    print("Проверка релизных метаданных: PASS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
