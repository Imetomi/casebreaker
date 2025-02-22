import { Container, Heading, Text, Card, Badge, Button } from '@radix-ui/themes';
import { MessageSquare } from 'lucide-react';
import Link from 'next/link';
import { BackButton } from '@/components/ui/BackButton';

// This would come from your API
const caseStudies = {
  1: {
    id: 1,
    title: 'The Miranda Rights Case',
    description: 'Analyze the landmark case that established the requirement for law enforcement to inform suspects of their rights.',
    difficulty: 'Beginner',
    estimatedTime: '30 min',
    objectives: [
      'Understand the historical context of Miranda Rights',
      'Analyze the Supreme Court\'s decision',
      'Apply Miranda Rights to modern scenarios'
    ],
    content: `In 1966, the U.S. Supreme Court made a landmark decision in Miranda v. Arizona...`,
  },
  2: {
    id: 2,
    title: 'Self-Defense in Criminal Law',
    description: 'Explore the legal boundaries and requirements for claiming self-defense in criminal cases.',
    difficulty: 'Intermediate',
    estimatedTime: '45 min',
    objectives: [
      'Define the elements of self-defense',
      'Analyze real case examples',
      'Evaluate the reasonableness standard'
    ],
    content: `Self-defense is a legal justification that can be used as a defense to criminal charges...`,
  },
};

export default function CasePage({ 
  params 
}: { 
  params: { fieldId: string; subtopicId: string; caseId: string } 
}) {
  const caseId = parseInt(params.caseId);
  const caseStudy = caseStudies[caseId as keyof typeof caseStudies];

  if (!caseStudy) {
    return (
      <Container size="4" className="py-12">
        <BackButton />
        <div className="text-center">
          <Heading size="8" className="mb-4">Case Not Found</Heading>
          <Text size="4" as="p" color="gray">
            The requested case study could not be found.
          </Text>
        </div>
      </Container>
    );
  }

  const difficultyColor = {
    'Beginner': 'green',
    'Intermediate': 'yellow',
    'Advanced': 'red'
  }[caseStudy.difficulty] as 'green' | 'yellow' | 'red';

  return (
    <Container size="4" className="py-12">
      <BackButton />
      
      <div className="space-y-12">
        <div>
          <div className="flex justify-between items-start mb-6 gap-4">
            <Heading size="8" highContrast>
              {caseStudy.title}
            </Heading>
            <div className="flex gap-2">
              <Badge size="2" color={difficultyColor}>
                {caseStudy.difficulty}
              </Badge>
              <Badge size="2" color="blue">
                {caseStudy.estimatedTime}
              </Badge>
            </div>
          </div>
          
          <Text size="4" as="p" color="gray">
            {caseStudy.description}
          </Text>
        </div>

        <div className="space-y-8">
          <Card className="p-6">
            <Heading size="4" className="mb-6">Learning Objectives</Heading>
            <div className="space-y-4">
              {caseStudy.objectives.map((objective, index) => (
                <div key={index} className="flex items-start gap-3">
                  <div className="mt-1 flex-shrink-0">
                    <input
                      type="checkbox"
                      className="h-4 w-4 rounded border-gray-300 text-blue-500 focus:ring-blue-500"
                    />
                  </div>
                  <Text size="2">{objective}</Text>
                </div>
              ))}
            </div>
          </Card>

          <Card className="p-6">
            <Heading size="4" className="mb-6">Case Content</Heading>
            <Text as="p" size="2" className="leading-relaxed">
              {caseStudy.content}
            </Text>
          </Card>

          <Link href={`/fields/${params.fieldId}/subtopics/${params.subtopicId}/cases/${caseId}/chat`} className="block">
            <Button size="4" className="w-full">
              <MessageSquare className="w-5 h-5 mr-2" />
              Solve Case Study
            </Button>
          </Link>
        </div>
      </div>
    </Container>
  );
}
