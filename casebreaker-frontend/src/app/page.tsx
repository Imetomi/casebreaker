import { Container, Heading, Text, Grid, Button, Link } from '@radix-ui/themes';
import { FieldCard } from '@/components/fields/FieldCard';
import { AnimatedHeading } from '@/components/ui/AnimatedHeading';

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
      <div className="absolute inset-0 bg-gradient-to-b from-cyan-100 via-cyan-50/50 to-white" />
      <Container size="4" className="relative pt-32 pb-24">
        <div className="text-center max-w-2xl mx-auto">
          <Heading size="9" className="mb-8" >
            Learn{" "}
            <AnimatedHeading />
            {" "}with <br/>real-world case studies
          </Heading>
            <Text size="4" as="p" color="gray" weight="medium" className="mb-12 leading-relaxed">
              Choose from <Text weight="bold" color="gray" highContrast>over 1000 case studies</Text> and gain practical knowledge in your field
              with an intelligent agent to help you and. 🤖
            </Text>
            <Button size="4" variant="solid" asChild>
              <Link href="/fields" className="no-underline">
                Find your course
              </Link>
            </Button>
        </div>
      </Container>
    </div>

    {/* Available Exams Section */}
    <div className="relative py-16">
      <div className="absolute inset-0 bg-gradient-to-b from-white via-white to-cyan-50/20" style={{ zIndex: 0 }} />
      <Container className="relative" style={{ zIndex: 1 }}>
        <div className="text-center">
          <Text size="4" as="p" color="gray" weight="medium" className="mb-4">Popular case studies in university courses</Text>
          <div className="flex flex-wrap justify-center gap-3 mb-4">
            <Button variant="surface" size="3">
              🧬 Human Genome Project
            </Button>
            <Button variant="surface" size="3">
              🔬 Stanford Prison Experiment
            </Button>
            <Button variant="surface" size="3">
              💊 Thalidomide Crisis
            </Button>
            <Button variant="surface" size="3">
              🧪 Manhattan Project Ethics
            </Button>
          </div>
          <div className="flex flex-wrap justify-center gap-3 mb-4">
            <Button variant="surface" size="3">
              💼 Enron Accounting Scandal
            </Button>
            <Button variant="surface" size="3">
              📱 Apple vs. Samsung Patent
            </Button>
            <Button variant="surface" size="3">
              🏦 Lehman Brothers Collapse
            </Button>
            <Button variant="surface" size="3">
              🤖 Cambridge Analytica
            </Button>
          </div>
          <div className="flex flex-wrap justify-center gap-3">
            <Button variant="surface" size="3">
              🌍 Climate Change Models
            </Button>
            <Button variant="surface" size="3">
              🧮 Nash Equilibrium Apps
            </Button>
            <Button variant="surface" size="3">
              🧫 CRISPR Ethics Cases
            </Button>
            <Button variant="surface" size="3">
              🔋 Tesla Battery Innovation
            </Button>
          </div>
        </div>
      </Container>
    </div>

    {/* Recommended Fields Section */}
    <div className="relative py-24">
      <div className="absolute inset-0 bg-gradient-to-b from-cyan-50/20 to-cyan-100" style={{ zIndex: 0 }} />
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
          {fields.slice(0, 4).map((field: any) => (
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


    {/* Available Exams Section per counrty */}
    <div className="relative py-16">
      <div className="absolute inset-0 bg-gradient-to-b from-cyan-100 to-white" style={{ zIndex: 0 }} />
      <Container className="relative" style={{ zIndex: 1 }}>
        <div className="text-center">
          {/* International cases section */}
          <Text size="4" as="p" color="gray" weight="medium" className="mb-4">Notable cases from your counrty</Text>
          <div className="flex flex-wrap justify-center gap-3 mb-4">
            <Button variant="surface" size="3">
              🇺🇸 Harvard Business School Cases
            </Button>
            <Button variant="surface" size="3">
              🇬🇧 Oxford Medical Ethics
            </Button>
            <Button variant="surface" size="3">
              🇩🇪 Max Planck Research Cases
            </Button>
            <Button variant="surface" size="3">
              🇯🇵 Toyota Production System
            </Button>
          </div>
          <div className="flex flex-wrap justify-center gap-3">
            <Button variant="surface" size="3">
              🇨🇭 CERN Physics Studies
            </Button>
            <Button variant="surface" size="3">
              🇸🇪 Karolinska Medical Research
            </Button>
            <Button variant="surface" size="3">
              🇳🇱 Rotterdam School of Management
            </Button>
            <Button variant="surface" size="3">
              🇸🇬 NUS Technology Innovation
            </Button>
          </div>
        </div>
      </Container>
    </div>


    {/* Why Case Studies Section */}
    <div className="relative py-16 bg-white">
      <Container>
        <Grid columns="2" gap="9" className="items-center">
          <div>
            <Heading size="6" className="mb-4" highContrast>
              Why Case Studies Beat Traditional Learning Methods
            </Heading>
            <Text as="p" size="4" color="gray" className="mb-4 leading-relaxed">
              While flashcards and rote memorization might help you remember facts, they don't prepare you for real-world scenarios. Case studies offer a superior learning experience by:
            </Text>
            <div className="space-y-4">
              <div>
                <Text as="p" size="3" weight="bold" className="mb-1">
                  🧠 Deep Understanding Over Surface Learning
                </Text>
                <Text as="p" size="2" color="gray">
                  Case studies challenge you to apply knowledge in context, leading to better retention and understanding than memorizing isolated facts.
                </Text>
              </div>
              <div>
                <Text as="p" size="3" weight="bold" className="mb-1">
                  💡 Critical Thinking Development
                </Text>
                <Text as="p" size="2" color="gray">
                  Analyze complex situations, identify key issues, and develop problem-solving skills that are essential in professional practice.
                </Text>
              </div>
              <div>
                <Text as="p" size="3" weight="bold" className="mb-1">
                  🌟 Real-World Application
                </Text>
                <Text as="p" size="2" color="gray">
                  Experience scenarios you'll encounter in your career, building confidence and practical expertise before entering the field.
                </Text>
              </div>
              <div>
                <Text as="p" size="3" weight="bold" className="mb-1">
                  🤝 Better Professional Preparation
                </Text>
                <Text as="p" size="2" color="gray">
                  Learn how to navigate complex decisions, stakeholder relationships, and ethical considerations in your field.
                </Text>
              </div>
            </div>
          </div>
          <div className="relative">
            <div className="absolute inset-0 bg-gradient-to-tr from-cyan-100/50 to-purple-100/30 rounded-2xl" />
            <div className="relative p-8">
              <Text as="p" size="8" weight="bold" className="mb-6 text-cyan-900">
                83%
              </Text>
              <Text as="p" size="3" className="mb-2">
                of professionals agree that case-based learning better prepared them for their careers compared to traditional study methods.
              </Text>
              <Text as="p" size="2" color="gray">
                Based on a survey of 1,000+ industry professionals across multiple fields
              </Text>
            </div>
          </div>
        </Grid>
      </Container>
    </div>

    {/* AI-Powered Learning Section */}
    <div className="relative py-16 bg-gradient-to-b from-white to-cyan-50/30">
      <Container>
        <Grid columns="2" gap="9" className="items-center">
          <div className="relative order-1">
            <div className="absolute inset-0 bg-gradient-to-bl from-cyan-50/40 to-white rounded-2xl" />
            <div className="relative p-8">
              <Text as="p" size="8" weight="bold" className="mb-6 text-cyan-900">
                2.5x
              </Text>
              <Text as="p" size="3" className="mb-2">
                faster learning progress reported by students using AI-assisted case study analysis compared to traditional methods.
              </Text>
              <Text as="p" size="2" color="gray">
                Research conducted across multiple universities in 2024
              </Text>
            </div>
          </div>
          <div className="order-2">
            <Heading size="6" className="mb-4" highContrast>
              AI-Powered Learning Assistant
            </Heading>
            <Text as="p" size="4" color="gray" className="mb-4 leading-relaxed">
              Our intelligent AI companion transforms how you learn from case studies, providing:
            </Text>
            <div className="space-y-4">
              <div>
                <Text as="p" size="3" weight="bold" className="mb-1">
                  🤖 Interactive Discussions
                </Text>
                <Text as="p" size="2" color="gray">
                  Engage in dynamic conversations with our AI tutor that challenges your thinking and helps you explore different perspectives.
                </Text>
              </div>
              <div>
                <Text as="p" size="3" weight="bold" className="mb-1">
                  📊 Personalized Feedback
                </Text>
                <Text as="p" size="2" color="gray">
                  Receive instant, detailed feedback on your analysis and decision-making process, helping you improve continuously.
                </Text>
              </div>
              <div>
                <Text as="p" size="3" weight="bold" className="mb-1">
                  🎯 Adaptive Learning Path
                </Text>
                <Text as="p" size="2" color="gray">
                  Experience a learning journey that adapts to your progress and focuses on areas where you need the most improvement.
                </Text>
              </div>
              <div>
                <Text as="p" size="3" weight="bold" className="mb-1">
                  🔍 Deep Analysis Support
                </Text>
                <Text as="p" size="2" color="gray">
                  Get help identifying key issues, exploring solutions, and understanding complex relationships within case studies.
                </Text>
              </div>
            </div>
          </div>
        </Grid>
      </Container>
    </div>

    {/* Footer */}
    <footer className="bg-white border-t border-gray-200">
      <Container className="py-12">
        <Grid columns="4" gap="6">
          <div className="space-y-4">
            <Text as="p" size="3" weight="bold">
              CaseBreaker
            </Text>
            <Text as="p" size="2" color="gray">
              Revolutionizing case-based learning with AI-powered assistance and real-world scenarios.
            </Text>
          </div>
          <div className="space-y-4">
            <Text as="p" size="3" weight="bold">
              Popular Fields
            </Text>
            <div className="space-y-2">
              <Text as="p" size="2" color="gray">Law</Text>
              <Text as="p" size="2" color="gray">Business</Text>
              <Text as="p" size="2" color="gray">Medicine</Text>
              <Text as="p" size="2" color="gray">Public Policy</Text>
            </div>
          </div>
          <div className="space-y-4">
            <Text as="p" size="3" weight="bold">
              Resources
            </Text>
            <div className="space-y-2">
              <Text as="p" size="2" color="gray">Blog</Text>
              <Text as="p" size="2" color="gray">Case Library</Text>
              <Text as="p" size="2" color="gray">Study Guide</Text>
              <Text as="p" size="2" color="gray">FAQ</Text>
            </div>
          </div>
          <div className="space-y-4">
            <Text as="p" size="3" weight="bold">
              Contact
            </Text>
            <div className="space-y-2">
              <Text as="p" size="2" color="gray">Support</Text>
              <Text as="p" size="2" color="gray">Feedback</Text>
              <Text as="p" size="2" color="gray">Terms of Service</Text>
              <Text as="p" size="2" color="gray">Privacy Policy</Text>
            </div>
          </div>
        </Grid>
        <div className="mt-12 pt-8 border-t border-gray-200">
          <Text as="p" size="1" color="gray" className="text-center mt-1">
            &copy; {new Date().getFullYear()} CaseBreaker. All rights reserved.
          </Text>
        </div>
      </Container>
    </footer>
    </>
  );
}
