
Tweet Generator App
A simple Streamlit app that generates short, creative tweets on any topic using Google Gemini (via LangChain). Tweets are concise, respectful, and suitable for all audiences.

Features
Generates up to 10 tweets on any topic you enter.

Each tweet is a maximum of 15 words.

Ensures content remains appropriate for all ages.

Clean and user-friendly Streamlit interface.

Requirements
Python 3.8+

Streamlit

LangChain

langchain-google-genai

Google Gemini API Key

Getting Started
Clone this repository (if applicable) or copy the code.

Install Dependencies:

bash
pip install streamlit langchain langchain-google-genai
Set your Google Gemini API Key:

Replace the placeholder in the code

python
os.environ["GOOGLE_API_KEY"] = "YOUR_GEMINI_API_KEY"
Alternatively, set the environment variable in your terminal:

bash
export GOOGLE_API_KEY=your_api_key_here
Run the app:

bash
streamlit run tweet_generator.py
Use the App:

Enter a topic (e.g., "AI in education").

Select the number of tweets (1-10).

Click "Generate Tweets" and view results instantly.

Example
Topic: AI in education

Number: 3

Output (sample):

🟦 AI is transforming classrooms, making learning fun and accessible for all.

🟦 Personalized education empowers students to learn at their own pace.

🟦 Teachers plus AI equals an unstoppable learning team!

Notes
All tweets are generated using Google Gemini models through LangChain.

The app is designed to avoid offensive or sensitive content, but always review generated outputs.

License
This project is for educational and demonstration purposes. Please comply with Google Gemini's terms of service and never share your API key publicly.
