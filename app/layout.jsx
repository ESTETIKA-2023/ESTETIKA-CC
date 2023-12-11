import { Inter } from 'next/font/google'
import './globals.css'
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import CTA from '@/components/CTA'
import { ThemeProvider } from '@/components/ThemeProvider'
import Arrow from '@/components/Arrow'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'ESTETIKA',
  description: 'Enriching the world with Indonesian Batik culture',
  icons: {
    icon: '/favicon.ico',
  },
}

export default function RootLayout({ children }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={inter.className}>
        <ThemeProvider attribute="class" defaultTheme='light'>
          <Arrow />
          <Header />
          {children}
          <CTA />
          <Footer />
        </ThemeProvider>
      </body>
    </html>
  )
}
