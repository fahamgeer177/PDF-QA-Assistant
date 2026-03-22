# PDF-QA Assistant 📄🤖

Ask questions from your documents (PDF, DOCX, PPTX) using an LLM-powered retrieval pipeline.

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
