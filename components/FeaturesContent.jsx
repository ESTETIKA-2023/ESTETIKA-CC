import React from 'react'
import Container from './Container'

const FeaturesContent = () => {
    return (
        <Container className={`mt-3 flex flex-col justify-center items-center`}>
            <div className='lg:flex items-center gap-x-5 justify-center mb-10'>
                <div
                    className="flex flex-col rounded-lg hover:shadow-2xl dark:hover:shadow-[0_35px_60px_-15px_rgba(255,255,255,0.3)] hover:mt-[-10px] bg-white border border-gray-200 dark:bg-gray-800 dark:border-gray-700 sm:max-w-xl sm:flex-row mb-10 lg:mb-0" data-aos="fade-right">
                    <img
                        className="h-auto w-full rounded-t-lg object-cover md:h-auto md:w-48 md:rounded-none md:rounded-l-lg"
                        src="/features/detection.png"
                        alt="" />
                    <div className="flex flex-col justify-center p-6">
                        <h5
                            className="mb-2 text-center sm:text-start text-xl font-medium text-neutral-800 dark:text-neutral-50">
                            Batik Detection
                        </h5>
                        <p className="mb-4 text-base text-center sm:text-left text-neutral-600 dark:text-neutral-200">
                            This feature is very useful for you to detect Indonesian Batik, you can find out the history of Indonesian Batik, the types of Indonesian Batik, and the meaning of Indonesian Batik.
                        </p>
                    </div>
                </div>
                <div
                    className="flex flex-col rounded-lg hover:shadow-2xl dark:hover:shadow-[0_35px_60px_-25px_rgba(255,255,255,0.3)] hover:mt-[-10px] bg-white border border-gray-200 dark:bg-gray-800 dark:border-gray-700 sm:max-w-xl sm:flex-row" data-aos="fade-left">
                    <img
                        className="h-auto w-full rounded-t-lg object-cover md:h-auto md:w-48 md:rounded-none md:rounded-l-lg"
                        src="/features/batik-article.png"
                        alt="" />
                    <div className="flex flex-col justify-center p-6">
                        <h5
                            className="mb-2 text-center sm:text-start text-xl font-medium text-neutral-800 dark:text-neutral-50">
                            Batik Articles
                        </h5>
                        <p className="mb-4 text-base text-center sm:text-left text-neutral-600 dark:text-neutral-200">
                            This feature offers an insightful journey into the vibrant world of Indonesian Batik, encompassing the latest news, the historical roots of this traditional art form, and its cultural significance.
                        </p>
                    </div>
                </div>
            </div>
            <div className='lg:flex items-center gap-x-5 justify-center'>
                <div
                    className="flex flex-col rounded-lg hover:shadow-2xl dark:hover:shadow-[0_35px_60px_-15px_rgba(255,255,255,0.3)] hover:mt-[-10px] bg-white border border-gray-200 dark:bg-gray-800 dark:border-gray-700 sm:max-w-xl sm:flex-row mb-10 lg:mb-0" data-aos="fade-right">
                    <img
                        className="h-auto w-full rounded-t-lg object-cover md:h-auto md:w-48 md:rounded-none md:rounded-l-lg"
                        src="/features/tourist-experience.png"
                        alt="" />
                    <div className="flex flex-col justify-center p-6">
                        <h5
                            className="mb-2 text-center sm:text-start text-xl font-medium text-neutral-800 dark:text-neutral-50">
                            Batik Tourist Experience
                        </h5>
                        <p className="mb-4 text-base text-center sm:text-left text-neutral-600 dark:text-neutral-200">
                            This feature can help you to find out the tourist experience of Indonesian Batik, allowing you to explore the rich cultural heritage, craftsmanship, and the stories behind each unique batik creation.
                        </p>
                    </div>
                </div>
                <div
                    className="flex flex-col rounded-lg hover:shadow-2xl dark:hover:shadow-[0_35px_60px_-15px_rgba(255,255,255,0.3)] hover:mt-[-10px] bg-white border border-gray-200 dark:bg-gray-800 dark:border-gray-700 sm:max-w-xl sm:flex-row" data-aos="fade-left">
                    <img
                        className="h-auto w-full rounded-t-lg object-cover md:h-auto md:w-48 md:rounded-none md:rounded-l-lg"
                        src="/features/batik-shop.png"
                        alt="" />
                    <div className="flex flex-col justify-center p-6">
                        <h5
                            className="mb-2 text-center sm:text-start text-xl font-medium text-neutral-800 dark:text-neutral-50">
                            Batik e-Commerce
                        </h5>
                        <p className="mb-4 text-base text-center sm:text-left text-neutral-600 dark:text-neutral-200">
                            This feature will collect local batik SMEs in Indonesia, bringing these skilled artisans to the forefront of the global batik industry, and allowing them to showcase their unique creations to the world.
                        </p>
                    </div>
                </div>
            </div>
        </Container>
    )
}

export default FeaturesContent