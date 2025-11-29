"""
Recommendation Agent:
Takes parsed report data and generates basic recommendations.
"""

def generate_recommendations(report_data):
    text = report_data.get("raw_text", "").lower()
    recs = []

    # simple rule-based recommendations
    if "cholesterol" in text:
        recs.append("Reduce oily and fried foods. Increase fiber intake.")
    if "sugar" in text or "glucose" in text:
        recs.append("Monitor sugar levels and reduce sweets.")
    if "blood pressure" in text or "bp" in text:
        recs.append("Reduce salt intake and check BP regularly.")
    if "hemoglobin" in text:
        recs.append("Increase iron-rich foods like spinach and broccoli.")
    if len(recs) == 0:
        recs.append("No specific issues detected. Maintain a healthy lifestyle.")

    return {"recommendations": recs}