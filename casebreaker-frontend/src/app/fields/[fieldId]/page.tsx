import { Container, Heading, Text, Grid } from '@radix-ui/themes';
import { BackButton } from '@/components/ui/BackButton';
import { SubtopicCard } from '@/components/fields/SubtopicCard';

// This would come from your API
const subtopics = {
  1: [ // Law
    {
      id: 1,
      name: 'Criminal Law',
      description: 'Study criminal cases involving various offenses and legal procedures.',
      caseStudyCount: 5,
    },
    {
      id: 2,
      name: 'Corporate Law',
      description: 'Examine business-related legal cases and corporate governance issues.',
      caseStudyCount: 3,
    },
    {
      id: 3,
      name: 'Constitutional Law',
      description: 'Analyze cases involving constitutional rights and governmental powers.',
      caseStudyCount: 4,
    },
  ],
  2: [ // Healthcare
    {
      id: 4,
      name: 'Emergency Medicine',
      description: 'Learn from emergency room cases and critical care scenarios.',
      caseStudyCount: 6,
    },
    {
      id: 5,
      name: 'Medical Ethics',
      description: 'Explore ethical dilemmas in healthcare decision-making.',
      caseStudyCount: 4,
    },
    {
      id: 6,
      name: 'Public Health',
      description: 'Study cases related to population health and healthcare policy.',
      caseStudyCount: 3,
    },
  ],
  3: [ // Economics
    {
      id: 7,
      name: 'Microeconomics',
      description: 'Analyze individual market behaviors and business decisions.',
      caseStudyCount: 5,
    },
    {
      id: 8,
      name: 'Macroeconomics',
      description: 'Study economic trends, policies, and their global impact.',
      caseStudyCount: 4,
    },
    {
      id: 9,
      name: 'Financial Markets',
      description: 'Examine cases involving financial instruments and market dynamics.',
      caseStudyCount: 6,
    },
  ],
};

const fieldNames = {
  1: 'Law',
  2: 'Healthcare',
  3: 'Economics',
};

export default function FieldPage({ params }: { params: { fieldId: string } }) {
  const fieldId = parseInt(params.fieldId);
  const fieldSubtopics = subtopics[fieldId as keyof typeof subtopics] || [];
  const fieldName = fieldNames[fieldId as keyof typeof fieldNames];

  return (
    <Container size="4" className="py-12">
      <BackButton />
      
      <div className="text-center mb-12">
        <Heading size="8" className="mb-4" highContrast>
          {fieldName} Subtopics
        </Heading>
        <Text size="4" as="p" color="gray" className="max-w-2xl mx-auto">
          Select a subtopic to explore its case studies
        </Text>
      </div>

      <Grid columns={{ initial: '1', sm: '2', md: '3' }} gap="6">
        {fieldSubtopics.map((subtopic) => (
          <SubtopicCard
            key={subtopic.id}
            {...subtopic}
            fieldId={fieldId}
          />
        ))}
      </Grid>
    </Container>
  );
}
