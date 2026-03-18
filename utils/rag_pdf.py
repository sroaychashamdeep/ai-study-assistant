from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def create_vector_store(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = FAISS.from_texts(chunks, embeddings)

    return vector_db


def search_pdf(vector_db, question):

    docs = vector_db.similarity_search(question, k=2)

    context = ""

    for doc in docs:
        context += doc.page_content

    return context

