'use client';

import { Card, Text, Avatar } from '@radix-ui/themes';
import { GraduationCap, UserCircle2 } from 'lucide-react';

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
        fallback={isUser ? <UserCircle2 className="p-1" /> : <GraduationCap className="p-1" />}
        className={isUser ? 'bg-cyan-9 text-white' : 'bg-accent-9 text-white'}
      />
      <div className={`flex flex-col ${isUser ? 'items-end' : 'items-start'} max-w-[70%]`}>
        <Card
          size="1"
          className={`${isUser ? 'bg-cyan-2' : 'bg-accent-2'}`}
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
