---
slug: "signspeak-ai"
url: "https://devpost.com/software/signspeak-ai"
title: "SignSpeak AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 625
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "substrate/video_visual"
---

# SignSpeak AI

> Bridging the gap between the Deaf and hearing worlds with real-time AI translation.

[Devpost](https://devpost.com/software/signspeak-ai) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]] [[developer_tools]]
**substrate** [[video_visual]]

**stack** canvas-api, css3, generative-ai, git, google-gemini, html5, react, tailwind-css, typescript, vite, web-speech-api

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for signspeak ai

## Body

Voice & Text => Gesture Inspiration Communication is a fundamental human right, yet for the millions of people who rely on Sign Language, daily interactions with non-signers remain a significant challenge. We often see tools that translate speech to text, but very few that truly bridge the visual gap for the Deaf community in real-time. I was inspired to build SignSpeak to create a true two-way bridge. I didn't want just a translation tool; I wanted to build a conversation enabler that empowers Deaf users to be understood instantly and helps hearing users learn and communicate back visually. The goal was to make accessibility seamless, modern, and respectful. What it does SignSpeak is a bidirectional AI communication assistant powered by Google Gemini: Sign-to-Speech (For Deaf Users): The app accesses the webcam to monitor hand gestures in real-time. It captures video frames, analyzes the specific ASL signs using Multimodal AI, and instantly converts them into spoken audio and text. Speech-to-Sign (For Hearing Users): It listens to spoken English (or text input) and generates visual references (images) of how to sign those words back. This allows a hearing person to reply in a way the Deaf user understands natively. How I built it I built SignSpeak using a modern, performance-focused stack: Frontend: Developed with React (Vite) and TypeScript for type safety and speed. AI Engine: Integrated Google Gemini 1.5 Flash (via the Google GenAI SDK). I leveraged its "multimodal" capabilities to process raw image data directly from the HTML5 Canvas, rather than relying on traditional, brittle computer vision models. Styling: Used Tailwind CSS to create a clean, "Glassmorphism" UI that focuses on readability and accessibility. Browser APIs: Utilized the MediaDevices API for camera control, Canvas API for frame compression (to save bandwidth), and the Web Speech API for native Text-to-Speech and Speech-to-Text conversion. Challenges I ran into API Rate Limits: Handling the quota limits of the Gemini API was the biggest hurdle. The app would often crash when sending too many video frames. I solved this by implementing a smart Cooldown System and a "Demo Mode" architecture that gracefully handles 429 errors without breaking the user experience. Latency vs. Accuracy: Balancing the need for real-time feedback with the processing time of an LLM was tricky. I optimized this by scaling down video frames on the client side before sending them to the cloud, reducing token usage and latency significantly. Prompt Engineering: Teaching the AI to distinguish between a "resting hand" and an active sign required rigorous testing of system instructions. Accomplishments that I'm proud of Seamless Multimodal Integration: Successfully connecting a live webcam stream to a Generative AI model and getting accurate text responses back feels like magic. Bidirectional Flow: Most hackathon projects only do one side (video-to-text). I am proud that I built both sides so a full conversation can actually happen. Resilient Error Handling: Building a robust error state (the "Rate Limit Hit" screen) that informs the user instead of just crashing the screen. What I learned I learned how to manage Multimodal RPC payloads, converting Base64 image data efficiently for API consumption. I gained a deeper appreciation for Accessibility UI design—realizing that high contrast and clear visual feedback are critical for this specific user base. I learned how to implement client-side throttling to respect API quotas while keeping the UI responsive. What's next for SignSpeak AI Continuous Sentence Parsing: Currently, the model excels at single words/phrases. The next step is implementing a context window to understand full ASL sentences and grammar. 3D Avatar Generation: Replacing static reference images with a WebGL-based 3D avatar that can perform fluid sign animations for smoother Speech-to-Sign translation. Mobile App: Porting the logic to React Native to make this a pocket companion for users in the real world. <div