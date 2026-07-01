# 📄 Secure PDF QA Assistant: Robust RAG Architecture

A Retrieval-Augmented Generation (RAG) system designed to securely process complex documents, evaluate factual grounding, and mitigate hallucinations in Large Language Models (LLMs). 

This project serves as a foundational architecture for researching retrieval robustness, context-bounding, and safe knowledge extraction in generative AI systems.

## 🛡️ AI Safety & Retrieval Robustness

Standard LLMs are prone to factual hallucinations and relying on their pre-trained parametric memory instead of provided context. This pipeline implements critical safety guardrails to ensure reliable and auditable information retrieval:

*   **Factual Grounding (Parametric Memory Override):** The system is engineered to strictly bound the LLM's response to the retrieved vector context. It actively suppresses the model's pre-trained knowledge to prevent out-of-context hallucinations.
*   **Deterministic Abstention:** Implements strict negative-constraint prompting. If the retrieved document chunks do not contain the answer to the user's query, the system is forced to abstain (e.g., "The provided document does not contain information to answer this question") rather than guessing.
*   **Context Traceability:** By chunking and embedding specific PDF segments, every generated answer can be traced back to its exact source within the document, ensuring high auditability and transparency.
*   **Data Privacy & Poisoning Defense:** Documents are processed securely within the local environment/vector store, ensuring sensitive data is not leaked into global training pipelines, while protecting the retrieval corpus from external data poisoning.

## ⚙️ System Architecture

The pipeline processes unstructured data into a secure, queryable state machine:
1.  **Document Ingestion & Chunking:** Unstructured PDF text is extracted and algorithmically chunked to preserve semantic context without exceeding embedding window limits.
2.  **Vector Embeddings:** Text chunks are converted into dense vector representations and stored in an optimized vector database for high-dimensional similarity search.
3.  **Semantic Retrieval:** User queries are embedded and matched against the local vector store to retrieve only the top-$K$ most relevant, high-fidelity context blocks.
4.  **Constrained Generation:** The LLM synthesizes an answer using *only* the retrieved context, governed by safety-focused system prompts.

https://github.com/user-attachments/assets/67bf631d-6258-43b4-8930-a36a940843d4

## ✨ Features

- 📤 Upload and process documents from a clean web UI
- 🧠 Ask natural language questions about uploaded content
- 🔎 Retrieval-augmented answers using LangChain + Chroma
- 📚 Supports `PDF`, `DOCX`, and `PPTX`
- 🌐 Flask backend with simple HTML frontend

## 🗂️ Project Structure

```text
PDF-QA/
├── app.py
├── document_qa.py
├── frontend.html
├── requirements.txt
├── README.md
└── uploads/
```

## 🧰 Tech Stack

- Python
- Flask + Flask-CORS
- LangChain
- Chroma Vector Store
- OpenAI API
- python-docx / python-pptx / pypdf

## 🚀 Quick Start

### 1) Clone the repository

```bash
git clone <your-repo-url>
cd PDF-QA
```

### 2) Create and activate a virtual environment

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Set your OpenAI API key

Windows (PowerShell):

```powershell
$env:OPENAI_API_KEY="your_openai_api_key_here"
```

macOS/Linux:

```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

### 5) Run the app

```bash
python app.py
```

Open your browser at:

```text
http://127.0.0.1:5000
```

## 🧪 How To Use

1. Upload a supported document.
2. Wait for processing confirmation.
3. Ask your question in the input box.
4. Read the generated answer.

## 🔐 Security Notes

- Never hardcode API keys in source files.
- Use environment variables for secrets.
- Keep `.env` files and local caches out of Git.

## 📌 Supported File Types

- `.pdf`
- `.docx`
- `.pptx`

## 🛠️ Troubleshooting

- If you get API key errors, re-check `OPENAI_API_KEY`.
- If a file fails to process, verify extension and file integrity.
- If dependency install fails, upgrade `pip` and retry:

```bash
python -m pip install --upgrade pip
```

## 🙌 Contributing

Pull requests and improvements are welcome. Feel free to fork and enhance this project.

## 📄 License

MIT

---

Made with curiosity, code, and coffee ☕💡
