#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Полная RelaxNG-валидация tei/*.xml против схемы tei_all (шаг B3 дорожной карты).

Экспортер export_tei.py проверяет выгрузку разбором через ElementTree — это
ловит только неправильную форму XML, но не нарушение контентной модели TEI.
Настоящую проверку даёт RelaxNG-схема tei_all.

Где взять схему (1,05 МБ, в репозиторий не кладётся): файл
xml/tei/custom/schema/relaxng/tei_all.rng из релиза TEI P5
(https://github.com/TEIC/TEI/releases).

Порядок поиска схемы: --schema → $TEI_ALL_RNG → schema/tei_all.rng.
Схемы или xmllint нет — печатается SKIP и код возврата 0 (шаг необязателен в
окружении без схемы); настоящая ошибка валидации — код возврата 1.

Запуск:
    TEI_ALL_RNG=/path/to/tei_all.rng python scripts/validate_tei_rng.py
"""

import os
import shutil
import subprocess
import sys
import pathlib

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEI = ROOT / "tei"


def find_schema(argv):
    for i, a in enumerate(argv):
        if a == "--schema" and i + 1 < len(argv):
            return pathlib.Path(argv[i + 1])
        if a.startswith("--schema="):
            return pathlib.Path(a.split("=", 1)[1])
    env = os.environ.get("TEI_ALL_RNG")
    if env:
        return pathlib.Path(env)
    return ROOT / "schema" / "tei_all.rng"


def main():
    if not shutil.which("xmllint"):
        print("SKIP: xmllint не найден в PATH — RNG-валидация пропущена.")
        return 0

    schema = find_schema(sys.argv[1:])
    if not schema.is_file():
        print(f"SKIP: схема tei_all не найдена ({schema}).")
        print("      Путь задаётся через --schema или $TEI_ALL_RNG (см. docstring).")
        return 0

    files = sorted(TEI.glob("*.xml"))
    if not files:
        print("SKIP: в tei/ нет файлов — сначала python scripts/export_tei.py")
        return 0

    print(f"Схема: {schema} ({schema.stat().st_size} байт)")
    failed = []
    for path in files:
        proc = subprocess.run(
            ["xmllint", "--noout", "--relaxng", str(schema), str(path)],
            capture_output=True, text=True,
        )
        if proc.returncode == 0:
            print(f"✓ {path.relative_to(ROOT)} — валиден по tei_all")
        else:
            failed.append(path)
            print(f"✗ {path.relative_to(ROOT)} — НЕ валиден:")
            for line in proc.stderr.strip().splitlines():
                print(f"    {line}")

    print(f"\nПроверено {len(files)} файлов, ошибок: {len(failed)}.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
