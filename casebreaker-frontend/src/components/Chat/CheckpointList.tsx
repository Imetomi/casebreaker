'use client';

import * as Checkbox from '@radix-ui/react-checkbox';
import { CheckIcon } from '@radix-ui/react-icons';
import { Text } from '@radix-ui/themes';
import { cn } from '@/lib/utils';

interface Checkpoint {
  id: string;
  title: string;
  description: string;
  hints: string[];
}

interface CheckpointListProps {
  checkpoints: Checkpoint[];
  completedCheckpoints: string[];
  className?: string;
}

export function CheckpointList({
  checkpoints,
  completedCheckpoints,
  className
}: CheckpointListProps) {
  return (
    <div
      role="complementary"
      aria-label="Checkpoint Progress"
      className={cn(
        "w-56 h-fit bg-white rounded-lg border shadow-sm p-4 space-y-4",
        className
      )}
    >
      <h3 className="font-semibold text-gray-900">Checkpoints</h3>
      <div className="space-y-3">
        {checkpoints.map((checkpoint) => {
          const isCompleted = completedCheckpoints.includes(checkpoint.id);
          return (
            <div 
              key={checkpoint.id}
              className="flex items-start gap-2 p-2"
            >
              <Checkbox.Root
                className={cn(
                  "h-5 w-5 rounded border flex items-center justify-center",
                  "transition-colors duration-200",
                  isCompleted
                    ? "border-green-600 bg-green-50"
                    : "border-gray-300 bg-white"
                )}
                checked={isCompleted}
                disabled
                aria-label={`Checkpoint: ${checkpoint.title}${isCompleted ? " (Completed)" : ""}`}
              >
                <Checkbox.Indicator>
                  <CheckIcon className={cn(
                    "h-4 w-4",
                    isCompleted ? "text-green-600" : "text-gray-400"
                  )} />
                </Checkbox.Indicator>
              </Checkbox.Root>
              <label 
                className={cn(
                  "text-sm leading-none pt-0.5 transition-colors duration-200",
                  isCompleted ? "text-green-900" : "text-gray-700"
                )}
              >
                {checkpoint.title}
              </label>
            </div>
          );
        })}
      </div>
      <div className="pt-8 border-t border-gray-100">
        <Text size="2" color="gray">
          Checklist is tracked automatically, solve the case to complete them.
        </Text>
      </div>
    </div>
  );
}
