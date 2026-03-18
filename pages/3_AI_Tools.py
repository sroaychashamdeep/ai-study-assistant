import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
MODEL="gemini-3.1-flash-lite-preview"

st.title("🧠 AI Tools")

tab1,tab2,tab3=st.tabs(["Notes","Flashcards","Quiz"])

with tab1:

    topic=st.text_input("Topic")

    if st.button("Generate Notes"):

        response=client.models.generate_content(
            model=MODEL,
            contents=f"Create notes for {topic}"
        )

        st.markdown(response.text)

with tab2:

    topic=st.text_input("Flashcard topic")

    if st.button("Generate Flashcards"):

        response=client.models.generate_content(
            model=MODEL,
            contents=f"Create flashcards for {topic}"
        )

        st.markdown(response.text)

with tab3:

    topic=st.text_input("Quiz topic")

    if st.button("Generate Quiz"):

        response=client.models.generate_content(
            model=MODEL,
            contents=f"Create quiz questions for {topic}"
        )

        st.markdown(response.text)