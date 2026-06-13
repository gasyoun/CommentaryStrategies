#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Деривация канонических CTS-URN из shloka_addr (шаг B2 дорожной карты).

Каждому примечанию присваивается канонический идентификатор стиха в формате
CTS (Canonical Text Services, как в Perseus/SARIT):

    urn:cts:sanskritLit:<work>:<passage>

где work — ramayana / mahabharata / <упанишада>, а passage — точечная нумерация
(kāṇḍa.sarga.verse | parva.adhyāya.verse | a.b.c). Поскольку у Рам./Мбх. первый
элемент точечной нумерации совпадает с номером книги/парвы, имя книги в адресе
служит перекрёстной проверкой целостности.

Запуск:
    python scripts/derive_urn.py --check   # только проверка, без записи
    python scripts/derive_urn.py            # внедрить поле "urn" в data/*_markup_50.json

Замечание о схеме CTS: используется один work на эпос (ramayana / mahabharata),
книга кодируется первым элементом passage. Это отличается от чернового примера
в ROADMAP (ramayana.sundara:5.1.1), который дублировал бы книгу (sundara И 5);
здесь — urn:cts:sanskritLit:ramayana:5.1.1.
"""

import json
import re
import sys
import pathlib

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

DATA = pathlib.Path(__file__).resolve().parent.parent / "data"
NS = "urn:cts:sanskritLit"

# Рамаяна: кāṇḍa → номер
RAM_KANDA = {
    "Bāla": 1, "Ayodhyā": 2, "Araṇya": 3, "Kiṣkindhā": 4,
    "Sundara": 5, "Yuddha": 6, "Uttara": 7,
}

# Махабхарата: parva (и upaparva-псевдонимы) → номер parva
MBH_PARVA = {
    "Ādi": 1, "Sabhā": 2, "Vana": 3, "Virāṭa": 4, "Udyoga": 5,
    "Bhīṣma": 6, "Gītā": 6, "Droṇa": 7, "Karṇa": 8, "Śalya": 9,
    "Sauptika": 10, "Strī": 11, "Śānti": 12, "Mokṣa": 12,
    "Anuśāsana": 13, "Aśvamedhika": 14, "Āśramavāsika": 15,
    "Mausala": 16, "Mahāprasthānika": 17, "Svargārohaṇa": 18,
}

# Упанишады: сокращение перед "Up." → CTS work id
UPANISHAD = {
    "Aitareya": "aitareya", "Bṛh.": "brhadaranyaka", "Chānd.": "chandogya",
    "Kaivalya": "kaivalya", "Kauṣ.": "kausitaki", "Kaṭha": "katha",
    "Kena": "kena", "Maitrī": "maitri", "Muṇḍ.": "mundaka",
    "Māṇḍ.": "mandukya", "Praśna": "prasna", "Taitt.": "taittiriya",
    "Īśā": "isa", "Śvet.": "svetasvatara",
}


def derive(addr):
    """shloka_addr → (urn, ok, note). ok=False если перекрёстная проверка не прошла."""
    addr = addr.strip()

    m = re.match(r"^(Rām|MBh)\.\s+(\S+)\s+([\d.]+)$", addr)
    if m:
        epic, name, passage = m.groups()
        if epic == "Rām":
            work, table = "ramayana", RAM_KANDA
        else:
            work, table = "mahabharata", MBH_PARVA
        if name not in table:
            return f"{NS}:{work}:{passage}", False, f"неизвестная книга/парва «{name}»"
        booknum = table[name]
        parts = passage.split(".")
        # Канонический passage = <книга>.<sarga/adhyāya>.<стих>. Если адрес даёт
        # полную форму (≥3 уровня), первый элемент = номер книги — проверяем.
        # Если даёт укороченную форму (2 уровня, как у Кальянова: adhyāya.verse),
        # номер книги в цифрах отсутствует — добавляем его слева.
        if len(parts) >= 3:
            lead = int(parts[0])
            urn = f"{NS}:{work}:{passage}"
            if lead != booknum:
                return urn, False, f"«{name}»={booknum} ≠ ведущий номер {lead}"
            return urn, True, ""
        # 1–2 уровня: префиксуем номер книги
        return f"{NS}:{work}:{booknum}.{passage}", True, ""

    m = re.match(r"^(\S+)\s+Up\.\s+([\d.]+)$", addr)
    if m:
        abbr, passage = m.groups()
        work = UPANISHAD.get(abbr)
        if not work:
            return f"{NS}:upanishad-unknown:{passage}", False, f"неизвестная упанишада «{abbr}»"
        return f"{NS}:{work}:{passage}", True, ""

    return None, False, f"неразобранный адрес «{addr}»"


def reorder(rec, urn):
    """Вставить urn сразу после comment_id, сохранив порядок остальных ключей."""
    out = {}
    for k, v in rec.items():
        out[k] = v
        if k == "comment_id":
            out["urn"] = urn
    if "urn" not in out:  # на случай отсутствия comment_id
        out = {"urn": urn, **out}
    return out


def dump_compact(records):
    """Один объект на строку — компактный, удобный для diff формат корпуса."""
    lines = ["["]
    for i, rec in enumerate(records):
        comma = "," if i < len(records) - 1 else ""
        lines.append("  " + json.dumps(rec, ensure_ascii=False) + comma)
    lines.append("]")
    return "\n".join(lines) + "\n"


def main():
    check = "--check" in sys.argv
    files = sorted(DATA.glob("*_markup_50.json"))
    total, bad = 0, []
    for path in files:
        records = json.loads(path.read_text(encoding="utf-8"))
        new_records = []
        for rec in records:
            urn, ok, note = derive(rec["shloka_addr"])
            total += 1
            if not ok:
                bad.append((rec.get("comment_id", "?"), rec["shloka_addr"], note))
            new_records.append(reorder(rec, urn))
        if not check:
            path.write_text(dump_compact(new_records), encoding="utf-8")
        sample = derive(records[0]["shloka_addr"])[0]
        print(f"{'(check) ' if check else 'wrote  '}{path.name:28s} "
              f"{len(records):3d} rec  напр.: {sample}")

    print(f"\nВсего: {total} примечаний.")
    if bad:
        print(f"⚠ Проблемы перекрёстной проверки ({len(bad)}):")
        for cid, addr, note in bad:
            print(f"  {cid}: {addr} — {note}")
    else:
        print("✓ Все адреса разобраны, перекрёстная проверка книга↔номер пройдена.")


if __name__ == "__main__":
    main()
