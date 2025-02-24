'use client';

import { useCallback, useEffect, useRef, useState } from 'react';
import { Message } from './Message';
import { Input } from './Input';
import { useChat } from '@/hooks/useChat';
import { api } from '@/lib/api';
import type { CaseStudy } from '@/lib/api';
import { CheckpointList } from './CheckpointList';
import { ContextView } from './ContextView';
import { Button, Flex } from '@radix-ui/themes';
import { MessageSquare, BookOpen } from 'lucide-react';

interface ChatProps {
  sessionId: number;
  initialMessage?: string;
}

export function Chat({ sessionId, initialMessage }: ChatProps) {
  const [view, setView] = useState<'chat' | 'context'>('chat');
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
        console.log('Session:', session);
        const [study] = await Promise.all([
          api.getCaseStudy(session.case_study_id),
        ]);
        console.log('Fetched case study:', study);
        console.log('Context materials:', study.contextMaterials);
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
      <div>
        <Flex gap="2" mb="4" justify="center">
          <Button
            variant={view === 'chat' ? 'solid' : 'surface'}
            onClick={() => setView('chat')}
          >
            <MessageSquare className="w-4 h-4" />
            Chat
          </Button>
          <Button
            variant={view === 'context' ? 'solid' : 'surface'}
            onClick={() => {
              console.log('Switching to context view');
              setView('context');
            }}
          >
            <BookOpen className="w-4 h-4" />
            Context
          </Button>
        </Flex>

        {caseStudy?.checkpoints && (
          <CheckpointList
            checkpoints={caseStudy.checkpoints}
            completedCheckpoints={completedCheckpoints}
          />
        )}
      </div>

      <div className="flex-1">
        {view === 'chat' ? (
          <div 
            className="flex flex-col h-[calc(100vh-14rem)] max-h-[700px] bg-white rounded-lg border shadow-sm overflow-hidden"
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
        ) : (
          <>
            {!caseStudy && <div className="text-center p-4">Loading case study...</div>}
            {caseStudy && (
              <>
                {console.log('Rendering ContextView with:', caseStudy)}
                <ContextView caseStudy={caseStudy} />
              </>
            )}
          </>
        )}
      </div>
    </div>
  );
}
