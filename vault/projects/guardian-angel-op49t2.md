---
slug: "guardian-angel-op49t2"
url: "https://devpost.com/software/guardian-angel-op49t2"
title: "Guardian Angel"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 569
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/security_privacy"
  - "user/patient_family"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Guardian Angel

> Guardian Angel, always by your side.

[Devpost](https://devpost.com/software/guardian-angel-op49t2) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[elder_child_care]] [[health_clinical]] [[labor_employment]] [[security_privacy]]
**user** [[patient_family]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[transcript_audio]]

**stack** deepgram, expo.io, fastapi, google-gemini, node.js, python, react-native, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for guardian angel

## Body

Logo Introduction Stack UI design MVP Inspiration Guardian Angel was born from the need for reliable emergency assistance in an unpredictable world. Our experiences with the elderly, such as our grandparents, who may fall when we’re not around, and the challenges we may face in vulnerable situations motivated us to create a tool that automatically reaches out for help when it’s needed most. We aimed to empower individuals to feel safe and secure, knowing that assistance is just a call away, even in their most vulnerable moments. What it does Core to Guardian Angel, our life-saving Emergency Reporter AI speech app, is an LLM and text-to-speech pipeline that provides real-time, situation-critical responses to 911 dispatchers. The app automatically detects distress signals—such as falls or other emergencies—and contacts dispatch services on behalf of the user, relaying essential information like patient biometric data, medical history, current state, and location. By integrating these features, Guardian Angel enhances efficiency and improves success in time-sensitive situations where rapid, accurate responses are crucial. How we built it We developed Guardian Angel using React Native with Expo, leveraging Python and TypeScript for enhanced code quality. The backend is powered by FastAPI, allowing for efficient data handling. We integrated AI technologies, including Google Gemini for voice transcription and Deepgram for audio processing, which enhances our app’s ability to communicate effectively with dispatch services. Challenges we ran into Our team faced several challenges during development, including difficulties with database integration and frontend design. Many team members were new to React Native, leading to styling and compatibility issues. Additionally, figuring out how to implement functions in the API for text-to-speech and speech-to-text during phone calls required significant troubleshooting. Accomplishments that we're proud of We are proud of several milestones achieved during this project. First, we successfully integrated a unique aesthetic into our UI by incorporating hand-drawn elements, which sets our app apart and creates a friendly, approachable user experience. Additionally, we reached a significant milestone in audio processing by effectively transcribing audio input using the Gemini model, allowing us to capture user commands accurately, and converting the transcribed text back to voice with Deepgram for seamless communication with dispatch. We’re also excited to share that our members have only built websites, making the experience of crafting an app and witnessing the fruits of our labor even more rewarding. It’s been exciting to acquire and apply new tools throughout this project, diving into various aspects of transforming our idea into a scalable application—from designing and learning UI/UX to implementing the React Native framework, emulating iOS and Android devices for testing compatibility, and establishing communication between the frontend and backend/database. What we learned Through this hackathon, our team learned the importance of effective collaboration, utilizing a “divide and conquer” approach while keeping each other updated on our progress. We gained hands-on experience in mobile app development, transitioning from our previous focus on web development, and explored new tools and technologies essential for creating a scalable application. What's next for Guardian Angel Looking ahead, we plan to enhance Guardian Angel by integrating features such as smartwatch compatibility for monitoring vital signs like heart rate and improving fall detection accuracy. We aim to refine our GPS location services for better tracking and continue optimizing our AI speech models for enhanced performance. Additionally, we’re exploring the potential for spatial awareness and microphone access to record surroundings during emergencies, further improving our response capabilities. <div