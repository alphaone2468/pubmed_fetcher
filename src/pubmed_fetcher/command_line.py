import argparse
from pubmed_fetcher.main import fetch_pubmed_papers, save_to_csv

def print_results(papers):
    for paper in papers:
        print(f"\nPubmedID: {paper['PubmedID']}")
        print(f"Title: {paper['Title']}")
        print(f"Publication Date: {paper['Publication Date']}")
        print(f"Non-academic Authors: {paper['Non-academic Author(s)']}")
        print(f"Company Affiliations: {paper['Company Affiliation(s)']}")
        print(f"Corresponding Author Email: {paper['Corresponding Author Email']}")
        print("-" * 80)

def main():
    parser = argparse.ArgumentParser(description="Fetch pharma/biotech research papers from PubMed.")
    parser.add_argument("query", type=str, help="PubMed search query")
    parser.add_argument("-f", "--file", type=str, help="Save results to a CSV file")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug info")

    args = parser.parse_args()

    papers = fetch_pubmed_papers(args.query, debug=args.debug)
    if args.file:
        save_to_csv(papers, args.file)
    else:
        print_results(papers)
