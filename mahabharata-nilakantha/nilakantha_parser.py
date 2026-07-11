import os
import re
import sys
import json
import time
import argparse
import html as _html
import urllib.request
import urllib.error
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

# ==========================================
# 1. ТРАНСЛИТЕРАТОР (Devanagari -> IAST)
# ==========================================
def devanagari_to_iast(text):
    """Транслитерирует текст в академический IAST."""
    if not text:
        return ""
    # Прямая транслитерация
    iast_text = transliterate(text, sanscript.DEVANAGARI, sanscript.IAST)
    return iast_text

# ==========================================
# 2. ПАРСЕР ТЕКСТА
# ==========================================
def parse_nilakantha_commentary(file_path):
    """Разбивает сплошной текст на структурированный массив (Шлока + Комментарий)."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = [b.strip() for b in content.split('\n\n') if b.strip()]
    parsed_corpus = []
    current_chapter = "Unknown Chapter"
    current_verse_num = None
    current_shloka_data = None
    
    verse_pattern = re.compile(r'॥([०-९]+)॥$')
    colophon_pattern = re.compile(r'^इति श्रीमहाभारते')
    chapter_pattern = re.compile(r'अध्यायः$')

    for block in blocks:
        if block in ["॥", "❧✿❧"] or ("पर्व" in block and "अध्यायः" not in block):
            continue
            
        if colophon_pattern.match(block):
            current_verse_num = None
            continue
            
        if chapter_pattern.search(block) and not verse_pattern.search(block):
            current_chapter = block
            current_verse_num = None
            continue
            
        match = verse_pattern.search(block)
        if match:
            verse_num = match.group(1)
            if verse_num != current_verse_num:
                current_verse_num = verse_num
                current_shloka_data = {
                    "chapter": current_chapter,
                    "verse": verse_num,
                    "mula": block,
                    "tika": None
                }
                parsed_corpus.append(current_shloka_data)
            else:
                if current_shloka_data:
                    current_shloka_data["tika"] = block

    return parsed_corpus

# ==========================================
# 3. АНАЛИЗАТОР СЛОЖНОСТИ (Teacher Dashboard)
# ==========================================
def evaluate_difficulty_and_topics(tika_text):
    """Эвристический анализатор для тегирования шлок в LMS."""
    if not tika_text:
        return "low", []
    
    topics = []
    difficulty = "medium"
    
    if "आर्ष" in tika_text or "छान्दसं" in tika_text:
        topics.append("ārṣa-prayoga")
        difficulty = "high"
    if "समास" in tika_text:
        topics.append("samāsa-vigraha")
    if "पाठे" in tika_text or "पाठान्तरम्" in tika_text:
        topics.append("pāṭhāntara")
        difficulty = "high"
    if "मेदिनी" in tika_text or "यास्कः" in tika_text or "निघण्टु" in tika_text:
        topics.append("kośa-nirukta")
        
    return difficulty, topics

# ==========================================
# 4. ЭКСТРАКТОР СЛОЖНЫХ СЛОВ (Samāsa)
# ==========================================
def extract_and_build_samasas(corpus, text_name, base_dir="Sanskrit_Vault"):
    """Ищет виграхи Нилакантхи и создает словарь композитов."""
    samasa_dir = os.path.join(base_dir, text_name, "Samasa_Dictionary")
    os.makedirs(samasa_dir, exist_ok=True)
    
    vigraha_patterns = [
        re.compile(r'([^\s]+)\s+.*?(यस्य|यस्याः|येषाम्|ययोः)\s+(सः|सा|तत्|तानि|इति)\b'),
        re.compile(r'([^\s]+)\s+.*?(इति समासः)'),
        re.compile(r'([^\s]+)\s+.*?(इत्यर्थः)')
    ]
    
    extracted_count = 0
    for item in corpus:
        tika = item.get('tika', '')
        if not tika: continue
            
        for pattern in vigraha_patterns:
            match = pattern.search(tika)
            if match:
                pratika = re.sub(r'[।॥0-9]', '', match.group(1)).strip()
                if len(pratika) < 3: continue
                    
                safe_name = re.sub(r'[\\/*?:"<>|]', "", pratika)
                filepath = os.path.join(samasa_dir, f"{safe_name}.md")
                
                if os.path.exists(filepath):
                    filepath = os.path.join(samasa_dir, f"{safe_name}_{item['verse']}.md")
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write("---\n")
                    f.write("type: samasa\n")
                    f.write(f"text_source: {text_name}\n")
                    f.write(f"chapter: \"{item['chapter']}\"\n")
                    f.write(f"verse: {item['verse']}\n")
                    f.write("---\n\n")
                    f.write(f"# {pratika}\n\n")
                    f.write(f"**Виграха Нилакантхи:**\n> {tika}\n\n")
                    f.write("---\n")
                    
                    chapter_safe = re.sub(r'[\\/*?:"<>|]', "", item['chapter']).strip()
                    f.write(f"**Контекст:** [[{text_name}_{chapter_safe}_{item['verse'].zfill(2)}|Перейти к шлоке]]\n")
                
                extracted_count += 1
                break
                
    print(f"[{text_name}] Словарь Самас сгенерирован: {extracted_count} статей.")

# ==========================================
# 5. ГЕНЕРАТОР БАЗЫ ЗНАНИЙ (MDX + Docusaurus)
# ==========================================
def generate_lms_markdown(corpus, text_name, base_dir="Sanskrit_Vault"):
    """Создает атомарные заметки и лонгриды для LMS/Obsidian."""
    text_dir = os.path.join(base_dir, text_name)
    atomic_dir = os.path.join(text_dir, "Atomic_Notes")
    longread_dir = os.path.join(text_dir, "Longreads")
    
    os.makedirs(atomic_dir, exist_ok=True)
    os.makedirs(longread_dir, exist_ok=True)

    def sanitize_filename(name):
        return re.sub(r'[\\/*?:"<>|]', "", name).strip()

    chapters_data = {}

    # СЦЕНАРИЙ 1: Атомарные заметки (Zettelkasten / LMS Cards)
    for item in corpus:
        ch = item['chapter']
        if ch not in chapters_data:
            chapters_data[ch] = []
        chapters_data[ch].append(item)
        
        chapter_safe = sanitize_filename(ch)
        filename = f"{text_name}_{chapter_safe}_{item['verse'].zfill(2)}.md"
        filepath = os.path.join(atomic_dir, filename)
        
        mula_iast = devanagari_to_iast(item['mula'])
        tika_iast = devanagari_to_iast(item['tika']) if item['tika'] else ""
        
        difficulty, topics = evaluate_difficulty_and_topics(item['tika'])
        topics_str = ", ".join([f'"{t}"' for t in topics])
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("---\n")
            f.write("type: shloka\n")
            f.write(f"text: {text_name}\n")
            f.write(f"chapter: \"{item['chapter']}\"\n")
            f.write(f"verse: {item['verse']}\n")
            f.write(f"difficulty: {difficulty}\n")
            if topics:
                f.write(f"topics: [{topics_str}]\n")
            f.write("tags: [lms_ready]\n")
            f.write("---\n\n")
            
            # MDX Разметка для Docusaurus
            f.write(f'<a id="verse-{item["verse"]}" class="shloka-anchor"></a>\n')
            f.write(f'<div class="verse-number">॥ {item["verse"]} ॥</div>\n\n')
            
            f.write("### Mūla (IAST)\n")
            f.write(f'<div class="mula-iast">\n{mula_iast}\n</div>\n\n')
            
            f.write("### Mūla (Devanagari)\n")
            f.write(f"```devanagari\n{item['mula']}\n```\n\n")
            
            if item['tika']:
                f.write("### Ṭīkā (Nīlakaṇṭha)\n")
                f.write('<div class="tika-block">\n')
                f.write(f'  <p>{tika_iast}</p>\n')
                f.write(f'  <p class="tika-devanagari">{item["tika"]}</p>\n')
                f.write('</div>\n\n')
            
            f.write("---\n")
            f.write("### Morphological Links (Zaliznyakiada)\n")
            f.write("- Roots: [[Whitney-linked-2026]]\n")
            f.write("- Samāsa: \n\n")
            f.write("---\n**Navigation:**\n")
            f.write(f"[[{text_name}_{chapter_safe}_Full|Full Chapter]]\n")

    # СЦЕНАРИЙ 2: Лонгриды (Сплошное чтение Docusaurus/HTML)
    for chapter_name, shlokas in chapters_data.items():
        chapter_safe = sanitize_filename(chapter_name)
        filepath = os.path.join(longread_dir, f"{text_name}_{chapter_safe}_Full.md")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {chapter_name} ({text_name})\n\n")
            
            for s in shlokas:
                mula_iast = devanagari_to_iast(s['mula'])
                
                f.write(f'<a id="verse-{s["verse"]}" class="shloka-anchor"></a>\n')
                f.write(f'<div class="verse-number">॥ {s["verse"]} ॥</div>\n\n')
                f.write(f'<div class="mula-iast">\n{mula_iast}\n</div>\n\n')
                f.write(f"```devanagari\n{s['mula']}\n```\n\n")
                
                if s['tika']:
                    tika_iast = devanagari_to_iast(s['tika'])
                    f.write('<div class="tika-block">\n')
                    f.write(f'  <p>{tika_iast}</p>\n')
                    f.write(f'  <p class="tika-devanagari">{s["tika"]}</p>\n')
                    f.write('</div>\n\n')
                
                f.write("---\n\n")

    print(f"[{text_name}] База знаний сгенерирована: {len(corpus)} шлок, {len(chapters_data)} лонгридов.")

# ==========================================
# 6. СКРЕЙПЕР ПОЛНОГО КОРПУСА НИЛАКАНТХИ (sanatana.in)
# ==========================================
# Источник: https://sanatana.in/mahabharata/ (проект Sanatana Sampatti /
# srirangadigital.com). Весь текст-мула вульгаты (Nīlakaṇṭha-recension) вместе с
# ṭīkā «Bhāratabhāvadīpa» отдаётся постранично AJAX-эндпоинтом
#   GET /mahabharata/listing/getParvaByPage/{parva}?page={N}
# Каждая шлока — <div class="shloka" id="P{pp}_U{uu}_A{aaa}_S{sss}"> с одним
# <p class="shloka_text"> (мула) и 0+ <p class="bhavadeepa"> (глоссы Нилакантхи).
# Адресация P/U/A/S берётся прямо из id — машиночитаемая нумерация вульгаты.

BASE = "https://sanatana.in/mahabharata"
PAGE_URL = BASE + "/listing/getParvaByPage/{parva}?page={page}"

# 18 парванов Махабхараты (+ harivamsha — отдельный придаток, по умолчанию НЕ входит).
PARVAS = [
    "adiparva", "sabhaparva", "vanaparva", "virataparva", "udyogaparva",
    "bhishmaparva", "dronaparva", "karnaparva", "shalyaparva", "sauptikaparva",
    "striparva", "shantiparva", "anushasanaparva", "ashwamedhikaparva",
    "ashramavasikaparva", "mausalaparva", "mahaprasthanikaparva", "swargarohanaparva",
]
HARIVAMSHA = "harivamsha"

_SHLOKA_START = re.compile(
    r'<div class="shloka[^"]*"\s+id="(P\d+_U\d+_A\d+_S\d+)"\s*>')
_SHLOKA_TEXT = re.compile(
    r'<p class="shloka_text[^"]*"[^>]*>(.*?)</p>', re.S)
_BHAVADEEPA = re.compile(
    r'<p class="bhavadeepa"[^>]*>(.*?)</p>', re.S)
_TAG = re.compile(r'<[^>]+>')
_WS = re.compile(r'[ \t ]+')


def _clean_html(fragment):
    """HTML-фрагмент -> чистый Devanagari-текст (снять теги, <br>->\\n, unescape)."""
    if not fragment:
        return ""
    t = re.sub(r'<br\s*/?>', '\n', fragment, flags=re.I)
    t = _TAG.sub('', t)          # убрать <span class="uvacha"> и прочие теги, сохранив текст
    t = _html.unescape(t)
    t = _WS.sub(' ', t)
    t = re.sub(r'\s*\n\s*', '\n', t)
    return t.strip()


def fetch_parva_page(parva, page, cache_dir, delay=1.0, timeout=60):
    """Скачать одну страницу парвана (с дисковым кэшем; пустая страница -> '')."""
    os.makedirs(cache_dir, exist_ok=True)
    cache_fp = os.path.join(cache_dir, f"{parva}_p{page:03d}.html")
    if os.path.exists(cache_fp):
        with open(cache_fp, encoding="utf-8") as f:
            return f.read()
    url = PAGE_URL.format(parva=parva, page=page)
    req = urllib.request.Request(url, headers={"User-Agent": "csl-research/1.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                body = r.read().decode("utf-8", "replace")
            with open(cache_fp, "w", encoding="utf-8") as f:
                f.write(body)
            time.sleep(delay)     # вежливость к серверу
            return body
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt == 2:
                raise
            time.sleep(2 * (attempt + 1))
    return ""


def parse_page(html_body):
    """Одна страница -> список шлок [{parva_no,upaparva,adhyaya,shloka,mula,tikas}]."""
    out = []
    starts = [(m.start(), m.group(1)) for m in _SHLOKA_START.finditer(html_body)]
    for i, (pos, sid) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(html_body)
        chunk = html_body[pos:end]
        mt = _SHLOKA_TEXT.search(chunk)
        mula = _clean_html(mt.group(1)) if mt else ""
        tikas = [_clean_html(x) for x in _BHAVADEEPA.findall(chunk)]
        tikas = [t for t in tikas if t]
        pp, uu, aaa, sss = re.match(
            r'P(\d+)_U(\d+)_A(\d+)_S(\d+)', sid).groups()
        out.append({
            "id": sid,
            "parva_no": int(pp), "upaparva": int(uu),
            "adhyaya": int(aaa), "shloka": int(sss),
            "mula": mula, "tikas": tikas,
        })
    return out


def scrape_parva(parva, cache_dir, delay=1.0, max_pages=1000):
    """Итерировать страницы парвана до пустой; вернуть дедуплицированные шлоки."""
    seen = {}
    page = 1
    while page <= max_pages:
        body = fetch_parva_page(parva, page, cache_dir, delay=delay)
        rows = parse_page(body) if body and len(body) > 8 else []
        if not rows:
            break
        for r in rows:
            seen[r["id"]] = r            # дедуп по уникальному P/U/A/S id
        print(f"  {parva} page {page:3d}: +{len(rows):4d} shlokas (total {len(seen)})")
        page += 1
    return list(seen.values())


def scrape_all(parvas, out_jsonl, cache_dir, delay=1.0, with_iast=True):
    """Полный скрейп + разбор -> JSONL (мула + ṭīkā, Devanagari [+ IAST])."""
    total = tika_total = 0
    with open(out_jsonl, "w", encoding="utf-8") as out:
        for parva in parvas:
            print(f"[{parva}] scraping ...")
            rows = scrape_parva(parva, cache_dir, delay=delay)
            rows.sort(key=lambda r: (r["upaparva"], r["adhyaya"], r["shloka"]))
            nt = sum(1 for r in rows if r["tikas"])
            total += len(rows); tika_total += nt
            for r in rows:
                rec = {
                    "parva": parva,
                    "parva_no": r["parva_no"], "upaparva": r["upaparva"],
                    "adhyaya": r["adhyaya"], "shloka": r["shloka"],
                    "id": r["id"],
                    "mula_dev": r["mula"],
                    "tika_dev": r["tikas"],
                }
                if with_iast:
                    rec["mula_iast"] = devanagari_to_iast(r["mula"])
                    rec["tika_iast"] = [devanagari_to_iast(t) for t in r["tikas"]]
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")
            print(f"[{parva}] {len(rows)} shlokas, {nt} with ṭīkā "
                  f"({100*nt/len(rows):.1f}%)" if rows else f"[{parva}] EMPTY")
    print(f"\nTOTAL {total} shlokas, {tika_total} with ṭīkā "
          f"({100*tika_total/total:.1f}%) -> {out_jsonl}")


# ==========================================
# 7. ГЛАВНЫЙ ЦИКЛ ЗАПУСКА
# ==========================================
def _run_lms():
    """Старый режим: локальные .md эпизоды -> Sanskrit_Vault (LMS/Zettelkasten)."""
    target_file = 'MBh-Nalopakhyanam-Nilakantha.md'
    text_name = "Nalopakhyanam"
    if os.path.exists(target_file):
        print(f"Начат процесс обработки файла: {target_file}...")
        corpus = parse_nilakantha_commentary(target_file)
        extract_and_build_samasas(corpus, text_name=text_name)
        generate_lms_markdown(corpus, text_name=text_name)
        print("\n✅ Выполнение успешно завершено. Проверьте папку 'Sanskrit_Vault'.")
    else:
        print(f"❌ Ошибка: Файл {target_file} не найден в текущей директории.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description="Nīlakaṇṭha-vulgate Mahābhārata: полный скрейп с sanatana.in "
                    "или старая LMS-генерация из локальных .md.")
    sub = ap.add_subparsers(dest="cmd")

    sp = sub.add_parser("scrape", help="Скачать ВЕСЬ корпус Нилакантхи -> JSONL")
    sp.add_argument("--out", default="nilakantha_vulgate_full.jsonl")
    sp.add_argument("--cache-dir", default="_cache")
    sp.add_argument("--delay", type=float, default=1.0, help="пауза между запросами, сек")
    sp.add_argument("--parvas", nargs="*", default=None,
                    help="подмножество слугов парванов (по умолчанию все 18)")
    sp.add_argument("--harivamsha", action="store_true", help="включить харивамшу")
    sp.add_argument("--no-iast", action="store_true", help="не считать IAST")

    sub.add_parser("lms", help="Старый режим: локальные .md -> Sanskrit_Vault")

    args = ap.parse_args()
    if args.cmd == "scrape":
        parvas = args.parvas if args.parvas else list(PARVAS)
        if args.harivamsha:
            parvas.append(HARIVAMSHA)
        scrape_all(parvas, args.out, args.cache_dir,
                   delay=args.delay, with_iast=not args.no_iast)
    else:
        _run_lms()