'use client';

import { Heading } from '@radix-ui/themes';
import type { CaseStudy } from '@/lib/api';
import { useState } from 'react';
import styles from './Flashcard.module.css';

interface ContextViewProps {
  caseStudy: CaseStudy;
}

interface FlashcardProps {
  title: string;
  description: string;
}

function Flashcard({ title, description }: FlashcardProps) {
  const [isFlipped, setIsFlipped] = useState(false);

  return (
    <div
      className="cursor-pointer h-[200px] relative"
      onClick={() => setIsFlipped(!isFlipped)}
      style={{ perspective: '1000px' }}
    >
      <div
        className={`w-full h-full transition-transform duration-500 relative ${styles['transform-style-preserve-3d']} ${
          isFlipped ? styles['rotate-y-180'] : ''
        }`}
      >
        {/* Front side */}
        <div className={`absolute w-full h-full rounded-lg p-6 flex items-center justify-center ${styles['backface-hidden']}`} style={{ backgroundColor: 'var(--cyan-8)' }}>
          <h3 className="text-xl font-semibold text-center text-white">{title}</h3>
        </div>
        
        {/* Back side */}
        <div className={`absolute w-full h-full bg-white rounded-lg p-6 flex items-center justify-center ${styles['rotate-y-180']} ${styles['backface-hidden']}`}>
          <p className="text-gray-600 text-center">{description}</p>
        </div>
      </div>
    </div>
  );
}

export function ContextView({ caseStudy }: ContextViewProps) {
  if (!caseStudy?.contextMaterials?.cards) {
    return null;
  }

  return (
    <div className="flex flex-col h-[calc(100vh-14rem)] max-h-[700px] bg-white rounded-lg border shadow-sm overflow-hidden">
      <div className="flex-1 overflow-y-auto p-4">
        <Heading size="4" mb="6">
          Case Context
        </Heading>
        
        <div className="grid grid-cols-2 gap-4">
          {caseStudy.contextMaterials.cards.map((card, index) => (
            <Flashcard
              key={index}
              title={card.title}
              description={card.description}
            />
          ))}
        </div>
      </div>
    </div>
  );
}
