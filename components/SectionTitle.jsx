import React from "react";
import Container from "./Container";

const SectionTitle = (props) => {
    return (
        <Container
            className={`flex w-full flex-col mt-4 ${props.align === "left" ? "" : "items-center justify-center text-center"
                }`}>
            {props.pretitle && (
                <div className="text-sm font-bold tracking-wider text-indigo-600 uppercase" data-aos="fade-down">
                    {props.pretitle}
                </div>
            )}

            {props.title && (
                <h2 className="max-w-3xl mt-3 text-3xl font-bold leading-snug tracking-tight text-gray-800 lg:leading-tight lg:text-4xl dark:text-white" data-aos="fade-down" data-aos-delay="100">
                    {props.title}
                </h2>
            )}

            {props.children && (
                <p className="max-w-2xl py-4 text-lg leading-normal text-gray-500 dark:text-gray-300" data-aos="fade-down" data-aos-delay="200">
                    {props.children}
                </p>
            )}
        </Container>
    );
}

export default SectionTitle;