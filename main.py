import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Set your Google Gemini API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAEqYZHrYZ9jcsJd-_F992VmANSZdhlIkI"  # 🔁 Replace with your actual key

# Initialize Gemini model
gemini_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

# Define prompt template
tweet_template = """Give me {number} tweets on {topic} in English.
Please follow these instructions:
1. Limit each tweet to a maximum of 15 words.
2. Ensure all content is respectful and appropriate for all audiences.
3. Avoid creating tweets on offensive, controversial, or sensitive topics.
"""

prompt = PromptTemplate(template=tweet_template, input_variables=["number", "topic"])
tweet_chain = prompt | gemini_model

# Streamlit App UI
st.set_page_config(page_title="Tweet Generator", layout="centered")
st.title("🐦Tweet Generator")

# User inputs
topic = st.text_input("Enter a topic", "AI in education")
number = st.slider("How many tweets do you want?", 1, 10, 5)

# Generate tweets on button click
if st.button("Generate Tweets"):
    with st.spinner("Generating tweets..."):
        try:
            result = tweet_chain.invoke({"number": number, "topic": topic})
            st.success("Here are your tweets:")
            
            # Clean & format output
            tweets = result.content.strip().split("\n")
            for tweet in tweets:
                tweet = tweet.strip()
                if tweet:
                    st.write(f"🟦 {tweet}")
        except Exception as e:
            st.error(f"Error: {e}")
