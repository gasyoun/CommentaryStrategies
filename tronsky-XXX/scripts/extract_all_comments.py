import zipfile
from lxml import etree

def extract_all_comments(docx_path, output_path):
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
          'w16ce': 'http://schemas.microsoft.com/office/word/2018/wordml/cex'}
    
    print(f"Extracting all possible comment sources from {docx_path}...")
    
    with open(output_path, "w", encoding="utf-8") as out:
        out.write(f"Comments from {docx_path}\n\n")
        
        with zipfile.ZipFile(docx_path, 'r') as z:
            # 1. Standard comments.xml
            try:
                if 'word/comments.xml' in z.namelist():
                    content = z.read('word/comments.xml')
                    root = etree.fromstring(content)
                    comments = root.xpath('//w:comment', namespaces=ns)
                    out.write(f"[word/comments.xml] Found {len(comments)} comments:\n")
                    for c in comments:
                        author = c.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}author')
                        text = "".join([t.text for t in c.xpath('.//w:t', namespaces=ns) if t.text])
                        out.write(f"- [{author}]: {text}\n")
            except Exception as e:
                out.write(f"Error reading word/comments.xml: {e}\n")

            # 2. word/commentsExtensible.xml
            try:
                if 'word/commentsExtensible.xml' in z.namelist():
                    content = z.read('word/commentsExtensible.xml')
                    root = etree.fromstring(content)
                    comments = root.xpath('//w16ce:comment', namespaces=ns)
                    out.write(f"\n[word/commentsExtensible.xml] Found {len(comments)} extensible comments:\n")
                    for c in comments:
                        text_nodes = c.xpath('.//w16ce:text/w:p/w:r/w:t', namespaces=ns)
                        text = "".join([t.text for t in text_nodes if t.text])
                        if not text:
                             text_nodes = c.xpath('.//w:t', namespaces=ns)
                             text = "".join([t.text for t in text_nodes if t.text])
                        out.write(f"- {text}\n")
            except Exception as e:
                out.write(f"Error reading word/commentsExtensible.xml: {e}\n")

if __name__ == "__main__":
    path = r"c:\Users\user\Documents\GitHub\CommentaryStrategies\tronsky-XXX\CommentaryStrategies_Tronsky30_Kostina.docx"
    extract_all_comments(path, "kostina_comments.txt")
