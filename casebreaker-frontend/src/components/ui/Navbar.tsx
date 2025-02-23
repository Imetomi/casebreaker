import { Button, Container, Flex, Heading, Link, Text } from '@radix-ui/themes';
import NextLink from 'next/link';

export function Navbar() {
  return (
    <div className="sticky top-0 z-50 backdrop-blur-xl bg-white/90 border-b border-ruby-200/50 shadow-sm">
      <Container size="4">
        <Flex justify="between" align="center" py="4">
          <NextLink href="/" passHref legacyBehavior>
            <Link>
              <Heading size="5">
                <Text color="ruby" highContrast as="span">Case</Text><Text color="blue" as="span">Breaker</Text>
              </Heading>
            </Link>
          </NextLink>
          <Flex gap="4" align="center">
            <NextLink href="/fields" passHref legacyBehavior>
              <Link>Fields</Link>
            </NextLink>
            <NextLink href="/about" passHref legacyBehavior>
              <Link>About</Link>
            </NextLink>
            <Button variant="solid">Get started</Button>
          </Flex>
        </Flex>
      </Container>
    </div>
  );
}
