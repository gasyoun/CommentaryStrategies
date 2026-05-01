import os
import re
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

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
# 6. ГЛАВНЫЙ ЦИКЛ ЗАПУСКА
# ==========================================
if __name__ == "__main__":
    target_file = 'MBh-Nalopakhyanam-Nilakantha.md'
    text_name = "Nalopakhyanam"
    
    if os.path.exists(target_file):
        print(f"Начат процесс обработки файла: {target_file}...")
        
        # 1. Парсинг
        corpus = parse_nilakantha_commentary(target_file)
        
        # 2. Извлечение Самас
        extract_and_build_samasas(corpus, text_name=text_name)
        
        # 3. Генерация Базы Знаний
        generate_lms_markdown(corpus, text_name=text_name)
        
        print("\n✅ Выполнение успешно завершено. Проверьте папку 'Sanskrit_Vault'.")
    else:
        print(f"❌ Ошибка: Файл {target_file} не найден в текущей директории.")