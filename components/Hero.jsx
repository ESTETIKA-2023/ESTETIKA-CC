import Link from "next/link"
import { Button } from "./ui/button"
import { Download } from "lucide-react"

import {
    RiArrowDownSLine,
} from 'react-icons/ri'

import DevImg from "./DevImg"

const Hero = () => {
    return (
        <section className="mt-[100px] pt-8 xl:py-24 xl:h-[84vh] xl:pt-8 bg-hero bg-no-repeat bg-bottom bg-cover dark:bg-none">
            <div className="container mx-auto">
                <div className="flex flex-col md:flex-row justify-between items-center gap-x-4 md:gap-x-8">
                    <div className="flex flex-col items-center md:items-center lg:items-center xl:items-start max-w-[800px] mx-auto text-center md:text-left">
                        <h1 className="text-3xl md:text-4xl lg:text-5xl xl:text-6xl xl:mb-1 font-bold" data-aos="fade-right">ESTETIKA</h1>
                        <div className="text-xs uppercase font-semibold mb-2 xl:mb-3 text-primary tracking-[2px]" data-aos="fade-right" data-aos-delay="100">(Eksplorasi Tentang Batik Indonesia)</div>
                        <p className="text-sm md:text-center lg:text-lg xl:text-xl xl:text-start max-w-[90vw] mx-auto md:mx-0" data-aos="fade-right" data-aos-delay="200">
                            Embark on a journey of cultural exploration with ESTETIKA, an immersive platform dedicated to the rich heritage of Indonesian Batik.
                        </p>
                        <div className="mt-4" data-aos="fade-right" data-aos-delay="300">
                            <Link href='/'>
                                <Button className="bg-[#38549c] gap-x-2 text-sm md:text-base lg:text-lg xl:text-xl dark:text-white">
                                    Explore Our App <Download className="mt-[6px]" size={22} />
                                </Button>
                            </Link>
                        </div>
                    </div>
                    <div className="hidden xl:flex relative" data-aos="fade-left">
                        <div className="bg-hero_shape2_light dark:bg-hero_shape2_dark w-[180px] h-[180px] md:w-[530px] md:h-[530px] bg-no-repeat absolute -top-1 -right-2"></div>
                        <DevImg containerStyles='bg-hero_shape w-[180px] h-[180px] md:w-[510px] md:h-[462px] bg-no-repeat relative bg-bottom' imgSrc='/hero/person.png' />
                    </div>
                </div>
                <div className="flex flex-col items-center mt-8 xl:mt-18 animate-bounce" data-aos="fade-up">
                    <RiArrowDownSLine className="text-2xl text-primary mb-2" />
                </div>
            </div>
        </section>

    )
}

export default Hero