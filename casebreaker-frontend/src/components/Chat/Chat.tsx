'use client';

import { useEffect, useRef, useState } from 'react';
import { Message } from './Message';
import { Input } from './Input';

interface ChatMessage {
  content: string;
  isUser: boolean;
}

interface ChatProps {
  initialMessage?: string;
}

export function Chat({ initialMessage }: ChatProps) {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const chatContainerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (initialMessage) {
      setMessages([
        {
          content: initialMessage,
          isUser: false,
        },
      ]);
    }
  }, [initialMessage]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async (content: string) => {
    const userMessage: ChatMessage = {
      content,
      isUser: true,
    };
    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);

    // Simulate AI response
    setTimeout(() => {
      const aiMessage: ChatMessage = {
        content: 'This is a simulated response. The backend integration is not yet implemented.',
        isUser: false,
      };
      setMessages((prev) => [...prev, aiMessage]);
      setIsLoading(false);
    }, 1000);
  };

  return (
    <div className="flex flex-col h-[calc(100vh-14rem)] max-h-[700px] bg-white rounded-lg border shadow-sm">
      <div className="flex-1 overflow-y-auto p-4" ref={chatContainerRef}>
        <div className="space-y-6">
          {messages.map((message, index) => (
            <Message key={index} {...message} />
          ))}
          {isLoading && (
            <div className="flex justify-start">
              <div className="flex space-x-2 p-4 bg-gray-100 rounded-lg">
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>
      </div>
      
      <div className="border-t p-4 bg-white">
        <Input onSend={handleSend} disabled={isLoading} />
      </div>
    </div>
  );
}
