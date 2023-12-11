'use client'
import React, { useState } from 'react';

const FAQ = () => {
    const [openDropdown, setOpenDropdown] = useState(null);

    const toggleDropdown = (index) => {
        setOpenDropdown(openDropdown === index ? null : index);
    };

    const faqData = [
        {
            question: 'What is the significance of Batik in Indonesian culture?',
            answer: 'Batik holds immense cultural significance in Indonesia, serving as a traditional art form that reflects the country’s diverse heritage. It is considered a symbol of identity, representing different regions and communities through its unique patterns and designs.'
        },
        {
            question: 'How is ESTETIKA reimagining the appreciation for Batik?',
            answer: 'ESTETIKA is revolutionizing the appreciation for Batik by seamlessly blending traditional craftsmanship with modern technology. Through its innovative platform, ESTETIKA empowers users to explore, create, and celebrate the beauty of Batik, ensuring its legacy transcends generations.'
        },
        {
            question: 'Can ESTETIKA be used by individuals with no prior knowledge of Batik art?',
            answer: 'Absolutely! ESTETIKA is designed for users of all levels of expertise. Whether you are a seasoned Batik enthusiast or a newcomer, ESTETIKA provides an intuitive and user-friendly experience, allowing everyone to engage with the artistry of Batik.'
        },
        {
            question: 'How does ESTETIKA contribute to the preservation of cultural heritage?',
            answer: 'ESTETIKA plays a pivotal role in preserving cultural heritage by providing a digital platform for the creation and exploration of Batik. By fostering creativity and awareness, ESTETIKA ensures that the rich traditions and stories embedded in Batik continue to thrive in the contemporary world.'
        },
    ];
    

    return (
        <section className="w-full my-24">
            <div className="relative max-w-screen-xl px-4 sm:px-8 mx-auto grid grid-cols-12 gap-x-6 overflow-hidden">
                <div className="col-span-12 lg:col-span-6" data-aos="fade-right">
                    <div className="w-full">
                        <img src="/getting-started/FAQ.png" alt="" className="w-full" />
                    </div>
                </div>
                <div className="col-span-12 lg:col-span-6 px-4 sm:px-6 mt-8" data-aos="fade-down">
                    <span className="text-base text-indigo-600 font-semibold uppercase mb-4 sm:mb-2">FAQ</span>
                    <h2 className="text-3xl sm:text-4xl font-semibold mb-10 sm:mb-6">Frequently Asked Questions</h2>
                    <ul className="shadow-box">
                        {faqData.map((faq, index) => (
                            <li key={index} className={`relative border-b-2 border-gray-200 ${openDropdown === index ? 'open' : ''}`}>
                                <button
                                    type="button"
                                    onClick={() => toggleDropdown(index)}
                                    className="w-full py-4 text-left focus:outline-none transition duration-300 ease-in-out"
                                >
                                    <div className="flex items-center justify-between">
                                        <span className="font-medium">{faq.question}</span>
                                        <span
                                            aria-hidden="true"
                                            role="img"
                                            className={`material-design-icon chevron-down-icon ${openDropdown === index ? 'rotate' : ''}`}
                                        >
                                            <svg fill="currentColor" width="20" height="20" viewBox="0 0 24 24" className="material-design-icon__svg">
                                                <path d="M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z"></path>
                                            </svg>
                                        </span>
                                    </div>
                                </button>
                                <div className={`dropdown-content ${openDropdown === index ? 'open' : ''}`}>
                                    <p className='text-gray-500 dark:text-gray-400 mb-2'>{faq.answer}</p>
                                </div>
                            </li>
                        ))}
                    </ul>
                </div>
            </div>
        </section>
    );
};

export default FAQ;
