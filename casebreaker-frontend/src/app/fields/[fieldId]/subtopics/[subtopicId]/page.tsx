import { Container, Heading, Text, Grid } from '@radix-ui/themes';
import { BackButton } from '@/components/ui/BackButton';
import { CaseCard } from '@/components/Cases/CaseCard';

// This would come from your API
const cases = {
  1: [ // Criminal Law
    {
      id: 1,
      title: 'The Miranda Rights Case',
      description: 'Analyze the landmark case that established the requirement for law enforcement to inform suspects of their rights.',
      difficulty: 'Beginner',
      estimatedTime: '30 min',
    },
    {
      id: 2,
      title: 'Self-Defense in Criminal Law',
      description: 'Explore the legal boundaries and requirements for claiming self-defense in criminal cases.',
      difficulty: 'Intermediate',
      estimatedTime: '45 min',
    },
  ],
  2: [ // Corporate Law
    {
      id: 3,
      title: 'Shareholder Rights Dispute',
      description: 'Study a complex case involving minority shareholder rights and corporate governance.',
      difficulty: 'Advanced',
      estimatedTime: '60 min',
    },
  ],
  4: [ // Emergency Medicine
    {
      id: 4,
      title: 'Acute Respiratory Distress',
      description: 'Evaluate an emergency case involving rapid diagnosis and treatment decisions.',
      difficulty: 'Intermediate',
      estimatedTime: '45 min',
    },
  ],
  7: [ // Microeconomics
    {
      id: 5,
      title: 'Market Monopoly Analysis',
      description: 'Analyze the effects of monopolistic behavior on market dynamics and consumer welfare.',
      difficulty: 'Advanced',
      estimatedTime: '60 min',
    },
  ],
};

const subtopicNames = {
  1: 'Criminal Law',
  2: 'Corporate Law',
  4: 'Emergency Medicine',
  7: 'Microeconomics',
};

export default function SubtopicPage({ 
  params 
}: { 
  params: { fieldId: string; subtopicId: string } 
}) {
  const fieldId = parseInt(params.fieldId);
  const subtopicId = parseInt(params.subtopicId);
  const subtopicCases = cases[subtopicId as keyof typeof cases] || [];
  const subtopicName = subtopicNames[subtopicId as keyof typeof subtopicNames];

  return (
    <Container size="4" className="py-12">
      <BackButton />
      
      <div className="text-center mb-12">
        <Heading size="8" className="mb-4" highContrast>
          {subtopicName} Cases
        </Heading>
        <Text size="4" as="p" color="gray" className="max-w-2xl mx-auto">
          Select a case study to begin your learning journey
        </Text>
      </div>

      <Grid columns={{ initial: '1', sm: '2', md: '3' }} gap="6">
        {subtopicCases.map((caseStudy) => (
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
