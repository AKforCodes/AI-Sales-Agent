"use client";

import React, { useState, useRef, useEffect } from 'react';
import { fetchQuote } from '../lib/api';
import LoadingSpinner from './LoadingSpinner';
import ChatMessage from './ChatMessage';
import toast from 'react-hot-toast';

type Message = {
  sender: 'user' | 'ai';
  text: string;
};

const ChatInterface = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<null | HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;

    const userMessage: Message = { sender: 'user', text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      const response = await fetchQuote(userMessage.text);
      const aiMessage: Message = { sender: 'ai', text: response.natural_language_summary };
      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : "An unknown error occurred.";
      toast.error(`Error: ${errorMessage}`);
      const aiErrorMessage: Message = { sender: 'ai', text: `Sorry, I encountered an error: ${errorMessage}` };
      setMessages((prev) => [...prev, aiErrorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-screen w-full max-w-4xl mx-auto bg-gray-800 shadow-2xl rounded-lg">
      {/* Header */}
      <div className="bg-gray-900 p-4 rounded-t-lg shadow-md">
        <h1 className="text-xl font-bold text-center text-blue-400">AI Sales Agent</h1>
      </div>

      {/* Chat Messages */}
      <div className="flex-1 p-6 overflow-y-auto">
        {messages.length === 0 && !isLoading && (
             <div className="flex justify-center items-center h-full">
                <p className="text-gray-400">Ask me for a product quote to get started!</p>
             </div>
        )}
        {messages.map((msg, index) => (
          <ChatMessage key={index} message={msg} />
        ))}
        {isLoading && (
          <div className="flex justify-start mb-4">
              <div className="max-w-md px-4 py-3 rounded-lg shadow-md bg-gray-700 text-gray-100 rounded-bl-none">
                 <LoadingSpinner />
              </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input Area */}
      <div className="p-4 bg-gray-900 rounded-b-lg">
        <form onSubmit={handleSubmit} className="flex items-center">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask for a quote..."
            className="flex-1 p-3 bg-gray-700 rounded-l-md border-0 focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-100 disabled:opacity-50"
            disabled={isLoading}
          />
          <button
            type="submit"
            className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded-r-md transition duration-300 disabled:bg-blue-800 disabled:cursor-not-allowed"
            disabled={isLoading || !input.trim()}
          >
            Send
          </button>
        </form>
      </div>
    </div>
  );
};

export default ChatInterface;
