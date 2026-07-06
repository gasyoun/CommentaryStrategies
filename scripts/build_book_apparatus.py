#!/usr/bin/env python3
"""H268 WS-D: camera-ready ЛП print master for the Sundarakāṇḍa volume.

Builds the typeset-ready book master (Markdown; DOCX via pandoc when available)
from the repo's data layers — NOT the interactive HTML (that is the review
artifact; this is the print path):

  body        «Песнь N» — Leonov/Kostina's literary translation, verse-numbered,
              parsed from ramayana-leonov/«Рамаяна. Книга 5. Сундараканда 2026.html»
              (citation_block → chapter_block.translation);
  endnotes    «ПРИМЕЧАНИЯ» per sarga — merged apparatus:
                tier-1 Leonov notes verbatim (the reader apparatus);
                tier-2 generated notes (commentator/lexical/base/cross-text/
                hist-cultural), each SLOTTED with its gate status — nothing
                loses review_required here;
  appendix A  Kostina's editorial-control marks as a separate thin stratum
              (WS-E default (b) — until M.G. rules §8.4);
  appendix B+ skeleton pointers (edition-comparison table, epithet index,
              commentator-citation stats) — generated summaries, not prose.

Also writes BOOK_BUILD_REPORT.md: per-sarga translation completeness vs the
canonical vulgate verse count (the empirical answer to H268 §8.3), apparatus
counts by layer/status, and the open human gates.

Deterministic, stdlib-only.  Usage:
    python scripts/build_book_apparatus.py            # all 68 sargas
"""
import sys
import os
import re
import json
from collections import defaultdict
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DATA = os.path.join(REPO, "data")
sys.path.insert(0, HERE)
from sa_align import find_sibling  # noqa: E402

SRC = os.path.join(REPO, "ramayana-leonov", "Рамаяна. Книга 5. Сундараканда 2026.html")
T1 = os.path.join(DATA, "leonov_own_notes.json")
T2 = os.path.join(DATA, "sundara_commentary_to_add.json")
STATS = os.path.join(DATA, "analysis", "book_density_stats.json")
OUTDIR = os.path.join(DATA, "book")
JSONL = os.path.join(find_sibling("SamudraManthanam") or "",
                     "web", "corpus_builder", "jsonl", "05_ramayana-sundarakanda.jsonl")

SERVICE_MARKERS = ("[Claude.AI", "[Claude .AI", "Claude.AI —", "[Е. Костина]")

SUBTYPE_LABEL = {
    "commentator": "комментаторский диалог",
    "lexical": "лексический",
    "base": "базовый",
    "cross_text": "межтекстовый",
    "hist_cultural": "историко-культурный",
}


class BookParser(HTMLParser):
    """Pull per-verse translation text (chapter_block translation) per sarga."""

    def __init__(self):
        super().__init__()
        self.trans = defaultdict(dict)   # sarga -> {verse: text}
        self._sarga = None
        self._verse = None
        self._in_trans = 0
        self._depth = 0
        self._buf = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "")
        if tag == "div" and "citation_block" in cls:
            m = re.match(r"(\d+)\.(\d+)$", a.get("id", ""))
            if m:
                self._sarga, self._verse = int(m.group(1)), int(m.group(2))
        elif tag == "div" and "chapter_block" in cls and "translation" in cls:
            self._in_trans, self._depth, self._buf = 1, 1, []
        elif self._in_trans:
            self._depth += 1
            if tag == "br":
                self._depth -= 1          # void element
                self._buf.append("\n")

    def handle_endtag(self, tag):
        if self._in_trans:
            self._depth -= 1
            if self._depth <= 0:
                if self._sarga is not None and self._verse is not None:
                    txt = "".join(self._buf).strip()
                    if txt:
                        self.trans[self._sarga][self._verse] = txt
                self._in_trans = 0

    def handle_data(self, data):
        if self._in_trans:
            self._buf.append(data)


def canonical_counts():
    counts = defaultdict(set)
    if not os.path.exists(JSONL):
        return {}
    with open(JSONL, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            m = re.match(r"(\d+)\.(\d+)$", d.get("passage", ""))
            if m and d.get("seg") == "sa":
                counts[int(m.group(1))].add(int(m.group(2)))
    return {s: len(v) for s, v in counts.items()}


def gate_status(note):
    g = note.get("gate") or {}
    if g.get("action") in ("accept", "edit") or g.get("decision") in ("accept", "edit"):
        return "⟦гейт М.Г. ✓ · сборочный гейт Леонова/Костиной⟧"
    return "⟦ожидает гейта⟧"


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    p = BookParser()
    with open(SRC, encoding="utf-8") as fh:
        p.feed(fh.read())

    t1 = json.load(open(T1, encoding="utf-8"))["notes"]
    t2 = [n for n in json.load(open(T2, encoding="utf-8")) if "shloka" in n]
    canon = canonical_counts()

    leo = defaultdict(list)
    kos = defaultdict(list)
    for n in t1:
        s, v = int(n["sarga"]), n["verse"]
        if not str(v).isdigit():
            continue
        (kos if n.get("editor") == "kostina" else leo)[(s, int(v))].append(n)

    t2map = defaultdict(list)
    for n in t2:
        m = re.match(r"V\.(\d+)\.(\d+)", n["shloka"])
        if m:
            t2map[(int(m.group(1)), int(m.group(2)))].append(n)

    sargas = sorted(p.trans)
    body = []
    notes_md = []
    kost_md = []
    stats = defaultdict(int)

    body.append("# Рамаяна. Книга пятая. Сундараканда\n")
    body.append("_Перевод М. Леонова; литературная редакция Е. Костиной_\n")
    body.append("> **Сборка-макет (camera-ready draft)** — сгенерировано H268; "
                "формат по образцу серии «Литературные памятники» (эталоны корпуса: "
                "Кальянов, Васильков/Невелева, Елизаренкова). Шаблон ЛП — @DECIDE М.Г. (H268 §8.2).\n")

    for s in sargas:
        verses = p.trans[s]
        body.append(f"\n## Песнь {s}\n")
        for v in sorted(verses):
            txt = verses[v].replace("\n", "  \n")
            marks = []
            if (s, v) in leo or (s, v) in t2map:
                marks.append(f"[^{s}-{v}]")
            body.append(f"**{v}.** {txt}{''.join(marks)}\n")

        sarga_notes = []
        for v in sorted(set(k[1] for k in list(leo) + list(t2map) if k[0] == s)):
            entries = []
            for n in leo.get((s, v), []):
                text = n["raw_text"].strip()
                flag = ""
                if any(mk in text for mk in SERVICE_MARKERS):
                    flag = " ⟦содержит рабочие пометы — к сборке⟧"
                entries.append(f"{text}{flag}")
                stats["t1_leonov_notes"] += 1
            for n in t2map.get((s, v), []):
                sub = SUBTYPE_LABEL.get(n.get("subtype", "base"), n.get("subtype", ""))
                lemma = n.get("lemma_iast", "")
                entries.append(f"*{lemma}* — {n['note_ru'].strip()} "
                               f"⟨ярус 2 · {sub}⟩ {gate_status(n)}")
                stats["t2_notes"] += 1
                if "гейт М.Г. ✓" in gate_status(n):
                    stats["t2_gated_mg"] += 1
            if entries:
                sarga_notes.append((v, entries))

        if sarga_notes:
            notes_md.append(f"\n### К песни {s}\n")
            for v, entries in sarga_notes:
                for e in entries:
                    notes_md.append(f"**{s}.{v}.** {e}\n")

        for (ss, v), ns in sorted(kos.items()):
            if ss != s:
                continue
            for n in ns:
                kost_md.append(f"**{s}.{v}.** {n['raw_text'].strip()}\n")
                stats["kostina_marks"] += 1

    master = OUTDIR + os.sep + "sundarakanda_print_master.md"
    with open(master, "w", encoding="utf-8") as fh:
        fh.write("\n".join(body))
        fh.write("\n\n---\n\n# ПРИМЕЧАНИЯ\n")
        fh.write("\n> Ярус 1 (Леонов) — авторский аппарат, печатается как есть. "
                 "Ярус 2 (генерированный) — каждая нота помечена статусом гейта; "
                 "ни одна не теряет `review_required` до сборочного гейта Леонова/Костиной.\n")
        fh.write("\n".join(notes_md))
        fh.write("\n\n---\n\n# Приложение А. Редакционные пометы Е. Костиной (служебный слой)\n")
        fh.write("\n> WS-E: пометы — сигнал редактора (опущения, текстологические вопросы), "
                 "НЕ читательские примечания. Судьба слоя в печати — @DECIDE М.Г. (H268 §8.4); "
                 "по умолчанию вынесены отдельным стратумом.\n\n")
        fh.write("\n".join(kost_md))
        fh.write("\n\n---\n\n# Приложение Б. Сопоставление изданий (скелет)\n\n"
                 "> Источник: [data/edition_comparison/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/edition_comparison) "
                 "— 66 сарг критического (Барода) vs 68 южной вульгаты, +371 шлока; "
                 "51 сноска-кандидат ⟦ожидает гейта⟧ в [data/edition_footnotes/](https://github.com/gasyoun/CommentaryStrategies/tree/main/data/edition_footnotes).\n")
        fh.write("\n# Приложение В. Указатель эпитетов (скелет)\n\n"
                 "> Источник: [data/ramayana_epithets.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/ramayana_epithets.json) "
                 "— 509 эпитетных статей, 478 персонажей.\n")
        fh.write("\n# Приложение Г. Статистика цитирования комментаторов (скелет)\n\n"
                 "> Источник: [data/analysis/leonov_commentator_stats.json](https://github.com/gasyoun/CommentaryStrategies/blob/main/data/analysis/leonov_commentator_stats.json) "
                 "— Тилака 25.8%, Широмани 8.5%, Бхушана 8.2%; контрастивный слой 10.2%.\n")
        fh.write("\n\n_Сборка: scripts/build_book_apparatus.py (H268), Fable 5 (`claude-fable-5`)._\n")

    # ---- build report ----
    report = OUTDIR + os.sep + "BOOK_BUILD_REPORT.md"
    total_trans = sum(len(v) for v in p.trans.values())
    total_canon = sum(canon.values()) if canon else 0
    missing = []
    for s in sorted(set(list(canon.keys()) + sargas)):
        have, want = len(p.trans.get(s, {})), canon.get(s, 0)
        if want and have < want:
            missing.append((s, have, want))
    with open(report, "w", encoding="utf-8") as fh:
        fh.write("# Отчёт сборки книги (H268 WS-D)\n\n_Created: 07-07-2026 · Last updated: 07-07-2026_\n\n")
        fh.write(f"- Перевод в HTML-источнике: **{total_trans} строф** в {len(sargas)} песнях "
                 f"(канонический объём вульгаты: {total_canon}).\n")
        if missing:
            fh.write(f"- **Неполные песни ({len(missing)}) — эмпирика к §8.3 (@DECIDE полнота перевода):** "
                     + ", ".join(f"песнь {s}: {h}/{w}" for s, h, w in missing) + ".\n")
        else:
            fh.write("- Все песни укомплектованы против канонического счёта — §8.3 подтверждена эмпирически.\n")
        fh.write(f"- Примечания яруса 1 (Леонов, читательский аппарат): **{stats['t1_leonov_notes']}**.\n")
        fh.write(f"- Пометы Костиной (служебный слой, Приложение А): **{stats['kostina_marks']}**.\n")
        fh.write(f"- Ноты яруса 2 в мастере: **{stats['t2_notes']}** "
                 f"(из них гейтированы М.Г.: {stats['t2_gated_mg']}; все `review_required` до сборочного гейта).\n")
        fh.write("- Открытые человеческие гейты: сборочный гейт Леонова/Костиной (§8.1) · шаблон ЛП (§8.2) · "
                 "судьба помет Костиной (§8.4) · бюджет страниц при ~37% (§8.7).\n")
        fh.write("\n_Сгенерировано `scripts/build_book_apparatus.py`; оркестрация Fable 5 (`claude-fable-5`)._\n")

    print(f"master: {master}")
    print(f"report: {report}")
    print(f"translation verses: {total_trans}/{total_canon}; sargas: {len(sargas)}; "
          f"t1 notes {stats['t1_leonov_notes']}, kostina marks {stats['kostina_marks']}, "
          f"t2 notes {stats['t2_notes']} (MG-gated {stats['t2_gated_mg']})")
    if missing:
        print(f"incomplete sargas ({len(missing)}): " + ", ".join(f"{s}:{h}/{w}" for s, h, w in missing))


if __name__ == "__main__":
    main()
