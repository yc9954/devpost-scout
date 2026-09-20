---
slug: "voicemate-tsoj45"
url: "https://devpost.com/software/voicemate-tsoj45"
title: "Voicemate"
hackathon: "Hack for Humanity | 2025"
organization: "Kuba Apps"
winner: true
words: 618
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "substrate/video_visual"
---

# Voicemate

> Seamless Video Calls & Real-Time Translation at Your Fingertips!

[Devpost](https://devpost.com/software/voicemate-tsoj45) · hackathon [[Hack for Humanity - 2025]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**substrate** [[video_visual]]

**stack** dart, figma, firebase, flutter, webrtc

## How they structured the write-up

- what it does
- challenges we ran into

## Body

Inspiration The inspiration behind VoiceMate stems from the growing need for seamless, real-time communication between people who speak different languages. With an increasing number of global interactions, breaking down language barriers became a crucial challenge. I wanted to create an app that not only allowed video calls but also included real-time translation for speech and text, making communication smoother and more inclusive. Whether you're speaking in English, Hindi, or Urdu, VoiceMate empowers users to connect and communicate effortlessly. What it does VoiceMate is an innovative communication app that enables: Real-time video calling through WebRTC. Speech-to-text translation, converting spoken language into text. Text-to-speech functionality that plays translated text in multiple languages. Translation between English, Hindi, and Urdu via the Translated Plus package. Firebase Authentication for user sign-in and secure account management. State management using Provider to manage the app’s data flow. The app is designed to help users communicate without worrying about language differences, whether it’s for personal, professional, or educational purposes. How we built it We built VoiceMate using the following technologies: Flutter: The framework for developing the app, providing a smooth and responsive UI. WebRTC: Used for implementing real-time video calls. Flutter Speech_to_Text: Enabled speech recognition to convert spoken words into text. Translated Plus: Translates text across languages, supporting English, Hindi, and Urdu. Flutter TTS (Text-to-Speech): Converts translated text into spoken language. Firebase Authentication: Used for user authentication and account management. Provider: Implemented for managing the state of the app, ensuring smooth transitions and updates across the app. We combined these technologies to create an intuitive and user-friendly platform that allows for effective communication, regardless of the language. Challenges we ran into While building VoiceMate, we faced several challenges: WebRTC Integration: Implementing WebRTC for smooth video calls was technically challenging, especially ensuring stable connections for real-time communication. Translation Accuracy: Fine-tuning the translation features to ensure accurate translations between English, Hindi, and Urdu was difficult, as certain phrases don’t have direct equivalents. Performance Issues: Handling multiple tasks (video calls, speech recognition, translation, and text- to-speech) at the same time posed performance challenges that required optimization. State Management: Managing app state with Provider in a way that didn't compromise performance and user experience across various functionalities (video calls, translations, and login) was complex. Accomplishments that we're proud of We’re proud of: Successfully implementing real-time video calling and language translation in one app. Creating an app that can support multiple languages (English, Hindi, and Urdu), empowering users to communicate freely across cultural boundaries. Building a user-friendly interface that integrates complex technologies seamlessly for an intuitive experience. Overcoming performance optimization issues to ensure a smooth experience despite resource- intensive tasks like video calling and translation. What we learned Through building VoiceMate, we learned: The complexities of WebRTC and how to implement real-time video calling in Flutter. The power of speech-to-text and text-to-speech technologies, which made real-time translation feasible. How to integrate multiple technologies and services (Firebase, WebRTC, translation APIs) into a cohesive app. Best practices in state management using Provider to ensure the app runs smoothly and data flows correctly. The importance of optimizing performance when working with multiple heavy tasks in an app. What's next for VoiceMate For the future of VoiceMate, we plan to: Expand the language support to include more languages beyond English, Hindi, and Urdu. Add additional video call features such as screen sharing, group calls, and better video/audio quality. Integrate AI-driven voice assistants for a more interactive user experience. Enhance the translation capabilities to offer more precise translations with context-based understanding. Work on performance improvements and optimizing the app for various devices to ensure smooth operation. We’re excited to continue enhancing VoiceMate to make it a more powerful communication tool for people around the world. <div