import { Container, Heading, Text, Card, Badge, Button, Flex, Box } from '@radix-ui/themes';
import { MessageSquare, Book, Lightbulb } from 'lucide-react';
import Link from 'next/link';
import { BackButton } from '@/components/ui/BackButton';
import { api } from '@/lib/api';

export default async function CasePage({ 
  params 
}: { 
  params: { fieldId: string; subtopicId: string; caseId: string } 
}) {
  const caseId = parseInt(params.caseId);
  const caseStudy = await api.getCaseStudy(caseId);

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
          <div className="text-center mb-6">
            <Heading size="8" highContrast className="mb-4">
              {caseStudy.title}
            </Heading>
            <Text size="4" as="p" color="gray" className="max-w-2xl mx-auto">
              {caseStudy.description}
            </Text>
            <div className="flex justify-center gap-2 mt-6">
              <Badge size="2" color={difficultyColor}>
                {caseStudy.difficulty}
              </Badge>
              <Badge size="2" color="blue">
                {caseStudy.estimatedTime}
              </Badge>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Context Materials */}
          {(caseStudy.contextMaterials.background || caseStudy.contextMaterials.keyConcepts.length > 0 || caseStudy.contextMaterials.requiredReading) && (
            <Card className="p-6 h-full">
              <Flex gap="2" align="center" mb="4">
                <Book className="w-5 h-5" />
                <Heading size="4">Context Materials</Heading>
              </Flex>
              <div className="space-y-6">
                {caseStudy.contextMaterials.background && (
                  <div>
                    <Text as="p" size="2" weight="bold" mb="2">Background</Text>
                    <Text as="p" size="2" color="gray">{caseStudy.contextMaterials.background}</Text>
                  </div>
                )}
                {caseStudy.contextMaterials.keyConcepts.length > 0 && (
                  <div>
                    <Text as="p" size="2" weight="bold" mb="2">Key Concepts</Text>
                    <ul className="list-disc pl-5 space-y-1">
                      {caseStudy.contextMaterials.keyConcepts.map((concept, index) => (
                        <li key={index}>
                          <Text as="p" size="2" color="gray">{concept}</Text>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
                {caseStudy.contextMaterials.requiredReading && (
                  <div>
                    <Text as="p" size="2" weight="bold" mb="2">Required Reading</Text>
                    <Text as="p" size="2" color="gray">{caseStudy.contextMaterials.requiredReading}</Text>
                  </div>
                )}
              </div>
            </Card>
          )}

          {/* Learning Objectives */}
          {caseStudy.learningObjectives.length > 0 && (
            <Card className="p-6 h-full">
              <Flex gap="2" align="center" mb="4">
                <Lightbulb className="w-5 h-5" />
                <Heading size="4">Learning Objectives</Heading>
              </Flex>
              <ul className="list-disc pl-5 space-y-2">
                {caseStudy.learningObjectives.map((objective, index) => (
                  <li key={index}>
                    <Text size="2" color="gray">{objective}</Text>
                  </li>
                ))}
              </ul>
            </Card>
          )}

          <div className="col-span-1 md:col-span-2 flex justify-center mt-8">
            <Link href={`/fields/${params.fieldId}/subtopics/${params.subtopicId}/cases/${caseId}/chat`}>
              <Button size="4">
                <MessageSquare className="w-5 h-5 mr-2" />
                Start Case Study
              </Button>
            </Link>
          </div>
        </div>
      </div>
    </Container>
  );
}
