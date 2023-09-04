import fitz

path = "pdf.pdf"

# extract text
doc = fitz.open(path)
for page in doc:
    text = page.get_text()
    print(text)