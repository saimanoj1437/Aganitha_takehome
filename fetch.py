import requests
import xml.etree.ElementTree as ET

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

DETAILS_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_pubmed_papers(query: str, max_results: int = 10):
    
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "xml"
    }
    
    response = requests.get(PUBMED_API_URL, params=params)
    response.raise_for_status()
    
    root = ET.fromstring(response.text)
    pmids = [pmid.text for pmid in root.findall(".//Id")]
    
    return pmids

def fetch_paper_details(pmids):
   
    if not pmids:
        return []
    
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml"
    }
    
    response = requests.get(DETAILS_API_URL, params=params)
    response.raise_for_status()
    
    return response.text  # XML data to be processed in the next step
