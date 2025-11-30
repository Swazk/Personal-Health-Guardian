Personal Health Guardian

A modular AI-powered health analysis tool that extracts data from medical PDF reports and generates:

📄 Raw text extraction

📝 Summaries

💡 Health recommendations

📈 Trend analysis

🍽 Diet analysis

😴 Sleep analysis

🧠 Stress & mental health analysis

💧 Hydration analysis


Built with a clean, extensible agent-based architecture, allowing multiple independent health modules to work together and produce a combined full report.


🚀 Features

🔍 PDF Extraction

Uses PyMuPDF to extract raw text from any medical report.


🤖 Modular Agents

Each health domain has its own agent:

report_agent – raw text extraction

summary_agent – generates high-level summary

recommendation_agent – health recommendations

trend_agent – detects repeating patterns

diet_agent – BMI, nutrition flags & diet suggestions

sleep_agent – sleep score & sleep hygiene evaluation

stress_agent – stress/mental health checks

hydration_agent – water-intake analysis


🧩 Main Entrypoint

The src/main.py script:

Reads the input PDF

Calls all health agents

Prints a complete consolidated report


🗂 Project Structure

Personal-Health-Guardian/
│
├── sample_reports/
│   └── sample1.pdf
│
├── src/
│   ├── main.py
│   ├── agents/
│   │   ├── report_agent.py
│   │   ├── summary_agent.py
│   │   ├── recommendation_agent.py
│   │   ├── trend_agent.py
│   │   ├── diet_agent.py
│   │   ├── sleep_agent.py
│   │   ├── stress_agent.py
│   │   └── hydration_agent.py
│   │
│   └── utils/
│       └── pdf_utils.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE


⚙ Installation & Usage

1️⃣ Create and activate virtual environment

python -m venv venv
venv\Scripts\activate

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Run the tool

python -m src.main


👥 Contributors

Swathi Senthil Kumar

Shakthivel K (Associate Developer)

S Kalaiarasan — UI, Implementation


📜 License

This project is licensed under the MIT Licens
