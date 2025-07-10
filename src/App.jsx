import React, { useState } from "react";
import CsvUpload from "./components/CsvUpload";
import OrcamentoTable from "./components/OrcamentoTable";
// import axios from "axios";

export default function App() {
  const [data, setData] = useState([]);

  const fetchData = async () => {
    // Aqui você pode criar um endpoint no backend para buscar os dados do orçamento
    // Exemplo:
    // const res = await axios.get("http://localhost:8000/orcamento/");
    // setData(res.data);
  };

  return (
    <div>
      <h1>Importação de Orçamento</h1>
      <CsvUpload onUploadSuccess={fetchData} />
      <hr />
      <OrcamentoTable data={data} />
    </div>
  );
} 