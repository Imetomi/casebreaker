import { Container, Heading, Text, Grid } from '@radix-ui/themes';
import { FieldCard } from '@/components/fields/FieldCard';

async function getFields() {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/api/v1/fields/`, {
    cache: 'no-store',
  });
  if (!res.ok) throw new Error('Failed to fetch fields');
  return res.json();
}

export default async function Home() {
  const fields = await getFields();

  return (
    <Container size="4" className="py-12">
      <div className="text-center mb-12">
        <Heading size="9" className="mb-4" highContrast>
          Case
          <span className="text-blue-500">Breaker</span>
        </Heading>
        <Text size="5" as="p" color="gray" className="max-w-2xl mx-auto">
          AI-guided case study learning experiences across multiple disciplines.
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
