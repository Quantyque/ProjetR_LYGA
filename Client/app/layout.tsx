import '@/app/globals.css'
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import Navbar from './components/Navbar/Navbar'
import Providers from './components/Providers/Providers'

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
        <body className={inter.className}>
          <Providers>
            <Navbar/>
            {children}
          </Providers>
        </body>
      </html>
  )
}
