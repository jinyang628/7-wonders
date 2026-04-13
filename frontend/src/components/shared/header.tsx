'use client';

import ThemeToggle from '@/components/shared/theme/toggle';

export default function Header() {
  return (
    <header className="flex w-full items-center justify-end gap-4">
      <ThemeToggle />
    </header>
  );
}
