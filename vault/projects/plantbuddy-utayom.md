---
slug: "plantbuddy-utayom"
url: "https://devpost.com/software/plantbuddy-utayom"
title: "PlantBuddy"
hackathon: "Maximally Vibe-a-thon"
organization: "Maximally (https://maximally.in)"
winner: true
words: 602
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/structural_withholding"
  - "mechanism/voice_speech"
  - "domain/finance_payments"
  - "substrate/sensor_telemetry"
---

# PlantBuddy

> 🌱 PlantBuddy - Talk With Plants. PlantBuddy is an AI-powered, IoT-based device that wraps around a plant stem and transforms real plant electrical signals into emotional conversations & music.

[Devpost](https://devpost.com/software/plantbuddy-utayom) · hackathon [[Maximally Vibe-a-thon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[structural_withholding]] [[voice_speech]]
**domain** [[finance_payments]]
**substrate** [[sensor_telemetry]]
  <sub>weak: web_dom</sub>

**stack** css, html, move, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for plantbuddy

## Body

Device PlantBuddy - Web App Device Interface Features 🌱 PlantBuddy is an AI-powered, IoT-based device that wraps around a plant stem and transforms real plant electrical signals into emotional conversations and music. Inspiration Emotional loneliness is rising, yet most digital platforms feel impersonal and often monetize or centralize deeply private data. At the same time, humans naturally feel calm and safe around plants — they are non-judgmental, grounding, and alive. The inspiration for PlantBuddy came from a simple question: What if a plant could become an interface for emotional expression — one that listens, responds, and protects your data instead of exploiting it? We wanted to merge nature, AI, and decentralized technology to create a new kind of interaction where people can talk, express emotions, or create music — while retaining full ownership of their data. What it does PlantBuddy is an AI-powered, IoT-based interactive plant companion. By sensing tiny electrical (capacitive) changes in a real plant when it is touched, PlantBuddy enables two core interaction modes: 🎙️ Talking Mode: Touching the plant activates an AI conversation. The user speaks, speech is transcribed, the AI responds empathetically, and the plant “talks back.” 🎹 Music Mode: Touch intensity modulates sound frequency, allowing users to play the plant like a living piano. All conversations are encrypted locally and stored on Walrus decentralized storage, ensuring privacy and user ownership. Users can optionally opt into anonymous emotional sharing, where encrypted stories can be shared and listened to without revealing identity. PlantBuddy lays the foundation for a decentralized emotional data economy, where users control, share, or monetize their emotional data on their own terms. How we built it Hardware: An Arduino-based capacitive sensing circuit detects micro-variations in plant capacitance caused by human touch. Signal Processing: Touch intensity is mapped to interaction triggers (conversation start) or continuous values (music frequency). AI Layer: Speech is transcribed using Whisper-style speech-to-text. Conversational responses are generated using an LLM (Gemini API). The plant replies via text-to-speech. Security & Storage: Conversation data is encrypted on the client using AES-256. Only encrypted blobs are uploaded to Walrus, ensuring zero-knowledge storage. Web App: A web interface allows users to switch modes, view real-time sensor data, and manage encrypted uploads. Challenges we ran into Noise in capacitive sensing: Plant capacitance is highly sensitive to environment, humidity, and grounding. We had to carefully tune thresholds and filtering to avoid false triggers. Bridging hardware and web reliably: Integrating real-time Arduino signals with a responsive web interface required careful synchronization and buffering. Privacy with AI APIs: Ensuring that AI inference remained ephemeral while long-term storage stayed encrypted required a clean architectural separation. Defining “emotional data” responsibly: We were careful to design sharing as strictly opt-in, anonymous, and user-controlled. Accomplishments that we're proud of Successfully turning a living plant into an interactive AI interface Building two distinct modes (talking + music) from the same sensor input Implementing client-side encryption before decentralized storage Creating a working end-to-end demo: touch → AI response → encryption → Walrus upload Designing a system where no identity is ever required What we learned Plants are surprisingly expressive electrical systems. Privacy-first design must be intentional from day one — it cannot be added later. Combining hardware, AI, and decentralized storage significantly increases complexity, but also unlocks entirely new interaction paradigms. Emotional data needs more protection, not more optimization. What's next for PlantBuddy Miniaturizing the hardware into a clip-on stem device Adding on-chain ownership proofs for devices and datasets Introducing micro-payments and rewards for opt-in emotional data sharing Supporting multiple plants as a distributed emotional network Exploring partnerships in mental wellness, art installations, and ambient computing <div