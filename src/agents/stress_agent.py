"""
Stress / Mental Health Agent
Detects mental health indicators from report text and provides suggestions.
"""

def analyze_stress(report_data):
    text = report_data.get("raw_text", "").lower()

    flags = []
    recommendations = []

    # Keyword-based stress detection
    if "stress" in text or "anxiety" in text or "anxious" in text:
        flags.append("stress/anxiety detected")
        recommendations.append("Practice deep breathing or meditation for 10–15 minutes daily.")

    if "depression" in text or "low mood" in text or "sad" in text:
        flags.append("low mood indicators")
        recommendations.append("Maintain routine, stay socially connected, and consider counseling if symptoms persist.")

    if "fatigue" in text or "tired" in text:
        flags.append("fatigue")
        recommendations.append("Balance work and rest; avoid overexertion.")

    if "panic" in text:
        flags.append("panic indicators")
        recommendations.append("Practice grounding techniques; consult healthcare if episodes repeat.")

    if "sleep" in text and ("poor" in text or "lack" in text):
        flags.append("sleep-related stress")
        recommendations.append("Maintain sleep hygiene: fixed sleep times, no caffeine late evening.")

    # General baseline recommendation
    if not recommendations:
        recommendations.append("Maintain a balanced schedule, practice mindfulness, and stay physically active.")

    # Stress score (mock scoring)
    score = 100
    if "stress/anxiety detected" in flags:
        score -= 25
    if "low mood indicators" in flags:
        score -= 25
    if "panic indicators" in flags:
        score -= 30
    if "sleep-related stress" in flags:
        score -= 10
    if "fatigue" in flags:
        score -= 5

    # Clip score to 0–100 range
    if score < 0:
        score = 0

    return {
        "stress_flags": flags,
        "stress_score": score,
        "stress_recommendations": recommendations,
    }