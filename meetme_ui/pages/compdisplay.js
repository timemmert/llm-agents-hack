import React from 'react';
import { useEffect, useState } from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';

function CompatibilityDisplay() {
  const [isLoading, setIsLoading] = useState(true);
  const [convo_result, setConvoResult] = useState({name: "", score: 0, pros: [], cons: []});
  const call_backend = async () => {
    try {
      const queryParams = new URLSearchParams(window.location.search);
      const name = queryParams.get("name");
      const response = await fetch("http://127.0.0.1:5000/run_convos", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ name: name })
    });

      const data = await response.json()
      setConvoResult({ name: data.data.name_of_match, score: data.data.score, pros: data.data.reasons_for, cons: data.data.reasons_against});
      setIsLoading(false);
    } catch (error) {
      console.error(error);
    }
  }
  useEffect(() => {call_backend()}, [])
  if (isLoading) {
    return (
      <div className="compatibility-container">
        <div className="loader"></div>
      </div>
    );
  }

  return (
    <div className="compatibility-container">
      <h1>Your best match is {convo_result.name}</h1>
      <div className="score-display">Compatibility Score: {convo_result.score}</div>
      <div className="list-container">
        <div className="pros">
          <h3>Pros</h3>
          <ul>
            {convo_result.pros.map((pro, index) => (
              <li key={index}>{pro}</li>
            ))}
          </ul>
        </div>
        <div className="cons">
          <h3>Cons</h3>
          <ul>
            {convo_result.cons.map((con, index) => (
              <li key={index}>{con}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

export default CompatibilityDisplay;