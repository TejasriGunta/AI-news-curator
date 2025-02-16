from agents.fetch_news import fetch_news
from agents.sentiment import analyze_sentiment

def filter_senti(articles, sentiment_filter):

    filtered_articles = []

    for article in articles:
            text=article.get('content')
            sentiment = analyze_sentiment(text)
            sentiment= sentiment[0]['label']
        # Apply sentiment filter logic
            if sentiment_filter == "Positive" and sentiment != "POSITIVE":
                continue
            if sentiment_filter == "Negative" and sentiment != "NEGATIVE":
                continue

        # No filtering if "All" is selected
            filtered_articles.append(article)
    return (filtered_articles)