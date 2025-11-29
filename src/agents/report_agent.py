from ..utils.pdf_utils import extract_text_from_pdf

def parse_report(path):
    txt = extract_text_from_pdf(path)
    # placeholder parsing - later replace with real extraction
    return {"raw_text": txt}