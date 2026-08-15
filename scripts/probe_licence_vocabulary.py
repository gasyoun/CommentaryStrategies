"""H1324 §5 probe, pass 2 — word-anchored licence vocabulary.

Pass 1's naive `ārṣ\\w*` matched INSIDE pārṣada / kārṣīr / vārṣika, which is a defect of the
pattern, not a property of the corpus. Sanskrit compounds mean a licence term can legitimately
sit after a hyphen or a compound boundary, so "word start" here = start-of-string, whitespace,
or a hyphen — but never mid-morph.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

SRC = Path(sys.argv[1])
OUT = Path(sys.argv[2])
text = SRC.read_text(encoding="utf-8", errors="replace")

BOUND = r"(?:(?<=^)|(?<=[\s\-|>('‘’]))"
TERMS = {
    "ārṣa": BOUND + r"[aā]?ārṣ[aāiī]\w*",
    "chāndasa": BOUND + r"c?chāndas\w*",
    "pramāda": BOUND + r"[as]?pramād\w*",
}

records = []
counts = {}
for label, pat in TERMS.items():
    ms = list(re.finditer(pat, text, re.MULTILINE))
    counts[label] = len(ms)
    for m in ms:
        lo, hi = max(0, m.start() - 300), min(len(text), m.end() + 200)
        ctx = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text[lo:hi])).strip()
        records.append({"term": label, "match": m.group(0), "offset": m.start(), "context": ctx})

records.sort(key=lambda r: r["offset"])
OUT.write_text(json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8")
print("word-anchored hit counts:")
for k, v in counts.items():
    print(f"  {k:10} {v}")
print(f"total {len(records)} -> {OUT}")
