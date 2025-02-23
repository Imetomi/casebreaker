'use client';

import { useCallback, useEffect, useRef, useState } from 'react';
import { Message } from './Message';
import { Input } from './Input';
import { useChat } from '@/hooks/useChat';
import { api } from '@/lib/api';
import type { CaseStudy } from '@/lib/api';
import { CheckpointList } from './CheckpointList';

interface ChatProps {
  sessionId: number;
  initialMessage?: string;
}

export function Chat({ sessionId, initialMessage }: ChatProps) {
  const [caseStudy, setCaseStudy] = useState<CaseStudy | null>(null);
  const [completedCheckpoints, setCompletedCheckpoints] = useState<string[]>([]);

  const updateSessionData = useCallback(async () => {
    try {
      const session = await api.getSession(sessionId);
      setCompletedCheckpoints(session.completed_checkpoints || []);
    } catch (error) {
      console.error('Failed to fetch session:', error);
    }
  }, [sessionId]);

  const { messages, isLoading, error, sendMessage } = useChat({
    sessionId,
    initialMessage,
    onResponseComplete: updateSessionData,
  });

  const messagesEndRef = useRef<HTMLDivElement>(null);
  const chatContainerRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    const fetchInitialData = async () => {
      try {
        const session = await api.getSession(sessionId);
        const [study] = await Promise.all([
          api.getCaseStudy(session.case_study_id),
        ]);
        setCaseStudy(study);
        setCompletedCheckpoints(session.completed_checkpoints || []);
      } catch (error) {
        console.error('Failed to fetch initial data:', error);
      }
    };
    fetchInitialData();
  }, [sessionId]);

  return (
    <div className="flex gap-4">
      {caseStudy?.checkpoints && (
        <CheckpointList
          checkpoints={caseStudy.checkpoints}
          completedCheckpoints={completedCheckpoints}
        />
      )}

      {/* Chat Box */}
      <div 
        className="flex-1 flex flex-col h-[calc(100vh-14rem)] max-h-[700px] bg-white rounded-lg border shadow-sm"
        role="main"
        aria-label="Chat Interface"  
      >
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
    </div>
  );
}
