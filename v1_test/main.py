import pdfplumber
import os
import re

folder_path = r"C:\Users\Admin\PdfDoc"  # change to file location

pattern = re.compile(r"Total Investment \(RM\)\s*:\s*([\d,.,]+)") # checks for the line TOTAL INVESTMENT

def get_total_investment_from_pdf(pdf_path):
    """Return the numeric string after 'Total Investment (RM):', or None if not found."""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            match = pattern.search(text)
            if match:
                return match.group(1)  # e.g. "31,000.00"
    return None

for filename in os.listdir(folder_path):
    if not filename.lower().endswith(".pdf"):
        continue  # skip non-PDF files

    pdf_path = os.path.join(folder_path, filename)
    value = get_total_investment_from_pdf(pdf_path)

    if value is not None:
        print(f"{filename} -> Total Investment (RM): {value}")
    else:
        print(f"{filename} -> Could not find 'Total Investment (RM)'")