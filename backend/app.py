from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import PyPDF2

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin requests

@app.route('/')
def home():
    return "Welcome to the Resume Screening API", 200

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

# --- ATS Scoring and Explanation Functions ---
def evaluate_resume(text):
    # Define ATS keywords (customize this list as needed)
    ats_keywords = ["python", "machine learning", "data analysis", "react", "javascript"]
    score = 0
    keyword_counts = {}
    for keyword in ats_keywords:
        count = text.lower().count(keyword.lower())
        keyword_counts[keyword] = count
        score += count * 10  # 10 points per occurrence; adjust as needed
    return score, keyword_counts

def generate_explanation(keyword_counts):
    suggestions = []
    for keyword, count in keyword_counts.items():
        if count == 0:
            suggestions.append(f"Your resume is missing '{keyword}'.")
        elif count < 2:
            suggestions.append(f"Consider including more details about '{keyword}'.")
    if not suggestions:
        return "Your resume appears well-optimized for ATS."
    else:
        return " ".join(suggestions)

# --- API Endpoint to Handle File Upload, Ranking, and Explanation ---
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
        score, keyword_counts = evaluate_resume(text)
        explanation = generate_explanation(keyword_counts)
        results.append({
            "filename": filename,
            "score": score,
            "explanation": explanation
        })

    # Sort the results by score (highest score first)
    results.sort(key=lambda x: x["score"], reverse=True)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
