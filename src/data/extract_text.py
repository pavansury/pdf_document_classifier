import pdfplumber
import sys

def extract_text(path):
    with pdfplumber.open(path) as pdf:
        return " ".join([page.extract_text() or "" for page in pdf.pages])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_text.py <pdf_path>")
    else:
        text = extract_text(sys.argv[1])
        print(text[:500])  # print first 500 chars
