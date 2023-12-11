'use client'

import { motion } from "framer-motion"
import useScrollProgress from "@/hooks/useScrollProgress"

const variants = {
    hidden: { opacity: 0 },
    enter: { opacity: 1 },
}

const Template = ({ children }) => {
    const completion = useScrollProgress()
    return (
        <>
            <motion.main variants={variants} initial='hidden' animate='enter' transition={{type: 'linear', delay: 0.2, duration:0.4}}>
                {children}
            </motion.main>
            {/* Completion bar */}
            <span style={{transform: `translateY(${completion - 100}%)`}} className="fixed z-50 bg-[#38549c] dark:bg-primary w-1 top-0 right-0 bottom-0 transition-all duration-700"></span>
            <div className="h-auto"></div>
        </>
    )
}

export default Template