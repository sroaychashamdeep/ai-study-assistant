import streamlit as st
import google.generativeai as genai

from utils.quiz_generator import generate_quiz
from utils.voice_ai import record_voice
from utils.speech import speak
from utils.pdf_reader import read_pdf
from utils.rag_pdf import create_vector_store, search_pdf
from utils.speech_to_text import speech_to_text

# ---------------- CONFIG ----------------

import os
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# load model
@st.cache_resource
def load_model():
    model = genai.GenerativeModel("models/gemini-3.1-flash-lite-preview")
    return model

model = load_model()

# sidebar selector
tool = st.sidebar.selectbox(
    "Select Tool",
    [
        "Dashboard","Ask AI",
        "Chat",
        "PDF Assistant",
        "Image Solver",
        "Quiz Generator",
        "Study Notes",
        "Flashcards",
        "Voice Assistant",
        "Study Planner",
        "Document Summarizer",
        "Exam Preparation"
    ]
)

st.title("AI Study Assistant 🤖")


if "stats" not in st.session_state:
    st.session_state.stats = {
        "questions": 0,
        "pdf_queries": 0,
        "quizzes": 0,
        "notes": 0
    }
    
elif tool == "Dashboard":

    st.subheader("📊 Learning Dashboard")

    stats = st.session_state.stats

    col1, col2 = st.columns(2)

    col1.metric("Questions Asked", stats["questions"])
    col2.metric("PDF Queries", stats["pdf_queries"])

    col1.metric("Quizzes Generated", stats["quizzes"])
    col2.metric("Notes Created", stats["notes"])

    st.bar_chart(stats)
# ---------------- ASK AI ----------------

if tool == "Ask AI":

    question = st.text_input("Ask your question", key="ask_ai_input")

    if st.button("Explain", key="ask_ai_btn") and question:

        with st.spinner("AI is thinking..."):

            response = model.generate_content(
                f"Explain the topic in detail with examples:\n{question}"
            )

        st.markdown(response.text)

        audio_file = speak(response.text)
        st.audio(audio_file)


# ---------------- CHAT ----------------

# ---------------- CHAT ----------------
elif tool == "Chat":

    st.subheader("💬 Chat with AI")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    prompt = st.chat_input("Ask a question", key="chat_prompt")

    if prompt:

        # Save user message
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.write(prompt)

        # Build conversation history
        history = ""
        for msg in st.session_state.messages:
            history += f'{msg["role"]}: {msg["content"]}\n'

        # Generate response with memory
        with st.spinner("AI is thinking..."):
            response = model.generate_content(
                f"""
Conversation history:
{history}

User question:
{prompt}

Answer clearly and helpfully.
"""
            )

        # Save AI response
        st.session_state.messages.append({
            "role": "assistant",
            "content": response.text
        })

        with st.chat_message("assistant"):
            st.write(response.text)
            
            
if st.button("🗑 Clear Chat", key="clear_chat"):
    st.session_state.messages = []
    st.rerun()
            
# ---------------- SAVE CHAT HISTORY ----------------

if tool == "Chat":

    if st.session_state.messages:

        chat_text = ""

        for msg in st.session_state.messages:
            chat_text += f'{msg["role"].upper()}: {msg["content"]}\n\n'

        st.download_button(
            label="📥 Download Chat History",
            data=chat_text,
            file_name="chat_history.txt",
            mime="text/plain"
        )
        if st.button("🗑 Clear Chat", key="clear_chat"):
            st.session_state.messages = []
            st.rerun()

# ---------------- PDF ASSISTANT ----------------

elif tool == "PDF Assistant":

    uploaded_file = st.file_uploader("Upload PDF", type="pdf", key="pdf_upload")

    if uploaded_file:

        pdf_text = read_pdf(uploaded_file)

        vector_db = create_vector_store(pdf_text)

        pdf_question = st.text_input("Ask about the PDF", key="pdf_question")

        if pdf_question:

            context = search_pdf(vector_db, pdf_question)

            prompt = f"""
Use the context below to answer the question.

Context:
{context}

Question:
{pdf_question}
"""

            response = model.generate_content(prompt)

            st.markdown(response.text)


# ---------------- IMAGE SOLVER ----------------

elif tool == "Image Solver":

    image_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"], key="image_upload")

    if image_file:

        image_bytes = image_file.read()

        response = model.generate_content([
            "Explain the question in this image and solve it.",
            {"mime_type": "image/jpeg", "data": image_bytes}
        ])

        st.markdown(response.text)


# ---------------- QUIZ ----------------

elif tool == "Quiz Generator":

    topic = st.text_input("Quiz topic", key="quiz_topic")

    if st.button("Generate Quiz", key="quiz_btn") and topic:

        quiz = generate_quiz(topic, model)

        st.write(quiz)


# ---------------- NOTES ----------------

elif tool == "Study Notes":

    notes_topic = st.text_input("Enter topic", key="notes_topic")

    if st.button("Generate Notes", key="notes_btn") and notes_topic:

        prompt = f"""
Create structured study notes for {notes_topic}
Include definition, explanation, examples and summary.
"""

        response = model.generate_content(prompt)

        st.markdown(response.text)


# ---------------- FLASHCARDS ----------------

elif tool == "Flashcards":

    flash_topic = st.text_input("Topic", key="flash_topic")

    if st.button("Generate Flashcards", key="flash_btn") and flash_topic:

        response = model.generate_content(
            f"Create 5 flashcards for {flash_topic}"
        )

        st.markdown(response.text)
        
# ---------------- VOICE ASSISTANT ----------------

elif tool == "Voice Assistant":

    st.subheader("🎤 Ask by Voice")

    audio = record_voice()

    if len(audio) > 0:

        st.audio(audio.export().read())

        question = speech_to_text(audio)

        st.write("You said:", question)

        response = model.generate_content(question)

        st.markdown(response.text)

        audio_file = speak(response.text)

        st.audio(audio_file)
# ---------------- STUDY PLANNER ----------------

elif tool == "Study Planner":

    st.subheader("📅 AI Study Planner")

    subject = st.text_input("Enter subject or topic", key="planner_subject")

    days = st.number_input(
        "How many days until exam?",
        min_value=1,
        max_value=60,
        value=7
    )

    if st.button("Generate Study Plan", key="planner_button"):

        with st.spinner("Creating study plan..."):

            prompt = f"""
Create a daily study plan for the subject: {subject}.

The student has {days} days before the exam.

Provide:
- A clear day-by-day schedule
- Topics to study each day
- Final revision day
"""

            response = model.generate_content(prompt)

        st.markdown(response.text)
        
# ---------------- DOCUMENT SUMMARIZER ----------------

elif tool == "Document Summarizer":

    st.subheader("📚 AI Document Summarizer")

    uploaded_file = st.file_uploader(
        "Upload notes or PDF",
        type=["pdf", "txt"],
        key="summary_upload"
    )

    if uploaded_file:

        text = ""

        if uploaded_file.type == "application/pdf":
            text = read_pdf(uploaded_file)

        else:
            text = uploaded_file.read().decode("utf-8")

        with st.spinner("Analyzing document..."):

            prompt = f"""
Analyze the following study material and provide:

1. A short summary
2. Key points
3. Important exam questions

Document:
{text[:4000]}
"""

            response = model.generate_content(prompt)

        st.markdown(response.text)

# ---------------- EXAM PREPARATION ----------------

elif tool == "Exam Preparation":

    st.subheader("🎓 AI Exam Preparation Mode")

    subject = st.text_input("Enter subject", key="exam_subject")

    days = st.number_input(
        "Days before exam",
        min_value=1,
        max_value=60,
        value=7
    )

    difficulty = st.selectbox(
        "Difficulty level",
        ["Easy", "Medium", "Hard"]
    )

    if st.button("Generate Preparation Plan", key="exam_plan_btn"):

        with st.spinner("Creating exam plan..."):

            prompt = f"""
Create an exam preparation plan.

Subject: {subject}
Days remaining: {days}
Difficulty level: {difficulty}

Provide:
- Day by day schedule
- Topics to study
- Practice suggestions
- Final revision plan
"""

            response = model.generate_content(prompt)

        st.markdown(response.text)