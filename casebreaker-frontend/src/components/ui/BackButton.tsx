'use client';

import { Button } from '@radix-ui/themes';
import { ChevronLeft } from 'lucide-react';
import { useRouter } from 'next/navigation';

export function BackButton() {
  const router = useRouter();

  return (
    <Button
      variant="soft"
      onClick={() => router.back()}
      className="mb-6"
    >
      <ChevronLeft className="w-4 h-4 mr-1" />
      Back
    </Button>
  );
}
