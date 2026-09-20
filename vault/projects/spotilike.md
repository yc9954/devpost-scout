---
slug: "spotilike"
url: "https://devpost.com/software/spotilike"
title: "Spotilike"
hackathon: "SpurHacks"
organization: "SPUR & Konfer"
winner: true
words: 837
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/accessibility"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Spotilike

> Spotilike is an AI-powered music app that reads your mood through expressions to play songs that match how you feel. It learns from your skips and smiles to personalize your emotional soundtrack.

[Devpost](https://devpost.com/software/spotilike) · hackathon [[SpurHacks]]

## Facets

**mechanism** [[privacy_tech]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[accessibility]]
**user** [[researcher]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** cursor, deepface, flask, gemini-api, mongodb, next.js, opencv, spotify, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for spotilike

## Body

Intro We drown in choice. 100 million tracks, but none adapt to how we actually feel in the moment. Stressed before an exam → want Lo-Fi focus. Friday win → want hype. Going through heartbreak? → Calm. Spotilike reads your text or face, detects the vibe, and launches the perfect soundtrack. It’s like a DJ who can see your soul. Demonstration Techstack Inspiration Spotilike was inspired by the desire to create a more emotionally intelligent music experience. Traditional recommendation systems rely on genre, artist, or listening history, but often miss the user's current mood. We set out to bridge that gap by using AI to understand real-time emotions and personalize music accordingly. The project combines: Emotion Detection : Real-time facial expression recognition Music Intelligence : Spotify’s music database and recommendation engine Real-time Learning : Adapting recommendations based on user reactions What it does Spotilike is a full-stack app that recommends music based on how you feel and what you’re going through. Real-time Emotion Detection Uses your webcam to detect emotions like happy, sad, angry, or surprised Tracks how you react to songs Learns which songs improve your mood Context-Aware Recommendations Users describe their situation (e.g., “I got a promotion” or “I’m overwhelmed”) Google Gemini AI extracts the mood and topic from the text Matches music to both your emotion and context Smart Playback Control Full Spotify playback control Real-time progress tracking and controls Displays album art and track info Automatic Updates Tracks and updates your emotional responses in real time Uses Server-Sent Events for instant UI feedback How we built it Backend (Python/Flask) Flask API : Handles routes, logic, and Spotify control Spotipy : Integrates Spotify Web API MongoDB : Stores emotions, song scores, and user reactions DeepFace : Detects facial emotion Google Gemini : Analyzes text for mood and topic Frontend (Next.js/React) Next.js 14 with TypeScript Tailwind CSS for styling Responsive UI with live data using SSE Works on both desktop and mobile Key Features Secure Spotify OAuth Real-time emotion detection via webcam Resilient error handling and fallback logic API response caching for performance Challenges we ran into Technical Emotion Detection Balancing speed and accuracy Handling lighting and webcam quality Managing browser permissions and CPU usage Spotify API Handling complex OAuth flow Keeping playback state in sync Database Designing schema to score songs by emotion Real-time writes and reads for fast feedback Real-time Communication Implementing SSE and handling reconnects Keeping frontend and backend in sync UI/UX Making emotion detection feel natural Designing intuitive music controls Responsive layout across devices Balancing functionality with simplicity Accomplishments that we're proud of Technical AI Integration Combined DeepFace and Gemini into one system Spotify Playback Full Spotify control with real-time sync Built a modern, responsive music player Real-time Feedback UI updates instantly based on detected emotion SSE for smooth and efficient updates Error Resilience Graceful fallback systems for AI and API errors Clear error messages and auto-recovery User Experience Clean Interface Spotify-inspired design Mobile-friendly and accessible Emotional Intelligence Learns from how users react Improves over time with context-based recommendations Accessibility Keyboard navigation and screen reader support High contrast, visible feedback What we learned AI Emotion detection is powerful but sensitive to lighting and expression Multiple AI services require good error handling Real-time processing needs performance optimization Music Recommendation Emotions deeply influence music preferences Facial feedback gives useful, real-time user data Spotify API is robust but requires careful handling Full-Stack Dev SSE is a great alternative to WebSockets Managing state across frontend/backend is challenging Error handling is critical for a smooth experience UX Emotionally responsive design boosts engagement Performance is key for music apps Accessibility is easiest when built from the start What's next for Spotilike Short-term (Next 3 months) Better Emotion Detection Detect subtle moods Support for biometric data Improve webcam reliability Deeper Music Understanding Analyze lyrics and song energy Use emotional metadata from music APIs Social Features Share emotion-based playlists Mood-based collaborative sessions See what friends with similar moods are listening to Mid-term (3–6 months) Smarter AI Train models to personalize mood detection Use behavioral data for better recommendations Predict mood changes and suggest music in advance Platform Expansion Launch mobile apps Build a desktop app Integrate with smart speakers Analytics Track mood over time Correlate emotional trends with listening habits Offer insights and playlists based on mood history Long-term Vision (6+ months) AI Music Creation Generate music based on your emotional profile Adjust playback in real-time as your mood shifts Collaborate with AI to create music Ecosystem Integration Connect to smart home devices and wearables Work with health apps for wellness tracking R&D and Community Partner with researchers on emotion-music studies Share findings and open-source our tools Tech Roadmap Performance Move emotion detection to edge devices Optimize AI models for speed Cache music data efficiently Scalability Shift to microservices Cloud deployment with auto-scaling Global CDN support Security & Privacy End-to-end encryption Local-only emotion detection options Full GDPR and privacy compliance Spotilike is building the future of emotionally aware music — where your playlist truly understands how you feel. <div