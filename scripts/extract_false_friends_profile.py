"""Профиль «ложных друзей» по корпусу (данные для Article 1, ВЯ).

Извлекает из 6 размеченных файлов (data/*_markup_50.json) примечания, упоминающие
25 ключевых терминов-«ложных друзей», и считает:
  • общий профиль переводчика: axis_4_paribok (P/K/D) + доля IAST + ср. длина;
  • по каждому термину × переводчику: число попаданий, IAST, длина, Paribok,
    и эвристический класс T/C/D (рамка статьи).

⚠️ Сигнал тонкий: только золотая выборка (300 примечаний, ~80 попаданий). Робастны
лишь общие профили P/K/D (по 50 нот) и несколько хорошо засвидетельствованных
терминов (ātman/Сыркин, dharma, deva/Кальянов). По-термовые выводы для редких —
гипотезы до полнокорпусного прогона (пайплайн Года 1). См. false-friends-lexicon.md.

T/C/D (рамка ВЯ-статьи; ЗДЕСЬ — эвристический ПРОКСИ по сигналам примечания, не
прочтение самого перевода):
  T transliterate+gloss : IAST + развёрнутое пояснение (есть IAST и длина > 80)
  C contextual calque   : маркеры «букв.», «в данном контексте», «точнее», «ср.», «или»
  D domesticate         : короткое примечание (≤ 80 знаков)

Запуск:  python scripts/extract_false_friends_profile.py
Выход:   data/false_friends_profile.json + печать таблиц.
"""

import json
import re
import sys
import pathlib

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "false_friends_profile.json"

TRANSLATORS = ["kalyanov", "vassilkov", "erman", "grintser", "syrkin", "leonov"]
FILES = {t: DATA / f"{t}_markup_50.json" for t in TRANSLATORS}

WELL_ATTESTED_MIN = 4   # порог «робастности» термина по числу попаданий в корпусе

# Термин → паттерны (рус. транслитерации + фрагменты IAST)
TERMS = [
    ("dharma",     [r"дхарм", r"\bdharma\b"]),
    ("atman",      [r"атман", r"ātman", r"\batman\b"]),
    ("brahman_n",  [r"Брахман", r"brahman", r"брахман[еа]"]),
    ("maya",       [r"\bмай[яею]\b", r"\bmāyā\b", r"\bmaya\b"]),
    ("karma",      [r"\bкарм[аеуы]\b", r"\bkarma\b", r"\bkarman\b"]),
    ("moksha",     [r"\bмокш", r"\bmokṣa\b", r"\bmoksa\b"]),
    ("nirvana",    [r"\bнирван", r"\bnirvāṇa\b", r"\bnirvana\b"]),
    ("samsara",    [r"\bсансар", r"\bsaṃsāra\b", r"\bsamsara\b"]),
    ("yoga",       [r"\bйог[аеуи]\b", r"\byoga\b"]),
    ("bhakti",     [r"\bбхакт", r"\bbhakti\b"]),
    ("yajna",      [r"\bяджн", r"\byajña\b", r"\byajna\b"]),
    ("tapas",      [r"\bтапас", r"\btapas\b", r"\bтапа\b"]),
    ("mantra",     [r"\bмантр", r"\bmantra\b"]),
    ("varna",      [r"\bварн[аы]\b", r"\bvarṇa\b", r"\bvarna\b"]),
    ("guna",       [r"\bгун[аы]\b", r"\bguṇa\b", r"\bguna\b"]),
    ("purusha",    [r"\bпуруш", r"\bpuruṣa\b", r"\bpurusa\b"]),
    ("prakriti",   [r"\bпракрит", r"\bprakṛti\b", r"\bprakriti\b"]),
    ("akasha",     [r"\bакаш", r"\bākāśa\b", r"\bakasa\b"]),
    ("ashrama",    [r"\bашрам", r"\bāśrama\b", r"\basrama\b"]),
    ("deva_asura", [r"\bасур", r"\basura\b", r"\bdeva\b", r"\bдев[аы]\b"]),
    ("ahamkara",   [r"\bахамкар", r"\bahaṃkāra\b", r"я-делател"]),
    ("buddhi",     [r"\bбуддх", r"\bbuddhi\b"]),
    ("shunya",     [r"\bшунь", r"\bśūnya\b", r"\bsunyata\b"]),
    ("satya",      [r"\bсатья\b", r"\bsatya\b"]),
    ("rita",       [r"\bрит[аеу]\b", r"\bṛta\b", r"\brita\b"]),
]

IAST_RE = re.compile(r"[āĀīĪūŪṛṝḷṅñṭḍṇśṣḥṃ]")
C_MARKERS = re.compile(r"букв\.|в данном контексте|точнее|иногда|вариант|\bср\.|\bили «", re.I)


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def matches(text, patterns):
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)


def tcd(note):
    """Эвристический класс T/C/D из сигналов примечания (см. docstring; это прокси)."""
    text = note.get("raw_text", "")
    has_iast = bool(note.get("has_iast") or IAST_RE.search(text))
    n = len(text)
    if C_MARKERS.search(text):
        return "C"
    if has_iast and n > 80:
        return "T"
    if n <= 80:
        return "D"
    return "C"   # длинное, дискурсивное, без явных маркеров ≈ контекстуальное


def main():
    corpus = {t: load(p) for t, p in FILES.items() if p.exists()}

    # Общий профиль переводчика
    per_translator = {}
    for t, notes in corpus.items():
        pk = {"P": 0, "K": 0, "D": 0}
        for c in ("P", "K", "D"):
            pk[c] = sum(1 for n in notes if n.get("axis_4_paribok") == c)
        iast = sum(1 for n in notes if n.get("has_iast"))
        per_translator[t] = {
            "n": len(notes), "paribok": pk,
            "iast_rate": round(100 * iast / len(notes), 1) if notes else 0,
            "mean_len": round(sum(len(n.get("raw_text", "")) for n in notes) / len(notes), 1) if notes else 0,
        }

    # По термину × переводчику
    per_term = {}
    for term, patterns in TERMS:
        per_term[term] = {}
        for t, notes in corpus.items():
            hits = [n for n in notes if matches(n.get("raw_text", ""), patterns)]
            if not hits:
                continue
            pk = {"P": 0, "K": 0, "D": 0}
            tc = {"T": 0, "C": 0, "D": 0}
            for n in hits:
                pk[n.get("axis_4_paribok", "P")] = pk.get(n.get("axis_4_paribok", "P"), 0) + 1
                tc[tcd(n)] += 1
            per_term[term][t] = {
                "hits": len(hits),
                "iast_n": sum(1 for n in hits if n.get("has_iast")),
                "mean_len": round(sum(len(n.get("raw_text", "")) for n in hits) / len(hits), 1),
                "paribok": pk, "tcd": tc,
                "snippets": [n.get("raw_text", "")[:140] for n in hits],
            }

    term_totals = {term: sum(d["hits"] for d in per_term[term].values()) for term, _ in TERMS}
    well_attested = sorted([t for t, n in term_totals.items() if n >= WELL_ATTESTED_MIN],
                           key=lambda t: -term_totals[t])
    sparse = [t for t, n in term_totals.items() if 0 < n < WELL_ATTESTED_MIN]
    absent = [t for t, n in term_totals.items() if n == 0]

    payload = {
        "scope": "gold sample only (6×50 = 300 notes); thin signal — see caveats",
        "generated_by": "scripts/extract_false_friends_profile.py",
        "tcd_note": "T/C/D is a heuristic proxy from note signals, NOT a reading of the translation.",
        "per_translator": per_translator,
        "well_attested_terms": {t: term_totals[t] for t in well_attested},
        "sparse_terms": {t: term_totals[t] for t in sparse},
        "absent_terms": absent,
        "per_term": per_term,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
                   encoding="utf-8", newline="\n")

    # ── Печать ──
    print(f"Записано: {OUT.relative_to(ROOT)}\n")
    print("## Общий профиль переводчика (50 нот каждый)\n")
    print(f"{'переводчик':<12}{'P':>4}{'K':>4}{'D':>4}{'IAST%':>7}{'ср.длина':>10}")
    for t in TRANSLATORS:
        if t not in per_translator:
            continue
        s = per_translator[t]
        print(f"{t:<12}{s['paribok']['P']:>4}{s['paribok']['K']:>4}{s['paribok']['D']:>4}"
              f"{s['iast_rate']:>7}{s['mean_len']:>10}")

    print("\n## Хорошо засвидетельствованные термины (≥%d попаданий)\n" % WELL_ATTESTED_MIN)
    for term in well_attested:
        cells = []
        for t in TRANSLATORS:
            d = per_term[term].get(t)
            if d:
                tc = d["tcd"]
                cells.append(f"{t}: {d['hits']}× (T{tc['T']}/C{tc['C']}/D{tc['D']})")
        print(f"  {term:12s} [{term_totals[term]}]  " + " · ".join(cells))

    print(f"\n## Редкие (1–{WELL_ATTESTED_MIN - 1} попаданий — гипотезы, нужен пайплайн): "
          + ", ".join(f"{t}({term_totals[t]})" for t in sparse))
    print(f"## Отсутствуют в выборке: " + ", ".join(absent))


if __name__ == "__main__":
    main()
