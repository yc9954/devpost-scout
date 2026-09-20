---
slug: "moodmelodyai"
url: "https://devpost.com/software/moodmelodyai"
title: "MoodMelody.AI"
hackathon: "2024 TikTok TechJam"
organization: "TikTok"
winner: true
words: 814
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/code_repository"
  - "substrate/transcript_audio"
---

# MoodMelody.AI

> An AI web app that automatically generates a mood-based background music soundtrack for your TikTok videos to customise your internet presence and appealingly convey your message to your audience.

[Devpost](https://devpost.com/software/moodmelodyai) · hackathon [[2024 TikTok TechJam]]

## Facets

**substrate** [[code_repository]] [[transcript_audio]]

**stack** api-integration, assembly-ai, figma, flask, gemini, github, hugging-face, javascript, material-ui, musicgen-small-model, musicpy, python, react, s3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for moodmelodyai

## Body

Web App Landing Page 1 Web App Landing Page 2 Web App Create Music Page Tech Workflow Diagram Sentiment Analysis on Video Content Figma Landing Page Figma Create Music page Figma Create Music page with AI-gen Video TechStack Inspiration Our project aims to revolutionize how we experience video content by seamlessly integrating custom-generated music that aligns with the video's emotional tone. Imagine uploading a video and receiving a perfectly matched soundtrack that enhances the viewer's emotional journey. This is the innovation we aspire to create. As huge fans of the Inside Out 2 movie, we decided to centre our entire product on the idea that emotion-based content creation can help content creators connect with their audience. In the hustle and bustle of our daily lives, music has the power to evoke emotions, calm our minds, and enhance our experiences. We wanted to leverage this powerful medium to create an innovative tool that combines the art of music with the science of AI. Inspired by the idea of translating human emotions captured in videos into personalized music tracks, we embarked on the journey of creating MoodMelodyAI. Our goal was to build a solution that not only understands the emotions conveyed in videos but also enhances them with custom-generated music, providing a unique and immersive experience for users. What it does MoodMelodyAI is an AI-powered application that generates custom music based on the emotional content of video transcripts. Here’s how it works: User Uploads a Video: Users start by uploading a video to the MoodMelodyAI platform. Video-to-Transcript Conversion: The uploaded video is converted into a text transcript using the Assembly AI API. Sentiment Analysis: The transcript is analyzed to determine the dominant emotions conveyed in the video using TensorFlow and Gemini AI API. Music Generation: Based on the identified emotions, MoodMelodyAI generates a custom music track that complements the mood of the video using a Hugging Face AI music gen model. Downloadable Link: The generated music is then combined with the video, and users are provided with a download option to the final product. How we built it GitHub Repository: We finalized and set up our project repository on GitHub to manage and track our code collaboratively. UI/UX Design: Initial designs were created in Figma, focusing on an intuitive and aesthetically pleasing user interface. API Research: We researched and selected appropriate APIs for converting video to transcripts. Backend Development: We set up the foundation of our backend using Flask's web server, providing a robust and scalable environment for our application. Frontend Development: We employed React.js and Material UI for the front end, ensuring a dynamic and responsive user experience. Music Generation: Leveraged AI models, including those from Tensorflow, Gemini AI API, Hugging Face's open-source model facebook/musicgen-small and musicpy, to create custom music tracks based on emotional analysis. Challenges we ran into API Integration: Integrating multiple APIs and ensuring seamless communication between them posed a significant challenge. Emotion Analysis Accuracy: Achieving accurate sentiment analysis from transcripts to generate appropriate music tracks required extensive tuning and testing. Time Constraints: Balancing the project’s scope with the limited timeframe of the hackathon was challenging, leading to the prioritization of core features over additional functionalities. File Size Management: Handling large video files and ensuring efficient processing and storage within practical limitations was another key challenge. Hosting Issues: We ran out of time to host the frontend and backend, so for now users would have to clone the repo and follow instructions on the README file to test out our web app. Accomplishments that we're proud of Functional Prototype: Successfully developed a functioning prototype that can analyze video transcripts and generate custom background music tracks. Collaborative Effort: The team worked collaboratively across time zones, making critical decisions and overcoming obstacles together. User-Friendly UI: Created an intuitive and aesthetically pleasing user interface that enhances user experience. Time Management: We were able to submit our functioning web app on time for the hackathon :) What we learned API Integration Skills: Improved our skills in integrating and working with various APIs. AI and Sentiment Analysis: Gained deeper insights into AI-driven sentiment analysis and its applications in creative projects. Time Management: Learned the importance of prioritizing tasks and managing time effectively within the constraints of a hackathon. Collaborative Development: Enhanced our ability to work as a cohesive team, communicating effectively and sharing responsibilities. What's next for MoodMelodyAI Facial Emotion Recognition: Expand the project to include facial emotion recognition for a more comprehensive analysis of the video’s emotional content instead of only pertaining to textual mood analysis. Enhanced Music Generation: Improve the music generation algorithms to produce even more personalised and high-quality music tracks. Scalability: Optimize the platform to efficiently handle larger, longer videos. User Feedback Integration: Gather user feedback to refine and enhance the application’s features and usability. Mobile Application: Develop a mobile version of MoodMelodyAI to reach a wider audience and provide on-the-go accessibility. <div