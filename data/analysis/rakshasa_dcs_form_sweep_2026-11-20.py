#!/usr/bin/env python3
"""DCS FORM-свип семейства rākṣasa- по группам корпуса (H8498, M02 §1.4.8/§6).

Числа числового журнала: FORM-токены (колонка FORM, только строки-токены —
чистые формы, без смешения текст/глосса и без авто-парсов *_parsed) для
стемов rakṣas / rākṣasa / rākṣasī в КАЖДОЙ группе корпуса DCS-conllu
(Rāmāyaṇa, Mahābhārata, Kathāsaritsāgara, Garuḍapurāṇa, проч.), с пином
корпуса через runtime `git rev-parse HEAD` (паттерн H7924): нет клона/пина —
ненулевой выход, числа НЕ пишутся.

Корпус читается git-пламбингом на пине (ls-tree -r -z + cat-file --batch):
локальный sparse-checkout не расширяется. Повторный прогон на том же пине —
байт-идентичный JSON (порядок вставки детерминирован, таймстампов нет).

Образец: data/analysis/rakshasa_census_vulgate_2026-11-01.py (+ H7924).
Корпусный паттерн: VisualDCS derived-data/Fonetika/regen-2026 (REUSE_INDEX §1).

Usage: python3 rakshasa_dcs_form_sweep_2026-11-20.py [--corpus DIR]
Выход: rakshasa_dcs_form_sweep_2026-11-20.json рядом со скриптом;
        в stdout — corpus + headline + totals + путь сохранения.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

OUT = Path(__file__).with_suffix(".json")

# Кандидаты локального клона корпуса (как в образце H7924); --corpus переопределяет.
CANDIDATES = [
    (Path.home() / "Documents" / "GitHub" / "dcs-conllu", "dcs-conllu"),
    (Path.home() / "Documents" / "GitHub" / "DCS", "DCS"),
]

# Бакеты — конвенция переписи 01-11: семейство включает rākṣasī; ср. род disjoint.
IAST_FAMILY = re.compile(r"rākṣas")                         # rākṣasa- (вкл. rākṣasī)
IAST_RAKSHASI = re.compile(r"rākṣasī")
IAST_NEUTER = re.compile(r"rakṣas[ः]?\b|rakṣo\b|rakṣāṃsi")   # ср. род rakṣas- (без ā)
PARSED_TAIL = re.compile(r"_parsed(\.conllu)?$")

HEADLINE_GROUPS = ["Rāmāyaṇa", "Mahābhārata", "Kathāsaritsāgara", "Garuḍapurāṇa"]


def fail(msg):
    print(f"[H8498-FAIL] {msg}", file=sys.stderr)
    sys.exit(3)


def find_corpus(override):
    if override:
        p = Path(override)
        if (p / ".git").exists():
            return p, "override"
        fail(f"--corpus {p}: не git-клон")
    for p, label in CANDIDATES:
        if (p / ".git").exists():
            return p, label
    fail("локальный клон корпуса не найден (~/Documents/GitHub/dcs-conllu либо "
         "~/Documents/GitHub/DCS); числа НЕ выдуманы — прогон не состоялся")


def git_bytes(corpus, *args):
    r = subprocess.run(["git", "-C", str(corpus), *args], capture_output=True, timeout=120)
    if r.returncode != 0:
        fail("git %s: %s" % (" ".join(args[:2]), r.stderr.decode("utf-8", "replace")[:160]))
    return r.stdout


def main():
    corpus_override = None
    if "--corpus" in sys.argv:
        try:
            corpus_override = sys.argv[sys.argv.index("--corpus") + 1]
        except IndexError:
            fail("--corpus требует значение: путь к клону корпуса")
    corpus, corpus_label = find_corpus(corpus_override)

    pin = git_bytes(corpus, "rev-parse", "HEAD").decode().strip()
    if not pin:
        fail("пин корпуса пуст (git rev-parse HEAD); без пина числа не пишутся")

    # Перечень blob'ов на ПИНЕ (не рабочего дерева): NUL-разделённые записи.
    raw = git_bytes(corpus, "ls-tree", "-r", "-z", pin, "--", "files/")
    entries, skipped_parsed = [], 0
    for chunk in raw.split(b"\x00"):
        if not chunk:
            continue
        meta, _, path_b = chunk.partition(b"\t")
        parts = meta.decode().split(" ")
        if len(parts) != 3 or parts[1] != "blob":
            continue
        path = path_b.decode("utf-8", "replace")
        if path.count("/") < 2:
            continue  # blob прямо в files/, не в группе
        name = path.rsplit("/", 1)[-1]
        if PARSED_TAIL.search(name):
            skipped_parsed += 1
            continue
        if not name.endswith(".conllu"):
            continue
        entries.append((parts[2], path))

    groups = {}
    proc = subprocess.Popen(["git", "-C", str(corpus), "cat-file", "--batch"],
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def blob_text(sha):
        proc.stdin.write((sha + "\n").encode())
        proc.stdin.flush()
        header = proc.stdout.readline().decode()
        hp = header.split()
        if len(hp) != 3 or hp[1] != "blob":
            fail("блоб %s недоступен (%s); корпус повреждён?" % (sha, header.strip()[:60]))
        size = int(hp[2])
        data = proc.stdout.read(size + 1)
        return data[:-1].decode("utf-8", "replace")

    for sha, path in entries:
        group = path.split("/")[1]
        g = groups.setdefault(
            group, {"files": 0, "family": 0, "rakshasi": 0, "neuter": 0, "forms": {}})
        g["files"] += 1
        for line in blob_text(sha).splitlines():
            if not line or line.startswith("#"):
                continue
            cols = line.split("\t")
            # только строки-токены (ID — целое): чистые формы, без multiword-склеек
            if len(cols) < 2 or not cols[0].isdigit():
                continue
            form = cols[1]
            fam = IAST_FAMILY.search(form)
            neu = None if fam else IAST_NEUTER.search(form)
            if not (fam or neu):
                continue
            d = g["forms"].setdefault(
                form, {"rākṣasa_family": 0, "rākṣasī": 0, "rakṣas_neuter": 0})
            if fam:
                g["family"] += 1
                d["rākṣasa_family"] += 1
                if IAST_RAKSHASI.search(form):
                    g["rakshasi"] += 1
                    d["rākṣasī"] += 1
            else:
                g["neuter"] += 1
                d["rakṣas_neuter"] += 1
    proc.stdin.close()
    proc.wait()

    groups_out = {}
    for name in sorted(groups):
        g = groups[name]
        row = {"files": g["files"], "rākṣasa_family": g["family"],
               "rākṣasī": g["rakshasi"], "rakṣas_neuter": g["neuter"]}
        if g["forms"]:
            row["forms"] = [{"form": f, **cnt} for f, cnt in
                            sorted(g["forms"].items(),
                                   key=lambda kv: (-sum(kv[1].values()), kv[0]))]
        groups_out[name] = row

    totals = {"rākṣasa_family": 0, "rākṣasī": 0, "rakṣas_neuter": 0}
    for g in groups.values():
        totals["rākṣasa_family"] += g["family"]
        totals["rākṣasī"] += g["rakshasi"]
        totals["rakṣas_neuter"] += g["neuter"]
    totals["groups_nonzero_family"] = sum(1 for g in groups.values() if g["family"])

    report = {
        "script": Path(__file__).name,
        "unit": "H8498 — M02 §1.4.8/§6: DCS FORM-свип rākṣasa- (числа; проза не тронута)",
        "corpus": {
            "clone_label": corpus_label,
            "pin": pin,
            "pin_source": "git rev-parse HEAD in local clone (%s)" % corpus_label,
            "pin_rule": "нет клона/пина — ненулевой выход, числа не пишутся (H7924)",
            "groups_total": len(groups_out),
            "conllu_files_scanned": len(entries),
            "conllu_files_skipped_parsed": skipped_parsed,
        },
        "method": {
            "form_column": "CoNLL-U cols[1], только строки-токены (ID — целое); "
                            "multiword-склейки и комментарии не считаются",
            "buckets": {
                "rākṣasa_family": "подстрока «rākṣas» (семейство rākṣasa-, вкл. rākṣasī)",
                "rākṣasī": "подмножество family: подстрока «rākṣasī»",
                "rakṣas_neuter": "ср. род rakṣas-: rakṣas[ः]?\\b | rakṣo\\b | rakṣāṃsi "
                                 "(конвенция образца 01-11)",
            },
            "skipped": "файлы *_parsed — авто-парсы, не канонический слой (правило образца)",
        },
        "headline": {n: groups_out[n] for n in HEADLINE_GROUPS if n in groups_out},
        "groups": groups_out,
        "totals": totals,
        "dossier_crosscheck": ("досье §3 (веб-числа, НЕ печатные): Ram 131 / MBh 59 / "
                               "Kathā 24 / Garuda 8 — только сверка масштаба; печатные "
                               "числа — исключительно этот JSON."),
    }

    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    summary = {k: report[k] for k in ("corpus", "headline", "totals")}
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    print(f"\n[saved] {OUT}")


if __name__ == "__main__":
    main()
