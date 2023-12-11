'use client'
import ContactForm from '@/components/ContactForm'
import React, { useEffect } from 'react'
import AOS from 'aos';
import 'aos/dist/aos.css';

const Contact = () => {
    useEffect(() => {
        AOS.init({
            easing: 'ease-out-cubic',
            offset: 50,
            duration: 1000,
        });
    });
    return (
        <>
            <ContactForm />
        </>
    )
}

export default Contact