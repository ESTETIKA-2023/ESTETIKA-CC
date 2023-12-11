'use client'
import React, { useEffect } from 'react'
import SectionTitle from '@/components/SectionTitle'
import FeaturesContent from '@/components/FeaturesContent'
import AOS from 'aos';
import 'aos/dist/aos.css';

const Feature = () => {
    useEffect(() => {
        AOS.init({
            easing: 'ease-out-cubic',
            offset: 50,
            duration: 1000,
        });
    });
    return (
        <>
            <div className='mt-[100px]'>
                <SectionTitle
                    pretitle="This Our Features"
                    title="Can make it easier for you to find out about Indonesian Batik">
                    There are several features that we provide for you to find out about Indonesian Batik, let's see what features we provide.
                </SectionTitle >
            </div>
            <FeaturesContent />
        </>
    )
}

export default Feature