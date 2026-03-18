import streamlit as st

st.warning("🎤 Voice feature not supported in cloud deployment")
from streamlit_mic_recorder import mic_recorder

from utils.speech_to_text import speech_to_text
from utils.speech import speak
from utils.ai_service import ask_ai


st.title("🎤 AI Voice Assistant")

st.markdown(
"""
Speak directly to your **AI Study Assistant**.

Steps:
1️⃣ Click the microphone  
2️⃣ Speak your question  
3️⃣ AI will answer with **text + voice**
"""
)

audio = mic_recorder(
    start_prompt="🎙 Start Recording",
    stop_prompt="⏹ Stop Recording",
    just_once=True,
    use_container_width=True
)

if audio:

    st.audio(audio["bytes"])

    with st.spinner("Converting speech to text..."):

        question = speech_to_text(audio["bytes"])

    st.subheader("You said")

    st.write(question)

    with st.spinner("AI thinking..."):

        response = ask_ai(question)

    st.subheader("AI Response")

    st.write(response)

    voice = speak(response)

    st.audio(voice)