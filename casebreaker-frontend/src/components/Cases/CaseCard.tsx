'use client';

import { Card, Heading, Text, Button, Badge } from '@radix-ui/themes';
import { MessageSquare } from 'lucide-react';
import Link from 'next/link';

interface CaseCardProps {
  id: number;
  title: string;
  description: string;
  difficulty: 'Beginner' | 'Intermediate' | 'Advanced';
  estimatedTime: string;
  fieldId: number;
  subtopicId: number;
}

export function CaseCard({ 
  id, 
  title, 
  description, 
  difficulty, 
  estimatedTime,
  fieldId,
  subtopicId
}: CaseCardProps) {
  const difficultyColor = {
    'Beginner': 'green',
    'Intermediate': 'yellow',
    'Advanced': 'red'
  }[difficulty] as 'green' | 'yellow' | 'red';

  return (
    <Card size="3" className="flex flex-col h-full">
      <div className="flex flex-col flex-1">
        <div className="flex justify-between items-start mb-2 gap-4">
          <Heading as="h3" size="5" trim="start">
            {title}
          </Heading>
          <div className="flex gap-2">
            <Badge size="2" color={difficultyColor}>
              {difficulty}
            </Badge>
            <Badge size="2" color="blue">
              {estimatedTime}
            </Badge>
          </div>
        </div>
        
        <Text as="p" color="gray" size="2" className="flex-1 mb-4">
          {description}
        </Text>
        
        <Link href={`/fields/${fieldId}/subtopics/${subtopicId}/cases/${id}`} className="mt-auto">
          <Button size="3" variant="soft" className="w-full">
            <MessageSquare className="w-4 h-4 mr-2" />
            Start Case Study
          </Button>
        </Link>
      </div>
    </Card>
  );
}
