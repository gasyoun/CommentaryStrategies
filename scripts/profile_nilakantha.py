#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Структурный профиль ṭīkā Нилакантхи (Bhāratabhāvadīpa) + пул для Article 4.

⚠️ НЕ маркер-детектор. Комментарий Нилакантхи к нарративным эпизодам (Налопакхьяна,
Рамопакхьяна) терсный и БЕЗ эксплицитных лакшана-маркеров: глоссы вида «слово =
синоним» без इत्यर्थः; пратики «X iti ॥N॥» без толкования. Подсчёт маркеров дал бы
ЛОЖНЫЙ НОЛЬ (урок: не читать 0 как отсутствие содержания). Поэтому классифицируем
СТРУКТУРНО по длине/форме ṭīkā (после снятия номера стиха):

  bare         : стих без ṭīkā
  pratika_only : только пратика (катчворд + номер), глоссы нет     (≤15 знаков)
  short_gloss  : терсная глосса «слово = объяснение»               (16–60 знаков)
  substantive  : содержательное примечание                        (>60 знаков)

substantive-глоссы (>60) — кандидатный пул на «30 параллельных локусов» для
Article 4 (JAOS) / гл. 3 монографии.

Выход:
  data/nilakantha_profile.json — профиль + substantive-пул (Dev + IAST)
  печать таблицы профиля.

Зависимость: indic_transliteration (как у mahabharata-nilakantha/nilakantha_parser.py,
который переиспользуется здесь для сегментации и Dev→IAST).
"""

import importlib.util
import json
import re
import statistics
import sys
import pathlib

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
NK_DIR = ROOT / "mahabharata-nilakantha"
OUT = ROOT / "data" / "nilakantha_profile.json"

# Пороги структурной классификации (по длине ṭīkā без номера стиха)
PRATIKA_MAX = 15      # ≤ — только катчворд/пратика, толкования нет
SHORT_MAX = 60        # ≤ — терсная глосса; > — содержательное примечание

TEXTS = [
    ("MBh-Nalopakhyanam-Nilakantha.md", "Nalopākhyāna"),
    ("MBh-Ramopakhyanam-Nilakantha.md", "Rāmopākhyāna"),
]

_DEV_DIGITS = str.maketrans("०१२३४५६७८९", "0123456789")


def load_parser():
    """Переиспользуем канонический парсер (сегментация + Dev→IAST)."""
    spec = importlib.util.spec_from_file_location(
        "nilakantha_parser", NK_DIR / "nilakantha_parser.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def strip_verse_num(tika):
    """Снять завершающий ॥N॥ и пробелы, оставив тело глоссы."""
    return re.sub(r"॥[०-९0-9]+॥", "", tika or "").strip()


def classify(gloss):
    """Структурный класс ṭīkā по длине тела."""
    n = len(gloss)
    if n == 0:
        return "empty"
    if n <= PRATIKA_MAX:
        return "pratika_only"
    if n <= SHORT_MAX:
        return "short_gloss"
    return "substantive"


def profile_text(nk, filename, name):
    corpus = nk.parse_nilakantha_commentary(str(NK_DIR / filename))
    n_verses = len(corpus)
    counts = {"pratika_only": 0, "short_gloss": 0, "substantive": 0}
    gloss_lengths = []
    variants = 0
    substantive = []
    for item in corpus:
        gloss = strip_verse_num(item.get("tika"))
        if not gloss:
            continue
        gloss_lengths.append(len(gloss))
        cls = classify(gloss)
        counts[cls] = counts.get(cls, 0) + 1
        if re.search(r"पाठे|पाठान्तर", gloss):
            variants += 1
        if cls == "substantive":
            verse_dev = item.get("verse", "")
            substantive.append({
                "text": name,
                "chapter": (item.get("chapter") or "").strip(),
                "verse_dev": verse_dev,
                "verse": int(verse_dev.translate(_DEV_DIGITS)) if verse_dev else None,
                "mula_dev": item.get("mula", ""),
                "mula_iast": nk.devanagari_to_iast(item.get("mula", "")),
                "tika_dev": gloss,
                "tika_iast": nk.devanagari_to_iast(gloss),
                "tika_len": len(gloss),
            })
    with_tika = sum(counts.values())
    stats = {
        "verses": n_verses,
        "with_tika": with_tika,
        "tika_coverage_pct": round(100 * with_tika / n_verses, 1) if n_verses else 0,
        "pratika_only": counts["pratika_only"],
        "short_gloss": counts["short_gloss"],
        "substantive": counts["substantive"],
        "patha_variants": variants,
        "tika_len_median": int(statistics.median(gloss_lengths)) if gloss_lengths else 0,
        "tika_len_max": max(gloss_lengths) if gloss_lengths else 0,
    }
    return stats, substantive


def main():
    nk = load_parser()
    texts, pool = {}, []
    for filename, name in TEXTS:
        stats, substantive = profile_text(nk, filename, name)
        texts[name] = stats
        pool.extend(substantive)

    totals = {k: sum(t[k] for t in texts.values())
              for k in ("verses", "with_tika", "pratika_only",
                        "short_gloss", "substantive", "patha_variants")}

    payload = {
        "source": [f for f, _ in TEXTS],
        "generated_by": "scripts/profile_nilakantha.py",
        "method": "structural (length/form of ṭīkā), NOT marker-based — "
                  "Nīlakaṇṭha glosses without explicit lakṣaṇa markers; "
                  "marker counting would yield a false zero. See NILAKANTHA_PROFILE.md.",
        "thresholds": {"pratika_max": PRATIKA_MAX, "short_max": SHORT_MAX},
        "texts": texts,
        "totals": totals,
        "substantive_pool_count": len(pool),
        "substantive_pool": pool,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                   encoding="utf-8", newline="\n")

    # Печать
    print(f"Записано: {OUT.relative_to(ROOT)}")
    hdr = f"{'текст':16s}{'стихов':>8}{'ṭīkā':>7}{'%':>6}{'пратика':>9}{'глосса':>8}{'содерж.':>9}{'варианты':>10}"
    print("\n" + hdr)
    for name, s in texts.items():
        print(f"{name:16s}{s['verses']:>8}{s['with_tika']:>7}{s['tika_coverage_pct']:>6}"
              f"{s['pratika_only']:>9}{s['short_gloss']:>8}{s['substantive']:>9}{s['patha_variants']:>10}")
    print(f"{'ИТОГО':16s}{totals['verses']:>8}{totals['with_tika']:>7}"
          f"{round(100*totals['with_tika']/totals['verses'],1):>6}"
          f"{totals['pratika_only']:>9}{totals['short_gloss']:>8}"
          f"{totals['substantive']:>9}{totals['patha_variants']:>10}")
    print(f"\nsubstantive-пул (кандидаты на 30 локусов Article 4): {len(pool)} глосс")


if __name__ == "__main__":
    main()
