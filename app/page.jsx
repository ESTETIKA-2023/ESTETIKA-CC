'use client'
import { useEffect } from 'react';
import PAS from '@/components/PAS'
import Hero from '@/components/Hero'
import Video from '@/components/Video'
import FAQ from '@/components/FAQ'
import AOS from 'aos';
import 'aos/dist/aos.css';

export default function Home() {
  useEffect(() => {
    AOS.init({
      easing: 'ease-out-cubic',
      offset: 50,
      duration: 1000,
    });
  });
  return (
    <main>
      <Hero />
      <PAS />
      <Video />
      <FAQ />
    </main>
  )
}
