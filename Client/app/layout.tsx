import '@/app/globals.css'
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import Providers from './components/Providers/Providers'
import { ToastProvider } from './components/Providers/ToastProvider'

export const metadata: Metadata = {
  title: 'ProjetR'
}

const inter = Inter({ subsets: ['latin'] })

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
      <html lang="en">
          <Providers>
            {children}
          </Providers>
      </html>
  )
}
