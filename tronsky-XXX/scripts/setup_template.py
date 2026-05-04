from docx import Document
from docx.shared import Pt, Cm

def configure_template():
    input_file = "custom-reference.docx"
    output_file = "tronsky_reference.docx"
    
    print(f"Открываем базовый шаблон Pandoc: {input_file}...")
    try:
        doc = Document(input_file)
    except Exception as e:
        print(f"Ошибка при открытии {input_file}. Убедитесь, что вы выполнили команду генерации шаблона.")
        return

    print("Настраиваем стили под требования журнала...")
    
    # 1. Настройка основного текста (Normal)
    # Кегль 11, абзацный отступ 0,6 см
    if 'Normal' in doc.styles:
        normal_style = doc.styles['Normal']
        normal_style.font.size = Pt(11)
        normal_style.paragraph_format.first_line_indent = Cm(0.6)
        print(" - Стиль 'Normal' (Основной текст): установлен шрифт 11 пт и отступ 0.6 см.")

    # 2. Настройка сносок (Footnote Text)
    # Кегль 10
    if 'Footnote Text' in doc.styles:
        footnote_style = doc.styles['Footnote Text']
        footnote_style.font.size = Pt(10)
        print(" - Стиль 'Footnote Text' (Текст сноски): установлен шрифт 10 пт.")

    # 3. Настройка библиографии (Bibliography)
    # Кегль 10
    if 'Bibliography' in doc.styles:
        bib_style = doc.styles['Bibliography']
        bib_style.font.size = Pt(10)
        print(" - Стиль 'Bibliography' (Библиография): установлен шрифт 10 пт.")

    # Сохраняем готовый шаблон
    doc.save(output_file)
    print(f"\nГотово! Настроенный шаблон сохранен как: {output_file}")
    print("Теперь вы можете запускать основной скрипт сборки статьи: python build_docx.py")

if __name__ == "__main__":
    configure_template()