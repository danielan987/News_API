# Import packages
import json
import requests
import os
from dotenv import load_dotenv

# Access API
load_dotenv()
NEWS_KEY = os.getenv("NEWS_KEY") 
api_endpoint = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={NEWS_KEY}"

# Fetch the data
def fetch_and_print_articles(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        for index, article in enumerate(articles[:3], start=1):
            print(f"Article {index}:\n{json.dumps(article, sort_keys=True, indent=4)}\n")
    else:
        print(f"Error: {response.status_code}")
fetch_and_print_articles(api_endpoint)
