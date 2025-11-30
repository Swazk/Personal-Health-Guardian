"""
Diet Agent
- Extracts weight/height from raw text (if present) and computes BMI.
- Scans report text for keywords (cholesterol, glucose, bp, triglyceride)
  and returns diet recommendations and a short sample meal plan.
"""

import re
from typing import Dict, Any, List, Optional

def _extract_number_with_units(text: str, units: List[str]) -> Optional[float]:
    """Find first numeric value followed by any of the units in the list (case-insensitive)."""
    for unit in units:
        # e.g. "70 kg" or "170 cm" or "1.70 m"
        pattern = rf"(\d{{1,3}}(?:\.\d+)?)\s*{re.escape(unit)}"
        m = re.search(pattern, text, re.IGNORECASE)
        if m:
            try:
                return float(m.group(1))
            except:
                pass
    return None

def _compute_bmi(weight_kg: float, height_m: float) -> float:
    return round(weight_kg / (height_m * height_m), 1)

def _bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal"
    if bmi < 30:
        return "Overweight"
    return "Obese"

def analyze_diet(report_data: Dict[str, Any]) -> Dict[str, Any]:
    text = report_data.get("raw_text", "")
    text_l = text.lower()

    # Extract weight and height (several unit variants)
    weight = _extract_number_with_units(text, ["kg", "kgs", "kilograms"])
    height_cm = _extract_number_with_units(text, ["cm", "centimeters"])
    height_m = None
    if height_cm:
        height_m = height_cm / 100.0
    else:
        # try meters like "1.70 m" or "1.7 m"
        hm = _extract_number_with_units(text, ["m", "meters"]) 
        if hm and hm > 3:  # if found meters but it is >3 then it's probably cm mis-detected; ignore
            # it's ambiguous; ignore if >3
            pass
        elif hm:
            height_m = hm

    bmi = None
    bmi_cat = None
    if weight and height_m:
        try:
            bmi = _compute_bmi(weight, height_m)
            bmi_cat = _bmi_category(bmi)
        except Exception:
            bmi = None

    # Keyword-based diet flags
    flags = []
    if "cholesterol" in text_l or "ldl" in text_l or "hdl" in text_l:
        flags.append("cholesterol")
    if "glucose" in text_l or "sugar" in text_l or "hba1c" in text_l:
        flags.append("glucose")
    if "blood pressure" in text_l or "bp " in text_l:
        flags.append("hypertension")
    if "triglyceride" in text_l or "triglycerides" in text_l:
        flags.append("triglyceride")

    # Base suggestions
    suggestions: List[str] = []
    meal_plan: List[str] = []

    # General healthy advice
    suggestions.append("Prioritize whole foods, vegetables, fruits, lean proteins, whole grains, and legumes.")
    suggestions.append("Limit processed foods, sugary drinks, and excessive salt.")

    # Tailored by flags
    if "cholesterol" in flags:
        suggestions.append("Reduce saturated fats (butter, fatty cuts), avoid trans-fats; include oats, nuts, and fatty fish (omega-3s).")
        meal_plan.append("Breakfast: Oatmeal with berries and a handful of nuts.")
        meal_plan.append("Dinner: Grilled salmon, quinoa, and steamed broccoli.")
    if "glucose" in flags:
        suggestions.append("Prefer low-glycemic index carbs, control portion sizes, and avoid simple sugars.")
        meal_plan.append("Breakfast: Greek yogurt with chia seeds and seeds.")
        meal_plan.append("Snack: Apple with peanut butter (small portion).")
    if "hypertension" in flags:
        suggestions.append("Lower sodium intake, increase potassium-rich foods (bananas, spinach), and stay hydrated.")
        meal_plan.append("Lunch: Lentil soup (low salt) with mixed salad.")
    if "triglyceride" in flags:
        suggestions.append("Cut simple carbs and alcohol; increase physical activity and omega-3 rich foods.")
        if "triglyceride" not in meal_plan:
            meal_plan.append("Snack: Handful of raw almonds or walnuts.")

    # If BMI available, add BMI-specific tips
    if bmi is not None:
        suggestions.append(f"Calculated BMI: {bmi} ({bmi_cat}). Follow weight-targeted diet and exercise plan.")
        if bmi_cat == "Underweight":
            suggestions.append("Increase calorie-dense healthy foods: nuts, dairy, legumes; frequent small meals.")
        elif bmi_cat == "Normal":
            suggestions.append("Maintain balanced diet and regular physical activity.")
        elif bmi_cat == "Overweight":
            suggestions.append("Create moderate calorie deficit, increase protein, reduce processed carbs, and increase activity.")
        else:  # Obese
            suggestions.append("Consult healthcare provider for personalized weight-reduction plan and consider supervised programs.")

    # If no tailored meal_plan items were added, provide a simple default plan
    if not meal_plan:
        meal_plan = [
            "Breakfast: Oatmeal with banana or eggs & wholegrain toast.",
            "Lunch: Grilled chicken/fish or chickpea salad with mixed greens.",
            "Dinner: Vegetable stir-fry with tofu/lean protein and brown rice.",
            "Snacks: Fruit, yoghurt, nuts (small portions)."
        ]

    return {
        "bmi": bmi,
        "bmi_category": bmi_cat,
        "flags": flags,
        "suggestions": suggestions,
        "sample_meal_plan": meal_plan,
    }

# quick alias for convenience
def analyze(report_data: Dict[str, Any]) -> Dict[str, Any]:
    return analyze_diet(report_data)