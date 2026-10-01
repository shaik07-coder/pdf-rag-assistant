import streamlit as st

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama


# Page configuration
st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖"
)

# Title
st.title("🤖 RAG Document Chatbot")
st.write("Ask questions about your documents.")


# Load embeddings
@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


# Load vector database
@st.cache_resource
def load_vector_db():
    embeddings = load_embeddings()

    return Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )


# Load Ollama model
@st.cache_resource
def load_llm():
    return ChatOllama(
        model="llama3.2",
        temperature=0
    )


# Initialize
vector_db = load_vector_db()
retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)

llm = load_llm()


# User input
question = st.chat_input("Ask a question about your document...")


if question:

    # Display user message
    with st.chat_message("user"):
        st.write(question)

    # Retrieve documents
    documents = retriever.invoke(question)

    context = "\n\n".join(
        [document.page_content for document in documents]
    )

    # Create prompt
    prompt = f"""
You are a helpful AI assistant.

Answer the user's question using ONLY the information
provided in the context below.

Context:
{context}

Question:
{question}
"""

    # Get response
    response = llm.invoke(prompt)

    # Display AI response
    with st.chat_message("assistant"):
        st.write(response.content)