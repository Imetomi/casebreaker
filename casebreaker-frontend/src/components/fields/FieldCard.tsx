'use client';

import { Card, Heading, Text, Button } from '@radix-ui/themes';
import { ChevronRight } from 'lucide-react';
import Image from 'next/image';
import Link from 'next/link';

interface FieldCardProps {
  id: number;
  name: string;
  description: string;
  iconUrl?: string;
}

export function FieldCard({ id, name, description, iconUrl }: FieldCardProps) {
  return (
    <Card size="3" className="flex flex-col h-full">
      <div className="relative w-full h-48 mb-4 overflow-hidden rounded-lg">
        <Image
          src={iconUrl || `/images/placeholder.svg`}
          alt={name}
          fill
          className="object-cover"
          sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
        />
      </div>
      
      <div className="flex flex-col flex-1">
        <Heading as="h3" size="5" mb="2" trim="start">
          {name}
        </Heading>
        <Text as="p" color="gray" size="2" mb="4" className="flex-1">
          {description}
        </Text>
        
        <Link href={`/fields/${id}`} className="mt-auto">
          <Button size="3" className="w-full">
            Explore {name}
            <ChevronRight className="w-4 h-4 ml-1" />
          </Button>
        </Link>
      </div>
    </Card>
  );
}
