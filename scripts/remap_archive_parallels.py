#!/usr/bin/env python3
"""Remap the DCS archive-parallels layer from critical (Baroda) to vulgate numbering.

data/crosstext/archive_parallels.json is extracted from VisualDCS archive.sqlite,
whose Ramayana text is the CRITICAL edition — its V.<sarga>.<verse> anchors do not
match Leonov's southern-vulgate translation. This script deterministically remaps
every anchor via the verse-level concordance built by scripts/compare_editions.py
(data/edition_comparison/concordance.json, statuses identical/variant carry a
critical->southern verse pair).

Rules (H141 subtask 1):
  - every critical verse is looked up individually; comma-lists and en-dash ranges
    are expanded;
  - fully mapped entry     -> edition="vulgate",        shloka = vulgate ref
  - partially mapped entry -> edition="vulgate_partial", shloka = mapped subset
  - nothing mapped / "?"   -> edition="critical",       shloka unchanged (KEPT, not dropped)
  - the original anchor is always preserved in shloka_critical, and the per-verse
    mapping (with concordance status) in verse_map;
  - intratext entries whose verse_address is a Ram. book-V critical ref also get
    verse_address_vulgate.

Usage:  python scripts/remap_archive_parallels.py
Output: data/crosstext/archive_parallels_vulgate.json
"""
import sys
import os
import re
import json

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SRC = os.path.join(REPO, "data", "crosstext", "archive_parallels.json")
CONC = os.path.join(REPO, "data", "edition_comparison", "concordance.json")
OUT = os.path.join(REPO, "data", "crosstext", "archive_parallels_vulgate.json")


def parse_ref(rest):
    """'27' / '14,17,22' / '3–7' (also '3-7') -> sorted list of ints, or None for '?'."""
    if rest.strip() == "?":
        return None
    verses = []
    for part in rest.split(","):
        part = part.strip()
        m = re.match(r"^(\d+)\s*[–-]\s*(\d+)$", part)
        if m:
            verses.extend(range(int(m.group(1)), int(m.group(2)) + 1))
        elif part.isdigit():
            verses.append(int(part))
        else:
            return None
    return sorted(set(verses))


def parse_shloka(s):
    """'V.13.27' -> (13, [27]); 'V.31.?' -> (31, None)."""
    m = re.match(r"^V\.(\d+)\.(.+)$", str(s).strip())
    if not m:
        return None, None
    return int(m.group(1)), parse_ref(m.group(2))


def compress(verses):
    """[3,4,5,7] -> '3–5,7' (runs of >=2 use en dash, as in the source layer)."""
    out, i = [], 0
    while i < len(verses):
        j = i
        while j + 1 < len(verses) and verses[j + 1] == verses[j] + 1:
            j += 1
        out.append(str(verses[i]) if i == j else f"{verses[i]}–{verses[j]}")
        i = j + 1
    return ",".join(out)


def fmt_vulgate(pairs):
    """[(sarga, verse), ...] -> 'V.36.14,17' or 'V.36.14; V.37.2' if sargas differ."""
    by_sarga = {}
    for s, v in pairs:
        by_sarga.setdefault(s, []).append(v)
    return "; ".join(
        f"V.{s}.{compress(sorted(set(vs)))}" for s, vs in sorted(by_sarga.items())
    )


def remap_verses(sarga, verses, crit2south):
    """Return (verse_map, mapped_pairs). mapped_pairs = [(south_sarga, south_verse)]."""
    verse_map, mapped = [], []
    for v in verses:
        crit_id = f"5.{sarga}.{v}"
        hit = crit2south.get(crit_id)
        if hit:
            sm = re.match(r"^5\.(\d+)\.(\d+)$", hit["southern"])
            verse_map.append({"critical": crit_id, "vulgate": hit["southern"],
                              "status": hit["status"]})
            if sm:
                mapped.append((int(sm.group(1)), int(sm.group(2))))
        else:
            verse_map.append({"critical": crit_id, "vulgate": None,
                              "status": "critical_only"})
    return verse_map, mapped


def main():
    entries = json.load(open(SRC, encoding="utf-8"))
    conc = json.load(open(CONC, encoding="utf-8"))["concordance"]
    crit2south = {e["critical"]: {"southern": e["southern"], "status": e["status"]}
                  for e in conc if e.get("critical") and e.get("southern")}

    meta_in = entries[0]["_meta"] if entries and "_meta" in entries[0] else {}
    body = [e for e in entries if "_meta" not in e]

    out, counts = [], {"vulgate": 0, "vulgate_partial": 0, "critical": 0}
    for e in body:
        rec = dict(e)
        rec["shloka_critical"] = e.get("shloka", "")
        sarga, verses = parse_shloka(e.get("shloka", ""))
        if sarga is None or verses is None:
            rec["edition"] = "critical"
            rec["verse_map"] = []
        else:
            verse_map, mapped = remap_verses(sarga, verses, crit2south)
            rec["verse_map"] = verse_map
            if mapped and len(mapped) == len(verses):
                rec["edition"] = "vulgate"
                rec["shloka"] = fmt_vulgate(mapped)
            elif mapped:
                rec["edition"] = "vulgate_partial"
                rec["shloka"] = fmt_vulgate(mapped)
            else:
                rec["edition"] = "critical"
        # intratext parallel side: Ram. book-V critical refs get a vulgate echo too
        va = str(e.get("verse_address", ""))
        vm = re.match(r"^Rām 5\.(\d+)\.([\d,–\-\s]+)", va)
        if vm:
            pv = parse_ref(vm.group(2))
            if pv:
                _, pmapped = remap_verses(int(vm.group(1)), pv, crit2south)
                if pmapped:
                    rec["verse_address_vulgate"] = f"Rām {fmt_vulgate(pmapped)} (вульгата)"
        counts[rec["edition"]] += 1
        out.append(rec)

    meta = dict(meta_in)
    meta.update({
        "remapped_by": "scripts/remap_archive_parallels.py",
        "remap_source": "data/edition_comparison/concordance.json "
                        "(compare_editions.py, statuses identical/variant)",
        "remap_rule": "shloka = vulgate (southern / Leonov) ref; original critical anchor "
                      "in shloka_critical; per-verse mapping in verse_map; entries without "
                      "a concordance hit are KEPT with edition='critical'",
        "remap_counts": counts,
        "entries": len(out),
    })
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump([{"_meta": meta}] + out, fh, ensure_ascii=False, indent=2)
    print(f"wrote {OUT}: {len(out)} entries -> {counts}")


if __name__ == "__main__":
    main()
