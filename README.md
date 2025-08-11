Here’s your **final cleaned README** — you can copy-paste it directly into your `README.md` file on GitHub.

````markdown
# 🤖 RAG-Powered Document Chatbot (PDF, Word & More)

A **Retrieval-Augmented Generation (RAG)** chatbot built with **LangChain**, **FAISS**, **HuggingFace embeddings**, and **Ollama**.  
It allows you to **chat with your own documents** (PDF, DOCX, TXT) by creating a searchable vector database and retrieving relevant chunks to answer your questions.

---

## ✨ Features
- 📂 Upload **PDF, DOCX, and TXT** documents
- 🔍 Automatically **split text into chunks** for better search
- 📚 Store document embeddings in a **FAISS vector database**
- 💬 Use **Ollama LLM** (DeepSeek R1 model) for answering questions
- 🛠 **Custom Prompt Template** for concise answers (≤ 250 words)
- ⚡ Quick and interactive **Streamlit** UI

---

## 🛠 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/document-chatbot.git
cd document-chatbot
````

### 2️⃣ Install Dependencies

Make sure you have **Python 3.9+** installed.

```bash
pip install -r requirements.txt
```

### 3️⃣ Install Ollama & Model

* Download and install [Ollama](https://ollama.ai/download)
* Pull the DeepSeek R1 model:

```bash
ollama pull deepseek-r1:1.5b
```

---

## 🚀 Usage

### 1️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

### 2️⃣ Upload Documents

* Supported formats: `.pdf`, `.docx`, `.txt`
* Multiple files can be uploaded at once.

### 3️⃣ Create Vector Store

* Go to the **sidebar** and click **"Create / Update Vector Store"** to process your documents.

### 4️⃣ Ask Questions

* Type your question in the text box and click **"Get Answer"**
* The bot will search relevant chunks and generate an answer.

---

## 📂 Project Structure

```
📁 data/                 # Uploaded documents (auto-created)
📁 faiss_index/          # Vector store (auto-created)
app.py                   # Main Streamlit app
requirements.txt         # Python dependencies
README.md                # Project documentation
```

---

## ⚙️ Configuration

* **Embeddings Model:** `all-MiniLM-L6-v2` (HuggingFace)
* **LLM Model:** `deepseek-r1:1.5b` (Ollama)
* **Chunk Size:** 1000 characters (with 100 overlap)
* **Search Top-K:** 3 chunks

---

## 📌 Requirements

* Python 3.9+
* Streamlit
* LangChain
* HuggingFace Embeddings
* FAISS
* Ollama (with DeepSeek model)

---

## 📜 License

This project is licensed under the **MIT License** —
✅ You can use it freely
✅ You can modify it
✅ You can share it (even for commercial purposes)
📌 Just keep the original license and give credit to the author.

---

## 💡 Future Improvements

* ✅ Add chat history memory
* ✅ Support for more file formats (CSV, HTML, Markdown)
* ✅ Deploy on cloud platforms like **Streamlit Community Cloud** or **Hugging Face Spaces**

---

💙 **Contributions are welcome!** Fork the repo and submit a pull request.

```

Do you want me to **also make a ready `requirements.txt`** so that people can run your chatbot with just one command? That will make your GitHub project complete.
```

