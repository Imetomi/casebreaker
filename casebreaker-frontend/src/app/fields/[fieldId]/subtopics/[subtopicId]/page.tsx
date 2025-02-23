import { Container, Heading, Text, Grid } from '@radix-ui/themes';
import { BackButton } from '@/components/ui/BackButton';
import { CaseCard } from '@/components/Cases/CaseCard';
import { api } from '@/lib/api';

export default async function SubtopicPage({ 
  params 
}: { 
  params: { fieldId: string; subtopicId: string } 
}) {
  const fieldId = parseInt(params.fieldId);
  const subtopicId = parseInt(params.subtopicId);

  const [subtopic, caseStudies] = await Promise.all([
    api.getSubtopics(fieldId).then(subtopics => subtopics.find(s => s.id === subtopicId)),
    api.getCaseStudiesBySubtopic(subtopicId)
  ]);

  if (!subtopic) {
    throw new Error('Subtopic not found');
  }

  return (
    <Container size="4" className="py-12">
      <BackButton />
      
      <div className="text-center mb-12">
        <Heading size="8" className="mb-4" highContrast>
          {subtopic.name} Cases
        </Heading>
        <Text size="4" as="p" color="gray" className="max-w-2xl mx-auto">
          Select a case study to begin your learning journey
        </Text>
      </div>

      <Grid columns={{ initial: '1', sm: '2', md: '3' }} gap="6">
        {caseStudies.map((caseStudy) => (
          <CaseCard
            key={caseStudy.id}
            {...caseStudy}
            fieldId={fieldId}
            subtopicId={subtopicId}
          />
        ))}
      </Grid>
    </Container>
  );
}
