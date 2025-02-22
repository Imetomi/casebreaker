import { Container, Heading, Text } from '@radix-ui/themes';
import { BackButton } from '@/components/ui/BackButton';
import { Chat } from '@/components/Chat/Chat';

export default function CaseChatPage() {
  return (
    <Container size="4" className="py-12">
      <BackButton />
      
      <div className="mb-8">
        <Heading size="8" className="mb-4" highContrast>
          The Miranda Rights Case
        </Heading>
        <Text size="4" as="p" color="gray">
          Discuss the case with our AI tutor to deepen your understanding.
        </Text>
      </div>

      <Chat 
        initialMessage="Welcome! I'm here to help you analyze the Miranda Rights case. Let's start by discussing the historical context of this landmark decision.

What aspects of the Miranda v. Arizona case would you like to explore first?
1. The facts of the case
2. The Supreme Court's decision
3. The impact on law enforcement
4. Modern applications

Feel free to ask any questions!"
      />
    </Container>
  );
}
