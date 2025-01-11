// src/App.js

import React, { useState } from 'react';
import './App.css';

function App() {
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleQuery = async () => {
    try {
      setLoading(true);
      const response = await fetch("http://localhost:8000/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_query: query }),
      });
      const data = await response.json();
      setAnswer(data.answer);
    } catch (err) {
      setAnswer("Error calling the backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <div className="card">
        <h1 className="title">Steves RAG Demo</h1>
        
        <div className="input-container">
          <input
            type="text"
            className="query-input"
            placeholder="Ask a question..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <button
            className="query-button"
            onClick={handleQuery}
            disabled={loading}
          >
            {loading ? "Thinking..." : "Submit"}
          </button>
        </div>

        <div className="answer-section">
          <h2>Answer:</h2>
          <p>{answer}</p>
        </div>
      </div>

      <div className="bottom-image-container">
        <img src="/fun.webp" alt="Fun" className="bottom-image" />
      </div>
    </div>
  );
}

export default App;
