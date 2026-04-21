import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

QUERY = "AI OR technology OR LLM OR AI Agent"
LANGUAGE = "en"
SORTBY = "publishedAt"
PAGE_SIZE = 50

API_KEY = os.getenv("NEWS_API_KEY")

if not API_KEY or API_KEY == "your_newsapi_key":
    raise ValueError("NEWS_API_KEY not found in environment variables")

def fetch_news():
    url = "https://newsapi.org/v2/everything"

    params = {
        "q": QUERY,
        "language": LANGUAGE,
        "sortBy": SORTBY,
        "from": (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d"),
        "apiKey": API_KEY,
        "pageSize": PAGE_SIZE
    }

    # handle error responses
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if "articles" not in data:
            print(f"API error: {data.get('message', 'Unknown error')}")
            return []
        return data["articles"]
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return []
    except ValueError as e:
        print(f"JSON parsing error: {e}")
        return []

if __name__ == "__main__":
    articles = fetch_news()
    print(len(articles))

    if articles:
        print(articles[0])
    else:
        print("No articles found.")