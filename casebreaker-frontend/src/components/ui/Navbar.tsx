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
                <Text color="mauve" highContrast as="span">Case</Text><Text color="cyan" as="span">Breaker</Text>
              </Heading>
            </Link>
          </NextLink>
          <Flex gap="6" align="center">
            <Flex gap="4" align="center">
              <NextLink href="/about" passHref legacyBehavior>
                <Link>About</Link>
              </NextLink>
              <NextLink href="/fields" passHref legacyBehavior>
                <Link>Fields</Link>
              </NextLink>
              <NextLink href="/custom-case" passHref legacyBehavior>
                <Link>Custom Case</Link>
              </NextLink>
              <NextLink href="/pricing" passHref legacyBehavior>
                <Link>Pricing</Link>
              </NextLink>
            </Flex>
            <NextLink href="/fields" passHref legacyBehavior>
              <Button variant="solid" asChild>
                <Link className="cursor-pointer">Get started</Link>
              </Button>
            </NextLink>
          </Flex>
        </Flex>
      </Container>
    </div>
  );
}
