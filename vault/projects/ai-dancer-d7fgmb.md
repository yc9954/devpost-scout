---
slug: "ai-dancer-d7fgmb"
url: "https://devpost.com/software/ai-dancer-d7fgmb"
title: "AI Dancer"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 539
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# AI Dancer

> Turn your mood into movement. DanceAI reads your emotions from text and instantly brings them to life with dynamic dance animations — powered by AI and real-time emotion analysis.

[Devpost](https://devpost.com/software/ai-dancer-d7fgmb) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** blender, bolt.new, flask, github, mixamo, netlify, node.js, numpy, python, react, react-three, render, scikit-learn, three.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ai dancer

## Body

Inspiration AI Dancer was inspired by the idea of blending artificial intelligence, emotion recognition, and the universal language of dance. The goal was to create an interactive experience where users could see their feelings transformed into expressive movement, making AI both accessible and fun. The project was motivated by the challenge of mapping text-based emotions to animated 3D characters, bringing together technology and art in a unique way. What it does AI Dancer takes any text input from the user, analyzes it to predict the underlying emotions and their intensity, and animates a 3D character to dance according to those emotions. The character idles by default and springs to life with a unique dance whenever a new emotion is detected. The UI displays the predicted emotions and intensity, providing immediate, visual feedback. How we built it Machine Learning: We used the GoEmotions dataset, mapping 28 fine-grained emotions into 6 broader categories for clarity and accuracy. We trained and tuned models (including a HuggingFace RoBERTa model for emotion and an SVR for intensity) and deployed them for fast inference. Backend: A Python Flask API serves predictions, processing user text and returning emotion categories and intensity scores. The backend is cloud-hosted and leverages HuggingFace for model management. Frontend: Built with React and React Three Fiber for 3D rendering, the UI features a modern, glassmorphism-inspired panel, a stylish input form, and a real-time display of predictions. The 3D character loads separate .glb animation files for each emotion and transitions smoothly between idle and dance states. Animation System: The frontend manages animation state, ensuring only one animation plays at a time and that the character always returns to idle after dancing. Challenges we ran into Animation Switching: Ensuring smooth transitions between idle and dance animations, and handling edge cases like rapid user input or missing animation files. Model Performance: Achieving balanced accuracy across all emotion categories, especially for less common emotions. Frontend-Backend Sync: Keeping the UI in sync with backend predictions and handling asynchronous updates without glitches. UI/UX Polish: Designing a visually appealing, modern interface that works well on all devices. 3D Animation in React: Mastering React Three Fiber and the nuances of 3D animation, lighting, and camera controls. Accomplishments that we're proud of Seamlessly integrating AI-driven emotion recognition with real-time 3D animation. Creating a polished, modern UI that makes the experience engaging and intuitive. Achieving smooth, bug-free animation transitions and robust error handling. Making AI approachable and fun through creative technology. What we learned How to preprocess and map complex emotion datasets for practical applications. The importance of state management and component lifecycle in React, especially with 3D and animation. Techniques for dynamic loading and switching of 3D assets in a web environment. How to design and implement a user-friendly, visually appealing interface. What's next for AI Dancer More Animations: Add more nuanced dances and support for multiple simultaneous emotions. Voice Input: Allow users to speak their feelings and see them danced out. Custom Avatars: Let users choose or customize their 3D character. Mobile Optimization: Further refine the UI and controls for mobile devices. Social Sharing: Enable users to record and share their AI-generated dances. Deeper ML Integration: Experiment with more advanced models and real-time emotion detection from video or audio. <div