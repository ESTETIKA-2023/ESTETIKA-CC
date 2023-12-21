import React from 'react'
import SectionTitle from './SectionTitle'

const PAS = () => {
    return (
        <div className='px-2 sm:px-0 2xl:px-[90px]'>
            <SectionTitle
                pretitle="Problem and Solution"
                title="Why do we have to discuss Indonesian batik">
                We want to invite people to get to know, love and support Indonesian batik through our app. By combining modern technology and local wisdom, we want to create a unique and valuable exploration experience.
            </SectionTitle>
            <section className="relative max-w-full sm:mx-4 xl:mx-10 my-2 border-[1.5px] shadow-xl sm:rounded-2xl overflow-hidden">
                <div className="w-full py-1 flex flex-col items-center" data-aos="zoom-in">
                    <div className="relative w-full flex flex-col lg:flex-row items-center justify-between space-y-12 lg:space-y-0 px-4 xl:px-10 my-8 sm:mt-8">
                        {/* Dataset Batik Section */}
                        <div className="max-w-[280px] xl:max-w-[363px] space-y-6 sm:space-y-3 text-center">
                            <img src="/getting-started/batik-indonesia.png" alt="" className="max-w-[245px] mx-auto" />
                            <h3 className="text-xl text-gray-800 dark:text-white font-semibold">Dataset Batik Indonesia</h3>
                            <p className="text-sm text-gray-500 dark:text-gray-300 leading-relaxed">
                                We have a large collection of Indonesian batik data that you can explore and learn about
                            </p>
                        </div>

                        {/* AI Section */}
                        <div className="max-w-[280px] xl:max-w-[363px] space-y-6 sm:space-y-3 text-center">
                            <img src="/getting-started/ai.png" alt="" className="max-w-[245px] mx-auto" />
                            <h3 className="text-xl text-gray-800 dark:text-white font-semibold">Artificial Intelligence</h3>
                            <p className="text-sm text-gray-500 dark:text-gray-300 leading-relaxed">
                                With the help of artificial intelligence, we can recognize batik patterns and predict the type of batik
                            </p>
                        </div>

                        {/* Mobile App Section */}
                        <div className="max-w-[280px] xl:max-w-[363px] space-y-6 sm:space-y-3 text-center">
                            <img src="/getting-started/mobile-app.png" alt="" className="max-w-[245px] mx-auto" />
                            <h3 className="text-xl text-gray-800 dark:text-white font-semibold">Mobile App</h3>
                            <p className="text-sm text-gray-500 dark:text-gray-300 leading-relaxed">
                                The results of the exploration can be accessed through the mobile app that we have provided
                            </p>
                        </div>

                        <img src="/getting-started/arrow.png" alt="" className="arrow hidden absolute top-32 left-64 xl:left-[22rem] w-24 xl:w-[9.5rem]" />
                        <img src="/getting-started/arrow.png" alt="" className="arrow hidden absolute top-32 right-64 xl:right-[22rem] w-24 xl:w-[9.5rem]" />
                    </div>
                </div>
            </section>
        </div>
    )
}

export default PAS