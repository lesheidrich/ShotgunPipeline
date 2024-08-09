import os
import time
import requests
from xml.etree import ElementTree as ET
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
EMAIL = os.getenv('EMAIL')
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
TOOL_NAME = "my_gut_microbiome_fetcher"
TERM = "gut microbiome"


def taxonomy(max_recs=10000, batch_size=200):
    start_index = 0

    while True:
        url = f"{BASE_URL}/esearch.fcgi"
        search_params = {
            "db": "taxonomy",
            "term": TERM,
            "retstart": start_index,
            "retmax": batch_size,
            "usehistory": "y",
            "api_key": API_KEY,
            "tool": TOOL_NAME,
            "email": EMAIL
        }

        try:
            search_response = requests.get(url, params=search_params)
            search_response.raise_for_status()

            print(f"Response raw XML from : {url}")
            print(search_response.text)

            search_root = ET.fromstring(search_response.content)
            webenv = search_root.find("WebEnv").text
            query_key = search_root.find("QueryKey").text

            if not webenv or not query_key:
                raise RuntimeError("Failed to retrieve WebEnv or QueryKey.")

            fetch_url = f"{BASE_URL}/esummary.fcgi"
            fetch_params = {
                "db": "taxonomy",
                "webenv": webenv,
                "query_key": query_key,
                "retmode": "xml",
                "api_key": API_KEY,
                "tool": TOOL_NAME,
                "email": EMAIL
            }

            print(f"Sending fetch request: {fetch_url}")
            fetch_response = requests.get(fetch_url, params=fetch_params)
            fetch_response.raise_for_status()

            # Print the raw XML response for debugging
            print("Fetch Response Content:")
            print(fetch_response.text)

            # Parse fetch response
            fetch_root = ET.fromstring(fetch_response.content)
            docs = fetch_root.findall(".//DocSum")

            if not docs:
                print("No documents found in the fetch response.")
                break

            for doc in docs:
                print("\nDocument:")
                for item in doc.findall(".//Item"):
                    name = item.get("Name")
                    value = item.text
                    print(f"{name}: {value}")

            # Update the start index for the next batch
            start_index += batch_size

            # Optional: Adjust max_records to control total fetch size
            if start_index >= max_recs:
                break

            # Sleep to comply with NCBI request rate limits
            time.sleep(0.5)

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            break
        except RuntimeError as e:
            print(f"Runtime error: {e}")
            break


if __name__ == "__main__":
    try:
        taxonomy()
    except Exception as e:
        print(f"An error occurred: {e}")
