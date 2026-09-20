---
slug: "emotion-based-music-playlist-generator"
url: "https://devpost.com/software/emotion-based-music-playlist-generator"
title: "Emotion-Based Music Playlist Generator"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 565
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Emotion-Based Music Playlist Generator

> The Emotion-Based Music Playlist Generator is an AI-powered platform that uses facial expression recognition, diary sentiment analysis, and mood-based music recommendations to deliver an experience.

[Devpost](https://devpost.com/software/emotion-based-music-playlist-generator) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: developer_tools</sub>
**substrate** [[geospatial]] [[video_visual]]

**stack** beatoven.ai, node.js, python, react.js, three.js

## Body

Inspiration The idea was born from the realization that music has the power to influence and reflect our emotions. We wanted to create a seamless way for people to connect with their feelings through music, whether it’s uplifting their spirits, calming their minds, or resonating with their current mood. By combining AI technologies like emotion detection and sentiment analysis with interactive 3D visualizations, we aimed to build a platform that offers both functionality and immersion. What it does The Emotion-Based Music Playlist Generator leverages advanced AI techniques to: Analyze facial expressions in real-time via a webcam or uploaded photos to detect emotions. Process diary entries to perform sentiment analysis and understand the user’s reflections. Integrate with the Beatoven.ai API to create mood-specific playlists based on detected emotions and sentiments. Provide a visually immersive experience with interactive 3D stations for different functionalities, such as uploading images, analyzing diaries, or real-time webcam emotion detection. How we built it Frontend: Built using React, Three.js, and @react-three/fiber for interactive 3D visualizations. Integrated Webcam API for live emotion detection. Created dynamic stations for user interactions like uploading images and analyzing diaries. Backend: Developed with Flask to handle API requests and integrate machine learning models. Deployed pre-trained emotion recognition and sentiment analysis models using TensorFlow and NLTK. Leveraged the Beatoven.ai API to fetch music playlists tailored to detected moods. AI Models: Emotion detection using a pre-trained MobileNetV2 model fine-tuned on emotion datasets. Sentiment analysis with NLTK's SentimentIntensityAnalyzer for processing diary entries. Challenges we ran into Webcam Integration: Handling real-time webcam feeds and processing frames efficiently was a challenge. Model Training: Achieving a high accuracy within limited time and computational resources required careful optimization. API Integration: Mapping detected emotions and sentiments to music genres through the Beatoven.ai API required thoughtful design and testing. Frontend Performance: Ensuring smooth 3D interactions and responsive design across devices was tricky with complex visualizations. File Management: Managing model paths and ensuring compatibility across environments led to several debugging sessions. Accomplishments that we're proud of Successfully integrating real-time emotion detection via a webcam. Creating an immersive and interactive 3D user interface using Three.js. Deploying an AI pipeline that seamlessly combines facial emotion recognition, sentiment analysis, and music playlist generation. Achieving a responsive and visually engaging experience for users across devices. Mapping emotions to playlists effectively, providing users with a truly personalized experience. What we learned Frontend: Mastered the use of Three.js for building interactive 3D web applications and integrating real-time webcam functionality. Backend: Improved skills in deploying machine learning models and building scalable APIs with Flask. AI: Learned to optimize pre-trained models for quick training and inference while maintaining accuracy. Teamwork: The importance of collaboration and clear communication across teams to ensure smooth integration of various components. User Experience: Realized the importance of intuitive and visually appealing designs for engaging users. What's next for Emotion-Based Music Playlist Generator Enhanced Real-Time Detection: Improve webcam-based emotion recognition with faster and more accurate models. Expanded Emotion Mapping: Increase the granularity of detected emotions and map them to a wider variety of music genres. Personalized Insights: Add features like daily emotion tracking and mood journaling for self-reflection. Mobile App: Develop a mobile version of the application for easier access on the go. Social Features: Enable users to share playlists and emotions with friends for a collaborative experience. Multilingual Sentiment Analysis: Add support for multiple languages to make the platform accessible globally. <div