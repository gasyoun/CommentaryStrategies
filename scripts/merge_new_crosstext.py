"""
merge_new_crosstext.py -- Merge new cluster notes into sundara_commentary_to_add.json
Clusters: kavya (6), veda (2), upanishads (1), purana (0) = 9 new notes
"""
import sys, json, re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

CS_DIR  = Path(r"C:\Users\user\Documents\GitHub\CommentaryStrategies")
DATA    = CS_DIR / "data"
MAIN_F  = DATA / "sundara_commentary_to_add.json"
CROSS   = DATA / "crosstext"

NEW_CLUSTERS = ["kavya", "veda", "upanishads", "purana"]

# Load existing
with open(MAIN_F, encoding="utf-8") as f:
    all_data = json.load(f)

meta = all_data[0]
notes = all_data[1:]

# Existing dedup key: (shloka, lemma_iast, subtype)
existing_keys = set()
for n in notes:
    key = (n.get("shloka",""), n.get("lemma_iast",""), n.get("subtype",""))
    existing_keys.add(key)

print(f"Existing notes: {len(notes)}", file=sys.stderr)

# Load new cluster notes
new_notes = []
for cluster in NEW_CLUSTERS:
    cfile = CROSS / f"{cluster}.json"
    if not cfile.exists():
        print(f"  {cluster}: file missing", file=sys.stderr)
        continue
    with open(cfile, encoding="utf-8") as f:
        cnotes = json.load(f)
    added = 0
    skipped = 0
    for note in cnotes:
        if "_meta" in note:
            continue
        key = (note.get("shloka",""), note.get("lemma_iast",""), note.get("subtype","cross_text"))
        if key in existing_keys:
            print(f"  DEDUP: {key}", file=sys.stderr)
            skipped += 1
            continue
        # Ensure required fields
        note.setdefault("subtype", "cross_text")
        note.setdefault("review_required", True)
        note.setdefault("cluster", cluster)
        new_notes.append(note)
        existing_keys.add(key)
        added += 1
    print(f"  {cluster}: {added} added, {skipped} skipped", file=sys.stderr)

print(f"New notes to add: {len(new_notes)}", file=sys.stderr)

# Parse shloka address for sorting: V.ch.verse -> (ch, verse)
def shloka_key(n):
    addr = n.get("shloka","V.0.0")
    m = re.match(r"V\.(\d+)\.(\d+)", addr)
    if m:
        return (int(m.group(1)), int(m.group(2)))
    return (999, 0)

all_notes = notes + new_notes
all_notes.sort(key=shloka_key)

total_new = len(notes) + len(new_notes)
cross_text_total = sum(1 for n in all_notes if n.get("subtype") == "cross_text")
base_total = total_new - cross_text_total

print(f"Total after merge: {total_new} ({base_total} base + {cross_text_total} cross-text)", file=sys.stderr)

# Update _meta
meta["_meta"]["total_notes"] = total_new
meta["_meta"]["base_notes"] = base_total
meta["_meta"]["cross_text_notes"] = cross_text_total
meta["_meta"]["generated"] = "2026-06-27"
meta["_meta"]["cross_text_expanded"] = f"2026-06-27: добавлены кластеры kavya (+6), veda (+2), upanishads (+1) = +9 примечаний"

# Recount by_type and by_trigger from all_notes
by_type = {}
by_trigger = {}
for n in all_notes:
    t = n.get("type","?")
    by_type[t] = by_type.get(t, 0) + 1
    tr = n.get("trigger", n.get("subtype", "?"))
    by_trigger[tr] = by_trigger.get(tr, 0) + 1

meta["_meta"]["by_type"] = by_type
meta["_meta"]["by_trigger"] = by_trigger

# Rebuild per_chapter_notes
from collections import defaultdict
ch_notes = defaultdict(int)
for n in all_notes:
    addr = n.get("shloka","V.0.0")
    m = re.match(r"V\.(\d+)\.", addr)
    if m:
        ch_notes[int(m.group(1))] += 1

# Existing chapter_verse_counts from meta
cvc = meta["_meta"].get("chapter_verse_counts", meta["_meta"].get("per_chapter_notes", {}))

per_chapter = {}
for ch in range(1, 69):
    per_chapter[str(ch)] = ch_notes.get(ch, 0)
meta["_meta"]["per_chapter_notes"] = per_chapter

# Write back
out = [meta] + all_notes
MAIN_F.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Written {MAIN_F}", file=sys.stderr)
print(f"FINAL: {total_new} notes = {base_total} base + {cross_text_total} cross-text", file=sys.stderr)
