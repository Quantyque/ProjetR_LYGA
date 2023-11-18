import '@/app/globals.css'
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import Navbar from '@/app/components/Navbar/Navbar'

export const metadata: Metadata = {
  title: 'ProjetR'
}

const inter = Inter({ subsets: ['latin'] })

export default function MainLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <body className={inter.className}>
        <Navbar/>
        {children}
    </body>
  )
}
