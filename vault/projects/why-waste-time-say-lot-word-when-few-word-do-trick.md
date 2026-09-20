---
slug: "why-waste-time-say-lot-word-when-few-word-do-trick"
url: "https://devpost.com/software/why-waste-time-say-lot-word-when-few-word-do-trick"
title: "Why waste time say lot word when few word do trick?"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 693
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
---

# Why waste time say lot word when few word do trick?

> Real-time conversation assistant with AI-powered response suggestions and emotional state analysis

[Devpost](https://devpost.com/software/why-waste-time-say-lot-word-when-few-word-do-trick) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[voice_speech]]

**stack** elevenlabs, fastapi, javascript, lava, openai, python, react, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for why waste time say lot word when few word do trick?

## Body

Inspiration “Why waste time say lot word when few word do trick.” — Kevin Malone, The Office . Kevin might’ve been joking, but for many people with speech impediments or communication challenges, saying fewer words can actually make communication smoother, faster, and more accessible. We wanted to build something that not only helps people communicate, but also helps them express their personality and emotion . Because real communication isn’t just about words — it’s about who you are . What it does Few Words Do Trick is an assistive communication platform designed for people with speech impediments or expressive communication difficulties. Unlike traditional AAC (Augmentative and Alternative Communication) tools that focus purely on transmitting speech, our system adds an emotional and personalized layer using real-time EEG emotion detection and MBTI-based personality modeling . From previous research, giving LLMs a persona using the MBTI framework boosts their conversational intelligence by 17–22% . Thus, our system integrates emotional signals from the user’s EEG headset with their personality profile to generate responses that are not only faster and clearer but also more natural and authentic to who they are. This creates a communication experience that feels genuinely human — reflecting tone, mood, and individuality — rather than robotic or generic. By combining neuroscience, machine learning, and personality theory, Few Words Do Trick bridges the gap between accessibility and emotional expression, helping users communicate efficiently and meaningfully in real time. How we built it Our system runs on three main layers: Signal and Emotion Processing , Intelligent Backend , and Frontend Experience . The Signal and Emotion Processing Layer integrates the EEG headset, applies Fourier Transforms and temporal smoothing, and performs emotion classification using power spectrum density analysis and a Random Forest Classifier model. The Intelligent Backend Layer handles speech-to-text and sentence generation using Lava and OpenAI’s GPT-5, as well as text-to-speech synthesis with ElevenLabs (more specifically, Whisper model) for customizable, emotion-aware voices. It’s built with FastAPI and Pydantic for validation, with Vite ensuring a smooth connection between the backend and frontend. The Frontend Experience Layer is built with React and NGROK tunneling. It features a MBTI personality quiz, real-time EEG and voice visualization, and a voice customization dashboard using the ElevenLabs API. The UI is designed to be simple, intuitive, and a little fun — keeping accessibility at the center. Challenges we ran into We faced several challenges throughout development. Microphone and EEG data access proved difficult without deployment, and collecting consistent EEG signals for model training required plenty of creative “method acting” to simulate emotional states. Integrating detected emotions into the real-time speech output pipeline was complex, and setting up a server to merge MBTI personality data with generated responses added another layer of difficulty. On top of that, we had to design a user interface that felt approachable, expressive, and even enjoyable to use. Accomplishments that we're proud of We’re proud to have achieved 90% confidence in our emotion classification using EEG data, as well as successfully integrating multiple APIs across the frontend and backend. We built a fully functional real-time emotion-to-speech pipeline and developed personalized, expressive voice outputs that feel human and authentic. Most importantly, we built something that makes communication more natural and personal — a system that doesn’t just speak for you, but speaks like you. What we learned We learned how to process and classify EEG signals in real time, integrate emotional intelligence into speech systems, and design with empathy in mind. We also realized how vital personalization is in communication — even when powered by AI. And of course, we learned that Kevin Malone’s wisdom can be surprisingly relevant at a hackathon. What's next for Why waste time say lot word when few word do trick? Looking ahead, we plan to expand Few Words Do Trick into a tool for everyday use by integrating portable EEG hardware and refining our emotion models with larger datasets. We also hope to add multilingual and cultural context support and eventually release it as an open-source assistive communication platform. Our goal is to bridge technology and empathy to help everyone express themselves — because sometimes, the fewest words make the biggest difference. <div