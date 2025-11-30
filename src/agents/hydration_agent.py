"""
Hydration Agent
- Detects hydration-related mentions and gives practical hydration advice.
- If weight is present in report text (kg), estimates daily water need using a simple rule.
"""

import re
from typing import Dict, Any, Optional

def _extract_weight_kg(text: str) -> Optional[float]:
    # find numbers followed by kg or kilograms
    m = re.search(r"(\d{2,3}(?:\.\d+)?)\s*(?:kg|kgs|kilograms)\b", text, re.IGNORECASE)
    if m:
        try:
            return float(m.group(1))
        except:
            return None
    return None

def _estimate_water_ml_per_day(weight_kg: float) -> int:
    # Simple rule: 30-35 ml per kg body weight. We'll use 35 ml/kg for recommendation.
    return int(round(weight_kg * 35))

def analyze_hydration(report_data: Dict[str, Any]) -> Dict[str, Any]:
    text = report_data.get("raw_text", "") or ""
    text_l = text.lower()

    flags = []
    recommendations = []

    # Keyword checks
    if any(k in text_l for k in ["dehydrat", "dehydration", "thirst", "very thirsty", "dry mouth", "reduced urine", "dark urine"]):
        flags.append("possible_dehydration")
        recommendations.append("Increase fluid intake immediately and consult a doctor if symptoms persist.")

    if "sweat" in text_l or "diarrhoea" in text_l or "vomit" in text_l:
        flags.append("fluid_loss_risk")
        recommendations.append("Replace fluids and electrolytes; consider oral rehydration solutions if needed.")

    # Weight-based recommendation
    weight = _extract_weight_kg(text)
    water_ml = None
    if weight:
        water_ml = _estimate_water_ml_per_day(weight)
        recommendations.append(f"Estimated daily water need (based on weight {weight} kg): about {water_ml} ml (~{int(water_ml/250)} cups of 250ml).")

    # Generic advice added if none specific
    if not recommendations:
        recommendations.append("Aim for 1.5–3 liters of fluids daily depending on activity, climate and health status.")
        recommendations.append("Prefer water, herbal teas, and electrolyte drinks when needed; limit sugary drinks.")

    return {
        "flags": flags,
        "recommended_daily_ml": water_ml,
        "recommendations": recommendations,
    }

# convenience alias
def analyze(report_data: Dict[str, Any]) -> Dict[str, Any]:
    return analyze_hydration(report_data)