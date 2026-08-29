#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Перепись и охрана отслеживаемых бинарников: census → гейт анти-роста →
guarded upload в релизы (шаг B6, «большие .docx/.pdf — в релизы»).

Замер 26-08-2026 (drain A05): отслеживаемых бинарников ≈ 21,8 МБ, из них
20 МБ — один файл, tronsky-XXX/sources/kazansky_1987.pdf (скан чужой статьи).
Выкладка релизным ассетом = публикация охраняемого текста, т. е. правовое
решение человека (Дорожка C), а не механический перенос. Этот скрипт делает
механическую половину и держит границу:

  census   — пересчёт отслеживаемых бинарников с вердиктами классификации;
  --emit   — записать перепись в data/binary_census.json (derive-don't-store);
  --check  — гейт: новый отслеживаемый бинарник без классификации = отказ.
             Так замер 26-08 перестаёт быть разовым — молча накопить ещё
             20 МБ сканов больше нельзя (прецеденты дисциплины: H2832 —
             сканы Goldman в .gitignore, H3558 — веб-дампы выведены из git);
  upload   — выкладка ассетами релиза ТОЛЬКО по явному allowlist владельца,
             dry-run по умолчанию; файлы класса rights не проходят без
             --rights-cleared (бумажное/письменное разрешение — не флаг,
             флаг лишь фиксирует, что оно у владельца есть).

Классификация живёт здесь, в VERDICTS, а не в переписи: перепись — Derived
данные (размеры меняются), вердикты — решения. Новый бинарник обязан получить
вердикт в VERDICTS и перезаписать перепись одним PR, иначе --check красный.

Запуск:
    python scripts/release_binaries.py              # census (таблица + итог)
    python scripts/release_binaries.py --emit       # data/binary_census.json
    python scripts/release_binaries.py --check      # CI-гейт
    python scripts/release_binaries.py upload \
        --release v1.27.0 --allowlist allowlist.txt # dry-run (без --execute)
"""

import argparse
import json
import pathlib
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
CENSUS = ROOT / "data" / "binary_census.json"

# ---- классификация (решения, не данные) -----------------------------------
# rights  — скан чужого охраняемого текста: в релиз только при письменном
#           разрешении правообладателя (Дорожка C); см. docs/BINARY_RELEASES.md
# timing  — собственная рукопись, но неопубликованная (книга ЛП не вышла,
#           соавтор/анонимизация): момент выкладки решает владелец
# build-input — функциональный вход сборки (pandoc reference): остаётся в git,
#           релизным ассетом быть не должен
VERDICTS = {
    "tronsky-XXX/sources/kazansky_1987.pdf": "rights",
    "ramayana-leonov/02_Lidova_31-66.pdf": "rights",
    "data/book/sundarakanda_print_master.docx": "timing",
    "tronsky-XXX/CommentaryStrategies_Tronsky30_Kostina.docx": "timing",
    "tronsky-XXX/archive/CommentaryStrategies-Tronsky30.docx": "timing",
    "tronsky-XXX/article_v_tronsky_anon.docx": "timing",
    "tronsky-XXX/scripts/custom-reference.docx": "build-input",
    "tronsky-XXX/scripts/tronsky_reference.docx": "build-input",
}

VERDICT_LABEL = {
    "rights": "правовая дорожка C (скан чужого текста)",
    "timing": "решение о моменте публикации (неопубликованная рукопись)",
    "build-input": "вход сборки — остаётся в git, не ассет",
}

# ---- распознавание бинарников ----------------------------------------------
MAGIC = (
    b"%PDF",            # pdf
    b"PK\x03\x04",      # zip-семейство: docx/xlsx/pptx/epub/odt
    b"\xd0\xcf\x11\xe0",  # старое OLE: .doc/.xls/.ppt
    b"7z\xbc\xaf\x27\x1c",
    b"Rar!",
    b"\x1f\x8b",        # gzip
    b"BZh",             # bzip2
    b"\xfd7zXZ\x00",    # xz
    b"AT&TFORM",        # djvu
)
BIN_EXT = {".pdf", ".docx", ".doc", ".xlsx", ".pptx", ".epub", ".djvu",
           ".zip", ".7z", ".rar", ".gz", ".bz2", ".xz"}


def tracked_files():
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True,
                         text=True, check=True).stdout
    return [line for line in out.splitlines() if line]


def is_binary(path):
    """По магическим байтам; расширение — только дополнительный сигнал
    (пустой файл с именем .docx всё равно аномалия, поймает VERDICTS-гейт)."""
    try:
        with open(ROOT / path, "rb") as fh:
            head = fh.read(8)
    except OSError:
        return False
    if any(head.startswith(m) for m in MAGIC):
        return True
    return pathlib.Path(path).suffix.lower() in BIN_EXT and head


def census():
    """[(path, bytes, verdict_or_None)] по отслеживаемым бинарникам."""
    rows = []
    for path in tracked_files():
        if not is_binary(path):
            continue
        size = (ROOT / path).stat().st_size
        rows.append((path, size, VERDICTS.get(path)))
    rows.sort()
    return rows


def print_census(rows):
    total = sum(size for _, size, _ in rows)
    print(f"Отслеживаемых бинарников: {len(rows)}, "
          f"{total} байт ≈ {total / 1048576:.1f} МБ")
    for path, size, verdict in rows:
        label = VERDICT_LABEL.get(verdict, "БЕЗ КЛАССИФИКАЦИИ")
        print(f"  {size / 1048576:7.2f} МБ  {path}  [{label}]")
    return total


def cmd_emit(rows):
    total = sum(size for _, size, _ in rows)
    payload = {
        "_comment": "Derived: scripts/release_binaries.py --emit — не править руками",
        "total_bytes": total,
        "files": {path: size for path, size, _ in rows},
    }
    CENSUS.write_text(json.dumps(payload, ensure_ascii=False, indent=2,
                                 sort_keys=True) + "\n", encoding="utf-8")
    print(f"записано {CENSUS.relative_to(ROOT)}: {len(rows)} файлов, "
          f"{total / 1048576:.1f} МБ")


def cmd_check(rows):
    fail = 0
    known = {}
    if CENSUS.exists():
        known = json.loads(CENSUS.read_text(encoding="utf-8"))["files"]
    else:
        print(f"ОТКАЗ: {CENSUS.relative_to(ROOT)} нет — прогоните --emit и "
              f"закоммитьте перепись")
        fail = 1
    for path, size, verdict in rows:
        if verdict is None:
            print(f"ОТКАЗ: {path} — новый отслеживаемый бинарник без вердикта; "
                  f"внесите вердикт в VERDICTS (release_binaries.py), "
                  f"перезапишите перепись (--emit) — всё одним PR; "
                  f"если файл не должен жить в git, добавьте правило в "
                  f".gitignore (прецеденты H2832, H3558)")
            fail = 1
        elif path not in known:
            print(f"ОТКАЗ: {path} — есть в VERDICTS, но нет в переписи; "
                  f"прогоните --emit в том же PR")
            fail = 1
        elif known.get(path) != size:
            print(f"ВНИМАНИЕ: {path} — размер изменился "
                  f"({known[path]} → {size} байт); перепись обновится "
                  f"следующим --emit, гейт не блокирует")
    if not fail:
        print(f"Гейт пройден: {len(rows)} бинарников, все классифицированы, "
              f"перепись актуальна")
    return fail


def cmd_upload(args):
    rows = census()
    by_path = {path: (size, verdict) for path, size, verdict in rows}
    if not args.release:
        print("ОТКАЗ: укажите --release vX.Y.Z")
        return 1
    if not args.allowlist:
        print("ОТКАЗ: выкладка только по явному allowlist владельца "
              "(--allowlist FILE, по одному пути на строку); "
              "кандидаты и их вердикты — docs/BINARY_RELEASES.md")
        return 1
    wanted = [line.strip() for line in
              pathlib.Path(args.allowlist).read_text(encoding="utf-8")
              .splitlines() if line.strip() and not line.startswith("#")]
    if not wanted:
        print("ОТКАЗ: allowlist пуст")
        return 1
    plan = []
    for path in wanted:
        if path not in by_path:
            print(f"ОТКАЗ: {path} нет среди отслеживаемых бинарников")
            return 1
        _, verdict = by_path[path]
        if verdict == "build-input":
            print(f"ОТКАЗ: {path} — вход сборки, в релизы не выкладывается")
            return 1
        if verdict == "rights" and not args.rights_cleared:
            print(f"ОТКАЗ: {path} — скан чужого охраняемого текста; без "
                  f"--rights-cleared (разрешение правообладателя у владельца) "
                  f"механический перенос запрещён — Дорожка C")
            return 1
        plan.append(path)
    print(f"Релиз {args.release}: к выкладке {len(plan)} файл(ов):")
    for path in plan:
        print(f"  {by_path[path][0] / 1048576:7.2f} МБ  {path}")
    if not args.execute:
        print("dry-run: ничего не выложено. Для реальной выкладки добавьте "
              "--execute (используется gh release upload)")
        return 0
    subprocess.run(["gh", "release", "upload", args.release, *plan,
                    "--clobber"], cwd=ROOT, check=True)
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--emit", action="store_true",
                        help="записать data/binary_census.json")
    parser.add_argument("--check", action="store_true",
                        help="CI-гейт анти-роста")
    sub = parser.add_subparsers(dest="cmd")
    up = sub.add_parser("upload", help="выкладка ассетами релиза по allowlist")
    up.add_argument("--release", help="тег релиза, например v1.27.0")
    up.add_argument("--allowlist", help="файл путей (по одному на строку)")
    up.add_argument("--execute", action="store_true",
                    help="реальная выкладка через gh release upload")
    up.add_argument("--rights-cleared", action="store_true",
                    help="разрешение правообладателя получено (Дорожка C "
                         "закрыта владельцем); без него класс rights не "
                         "проходит никогда")
    args = parser.parse_args()
    rows = census()
    total = print_census(rows)
    if args.emit:
        return cmd_emit(rows)
    if args.check:
        return cmd_check(rows)
    if args.cmd == "upload":
        return cmd_upload(args)
    unclassified = [path for path, _, verdict in rows if verdict is None]
    if unclassified:
        print(f"\nБЕЗ КЛАССИФИКАЦИИ: {unclassified} — гейт --check красный")
        return 1
    print(f"\nитог: {total / 1048576:.1f} МБ; правовая дорожка C / решение о "
          f"выкладке — docs/BINARY_RELEASES.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
