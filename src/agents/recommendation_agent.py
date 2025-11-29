"""
Simple Recommendation Agent stub.
Takes parsed report text and produces basic recommendations.
"""

from typing import Dict, Any, List

def recommend_from_text(parsed_report: Dict[str, Any]) -> Dict[str, Any]:
    """
    Very small rule-based recommender for demo.
    parsed_report is expected to contain 'raw_text' (string).
    Returns a dict with recommendations.
    """
    text = parsed_report.get("raw_text", "").lower()
    recommendations: List[str] = []

    # simple rules (demo). Replace with ML/NLP or more rules later.
    if not text.strip():
        recommendations.append("No content found in report — ask for a clearer PDF.")
    if "blood pressure" in text or "bp" in text:
        recommendations.append("Monitor blood pressure daily; consult physician if consistently high.")
    if "glucose" in text or "sugar" in text:
        recommendations.append("Track blood glucose and follow dietary plan.")
    if "fever" in text or "temperature" in text:
        recommendations.append("Consider symptomatic care and medical check-up if fever persists.")
    if not recommendations:
        recommendations.append("No specific findings — consider standard wellness checks.")

    return {
        "summary": text[:300],               # first 300 chars as short summary
        "recommendations": recommendations,
        "recommendation_count": len(recommendations),
    }