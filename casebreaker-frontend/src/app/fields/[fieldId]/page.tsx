import { Container, Heading, Text, Grid } from '@radix-ui/themes';
import { BackButton } from '@/components/ui/BackButton';
import { SubtopicCard } from '@/components/fields/SubtopicCard';
import { api } from '@/lib/api';

export default async function FieldPage({ params }: { params: { fieldId: string } }) {
  const [field, subtopics] = await Promise.all([
    api.getField(parseInt(params.fieldId)),
    api.getSubtopics(parseInt(params.fieldId))
  ]);

  return (
    <Container size="4" className="py-12">
      <div className="mb-8">
        <BackButton href="/" />
        <div className="text-center">
          <Heading size="8" className="mb-2" highContrast>
            {field.name}
          </Heading>
          <Text size="4" as="p" color="gray" className="mb-8 max-w-2xl mx-auto">
            {field.description}
          </Text>
        </div>
      </div>

      <Grid columns={{ initial: '1', sm: '2', md: '3' }} gap="6">
        {subtopics.map((subtopic) => (
          <SubtopicCard
            key={subtopic.id}
            id={subtopic.id}
            fieldId={parseInt(params.fieldId)}
            name={subtopic.name}
            description={subtopic.description}
            caseStudyCount={subtopic.case_count}
          />
        ))}
      </Grid>
    </Container>
  );
}
