from dotenv import load_dotenv
import os
import json

load_dotenv()

import requests
NEWS_API_KEY= os.getenv("NEWS_API_KEY")

def fetch_news(topic,from_date,to_date):
    query=topic
    url=f"https://newsapi.org/v2/everything"
    params = {
        "q": query,           # Search keyword (e.g., "AI", "Tesla", "NASA")
        "from": from_date,    # Start date (YYYY-MM-DD)
        "to": to_date,        # End date (YYYY-MM-DD)
        "sortBy": "publishedAt",  # Sort by latest
        "language": "en",     # Filter only English articles
        "apiKey": NEWS_API_KEY
    }
    response=requests.get(url,params=params)
    if response.status_code==200:
        return response.json().get('articles',[])
    else:
        return[]