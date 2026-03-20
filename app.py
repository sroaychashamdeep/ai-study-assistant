import streamlit as st
import sys
sys.modules.pop("utils.ai_service", None)

from utils.auth import login
from utils.streak import update_streak
from utils.ai_service import ask_ai   # ✅ use centralized AI


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖",
    layout="wide"
)


# ---------------- LOGIN SYSTEM ----------------

if "user" not in st.session_state:
    login()
    st.stop()


# ---------------- HEADER ----------------

col1, col2 = st.columns([8, 2])

with col1:
    st.title("🤖 AI Study Assistant")

with col2:
    st.write("👤", st.session_state.user)

    if st.button("Logout"):
        del st.session_state["user"]
        st.rerun()


# ---------------- DESCRIPTION ----------------

st.markdown("""
Welcome to your **AI Learning Platform**.

Use the **sidebar to open tools** like:

- 💬 AI Chat  
- 📄 PDF Assistant  
- 🧠 Quiz Generator  
- 🎤 Voice Assistant  
- 📚 Study Agent  
- 📊 Learning Dashboard  
""")


# ---------------- STUDY STREAK ----------------

streak = update_streak(st.session_state.user)

st.sidebar.markdown("### 🔥 Study Streak")
st.sidebar.write(f"**{streak} days**")


# ---------------- NAVIGATION ----------------

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 📚 Available Tools

💬 Chat  
📄 PDF Assistant  
🧠 AI Tools  
🤖 Study Agent  
📊 Dashboard  
""")


# ---------------- SYSTEM STATUS ----------------

st.sidebar.markdown("---")

st.sidebar.markdown("### ⚙ System")
st.sidebar.write("AI Model:", "gemini-3.1-flash-lite-preview")


# ---------------- HOME PAGE ----------------

st.markdown("---")
st.subheader("🚀 What You Can Do")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📚 Study Tools
    - Ask AI questions  
    - Generate quizzes  
    - Create flashcards  
    - Build study plans  
    - Summarize documents  
    """)

with col2:
    st.markdown("""
    ### 🤖 AI Features
    - Chat with AI tutor  
    - Upload PDFs for answers  
    - Voice learning assistant  
    - Autonomous study agent  
    """)


# ---------------- QUICK AI TEST ----------------

st.markdown("---")
st.subheader("⚡ Quick AI Test")

question = st.text_input("Ask something quickly")

if st.button("Ask AI"):
    if question.strip() == "":
        st.warning("Please enter a question")
    else:
        with st.spinner("AI thinking..."):
            response = ask_ai(question)

        st.write(response)


# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown("""
Built with ❤️ using:

- **Streamlit**
- **Google Gemini AI**
- **LangChain**
- **FAISS Vector Search**
""")