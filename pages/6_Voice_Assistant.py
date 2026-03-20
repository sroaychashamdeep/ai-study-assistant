import streamlit as st
from utils.ai_service import ask_ai

st.set_page_config(page_title="Voice Assistant", page_icon="🎤")

st.title("🎤 Voice Assistant")

st.warning("⚠ Voice feature is not supported in Streamlit Cloud.")

user_input = st.text_input("Type your question")

if st.button("Ask AI"):
    if not user_input.strip():
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            response = ask_ai(user_input)

        st.write(response)