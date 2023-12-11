'use client'
import { Button } from "./ui/button"
import { Input } from "./ui/input"
import { Textarea } from "./ui/textarea"
import { User, MailIcon, ArrowRightIcon, MessageSquare } from 'lucide-react'

const Form = () => {
    return (
        <form className="mt-[-11px] flex flex-col gap-y-7">
            <div className="relative flex items-center" data-aos="fade-down" data-aos-delay="100">
                <Input type='email' id='email' placeholder='Email' />
                <MailIcon className="absolute right-6" size={20} />
            </div>
            <div className="relative flex items-center" data-aos="fade-down" data-aos-delay="200">
                <Input type='name' id='name' placeholder='Name' />
                <User className="absolute right-6" size={20} />
            </div>
            <div className="relative flex items-center" data-aos="fade-down" data-aos-delay="300">
                <Textarea type='text' id='text' placeholder='Your Message' className='pt-5' />
                <MessageSquare className="absolute top-5 right-6" size={20} />
            </div>
            <Button className="group flex items-center justify-center gap-x-2 dark:text-white" data-aos="fade-down" data-aos-delay="400">
                <span>Send Message</span>
                <ArrowRightIcon className="transition-transform transform group-hover:translate-x-2" size={16} />
            </Button>


        </form>
    )
}

export default Form