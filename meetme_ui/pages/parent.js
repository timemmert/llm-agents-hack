import React, { useState, useEffect } from 'react';
import CompatibilityDisplay from './CompatibilityDisplay';

function App() {
  const [isLoading, setIsLoading] = useState(true); 
  const [data, setData] = useState({});

  useEffect(() => {
    // Mock API call to fetch data
    setTimeout(() => {
      setData({
        imageUrl: "path_to_image.jpg",
        score: "85%",
        pros: ["Pro 1", "Pro 2", "Pro 3"],
        cons: ["Con 1", "Con 2"]
      });
      setIsLoading(false);
    }, 2000); // Delaying by 2 seconds to simulate data fetching
  }, []);

  return (
    <div className="App">
      <CompatibilityDisplay 
        imageUrl={data.imageUrl} 
        score={data.score} 
        pros={data.pros} 
        cons={data.cons} 
        isLoading={isLoading}
      />
    </div>
  );
}

export default App;
