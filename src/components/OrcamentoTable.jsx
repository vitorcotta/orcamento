import React from "react";

export default function OrcamentoTable({ data }) {
  if (!data || data.length === 0) return <p>Nenhum dado importado.</p>;
  return (
    <table border="1">
      <thead>
        <tr>
          {Object.keys(data[0]).map((col) => (
            <th key={col}>{col}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((row, idx) => (
          <tr key={idx}>
            {Object.values(row).map((val, i) => (
              <td key={i}>{val}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
} 