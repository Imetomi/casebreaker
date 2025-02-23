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
            <div className="flex justify-center gap-2 mb-6">
              <Badge size="2" color={difficultyColor}>
                {caseStudy.difficulty}
              </Badge>
              <Badge size="2" color="blue">
                {caseStudy.estimatedTime}
              </Badge>
            </div>
          </div>
        </div>

        <div className="space-y-8">
          {(caseStudy.contextMaterials.background || caseStudy.contextMaterials.keyConcepts.length > 0 || caseStudy.contextMaterials.requiredReading) && (
            <Card className="p-6">
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

          {caseStudy.learningObjectives.length > 0 && (
            <Card className="p-6">
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

          {caseStudy.checkpoints.length > 0 && (
            <Card className="p-6">
              <Heading size="4" className="mb-6">Checkpoints</Heading>
              <div className="space-y-8">
                {caseStudy.checkpoints.map((checkpoint) => (
                  <div key={checkpoint.id} className="space-y-2">
                    <Heading size="3">{checkpoint.title}</Heading>
                    <Text as="p" size="2" color="gray">{checkpoint.description}</Text>
                    {checkpoint.hints?.length > 0 && (
                      <Box mt="4">
                        <Text size="2" weight="bold">Hints:</Text>
                        <ul className="list-disc pl-5 mt-1">
                          {checkpoint.hints.map((hint, index) => (
                            <li key={index}>
                              <Text size="2" color="gray">{hint}</Text>
                            </li>
                          ))}
                        </ul>
                      </Box>
                    )}
                  </div>
                ))}
              </div>
            </Card>
          )}

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
