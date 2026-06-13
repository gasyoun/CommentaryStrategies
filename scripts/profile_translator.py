#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Профилировщик переводчика по 4-осной разметке.

Считает распределения по 4 осям, длины примечаний, долю IAST и тематические
доли для одного или нескольких размеченных JSON-файлов (data/*_markup_50.json).
Чисто детерминированный подсчёт — без обращений к LLM.

Использование:
    python scripts/profile_translator.py grintser
    python scripts/profile_translator.py grintser vassilkov kalyanov   # сравнение

Это шаг C0.1 дорожной карты (docs/ROADMAP_2026H2.md): операционализировать
«комментировать по Гринцеру» как измеримый профиль-ориентир для Сундараканды.
"""

import json
import statistics
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

AXIS2_LABELS = {
    "A": "филологический (A)",
    "B": "текстологический (B)",
    "V": "историко-культурный (V)",
    "G": "культурологический (G)",
}
AXIS4_LABELS = {
    "P": "понятие (P)",
    "K": "кодификатор (K)",
    "D": "концепт-расхождение (D)",
}


def load(name):
    path = DATA_DIR / f"{name}_markup_50.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def profile(name, records):
    n = len(records)
    lengths = [len(r.get("raw_text", "")) for r in records]
    iast = sum(1 for r in records if r.get("has_iast"))
    topics = Counter(t for r in records for t in r.get("axis_1_topic", []))
    axis2 = Counter(r.get("axis_2_kazansky") for r in records)
    axis3 = Counter(l for r in records for l in r.get("axis_3_lakshana", []))
    axis4 = Counter(r.get("axis_4_paribok") for r in records)
    multi_topic = sum(1 for r in records if len(r.get("axis_1_topic", [])) > 1)

    return {
        "name": name,
        "n": n,
        "len_min": min(lengths),
        "len_max": max(lengths),
        "len_mean": round(sum(lengths) / n, 1),
        "len_median": round(statistics.median(lengths)),
        "iast_pct": round(100 * iast / n, 1),
        "multi_topic_pct": round(100 * multi_topic / n, 1),
        "topics": topics,
        "axis2": axis2,
        "axis3": axis3,
        "axis4": axis4,
    }


def pct(counter, n):
    return {k: round(100 * v / n, 1) for k, v in counter.items()}


def report(p):
    n = p["n"]
    print(f"\n{'=' * 60}")
    print(f"  ПРОФИЛЬ: {p['name']}  (n={n})")
    print(f"{'=' * 60}")
    print("\nДлина примечания (знаков):")
    print(f"  мин={p['len_min']}  медиана={p['len_median']}  "
          f"среднее={p['len_mean']}  макс={p['len_max']}")
    print(f"\nIAST-плотность: {p['iast_pct']}% примечаний содержат IAST")
    print(f"Многотемность: {p['multi_topic_pct']}% примечаний несут >1 темы (axis_1)")

    print("\nОсь 1 — темы (доля примечаний, %):")
    for t, v in p["topics"].most_common():
        print(f"  {t:16s} {round(100 * v / n, 1):5.1f}%  ({v})")

    print("\nОсь 2 — тип комментария по Казанскому (%):")
    for k, v in p["axis2"].most_common():
        print(f"  {AXIS2_LABELS.get(k, k):28s} {round(100 * v / n, 1):5.1f}%  ({v})")

    print("\nОсь 3 — lakṣaṇa (доля примечаний, %):")
    for k, v in p["axis3"].most_common():
        print(f"  {k:6s} {round(100 * v / n, 1):5.1f}%  ({v})")

    print("\nОсь 4 — категория по Парибку (%):")
    for k, v in p["axis4"].most_common():
        print(f"  {AXIS4_LABELS.get(k, k):24s} {round(100 * v / n, 1):5.1f}%  ({v})")


def main():
    names = sys.argv[1:] or ["grintser"]
    profiles = [profile(name, load(name)) for name in names]
    for p in profiles:
        report(p)

    if len(profiles) > 1:
        print(f"\n{'=' * 60}")
        print("  СВОДНОЕ СРАВНЕНИЕ")
        print(f"{'=' * 60}")
        hdr = "метрика".ljust(22) + "".join(p["name"][:12].rjust(13) for p in profiles)
        print(hdr)
        rows = [
            ("медиана длины", lambda p: p["len_median"]),
            ("среднее длины", lambda p: p["len_mean"]),
            ("IAST %", lambda p: p["iast_pct"]),
            ("многотемность %", lambda p: p["multi_topic_pct"]),
            ("myth %", lambda p: pct(p["topics"], p["n"]).get("myth", 0)),
            ("realia %", lambda p: pct(p["topics"], p["n"]).get("realia", 0)),
            ("sanskrit_term %", lambda p: pct(p["topics"], p["n"]).get("sanskrit_term", 0)),
            ("philosophy %", lambda p: pct(p["topics"], p["n"]).get("philosophy", 0)),
            ("poetics %", lambda p: pct(p["topics"], p["n"]).get("poetics", 0)),
            ("Казанский G %", lambda p: pct(p["axis2"], p["n"]).get("G", 0)),
            ("Казанский V %", lambda p: pct(p["axis2"], p["n"]).get("V", 0)),
            ("Казанский A %", lambda p: pct(p["axis2"], p["n"]).get("A", 0)),
            ("Парибок P %", lambda p: pct(p["axis4"], p["n"]).get("P", 0)),
            ("Парибок K %", lambda p: pct(p["axis4"], p["n"]).get("K", 0)),
            ("Парибок D %", lambda p: pct(p["axis4"], p["n"]).get("D", 0)),
        ]
        for label, fn in rows:
            print(label.ljust(22) + "".join(str(fn(p)).rjust(13) for p in profiles))


if __name__ == "__main__":
    main()
