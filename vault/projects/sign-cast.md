---
slug: "sign-cast"
url: "https://devpost.com/software/sign-cast"
title: "Sign-Cast"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 597
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "user/clinician"
  - "user/general_public"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Sign-Cast

> Bridging the gap between sound and sign—Real-time, Privacy-First, and AI-Powered Accessibility.

[Devpost](https://devpost.com/software/sign-cast) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[voice_speech]]
**domain** [[accessibility]]
**user** [[clinician]] [[general_public]]
**substrate** [[transcript_audio]] [[video_visual]]

**stack** fastapi, groq, openaiwhisper, pytorch, react, sockeye, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for signcast
- created with care for global accessibility.

## Body

SignCast: Real-Time Voice-to-Sign AI Translator Inspiration Communication is a fundamental human right, yet over 70 million Deaf people worldwide face significant barriers in accessing spoken content in real-time. While captions exist, they often fail to capture the nuances of sign language—the primary language for many in the Deaf community. We built SignCast to provide a seamless, private, and powerful bridge between the hearing and Deaf worlds. Our goal was to create a tool that isn't just a translator, but an empowerment platform that works anywhere—from a doctor's office to a live lecture—without compromising user privacy. What it does SignCast is a sophisticated AI-powered application that transcribes spoken English and translates it instantly into two powerful visual formats: SignWriting Notation : A precise, visual script that captures the physical movements, handshapes, and facial expressions of sign language. Animated 2D Poses : Real-time skeletal animations that provide a lifelike representation of signs. Key Features: Real-Time Speech Capture : High-fidelity transcription using local AI models. Intelligent Text Simplification : Leverages cutting-edge LLMs to simplify complex spoken English into sign-friendly structures. Privacy-First (Local AI) : Core translation and transcription models run entirely on the user's device. Professional Export : Download translations as images for educational or documentation purposes. Premium UI : A sleek, modern dashboard with dark mode and responsive design for all devices. How we built it We engineered a high-performance stack to handle the intensive requirements of real-time AI translation: Frontend : Built with React + TypeScript and Vite for blistering speed. Styled with Tailwind CSS for a premium, accessible look. Backend : A high-performance FastAPI server that orchestrates the local AI pipeline. AI Models : OpenAI Whisper : Used for robust, local speech-to-text. Sockeye (NMT) : A Neural Machine Translation model specifically fine-tuned for Text-to-SignWriting conversion. Groq API : Integrated for ultra-fast, optional LLM-based text simplification (using Llama 3.3 / Gemini models). Visualization : @sutton-signwriting for notation rendering and Pose Viewer for skeletal animations. Challenges we ran into Local Inference Latency : Running heavy ML models like Whisper and Sockeye locally while maintaining a snappy UI was a major hurdle. We optimized the pipeline using PyTorch's efficiency tricks and FastAPI's asynchronous architecture. SignWriting Rendering : Rendering complex SignWriting symbols as high-quality SVGs in real-time required deep integration with the Sutton SignWriting engine. Audio Complexity : Handling various audio inputs (System Audio vs. Microphone) across different browsers and OS environments. Accomplishments that we're proud of Low-Latency Sync : The "magic" moment when you speak and see the SignWriting symbols appear almost instantly is something we're incredibly proud of. Aesthetic Integration : We didn't want this to look like a "research tool." We're proud of creating a product that feels like a premium, consumer-ready app. Offline Capability : Demonstrating that high-quality AI shouldn't always require a cloud connection, ensuring better privacy for sensitive conversations. What we learned The Beauty of SignWriting : We dove deep into the world of sign language linguistics and realized how much richer it is than just "hand signals." Learning to represent physical motion in a written script was a fascinating challenge. User-Centric Design : We learned that for an accessibility tool, accessibility in the interface is just as important as the core technology. What's next for SignCast Multilingual Support : Expanding beyond English to support Spanish, ASL, BSL, and more. Holographic Display : Visualizing signs in 3D or AR for a more immersive experience. Mobile App : Dedicated iOS and Android apps for on-the-go translation. Collaborative Sessions : Allowing multiple users to join a translation stream in real-time. Created with care for global accessibility. <div