# 📚 PDF RAG Assistant

An AI-powered **PDF Question Answering Assistant** built using **Retrieval-Augmented Generation (RAG)**.

This project allows users to interact with PDF documents using natural language. The system retrieves relevant information from the document and uses an AI language model to generate contextual answers.

## 🚀 Features

- 📄 PDF document processing
- 🔍 Semantic document search
- 🧠 Retrieval-Augmented Generation (RAG)
- 💬 Natural-language question answering
- 🗂️ Vector-based document retrieval
- ⚡ Interactive Streamlit interface
- 🤖 AI-powered contextual responses
- 🔐 Secure environment-variable configuration

## 🏗️ Project Structure

```text
RAG_PROJECT/
│
├── app.py                  # Streamlit application
├── ingest.py               # PDF ingestion and processing
├── requirements.txt        # Python dependencies
├── data/
│   └── sample.pdf          # Sample PDF document
├── .gitignore              # Git ignored files
└── README.md               # Project documentation
```

## 🔄 How It Works

```text
PDF Document
      ↓
Text Extraction
      ↓
Text Chunking
      ↓
Embedding Generation
      ↓
Vector Database
      ↓
Similarity Search
      ↓
Relevant Context
      ↓
Language Model
      ↓
AI-Generated Answer
```

### RAG Pipeline

1. **Document Loading** – Loads the PDF document.
2. **Text Extraction** – Extracts text from the PDF.
3. **Text Chunking** – Splits the document into smaller sections.
4. **Embedding Generation** – Converts text into vector representations.
5. **Vector Storage** – Stores the embeddings for efficient retrieval.
6. **Similarity Search** – Finds the most relevant document content.
7. **Context Retrieval** – Provides relevant content to the language model.
8. **Response Generation** – Generates an answer based on the retrieved context.

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **LangChain**
- **ChromaDB**
- **PyPDF**
- **Hugging Face**
- **OpenAI / LLM APIs**
- **Python-dotenv**

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/pdf-rag-assistant.git
cd pdf-rag-assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

On Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project directory and add the API credentials required by the application.

Example:

```env
OPENAI_API_KEY=your_api_key_here
HF_TOKEN=your_huggingface_token_here
```

> **Important:** Never upload API keys, passwords, or other secrets to GitHub.

The `.gitignore` file is configured to exclude `.env` and other sensitive/local files.

## ▶️ Running the Application

Run the ingestion process if required:

```bash
python ingest.py
```

Then start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## 🎯 Use Cases

This project can be used for:

- 📚 Academic document analysis
- 📑 Research paper question answering
- 📖 Study material assistance
- 🏢 Internal document search
- 🔎 Semantic document retrieval
- 🤖 AI-powered knowledge assistants

## 🔮 Future Improvements

- Multiple PDF uploads
- Multi-document conversations
- Source and page citations
- Conversation memory
- Improved retrieval and reranking
- Document summarization
- Advanced document analytics
- Cloud deployment
- User authentication

## 👨‍💻 Author

**Shaik Ajhar**

B.Tech Computer Science & Engineering (AI & ML)

Interested in:

**Artificial Intelligence · Machine Learning · Generative AI · LLMs · AI Agents**

---

