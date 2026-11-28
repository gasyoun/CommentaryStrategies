#!/usr/bin/env python3
"""A74, угол A — три регистра (лес · город · ярлык): материал для доборов §1 статьи M02 (H8641).

Числовая единица без прозы статьи: три актива на зафиксированных источниках,
один прогон — один JSON. Проза доборов пишется автором после вердиктов ревью
(руление М.Г. 20-11-2026); драфт M02 и его метадок здесь не трогаются.

  1  compounds     каталог компаундов с rākṣasa- / rākṣasī- как членом по корпусу
                   DCS на пине: каждый токен — группа · локус · стих/предложение;
                   сверка с n1.compound_lemmas (a74_c_branch_n1_n4.json): 91.
  2  designations   обозначения ракшасов «Рамаяны»: компаунды DCS в «Рамаяне» и
                   записи data/ramayana_epithets.json (книги I–II) со словом
                   «ракшас»; guards — стражи Ашока-рощи (Сундара 22–27) по
                   переписи вульгаты (rakshasa_census_vulgate_2026-11-01.json).
  3  yuddha         юддха-срез переписи по саргам (канда 6 DCS): только числа,
                   без речевой атрибуции (N7 — блокер: разметки речи в DCS нет).

Пин — как в a74_c_branch_n1_n4.py: клон корпуса обязан стоять на пине свипа
f6ec30f2…; иначе ненулевой выход, числа НЕ пишутся. Классы вхождений и счётчики
берутся из самого модуля H8579 (тот же код — метод не расползается). Каждая
сумма сверяется с зафиксированным JSON; расхождение — тоже ненулевой выход.
Повторный прогон на том же пине — байт-идентичный JSON (таймстампов нет).

Usage: python3 a74_a_registers.py [--corpus DIR]
Выход: a74_a_registers.json рядом со скриптом; в stdout — сводка и путь.
"""
import json
import re
import statistics
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = Path(__file__).resolve().parent
OUT = HERE / "a74_a_registers.json"
N14_JSON = HERE / "a74_c_branch_n1_n4.json"
SWEEP_JSON = HERE / "rakshasa_dcs_form_sweep_2026-11-20.json"
VULGATE_JSON = HERE / "rakshasa_census_vulgate_2026-11-01.json"
EPITHETS_JSON = HERE.parent / "ramayana_epithets.json"
SHLOKAS_SUNDARA = HERE.parent / "valmiki_shlokas" / "kanda_5_sundarakanda"

sys.path.insert(0, str(HERE))
import a74_c_branch_n1_n4 as n14  # noqa: E402 — метод H8579: классы, счётчики, слои

PIN = "f6ec30f2fc0340189a39be8f47a792988f9f4784"   # пин хендоффа = пин свипа = пин H8579
RAM, MBH = "Rāmāyaṇa", "Mahābhārata"
YUDDHA_KANDA = 6
GUARD_BLOCK = (22, 27)        # стражи Ашока-рощи, Сундара (южная вульгата)
PER = 10000
COUNT_KEYS = ["tokens", "form_family", "simple", "simple_noun", "simple_adj", "simple_fem",
              "simple_other_pos", "compound", "cross_morpheme", "old_rakshas_lemma"]

# --- деванагари: стем и поверхностные классы словоформ ----------------------
STEM = "राक्षस"
DEV_RUN = re.compile(r"[ऀ-ॿ]+")
DEV_SPLIT = re.compile(r"[।॥॰]")
STEM_AT = re.compile(STEM)
VSIGN, VLETTER = r"[ा-ौ]", r"[अ-औ]"
# Класс читается по тексту сразу ПОСЛЕ стема в его позиции внутри слова (при
# склейке сандхи стем может стоять не в начале — «…आ + राक्षसी»). Здесь — окончания
# склонения rākṣasa- (м./ср. р.) с учётом внешнего сандхи; всё прочее за стемом —
# первый член компаунда (rākṣasendra, rākṣasādhipa, rākṣasa-rūpa …). Разбор
# морфологии не делается.
INFLECTED = re.compile(
    "^(?:श्च|ः|ं|ौ|ो|ै"
    "|म(?:$|्|" + VSIGN + "|" + VLETTER + ")"
    "|ा(?:$|ं|ः|स्|श्|न|त्|य|भ्याम्|भ्यः|ऽ|" + VSIGN + "|" + VLETTER + ")"
    "|े(?:$|ण|न(?![ा-ौ्])|षु|ष्|भ्यः|ऽ|" + VSIGN + "|" + VLETTER + "))"
)
# rākṣasyaḥ / rākṣasyo / rākṣasyā / rākṣasi и rākṣasyaḥ перед s- (राक्षस्यस्…)
FEM_YA = re.compile(r"^्य(?:[ःोा]|स्)|^ि")
GEN_SG = "्य"                             # rākṣasya — род. п. ед. ч.
FORM_CLASSES = ["fem_i", "fem_ya", "gen_sg", "stem_inflected",
                "compound_first", "compound_other", "cross_morpheme", "irregular"]

# --- русский эпитетный материал ---------------------------------------------
RU_WORD = re.compile("ракшас", re.I)
RU_FORM = re.compile(r"ракшас[а-яё]*", re.I)
CAP_RU = re.compile(r"[А-ЯЁ][а-яё]+")
OTHER_CLASS_WORDS = {"якшини": re.compile(r"якшин", re.I),
                     "асуры": re.compile(r"асур", re.I),
                     "данавы": re.compile(r"данав", re.I)}
ROSTER_ENTRY = "Ракшасы"
# Класс носителя записи — чтение исполнителя по тексту самих записей (27-11-2026),
# закрытый список: носитель вне списка останавливает прогон. Ростр (запись
# «Ракшасы» источника) сверяется с классом roster_member механически.
BEARER_CLASS = {
    "Вирадха": "roster_member", "Кхара": "roster_member", "Кабандха": "roster_member",
    "Марича": "roster_member", "Триширас": "roster_member", "Душана": "roster_member",
    "Шурпанакха": "roster_member",
    "Равана": "rakshasa_named", "Вибхишана": "rakshasa_named", "Субаху": "rakshasa_named",
    "Марича и Субаху": "rakshasa_named", "Синхика": "rakshasa_named",
    "Ракшасы Марича и Субах": "rakshasa_named",
    "Тарака": "mixed_in_source",
    "Брахма": "third_party", "Васава": "third_party", "Вишвамитра": "third_party",
    "Махадева": "third_party", "Пуластья": "third_party", "Сутикшна": "third_party",
    "Шиту": "third_party", "Джанастхана": "third_party",
}
NAMED_GLOSS = re.compile(r"([ऀ-ॿ]+?)\s*नाम\s+(?:called|named)\s+([A-Za-z]+)")
NAMED_TEXT = re.compile(r"नाम\s+(?:सा\s+)?राक्षसी")
NAMED_EN = re.compile(r"(?i:rakshasi|ogress|demoness|she[- ]demon)(?:\s+(?:called|named))?"
                      r"\s+([A-Z][a-z]+)\b")
SENT_META = re.compile(r"^# (sent_id|sent_counter|sent_subcounter) = (.+)$")
RANGE_ID = re.compile(r"^(\d+)-(\d+)$")     # multiword-строка CoNLL-U («1-2»)
FUNC_UPOS = {"CONJ", "CCONJ", "SCONJ", "PART", "PRON", "ADV", "NUM"}   # служебные части


def fail(msg):
    print(f"[H8641-FAIL] {msg}", file=sys.stderr)
    sys.exit(3)


def load_json(path, what):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        fail(f"{what} не прочитан ({path.name}: {exc})")


def find_corpus(override):
    if override:
        p = Path(override)
        if (p / ".git").exists():
            return p, "override"
        fail(f"--corpus {p}: не git-клон")
    for p, label in n14.CANDIDATES:
        if (p / ".git").exists():
            return p, label
    fail("локальный клон корпуса не найден (~/Documents/GitHub/dcs-conllu либо "
         "~/Documents/GitHub/DCS); числа НЕ выдуманы — прогон не состоялся")


def git_bytes(corpus, *args):
    r = subprocess.run(["git", "-C", str(corpus), *args], capture_output=True, timeout=120)
    if r.returncode != 0:
        fail("git %s: %s" % (" ".join(args[:2]), r.stderr.decode("utf-8", "replace")[:160]))
    return r.stdout


def corpus_entries(corpus, pin):
    """*.conllu на пине — те же фильтры, что в a74_c_branch_n1_n4.py."""
    raw = git_bytes(corpus, "ls-tree", "-r", "-z", pin, "--", "files/")
    entries, skipped = [], 0
    for chunk in raw.split(b"\x00"):
        if not chunk:
            continue
        meta, _, path_b = chunk.partition(b"\t")
        parts = meta.decode().split(" ")
        if len(parts) != 3 or parts[1] != "blob":
            continue
        path = path_b.decode("utf-8", "replace")
        if path.count("/") < 2:
            continue
        name = path.rsplit("/", 1)[-1]
        if n14.PARSED_TAIL.search(name):
            skipped += 1
            continue
        if name.endswith(".conllu"):
            entries.append((parts[2], path))
    entries.sort(key=lambda e: e[1])
    return entries, skipped


def locus_parts(group, locus):
    """Книга и единица деления из локуса: «Rām, Su, 6» → (5, 6); «MBh, 3, 282» → (3, 282)."""
    parts = [p.strip() for p in locus.split(",")]
    book = n14.book_number(group, locus)
    unit = int(parts[2]) if len(parts) >= 3 and parts[2].isdigit() else None
    return book, unit


def form_class(word, pos):
    """Поверхностный класс словоформы с राक्षस: по тексту после стема в позиции pos."""
    rest = word[pos + len(STEM):]
    if rest.startswith("ी"):
        return "fem_i"
    if FEM_YA.match(rest):
        return "fem_ya"
    if pos and rest == GEN_SG:
        # «…राक्षस्य» не в начале слова: у настоящего компаунда с последним членом
        # rākṣasa- род. п. даёт «…राक्षसस्य»; так пишутся имена на -राक्षस् + अक्ष «род. п.»
        return "cross_morpheme"
    if rest == GEN_SG:
        return "gen_sg"
    if not rest:
        return "stem_inflected"       # голый стем перед знаком препинания (5.58.147 — звательная форма)
    if INFLECTED.match(rest):
        return "stem_inflected"
    if rest.startswith("स्"):
        return "irregular"
    return "compound_first" if pos == 0 else "compound_other"


def member_of(lemma):
    """Каким членом компаунда стоит стем и какой это стем."""
    if lemma.startswith("rākṣasī") or lemma.endswith("rākṣasī"):
        return "rākṣasī", ("initial" if lemma.startswith("rākṣasī") else "final")
    return "rākṣasa", ("initial" if lemma.startswith("rākṣas") else "final")


def clean(dev):
    """Как в rakshasa_census_vulgate_2026-11-01.py: без английских пояснений в [скобках]."""
    return "\n".join(l for l in dev.splitlines() if not l.strip().startswith("["))


def per10k(num, den):
    return round(num * PER / den, 2) if den else None


def vid_key(vid):
    """Ключ сортировки verse_id «K.S.V»; нестандартные и пустые id — в конец."""
    parts = str(vid or "").split(".")
    if len(parts) == 3 and all(p.isdigit() for p in parts):
        return (0, tuple(int(p) for p in parts))
    return (1, (str(vid or ""),))


def desc(d):
    return dict(sorted(d.items(), key=lambda kv: (-kv[1], kv[0])))


def asc(d):
    return dict(sorted(d.items(), key=lambda kv: (len(kv[0]), kv[0])))


def walk_corpus(corpus, pin):
    """Один проход по корпусу: компаунды (все группы) + счётчики по файлам «Рамаяны»."""
    entries, skipped = corpus_entries(corpus, pin)
    tokens = []
    by_lemma, by_group, by_stratum = {}, {}, {}
    by_kanda, by_parvan, by_upos, by_member, by_position = {}, {}, {}, {}, {}
    ram_files, groups_seen = {}, set()      # ram_files: (канда, сарга) → счётчики файла
    ram_tokens, no_counter = 0, 0
    split_all, split_ram = {}, {}   # DCS multiword-строки с семейством: [n, upos частей]
    proc = subprocess.Popen(["git", "-C", str(corpus), "cat-file", "--batch"],
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def bump(d, k):
        d[k] = d.get(k, 0) + 1

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

    def flush(cur, prev_text, cur_text, next_text):
        for rec in cur:
            rec["text_prev"], rec["text"], rec["text_next"] = prev_text, cur_text, next_text
        tokens.extend(cur)

    for sha, path in entries:
        group = path.split("/")[1]
        groups_seen.add(group)
        is_ram = group == RAM
        text = blob_text(sha)
        if not is_ram and n14.IAST_FAMILY.pattern not in text:
            continue                # семейства в файле нет — строки не разбираем
        base = path.rsplit("/", 1)[-1][:-len(".conllu")]
        m = re.search(r"^\D*?-(\d+)-(.+)-\d+$", base)
        locus = m.group(2) if m else ""
        book, unit = locus_parts(group, locus)
        row = None
        if is_ram:
            if not book or not unit:
                fail(f"«Рамаяна»: локус без канды/сарги — {path}")
            row = ram_files.setdefault((book, unit), {"kanda": book, "sarga": unit,
                                                      "locus": locus, "files": 0,
                                                      **n14.counter_bucket()})
            row["files"] += 1
        st = n14.STRATUM_OF.get(group, "other")
        cur, prev_text, cur_text, meta = [], None, "", {}
        ordinal = sent_ord = 0
        pending = None             # multiword-строка «a-b»: ждём её частей a…b
        for line in text.splitlines():
            if line.startswith("# text ="):
                nxt = line[len("# text ="):].strip()
                flush(cur, prev_text, cur_text, nxt)
                prev_text, cur_text, cur, meta = (cur_text or None), nxt, [], {}
                pending = None
                sent_ord += 1
                continue
            if not line or line[0] == "#":
                mm = SENT_META.match(line) if line else None
                if mm:
                    meta[mm.group(1)] = mm.group(2).strip()
                continue
            cols = line.split("\t")
            mr = RANGE_ID.match(cols[0]) if cols else None
            if mr and len(cols) > 3 and n14.IAST_FAMILY.search(cols[1]):
                # DCS склеивает соединённые сандхи слова в multiword-строку и лемматизирует
                # по частям (rākṣasendra → rākṣasa + indra): в каталоге по леммам её нет
                pending = [int(mr.group(2)), []]
                continue
            # только строки-токены (ID — целое), как в H8579
            if len(cols) < 4 or not cols[0].isdigit():
                continue
            ordinal += 1
            form, lemma, upos = cols[1], cols[2], cols[3]
            if pending is not None:
                pending[1].append((lemma, upos))
                if int(cols[0]) == pending[0]:
                    parts = pending[1]
                    if any(l in n14.SIMPLE_LEMMAS or n14.token_class(l) == "compound"
                           for l, _ in parts):
                        key = "+".join(l for l, _ in parts)
                        for d in ((split_all, split_ram) if is_ram else (split_all,)):
                            rec = d.get(key)
                            if rec is None:
                                d[key] = rec = [0, "+".join(u for _, u in parts)]
                            rec[0] += 1
                    pending = None
            if is_ram:
                ram_tokens += 1
                row["tokens"] += 1
                if lemma == n14.OLD_STEM_LEMMA:
                    row["old_rakshas_lemma"] += 1
            if not n14.IAST_FAMILY.search(form):
                continue
            cls = n14.token_class(lemma)
            if is_ram:
                row["form_family"] += 1
                if cls == "compound":
                    row["compound"] += 1
                elif cls == "cross_morpheme":
                    row["cross_morpheme"] += 1
                else:
                    pc = n14.pos_class(lemma, upos)
                    row["simple"] += 1
                    row["simple_" + pc] += 1
            if cls != "compound":
                continue
            member, position = member_of(lemma)
            bump(by_lemma, lemma)
            bump(by_group, group)
            bump(by_stratum, st)
            bump(by_upos, upos)
            bump(by_member, member)
            bump(by_position, position)
            if group == RAM:
                bump(by_kanda, book)
            elif group == MBH and book:
                bump(by_parvan, book)
            if "sent_counter" not in meta:
                no_counter += 1
            cur.append({
                "group": group, "locus": locus,
                "kanda": book if group == RAM else None,
                "kanda_ru": n14.KANDA_RU.get(book) if group == RAM else None,
                "sarga": unit if group == RAM else None,
                "parvan": book if group == MBH else None,
                "parvan_ru": n14.PARVAN_RU.get(book) if group == MBH else None,
                "unit": unit, "file": path,
                "sent_ord": sent_ord, "sent_counter": meta.get("sent_counter"),
                "sent_subcounter": meta.get("sent_subcounter"), "sent_id": meta.get("sent_id"),
                "tok": cols[0], "form": form, "lemma": lemma, "upos": upos,
                "feats": cols[5] if len(cols) > 5 else "",
                "member": member, "position": position,
            })
        flush(cur, prev_text, cur_text, None)
    proc.stdin.close()
    proc.wait()

    tokens.sort(key=lambda r: (r["file"], r["sent_ord"], int(r["tok"])))
    tokens = [{"n": i, **rec} for i, rec in enumerate(tokens, 1)]   # n — номер в каталоге
    return {
        "tokens": tokens, "by_lemma": desc(by_lemma), "by_group": desc(by_group),
        "by_stratum": {s: by_stratum.get(s, 0) for s in n14.STRATUM_ORDER},
        "by_kanda": asc({str(k): v for k, v in by_kanda.items()}),
        "by_parvan": asc({str(k): v for k, v in by_parvan.items()}),
        "by_upos": desc(by_upos), "by_member": desc(by_member), "by_position": desc(by_position),
        "ram_files": ram_files, "groups_seen": groups_seen, "files_scanned": len(entries),
        "files_skipped_parsed": skipped, "ram_tokens": ram_tokens,
        "no_sent_counter": no_counter,
        "mw_all": split_all, "mw_ram": split_ram,
    }


def mw_summary(d):
    """DCS multiword-строки: {леммы частей: {n, upos}} + свёртка по служебным частям."""
    by = {k: {"n": v[0], "upos": v[1]}
          for k, v in sorted(d.items(), key=lambda kv: (-kv[1][0], kv[0]))}
    func = sum(v[0] for v in d.values() if FUNC_UPOS & set(v[1].split("+")))
    total = sum(v[0] for v in d.values())
    return {"strings_total": total, "distinct": len(d),
            "with_function_word_part": func, "without_function_word_part": total - func,
            "by_lemma_parts": by}


def build_compounds(walk, rep):
    """Каталог компаундов + сверки с зафиксированным JSON H8579."""
    n1, groups, n3, n4 = rep["n1"], rep["groups"], rep["n3"], rep["n4"]
    total = len(walk["tokens"])
    checks = {
        "lemmas_equal": walk["by_lemma"] == n1["compound_lemmas"],
        "total_equal": total == n1["totals"]["compound"],
        "by_group_equal": all(walk["by_group"].get(g, 0) == v["compound"]
                              for g, v in groups.items()),
        "by_stratum_equal": all(walk["by_stratum"][s] == v["compound"]
                                for s, v in n1["strata"].items()),
        "by_kanda_equal": all(walk["by_kanda"].get(k, 0) == v["compound"]
                              for k, v in n4["by_kanda"].items()),
        "by_parvan_equal": all(walk["by_parvan"].get(k, 0) == v["compound"]
                               for k, v in n3["by_parvan"].items()),
    }
    bad = [k for k, ok in checks.items() if not ok]
    if bad:
        fail("каталог компаундов разошёлся с a74_c_branch_n1_n4.json: " + ", ".join(bad))
    tokens = walk["tokens"]          # уже пронумерованы в порядке корпуса (ключ n)
    return {
        "source": "DCS на пине; класс вхождения — по LEMMA (a74_c_branch_n1_n4.token_class)",
        "tokens_total": total, "lemmas": len(walk["by_lemma"]),
        "by_lemma": walk["by_lemma"], "by_group": walk["by_group"],
        "by_stratum": walk["by_stratum"], "by_kanda": walk["by_kanda"],
        "by_parvan": walk["by_parvan"], "by_upos": walk["by_upos"],
        "by_member": walk["by_member"], "by_position": walk["by_position"],
        "locus_kind": {"with_sent_counter": total - walk["no_sent_counter"],
                       "ordinal_only": walk["no_sent_counter"]},
        "crosscheck_n14": checks,
        "dcs_multiword_strings": {
            "note": "DCS склеивает соединённые сандхи слова в multiword-строки «a-b» и лемматизирует "
                    "их по частям. Среди них — компаунды, которых нет в n1.compound_lemmas (их часть "
                    "rākṣasa там идёт простым стемом): rākṣasa+indra, rākṣasa+adhipa …; а также "
                    "сандхи-группы отдельных слов (rākṣasa+ca, rākṣasa+tad) — у них есть служебная "
                    "часть (upos: CONJ, PART, PRON, ADV, NUM). Все группы корпуса.",
            **mw_summary(walk["mw_all"]),
        },
        "tokens": tokens,
    }


def build_epithets(ep):
    """Записи data/ramayana_epithets.json со словом «ракшас» + класс носителя."""
    entries = ep["entries"]
    if ep["entry_count"] != len(entries):
        fail(f"ramayana_epithets.json: entry_count {ep['entry_count']} ≠ entries {len(entries)}")
    roster_entry = [e for e in entries if e["name"] == ROSTER_ENTRY]
    if len(roster_entry) != 1:
        fail(f"запись «{ROSTER_ENTRY}» в json эпитетов: найдено {len(roster_entry)}, нужно 1")
    roster = sorted({m for s in roster_entry[0].get("epithets", [])
                     for m in CAP_RU.findall(s)})
    roster_class = sorted(n for n, c in BEARER_CLASS.items() if c == "roster_member")
    if roster != roster_class:
        fail(f"ростр источника {roster} ≠ классу roster_member {roster_class}")
    selected, by_class, word_forms = [], {}, {}
    matched_n = 0
    for idx, e in enumerate(entries):
        strings = list(e.get("epithets", [])) + list(e.get("members", []))
        matched = [s for s in strings if RU_WORD.search(s)]
        in_name = bool(RU_WORD.search(e["name"]))
        if not matched and not in_name:
            continue
        name = e["name"]
        if name == ROSTER_ENTRY:
            cls = "roster_entry"
        elif name in BEARER_CLASS:
            cls = BEARER_CLASS[name]
        else:
            fail(f"носитель «{name}» вне закрытого списка классов — пополни BEARER_CLASS")
        by_class[cls] = by_class.get(cls, 0) + 1
        for s in matched:
            matched_n += 1
            for f in RU_FORM.findall(s):
                word_forms[f.lower()] = word_forms.get(f.lower(), 0) + 1
        others = {k: len(rx.findall(" ".join(strings))) for k, rx in OTHER_CLASS_WORDS.items()}
        rec = {
            "index": idx, "name": name, "type": e["type"], "class": cls,
            "n_epithets": e.get("n_epithets", e.get("n_members")),
            "in_name": in_name,
            "matched": [{"epithet": s, "forms": list(dict.fromkeys(f.lower() for f in RU_FORM.findall(s)))}
                        for s in matched],
            "other_class_words": {k: v for k, v in others.items() if v},
        }
        if cls != "third_party":
            rec["epithets"] = strings
        selected.append(rec)
    stale = sorted(set(BEARER_CLASS) - {r["name"] for r in selected})
    if stale:
        fail("в BEARER_CLASS носители, которых нет в отборе: " + ", ".join(stale))
    return {
        "source": "data/ramayana_epithets.json (книги I–II; эпитеты из примечаний Леонова)",
        "source_entry_count": ep["entry_count"],
        "filter": "имя записи или строка эпитета содержит «ракшас» (без учёта регистра)",
        "class_rule": ("roster_member — имя входит в ростр записи «Ракшасы» (разобран из её текста); "
                       "roster_entry — сама запись «Ракшасы»; rakshasa_named — ракшас/ракшаси вне "
                       "ростра, источник называет его словом «ракшас…» или именем; mixed_in_source — "
                       "в источнике и «якшини», и «ракшаси»; third_party — слово относится к другому "
                       "лицу, не к носителю записи"),
        "entries_selected": len(selected), "matched_epithets": matched_n,
        "by_class": dict(sorted(by_class.items())), "word_forms": desc(word_forms),
        "roster": roster,
        "entries": selected,
    }


def build_guards(vul):
    """Стражи Ашока-рощи: Сундара 22–27 по переписи вульгаты + стихи того же текста."""
    sv = vul["sundara_vs_southern"]
    a, b = GUARD_BLOCK
    census = {r["sarga"]: r for r in sv["sundara_tokens_by_sarga"]}
    blocks = [blk for blk in sv["sundara_blocks"] if tuple(blk["sargas"]) == GUARD_BLOCK]
    if len(blocks) != 1:
        fail(f"блок {list(GUARD_BLOCK)} в sundara_blocks: найдено {len(blocks)}, нужно 1")
    block = blocks[0]
    kanda_rows = [r for r in vul["census_by_kanda"] if r["kanda"] == n14.KANDA_RU[5]]
    if len(kanda_rows) != 1:
        fail("строка канды Сундара не найдена в census_by_kanda")
    krow = kanda_rows[0]
    by_sarga, occurrences, forms = [], [], {k: {} for k in FORM_CLASSES}
    kanda_cls = {k: 0 for k in FORM_CLASSES}   # те же классы по всей канде — для сопоставимых долей
    kanda_forms = {k: {} for k in FORM_CLASSES}
    named_all, named_a, named_b = {}, {}, {}
    nama_without_gloss = 0
    for sarga in sorted(census):               # вся канда; стихи и имена — только блок стражей
        in_block = a <= sarga <= b
        path = SHLOKAS_SUNDARA / f"sarga_{sarga:02d}.json"
        verses = load_json(path, "вульгата Сундары")
        fc, prev_id, no_id = {}, None, 0
        for item, v in enumerate(verses, 1):
            txt = clean(v.get("sanskrit", ""))
            vid = str(v.get("verse_id") or "")
            # В исходнике есть объекты с пустым verse_id (полустих отдельным объектом):
            # перепись их считает. Локус такой записи — позиция в сарге + ближайший
            # предыдущий номер стиха (after_verse).
            if not vid:
                no_id += 1
            if in_block:
                wbw, expl = v.get("word_by_word", ""), v.get("explanation", "")
                names = NAMED_GLOSS.findall(wbw)
                for dev, tr in names:
                    named_all.setdefault(tr, {"dev": dev, "verse_ids": []})["verse_ids"].append(vid)
                has_nama = bool(NAMED_TEXT.search(txt))
                if has_nama:
                    if names:
                        for dev, tr in names:
                            named_a.setdefault(tr, []).append(vid)
                    else:
                        nama_without_gloss += 1
                for tr in NAMED_EN.findall(expl):
                    # Английское написание может разойтись с глоссой (Surpanakha /
                    # Soorpanakha): в стихе с единственным именем по глоссе относим к нему.
                    key = names[0][1] if len(names) == 1 else tr
                    mm = re.search(r"([ऀ-ॿ]+)\s+" + re.escape(tr) + r"\b", wbw, re.I)
                    named_b.setdefault(key, []).append((vid, mm.group(1) if mm else None))
            if STEM in txt:
                seen = 0
                for run in DEV_RUN.findall(txt):
                    for word in DEV_SPLIT.split(run):
                        hits = [m.start() for m in STEM_AT.finditer(word)]
                        seen += len(hits)
                        for pos in hits:
                            cls = form_class(word, pos)
                            fc[cls] = fc.get(cls, 0) + 1
                            kanda_cls[cls] += 1
                            kanda_forms[cls][word] = kanda_forms[cls].get(word, 0) + 1
                            if in_block:
                                occurrences.append({"verse_id": vid,
                                                    "after_verse": None if vid else prev_id,
                                                    "sarga": sarga, "item": item, "word": word,
                                                    "stem_at": pos, "form_class": cls})
                                forms[cls][word] = forms[cls].get(word, 0) + 1
                if seen != txt.count(STEM):
                    fail(f"разбор деванагари {sarga}.{item}: {seen} ≠ {txt.count(STEM)}")
            if vid:
                prev_id = vid
        row = census.get(sarga)
        tot = sum(fc.values())
        if row is None:
            fail(f"сарга {sarga} отсутствует в sundara_tokens_by_sarga")
        if (row["tokens"], row["female"], row["verses"]) != (tot, fc.get("fem_i", 0), len(verses)):
            fail(f"сарга {sarga}: перепись {row} ≠ пересчёт по стихам ({tot}, "
                 f"{fc.get('fem_i', 0)}, {len(verses)})")
        if not in_block:
            continue
        by_sarga.append({
            "sarga": sarga, "verses": len(verses), "items_without_verse_id": no_id, "tokens": tot,
            "female_i": fc.get("fem_i", 0),
            "male_other_census": tot - fc.get("fem_i", 0),
            **{k: fc.get(k, 0) for k in FORM_CLASSES},
        })
    tot = {k: sum(r[k] for r in by_sarga) for k in ["verses", "tokens"] + FORM_CLASSES}
    if (tot["tokens"], tot["fem_i"], tot["tokens"] - tot["fem_i"]) != (
            block["tokens"], block["female"], block["male_other"]):
        fail(f"блок {list(GUARD_BLOCK)}: сумма по саргам ≠ sundara_blocks ({block})")
    if (sum(kanda_cls.values()), kanda_cls["fem_i"]) != (krow["rākṣasa-family"], krow["rākṣasī"]):
        fail("классы по всей канде Сундара разошлись с census_by_kanda")
    occurrences.sort(key=lambda o: (o["sarga"], o["item"], o["stem_at"]))
    named = {}
    for tr, vids in named_a.items():
        named[tr] = {"name": tr, "name_dev": named_all[tr]["dev"],
                     "verse_ids": list(vids), "patterns": ["nama_rakshasi"]}
    for tr, hits in named_b.items():
        rec = named.setdefault(tr, {"name": tr, "name_dev": named_all.get(tr, {}).get("dev"),
                                    "verse_ids": [], "patterns": []})
        rec["patterns"].append("english_apposition")
        rec["verse_ids"].extend(vid for vid, _ in hits)
        if not rec["name_dev"]:
            rec["name_dev"] = next((dev for _, dev in hits if dev), None)
    for tr, rec in named.items():
        rec["verse_ids"] = sorted(set(rec["verse_ids"] + named_all.get(tr, {}).get("verse_ids", [])),
                                  key=vid_key)
    named_list = sorted(named.values(), key=lambda r: (vid_key(r["verse_ids"][0]), r["name"]))
    fi, fy = tot["fem_i"], tot["fem_ya"]
    return {
        "source": "rakshasa_census_vulgate_2026-11-01.json + data/valmiki_shlokas/kanda_5_sundarakanda "
                  "(тот же текст и тот же подсчёт, что у переписи)",
        "block": list(GUARD_BLOCK),
        "form_classes": {
            "fem_i": "राक्षसी… — стем rākṣasī; женский бакет переписи (подстрока «राक्षसी»)",
            "fem_ya": "राक्षस्यः / राक्षस्यो / राक्षस्या / राक्षसि — формы типа rākṣasyaḥ (мн. ж. р. "
                      "от rākṣasī, по лемме DCS); подстрокой «राक्षसी» не берутся; поверхностно "
                      "омонимичны род. п. ед. ч. rākṣasya",
            "gen_sg": "राक्षस्य — род. п. ед. ч. «ракшаса»",
            "stem_inflected": "прочие формы склонения rākṣasa- (м./ср. р.), в т. ч. голый стем",
            "compound_first": "rākṣasa- первым членом компаунда (rākṣasendra, rākṣasādhipa …)",
            "compound_other": "стем не в начале слова: не первым членом компаунда либо в склейке "
                              "сандхи с предыдущим словом",
            "irregular": "за стемом идёт «स्»: правильного окончания a-основы такого нет "
                         "(в канде — только राक्षसस्य, по контексту род. п. «ракшаса»)",
            "cross_morpheme": "«…्राक्षस…»: «राक्षस» на стыке морфем (धूम्राक्षस्य, मकराक्षस्य — "
                              "имена на -राक्षस् + род. п.); в счёт переписи входит, словом "
                              "rākṣasa- не является",
        },
        "by_sarga": by_sarga, "totals": tot,
        "by_class": {k: tot[k] for k in FORM_CLASSES},
        "kanda_classes": kanda_cls,
        "kanda_forms": {k: desc(v) for k, v in kanda_forms.items()},
        "class_share_of_block_pct": {k: round(100 * tot[k] / tot["tokens"], 1) for k in FORM_CLASSES},
        "forms": {k: desc(v) for k, v in forms.items()},
        "shares": {
            "block_female_i": fi, "kanda_female_i": krow["rākṣasī"],
            "block_female_i_pct_of_kanda_female_i": round(100 * fi / krow["rākṣasī"], 1),
            "block_female_i_plus_ya": fi + fy,
            "kanda_female_i_plus_ya": kanda_cls["fem_i"] + kanda_cls["fem_ya"],
            "block_female_i_plus_ya_pct_of_kanda_female_i_plus_ya":
                round(100 * (fi + fy) / (kanda_cls["fem_i"] + kanda_cls["fem_ya"]), 1),
            "female_i_share_of_block_pct": round(100 * fi / tot["tokens"], 1),
            "female_i_plus_ya_share_of_block_pct": round(100 * (fi + fy) / tot["tokens"], 1),
            "block_tokens": tot["tokens"], "kanda_tokens": krow["rākṣasa-family"],
            "block_tokens_pct_of_kanda": round(100 * tot["tokens"] / krow["rākṣasa-family"], 1),
            "block_verses": tot["verses"], "kanda_verses": krow["verses"],
            "block_verses_pct_of_kanda": round(100 * tot["verses"] / krow["verses"], 1),
            "block_tokens_per_100_verses": round(100 * tot["tokens"] / tot["verses"], 1),
            "kanda_tokens_per_100_verses": krow["per_100"],
        },
        "crosscheck_census": {
            "block_equal": True, "by_sarga_equal": True, "kanda_equal": True,
            "sargas_checked": len(census),
            "census_block": {"tokens": block["tokens"], "female": block["female"],
                             "male_other": block["male_other"]},
        },
        "named_rule": ("nama_rakshasi — глосс «X nāma called/named Y» в стихе, где текст имеет "
                       "«nāma (sā) rākṣasī»; english_apposition — explanation «rakshasi/ogress/"
                       "demoness [called|named] <Name>»; verse_ids — все стихи блока, где имя названо"),
        "named_rakshasi": named_list,
        "named_all": [{"name": tr, "name_dev": v["dev"], "verse_ids": sorted(set(v["verse_ids"]), key=vid_key),
                       "rakshasi": tr in named} for tr, v in sorted(named_all.items())],
        "nama_verses_without_gloss_name": nama_without_gloss,
        "occurrences_total": len(occurrences),
        "occurrences_without_verse_id": sum(1 for o in occurrences if not o["verse_id"]),
        "occurrences": occurrences,
    }


def build_yuddha(walk, rep, vul):
    """Юддха-срез: канда 6 DCS по саргам, сверка с n4.by_kanda H8579."""
    k = YUDDHA_KANDA
    if any(r["files"] != 1 for key, r in walk["ram_files"].items() if key[0] == k):
        fail(f"канда {k}: сарга из нескольких файлов — таблица по саргам неоднозначна")
    comp_by_sarga = {}
    for t in walk["tokens"]:
        if t["group"] == RAM and t["kanda"] == k:
            comp_by_sarga.setdefault(t["sarga"], []).append(t["n"])
    rows = []
    for key in sorted(k for k in walk["ram_files"] if k[0] == YUDDHA_KANDA):
        sarga, r = key[1], walk["ram_files"][key]
        rows.append({"sarga": sarga, "files": r["files"], "locus": r["locus"],
                     **{key: r[key] for key in COUNT_KEYS},
                     "simple_per_10k": per10k(r["simple"], r["tokens"]),
                     "compound_tokens": comp_by_sarga.get(sarga, [])})
    totals = {key: sum(r[key] for r in rows) for key in COUNT_KEYS}
    totals["sargas"] = len(rows)
    totals["files"] = sum(r["files"] for r in rows)
    pinned = rep["n4"]["by_kanda"][str(k)]
    if not all(totals[key] == pinned[key] for key in COUNT_KEYS + ["files"]):
        fail(f"канда {k}: сумма по саргам разошлась с n4.by_kanda")
    simples = sorted(r["simple"] for r in rows)
    top = sorted(rows, key=lambda r: (-r["simple"], r["sarga"]))[:12]
    vul_rows = [r for r in vul["census_by_kanda"] if r["kanda"] == n14.KANDA_RU[k]]
    if len(vul_rows) != 1:
        fail("строка канды Юддха не найдена в census_by_kanda")
    return {
        "source": "DCS на пине, «Рамаяна», канда 6 (критическая рамка сарг: 116); счётчики H8579",
        "note": "Только числа по саргам: речевой атрибуции в DCS нет (N7). Вульгата — другой текст.",
        "kanda": k, "kanda_ru": n14.KANDA_RU[k],
        "totals": totals,
        "summary": {
            "sargas": len(rows),
            "sargas_zero_simple": sum(1 for x in simples if x == 0),
            "simple_max": simples[-1], "simple_median": statistics.median(simples),
            "simple_per_10k": per10k(totals["simple"], totals["tokens"]),
            "female_share_pct": round(100 * totals["simple_fem"] / totals["simple"], 1),
            "sargas_with_fem": [r["sarga"] for r in rows if r["simple_fem"]],
            "top_sargas_by_simple": [{"sarga": r["sarga"], "simple": r["simple"],
                                      "simple_fem": r["simple_fem"], "compound": r["compound"]}
                                     for r in top],
            "top12_simple_sum": sum(r["simple"] for r in top),
            "top12_simple_pct": round(100 * sum(r["simple"] for r in top) / totals["simple"], 1),
            "top_sargas_by_fem": [{"sarga": r["sarga"], "simple_fem": r["simple_fem"]}
                                  for r in sorted(rows, key=lambda r: (-r["simple_fem"], r["sarga"]))[:8]],
        },
        "vulgate_census_row": vul_rows[0],
        "crosscheck_n14": {"by_kanda_equal": True,
                           "pinned": {key: pinned[key] for key in COUNT_KEYS + ["files"]}},
        "by_sarga": rows,
    }


def main():
    override = None
    if "--corpus" in sys.argv:
        try:
            override = sys.argv[sys.argv.index("--corpus") + 1]
        except IndexError:
            fail("--corpus требует значение: путь к клону корпуса")
    rep = load_json(N14_JSON, "JSON H8579")
    sweep = load_json(SWEEP_JSON, "JSON FORM-свипа")
    pins = {"handoff": PIN, "sweep": sweep["corpus"]["pin"], "n14": rep["corpus"]["pin"]}
    if len(set(pins.values())) != 1:
        fail("пины расходятся: " + json.dumps(pins, ensure_ascii=False))
    vul = load_json(VULGATE_JSON, "JSON переписи вульгаты")
    ep = load_json(EPITHETS_JSON, "JSON эпитетов")
    corpus, corpus_label = find_corpus(override)
    head = git_bytes(corpus, "rev-parse", "HEAD").decode().strip()
    if head != PIN:
        fail(f"клон не на пине: HEAD {head[:12]} ≠ {PIN[:12]}; числа не пишутся")

    walk = walk_corpus(corpus, PIN)
    ram_sum = {key: sum(r[key] for r in walk["ram_files"].values()) for key in COUNT_KEYS}
    ram_files_n = sum(r["files"] for r in walk["ram_files"].values())
    corpus_checks = {
        "files_scanned_equal": walk["files_scanned"] == rep["corpus"]["conllu_files_scanned"],
        "files_skipped_equal": walk["files_skipped_parsed"] == rep["corpus"]["conllu_files_skipped_parsed"],
        "groups_equal": len(walk["groups_seen"]) == rep["corpus"]["groups_total"],
        "rāmāyaṇa_totals_equal": all(ram_sum[key] == rep["groups"][RAM][key] for key in COUNT_KEYS)
        and ram_files_n == rep["groups"][RAM]["files"],
    }
    bad = [k for k, ok in corpus_checks.items() if not ok]
    if bad:
        fail("проход по корпусу разошёлся с a74_c_branch_n1_n4.json: " + ", ".join(bad))

    comp = build_compounds(walk, rep)
    ram = [t for t in comp["tokens"] if t["group"] == RAM]
    dcs_ram = {"tokens": len(ram), "by_lemma": desc({l: sum(1 for t in ram if t["lemma"] == l)
                                                      for l in {t["lemma"] for t in ram}}),
               "by_kanda": comp["by_kanda"],
               "dcs_multiword_strings": mw_summary(walk["mw_ram"])}
    designations = {
        "dcs_compounds_rāmāyaṇa": dcs_ram,
        "epithets_books_1_2": build_epithets(ep),
        "guards_asoka_22_27": build_guards(vul),
    }
    yuddha = build_yuddha(walk, rep, vul)

    report = {
        "script": Path(__file__).name,
        "unit": "H8641 — A74, угол A: три регистра (лес · город · ярлык) — материал для доборов "
                "§1 статьи M02 («каталог стражей», «юддха-срез»); проза статьи не пишется",
        "corpus": {
            "clone_label": corpus_label,
            "pin": PIN,
            "pin_rule": "клон обязан стоять на пине свипа = пину H8579; иначе ненулевой выход, "
                        "числа не пишутся",
            "groups_total": len(walk["groups_seen"]),
            "conllu_files_scanned": walk["files_scanned"],
            "conllu_files_skipped_parsed": walk["files_skipped_parsed"],
            "rāmāyaṇa_files": ram_files_n,
            "rāmāyaṇa_tokens": walk["ram_tokens"],
            "crosscheck_n14": corpus_checks,
        },
        "inputs": {
            "n14": N14_JSON.name, "sweep": SWEEP_JSON.name, "vulgate": VULGATE_JSON.name,
            "epithets": "data/ramayana_epithets.json",
            "valmiki_shlokas": "data/valmiki_shlokas/kanda_5_sundarakanda/sarga_22–27.json",
        },
        "method": {
            "token_line": "CoNLL-U: только строки-токены (ID — целое); *_parsed пропущены",
            "family": "FORM содержит «rākṣas» — бакет свипа; класс — по LEMMA (модуль H8579)",
            "compound": "лемма содержит rākṣasa / rākṣasī как член; каждый токен — с группой, "
                        "локусом файла, № стиха (sent_counter) и строки (sent_subcounter), "
                        "предложением и соседними",
            "epithets": "запись отобрана, если имя или строка эпитета содержит «ракшас»",
            "guards": "Сундара 22–27 вульгаты: подсчёт переписи (подстрока «राक्षस» / «राक्षसी») "
                      "воспроизведён по стихам; класс словоформы — по тексту после стема",
            "yuddha": "канда 6 DCS по файлам-саргам; те же счётчики, что в n4.by_kanda H8579",
        },
        "compounds": comp,
        "designations": designations,
        "yuddha": yuddha,
    }
    # newline="\n" явно: байт-идентичность не зависит от платформы.
    with OUT.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(report, ensure_ascii=False, indent=1) + "\n")
    g, e = designations["guards_asoka_22_27"], designations["epithets_books_1_2"]
    summary = {
        "corpus": report["corpus"],
        "compounds": {k: comp[k] for k in ("tokens_total", "lemmas", "by_member", "by_position")},
        "epithets": {k: e[k] for k in ("entries_selected", "matched_epithets", "by_class")},
        "guards": {"totals": g["totals"], "by_class": g["by_class"],
                   "named_rakshasi": [r["name"] for r in g["named_rakshasi"]],
                   "nama_verses_without_gloss_name": g["nama_verses_without_gloss_name"],
                   "occurrences_without_verse_id": g["occurrences_without_verse_id"]},
        "yuddha": yuddha["summary"],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    print(f"\n[saved] {OUT}")


if __name__ == "__main__":
    main()
