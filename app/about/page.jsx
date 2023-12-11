'use client'
import React, { useEffect } from 'react'
import SectionTitle from '@/components/SectionTitle'
import Slider from '@/components/Slider'
import AOS from 'aos';
import 'aos/dist/aos.css';

const About = () => {
    useEffect(() => {
        AOS.init({
            easing: 'ease-out-cubic',
            offset: 50,
            duration: 1000,
        });
    });
    return (
        <main>
            <div className='mt-[100px]'>
                <SectionTitle
                    pretitle="Meet The Team"
                    title="Let's get to know the ESTETIKA team">
                    We are a team of students from different universities who come together and collaborate to create a project that can be useful for many people.
                </SectionTitle >
            </div>
            <Slider />
        </main>
    )
}

export default About