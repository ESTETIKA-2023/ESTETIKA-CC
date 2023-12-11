'use client'
import React, { useState, useEffect } from 'react';
import { ArrowUpIcon } from 'lucide-react';

const Arrow = () => {
    const [visible, setVisible] = useState(false);

    const handleScroll = () => {
        if (window.scrollY > 20) {
            setVisible(true);
        } else {
            setVisible(false);
        }
    };

    const handleMouseEnter = () => {
        setVisible(true);
    };

    const handleMouseLeave = () => {
        if (window.scrollY <= 20) {
            setVisible(false);
        }
    };

    const handleScrollToTop = () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    useEffect(() => {
        window.addEventListener('scroll', handleScroll);
        return () => {
            window.removeEventListener('scroll', handleScroll);
        };
    }, []);

    return (
        <div
            className={`fixed bottom-4 right-4 z-50 cursor-pointer transition-all group ${visible ? 'transform translate-y-[-2px]' : 'opacity-0 pointer-events-none'
                }`}
            onMouseEnter={handleMouseEnter}
            onMouseLeave={handleMouseLeave}
            onClick={handleScrollToTop}
        >
            <div
                className={`bg-[#232570] text-white p-4 rounded-full ${visible ? 'hover:bg-primary-dark' : ''
                    }`}
            >
                <ArrowUpIcon className='h-6 w-6 transition-transform transform group-hover:-translate-y-0.5' />
            </div>
        </div>
    );
};

export default Arrow;
