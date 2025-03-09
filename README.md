This project utilizes LLM (Large Language Models) to generate concise summaries of research papers.
We use Hugging Face's Mistral-7B-Instruct model for this purpose.


Why LLM?

Extracts key insights from research abstracts
Provides short and readable summaries
Helps in quick understanding of research topics






🛠 Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
2️⃣ Install Dependencies (Using Poetry)
bash
Copy
Edit
pip install poetry  
poetry install
▶️ Usage
Run the command-line tool
bash
Copy
Edit
poetry run get-papers-list "YOUR_QUERY" -f output.csv
🔹 Example: Fetch cancer research papers

bash
Copy
Edit
poetry run get-papers-list "cancer research" --file results.csv
🔹 Example: Print results to console

bash
Copy
Edit
poetry run get-papers-list "AI in healthcare"
