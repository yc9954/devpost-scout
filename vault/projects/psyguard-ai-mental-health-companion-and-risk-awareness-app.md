---
slug: "psyguard-ai-mental-health-companion-and-risk-awareness-app"
url: "https://devpost.com/software/psyguard-ai-mental-health-companion-and-risk-awareness-app"
title: "PsyGuard AI — Mental Health Companion and Risk Awareness App"
hackathon: "GNEC Hackathon 2026 Spring - Compete For UN-Affiliated/NGO Internships & Prizes"
organization: "Global NGO Executive Committee"
winner: true
words: 629
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/education"
  - "domain/mental_health"
  - "user/clinician"
  - "user/educator_student"
  - "user/social_worker"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# PsyGuard AI — Mental Health Companion and Risk Awareness App

> PsyGuard AI is a mental health companion app that helps users reflect through AI chat, mood check-ins, sleep tracking, trend analysis, and risk awareness while encouraging safer early support.

[Devpost](https://devpost.com/software/psyguard-ai-mental-health-companion-and-risk-awareness-app) · hackathon [[GNEC Hackathon 2026 Spring - Compete For UN-Affiliated-NGO Internships - Prizes]]

## Facets

**mechanism** [[on_device_local]]
  <sub>weak: voice_speech</sub>
**domain** [[education]] [[mental_health]]
**user** [[clinician]] [[educator_student]] [[social_worker]]
**substrate** [[code_repository]] [[structured_db]]

**stack** chat/completions, dart, dio, drift, flutter, flutter-tts, github, gorouter, openai-compatible, riverpod, speech-to-text, sqlite

## How they structured the write-up

- about psyguard ai

## Body

About PsyGuard AI Inspiration PsyGuard AI was inspired by the reality that many students and young people experience stress, anxiety, poor sleep, and emotional pressure, but they may not always notice the warning signs early enough. Some people only realize they are struggling after their mood, sleep, energy, or daily routine has already been affected. We wanted to build a supportive mental health companion that helps users reflect on their daily condition, track emotional and sleep patterns, and receive gentle AI-assisted guidance. The goal is not to replace counselors, therapists, doctors, or emergency services. Instead, PsyGuard AI helps users become more aware of their mental state and encourages safer next steps when risk signals appear. The core idea can be described as: $$ Mental\ Health\ Awareness = Mood\ Check\text{-}ins + Sleep\ Tracking + Chat\ Reflection + Risk\ Observation $$ What it does PsyGuard AI provides several key features: AI companion chat : Responds in a supportive, counselor-like style and can use previous conversation context. Context memory : Reads recent chat history and summarizes older messages when needed. High-risk protection : Detects high-risk language and prioritizes safety guidance and human support resources. Daily check-ins : Records mood, stress, energy, and personal notes. Sleep tracking : Records sleep duration, bedtime, and sleep difficulty. Trend analysis : Shows recent mental and physical changes through charts and AI-generated reports. Local storage : Stores chats, records, and risk snapshots in a local SQLite database. Language settings : Supports English and Traditional Chinese, with English as the default language. Voice settings : Allows users to adjust AI response speech playback speed. How we built it We built PsyGuard AI as a Flutter mobile app. The main application lives inside the psyguard_ai_app directory. Flutter was used for the user interface, while Riverpod manages app state and GoRouter handles navigation. For local data persistence, we used Drift with SQLite, allowing the app to store chat history, daily check-ins, sleep records, and risk snapshots directly on the device. This local-first structure helps protect user privacy and allows the app to maintain useful personal records without depending entirely on cloud storage. For AI features, PsyGuard AI connects to an OpenAI-compatible chat/completions API. The AI is used for companion-style responses, mental health reflection, and trend reports. The app also includes voice-related features using speech_to_text and flutter_tts . What we learned Through this project, we learned that mental health technology must be designed carefully and responsibly. AI can help users reflect and organize their thoughts, but it should never pretend to be a professional therapist or medical service. We also learned how to connect multiple technical systems into one app experience: local databases, state management, navigation, AI chat APIs, multilingual settings, voice playback, and trend analysis. Another important lesson was safety design. When users express high-risk emotions or harmful thoughts, the app should not simply continue normal conversation. It should prioritize safety, encourage human support, and provide clearer next steps. Challenges we faced One major challenge was designing the AI companion so that it feels supportive without becoming unsafe or overconfident. Mental health support requires careful boundaries, especially when users may share sensitive or high-risk thoughts. Another challenge was context memory. We wanted the AI to remember useful conversation context, but long chat histories can become difficult to manage. To solve this, the app reads recent chat history and compresses older messages into summaries when needed. We also faced technical challenges in storing structured mental health records locally, generating useful trend analysis, supporting both English and Traditional Chinese, and integrating voice-related features smoothly. Finally, because the current repository only contains the Flutter client and does not include a standalone backend, production deployment would require a backend proxy in the future to better protect API keys and manage AI requests securely. <div