import React, { useState } from "react";
import axios from "axios";

export default function CsvUpload({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);
    try {
      const res = await axios.post("http://localhost:8000/import-csv/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setMessage(res.data.message);
      if (onUploadSuccess) onUploadSuccess();
    } catch (err) {
      setMessage(err.response?.data?.detail || "Erro ao importar.");
    }
  };

  return (
    <div>
      <input type="file" accept=".csv" onChange={handleFileChange} />
      <button onClick={handleUpload}>Importar CSV</button>
      {message && <p>{message}</p>}
    </div>
  );
} 