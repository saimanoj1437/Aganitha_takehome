 📄 Research Paper Fetcher
📌 Overview
This Python program fetches research papers from PubMed API, filters those with company-affiliated authors, and saves the results as a CSV file.

🚀 Features
Fetches research papers from PubMed API
Filters authors affiliated with pharmaceutical/biotech companies
Saves results as a CSV file with:
PubmedID (Unique ID)
Title (Paper title)
Publication Date (Full date)
Non-academic Authors (Company-affiliated authors)
Company Affiliations (Company names)
Corresponding Author Email




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
