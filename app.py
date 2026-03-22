from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

# Import your existing logic from document_qa.py
from document_qa import init_llm, process_document, process_prompt, reset_document_processing, process_new_document

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Initialize model once
init_llm()

@app.route('/')
def serve_frontend():
    return send_from_directory('.', 'frontend.html')

@app.route('/upload-document', methods=['POST'])
def upload_document():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty file name'}), 400

    upload_dir = 'uploads'
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, file.filename)
    file.save(file_path)

    try:
        # Process the newly uploaded document
        process_new_document(file_path)
        return "Document uploaded and processed", 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty file name'}), 400

    upload_dir = 'uploads'
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, file.filename)
    file.save(file_path)

    try:
        # Process the uploaded document
        process_new_document(file_path)
        return jsonify({'message': 'File processed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question', '')
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    try:
        answer = process_prompt(question)
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/reset-document', methods=['POST'])
def reset_document():
    reset_document_processing()  # Reset data
    return "Document processing reset", 200

@app.route('/list-documents', methods=['GET'])
def list_documents():
    upload_dir = 'uploads'
    os.makedirs(upload_dir, exist_ok=True)
    return jsonify(os.listdir(upload_dir))

if __name__ == '__main__':
    app.run(debug=True)
