import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { Theme } from "@radix-ui/themes";
import "@radix-ui/themes/styles.css";
import { Toaster } from 'sonner';

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
          accentColor="blue"
          grayColor="slate"
          radius="medium"
          scaling="100%"
        >
          <main className="min-h-screen bg-slate-50">
            <Toaster position="top-right" />
            {children}
          </main>
        </Theme>
      </body>
    </html>
  );
}
