from dotenv import load_dotenv
import os
import json

load_dotenv()

import requests
NEWS_API_KEY= os.getenv("NEWS_API_KEY")

def fetch_news(topic):
    query=topic
    url=f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    response=requests.get(url)
    if response.status_code==200:
        return response.json().get('articles',[])
    else:
        return[]