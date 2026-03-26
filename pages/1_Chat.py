import streamlit as st
from google import genai
import time
from utils.ai_service import stream_response
from utils.database import save_chat

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
MODEL = "gemini-3.1-flash-lite-preview"

st.set_page_config(page_title="AI Chat", page_icon="💬")

st.title("💬 AI Chat Assistant")

# ---------------- USER CHECK ----------------

if "user" not in st.session_state:
    st.warning("Please login first")
    st.stop()

# ---------------- SESSION ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- SIDEBAR ----------------

if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.messages = []

st.sidebar.markdown(f"👤 Logged in as: **{st.session_state.user}**")

# ---------------- DISPLAY CHAT ----------------

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------- INPUT ----------------

prompt = st.chat_input("Ask anything...")

if prompt:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    save_chat(st.session_state.user, prompt)

    # Show user message
    with st.chat_message("user"):
        st.write(prompt)

    # ---------------- CONTEXT ----------------

    history = ""
    for msg in st.session_state.messages[-6:]:
        history += f"{msg['role']}: {msg['content']}\n"

    final_prompt = f"""
You are a helpful AI tutor.

Conversation:
{history}

User: {prompt}
"""

    # ---------------- STREAM RESPONSE ----------------

    with st.chat_message("assistant"):
        response_container = st.empty()
        full_response = ""

        try:
            for chunk in stream_response(final_prompt):
                full_response += chunk
                response_container.markdown(full_response + "▌")

            response_container.markdown(full_response)

        except Exception as e:
            full_response = f"❌ Error: {str(e)}"
            response_container.write(full_response)

    # ---------------- SAVE RESPONSE ----------------

    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response
    })

    save_chat(st.session_state.user, full_response)