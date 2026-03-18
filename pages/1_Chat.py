import streamlit as st
from google import genai
import time
from utils.database import save_chat

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
MODEL = "gemini-3.1-flash-lite-preview"

st.title("💬 AI Chat")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt=st.chat_input("Ask something")

if prompt:

    st.session_state.messages.append(
        {"role":"user","content":prompt}
    )

    save_chat(st.session_state.user,prompt)

    history=""

    for msg in st.session_state.messages[-6:]:
        history+=msg["content"]

    response=client.models.generate_content(
        model=MODEL,
        contents=history+prompt
    )

    reply=response.text

    st.session_state.messages.append(
        {"role":"assistant","content":reply}
    )

    save_chat(st.session_state.user,reply)

    with st.chat_message("assistant"):
        st.write(reply)