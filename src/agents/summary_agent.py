"""
Summary Agent:
Creates a short summary from raw extracted text.
"""

def generate_summary(report_data):
    text = report_data.get("raw_text", "").strip()

    if not text:
        return {"summary": "No information found in the report."}

    # Simple summary logic (demo)
    sentences = text.split(".")
    first_sentence = sentences[0].strip()

    summary = f"Summary: {first_sentence}."

    return {"summary": summary}