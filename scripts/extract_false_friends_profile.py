"""
Extract axis_4_paribok (Paribok P/K/D) profiles for false-friend terms
from the 5 translator markup JSON files.

Paribok taxonomy (from ARCHITECTURE.md / schema):
  P = понятие  — term presented as factual / transliterate+gloss
  K = кодификатор — term treated as a key technical concept (calque / conceptual)
  D = дискурсивное — term elaborated discursively; domesticated Russian used

Usage: python scripts/extract_false_friends_profile.py
Output: prints a Markdown summary table + per-term findings.
"""

import json, re, sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

ROOT = pathlib.Path(__file__).parent.parent
DATA = ROOT / "data"

FILES = {
    "kalyanov":  DATA / "kalyanov_markup_50.json",
    "vassilkov": DATA / "vassilkov_markup_50.json",
    "erman":     DATA / "erman_markup_50.json",
    "grintser":  DATA / "grintser_markup_50.json",
    "syrkin":    DATA / "syrkin_markup_50.json",
    "leonov":    DATA / "leonov_markup_50.json",
}

# Search patterns: Russian transliterations + IAST fragments of each false-friend term
# Each entry: (term_label, [regex patterns to match in raw_text])
TERMS = [
    ("dharma",      [r"дхарм", r"\bdharma\b", r"дхармы", r"дхарме"]),
    ("atman",       [r"атман", r"ātman", r"\batman\b"]),
    ("brahman_n",   [r"Брахман", r"brahman", r"брахмане", r"брахмана"]),
    ("maya",        [r"\bмай[яею]\b", r"\bmāyā\b", r"\bmaya\b"]),
    ("karma",       [r"\bкарм[аеуы]\b", r"\bkarma\b", r"\bkarman\b"]),
    ("moksha",      [r"\bмокш", r"\bmokṣa\b", r"\bmoksa\b"]),
    ("nirvana",     [r"\bнирван", r"\bnirvāṇa\b", r"\bnirvana\b"]),
    ("samsara",     [r"\bсансар", r"\bsaṃsāra\b", r"\bsamsara\b"]),
    ("yoga",        [r"\bйог[аеуи]\b", r"\byoga\b"]),
    ("bhakti",      [r"\bбхакт", r"\bbhakti\b"]),
    ("yajna",       [r"\bяджн", r"\byajña\b", r"\byajna\b"]),
    ("tapas",       [r"\bтапас", r"\btapas\b", r"\bтапа\b"]),
    ("mantra",      [r"\bмантр", r"\bmantra\b"]),
    ("varna",       [r"\bварн[аы]\b", r"\bvarṇa\b", r"\bvarna\b"]),
    ("guna",        [r"\bгун[аы]\b", r"\bguṇa\b", r"\bguna\b"]),
    ("purusha",     [r"\bпуруш", r"\bpuruṣa\b", r"\bpurusa\b"]),
    ("prakriti",    [r"\bпракрит", r"\bprakṛti\b", r"\bprakriti\b"]),
    ("akasha",      [r"\bакаш", r"\bākāśa\b", r"\bakasa\b"]),
    ("ashrama",     [r"\bашрам", r"\bāśrama\b", r"\basrama\b"]),
    ("deva_asura",  [r"\bасур", r"\basura\b", r"\bdeva\b", r"\bдев[аы]\b"]),
    ("ahamkara",    [r"\bахамкар", r"\bahaṃkāra\b", r"\bahamkara\b", r"я-делател"]),
    ("buddhi",      [r"\bбуддх", r"\bbuddhi\b"]),
    ("shunya",      [r"\bшунь", r"\bśūnya\b", r"\bsunyata\b"]),
    ("satya",       [r"\bсатья\b", r"\bsatya\b"]),
    ("rita",        [r"\bрит[аеу]\b", r"\bṛta\b", r"\brita\b"]),
]

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def matches(text, patterns):
    for p in patterns:
        if re.search(p, text, re.IGNORECASE):
            return True
    return False

# ── Collect hits ──────────────────────────────────────────────────────────────
results = {}   # term → {translator → {P:n, K:n, D:n, hits:[raw_text,...]}}

for term_label, patterns in TERMS:
    results[term_label] = {}
    for tr, path in FILES.items():
        if not path.exists():
            continue
        notes = load(path)
        counts = {"P": 0, "K": 0, "D": 0, "total": 0, "hits": []}
        for note in notes:
            if matches(note.get("raw_text", ""), patterns):
                paribok = note.get("axis_4_paribok", "?")
                counts[paribok] = counts.get(paribok, 0) + 1
                counts["total"] += 1
                counts["hits"].append(note["raw_text"][:120])
        results[term_label][tr] = counts

# ── Overall profile per translator ────────────────────────────────────────────
print("\n## Overall axis_4_paribok profile (all 50 notes per translator)\n")
header = f"{'Translator':<12} {'P':>5} {'K':>5} {'D':>5} {'Total':>7}"
print(header)
print("-" * len(header))
for tr, path in FILES.items():
    if not path.exists():
        continue
    notes = load(path)
    p = sum(1 for n in notes if n.get("axis_4_paribok") == "P")
    k = sum(1 for n in notes if n.get("axis_4_paribok") == "K")
    d = sum(1 for n in notes if n.get("axis_4_paribok") == "D")
    print(f"{tr:<12} {p:>5} {k:>5} {d:>5} {len(notes):>7}")

# ── Per-term hit table ────────────────────────────────────────────────────────
print("\n\n## False-friend term hits and Paribok codes\n")
translators = list(FILES.keys())
col_w = 18
header = f"{'Term':<14}" + "".join(f"{t:<{col_w}}" for t in translators)
print(header)
print("-" * (14 + col_w * len(translators)))

for term_label, _ in TERMS:
    row = f"{term_label:<14}"
    for tr in translators:
        data = results[term_label].get(tr, {})
        total = data.get("total", 0)
        if total == 0:
            cell = "—"
        else:
            parts = []
            for code in ["P", "K", "D"]:
                n = data.get(code, 0)
                if n:
                    parts.append(f"{code}×{n}")
            cell = " ".join(parts) if parts else "?"
        row += f"{cell:<{col_w}}"
    print(row)

# ── Detailed hits for terms with K or D codes ─────────────────────────────────
print("\n\n## Detailed hits (terms with K or D codes)\n")
for term_label, _ in TERMS:
    for tr in translators:
        data = results[term_label].get(tr, {})
        if data.get("K", 0) + data.get("D", 0) > 0:
            print(f"### {term_label} / {tr}")
            for hit in data.get("hits", []):
                paribok_code = "?"
                # re-detect
                notes = load(FILES[tr])
                for n in notes:
                    if n.get("raw_text", "").startswith(hit[:60]):
                        paribok_code = n.get("axis_4_paribok", "?")
                        break
                print(f"  [{paribok_code}] {hit}")
            print()
