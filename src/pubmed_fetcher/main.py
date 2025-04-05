import re
import pandas as pd
from Bio import Entrez

Entrez.email = "mohdahmeduddinaaa@gmail.com"

PHARMA_KEYWORDS = ["biotech", "therapeutics", "biosciences", "corp", "laboratories", "llc", "ltd","inc","genomics", "biosystems", "pharma", "biopharma"]

def fetch_pubmed_papers(query, max_results=50, debug=False):
    if debug:
        print(f"[DEBUG] Fetching: {query}")

    search_handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    search_results = Entrez.read(search_handle)
    search_handle.close()

    paper_ids = search_results["IdList"]
    if not paper_ids:
        return []

    fetch_handle = Entrez.efetch(db="pubmed", id=",".join(paper_ids), rettype="xml", retmode="xml")
    papers = Entrez.read(fetch_handle)
    fetch_handle.close()

    results = []
    for article in papers["PubmedArticle"]:
        citation = article["MedlineCitation"]
        pubmed_id = citation["PMID"]
        title = citation["Article"].get("ArticleTitle", "No Title")
        pub_date = citation["Article"].get("Journal", {}).get("JournalIssue", {}).get("PubDate", {}).get("Year", "Unknown")

        authors = citation["Article"].get("AuthorList", [])
        company_affiliations = []
        non_academic_authors = []
        corresponding_email = ""

        for author in authors:
            if "AffiliationInfo" in author:
                for aff in author["AffiliationInfo"]:
                    affiliation = aff.get("Affiliation", "")
                    if any(re.search(k, affiliation, re.IGNORECASE) for k in PHARMA_KEYWORDS):
                        company_affiliations.append(affiliation)
                        name = f"{author.get('ForeName', '')} {author.get('LastName', '')}".strip()
                        non_academic_authors.append(name)

                    email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", affiliation)
                    if email_match:
                        corresponding_email = email_match.group(0)

        if company_affiliations:
            results.append({
                "PubmedID": pubmed_id,
                "Title": title,
                "Publication Date": pub_date,
                "Non-academic Author(s)": "; ".join(non_academic_authors) or "N/A",
                "Company Affiliation(s)": "; ".join(company_affiliations),
                "Corresponding Author Email": corresponding_email or "N/A"
            })

    return results

def save_to_csv(papers, filename):
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
