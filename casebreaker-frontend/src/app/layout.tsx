import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { Theme } from "@radix-ui/themes";
import "@radix-ui/themes/styles.css";
import { Toaster } from 'sonner';
import { NavbarWrapper } from '@/components/ui/NavbarWrapper';

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
});

export const metadata: Metadata = {
  title: "CaseBreaker - AI-Guided Case Study Learning",
  description: "Interactive case study learning experiences in law, healthcare, and economics",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={`${inter.variable} antialiased`}>
        <Theme
          accentColor="cyan"
          grayColor="mauve"
          radius="large"
          scaling="100%"
        >
          <div className="min-h-screen bg-slate-50">
            <Toaster position="top-right" />
            <NavbarWrapper />
            <main>
              {children}
            </main>
          </div>
        </Theme>
      </body>
    </html>
  );
}
