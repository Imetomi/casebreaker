'use client';

import { Card, Heading, Text, Box } from '@radix-ui/themes';
import type { CaseStudy } from '@/lib/api';

interface ContextViewProps {
  caseStudy: CaseStudy;
}

export function ContextView({ caseStudy }: ContextViewProps) {
  const listStyle = {
    listStyleType: 'disc',
    paddingLeft: '1rem',
    display: 'flex',
    flexDirection: 'column' as const,
    gap: '0.25rem'
  };

  if (!caseStudy?.contextMaterials) {
    return null;
  }

  return (
    <div
      className="flex flex-col h-[calc(100vh-14rem)] max-h-[700px] bg-white rounded-lg border shadow-sm overflow-hidden"
    >
      <div className="flex-1 overflow-y-auto p-4">
          <Heading size="4" mb="6">
            Case Context
          </Heading>
          
          <Box mb="5">
            <Heading size="2" mb="2" color="gray">
              Background
            </Heading>
            <Text as="p" size="2" color="gray">
              {caseStudy.contextMaterials.background}
            </Text>
          </Box>

          <Box mb="5">
            <Heading size="2" mb="2" color="gray">
              Key Concepts
            </Heading>
            <ul style={listStyle}>
              {caseStudy.contextMaterials.keyConcepts.map((concept, index) => (
                <li key={index}>
                  <Text size="2" color="gray">{concept}</Text>
                </li>
              ))}
            </ul>
          </Box>

          <Box>
            <Heading size="2" mb="2" color="gray">
              Required Reading
            </Heading>
            <Text as="p" size="2" color="gray">
              {caseStudy.contextMaterials.requiredReading}
            </Text>
          </Box>
      </div>
    </div>
  );
}
