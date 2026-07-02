"""
crosstext_grintser_locate.py — LOCATOR / VERIFIER helper.

Given a SLP1 regex on the Sanskrit side, print every matching verse in the
chosen work(s) with both #sa (IAST) and #ru (подстрочник), so each proposed
intratextual parallel can be verified before it is written into a note.

Usage:
  python crosstext_grintser_locate.py <work> <slp1_regex>
  work in: sund bala ayodhya aranya all
UTF-8, no BOM.
"""
import sys, json, re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

CORPUS = Path(r"C:\Users\user\Documents\GitHub\SamudraManthanam\web\corpus_builder\jsonl")
FILES = {
    "sund":    CORPUS / "05_ramayana-sundarakanda.jsonl",
    "bala":    CORPUS / "01_ramayana-balakanda.jsonl",
    "ayodhya": CORPUS / "02_ramayana-ayodhyakanda.jsonl",
    "aranya":  CORPUS / "03_ramayana-aranyakanda.jsonl",
}
ROMAN = {"sund": "V", "bala": "I", "ayodhya": "II", "aranya": "III"}

def load(work):
    rows = {}
    with open(FILES[work], encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            r = json.loads(line)
            rows.setdefault(r["passage"], {})[r["seg"]] = r
    return rows

def main():
    work = sys.argv[1]
    pat = re.compile(sys.argv[2], re.IGNORECASE)
    works = ["bala", "ayodhya", "aranya", "sund"] if work == "all" else [work]
    for w in works:
        rows = load(w)
        for passage, seg in rows.items():
            sa = seg.get("sa", {})
            if pat.search(sa.get("slp1", "")):
                ru = seg.get("ru", {})
                print(f"--- {ROMAN[w]}.{passage} ---")
                print(f"  SA: {sa.get('text','')}")
                print(f"  RU: {ru.get('text','')}")

if __name__ == "__main__":
    main()
