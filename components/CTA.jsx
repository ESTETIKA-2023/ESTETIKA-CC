import React from 'react'
import Container from './Container'
import { Download } from "lucide-react"

const CTA = () => {
    return (
        <Container>
            <div className="flex flex-wrap items-center justify-between w-full max-w-5xl gap-5 mx-auto text-white bg-[#38549c] px-7 py-7 lg:px-12 lg:py-12 lg:flex-nowrap rounded-xl" data-aos="zoom-out-up">
                <div className="flex-grow text-center lg:text-left">
                    <h2 className="text-2xl font-medium lg:text-3xl">
                        Ready to try-out our application?
                    </h2>
                    <p className="mt-2 font-medium text-white text-opacity-90 lg:text-lg">
                        Don&apos;t miss out on the opportunity to experience the beauty of Indonesian Batik!
                    </p>
                </div>
                <div className="flex-shrink-0 w-full text-center lg:w-auto">
                    <a
                        href="https://storage.googleapis.com/estetika-capstone-android-app-bucket/ESTETIKA.apk"
                        target="_blank"
                        rel="noopener"
                        className="py-3 mx-auto text-lg font-medium text-center text-[#38549c] bg-white rounded-md px-7 lg:px-10 lg:py-5 flex items-center justify-center hover:bg-opacity-90 hover:text-[#293e74] dark:hover:bg-white dark:hover:text-[#293e74] dark:hover:bg-opacity-90">
                        Download App <Download size={22} className="ml-2" />
                    </a>
                </div>
            </div>
        </Container>
    )
}

export default CTA