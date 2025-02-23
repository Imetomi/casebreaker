import { useCallback, useEffect, useState } from 'react';
import { api } from '@/lib/api';
import { ChatMessage } from '@/lib/api';

export interface UseChatOptions {
  sessionId: number;
  checkpointId: string;
  initialMessage?: string;
}

export function useChat({ sessionId, checkpointId, initialMessage }: UseChatOptions) {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Load existing messages
  useEffect(() => {
    async function loadMessages() {
      try {
        const existingMessages = await api.getMessages(sessionId);
        if (existingMessages.length === 0 && initialMessage) {
          setMessages([{
            role: 'assistant',
            content: initialMessage,
            checkpoint_id: checkpointId
          }]);
        } else {
          setMessages(existingMessages);
        }
      } catch (err) {
        setError('Failed to load messages');
        console.error('Failed to load messages:', err);
      }
    }
    loadMessages();
  }, [sessionId, initialMessage, checkpointId]);

  const sendMessage = useCallback(async (content: string) => {
    try {
      setError(null);

      // Add user message immediately
      const userMessage: ChatMessage = {
        role: 'user',
        content,
        checkpoint_id: checkpointId
      };
      setMessages(prev => [...prev, userMessage]);
      
      // Only set loading while waiting for the stream to start
      setIsLoading(true);

      // Send message and handle streaming response
      const stream = await api.sendMessage(sessionId, content, checkpointId);
      if (!stream) {
        throw new Error('No response stream received');
      }
      
      // Stream started, no need for loading indicator
      setIsLoading(false);

      // Process the stream
      const reader = stream.getReader();
      let assistantMessage = '';
      let currentStatus = 'thinking';

      try {
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
  
          // Convert the chunk to text
          const chunk = new TextDecoder().decode(value);
          const lines = chunk.split('\n');
  
          for (const line of lines) {
            if (line.startsWith('data: ')) {
              try {
                const data = JSON.parse(line.slice(6));
                
                switch (data.type) {
                  case 'status':
                    currentStatus = data.data.state;
                    setIsLoading(currentStatus !== 'complete');
                    break;
                    
                  case 'chunk':
                    assistantMessage += data.data;
                    // Update the message in real-time
                    setMessages(prev => {
                      // Find the last user message in the conversation
                      const lastUserMessageIndex = prev.map(msg => msg.role).lastIndexOf('user');
                      
                      if (lastUserMessageIndex === -1) {
                        // No user message found, just append assistant message
                        return [...prev, {
                          role: 'assistant',
                          content: assistantMessage,
                          checkpoint_id: checkpointId
                        }];
                      }
                      
                      // Check if there's already an assistant response after the last user message
                      const hasAssistantResponse = lastUserMessageIndex < prev.length - 1 && 
                        prev[lastUserMessageIndex + 1].role === 'assistant';
                      
                      if (hasAssistantResponse) {
                        // Update the existing assistant response
                        return prev.map((msg, index) => 
                          index === lastUserMessageIndex + 1
                            ? { ...msg, content: assistantMessage }
                            : msg
                        );
                      } else {
                        // Insert new assistant message after the last user message
                        return [
                          ...prev.slice(0, lastUserMessageIndex + 1),
                          {
                            role: 'assistant',
                            content: assistantMessage,
                            checkpoint_id: checkpointId
                          },
                          ...prev.slice(lastUserMessageIndex + 1)
                        ];
                      }
                    });
                    break;
                    
                  case 'error':
                    setError(data.data);
                    setIsLoading(false);
                    break;
                }
              } catch (e) {
                console.error('Failed to parse chunk:', e);
              }
            }
          }
        }
      } finally {
        reader.releaseLock();
        setIsLoading(false);
      }

    } catch (err) {
      setError('Failed to send message');
      console.error('Failed to send message:', err);
    } finally {
      setIsLoading(false);
    }
  }, [sessionId, checkpointId]);

  return {
    messages,
    isLoading,
    error,
    sendMessage
  };
}
