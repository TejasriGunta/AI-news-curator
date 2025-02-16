# News Curator App

A comprehensive news curation platform that provides personalized news based on user-defined topics and advanced sentiment analysis. This app offers real-time news updates, concise summaries, and sentiment insights, enhancing the news-reading experience.

## Features
- **Personalized News Curation**: Users can define topics of interest to receive tailored news updates.
- **Real-Time News Updates**: Integrated with NewsAPI to fetch the latest news articles from reliable sources.
- **Concise Summaries**: Utilizes Gemini to generate meaningful and concise news summaries.
- **Advanced Sentiment Analysis**: Implemented with Transformers to categorize news as positive, negative, or neutral.
- **User-Friendly Interface**: Designed using Streamlit with features like:
  - Sentiment-based filtering
  - Detailed news views with summaries, sentiment insights, and images

## Tech Stack
- **Python**: Core programming language for model integration and backend processing.
- **Generative AI**: Gemini is used for generating concise and informative news summaries.
- **NLP (Natural Language Processing)**: Employed for sentiment analysis and text categorization.
- **Transformers**: Utilized for advanced sentiment analysis.
- **NewsAPI**: Integrated via the `requests` library for fetching real-time news updates.
- **Streamlit**: For building an interactive and intuitive user interface.