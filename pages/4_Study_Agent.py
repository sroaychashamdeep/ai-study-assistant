import streamlit as st

from utils.pdf_reader import read_pdf
from utils.study_agent import generate_study_kit
from utils.ai_service import ask_ai


st.title("🤖 AI Study Agent")

st.write("Upload study material and generate a full learning kit.")

file = st.file_uploader(
    "Upload PDF or text file",
    type=["pdf","txt"]
)

if file:

    if file.type == "application/pdf":
        text = read_pdf(file)

    else:
        text = file.read().decode()

    if st.button("Generate Study Kit"):

        with st.spinner("AI creating study kit..."):

            kit = generate_study_kit(text, ask_ai)

        st.subheader("Summary")
        st.write(kit["summary"])

        st.subheader("Study Notes")
        st.write(kit["notes"])

        st.subheader("Flashcards")
        st.write(kit["flashcards"])

        st.subheader("Quiz")
        st.write(kit["quiz"])

        st.subheader("Exam Questions")
        st.write(kit["exam"])

        st.subheader("Study Plan")
        st.write(kit["plan"])