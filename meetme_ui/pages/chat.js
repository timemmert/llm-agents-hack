// ChatComponent.js
import React, { useState } from "react";
import axios from "axios";

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
    try {
      const response = await fetch("http://127.0.0.1:5000/user_input", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ name: "test", message: userInput })
    });

      const data = await response.json()

      // Add chatbot response to chat
      setMessages([...messages, { sender: "bot", text: data.data }]);
    } catch (error) {
      console.error(error);
    }

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
