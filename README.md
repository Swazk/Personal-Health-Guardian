Personal Health Guardian



A modular AI-powered health analysis tool that extracts data from medical PDF reports and generates:



?? Raw text extraction



?? Summaries



?? Health recommendations



?? Trend analysis



?? Diet analysis



?? Sleep analysis



?? Stress \& mental health analysis



?? Hydration analysis





Built with a clean, extensible agent-based architecture.



?? Features



? PDF extraction using PyMuPDF



? Individual “agents” for each health domain



? Central main.py orchestrates full analysis



? Easy to extend with new agents



? Fully modular folder structure



?? Project Structure



Personal-Health-Guardian/

¦

+-- sample\_reports/

¦   +-- sample1.pdf

¦

+-- src/

¦   +-- main.py

¦   +-- agents/

¦   ¦   +-- report\_agent.py

¦   ¦   +-- summary\_agent.py

¦   ¦   +-- recommendation\_agent.py

¦   ¦   +-- trend\_agent.py

¦   ¦   +-- diet\_agent.py

¦   ¦   +-- sleep\_agent.py

¦   ¦   +-- stress\_agent.py

¦   ¦   +-- hydration\_agent.py

¦   ¦

¦   +-- utils/

¦       +-- pdf\_utils.py

¦

+-- requirements.txt

+-- README.md



?? Setup Instructions



1\. Create virtual environment



python -m venv venv



2\. Activate the environment



venv\\Scripts\\activate



3\. Install dependencies



pip install -r requirements.txt



? How to Run the Project



Full analysis of a PDF report



python -m src.main --report sample\_reports\\sample1.pdf



This runs:



PDF extraction



Summary



Recommendations



Trend analysis



Diet Agent



Sleep Agent



Stress Agent



Hydration Agent





And prints everything in a neat report.



?? Agents Overview



Agent	              File	                Purpose



Report Agent	      report\_agent.py	        Extracts text from PDF

Summary Agent	      summary\_agent.py	        Generates document summary

Recommendation Agent  recommendation\_agent.py	Health guidance

Trend Agent	      trend\_agent.py	        Detects health trends

Diet Agent	      diet\_agent.py	        Nutrition \& BMI insights

Sleep Agent	      sleep\_agent.py	        Sleep pattern analysis

Stress Agent	      stress\_agent.py	        Mental health indicators

Hydration Agent	      hydration\_agent.py	Fluid intake evaluation



?? Contributors



Swathi S      (Lead Developer)

S Kalaiarasan (UI, Implementation)

Shakthivel K  (Associate Developer)



?? Future Enhancements



Add chatbot interface



Add automatic graph generation



Add anomaly detection for critical values



Export report to PDF / HTML

