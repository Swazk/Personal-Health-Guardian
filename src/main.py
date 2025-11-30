"""
Main entrypoint for Personal Health Guardian
Runs all agents: parser, summary, recommendations, trends
"""

from src.agents.report_agent import parse_report
from src.agents.summary_agent import generate_summary
from src.agents.recommendation_agent import generate_recommendations
from src.agents.trend_agent import analyze_trends
from src.agents.diet_agent import analyze as analyze_diet

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

    print("\n=== End of Analysis ===")


if __name__ == "__main__":
    main()