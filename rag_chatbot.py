import os
import streamlit as st
from langchain_community.document_loaders import (PyPDFLoader,Docx2txtLoader,TextLoader)
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

# --- OLLAMA_BASE_URL ---
OLLAMA_BASE_URL = os.getenv("RAG_CHATBOT_OLLAMA_BASE_URL")
print("Using Ollama at:", OLLAMA_BASE_URL)

# --- Embeddings Model ---
embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


# --- Load & Split Documents (PDF, DOCX, TXT) ---
def load_and_split_documents(folder_path="data"):
    docs = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if filename.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        elif filename.endswith(".docx"):
            loader = Docx2txtLoader(file_path)
        elif filename.endswith(".txt"):
            loader = TextLoader(file_path)
        else:
            print(f"❌ Skipped unsupported file: {filename}")
            continue

        docs.extend(loader.load())

    # Split the documents into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    return splitter.split_documents(docs)

# --- Create FAISS Vector Store ---
def create_vector_store(docs):
    db = FAISS.from_documents(docs, embeddings_model)
    db.save_local("faiss_index")

# --- Prompt Template ---
prompt_template = """
Use the provided data to answer the question in less than 250 words. 
If the answer is not found, ask the user to clarify.

<context>
{context}
</context>

Question: {question}

Assistant:
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# --- Load LLM from Ollama ---
def get_ollama_llm():
    return ChatOllama(model="deepseek-r1:1.5b")

# --- Get Answer from Retriever + LLM ---
def get_answer(query):
    if not os.path.exists("faiss_index/index.faiss"):
        return "⚠️ Vector store not found. Please create it first using the sidebar."
    
    db = FAISS.load_local("faiss_index", embeddings_model, allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    qa = RetrievalQA.from_chain_type(
        llm=get_ollama_llm(),
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt}
    )

    return qa.run(query)

# --- Streamlit App ---
def main():
    st.set_page_config(page_title="Chat with Word Docs")
    st.header("🤖 RAG-Powered Document Chatbot (PDF, Word & More)")

    # 📤 Upload PDF, DOCX, or TXT Files
    uploaded_files = st.file_uploader(
        "📤 Upload your document(s) (PDF, DOCX, or TXT)", 
        type=["pdf", "docx", "txt"],
        accept_multiple_files=True
    )

    if uploaded_files:
        os.makedirs("data", exist_ok=True)
        for f in uploaded_files:
            file_path = os.path.join("data", f.name)
            with open(file_path, "wb") as out_file:
                out_file.write(f.getbuffer())

        st.success(f"✅ {len(uploaded_files)} file(s) uploaded successfully.")
    
    # Sidebar for Vector Store
    with st.sidebar:
        st.subheader("⚙️ Vector Store")
        if st.button("Create / Update Vector Store"):
            with st.spinner("🔄 Processing uploaded documents..."):
                docs = load_and_split_documents()
                if docs:
                    create_vector_store(docs)
                    st.success("✅ Vector store updated successfully!")
                else:
                    st.warning("⚠️ No valid Word documents found.")

    # Ask a Question
    query = st.text_input("Ask a question from your documents:")
    if st.button("Get Answer"):
        if not os.path.exists("faiss_index/index.faiss"):
            st.warning("⚠️ Please create the vector store first from the sidebar.")
        elif not query.strip():
            st.warning("❓ Please enter a question.")
        else:
            with st.spinner("Thinking..."):
                try:
                    answer = get_answer(query)
                    st.write(answer)
                    st.success("✅ Answer generated.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")

# Run App
if __name__ == "__main__":
    main()










































