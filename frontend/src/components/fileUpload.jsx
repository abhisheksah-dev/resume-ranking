import React, { useState } from "react";
import "./FileUpload.css"; // Import the CSS file for styling

const FileUpload = ({ onUploadComplete }) => {
  const [files, setFiles] = useState([]);

  const handleFileChange = (e) => {
    // Convert the FileList to an array and update state
    setFiles(Array.from(e.target.files));
  };

  const handleUpload = async () => {
    const formData = new FormData();
    files.forEach((file) => {
      formData.append("files", file);
    });

    try {
      const response = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      onUploadComplete(data);
    } catch (error) {
      console.error("Upload error:", error);
      alert("Error uploading files.");
    }
  };

  return (
    <div className="upload-container">
      <h2>Upload Your Resumes</h2>
      <div className="file-input-wrapper">
        <input
          type="file"
          multiple
          onChange={handleFileChange}
          className="file-input"
        />
      </div>
      <button onClick={handleUpload} className="upload-button">
        Upload and Evaluate
      </button>
    </div>
  );
};

export default FileUpload;
