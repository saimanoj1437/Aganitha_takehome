📄 Research Paper Fetcher (PubMed API)
📌 Overview
This Python program fetches research papers from PubMed based on a user-specified query. It identifies papers with at least one non-academic author affiliated with a pharmaceutical or biotech company and returns the results in a CSV file.

🚀 Features
Fetches research papers from PubMed API
Filters papers with at least one company-affiliated author
Saves results as CSV with the following columns:
PubmedID: Unique identifier for the paper
Title: Title of the research paper
Publication Date: Full publication date
Non-academic Authors: Names of authors affiliated with non-academic institutions
Company Affiliations: Names of pharmaceutical/biotech companies
Corresponding Author Email: Email address of the corresponding author
Command-line options:
-h or --help: Display usage instructions
-d or --debug: Print debug information
-f or --file: Specify output filename (defaults to console output)
Follows GitHub version control
Uses Poetry for dependency management
🛠 Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
2️⃣ Install Dependencies (Using Poetry)
Ensure you have Poetry installed. If not, install it first:

bash
Copy
Edit
pip install poetry
Then install the project dependencies:

bash
Copy
Edit
poetry install
▶️ Usage
Run the command-line tool
bash
Copy
Edit
poetry run get-papers-list "YOUR_QUERY" -f output.csv
🔹 Example: Fetch papers related to cancer research

bash
Copy
Edit
poetry run get-papers-list "cancer research" --file results.csv
🔹 Example: Print results to console (without saving to a file)

bash
Copy
Edit
poetry run get-papers-list "AI in healthcare"
Command-line options:
Option	Description
-h or --help	Show usage instructions
-d or --debug	Enable debug mode for troubleshooting
-f or --file FILENAME	Save output to a CSV file instead of printing
