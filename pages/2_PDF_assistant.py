import streamlit as st
from google import genai
from utils.pdf_reader import read_pdf
from utils.rag_pdf import create_vector_store, search_pdf

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
MODEL="gemini-3.1-flash-lite-preview"

st.title("📄 PDF Assistant")

files=st.file_uploader(
    "Upload PDFs",
    type="pdf",
    accept_multiple_files=True
)

if files:

    text=""

    for file in files:
        text+=read_pdf(file)

    if "vector_db" not in st.session_state:
        st.session_state.vector_db=create_vector_store(text)

    question=st.text_input("Ask about PDFs")

    if question:

        context=search_pdf(
            st.session_state.vector_db,
            question
        )

        response=client.models.generate_content(
            model=MODEL,
            contents=context+question
        )

        st.markdown(response.text)