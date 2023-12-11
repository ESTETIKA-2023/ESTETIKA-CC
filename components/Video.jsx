'use client'
import { useState, useEffect } from 'react';
import dynamic from 'next/dynamic';
import Container from './Container';
import SectionTitle from './SectionTitle';

const DynamicVideoPlayer = dynamic(() => import('./VideoPlayer'), { ssr: false });

const Video = () => {
    const [playVideo, setPlayVideo] = useState(false);

    useEffect(() => {
        setPlayVideo(true);
    }, []);

    return (
        <Container>
            <div className='w-full lg:my-12 max-w-7xl mx-auto lg:flex lg:justify-between lg:items-center'>
                <div className='lg:w-1/2 lg:pr-16 lg:items-start'>
                    <SectionTitle
                        align="left"
                        pretitle="Revitalizing Traditional Elegance"
                        title="Unveiling Batik Harmony - The Essence of ESTETIKA"
                    >
                        By participating in the #BangkitElevatorPitch, we aspire to capture attention and gather support to propel ESTETIKA into the next phase, where we envision a global appreciation for the art of batik. Let's unite in preserving cultural elegance and keeping the tradition alive with ESTETIKA!
                    </SectionTitle>
                </div>
                <div className='lg:w-1/2' data-aos="fade-left">
                    <div className="w-full mx-auto overflow-hidden rounded-2xl">
                        <div
                            onClick={() => setPlayVideo(!playVideo)}
                            className="relative bg-indigo-300 cursor-pointer aspect-w-16 aspect-h-9 bg-gradient-to-tr from-purple-400 to-indigo-700"
                        >
                            {playVideo && (
                                <DynamicVideoPlayer />
                            )}
                        </div>
                    </div>
                </div>
            </div>
        </Container>
    );
};

export default Video;
