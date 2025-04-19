# Import packages
import json
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
NEWS_KEY = os.getenv("NEWS_KEY") 

# Function to construct API endpoint with optional filters
def build_api_url(category="business", query=None):
    base_url = "https://newsapi.org/v2/top-headlines?"
    params = [
        f"category={category}",
        f"apiKey={NEWS_KEY}"
    ]
    if query:
        params.append(f"q={query}")
    return base_url + "&".join(params)

# Fetch and print articles
def fetch_and_print_articles(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        if not articles:
            print("No articles found for this search.")
        else:
            for index, article in enumerate(articles[:3], start=1):
                print(f"Article {index}:\n{json.dumps(article, sort_keys=True, indent=4)}\n")
    else:
        print(f"Error: {response.status_code} - {response.text}")

# Example usage with query filter
query = "inflation"
api_endpoint = build_api_url(query=query)
fetch_and_print_articles(api_endpoint)
