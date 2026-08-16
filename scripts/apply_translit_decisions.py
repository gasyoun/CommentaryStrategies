#!/usr/bin/env python3
"""Apply the h2864 transliteration vote to the source JSON (H2884).

Consumes the sheet's export — `{sheet_id, generated, decided, items: [{id,
decision, note, time_seconds}]}` — from
<https://gasyoun.github.io/vote/sheets/h2864_translit_residue.html>.

The sheet promised that a written note outranks the button, and the returned
ballot uses that promise heavily: 20 of 23 cards carry one. But a note is not
always a *reading*. Some are readings («героя», «версия», «pañcāsya»); others are
rulings in prose («саститель такого слова в русском языке нет… Есть спаситель,
есть губитель»), and pasting those into the corpus would write the reviewer's
sentence where a Sanskrit word belongs. So notes are split:

  * a note that IS a reading (one token, or an explicit `x -> y`) is applied;
  * a note that RULES rather than spells is resolved against the word's own
    sentence, and the resolution is written down in PROSE_RULINGS below with the
    evidence that settles it — never inferred silently at run time.

Usage:
    python scripts/apply_translit_decisions.py <decisions.json>            # dry run
    python scripts/apply_translit_decisions.py <decisions.json> --apply
"""
import argparse
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import translit_hygiene as th  # noqa: E402

sys.path.insert(0, os.path.join(os.path.dirname(REPO), "sanskrit-util", "py"))
try:
    from sanskrit_util import from_slp1
except ImportError:                                        # pragma: no cover
    from_slp1 = None

CARDS = os.path.join(REPO, "data", "analysis", "translit_residue_cards.json")
SHEET_ID = "h2864_translit_residue"

# Policy card 1, approved. ś is deliberately absent from the automatic table:
# the ballot approved it WITH a correction — «ś помимо ш может также быть и щ» —
# so ś is a per-word call, not a substitution. Only one covered word carries it
# (see PROSE_RULINGS).
TABLE = {"ṭ": "т", "Ṭ": "Т", "ḍ": "д", "Ḍ": "Д", "ṇ": "н", "Ṇ": "Н",
         "ṣ": "ш", "Ṣ": "Ш", "ṅ": "н", "Ṅ": "Н", "ñ": "н", "Ñ": "Н",
         "ā": "а", "Ā": "А", "ī": "и", "Ī": "И", "ū": "у", "Ū": "У",
         "ḥ": "х", "Ḥ": "Х", "ḷ": "л"}
# Policy card 2, approved = "by sign".
FORK_BY_SIGN = {"ṛ": "ри", "Ṛ": "Ри", "ṝ": "ри", "ṃ": "м", "Ṃ": "М"}
FORK_BY_SOUND = {"ṛ": "р", "Ṛ": "Р", "ṝ": "р", "ṃ": "н", "Ṃ": "Н"}
READER_FIELDS = {"note_ru", "raw_text", "lemma_iast", "candidate_lemma",
                 "edited_note", "text_ru"}

# Cards whose note is a RULING, resolved against the word's own sentence. Each
# entry records the evidence, so the call can be checked rather than trusted.
PROSE_RULINGS = {
    # «о caститель врагов» renders parantapa (MBh XII.128.47), and the reviewer
    # named the shape: «Есть спаситель, есть губитель». parantapa is "scorcher
    # of foes", so губитель — not спаситель, which would invert the epithet.
    "translit-004": ("губитель", "parantapa = «губитель врагов»; MBh XII.128.47"),
    # «ср. perс. shakar» — the abbreviation for персидский, per the note
    # «перс. от персидское». The full stop is already in the sentence.
    "translit-006": ("перс", "«ср. перс. shakar» — сокращение от «персидский»"),
    # «поясняют cesтита как „плач и подобное“» is ceṣṭita; the note rules that a
    # Sanskrit word goes in Latin, not Cyrillic.
    "translit-029": ("ceṣṭita", "ceṣṭita «движение, поведение»; правило — латиница"),
    # QA prose quoting a Russian crib: «chье желание исполнилось» = «чьё».
    "translit-030": ("чьё", "цитата подстрочника «чьё желание исполнилось»"),
    # A Sanskrit word correctly written in Latin that grew a Cyrillic ш; the note
    # says to drop the Cyrillic, and ś is what ш stands for here.
    "translit-019": ("śāpopahata", "śāpa- + upahata; ш → ś, кириллицу убрать"),
    # The note gives the stem, against two wrong machine candidates.
    "translit-017": ("муни", "«эпитета муни» — чистая основа, по примечанию"),
    "translit-018": ("смрити", "«Ману-смрити» — принятая во вторичной литературе форма"),
    "translit-009": ("Сурасу", "«Сурасу, сияющую как солнце» — вин. п. от Сураса"),
    "translit-026": ("of Janaka", "английская цитата Голдменов, потерян пробел"),
    # The note names the reading and says what the machine offered was rubbish —
    # and it was right: the candidate list held «етймология»/«етумология», which
    # is what an unguarded "first candidate" path would have written in.
    "translit-041": ("этимология", "по примечанию; машинные варианты отвергнуты"),
    # ś, the letter policy card 1 was approved WITH a correction about. Here it
    # is ш, not щ: «аśокового сада» is the aśoka tree, Russian «ашоковый».
    "translit-010": ("ашокового", "aśoka → «ашока»; ś здесь ш, не щ"),
    # manuṣyaloka: the «я» after ṣ carries a ya, so the pair is «шья», not «шя».
    "translit-016": ("манушьялока", "manuṣyaloka: ṣya → «шья», мягкий знак нужен"),
    "translit-027": ("каруна", "karuṇa — «каруна» (раса)"),
    # Both sit inside a SANSKRIT quotation, so translit-019's ruling applies —
    # a Sanskrit word correctly written in Latin keeps the Latin.
    "translit-036": ("viṣṇur", "цитата «viṣṇur eva svayaṃ bhūtvā» — латиница"),
    "translit-040": ("saṃśrava", "saṃ-√śru; санскрит в латинице"),
}
# Screened off the sheet (review/screening_evidence_h2864_translit_residue.md),
# so they carry no vote — but the evidence file promised each an outcome, and
# this is where those are honoured.
SCREENED_SLP1 = ("kzitAv", "laNkA", "siMha")     # -> from_slp1, deterministic
SCREENED_KEEP = ("ruH", "medъ")                  # reconstructions: leave alone
# Cards whose vote is explicitly not a repair.
DEFERRED = {"translit-024": "переспросить Костину — запись maharJayai в санскрите "
                            "невозможна, вероятно ошибка транслитерации"}

READING_RE = re.compile(r"^[^\s]+$")
ARROW_RE = re.compile(r"^\s*\S+\s*->\s*(.+?)\s*$")


def load_decisions(path):
    doc = json.load(open(path, encoding="utf-8"))
    if doc.get("sheet_id") != SHEET_ID:
        sys.exit(f"REFUSE: file is for sheet_id {doc.get('sheet_id')!r}, "
                 f"not {SHEET_ID!r}.")
    return {i["id"]: i for i in doc.get("items", [])}, doc


def note_reading(note):
    """A note that spells a reading -> that reading; a note that rules -> None."""
    n = (note or "").strip()
    if not n:
        return None
    m = ARROW_RE.match(n)
    if m:
        return m.group(1)
    return n if READING_RE.match(n) else None


def plan(cards, votes):
    repairs, skipped, blocked = {}, [], []
    for pid in ("policy-translit-table", "policy-fork-rows", "policy-qa-scope"):
        if not (votes.get(pid) or {}).get("decision"):
            blocked.append((pid, "не проголосовано — правило не определено"))
    if blocked:
        return repairs, skipped, blocked

    table_ok = votes["policy-translit-table"]["decision"] == "approve"
    qa_ok = votes["policy-qa-scope"]["decision"] == "approve"
    fork = (FORK_BY_SIGN if votes["policy-fork-rows"]["decision"] == "approve"
            else FORK_BY_SOUND)

    for c in cards:
        word, cid = c["word"], c["id"]
        if cid in DEFERRED:
            skipped.append((word, f"отложено: {DEFERRED[cid]}"))
            continue
        reader = any(o["field"] in READER_FIELDS for o in c["occurrences"])
        if not reader and not qa_ok:
            skipped.append((word, "служебное поле, п.3 отклонён"))
            continue

        if cid in PROSE_RULINGS:
            repairs[word] = PROSE_RULINGS[cid][0]
            continue
        if word in SCREENED_KEEP:
            skipped.append((word, "снято скринингом: реконструкция, смешение нормативно"))
            continue
        if word in SCREENED_SLP1:
            if from_slp1 is None:
                skipped.append((word, "снято скринингом, но sanskrit-util недоступен"))
            else:
                repairs[word] = from_slp1(word)
            continue
        vote = votes.get(cid, {})
        reading = note_reading(vote.get("note"))
        if reading:
            repairs[word] = reading
            continue
        if vote.get("decision") == "reject":
            skipped.append((word, "не дефект — оставлено как есть"))
            continue

        cyr = sum(1 for ch in word if re.match(f"[{th.CYR}]", ch))
        lat = sum(1 for ch in word if re.match(f"[{th.IAST}]", ch))
        covered = cyr > lat and any(ch in TABLE or ch in fork for ch in word)
        if covered:
            if not table_ok:
                skipped.append((word, "таблица транскрипции отклонена (п.1)"))
                continue
            merged = dict(TABLE)
            merged.update(fork)
            # A covered word can also carry a PLAIN Latin letter left behind by
            # the same dropped IME switch — `каруṇa` ends in a Latin `a`. The
            # transcription table only knows diacritics, so without this the word
            # comes out half-repaired («карунa»), which is worse than untouched:
            # it looks fixed. th.LAT_TO_CYR is the unambiguous half of H2831's map.
            merged.update({k: v for k, v in th.LAT_TO_CYR.items()
                           if k not in merged})
            fixed = "".join(merged.get(ch, ch) for ch in word)
            if any(re.match(f"[{th.IAST}]", ch) for ch in fixed):
                skipped.append((word, f"таблица не покрывает все знаки → {fixed!r}"))
            elif fixed != word:
                repairs[word] = fixed
            continue
        if vote.get("decision") == "approve" and c["candidates"]:
            repairs[word] = c["candidates"][0]["reading"]
        else:
            skipped.append((word, "не проголосовано и не покрыто правилом"))
    return repairs, skipped, blocked


def write(repairs):
    touched = {}
    for path in th.target_files():
        with open(path, encoding="utf-8", newline="") as fh:
            raw = fh.read()
        before = raw
        for bad, good in sorted(repairs.items(), key=lambda kv: -len(kv[0])):
            raw = raw.replace(bad, good)
        if raw == before:
            continue
        json.loads(raw)              # never write a file we just broke
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(raw)
        touched[os.path.relpath(path, REPO).replace("\\", "/")] = sum(
            before.count(b) for b in repairs)
    return touched


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("decisions")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    votes, doc = load_decisions(args.decisions)
    cards = json.load(open(CARDS, encoding="utf-8"))["cards"]
    repairs, skipped, blocked = plan(cards, votes)

    print(f"лист {doc['sheet_id']} · решений {doc.get('decided')} · "
          f"время {doc.get('time_total_seconds')} с")
    if blocked:
        print("\nОСТАНОВ:")
        for pid, why in blocked:
            print(f"  {pid}: {why}")
        return 2
    print(f"\nк исправлению {len(repairs)}:")
    for bad, good in sorted(repairs.items()):
        src = PROSE_RULINGS.get(
            next((c["id"] for c in cards if c["word"] == bad), ""), None)
        why = f"   ← {src[1]}" if src else ""
        print(f"  {bad!r:26} -> {good!r}{why}")
    print(f"\nне трогаем {len(skipped)}:")
    for word, why in sorted(skipped):
        print(f"  {word!r:26} — {why}")
    if not args.apply:
        print("\n(сухой прогон; повторите с --apply)")
        return 0
    touched = write(repairs)
    print(f"\nизменено файлов: {len(touched)}")
    for p in sorted(touched):
        print(f"  {p}")
    print("\nДальше: python scripts/translit_hygiene.py --check")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
