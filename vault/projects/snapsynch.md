---
slug: "snapsynch"
url: "https://devpost.com/software/snapsynch"
title: "SnapSynch: Transform Any Video into Highlights with Ease"
hackathon: "2024 TikTok TechJam"
organization: "TikTok"
winner: true
words: 701
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
  - "substrate/transcript_audio"
---

# SnapSynch: Transform Any Video into Highlights with Ease

> Ever wished for Ctrl + F in videos? SnapSynch uses AI to quickly find and compile key clips based on your prompts. Perfect for sports highlights, custom trailers, and efficient content creation!

[Devpost](https://devpost.com/software/snapsynch) · hackathon [[2024 TikTok TechJam]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[transcript_audio]]

**stack** amazon-ec2, amazon-web-services, certifi, fastapi, ffmpeg, moviepy, next.js, openai, python, sklearn, tailwind, vercel, whisper

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for snapsynch

## Body

What is SnapSynch? Development Technologies After pressing "+" on the homepage, there will be a new feature "SnapSynch" that creates Highlight video in one click! Tell us your crucial moments! Wait for the magic to happen! Highlight result! Post it on TikTok! TikTok's homepage Inspiration The inspiration came from our daily lives as students. We often found ourselves wishing for a "Ctrl + F" function for videos, especially for lengthy lecture recordings. Searching for specific parts of a lecture manually is time-consuming. Additionally, as sports enthusiasts, we dreamed of making our own highlight videos from lengthy matches. Movie lovers can also easily create their own trailer using this feature! Hence, we developed SnapSynch to make everyone's dream happen. What it does SnapSynch is an intelligent video editing assistant that leverages advanced machine learning and generative AI technologies to transform the way we interact with video content. By analyzing videos based on user-defined prompts, SnapSynch instantly finds and compiles the most relevant clips, thereby making video editing not only effortless but also highly efficient. This innovative tool is particularly well-suited for a variety of users, including sports enthusiasts who want to highlight key moments from their favorite matches, movie lovers aiming to create custom trailers, and content creators and marketers seeking to produce compelling content quickly and effectively. At the core of SnapSynch is its ability to understand and process natural language prompts using state-of-the-art generative AI models. This allows the tool to accurately identify and extract video segments that match the user's intent, whether it’s finding every goal in a soccer match or pinpointing the most dramatic scenes in a movie. By combining these powerful AI capabilities with user-friendly functionality, SnapSynch provides a seamless and intuitive video editing experience that significantly reduces the time and effort typically required in manual editing processes. How we built it We built SnapSynch using a combination of technologies and tools: Python for the core logic and processing. OpenAI GPT-4 for natural language processing and generating captions based on video content. Whisper for accurate audio transcription. MoviePy for video editing and manipulation. Concurrent.futures for parallel processing to speed up the analysis and editing. FFmpeg for handling video and audio processing tasks. Sklearn for implementing machine learning models. Cosine Similarity for measuring the similarity between user prompts and video content. Certifi and custom SSL context to ensure secure network requests. We also used several helper libraries like yt_dlp for downloading videos and requests for making API calls. Challenges we ran into Initially, we aimed to directly convert the entire video to text for processing (using BLIP-2). However, due to hardware limitations and the high cost of processing large videos, we had to split the videos into frames and take snapshots from the front, middle, and back of each segment. This approach required additional logic to ensure accuracy and synchronisation but ultimately provided a more feasible solution. Accomplishments that we're proud of We're proud of creating a tool that significantly simplifies the video editing process. SnapSynch not only reduces the time required to edit videos but also makes advanced editing accessible to users without specialized skills. The seamless integration of machine learning for video analysis and the ability to handle user-defined prompts are key accomplishments. We are also proud to have developed a user-friendly interface that allows everyone to use the platform easily. What we learned Throughout this project, we learned a great deal about video processing, as well as integrating machine learning models for natural language processing. We also gained valuable experience in optimising performance for handling large datasets and parallel processing. What's next for SnapSynch We plan to enhance the machine learning models for even more accurate video analysis and adding support for more video formats and platforms. We also plan to explore real-time video processing capabilities so that this feature can be used for even more usage such as creating highlight video from live streaming, whether it is gaming live streams or just normal content creator live streams. Integrating more advanced editing features like transitions, effects, and audio enhancements is also part of our future plans. SnapSynch has the potential to revolutionise video editing, and we're excited about its future development! Try out SnapSynch <div