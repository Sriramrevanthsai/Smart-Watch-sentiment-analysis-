# Smart-Watch-sentiment-analysis-
Project Title:

Smartwatch Sentiment Analyzer using Streamlit & NLP

Project Overview

This project analyzes smartwatch reviews and classifies them as Positive, Negative, or Neutral.

It contains two versions:

1️⃣ Basic Version – main.py

Uses TextBlob

Works offline

Simple and fast sentiment analysis

Matches the official project guidelines

2️⃣ Advanced Version – extra_with_ai.py

Uses Gemini AI API (optional)

Gives more accurate, context-aware sentiment

Added only as an extended/advanced feature

Technologies Used

Python

Streamlit

TextBlob

(Optional) Google Gemini API

How to Run the Basic Version (main.py)

Install dependencies:

pip install streamlit textblob


Run the application:

streamlit run main.py


Enter a smartwatch review and view the sentiment.

How to Run the AI Version (extra_with_ai.py)

(Use only if you want the advanced version)

Install dependencies:

pip install streamlit textblob google-generativeai


Add your Gemini API key inside extra_with_ai.py

Run the file:

streamlit run extra_with_ai.py

How It Works

User enters a review

main.py → TextBlob calculates polarity & sentiment

extra_with_ai.py → Gemini AI interprets meaning and gives a smarter sentiment

Output is displayed instantly

Example

Input:
“The watch is amazing but battery life is average.”

Output may be:

TextBlob (main.py): Positive

Gemini AI (extra_with_ai.py): Mixed but slightly positive

Features

Easy-to-use Streamlit interface

Supports review history

No dataset required

Works offline (main.py)

Optional GEN-AI powered version

Future Enhancements

Use VADER or BERT for deeper analysis

Add graphs and analytics dashboard

Add multilingual review support