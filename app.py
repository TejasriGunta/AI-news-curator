import streamlit as st
from datetime import datetime
from agents.fetch_news import fetch_news
from agents.summarizaton import summarization
from agents.sentiment import analyze_sentiment
from agents.filter_sentiment import filter_senti 

st.title("AI-Powered Personalized News Curator")

# User Preferences
topic = st.text_input("Enter a topic")
from_date = st.date_input("From Date", datetime.today())
to_date = st.date_input("To Date", datetime.today())
sentiment=st.radio("Filter articles by sentiment:", ["All", "Positive", "Negative"])

# Initialize session state for articles
if "articles" not in st.session_state:
    st.session_state.articles = []

if st.button("Fetch and Curate News"):
    st.session_state.articles = fetch_news(topic,from_date,to_date)
    st.session_state.articles = filter_senti(st.session_state.articles, sentiment)

for index, article in enumerate(st.session_state.articles[:5]):
    st.subheader(article.get('title'))
    st.write(article['description'])
    if article.get('urlToImage'):
        st.image(article.get('urlToImage'),use_container_width=True,caption=f'Picture taken from-{article['source']['name']}')

    # Use session state for checkboxes and buttons
    if f"show_content_{index}" not in st.session_state:
        st.session_state[f"show_content_{index}"] = False

    if f"summarize_{index}" not in st.session_state:
        st.session_state[f"summarize_{index}"] = False

    if f"sentiment_{index}" not in st.session_state:
        st.session_state[f"sentiment_{index}"] = False

    # Show content button
    if st.button("Show full content", key=f"show_content_btn_{index}"):
        st.session_state[f"show_content_{index}"] = not st.session_state[f"show_content_{index}"]

    if st.session_state[f"show_content_{index}"]:
        st.write(article.get('content'))
        st.write(f"To view full content click on the url-{article.get('url')}")

        # Summarize this article
        if st.checkbox("Summarize this article", key=f"summarize_chk_{index}"):
            st.write("Summary:")
            st.write(summarization(article.get('description'),article.get('title'),article['source']['name'],article.get('url')))
        # Analyze sentiment
        if st.checkbox("Analyze Sentiment", key=f"sentiment_chk_{index}"):
            sentiment = analyze_sentiment(article.get('description'))
            st.write(f"Sentiment: {sentiment[0]['label']} with score {sentiment[0]['score']}")
