import streamlit as st
import sys

# Fix module cache issue
sys.modules.pop("utils.ai_service", None)

from utils.auth import login
from utils.streak import update_streak
from utils.ai_service import ask_ai


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖",
    layout="wide"
)


# ---------------- CUSTOM UI (PRO DESIGN) ----------------

st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}

h1, h2, h3 {
    color: #00ADB5;
}

.stTextInput input {
    background-color: #262730;
    color: white;
    border-radius: 8px;
}

.stButton>button {
    background-color: #00ADB5;
    color: white;
    border-radius: 10px;
    padding: 8px 16px;
}

.stSidebar {
    background-color: #111827;
}

.card {
    background-color: #1e1e2f;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)


# ---------------- LOGIN SYSTEM ----------------

if "user" not in st.session_state:
    login()
    st.stop()


# ---------------- HEADER ----------------

col1, col2 = st.columns([8, 2])

with col1:
    st.title("🤖 AI Study Assistant")

with col2:
    st.markdown(f"👤 **{st.session_state.user}**")

    if st.button("Logout"):
        del st.session_state["user"]
        st.rerun()


# ---------------- SIDEBAR ----------------

st.sidebar.title("🚀 AI Study Assistant")

st.sidebar.markdown("### 🔥 Study Streak")
streak = update_streak(st.session_state.user)
st.sidebar.write(f"**{streak} days**")

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 📚 Tools

💬 Chat  
📄 PDF Assistant  
🧠 AI Tools  
🤖 Study Agent  
📊 Dashboard  
📸 Image AI  
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### ⚙ System")
st.sidebar.write("Model:", "Gemini 3.1 Preview")


# ---------------- HERO SECTION ----------------

st.markdown("""
<div class="card">
<h2>🚀 Welcome to AI Study Assistant</h2>
<p>Your all-in-one AI-powered learning platform.</p>
</div>
""", unsafe_allow_html=True)


# ---------------- FEATURES ----------------

st.subheader("✨ Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
<div class="card">
<h3>📚 Study Tools</h3>
<ul>
<li>Ask AI questions</li>
<li>Generate quizzes</li>
<li>Create flashcards</li>
<li>Build study plans</li>
<li>Summarize documents</li>
</ul>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="card">
<h3>🤖 AI Features</h3>
<ul>
<li>Chat with AI tutor</li>
<li>Upload PDFs for answers</li>
<li>Image analysis (AI Vision)</li>
<li>Voice assistant (local)</li>
<li>Autonomous study agent</li>
</ul>
</div>
""", unsafe_allow_html=True)


# ---------------- QUICK AI TEST ----------------

st.markdown("---")
st.subheader("⚡ Quick AI Test")

question = st.text_input("Ask something instantly...")

if st.button("Ask AI"):
    if not question.strip():
        st.warning("⚠ Please enter a question")
    else:
        with st.spinner("🤖 AI thinking..."):
            response = ask_ai(question)

        st.success("✅ Response")
        st.write(response)


# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown("""
<center>
Made with ❤️ using <b>Streamlit + Gemini AI + LangChain</b>
</center>
""", unsafe_allow_html=True)