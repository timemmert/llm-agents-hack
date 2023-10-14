// ChatComponent.js
import React, { useState } from "react";

const ChatComponent = () => {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState("");

  const handleInputChange = (e) => {
    setUserInput(e.target.value);
  };

  const handleSubmit = async () => {
    if (userInput.trim() === "") return;

    // Add user message to chat
    setMessages([...messages, { sender: "user", text: userInput }]);

    const response = await fetch("https://your-chatbot-api-url.com", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: userInput }),
    });

    const data = await response.json();

    // Add chatbot response to chat
    setMessages([...messages, { sender: "user", text: userInput }, { sender: "bot", text: data.response }]);

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
