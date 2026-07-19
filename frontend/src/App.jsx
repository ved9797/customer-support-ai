import { useState, useRef, useEffect } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const [chat, setChat] = useState([
    {
      sender: "AI",
      text: "👋 Welcome to TechMart AI Support!\n\nI can help you with:\n• Refunds\n• Pricing\n• Technical Issues\n• Product Information\n• Complaints\n\nHow can I help you today?",
    },
  ]);

  const chatBoxRef = useRef(null);

  useEffect(() => {
    if (chatBoxRef.current) {
      chatBoxRef.current.scrollTop = chatBoxRef.current.scrollHeight;
    }
  }, [chat, loading]);

  async function sendMessage() {
    if (message.trim() === "") return;

    const updatedChat = [
      ...chat,
      {
        sender: "You",
        text: message,
      },
    ];

    setChat(updatedChat);
    setLoading(true);

    const userMessage = message;
    setMessage("");

    try {
      const response = await fetch("https://customer-support-ai-m33r.onrender.com/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: userMessage,
        }),
      });

      const data = await response.json();

      setChat([
        ...updatedChat,
        {
          sender: "AI",
          text: data.ai_response,
        },
      ]);
    } catch (error) {
      setChat([
        ...updatedChat,
        {
          sender: "AI",
          text: "❌ Unable to connect to the backend.",
        },
      ]);
    }

    setLoading(false);
  }

  return (
    <div className="app">
      <h1>🤖 TechMart AI Customer Support</h1>

      <p className="subtitle">
        AI-Powered Multi-Agent Customer Support
      </p>

      <div className="chat-box" ref={chatBoxRef}>
        {chat.map((msg, index) => (
          <div
            key={index}
            className={msg.sender === "You" ? "message user" : "message ai"}
          >
            <strong>{msg.sender}:</strong> {msg.text}
          </div>
        ))}

        {loading && (
          <div className="message ai">
            <strong>AI:</strong> 🤖 AI is typing...
          </div>
        )}
      </div>

      <div className="input-area">
        <input
          type="text"
          placeholder="Type your message..."
          value={message}
          disabled={loading}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              sendMessage();
            }
          }}
        />

        <button
          onClick={sendMessage}
          disabled={loading}
        >
          {loading ? "Sending..." : "Send"}
        </button>
      </div>
    </div>
  );
}

export default App;