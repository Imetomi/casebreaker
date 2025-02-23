'use client';

import { useEffect, useRef, useState } from 'react';
import { Message } from './Message';
import { Input } from './Input';
import { useChat } from '@/hooks/useChat';
import { api } from '@/lib/api';
import type { CaseStudy } from '@/lib/api';
import * as Checkbox from '@radix-ui/react-checkbox';
import { CheckIcon } from '@radix-ui/react-icons';

interface ChatProps {
  sessionId: number;
  checkpointId: string;
  initialMessage?: string;
}

export function Chat({ sessionId, checkpointId, initialMessage }: ChatProps) {
  const [caseStudy, setCaseStudy] = useState<CaseStudy | null>(null);
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

  useEffect(() => {
    const fetchCaseStudy = async () => {
      try {
        const session = await api.getSession(sessionId);
        const study = await api.getCaseStudy(session.case_study_id);
        setCaseStudy(study);
      } catch (error) {
        console.error('Failed to fetch case study:', error);
      }
    };
    fetchCaseStudy();
  }, [sessionId]);

  return (
    <div className="flex gap-4">
      {/* Checkpoints Box */}
      <div className="w-56 h-fit bg-white rounded-lg border shadow-sm p-4 space-y-4">
        <h3 className="font-semibold">Checkpoints</h3>
        {caseStudy?.checkpoints && (
          <div className="space-y-3">
            {caseStudy.checkpoints.map((checkpoint) => (
              <div 
                key={checkpoint.id}
                className="flex items-start gap-2"
              >
                <Checkbox.Root
                  className="h-5 w-5 rounded border border-gray-300 flex items-center justify-center bg-white"
                  checked={checkpoint.id === checkpointId}
                  disabled
                >
                  <Checkbox.Indicator>
                    <CheckIcon className="h-4 w-4 text-blue-600" />
                  </Checkbox.Indicator>
                </Checkbox.Root>
                <label className="text-sm leading-none pt-0.5">
                  {checkpoint.title}
                </label>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Chat Box */}
      <div className="flex-1 flex flex-col h-[calc(100vh-14rem)] max-h-[700px] bg-white rounded-lg border shadow-sm">
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
