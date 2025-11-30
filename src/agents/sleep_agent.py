"""
Sleep Analysis Agent:
Detects sleep-related indicators in report text and recommends improvements.
"""

def analyze_sleep(report_data):
    text = report_data.get("raw_text", "").lower()

    flags = []
    recommendations = []
    
    # Keyword detection (simple NLP)
    if "tired" in text or "fatigue" in text or "exhaustion" in text:
        flags.append("fatigue")
        recommendations.append("Ensure 7–9 hours of consistent sleep; avoid screens 1 hour before bed.")

    if "insomnia" in text or "sleep" in text and "poor" in text:
        flags.append("possible insomnia")
        recommendations.append("Maintain fixed sleep schedule and avoid caffeine after 5 PM.")

    if "iron" in text or "hemoglobin" in text:
        recommendations.append("Low iron can affect sleep; consider iron-rich foods if suggested by doctor.")

    if "thyroid" in text:
        recommendations.append("Thyroid imbalance may disrupt sleep; follow prescribed treatment.")

    # General recommendations (added only if no specific flags)
    if not recommendations:
        recommendations.append("Maintain consistent sleep schedule and good sleep hygiene practices.")

    # Simple sleep score (mock)
    score = 100
    if "fatigue" in flags:
        score -= 20
    if "possible insomnia" in flags:
        score -= 30

    return {
        "sleep_flags": flags,
        "sleep_score": score,
        "sleep_recommendations": recommendations,
    }