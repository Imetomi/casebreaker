'use client';

import { Card, Heading, Text, Button, Badge } from '@radix-ui/themes';
import { BookOpen } from 'lucide-react';
import Link from 'next/link';

interface SubtopicCardProps {
  id: number;
  name: string;
  description: string;
  caseStudyCount: number;
  fieldId: number;
}

export function SubtopicCard({ id, name, description, caseStudyCount, fieldId }: SubtopicCardProps) {
  return (
    <Card size="3" className="flex flex-col h-full">
      <div className="flex flex-col flex-1">
        <div className="flex justify-between items-start mb-2 gap-4">
          <Heading as="h3" size="5" trim="start">
            {name}
          </Heading>
          <Badge size="2" color="blue">
            {caseStudyCount} Cases
          </Badge>
        </div>
        
        <Text as="p" color="gray" size="2" className="flex-1 mb-4">
          {description}
        </Text>
        
        <Link href={`/fields/${fieldId}/subtopics/${id}`} className="mt-auto">
          <Button size="3" variant="soft" className="w-full">
            <BookOpen className="w-4 h-4 mr-2" />
            View Case Studies
          </Button>
        </Link>
      </div>
    </Card>
  );
}
