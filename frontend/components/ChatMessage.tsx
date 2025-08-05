import React from 'react';
import ReactMarkdown from 'react-markdown';

interface ChatMessageProps {
  message: {
    sender: 'user' | 'ai';
    text: string;
  };
}

const ChatMessage: React.FC<ChatMessageProps> = ({ message }) => {
  const isUser = message.sender === 'user';

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-4`}>
      <div
        className={`max-w-xl lg:max-w-2xl px-4 py-3 rounded-lg shadow-md ${
          isUser
            ? 'bg-blue-600 text-white rounded-br-none'
            // THE FIX IS HERE: The hyphen before 'bg-gray-700' has been removed.
            : 'bg-gray-700 text-gray-100 rounded-bl-none'
        }`}
      >
        {isUser ? (
          <p>{message.text}</p>
        ) : (
          <article className="prose prose-invert">
            <ReactMarkdown>{message.text}</ReactMarkdown>
          </article>
        )}
      </div>
    </div>
  );
};

export default ChatMessage;
