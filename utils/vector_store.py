from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

DB_PATH = "faiss_index"

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def save_vector_store(docs):
    db = FAISS.from_documents(docs, embedding)
    db.save_local(DB_PATH)


def load_vector_store():
    if os.path.exists(DB_PATH):
        return FAISS.load_local(
            DB_PATH,
            embedding,
            allow_dangerous_deserialization=True  # IMPORTANT
        )
    return None