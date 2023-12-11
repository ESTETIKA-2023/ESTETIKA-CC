import React from 'react';

const VideoPlayer = () => (
    <iframe
        width="100%"
        height="500px"
        src="https://www.youtube.com/embed/Jq6ictHBH8U"
        title="YouTube video player"
        frameBorder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowFullScreen
    ></iframe>
);

export default VideoPlayer;
