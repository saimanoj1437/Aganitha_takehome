import requests
import os
import xml.etree.ElementTree as ET
import csv

# Hugging Face API Key
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")


# Keywords to detect company affiliations
COMPANY_KEYWORDS = ["Pharma", "Biotech", "Laboratories", "Inc", "LLC", "Corp"]

# Function to extract paper details
def extract_paper_details(xml_data):
    root = ET.fromstring(xml_data)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.find(".//PMID").text if article.find(".//PMID") is not None else "Unknown"

        title = article.find(".//ArticleTitle").text if article.find(".//ArticleTitle") is not None else "Unknown"

        
        pub_date_year = article.find(".//PubDate/Year")

        pub_date_month = article.find(".//PubDate/Month")

        pub_date_day = article.find(".//PubDate/Day")

        # Construct the full date
        pub_date = pub_date_year.text if pub_date_year is not None else "Unknown"

        if pub_date_month is not None:

            pub_date += f"-{pub_date_month.text}"

        if pub_date_day is not None:

            pub_date += f"-{pub_date_day.text}"

        # Extract author affiliations
        authors = article.findall(".//Author")

        non_academic_authors = []

        company_affiliations = []

        corresponding_author_email = "Not Available"

        for author in authors:

            affiliations = author.findall(".//AffiliationInfo/Affiliation")

            for affiliation in affiliations:

                if affiliation.text:

                    if any(keyword in affiliation.text for keyword in COMPANY_KEYWORDS):

                        non_academic_authors.append(author.find("LastName").text if author.find("LastName") is not None else "Unknown")
                        company_affiliations.append(affiliation.text)

            # Extract Corresponding Author Email  - if availble
            email = author.find(".//AffiliationInfo/Affiliation/Email")

            if email is not None and corresponding_author_email == "Not Available":

                corresponding_author_email = email.text  

        papers.append({
            "PubmedID": pmid,

            "Title": title,

            "Publication Date": pub_date,  

            "Non-academic Author(s)": ", ".join(non_academic_authors) if non_academic_authors else "None",

            "Company Affiliation(s)": ", ".join(company_affiliations) if company_affiliations else "None",
            
            "Corresponding Author Email": corresponding_author_email
        })

    return papers

# Function to save results to CSV
def save_to_csv(papers, filename="results.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", 
                      "Company Affiliation(s)", "Corresponding Author Email"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(papers)
