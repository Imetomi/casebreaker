import { Container, Heading, Text, Grid, Button, Link } from '@radix-ui/themes';
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
    <>
    <div className="relative">
      {/* Main gradient */}
      <div className="absolute inset-0 bg-gradient-to-b from-blue-100 via-blue-50/50 to-white" />
      <Container size="4" className="relative pt-32 pb-24">
        <div className="text-center max-w-2xl mx-auto">
          <Heading size="9" className="mb-8">
            Get ready for your exam with{" "}
            <Text className="font-bold inline-block" color="blue">real-world</Text>
            {" "}case studies 📚
          </Heading>
            <Text size="4" as="p" color="gray" weight="medium" className="mb-12 leading-relaxed">
              Dive into interactive case studies and gain practical knowledge in your field
              with an intelligent agent to help you. 🤖
            </Text>
            <Button size="4" variant="solid" asChild>
              <Link href="/fields" className="no-underline">
                Find your field
              </Link>
            </Button>
        </div>
      </Container>
    </div>

    {/* Available Exams Section */}
    <div className="relative py-16">
      <div className="absolute inset-0 bg-gradient-to-b from-white via-white to-blue-50/20" style={{ zIndex: 0 }} />
      <Container className="relative" style={{ zIndex: 1 }}>
        <div className="text-center">
          <Text size="4" as="p" color="gray" weight="medium" className="mb-4">Popular case studies at your university</Text>
          <div className="flex flex-wrap justify-center gap-3 mb-4">
            <Button variant="surface" size="3">
              🇺🇸 Roe v. Wade
            </Button>
            <Button variant="surface" size="3">
              🇬🇧 Donoghue v. Stevenson
            </Button>
            <Button variant="surface" size="3">
              🇩🇪 Nuremberg Trials
            </Button>
            <Button variant="surface" size="3">
              🇺🇸 Brown v. Board
            </Button>
            <Button variant="surface" size="3">
              🇨🇦 Legroulx v. Pitre
            </Button>
          </div>
          <div className="flex flex-wrap justify-center gap-3 mb-4">
            <Button variant="surface" size="3">
              🇺🇸 2008 Financial Crisis
            </Button>
            <Button variant="surface" size="3">
              🇫🇮 UBI Trials
            </Button>
            <Button variant="surface" size="3">
              🇬🇧 Brexit Impact
            </Button>
            <Button variant="surface" size="3">
              🇺🇸 Gig Economy
            </Button>
          </div>
          <div className="flex flex-wrap justify-center gap-3">
            <Button variant="surface" size="3">
              🇺🇸 Affordable Care Act
            </Button>
            <Button variant="surface" size="3">
              🇦🇺 Mental Health Reform
            </Button>
            <Button variant="surface" size="3">
              🇺🇸 Vaccination Laws
            </Button>
            <Button variant="surface" size="3">
              🇦🇪 Dubai Healthcare City
            </Button>
          </div>
        </div>
      </Container>
    </div>

    {/* Recommended Fields Section */}
    <div className="relative py-24">
      <div className="absolute inset-0 bg-gradient-to-b from-blue-50/20 to-blue-100" style={{ zIndex: 0 }} />
      <Container size="3" className="relative" style={{ zIndex: 1 }}>
        <div className="text-center mb-20">
          <Heading size="8" className="mb-4" highContrast>
            <Text>Popular Learning Fields</Text> 🎯
          </Heading>
          <Text size="5" as="p" color="gray" className="max-w-lg mx-auto">
            Start your journey with our most engaging disciplines
          </Text>
        </div>
        <Grid columns={{ initial: '1', sm: '2' }} gap="8">
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
        <div className="text-center mt-12">
          <Button size="4" variant="outline" asChild>
            <Link href="/fields" className="no-underline">
              Find more fields
            </Link>
          </Button>
        </div>
      </Container>
    </div>
    </>
  );
}
