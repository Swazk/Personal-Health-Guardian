_**🩺 Personal Health Guardian – AI-Powered Health Analysis Tool**_

Personal Health Guardian is a modular AI-driven health analysis system that extracts data from medical PDF reports and generates actionable insights including summaries, trends, lifestyle recommendations, and detailed health domain analysis (diet, sleep, hydration, stress and trends).


_**Features**_

- 🗂 **Raw text extraction** from medical/diagnostic PDF reports (PyMuPDF)
- 📝 **Summary** generation (concise report summary)
- 💡 **Health recommendations** (diet, blood sugar, BP, general guidance)
- 📈 **Trend analysis** (detects longitudinal changes in key metrics)
- 🥗 **Diet analysis** (basic meal suggestions and flags)
- 💤 **Sleep analysis** (sleep score & hygiene tips)
- 🧘 **Stress / mental health analysis** (flags & recommendations)
- 💧 **Hydration analysis** (recommended intake and tips)
- 🧩 **Modular agent-based architecture** — each health domain is an independent "agent"

  
_**⭐ Key Capabilities**_

* Extracts raw text from medical PDFs
* Generates concise summaries
* Provides personalized health recommendations
* Performs trend analysis
* Diet evaluation (BMI, nutrition flags, meal suggestions)
* Sleep quality assessment
* Stress & mental health analysis
* Hydration & water intake evaluation
* Clean, fully modular Agent Architecture


_**Demo / Quick start**_

**Requirements:**
- Python 3.11 (recommended)
- Virtual environment (venv)
- `pip install -r requirements.txt`

  
_**🧠 How It Works**_

The system is built around independent agents, each responsible for one part of the analysis:
* **Report Agent** → Extract raw PDF text
* **Summary Agent** → Generate clean summary
* **Recommendation Agent** → Provide health suggestions
* **Trend Agent** → Detect patterns or abnormalities
* **Diet Agent** → Evaluate nutrition and BMI
* **Sleep Agent** → Analyze sleep-related information
* **Stress Agent** → Mental health and stress-level insights
* **Hydration Agent** → Water intake recommendations
All results are collected together by the main entrypoint script to generate a full health report.


## 📂 Project Structure

```
Personal-Health-Guardian/
├── sample_reports/
│   └── sample1.pdf
├── app/
│   └── app.py              # Streamlit UI
├── src/
│   ├── main.py             # entrypoint (CLI/demo)
│   └── agents/
│       ├── report_agent.py
│       ├── summary_agent.py
│       ├── recommendation_agent.py
│       ├── trend_agent.py
│       ├── diet_agent.py
│       ├── sleep_agent.py
│       ├── stress_agent.py
│       └── hydration_agent.py
├── utils/
│   └── pdf_utils.py
├── requirements.txt
├── README.md
└── LICENSE
```


_**🚀 Installation & Usage**_

_**1️⃣ Create a Virtual Environment**_

python -m venv venv


**_2️⃣ Activate It_**

venv\Scripts\activate   # Windows


**_3️⃣ Install Required Libraries_**

pip install -r requirements.txt


**_4️⃣ Run the Program_**

python -m src.main


_**start the Streamlit run demo UI**_

streamlit run app/app.py


_**Testing**_
- Drop `sample_reports/sample1.pdf` or your own PDF into the UI, upload and inspect the generated sections.
- Unit tests (if present) are in `/tests`; run with `pytest`.


_**Development notes**_
- Use modular agents to extend functionality (add new `agent_x.py` and import in `src/main.py` / `app/app.py`).
- Keep `requirements.txt` updated after adding libs: `pip freeze > requirements.txt`.


Open `http://localhost:8501` and upload a sample PDF (`sample_reports/sample1.pdf`) to test.


_**🖥️ What the Program Outputs**_

* Extracted raw text
* Summary of the health report
* Key recommendations
* Diet/BMI insights
* Sleep quality score
* Stress & mental health suggestions
* Hydration advice
* Trend observations
* Final consolidated report


**_🛠️ Tech Stack_**

| Component       | Technology          |
| --------------- | ------------------- |
| Language        | Python 3.10+        |
| PDF Parsing     | PyMuPDF (fitz)      |
| Architecture    | Modular Agent-based |
| Version Control | Git + GitHub        |


**_👥 Team Members_**

| Name                     | Role                                     |
| ------------------------ | ---------------------------------------- |
| **Swathi Senthil Kumar** | Lead Developer (Complete Implementation) |
| **Shakthivel K**         | Associate Developer                      |
| **S. Kalaiarasan**       | UI & Implementation                      |


**_📝 Future Improvements_**

* Convert into a web dashboard (Flask / FastAPI)
* Export final reports as PDF/HTML
* Add Machine Learning health anomaly detection
* Integrate with smartwatch/fitness tracker data


_**📜 License**_

Distributed under the MIT License.
Feel free to use, modify, and enhance.
Hydration Agent → Water intake recommendations

All results are collected together by the main entrypoint script to generate a full health report.
