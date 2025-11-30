"""
Main entrypoint for Personal Health Guardian
Usage:
  python -m src.main --report sample_reports/sample1.pdf
  python -m src.main --interactive
"""
import argparse
import importlib
import os
import sys
from typing import Any, Callable, Dict

# Helper to attempt import and find a function under likely names
def load_callable(module_name: str, candidates: list[str]) -> Callable[..., Any] | None:
    try:
        mod = importlib.import_module(module_name)
    except Exception:
        return None
    for name in candidates:
        fn = getattr(mod, name, None)
        if callable(fn):
            return fn
    return None

def safe_call(fn: Callable[..., Any] | None, *args, **kwargs) -> Any:
    if fn is None:
        return None
    try:
        return fn(*args, **kwargs)
    except Exception as e:
        return {"_error": f"{e}"}

def build_agents():
    """
    Try to load each agent function with common candidate names.
    Returns dict name -> callable or None
    """
    agents = {}

    agents["parse_report"] = load_callable("src.agents.report_agent", ["parse_report", "report_agent", "parse"])
    agents["generate_summary"] = load_callable("src.agents.summary_agent", ["generate_summary", "make_summary", "summarize", "generate_summary_from_report"])
    agents["generate_recommendations"] = load_callable("src.agents.recommendation_agent", ["generate_recommendations", "recommendations", "generate_recs"])
    agents["analyze_trends"] = load_callable("src.agents.trend_agent", ["analyze_trends", "analyze_trend", "trend_analysis", "detect_trends"])
    agents["analyze_diet"] = load_callable("src.agents.diet_agent", ["analyze_diet", "diet_analysis", "analyze_diet_report", "diet_agent"])
    agents["analyze_sleep"] = load_callable("src.agents.sleep_agent", ["analyze_sleep", "sleep_analysis", "sleep_agent"])
    agents["analyze_stress"] = load_callable("src.agents.stress_agent", ["analyze_stress", "stress_analysis", "stress_agent"])
    agents["analyze_hydration"] = load_callable("src.agents.hydration_agent", ["analyze_hydration", "hydration_analysis", "hydration_agent"])
    return agents

def pretty_print_section(title: str, data: Any):
    print()
    print(title)
    print("-" * len(title))
    if data is None:
        print("Not available")
        return
    # If dict-like, pretty print keys
    if isinstance(data, dict):
        import json
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return
    # Otherwise, just print repr
    print(data)

def run_all(report_path: str | None, interactive: bool = False):
    agents = build_agents()

    if report_path is None:
        # default sample if exists
        candidate = os.path.join("sample_reports", "sample1.pdf")
        if os.path.exists(candidate):
            report_path = candidate
        else:
            report_path = None

    # 1. Parse PDF -> data
    parsed = safe_call(agents.get("parse_report"), report_path) if agents.get("parse_report") else None
    pretty_print_section("Reading report:", {"report_path": report_path})
    pretty_print_section("Extracted Data:", parsed)

    # 2. Summary
    summary = safe_call(agents.get("generate_summary"), parsed) if agents.get("generate_summary") else None
    pretty_print_section("Summary:", summary)

    # 3. Recommendations
    recs = safe_call(agents.get("generate_recommendations"), parsed) if agents.get("generate_recommendations") else None
    pretty_print_section("Recommendations:", recs)

    # 4. Trends
    trends = safe_call(agents.get("analyze_trends"), parsed) if agents.get("analyze_trends") else None
    pretty_print_section("Trend Analysis:", trends)

    # 5. Diet
    diet = safe_call(agents.get("analyze_diet"), parsed) if agents.get("analyze_diet") else None
    pretty_print_section("Diet Analysis:", diet)

    # 6. Sleep
    sleep = safe_call(agents.get("analyze_sleep"), parsed) if agents.get("analyze_sleep") else None
    pretty_print_section("Sleep Analysis:", sleep)

    # 7. Stress
    stress = safe_call(agents.get("analyze_stress"), parsed) if agents.get("analyze_stress") else None
    pretty_print_section("Stress / Mental Health Analysis:", stress)

    # 8. Hydration
    hydration = safe_call(agents.get("analyze_hydration"), parsed) if agents.get("analyze_hydration") else None
    pretty_print_section("Hydration Analysis:", hydration)

    print("\n=== End of Analysis ===\n")

def interactive_menu():
    print("Interactive mode — pick which parts to run")
    agents = build_agents()
    choices = [
        ("parse_report", "Parse PDF"),
        ("generate_summary", "Summary"),
        ("generate_recommendations", "Recommendations"),
        ("analyze_trends", "Trends"),
        ("analyze_diet", "Diet"),
        ("analyze_sleep", "Sleep"),
        ("analyze_stress", "Stress"),
        ("analyze_hydration", "Hydration"),
    ]
    print("Enter path to report PDF (or blank to use sample_reports/sample1.pdf):")
    rp = input("Report path: ").strip() or None

    print("\nAvailable actions:")
    for i, (_, label) in enumerate(choices, start=1):
        print(f"{i}. {label}")
    print("0. Run all")
    sel = input("Choose numbers separated by comma (e.g. 0 or 1,3,5): ").strip()
    to_run = []
    if not sel:
        to_run = [c[0] for c in choices]
    else:
        if "0" in sel.split(","):
            to_run = [c[0] for c in choices]
        else:
            for s in sel.split(","):
                s = s.strip()
                if not s: continue
                try:
                    idx = int(s) - 1
                    if 0 <= idx < len(choices):
                        to_run.append(choices[idx][0])
                except:
                    pass

    # call individually
    parsed = None
    if "parse_report" in to_run:
        parsed = safe_call(load_callable("src.agents.report_agent", ["parse_report", "parse"]), rp)
        pretty_print_section("Parsed", parsed)

    for name in to_run:
        if name == "parse_report":
            continue
        fn = build_agents().get(name)
        out = safe_call(fn, parsed) if fn else None
        pretty_print_section(name, out)

def main():
    parser = argparse.ArgumentParser(prog="Personal Health Guardian")
    parser.add_argument("--report", "-r", help="Path to PDF report", default=None)
    parser.add_argument("--interactive", "-i", action="store_true", help="Run interactive menu")
    args = parser.parse_args()

    if args.interactive:
        interactive_menu()
    else:
        run_all(args.report, interactive=False)

if __name__ == "__main__":
    main()