'use client';

import { Card, Text, Avatar } from '@radix-ui/themes';
import { User, Bot } from 'lucide-react';

interface MessageProps {
  content: string;
  isUser: boolean;
}

export function Message({ content, isUser }: MessageProps) {
  return (
    <div className={`flex items-start gap-3 ${isUser ? 'flex-row-reverse' : ''}`}>
      <Avatar
        size="2"
        radius="full"
        fallback={isUser ? <User className="p-1" /> : <Bot className="p-1" />}
        className={isUser ? 'bg-blue-500 text-white' : 'bg-gray-500 text-white'}
      />
      <div className={`flex flex-col ${isUser ? 'items-end' : 'items-start'} max-w-[70%]`}>
        <Card
          size="1"
          className={`${isUser ? 'bg-blue-50' : 'bg-gray-50'}`}
          style={{ marginBottom: 'var(--space-1)' }}
        >
          <Text as="p" size="2" className="whitespace-pre-wrap">
            {content}
          </Text>
        </Card>

      </div>
    </div>
  );
}
