'use client';

import { Container, Heading, Text } from '@radix-ui/themes';
import { BackButton } from '@/components/ui/BackButton';
import { Chat } from '@/components/Chat/Chat';
import { useEffect, useState } from 'react';
import { api } from '@/lib/api';
import { useParams } from 'next/navigation';
import { v4 as uuidv4 } from 'uuid';

const DEVICE_ID_KEY = 'casebreaker_device_id';

export default function CaseChatPage() {
  const params = useParams();
  const [sessionId, setSessionId] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [caseStudy, setCaseStudy] = useState<any>({ pitfalls: [] });
  const caseId = parseInt(params.caseId as string);

  useEffect(() => {
    async function initialize() {
      try {
        // Get or create device ID
        let deviceId = localStorage.getItem(DEVICE_ID_KEY);
        if (!deviceId) {
          deviceId = uuidv4();
          localStorage.setItem(DEVICE_ID_KEY, deviceId);
        }

        // Fetch case study and create session in parallel
        const [study, session] = await Promise.all([
          api.getCaseStudy(caseId),
          api.createSession(caseId, deviceId)
        ]);

        setCaseStudy(study);
        setSessionId(session.id);
      } catch (err) {
        console.error('Failed to initialize:', err);
        setError('Failed to initialize chat session');
      } finally {
        setIsLoading(false);
      }
    }

    initialize();
  }, [caseId]);

  if (error) {
    return (
      <Container size="4" className="py-12">
        <BackButton />
        <div className="p-4 bg-red-50 text-red-700 rounded-lg mt-8">
          {error}
        </div>
      </Container>
    );
  }

  if (isLoading || !sessionId || !caseStudy) {
    return (
      <Container size="4" className="py-12">
        <BackButton />
        <div className="flex justify-center items-center h-[calc(100vh-14rem)]">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900" />
        </div>
      </Container>
    );
  }

  const initialMessage = `Welcome! I'm here to help you analyze the ${caseStudy.title}. Let's start by discussing the historical context of this landmark decision.

To help guide our discussion, here are some key aspects we can explore:
${caseStudy.learningObjectives.map((obj: string, i: number) => `${i + 1}. ${obj}`).join('\n')}

Feel free to ask any questions!`;

  return (
    <Container size="4" className="py-12">
      <BackButton />
      
      <div className="mb-8">
        <Heading size="8" className="text-center mb-4" highContrast>
          {caseStudy.title}
        </Heading>
      </div>

      <Chat
        sessionId={sessionId}
        initialMessage={initialMessage}
      />
    </Container>
  );
}
