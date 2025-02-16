import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def summarization(news,title,source,url):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {'Content-Type': 'application/json'}
    prompt=f"summarise focusing on the title-{title}.Compile based on multiple reputable news sources,focusing on the common information across the articles.(description-{news},source-{source}).explain in simple human text with a minimum of 100words"
    data= {"contents": [{"parts": [{"text": prompt}]}]}
    response= requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_data = response.json()
        response_1=response_data['candidates'][0]['content']['parts'][0]['text']
        return(response_1)
    else:
        print(f"Error: {response.status_code} - {response.text}")

