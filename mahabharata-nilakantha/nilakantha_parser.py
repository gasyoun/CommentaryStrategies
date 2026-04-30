import os
import re
import json

def parse_nilakantha_commentary(file_path):
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
        if block in ["॥", "❧✿❧"] or "पर्व" in block and "अध्यायः" not in block:
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

def generate_markdown_scenarios(corpus, text_name, base_dir="Sanskrit_Vault"):
    # Создаем изолированные папки для конкретного текста
    text_dir = os.path.join(base_dir, text_name)
    atomic_dir = os.path.join(text_dir, "Atomic_Notes")
    longread_dir = os.path.join(text_dir, "Longreads")
    
    os.makedirs(atomic_dir, exist_ok=True)
    os.makedirs(longread_dir, exist_ok=True)

    def sanitize_filename(name):
        return re.sub(r'[\\/*?:"<>|]', "", name).strip()

    # СЦЕНАРИЙ 1: Атомарные заметки
    for item in corpus:
        chapter_safe = sanitize_filename(item['chapter'])
        # Добавляем префикс текста к файлу, чтобы имена были уникальны глобально
        filename = f"{text_name}_{chapter_safe}_{item['verse'].zfill(2)}.md"
        filepath = os.path.join(atomic_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("---\n")
            f.write("type: shloka\n")
            f.write(f"text: {text_name}\n") # Изоляция по метаданным
            f.write(f"chapter: \"{item['chapter']}\"\n")
            f.write(f"verse: {item['verse']}\n")
            f.write("tags: [raw_import]\n")
            f.write("---\n\n")
            
            f.write("### Mūla\n")
            f.write(f"{item['mula']}\n\n")
            
            if item['tika']:
                f.write("### Ṭīkā (Nīlakaṇṭha)\n")
                f.write(f"> {item['tika']}\n\n")
            
            f.write("---\n**Ссылки:**\n")
            f.write(f"[[{text_name}_{chapter_safe}_Full|Перейти к полному тексту главы]]\n")

    # СЦЕНАРИЙ 2: Лонгриды
    chapters_data = {}
    for item in corpus:
        ch = item['chapter']
        if ch not in chapters_data:
            chapters_data[ch] = []
        chapters_data[ch].append(item)
        
    for chapter_name, shlokas in chapters_data.items():
        chapter_safe = sanitize_filename(chapter_name)
        filepath = os.path.join(longread_dir, f"{text_name}_{chapter_safe}_Full.md")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {chapter_name} ({text_name})\n\n")
            for s in shlokas:
                f.write(f"<a id=\"verse-{s['verse']}\"></a>\n")
                f.write(f"**॥ {s['verse']} ॥**\n\n")
                f.write(f"{s['mula']}\n\n")
                if s['tika']:
                    f.write(f"> *{s['tika']}*\n\n")
                f.write("---\n\n")

    print(f"Успешно обработан текст: {text_name}. Заметок: {len(corpus)}.")

# ==========================================
# БЛОК ЗАПУСКА (УПРАВЛЕНИЕ ТЕКСТАМИ)
# ==========================================

if __name__ == "__main__":
    # 1. Обрабатываем Рамопакхьяну
    if os.path.exists('MBh-Ramopakhyanam-Nilakantha.md'):
        corpus_ram = parse_nilakantha_commentary('MBh-Ramopakhyanam-Nilakantha.md')
        generate_markdown_scenarios(corpus_ram, text_name="Ramopakhyanam")

    # 2. Обрабатываем Налопакхьяну (когда файл будет готов)
    if os.path.exists('MBh-Nalopakhyanam-Nilakantha.md'):
        corpus_nal = parse_nilakantha_commentary('MBh-Nalopakhyanam-Nilakantha.md')
        generate_markdown_scenarios(corpus_nal, text_name="Nalopakhyanam")