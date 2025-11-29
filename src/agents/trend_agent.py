"""
Trend Agent:
Extracts basic trends from report text (demo version).
"""

def analyze_trends(report_data):
    text = report_data.get("raw_text", "").lower()

    trends = []

    # Simple keyword-based trend extraction
    if "increase" in text:
        trends.append("There are indicators of increasing values in your report.")
    if "decrease" in text:
        trends.append("Some values show decreasing trends.")
    if "stable" in text:
        trends.append("Your report suggests stable readings.")
    if len(trends) == 0:
        trends.append("No clear trends detected from the report.")

    return {"trends": trends}