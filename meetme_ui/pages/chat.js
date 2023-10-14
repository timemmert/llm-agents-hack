// ChatComponent.js
import React, { useState } from "react";

const ChatComponent = () => {
  const [messages, setMessages] = 
  useState([{ sender: "bot", text: "Tell me about yourself." }]);
  const [userInput, setUserInput] = useState("");

  const handleInputChange = (e) => {
    setUserInput(e.target.value);
  };

  const handleSubmit = async () => {
    if (userInput.trim() === "") return;
  
    // Add user message to chat
    setMessages([...messages, { sender: "user", text: userInput }]);
  
    const response = await fetch("http://localhost:5000/send_message", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: userInput }),
    });
  
    const data = await response.json();
  
    // Add server response to chat
    setMessages(prev => [...prev, { sender: "bot", text: data.response }]);
    setUserInput("");
  };
  

  return (
    <div className="chat-container">
      <div className="chat-display">
        {messages.map((message, index) => (
          <div key={index} className={`chat-message ${message.sender}`}>
            {message.text}
          </div>
        ))}
      </div>
      <div className="chat-input">
        <input
          type="text"
          value={userInput}
          onChange={handleInputChange}
          placeholder="Type a message..."
        />
        <button onClick={handleSubmit}>Send</button>
      </div>
    </div>
  );
};

export default ChatComponent;
