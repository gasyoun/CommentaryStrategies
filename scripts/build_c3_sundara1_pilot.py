#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""C3 pilot (docs/ROADMAP_2026H2.md, Workstream C, C3): born-structured JSON
annotations for Sundara 1.1-1.20, model II (two-tier hybrid, D2), plus a
parallel Govindaraja (Bhusana) / Tilaka gloss layer for the same 20 stanzas
(tertium comparationis, Article-3 method).

Sources (all already on disk, no scraping/fabrication; prior-art checked --
scripts/extract_yellow_sargas.py is the existing calibrated segmenter
(H268 WS-C2, pratika + content-anchor verified alignment) and does the actual
per-verse commentary segmentation; this script only assembles its Sundara-1
output plus the existing tier-2 apparatus into the C3 pilot record):
  - data/leonov_own_notes.json               -- Leonov/Kostina tier-2 apparatus
  - scripts/extract_yellow_sargas.py output   -- tilaka/bhusana/siromani/
    tattvadipika commentary, verse-segmented and alignment-verified
  - corpus sa/ru text pulled in by the segmenter from the sibling
    SamudraManthanam jsonl

Run:
    python scripts/extract_yellow_sargas.py 1 --outdir data/analysis/sundara1_c3
    python scripts/build_c3_sundara1_pilot.py

Output: data/sundara1_pilot_c3_20.json
"""
import json
import subprocess
import sys
import pathlib

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import derive_urn  # noqa: E402

DATA = ROOT / "data"
SEG_DIR = DATA / "analysis" / "sundara1_c3"
SEG_FILE = SEG_DIR / "sarga_01_segmented.json"
N_VERSES = 20

# Tier-1 (print) wording already fixed by C0.2 apparatus II -- verbatim reuse,
# see ramayana-leonov/C0_SPECIMENS_SUNDARA1.md "Аппарат II / Ярус 1". New
# verses (11-20, plus 2/4/5/9 which C0.2 left silent) get a fresh gloss
# condensed from the SAME already-vetted tier-2 note -- compression only, no
# new philological claim.
TIER1_C02 = {
    1: "Чараны — небесные певцы; их тропа — воздушный путь.",
    3: "«Кошачий глаз» — драгоценный камень.",
    6: "Якши, киннары, гандхарвы — полубожественные существа.",
    7: "Наг — полубожественный змей.",
    8: "Анджали — жест приветствия: сложенные ладони.",
    10: "В полнолуние и новолуние приливы особенно сильны.",
}
TIER1_NEW = {
    16: "Сандарак — минеральная красная краска (реальгар).",
    18: "«Вопль великих существ» — двоякое чтение композита.",
    19: "«Свастика» здесь — тёмная полоса на капюшоне змея.",
    20: "Укушенные ядом камни — эпическая гипербола.",
}

# axis_2_kazansky, best-effort per data/commentary_schema.json (V=realia/being
# identification, A=word-level philology with no realia, B=textual variant).
# First pass only -- flagged needs_review, gated on the C3 Leonov/Kostina
# review (roadmap line 127), not a ratified verdict.
AXIS2_BY_VERSE = {
    1: "V", 2: "A", 3: "V", 5: "V", 6: "V", 7: "A", 8: "A", 9: "B",
    10: "A", 12: "B", 16: "V", 18: "A", 19: "A", 20: "A",
}


def ensure_segmented():
    if SEG_FILE.exists():
        return
    SEG_DIR.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "extract_yellow_sargas.py"), "1", "--outdir", str(SEG_DIR)],
        check=True, cwd=str(ROOT),
    )


def load_leonov_notes():
    d = json.loads((DATA / "leonov_own_notes.json").read_text(encoding="utf-8"))
    return {n["verse"]: n for n in d["notes"] if n["sarga"] == 1 and n["verse"] <= N_VERSES}


def load_segmented():
    seg = json.loads(SEG_FILE.read_text(encoding="utf-8"))
    by_verse = {}
    for b in seg["verses"]:
        tok = b["verse"]
        if tok.isdigit() and 1 <= int(tok) <= N_VERSES:
            by_verse[int(tok)] = b
    return by_verse, seg["_meta"]


def build():
    ensure_segmented()
    leonov = load_leonov_notes()
    segmented, seg_meta = load_segmented()

    out = []
    for v in range(1, N_VERSES + 1):
        addr = f"Rām. Sundara 5.1.{v}"
        urn, ok, _ = derive_urn.derive(addr)
        note2 = leonov.get(v)
        seg = segmented.get(v)
        tier1 = TIER1_C02.get(v) or TIER1_NEW.get(v)
        entry = {
            "comment_id": f"sundara1/leonov/comment_1_{v}",
            "urn": urn,
            "shloka_addr": addr,
            "translator": "leonov",
            "editor": "kostina",
            "sanskrit_iast": seg["sanskrit_iast"] if seg else None,
            "translation_ru": seg["leonov_ru"] if seg else None,
            "model": "II (двухъярусный гибрид, D2 решено 2026-07-01)",
            "tier1_print_gloss": tier1,
            "tier2_digital_note": note2["raw_text"] if note2 else None,
            "tier2_char_count": note2["char_count"] if note2 else 0,
            "tier2_has_iast": note2["has_iast"] if note2 else False,
            "axis_1_topic": ["sanskrit_term"] if note2 else [],
            "axis_2_kazansky": AXIS2_BY_VERSE.get(v),
            # parallel Govindaraja (Bhūṣaṇa) / Tilaka layer -- tertium
            # comparationis against Leonov's tier 2, per scripts/extract_yellow_sargas.py
            # (pratika+content-anchor verified segmentation; commentary Sanskrit
            # verbatim, no translation added here -- translation is Leonov/Kostina's
            # C3 review step, not a mechanical pass).
            "govindaraja_bhusana_raw": seg["commentary"].get("bhusana") if seg else None,
            "tilaka_raw": seg["commentary"].get("tilaka") if seg else None,
            "siromani_raw": seg["commentary"].get("siromani") if seg else None,
            "tattvadipika_raw": seg["commentary"].get("tattvadipika") if seg else None,
            "commentary_ambiguous_marker": seg["ambiguous_marker"] if seg else None,
            "needs_review": True,
        }
        out.append(entry)

    meta = {
        "generated_by": "scripts/build_c3_sundara1_pilot.py",
        "roadmap_item": "docs/ROADMAP_2026H2.md Workstream C, C3 (pilot: 20 Sundara-1 stanzas)",
        "model": "II — двухъярусный гибрид (D2, решено 2026-07-01)",
        "scope": "Sundara 1.1-1.20, born-structured (assembled directly as JSON, not retrofitted from prose)",
        "sources": [
            "data/leonov_own_notes.json (tier-2, vetted, existing)",
            "scripts/extract_yellow_sargas.py output (tilaka/bhusana/siromani/tattvadipika, "
            f"pratika precision {seg_meta.get('alignment_precision')}, "
            f"verified {seg_meta.get('alignment_precision_verified')})",
            "data/valmiki_PERMISSION.md — Gita Supersite grant, CC BY 4.0",
        ],
        "status": "PILOT — gate: human:leonov,kostina (C3 review, roadmap line 127); "
                  "axis_2_kazansky is a first pass, not ratified",
        "verses_with_tier2_note": sum(1 for v in range(1, N_VERSES + 1) if v in leonov),
        "verses_without_tier2_note": sorted(v for v in range(1, N_VERSES + 1) if v not in leonov),
    }
    payload = {"_meta": meta, "verses": out}
    outpath = DATA / "sundara1_pilot_c3_20.json"
    outpath.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {outpath} ({len(out)} verses)")


if __name__ == "__main__":
    build()
