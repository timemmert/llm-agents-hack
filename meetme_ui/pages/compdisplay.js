import React from 'react';
import './CompatibilityDisplay.css';

function CompatibilityDisplay({ imageUrl, score, pros, cons, isLoading }) {
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
      <div className="score-display">Compatibility Score: {score}</div>
      <div className="list-container">
        <div className="pros">
          <h3>Pros</h3>
          <ul>
            {pros.map((pro, index) => (
              <li key={index}>{pro}</li>
            ))}
          </ul>
        </div>
        <div className="cons">
          <h3>Cons</h3>
          <ul>
            {cons.map((con, index) => (
              <li key={index}>{con}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

export default CompatibilityDisplay;
