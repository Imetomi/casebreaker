'use client';

import { TypeAnimation } from 'react-type-animation';

export function AnimatedHeading() {
  return (
    <span className="inline-block min-w-[120px] transition-all duration-200">
      <TypeAnimation
        sequence={[
          'for exams',
          2000,
          'to diagnose',
          2000,
          'jurisdiction',
          2000,
          'investing',
          2000,
          'marketing',
          2000,
          'art & history',
          2000,
        ]}
        wrapper="span"
        speed={50}
        repeat={Infinity}
        className="text-cyan-500 font-bold"
      />
    </span>
  );
}
