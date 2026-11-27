#!/usr/bin/env python3
"""A74, ветка C — N1–N4: пересчёт по леммам, плотности, МБх по парвам, вульгата ↔ DCS (H8579).

Один проход по корпусу DCS-conllu на ТОМ ЖЕ пине, что у FORM-свипа
(rakshasa_dcs_form_sweep_2026-11-20.json `corpus.pin`): клон не на пине —
ненулевой выход, числа НЕ пишутся (паттерн H7924).

  N1  пересчёт по LEMMA/UPOS: простой стем (rākṣasa, rākṣasī) · компаунды ·
      межморфемные попадания (sahasrākṣa-, dhūmrākṣa- …); существительное /
      прилагательное / ж. р.; слои (архайический ведийский · поздневедийская
      обрядовая проза · дхарма · медицина · раса-шастра · тантра · эпосы);
      написания rākṣasam / rākṣasaṃ сходятся на лемме.
  N2  знаменатели: токены на группу → плотности на 10 000 токенов.
  N3  «Махабхарата» по парвам.
  N4  «Рамаяна» по кандам: DCS ↔ южная вульгата (rakshasa_census_vulgate_2026-11-01).
  Аудит: каждое внеэпическое вхождение — с контекстом; метки смысла читаются
      из a74_c_branch_n1_n4.audit.tsv (ручная разметка), без меток считаются
      «unlabelled» и ничем не заменяются.

Корпус читается git-пламбингом на пине (ls-tree -r -z + cat-file --batch):
локальный sparse-checkout не расширяется. Повторный прогон на том же пине и
с тем же audit-файлом — байт-идентичный JSON (таймстампов нет).

Usage: python3 a74_c_branch_n1_n4.py [--corpus DIR] [--dump-tokens]
Выход: a74_c_branch_n1_n4.json рядом со скриптом;
        --dump-tokens — ещё и a74_c_branch_n1_n4.tokens.tsv (внеэпические
        вхождения с контекстом, исходник для ручной разметки);
        в stdout — corpus, crosscheck, headline и путь сохранения.
"""
import csv
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

HERE = Path(__file__).parent
OUT = HERE / "a74_c_branch_n1_n4.json"
TOKENS_TSV = HERE / "a74_c_branch_n1_n4.tokens.tsv"
AUDIT_TSV = HERE / "a74_c_branch_n1_n4.audit.tsv"
SWEEP_JSON = HERE / "rakshasa_dcs_form_sweep_2026-11-20.json"
VULGATE_JSON = HERE / "rakshasa_census_vulgate_2026-11-01.json"

# Кандидаты локального клона корпуса (как в свипе H8498); --corpus переопределяет.
CANDIDATES = [
    (Path.home() / "Documents" / "GitHub" / "dcs-conllu", "dcs-conllu"),
    (Path.home() / "Documents" / "GitHub" / "DCS", "DCS"),
]

IAST_FAMILY = re.compile(r"rākṣas")          # семейство rākṣasa- (вкл. rākṣasī), бакет свипа
IAST_RAKSHASI = re.compile(r"rākṣasī")      # подстрока ж. р. — бакет переписи вульгаты (D2)
PARSED_TAIL = re.compile(r"_parsed(\.conllu)?$")
HEADLINE_GROUPS = ["Rāmāyaṇa", "Mahābhārata", "Kathāsaritsāgara", "Garuḍapurāṇa"]
SIMPLE_LEMMAS = ("rākṣasa", "rākṣasī")
OLD_STEM_LEMMA = "rakṣas"
PER = 10000
RANK_MIN_TOKENS = 20000   # рейтинг плотностей — только группы не меньше этого объёма

EPIC_GROUPS = ("Rāmāyaṇa", "Mahābhārata", "Harivaṃśa")

# Слои — явные списки групп DCS (270 групп); всё не перечисленное — «other».
STRATA = {
    "archaic_vedic": [
        "Aitareya-Āraṇyaka", "Aitareyabrāhmaṇa", "Aitareyopaniṣad",
        "Atharvaveda (Paippalāda)", "Atharvaveda (Śaunaka)", "Atharvavedapariśiṣṭa",
        "Baudhāyanaśrautasūtra", "Bhāradvājaśrautasūtra", "Bṛhadāraṇyakopaniṣad",
        "Chāndogyopaniṣad", "Drāhyāyaṇaśrautasūtra", "Garbhopaniṣat",
        "Jaiminīya-Upaniṣad-Brāhmaṇa", "Jaiminīyabrāhmaṇa", "Jaiminīyaśrautasūtra",
        "Kauṣītakibrāhmaṇa", "Kauṣītakyupaniṣad", "Kaṭhopaniṣad", "Kaṭhāraṇyaka",
        "Kātyāyanaśrautasūtra", "Kāṭhakasaṃhitā", "Maitrāyaṇīsaṃhitā",
        "Mānavaśrautasūtra", "Muṇḍakopaniṣad", "Nirukta", "Pañcaviṃśabrāhmaṇa",
        "Sāmavidhānabrāhmaṇa", "Taittirīyabrāhmaṇa", "Taittirīyasaṃhitā",
        "Taittirīyopaniṣad", "Taittirīyāraṇyaka", "Vaitānasūtra",
        "Vaikhānasaśrautasūtra", "Vājasaneyisaṃhitā (Mādhyandina)",
        "Vārāhaśrautasūtra", "Āpastambaśrautasūtra", "Śatapathabrāhmaṇa",
        "Śira'upaniṣad", "Śvetāśvataropaniṣad", "Śāṅkhāyanaśrautasūtra",
        "Śāṅkhāyanāraṇyaka", "Ṛgveda", "Ṛgvedakhilāni", "Ṛgvedavedāṅgajyotiṣa",
        "Ṛgvidhāna", "Ṣaḍviṃśabrāhmaṇa",
    ],
    "late_vedic_ritual": [
        "Āpastambagṛhyasūtra", "Baudhāyanagṛhyasūtra", "Bhāradvājagṛhyasūtra",
        "Gobhilagṛhyasūtra", "Gopathabrāhmaṇa", "Hiraṇyakeśigṛhyasūtra",
        "Jaiminigṛhyasūtra", "Khādiragṛhyasūtra", "Kauṣītakagṛhyasūtra",
        "Kāṭhakagṛhyasūtra", "Mānavagṛhyasūtra", "Pāraskaragṛhyasūtra",
        "Paraśurāmakalpasūtra", "Vaikhānasagṛhyasūtra", "Vārāhagṛhyasūtra",
        "Āśvalāyanagṛhyasūtra", "Śāṅkhāyanagṛhyasūtra",
    ],
    "dharma": [
        "Āpastambadharmasūtra", "Baudhāyanadharmasūtra", "Gautamadharmasūtra",
        "Vaikhānasadharmasūtra", "Vasiṣṭhadharmasūtra", "Manusmṛti",
        "Yājñavalkyasmṛti", "Viṣṇusmṛti", "Nāradasmṛti", "Kātyāyanasmṛti",
        "Parāśaradharmasaṃhitā", "Parāśarasmṛtiṭīkā", "Vṛddhayamasmṛti",
        "Gṛhastharatnākara", "Nibandhasaṃgraha",
    ],
    "medicine": [
        "Aṣṭāṅgahṛdayasaṃhitā", "Aṣṭāṅgasaṃgraha", "Aṣṭāṅganighaṇṭu",
        "Āyurvedadīpikā", "Ayurvedarasāyana", "Bhāvaprakāśa", "Carakasaṃhitā",
        "Carakatattvapradīpikā", "Dhanvantarinighaṇṭu", "Indu (ad AHS)",
        "Kaiyadevanighaṇṭu", "Madanapālanighaṇṭu", "Nāḍīparīkṣā",
        "Rājanighaṇṭu", "Sarvāṅgasundarā", "Suśrutasaṃhitā", "Śārṅgadharasaṃhitā",
        "Śārṅgadharasaṃhitādīpikā", "Yogaratnākara",
    ],
    "rasa": [
        "Rasahṛdayatantra", "Rasakāmadhenu", "Rasamañjarī",
        "Rasaprakāśasudhākara", "Rasaratnasamuccaya",
        "Rasaratnasamuccayabodhinī", "Rasaratnasamuccayadīpikā",
        "Rasaratnasamuccayaṭīkā", "Rasaratnākara", "Rasasaṃketakalikā",
        "Rasataraṅgiṇī", "Rasendracintāmaṇi", "Rasendracūḍāmaṇi",
        "Rasendrasārasaṃgraha", "Rasādhyāya", "Rasādhyāyaṭīkā", "Rasārṇava",
        "Rasārṇavakalpa",
    ],
    "tantra": [
        "Ānandakanda", "Devīkālottarāgama", "Kṛṣṇāmṛtamahārṇava",
        "Mahācīnatantra", "Mātṛkābhedatantra", "Mṛgendratantra",
        "Mṛgendraṭīkā", "Pañcārthabhāṣya", "Pāśupatasūtra", "Saṃvitsiddhi",
        "Spandakārikā", "Spandakārikānirṇaya", "Sātvatatantra", "Tantrasāra",
        "Tantrāloka", "Toḍalatantra", "Uḍḍāmareśvaratantra",
        "Vātūlanāthasūtras", "Vātūlanāthasūtravṛtti", "Śivasūtra",
        "Śivasūtravārtika", "Śāktavijñāna",
    ],
    "epic": list(EPIC_GROUPS),
}
STRATUM_OF = {g: s for s, gs in STRATA.items() for g in gs}
STRATUM_ORDER = ["archaic_vedic", "late_vedic_ritual", "dharma", "medicine", "rasa",
                 "tantra", "epic", "other"]

KANDA_OF = {"Bā": 1, "Ay": 2, "Ār": 3, "Ki": 4, "Su": 5, "Yu": 6, "Utt": 7}
KANDA_RU = {1: "Бала", 2: "Аётья", 3: "Аранья", 4: "Кишикиндха", 5: "Сундара", 6: "Юддха"}
PARVAN_RU = {
    1: "Ādi", 2: "Sabhā", 3: "Vana", 4: "Virāṭa", 5: "Udyoga", 6: "Bhīṣma",
    7: "Droṇa", 8: "Karṇa", 9: "Śalya", 10: "Sauptika", 11: "Strī", 12: "Śānti",
    13: "Anuśāsana", 14: "Aśvamedhika", 15: "Āśramavāsika", 16: "Mausala",
    17: "Mahāprasthānika", 18: "Svargārohaṇa",
}

AUDIT_LABELS = ["being", "compound", "marriage", "rite", "quality", "label",
                "technical", "cross_morpheme", "unclear"]


def fail(msg):
    print(f"[H8579-FAIL] {msg}", file=sys.stderr)
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


def token_class(lemma):
    """Класс вхождения по лемме: simple · compound · cross_morpheme.

    Компаунд — rākṣasa-/rākṣasī- первым или последним членом; на стыке возможен
    сандхи (rākṣasa + īśvara → rākṣaseśvara, rākṣasa + ālaya → rākṣasālaya),
    поэтому первый член проверяется по префиксу «rākṣas».
    """
    if lemma in SIMPLE_LEMMAS:
        return "simple"
    if lemma.startswith("rākṣas") or lemma.endswith(("rākṣasa", "rākṣasī")):
        return "compound"
    return "cross_morpheme"


def pos_class(lemma, upos):
    if lemma == "rākṣasī":
        return "fem"
    return {"NOUN": "noun", "ADJ": "adj"}.get(upos, "other_pos")


def book_number(group, locus):
    """Номер книги по локусу из имени файла: «Rām, Su, 6» → 5; «MBh, 7, 3» → 7."""
    parts = [p.strip() for p in locus.split(",")]
    if len(parts) < 2:
        return None
    if group == "Rāmāyaṇa":
        return KANDA_OF.get(parts[1])
    if group == "Mahābhārata" and parts[1].isdigit():
        return int(parts[1])
    return None


def per10k(num, den):
    return round(num * PER / den, 2) if den else None


def counter_bucket():
    return {"tokens": 0, "form_family": 0, "simple": 0, "simple_noun": 0,
            "simple_adj": 0, "simple_fem": 0, "simple_other_pos": 0,
            "compound": 0, "cross_morpheme": 0, "old_rakshas_lemma": 0}


def load_audit(non_epic):
    """Метки senses: audit-файл (n, form, label, note) → {n: label}.

    n — номер строки внеэпического вхождения в порядке прохода (тот же, что в
    a74_c_branch_n1_n4.tokens.tsv). Форма в строке файла обязана совпасть с
    формой вхождения: расходится — прогон останавливается, а не тихо съезжает.
    """
    labels = {}
    if not AUDIT_TSV.exists():
        return labels
    with AUDIT_TSV.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if not row.get("n") or not row.get("label"):
                continue
            n = int(row["n"])
            tok = non_epic[n - 1]
            if row.get("form") and row["form"] != tok[4]:
                fail("audit: строка %d — форма «%s» ≠ «%s»; порядок вхождений изменился"
                     % (n, row["form"], tok[4]))
            if row["label"] not in AUDIT_LABELS:
                fail("audit: неизвестная метка «%s» (строка %d); допустимы: %s"
                     % (row["label"], n, ", ".join(AUDIT_LABELS)))
            labels[n] = row["label"]
    return labels


def main():
    corpus_override = None
    if "--corpus" in sys.argv:
        try:
            corpus_override = sys.argv[sys.argv.index("--corpus") + 1]
        except IndexError:
            fail("--corpus требует значение: путь к клону корпуса")
    dump_tokens = "--dump-tokens" in sys.argv
    corpus, corpus_label = find_corpus(corpus_override)

    try:
        sweep_pin = json.loads(SWEEP_JSON.read_text(encoding="utf-8"))["corpus"]["pin"]
        sweep_family = json.loads(SWEEP_JSON.read_text(encoding="utf-8"))["totals"]["rākṣasa_family"]
    except (OSError, KeyError, ValueError) as exc:
        fail(f"свип JSON не прочитан ({SWEEP_JSON.name}: {exc}); пин свипа неизвестен")
    pin = git_bytes(corpus, "rev-parse", "HEAD").decode().strip()
    if pin != sweep_pin:
        fail(f"клон не на пине свипа: HEAD {pin[:12]} ≠ {sweep_pin[:12]}; числа не пишутся")

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
            continue
        name = path.rsplit("/", 1)[-1]
        if PARSED_TAIL.search(name):
            skipped_parsed += 1
            continue
        if name.endswith(".conllu"):
            entries.append((parts[2], path))
    entries.sort(key=lambda e: e[1])

    groups = {}
    lemma_pos = {}
    compound_lemmas = {}
    cross_lemmas = {}
    books = {"Rāmāyaṇa": {}, "Mahābhārata": {}, "Harivaṃśa": {}}
    strata = {s: counter_bucket() for s in STRATUM_ORDER}
    strata_groups = {s: set() for s in STRATUM_ORDER}
    tokens_total = 0
    form_anusvara = form_final_m = 0
    fem_forms, fem_substring = {}, 0
    non_epic = []

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
        base = path.rsplit("/", 1)[-1][:-len(".conllu")]
        m = re.search(r"^\D*?-(\d+)-(.+)-\d+$", base)
        locus = m.group(2) if m else ""
        st = STRATUM_OF.get(group, "other")
        strata_groups[st].add(group)
        g = groups.setdefault(group, {**counter_bucket(), "files": 0})
        g["files"] += 1
        book_no = book_number(group, locus)
        bk = (books[group].setdefault(book_no, {**counter_bucket(), "files": 0})
              if group in books and book_no else None)
        if bk is not None:
            bk["files"] += 1
        sk = strata[st]
        textline = ""
        ordinal = 0
        for line in blob_text(sha).splitlines():
            if line.startswith("# text ="):
                textline = line[len("# text ="):].strip()
                continue
            if not line or line[0] == "#":
                continue
            cols = line.split("\t")
            # только строки-токены (ID — целое): чистые формы, без multiword-склеек
            if len(cols) < 4 or not cols[0].isdigit():
                continue
            ordinal += 1
            for b in (g, sk, bk):
                if b is not None:
                    b["tokens"] += 1
            tokens_total += 1
            form, lemma, upos = cols[1], cols[2], cols[3]
            if lemma == OLD_STEM_LEMMA:
                for b in (g, sk, bk):
                    if b is not None:
                        b["old_rakshas_lemma"] += 1
            if not IAST_FAMILY.search(form):
                continue
            for b in (g, sk, bk):
                if b is not None:
                    b["form_family"] += 1
            if "ṃ" in form:
                form_anusvara += 1
            if form.endswith("m"):
                form_final_m += 1
            cls = token_class(lemma)
            pc = pos_class(lemma, upos) if cls == "simple" else None
            lp = lemma_pos.setdefault(lemma, {})
            lp[upos] = lp.get(upos, 0) + 1
            if cls == "compound":
                compound_lemmas[lemma] = compound_lemmas.get(lemma, 0) + 1
                for b in (g, sk, bk):
                    if b is not None:
                        b["compound"] += 1
            elif cls == "cross_morpheme":
                cross_lemmas[lemma] = cross_lemmas.get(lemma, 0) + 1
                for b in (g, sk, bk):
                    if b is not None:
                        b["cross_morpheme"] += 1
            else:
                for b in (g, sk, bk):
                    if b is not None:
                        b["simple"] += 1
                        b["simple_" + pc] += 1
                if group == "Rāmāyaṇa" and lemma == "rākṣasī":
                    # женский род «Рамаяны» по лемме: какие формы он покрывает
                    fem_forms[form] = fem_forms.get(form, 0) + 1
                    if IAST_RAKSHASI.search(form):
                        fem_substring += 1
            if group not in EPIC_GROUPS:
                non_epic.append((f"{group}|{base}#{ordinal}", st, group, locus, form,
                                 lemma, upos, cls, pc, textline))
    proc.stdin.close()
    proc.wait()

    # Списки слоёв — часть метода: имя, которого нет в корпусе, опечатка, а не ноль.
    unknown = sorted(g for s, gs in STRATA.items() for g in gs if g not in groups)
    if unknown:
        fail("в списках слоёв групп нет в корпусе: %s" % ", ".join(unknown))

    # --- N1: итоги ---------------------------------------------------------
    tot = counter_bucket()
    for s in STRATUM_ORDER:
        for k in counter_bucket():
            tot[k] += strata[s][k]
    tot["groups_total"] = len(groups)
    tot["groups_nonzero_simple"] = sum(1 for g in groups.values() if g["simple"])
    two_epics = sum(groups[n]["simple"] for n in ("Rāmāyaṇa", "Mahābhārata") if n in groups)
    two_epics_form = sum(groups[n]["form_family"] for n in ("Rāmāyaṇa", "Mahābhārata") if n in groups)
    n1 = {
        "totals": tot,
        "simple_by_lemma_pos": {l: dict(sorted(v.items())) for l, v in sorted(lemma_pos.items())
                                if l in SIMPLE_LEMMAS},
        "compound_lemmas": dict(sorted(compound_lemmas.items(), key=lambda kv: (-kv[1], kv[0]))),
        "cross_morpheme_lemmas": dict(sorted(cross_lemmas.items(), key=lambda kv: (-kv[1], kv[0]))),
        "form_spelling": {
            "family_forms_with_anusvara_ṃ": form_anusvara,
            "family_forms_ending_in_m": form_final_m,
            "note": "rākṣasam / rākṣasaṃ — написания различаются в FORM и сходятся на лемме",
        },
        "epic_share": {
            "two_epics_form_family_pct": round(100 * two_epics_form / tot["form_family"], 1),
            "two_epics_simple_pct": round(100 * two_epics / tot["simple"], 1),
            "two_epics_simple": two_epics,
            "two_epics_form_family": two_epics_form,
        },
        "feminine_rāmāyaṇa": {
            "by_lemma": groups["Rāmāyaṇa"]["simple_fem"] if "Rāmāyaṇa" in groups else 0,
            "by_lemma_with_substring_rākṣasī": fem_substring,
            "forms": dict(sorted(fem_forms.items(), key=lambda kv: (-kv[1], kv[0]))),
            "note": "подстрока «rākṣasī» (бакет D2) не берёт косые формы rākṣasyaḥ / rākṣasyo / rākṣasyā / rākṣasi",
        },
        "headline_groups": {n: {k: v for k, v in groups[n].items()} for n in HEADLINE_GROUPS
                            if n in groups},
        "strata": {s: {**strata[s], "groups": len(strata_groups[s])} for s in STRATUM_ORDER},
    }

    # --- N2: плотности -----------------------------------------------------
    ranked = sorted(((n, g["tokens"], g["simple"], per10k(g["simple"], g["tokens"]))
                     for n, g in groups.items()
                     if g["simple"] and g["tokens"] >= RANK_MIN_TOKENS),
                    key=lambda x: (-x[3], x[0]))
    n2 = {
        "per_tokens": PER,
        "rank_min_tokens": RANK_MIN_TOKENS,
        "rank_by_simple_per": [{"group": n, "tokens": t, "simple": s, "simple_per": d}
                               for n, t, s, d in ranked[:25]],
        "strata_density": {s: {"tokens": strata[s]["tokens"], "simple": strata[s]["simple"],
                               "simple_per": per10k(strata[s]["simple"], strata[s]["tokens"]),
                               "old_rakshas_lemma": strata[s]["old_rakshas_lemma"],
                               "old_per": per10k(strata[s]["old_rakshas_lemma"], strata[s]["tokens"])}
                           for s in STRATUM_ORDER},
    }

    # --- N3: «Махабхарата» по парвам ----------------------------------------
    n3 = {"by_parvan": {str(no): {"parvan": PARVAN_RU.get(no), **v}
                        for no, v in sorted(books["Mahābhārata"].items())},
          "totals": groups.get("Mahābhārata")}

    # --- N4: «Рамаяна» по кандам, DCS ↔ вульгата ----------------------------
    ram = {str(no): v for no, v in sorted(books["Rāmāyaṇa"].items())}
    try:
        vul = json.loads(VULGATE_JSON.read_text(encoding="utf-8"))
        vul_rows = {r["kanda"]: r for r in vul["census_by_kanda"]}
    except (OSError, KeyError, ValueError, TypeError) as exc:
        fail(f"JSON переписи вульгаты не прочитан ({VULGATE_JSON.name}: {exc})")
    comparison = []
    for no, name in KANDA_RU.items():
        d, v = ram.get(str(no)), vul_rows.get(name)
        if not d or not v:
            continue
        comparison.append({
            "kanda": no, "kanda_ru": name,
            "dcs_sargas": d["files"],
            "dcs_tokens": d["tokens"], "dcs_form_family": d["form_family"],
            "dcs_simple": d["simple"], "dcs_simple_fem": d["simple_fem"],
            "dcs_simple_per_10k": per10k(d["simple"], d["tokens"]),
            "vulgate_verses": v["verses"], "vulgate_form_family": v["rākṣasa-family"],
            "vulgate_rākṣasī": v["rākṣasī"],
            "delta_form_family_dcs_minus_vulgate": d["form_family"] - v["rākṣasa-family"],
            "delta_fem_dcs_minus_vulgate": d["simple_fem"] - v["rākṣasī"],
        })
    n4 = {"by_kanda": ram, "comparison": comparison,
          "totals": {"dcs": groups.get("Rāmāyaṇa"),
                     "vulgate": {k: vul["totals"][k] for k in ("verses", "family", "rakshasi", "neuter")}},
          "note": "Разные текстовые базы: DCS — критическое издание (66 сарг Сундары), "
                  "вульгата — южная рецензия (D2). Расхождение описывается, не сглаживается."}

    # --- Аудит внеэпических вхождений ---------------------------------------
    labels = load_audit(non_epic)
    by_label = {l: 0 for l in AUDIT_LABELS}
    by_label["unlabelled"] = 0
    stratum_label = {s: {} for s in STRATUM_ORDER if s != "epic"}
    pre_epic_being = []
    labelled_senses = {}
    for idx, (tid, st, group, locus, form, lemma, upos, cls, pc, _text) in enumerate(non_epic, 1):
        lab = labels.get(idx, "unlabelled")
        by_label[lab] += 1
        sl = stratum_label[st]
        sl[lab] = sl.get(lab, 0) + 1
        if lab != "unlabelled":
            labelled_senses[cls] = labelled_senses.get(cls, 0) + 1
        if st in ("archaic_vedic", "late_vedic_ritual") and lab == "being" and cls == "simple" and pc == "noun":
            pre_epic_being.append({"id": tid, "group": group, "locus": locus, "form": form})
    audited_noun_by_stratum = {}
    for s in STRATUM_ORDER:
        if s == "epic":
            continue
        c = stratum_label[s]
        audited_noun_by_stratum[s] = {l: c.get(l, 0) for l in
                                      ("being", "marriage", "rite", "quality", "label",
                                       "technical", "compound", "cross_morpheme", "unclear", "unlabelled")}
    audit = {
        "tokens_non_epic": len(non_epic),
        "labelled": len(non_epic) - by_label["unlabelled"],
        "unlabelled": by_label["unlabelled"],
        "labels": AUDIT_LABELS,
        "label_meanings": {
            "being": "существительное — класс существ (демоны), мифические ракшасы, списки существ, одержимость",
            "compound": "компаунд с rākṣasa-/rākṣasī- вне названия класса существ",
            "marriage": "вид брака (захват): brāhma · daiva · … · rākṣasa · paiśāca",
            "rite": "класс обрядов/заговоров (raudra · rākṣasa · nairṛta · ābhicaraṇīya)",
            "quality": "прилагательное «демонический» при другом существительном",
            "label": "ярлык для людей и человеческих типов (враги, темперамент, метафора)",
            "technical": "специальный технический смысл (алхимия, растения, лексикография)",
            "cross_morpheme": "ложное попадание: «rākṣas» на стыке морфем (sahasrākṣa- и т. п.)",
            "unclear": "контекст не позволяет решить",
        },
        "by_label": by_label,
        "by_stratum_label": stratum_label,
        "audited_tokens_by_class": labelled_senses,
        "non_epic_senses": audited_noun_by_stratum,
        "pre_epic_being_noun": pre_epic_being,
        "simple_by_stratum_pos": {
            s: {"noun": strata[s]["simple_noun"], "adj": strata[s]["simple_adj"],
                "fem": strata[s]["simple_fem"]}
            for s in STRATUM_ORDER},
    }

    report = {
        "script": Path(__file__).name,
        "unit": "H8579 — A74, ветка C: N1–N4 (леммы, плотности, МБх по парвам, вульгата ↔ DCS) + аудит",
        "corpus": {
            "clone_label": corpus_label,
            "pin": pin,
            "pin_rule": "клон обязан стоять на пине FORM-свипа; иначе ненулевой выход, числа не пишутся",
            "sweep_json": SWEEP_JSON.name,
            "groups_total": len(groups),
            "conllu_files_scanned": len(entries),
            "conllu_files_skipped_parsed": skipped_parsed,
            "tokens_total": tokens_total,
        },
        "crosscheck_sweep": {
            "family_tokens_this_run": tot["form_family"],
            "sweep_totals_rākṣasa_family": sweep_family,
            "equal": tot["form_family"] == sweep_family,
        },
        "method": {
            "token_line": "CoNLL-U: только строки-токены (ID — целое); *_parsed пропущены",
            "family": "FORM содержит «rākṣas» — бакет свипа, воспроизводится для сверки",
            "token_class": {
                "simple": "LEMMA ∈ {rākṣasa, rākṣasī}",
                "compound": "лемма содержит rākṣasa / rākṣasī как член (brahmarākṣasa, rākṣaseśvara, sa-rākṣasa …)",
                "cross_morpheme": "подстрока «rākṣas» на стыке морфем (sahasrākṣa-, dhūmrākṣa-, kuberākṣa- …)",
            },
            "pos_class": "fem = лемма rākṣasī; noun = UPOS NOUN; adj = UPOS ADJ; прочее — other_pos",
            "strata": STRATA,
            "audit_file": AUDIT_TSV.name,
        },
        "n1": n1, "n2": n2, "n3": n3, "n4": n4, "audit": audit,
        "groups": {n: {k: v for k, v in groups[n].items()} for n in sorted(groups)},
    }

    # newline="\n" явно: байт-идентичность не зависит от платформы (write_text
    # даёт CRLF на Windows); newline= у Path.write_text появился только в 3.13.
    with OUT.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(report, ensure_ascii=False, indent=1) + "\n")
    if dump_tokens:
        with TOKENS_TSV.open("w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh, delimiter="\t", lineterminator="\n")
            w.writerow(["id", "stratum", "group", "locus", "form", "lemma", "upos", "class", "pos", "text"])
            w.writerows(non_epic)
    summary = {k: report[k] for k in ("corpus", "crosscheck_sweep")}
    summary["n1_totals"] = n1["totals"]
    summary["epic_share"] = n1["epic_share"]
    summary["audit"] = {k: audit[k] for k in ("tokens_non_epic", "labelled", "unlabelled", "pre_epic_being_noun")}
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    print(f"\n[saved] {OUT}" + (f" + {TOKENS_TSV.name}" if dump_tokens else ""))


if __name__ == "__main__":
    main()
