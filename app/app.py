# app/app.py
import streamlit as st
import tempfile
import json
from pathlib import Path

# Import your project agents (adjust names if needed)
from src.agents.report_agent import parse_report
from src.agents.summary_agent import generate_summary
from src.agents.recommendation_agent import generate_recommendations
from src.agents.trend_agent import analyze_trends
from src.agents.diet_agent import analyze_diet
from src.agents.sleep_agent import analyze_sleep
from src.agents.stress_agent import analyze_stress
from src.agents.hydration_agent import analyze_hydration

st.set_page_config(page_title="Personal Health Guardian", layout="wide")

st.title("Personal Health Guardian — Demo")

with st.sidebar:
    st.header("Run analysis")
    uploaded_file = st.file_uploader("Upload medical report (PDF)", type=["pdf"])
    if st.checkbox("Use sample PDF"):
        sample = True
    else:
        sample = False

    run_btn = st.button("Run analysis")

def run_pipeline(report_path: str):
    """Call project agents and return a consolidated result dict."""
    result = {}
    # parse raw report
    parsed = parse_report(report_path)
    result["extracted"] = parsed

    # summary
    try:
        summary = generate_summary(parsed)
    except Exception:
        summary = {"summary": "No summary available."}
    result["summary"] = summary

    # recommendations
    try:
        recs = generate_recommendations(parsed)
    except Exception:
        recs = {"recommendations": ["No recommendations available."]}
    result["recommendations"] = recs

    # trends
    try:
        trends = analyze_trends(parsed)
    except Exception:
        trends = {"trends": ["No trends analysis available."]}
    result["trends"] = trends

    # diet
    try:
        diet = analyze_diet(parsed)
    except Exception:
        diet = {"diet": "No diet analysis available."}
    result["diet"] = diet

    # sleep
    try:
        sleep = analyze_sleep(parsed)
    except Exception:
        sleep = {"sleep": "No sleep analysis available."}
    result["sleep"] = sleep

    # stress
    try:
        stress = analyze_stress(parsed)
    except Exception:
        stress = {"stress": "No stress analysis available."}
    result["stress"] = stress

    # hydration
    try:
        hydration = analyze_hydration(parsed)
    except Exception:
        hydration = {"hydration": "No hydration analysis available."}
    result["hydration"] = hydration

    return result

def show_results(res: dict):
    st.header("=== Consolidated Report ===")
    cols = st.columns([1, 1])

    with cols[0]:
        st.subheader("Summary")
        st.json(res.get("summary", {}))

        st.subheader("Recommendations")
        st.json(res.get("recommendations", {}))

        st.subheader("Trends")
        st.json(res.get("trends", {}))

    with cols[1]:
        st.subheader("Diet Analysis")
        st.json(res.get("diet", {}))

        st.subheader("Sleep Analysis")
        st.json(res.get("sleep", {}))

        st.subheader("Stress / Mental Health")
        st.json(res.get("stress", {}))

        st.subheader("Hydration")
        st.json(res.get("hydration", {}))

    st.markdown("---")
    st.subheader("Raw extracted data")
    st.json(res.get("extracted", {}))

if run_btn:
    if uploaded_file is None and not sample:
        st.error("Please upload a PDF or check 'Use sample PDF'.")
    else:
        # Save uploaded to a temp file (or use your sample file path)
        if sample:
            # expect repository sample path
            sample_path = Path.cwd() / "sample_reports" / "sample1.pdf"
            if not sample_path.exists():
                st.error("Sample PDF not found in sample_reports/sample1.pdf")
            else:
                report_path = str(sample_path)
        else:
            t = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
            t.write(uploaded_file.read())
            t.flush()
            report_path = t.name

        with st.spinner("Running analysis... this may take a few seconds"):
            try:
                consolidated = run_pipeline(report_path)
                show_results(consolidated)
                st.success("Analysis complete")
            except Exception as e:
                st.exception(e)