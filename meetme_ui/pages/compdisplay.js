import React from 'react';
import { useEffect, useState } from 'react';

function CompatibilityDisplay() {
  const [isLoading, setIsLoading] = useState(true);
  const [convo_result, setConvoResult] = useState({score: 0, pros: [], cons: []});
  useEffect(async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/run_convos", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ name: "test", message: userInput })
    });

      const data = await response.json()
      setConvoResult(data.data);
    } catch (error) {
      console.error(error);
    }
  }, [])
  if (isLoading) {
    return (
      <div className="compatibility-container">
        <div className="loader"></div>
      </div>
    );
  }

  return (
    <div className="compatibility-container">
      <img src={imageUrl} alt="Uploaded Image" className="image-display" />
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
