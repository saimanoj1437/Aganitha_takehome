import click
import pandas as pd
from pubmed_fetcher.fetch import fetch_pubmed_papers, fetch_paper_details

from pubmed_fetcher.filter import extract_paper_details



@click.command()

@click.argument("query", required=False)

@click.option("-h", "--help", is_flag=True, help="Display usage instructions.")


@click.option("-d", "--debug", is_flag=True, help="Print debug information during execution.")




@click.option("-f", "--file", type=click.Path(), help="Specify the filename to save the results.")
def main(query, help, debug, file):
    

    if help:
        click.echo("""
        Usage: poetry run get-papers-list <query> [options]

        Options:
          -h, --help       Show this message and exit.
          -d, --debug      Print debug information during execution.
          -f, --file FILE  Save results to a specified CSV file.
        
        Example:
          poetry run get-papers-list "cancer research" -d
          poetry run get-papers-list "AI in healthcare" -f results.csv
        """)
        return

    if not query:
        click.echo("Query is required. Run with '--help' for usage details.")
        return

    if debug:
        click.echo(f"Debug: Searching PubMed for '{query}'")

    
    pmids = fetch_pubmed_papers(query)

    xml_data = fetch_paper_details(pmids)

  
    if debug:
        click.echo("Raw XML data received from PubMed API:")
        click.echo(xml_data[:1000]) 

    papers = extract_paper_details(xml_data)
    df = pd.DataFrame(papers)
    

    if file:
        df.to_csv(file, index=False)
        click.echo(f"Results saved to {file}")
   

if __name__ == "__main__":
    main()
