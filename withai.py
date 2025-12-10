import streamlit as st
from textblob import TextBlob
from datetime import datetime
import google.generativeai as genai

# ---------------------------------------------------------
# CONFIGURE GEMINI API
# ---------------------------------------------------------

genai.configure(api_key="")#use the own API key here

# ---------------------------------------------------------
# GEMINI SENTIMENT (FRESH WORKING VERSION)
# ---------------------------------------------------------
def gemini_sentiment(review):
    prompt = f"""
    You are an expert sentiment analysis AI.
    Analyze the sentiment of this smartwatch review.
    Give output in this exact format:

    Sentiment: Positive / Negative / Neutral
    Explanation: short explanation

    Review: {review}
    """

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(prompt)

    return response.text.strip()


# ---------------------------------------------------------
# TEXTBLOB SENTIMENT FUNCTION
# ---------------------------------------------------------
def analyze_textblob_sentiment(review):
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0.1:
        label = "Positive"
    elif polarity < -0.1:
        label = "Negative"
    else:
        label = "Neutral"

    return polarity, subjectivity, label


# ---------------------------------------------------------
# STREAMLIT UI
# ---------------------------------------------------------
st.set_page_config(page_title="Smartwatch Sentiment Analyzer", page_icon="⌚")

st.title("⌚ Smartwatch Sentiment Analyzer")
st.subheader("TextBlob NLP + Gemini GEN-AI Version")

tabs = st.tabs(["🔹 Basic Sentiment (TextBlob)", "🔹 Advanced Sentiment (Gemini AI)"])


# =========================================================
# TAB 1: TEXTBLOB NLP
# =========================================================
with tabs[0]:
    st.header("🔹 Basic Sentiment Analysis (TextBlob)")
    review1 = st.text_area("Enter smartwatch review:", key="tb_review")

    if st.button("Analyze with TextBlob"):
        if not review1.strip():
            st.warning("Please enter a review.")
        else:
            polarity, subjectivity, label = analyze_textblob_sentiment(review1)

            st.subheader("🧠 TextBlob Result")
            if label == "Positive":
                st.success(f"Sentiment: {label}")
            elif label == "Negative":
                st.error(f"Sentiment: {label}")
            else:
                st.info(f"Sentiment: {label}")

            st.write(f"Polarity: `{polarity:.3f}`")
            st.write(f"Subjectivity: `{subjectivity:.3f}`")


# =========================================================
# TAB 2: GEMINI GEN-AI
# =========================================================
with tabs[1]:
    st.header("🔹 Advanced GEN-AI Sentiment (Gemini 1.5 Flash)")
    review2 = st.text_area("Enter smartwatch review:", key="gemini_review")

    if st.button("Analyze with Gemini AI"):
        if not review2.strip():
            st.warning("Please enter a review.")
        else:
            try:
                output = gemini_sentiment(review2)

                st.subheader("🤖 Gemini AI Result")
                st.success(output)

            except Exception as e:
                st.error("🔥 Gemini API Error — Check your API key or model name.")
                st.write(str(e))
