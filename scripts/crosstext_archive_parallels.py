#!/usr/bin/env python3
"""Cross-text apparatus layer for Sundarakāṇḍa from the VisualDCS ``parallels`` table.

Bridge 2 (see Uprava/handoffs/OPUS_Sundara_crosstext_apparatus.md): the DCS
full-text parallel search (archive.sqlite, table ``parallels``) flagged, for each
Rāmāyaṇa verse, the other corpus verses that share content lemmata. This script
extracts every parallel touching **Sundarakāṇḍa** (kāṇḍa 5, Rām text_id=248),
deduplicates the two DB directions, classifies each match, applies an adversarial
strength gate, and writes a machine-derived cross-text apparatus layer alongside
the hand-curated clusters in ``data/crosstext/``.

Design decisions (honest-yield principle):
  * The verse TEXT lives on the full-text run (source_verse / target_verse); it is
    rendered verbatim so an editor can locate and judge the pair. We do NOT
    fabricate Russian scholarly prose — ``parallel_ru`` is empty and every note is
    ``review_required``. This is a machine layer, not authored commentary.
  * ``matched_words`` is the DCS *distinguishing* lemma pair ("+ query_lemma
    - counterpart_lemma", i.e. the words that DIFFER at the aligned position, not
    the shared overlap). It is rendered raw and never reinterpreted (handoff
    guardrail). The real strength signal is therefore the shared verse **text**.
  * Adversarial gate = shared content-token overlap between the two verse texts.
    A pair sharing < 2 content tokens is rejected as spurious single-common-word
    noise (e.g. the 5.40 ``ādāya`` cluster vs Divyāvadāna / Pāśupatasūtra /
    Viṣṇusmṛti, overlap 0). Every rejection keeps its ``reject_reason`` — the
    reject log IS the quality signal.
  * Bidirectional dedup: the same underlying parallel appears twice (Rām-as-source
    and Rām-as-target), each direction carrying only one side's verse number. We
    group by the unordered pair of verse texts and merge, recovering the fullest
    addressing. scope = 'intratext' (Rāmāyaṇa-internal echo) vs 'crosstext'
    (parallel in a *different* work); an intratext pair whose both endpoints are in
    kāṇḍa 5 yields two per-verse notes (one anchored on each verse).

Addressing caveat: DCS Rāmāyaṇa uses the **critical (Baroda) edition** sarga/verse
numbering; Leonov's corpus is the **southern vulgate** (68 sargas). verse_address
is critical-edition; mapping onto Leonov's numbering needs the repo's existing
edition-alignment layer (scripts/sa_align.py, data/edition_comparison/).
Documented, not silently remapped.

Read-only on archive.sqlite. Writes only under data/crosstext/.
"""
import json
import os
import re
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

# --- paths -----------------------------------------------------------------
ARCHIVE = r"C:\Users\user\Documents\GitHub\VisualDCS\src\DCS-data-2026\archive.sqlite"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(REPO, "data", "crosstext")
OUT_JSON = os.path.join(OUT_DIR, "archive_parallels.json")
OUT_REJ = os.path.join(OUT_DIR, "archive_parallels.rejected.json")
OUT_COV = os.path.join(OUT_DIR, "ARCHIVE_PARALLELS_COVERAGE.md")

RAM_TEXT_ID = 248
KANDA = 5
MIN_OVERLAP = 2  # shared content tokens required to accept a pair

# Particles / pronominals excluded when counting *content* overlap.
STOP_TOKEN = {
    "ca", "tu", "vā", "hi", "api", "iva", "eva", "na", "atha", "tathā",
    "yathā", "sa", "saḥ", "tad", "tat", "tam", "te", "tān", "sā", "tā",
    "ma", "me", "mama", "tvam", "aham", "ha", "u", "ā", "iti", "vai", "ha",
}


def norm_tokens(text):
    """Lowercase, drop daṇḍa / digits / punctuation, split to word tokens."""
    t = (text or "").lower()
    t = t.replace("।", " ").replace("॥", " ").replace("|", " ")
    t = re.sub(r"[0-9]", " ", t)
    t = re.sub(r"[^\wऀ-ॿĀ-ỿ\s]", " ", t)
    return [w for w in t.split() if w]


def content_overlap(a, b):
    sa, sb = set(norm_tokens(a)), set(norm_tokens(b))
    return sorted((sa & sb) - STOP_TOKEN)


def parse_ref(ref, is_ram):
    """Return dict(kanda, sarga, dcs_id, verse) from a DCS ref string.

    Rām form:  '[Rāmāyaṇa ]Rām, 5, 56: 380 26'  -> kanda 5, sarga 56, dcs 380, verse 26
    single    :  'Divyāv, 7: 7' / 'MBh, 3, 65: 363' handled generically.
    Leading work-name tokens are ignored — the *_text_name column is authoritative
    for the label; here we only want the numeric coordinates.
    """
    ref = (ref or "").strip()
    if is_ram:
        m = re.search(r"(\d+),\s*(\d+):\s*(\d+)(?:\s+(\d+))?", ref)
        if m:
            return {"kanda": int(m.group(1)), "sarga": int(m.group(2)),
                    "dcs_id": int(m.group(3)),
                    "verse": int(m.group(4)) if m.group(4) else None}
    m = re.search(r"(?:(\d+),\s*)?(\d+):\s*(\d+)(?:\s+(\d+))?", ref)
    if m:
        return {"kanda": int(m.group(1)) if m.group(1) else None,
                "sarga": int(m.group(2)), "dcs_id": int(m.group(3)),
                "verse": int(m.group(4)) if m.group(4) else None}
    return None


def plus_lemmas(matched_words):
    if not matched_words:
        return []
    return re.findall(r"\+\s*(\S+)", matched_words)


WORK_CODE = {"Rāmāyaṇa": "Rām", "Mahābhārata": "MBh"}


def work_code(name):
    return WORK_CODE.get(name, name)


def verse_span(verses):
    """Render a set of verse numbers as '27' or '37–39'."""
    vs = sorted(v for v in verses if v is not None)
    if not vs:
        return None
    if len(vs) == 1:
        return str(vs[0])
    if vs == list(range(vs[0], vs[-1] + 1)):
        return f"{vs[0]}–{vs[-1]}"
    return ",".join(str(v) for v in vs)


def shloka_label(sarga, verses):
    v = verse_span(verses) or "?"
    return f"V.{sarga}.{v}"


def address(code, kanda, sarga, verses):
    v = verse_span(verses)
    vs = f".{v}" if v else ""
    if code == "Rām":
        return f"Rām {kanda}.{sarga}{vs} (крит. изд.)"
    if kanda is not None:
        return f"{code} {kanda}.{sarga}{vs}"
    return f"{code} {sarga}{vs}"


CURATED_CLUSTERS = [
    "mbh_narrative", "mbh_battle", "mbh_gnomic", "ramayana_grintser",
    "dharmashastra", "kavya", "purana", "upanishads", "veda", "gita",
]


def load_curated_notes():
    """Load hand-curated cross-text notes as (cluster, shloka, token_set)."""
    out = []
    for c in CURATED_CLUSTERS:
        path = os.path.join(OUT_DIR, c + ".json")
        if not os.path.exists(path):
            continue
        try:
            data = json.load(open(path, encoding="utf-8"))
        except Exception:
            continue
        for n in data:
            if not isinstance(n, dict) or "_meta" in n:
                continue
            blob = " ".join(str(n.get(k, "")) for k in (
                "parallel_sa_iast", "lemma_iast", "sundara_sa_iast", "note_ru"))
            toks = set(norm_tokens(blob)) - STOP_TOKEN
            if toks:
                out.append((c, n.get("shloka"), toks))
    return out


def curated_overlap(note, curated, min_shared=3):
    """Return {cluster, shloka, shared} for the best hand-curated match, else {}."""
    mine = (set(norm_tokens(note["parallel_sa_iast"]))
            | set(norm_tokens(note["sundara_sa_iast"]))) - STOP_TOKEN
    best = {}
    for cluster, shloka, toks in curated:
        shared = mine & toks
        if len(shared) >= min_shared and len(shared) > len(best.get("shared_tokens", [])):
            best = {"cluster": cluster, "shloka": shloka,
                    "shared_tokens": sorted(shared)}
    return best


def main():
    con = sqlite3.connect(f"file:{ARCHIVE}?mode=ro", uri=True)
    cur = con.cursor()
    rows = cur.execute(
        """SELECT source_text_id, source_text_name, source_ref, source_verse,
                  target_text_id, target_text_name, target_ref, target_verse,
                  quality, matched_words, run
           FROM parallels
           WHERE source_text_id=? OR target_text_id=?""",
        (RAM_TEXT_ID, RAM_TEXT_ID),
    ).fetchall()

    # Aggregate by LOCUS: (anchor_sarga, parallel_work_code, parallel_sarga). The
    # two DB directions of one parallel, and multiple verse-level hits within a
    # sarga-pair, merge into a single per-verse apparatus note.
    loci = {}
    for (s_id, s_name, s_ref, s_verse, t_id, t_name, t_ref, t_verse,
         quality, mw, run) in rows:
        s_ram = s_id == RAM_TEXT_ID
        t_ram = t_id == RAM_TEXT_ID
        s_p = parse_ref(s_ref, s_ram)
        t_p = parse_ref(t_ref, t_ram)
        if not s_p or not t_p:
            continue
        sides = [("s", s_name, s_ram, s_p, s_verse),
                 ("t", t_name, t_ram, t_p, t_verse)]
        for i, (_, name, ram, p, text) in enumerate(sides):
            if not (ram and p["kanda"] == KANDA):
                continue  # anchor must be a Sundarakāṇḍa Rām verse
            _, pname, pram, pp, ptext = sides[1 - i]
            code = work_code(pname)
            key = (p["sarga"], code, pp["sarga"])
            L = loci.setdefault(key, {
                "anchor_sarga": p["sarga"], "anchor_kanda": p["kanda"],
                "anchor_verses": set(), "anchor_text": "",
                "par_code": code, "par_kanda": pp.get("kanda"),
                "par_sarga": pp["sarga"], "par_verses": set(), "par_text": "",
                "par_is_ram": pram, "quality": "PARTLY", "mw": set(), "run": run,
            })
            if p.get("verse") is not None:
                L["anchor_verses"].add(p["verse"])
            if pp.get("verse") is not None:
                L["par_verses"].add(pp["verse"])
            # Keep the fullest (longest) text seen for each side.
            if len((text or "").strip()) > len(L["anchor_text"]):
                L["anchor_text"] = (text or "").strip()
            if len((ptext or "").strip()) > len(L["par_text"]):
                L["par_text"] = (ptext or "").strip()
            if mw:
                L["mw"].add(mw)
            if quality == "GOOD":
                L["quality"] = "GOOD"

    curated = load_curated_notes()

    accepted, rejected = [], []
    for L in loci.values():
        overlap = content_overlap(L["anchor_text"], L["par_text"])
        scope = "intratext" if L["par_is_ram"] else "crosstext"
        par_addr = address(L["par_code"], L["par_kanda"], L["par_sarga"], L["par_verses"])
        mw_join = " · ".join(sorted(L["mw"]))
        note = {
            "shloka": shloka_label(L["anchor_sarga"], L["anchor_verses"]),
            "lemma_iast": " ".join(dict.fromkeys(
                lem for m in L["mw"] for lem in plus_lemmas(m))),
            "note_ru": "",  # machine layer — no fabricated prose
            "type": "А",   # philological/lexical parallel (Kazansky A)
            "trigger": "parallel",
            "priority": "high" if L["quality"] == "GOOD" else "medium",
            "source": f"DCS parallel-search ({L['quality']}); {par_addr}",
            "subtype": "cross_text",
            "scope": scope,
            "parallel_sa_iast": L["par_text"],
            "parallel_ru": "",
            "work_label": L["par_code"],
            "verse_address": par_addr,
            "sundara_sa_iast": L["anchor_text"],
            "quality": L["quality"],
            "matched_words": mw_join,
            "overlap_tokens": overlap,
            "overlap_n": len(overlap),
            "method": "fulltext",
            "run": L["run"],
            "provenance": "VisualDCS archive.sqlite parallels (fulltext run 2026)",
            "review_required": True,
        }
        # Dedup against hand-curated clusters (edition-agnostic: token overlap of
        # the Sanskrit text, since hand-curated notes use vulgate verse numbers).
        if scope == "crosstext":
            hit = curated_overlap(note, curated)
            note["curated_overlap"] = hit  # {} if none

        if len(overlap) < MIN_OVERLAP:
            note["reject_reason"] = (
                f"weak overlap: {len(overlap)} shared content token(s) "
                f"({', '.join(overlap) or '∅'}) — single-common-word / spurious"
            )
            note["reject_bucket"] = "weak_text_overlap"
            rejected.append(note)
        else:
            accepted.append(note)

    con.close()

    # crosstext first (rarer), GOOD before PARTLY, then by shloka.
    accepted.sort(key=lambda n: (
        0 if n["scope"] == "crosstext" else 1,
        0 if n["quality"] == "GOOD" else 1,
        -n["overlap_n"],
        n["shloka"],
    ))

    n_cross = sum(1 for n in accepted if n["scope"] == "crosstext")
    n_intra = sum(1 for n in accepted if n["scope"] == "intratext")
    covered = sorted({n["shloka"] for n in accepted})

    meta = {"_meta": {
        "cluster": "archive_parallels",
        "cluster_label": "DCS parallel-search (archive.sqlite) — межтекстовый + внутритекстовый слой",
        "description": (
            "Машинно-выявленный слой параллелей ко всей Сундараканде (кн. V), "
            "извлечённый из полнотекстового прогона параллельного поиска DCS "
            "(VisualDCS archive.sqlite, таблица parallels). Для каждого стиха "
            "Сундары показаны стихи ДРУГИХ корпусных текстов (scope=crosstext: "
            "Махабхарата) и внутритекстовые переклички Рамаяны (scope=intratext: "
            "формульные самоповторы). Санскритский текст обеих сторон приведён "
            "дословно; русская нота НЕ сочиняется машиной (review_required). "
            "matched_words = РАЗЛИЧАЮЩАЯ пара лемм DCS ('+ запрос - контрагент'), "
            "рендерится как есть; сила совпадения измеряется пересечением "
            "содержательных токенов текста (overlap_tokens)."
        ),
        "editorial_focus": (
            "Приоритет — crosstext (реальные интертекстуальные локусы: описание "
            "Ситы ↔ Дамаянти в МБх III.65 (два стиха); нити-стих mūlaghātiṣu "
            "sajjante ↔ МБх III.240). Внутритекстовые самоповторы = отдельный "
            "«эхо»-аппарат (split on scope)."
        ),
        "method": (
            "SELECT из parallels WHERE source_text_id=248 OR target_text_id=248; "
            "фильтр kāṇḍa=5; группировка по неориентированной паре нормализованных "
            "текстов стихов (дедуп двух направлений БД, восстановление номеров "
            f"стихов); adversarial-гейт: <{MIN_OVERLAP} общих содержательных токенов → reject."
        ),
        "edition_caveat": (
            "Нумерация сарг/стихов — КРИТИЧЕСКОЕ (Бародское) издание DCS, НЕ южная "
            "вульгата Леонова (68 сарг). Сопоставление с нумерацией Леонова требует "
            "слоя выравнивания изданий (scripts/sa_align.py, data/edition_comparison/). "
            "Здесь НЕ переприсваивается."
        ),
        "provenance": "VisualDCS archive.sqlite; fulltext run 2026; Rām text_id=248",
        "generator": "scripts/crosstext_archive_parallels.py",
        "model_provenance": "Deterministic SQL/Python extraction (no LLM). Curation session: Opus 4.8 (claude-opus-4-8).",
        "counts": {
            "accepted": len(accepted), "crosstext": n_cross,
            "intratext": n_intra, "rejected": len(rejected),
            "sundara_verses_covered": len(covered),
        },
    }}

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump([meta] + accepted, f, ensure_ascii=False, indent=2)
    with open(OUT_REJ, "w", encoding="utf-8") as f:
        json.dump(rejected, f, ensure_ascii=False, indent=2)
    write_coverage(accepted, rejected, n_cross, n_intra, covered)

    print(f"accepted={len(accepted)} (crosstext={n_cross}, intratext={n_intra}) "
          f"rejected={len(rejected)} verses_covered={len(covered)}")
    for p in (OUT_JSON, OUT_REJ, OUT_COV):
        print("  ->", os.path.relpath(p, REPO))


def write_coverage(accepted, rejected, n_cross, n_intra, covered):
    from collections import Counter
    cross = [n for n in accepted if n["scope"] == "crosstext"]
    work_dist = Counter(n["work_label"] for n in cross)
    rej_bucket = Counter(n.get("reject_bucket", "?") for n in rejected)

    L = ["# Cross-text apparatus (archive.sqlite) — Sundarakāṇḍa coverage", "",
         "_Created: 02-07-2026 · Last updated: 02-07-2026_", "",
         "Machine-derived from the VisualDCS DCS parallel-search "
         "([archive.sqlite](https://github.com/gasyoun/VisualDCS)) full-text run. "
         "Generator: [scripts/crosstext_archive_parallels.py]"
         "(https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/crosstext_archive_parallels.py). "
         "Layer file: [data/crosstext/archive_parallels.json]"
         "(https://github.com/gasyoun/CommentaryStrategies/blob/main/data/crosstext/archive_parallels.json).",
         "", "## Yield", "", "| Bucket | Count |", "|---|---|",
         f"| Accepted total | {len(accepted)} |",
         f"| — crosstext (other works) | {n_cross} |",
         f"| — intratext (Rām-internal echo) | {n_intra} |",
         f"| Rejected (adversarial gate) | {len(rejected)} |",
         f"| Sundara verses with ≥1 parallel | {len(covered)} |", "",
         "## Cross-text parallels by work", "", "| Work | Notes |", "|---|---|"]
    for w, c in work_dist.most_common():
        L.append(f"| {w} | {c} |")
    L += ["", "## Rejected buckets", "", "| Bucket | Count |", "|---|---|"]
    for b, c in rej_bucket.most_common():
        L.append(f"| {b} | {c} |")
    n_dupe = sum(1 for n in cross if n.get("curated_overlap"))
    L += ["", "## Cross-text candidates (full list)", "",
          f"Of {len(cross)} cross-text loci, **{n_dupe}** already have a "
          f"hand-curated equivalent (edition-agnostic Sanskrit-token match; the "
          f"machine layer independently rediscovered them at critical-edition "
          f"coordinates) and **{len(cross) - n_dupe}** {'is' if len(cross) - n_dupe == 1 else 'are'} new.", "",
          "| Sundara (crit.) | Parallel | Quality | Shared tokens | Hand-curated equivalent |",
          "|---|---|---|---|---|"]
    for n in cross:
        ov = n.get("curated_overlap") or {}
        dup = f"{ov['cluster']} {ov['shloka']}" if ov else "— (new)"
        L.append(f"| {n['shloka']} | {n['verse_address']} | {n['quality']} | "
                 f"{n['overlap_n']} ({', '.join(n['overlap_tokens'][:5])}) | {dup} |")
    L += ["", "## Caveats", "",
          "- **Edition numbering**: sarga/verse coordinates are DCS **critical "
          "(Baroda)** edition, not Leonov's southern vulgate (68 sargas). Mapping onto "
          "Leonov's numbering needs the edition-alignment layer "
          "([scripts/sa_align.py](https://github.com/gasyoun/CommentaryStrategies/blob/main/scripts/sa_align.py), "
          "[data/edition_comparison/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/edition_comparison)).",
          "- **Intratext ≠ crosstext**: the intratext echoes are Rāmāyaṇa-internal "
          "formulaic repetition, a distinct (legitimate) apparatus layer; split on "
          "`scope` before use.",
          "- **`matched_words` is the DCS *diff*** (differing lemma pair at the aligned "
          "position), NOT the shared overlap. The strength signal is `overlap_tokens` "
          "(shared content tokens of the two verse texts). Rendered raw, not reinterpreted.",
          "- **No fabricated prose**: `note_ru` / `parallel_ru` are intentionally empty. "
          "Every note is `review_required` and awaits editorial adjudication before "
          "entering an authored apparatus.", "",
          "_Auto-generated by scripts/crosstext_archive_parallels.py._"]
    with open(OUT_COV, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
