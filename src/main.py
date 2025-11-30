"""
Main entrypoint for Personal Health Guardian
Runs all agents: parser, summary, recommendations, trends
"""

from src.agents.report_agent import parse_report
from src.agents.summary_agent import generate_summary
from src.agents.recommendation_agent import generate_recommendations
from src.agents.trend_agent import analyze_trends
from src.agents.diet_agent import analyze as analyze_diet
from src.agents.sleep_agent import analyze_sleep
from src.agents.stress_agent import analyze_stress
from src.agents.hydration_agent import analyze as analyze_hydration

def main():
    print("=== Personal Health Guardian ===")

    report_path = "sample_reports/sample1.pdf"
    print(f"\nReading report: {report_path}")

    # Parse the PDF
    data = parse_report(report_path)
    print("\nExtracted Data:")
    print(data)

    # Summary
    summary = generate_summary(data)
    print("\nSummary:")
    print(summary)

    # Recommendations
    rec = generate_recommendations(data)
    print("\nRecommendations:")
    print(rec)

    # Trends
    trends = analyze_trends(data)
    print("\nTrend Analysis:")
    print(trends)

    #Diet
    diet = analyze_diet(data)
    print("\nDiet Analysis:")
    print(diet)

    # Sleep Analysis
    sleep = analyze_sleep(data)
    print("\nSleep Analysis:")
    print(sleep)

    # Stress Analysis
    stress = analyze_stress(data)
    print("\nStress / Mental Health Analysis:")
    print(stress)

    # Hydration Analysis
    hydration = analyze_hydration(data)
    print("\nHydration Analysis:")
    print(hydration)

    print("\n=== End of Analysis ===")


if __name__ == "__main__":
    main()