import os
import subprocess
from docx import Document
from docx.shared import Cm

def build_article():
    input_md = "10_article_v_tronsky_v6.md"
    temp_md = "temp_article.md"
    output_docx = "article_v_tronsky.docx"
    reference_docx = "tronsky_reference.docx"
    
    # Жестко заданный путь к вашему Pandoc
    pandoc_exe = r"C:\Users\user\Downloads\pandoc-3.9.0.2-windows-x86_64\pandoc-3.9.0.2\pandoc.exe"

    print("1. Чтение и предобработка Markdown...")
    with open(input_md, "r", encoding="utf-8") as f:
        text = f.read()

    # Корректировка атрибуции источника на 2005 год перед компиляцией
    text = text.replace("Tubb, Boose 2007", "Tubb, Boose 2005")
    text = text.replace("Tubb, G. A., Boose, E. R. 2007", "Tubb, G. A., Boose, E. R. 2005")

    with open(temp_md, "w", encoding="utf-8") as f:
        f.write(text)

    print("2. Конвертация через Pandoc...")
    pandoc_cmd = [
        pandoc_exe,
        temp_md,
        "-o", output_docx,
        f"--reference-doc={reference_docx}",
        "-f", "markdown",
        "-t", "docx"
    ]

    try:
        subprocess.run(pandoc_cmd, check=True)
        print("   Pandoc успешно сформировал DOCX.")
    except subprocess.CalledProcessError as e:
        print(f"   Ошибка при запуске Pandoc: {e}")
        return
    except FileNotFoundError:
        print(f"   Ошибка: Pandoc не найден по пути {pandoc_exe}")
        return

    print("3. Постобработка: настройка ширины таблиц (макс. 11 см)...")
    try:
        doc = Document(output_docx)
        max_width = Cm(11.0)
        tables_modified = 0

        for table in doc.tables:
            table.autofit = False
            
            if len(table.columns) > 0:
                col_width = max_width / len(table.columns)
                for row in table.rows:
                    for cell in row.cells:
                        cell.width = col_width
                tables_modified += 1

        if tables_modified > 0:
            doc.save(output_docx)
            print(f"   Скорректировано таблиц: {tables_modified}.")
        else:
            print("   Таблицы в документе не найдены, постобработка не требуется.")
            
    except Exception as e:
        print(f"   Ошибка при обработке через python-docx: {e}")

    if os.path.exists(temp_md):
        os.remove(temp_md)

    print(f"\nГотово! Итоговый файл сохранен как: {output_docx}")

if __name__ == "__main__":
    build_article()