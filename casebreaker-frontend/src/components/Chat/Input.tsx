'use client';

import { Button, TextArea } from '@radix-ui/themes';
import { Send } from 'lucide-react';
import { useState, KeyboardEvent } from 'react';

interface InputProps {
  onSend: (message: string) => void;
  disabled?: boolean;
}

export function Input({ onSend, disabled }: InputProps) {
  const [message, setMessage] = useState('');

  const handleSend = () => {
    if (message.trim() && !disabled) {
      onSend(message);
      setMessage('');
    }
  };

  const handleKeyPress = (e: KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="flex gap-2">
      <TextArea
        className="flex-1"
        placeholder="Type your message..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={handleKeyPress}
        disabled={disabled}
        style={{
          minHeight: '40px',
          height: '40px',
          resize: 'none',
          paddingTop: '8px',
          paddingBottom: '8px'
        }}
      />
      
      <Button 
        onClick={handleSend}
        disabled={!message.trim() || disabled}
        size="3"
        variant="solid"
      >
        <Send className="w-4 h-4" />
      </Button>
    </div>
  );
}
