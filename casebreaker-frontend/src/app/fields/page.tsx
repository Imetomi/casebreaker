import { Container, Grid, Heading, Text } from '@radix-ui/themes';
import { FieldCard } from '@/components/fields/FieldCard';

async function getFields() {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/v1/fields/`, {
    cache: 'no-store',
  });
  if (!res.ok) throw new Error('Failed to fetch fields');
  return res.json();
}

export default async function FieldsPage() {
  const fields = await getFields();

  return (
    <Container size="4" className="py-12">
      <div className="text-center mb-12">
        <Heading size="8" className="mb-4" highContrast>
          Explore Fields
        </Heading>
        <Text size="4" as="p" color="gray" className="max-w-2xl mx-auto">
          Discover various fields and start your journey in case-based learning. Each field contains multiple subtopics with real-world cases to help you master the subject matter.
        </Text>
      </div>

      <Grid columns={{ initial: '1', sm: '2', md: '3' }} gap="6">
        {fields.map((field: any) => (
          <FieldCard
            key={field.id}
            id={field.id}
            name={field.name}
            description={field.description}
            iconUrl={field.icon_url}
          />
        ))}
      </Grid>
    </Container>
  );
}
