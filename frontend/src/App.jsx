import React, { useState } from "react";
import FileUpload from "./components/FileUpload";

function App() {
  const [results, setResults] = useState([]);

  const handleUploadComplete = (data) => {
    setResults(data);
  };

  return (
    <div className="App">
      <h1>Resume Screening & Ranking</h1>
      <FileUpload onUploadComplete={handleUploadComplete} />
      <h2>Results:</h2>
      <ul>
        {results.map((result, index) => (
          <li key={index}>
            {result.filename} - Score: {result.score}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
