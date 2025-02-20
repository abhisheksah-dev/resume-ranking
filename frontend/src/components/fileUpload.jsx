import React, { useState } from "react";

const FileUpload = ({ onUploadComplete }) => {
  const [files, setFiles] = useState([]);

  const handleFileChange = (e) => {
    setFiles(e.target.files);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
      formData.append("files", files[i]);
    }

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
    <div>
      <input type="file" multiple onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload and Evaluate</button>
    </div>
  );
};

export default FileUpload;
