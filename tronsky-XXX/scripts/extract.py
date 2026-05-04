import os
import fitz  # PyMuPDF

def extract_text_from_pdfs(folder_path):
    if not os.path.exists(folder_path):
        print(f"Ошибка: Папка '{folder_path}' не найдена!")
        return

    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    print(f"Найдено PDF файлов в папке {folder_path}: {len(pdf_files)}\n")

    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        txt_path = os.path.join(folder_path, f"{os.path.splitext(pdf_file)[0]}.txt")
        
        try:
            doc = fitz.open(pdf_path)
            text = ""
            for page in doc:
                text += page.get_text() + "\n"
            
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(text)
                
            print(f"✅ Готово: {pdf_file}")
            
        except Exception as e:
            print(f"❌ Ошибка с файлом {pdf_file}: {e}")

if __name__ == "__main__":
    # Скрипт будет искать файлы в вашей подпапке PDFtoTXT
    extract_text_from_pdfs("PDFtoTXT")