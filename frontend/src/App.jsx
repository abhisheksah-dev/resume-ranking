import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import "./App.css"; // Import CSS for styling

function App() {
  const [results, setResults] = useState([]);

  const handleUploadComplete = (data) => {
    setResults(data);
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>Resume Screening & Ranking</h1>
      </header>
      <main className="app-main">
        <FileUpload onUploadComplete={handleUploadComplete} />
        <section className="results-section">
          <h2>Results:</h2>
          {results.length === 0 ? (
            <p>No resumes evaluated yet. Please upload your resumes.</p>
          ) : (
            <ul className="results-list">
              {results.map((result, index) => (
                <li key={index} className="result-item">
                  <h3>{result.filename}</h3>
                  <p>
                    <strong>Score:</strong> {result.score}
                  </p>
                  <p>
                    <em>{result.explanation}</em>
                  </p>
                </li>
              ))}
            </ul>
          )}
        </section>
      </main>
      <footer className="app-footer">
        <p>© {new Date().getFullYear()} Resume Screening & Ranking</p>
      </footer>
    </div>
  );
}

export default App;
