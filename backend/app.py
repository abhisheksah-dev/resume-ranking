from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import PyPDF2
import pickle
from dummy_model import DummyModel  # Ensure DummyModel is imported

app = Flask(__name__)            # <-- Create the Flask app instance first
CORS(app)                       # Enable Cross-Origin requests

@app.route('/')                # Now define your routes
def home():
    return "Welcome to the Resume Screening API", 200

# --- Load your pre-trained AI model ---
MODEL_PATH = 'model.pkl'
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
else:
    model = None  # Replace this with your actual model later

# --- Helper Function: Extract Text from PDF ---
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return text

# --- Helper Function: Evaluate Resume using the AI model ---
def evaluate_resume(text):
    # For demonstration, we'll use a dummy evaluation.
    # Replace this with your model's inference logic.
    if model:
        score = model.predict([text])[0]  # Adjust based on your model's API
    else:
        score = len(text) % 100  # Dummy score based on text length
    return score

# --- API Endpoint to Handle File Upload ---
@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('files')
    results = []

    if not files:
        return jsonify({"error": "No files uploaded"}), 400

    # Ensure the uploads folder exists
    os.makedirs("uploads", exist_ok=True)

    for file in files:
        filename = file.filename
        file_path = os.path.join("uploads", filename)
        file.save(file_path)

        text = extract_text_from_pdf(file_path)
        score = evaluate_resume(text)
        results.append({"filename": filename, "score": score})

    # Sort the results by score (highest score first)
    results.sort(key=lambda x: x["score"], reverse=True)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
