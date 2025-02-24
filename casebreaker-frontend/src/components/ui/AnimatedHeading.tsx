'use client';

import { TypeAnimation } from 'react-type-animation';

export function AnimatedHeading() {
  return (
    <span className="inline-block min-w-[200px]">
      <TypeAnimation
        sequence={[
          'for exams',
          200,
          'to diagnose',
          200,
          'jurisdiction',
          200,
          'investing',
          200,
          'marketing',
          200,
          'art & history',
          200,
        ]}
        wrapper="span"
        speed={50}
        repeat={Infinity}
        className="text-cyan-500 font-bold"
      />
    </span>
  );
}
