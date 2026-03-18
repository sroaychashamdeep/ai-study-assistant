from google import genai
import streamlit as st

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

MODEL = "gemini-3.1-flash-lite-preview"


def ask_ai(prompt):

    try:

        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        return response.text

    except:

        return "⚠ AI service unavailable"