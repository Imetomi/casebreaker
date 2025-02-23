'use client';

import { useEffect, useRef } from 'react';
import { Message } from './Message';
import { Input } from './Input';
import { useChat } from '@/hooks/useChat';

interface ChatProps {
  sessionId: number;
  checkpointId: string;
  initialMessage?: string;
}

export function Chat({ sessionId, checkpointId, initialMessage }: ChatProps) {
  const { messages, isLoading, error, sendMessage } = useChat({
    sessionId,
    checkpointId,
    initialMessage,
  });

  const messagesEndRef = useRef<HTMLDivElement>(null);
  const chatContainerRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  return (
    <div className="flex flex-col h-[calc(100vh-14rem)] max-h-[700px] bg-white rounded-lg border shadow-sm">
      <div className="flex-1 overflow-y-auto p-4" ref={chatContainerRef}>
        <div className="space-y-6">
          {error && (
            <div className="p-4 bg-red-50 text-red-700 rounded-lg">
              {error}
            </div>
          )}
          {messages.map((message, index) => (
            <Message 
              key={index} 
              content={message.content}
              isUser={message.role === 'user'}
            />
          ))}          
          <div ref={messagesEndRef} />
        </div>
      </div>
      
      <div className="border-t p-4 bg-white">
        <Input onSend={sendMessage} disabled={isLoading} />
      </div>
    </div>
  );
}
