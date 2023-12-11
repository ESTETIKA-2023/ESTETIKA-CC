import React from 'react'
import { MailIcon, MapPinIcon, PhoneCall } from 'lucide-react'
import Form from './Form'

const ContactForm = () => {
    return (
        <div className='container ps-5 mx-auto px-4 sm:px-6 lg:px-8 lg:pt-2 mt-[100px]'>
            <div className='grid grid-cols-1 md:grid-cols-2 pt-12 md:h-[480px] mb-6 md:mb-24'>
                <div className='flex flex-col justify-center'>
                    <div className='flex items-center gap-x-4 text-primary text-lg mb-4' data-aos="fade-right">
                        <span className='w-[30px] h-[2px] bg-primary'></span>
                        <div>Need More Information ?</div>
                    </div>
                    <h1 className='h1 max-w-xl mb-8' data-aos="fade-right" data-aos-delay="100">Let's Contact Us Now </h1>
                    <p className='subtitle max-w-[600px]' data-aos="fade-right" data-aos-delay="200">
                        Just contact us if you have any questions, suggestions or anything else. This below you can use form to contact us, dont worry we will not share your email to anyone. We will reply your email as soon as possible, thank you.
                    </p>
                </div>
                <div className='hidden lg:flex w-full bg-contact_illustration_light dark:bg-contact_illustration_dark bg-contain bg-top bg-no-repeat' data-aos="fade-left">
                </div>
            </div>
            {/* batas */}
            <div className='grid xl:grid-cols-2 mb-24 xl:mb-32'>
                {/* batas 2 */}
                <div className='flex flex-col gap-y-4 xl:gap-y-14 mb-12 xl:mb-24 text-base xl:text-lg'>
                    <div className='flex items-center gap-x-8' data-aos="fade-up" data-aos-delay="100">
                        <MailIcon size={18} className='text-primary'/>
                        <div>estetikateam2023@gmail.com</div>
                    </div>
                    <div className='flex items-center gap-x-8' data-aos="fade-up" data-aos-delay="200">
                        <MapPinIcon size={18} className='text-primary'/>
                        <div>Indonesia</div>
                    </div>
                    <div className='flex items-center gap-x-8' data-aos="fade-up" data-aos-delay="300">
                        <PhoneCall size={18} className='text-primary'/>
                        <div>+6282356473812</div>
                    </div>
                </div>
                <Form />
            </div>
        </div>

    )
}

export default ContactForm