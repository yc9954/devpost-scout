---
slug: "smartkisan"
url: "https://devpost.com/software/smartkisan"
title: "SmartKisan"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 769
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "user/frontline_worker"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# SmartKisan

> SmartKisan: An AI-powered digital assistant that helps Indian farmers make smarter decisions with real-time crop advice, disease detection, and market insights.

[Devpost](https://devpost.com/software/smartkisan) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[voice_speech]]
**domain** [[agriculture_food]] [[civic_government]]
**user** [[frontline_worker]]
**substrate** [[document_pdf]] [[geospatial]] [[sensor_telemetry]]

**stack** arduino/esp32-compatible, asyncstorage, expo-av, expo-speech, expo.io, i18n-js, iot, json-data-files, react-hooks, react-native, react-native-stylesheet, react-navigation, sensors, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for smartkisan

## Body

Real sensor integration, Arduino/Microcontroller setup Farm overview, crop cards, tasks, quick actions Voice commands, quick actions My Crops, health badges, disease alerts Smart stats, soil types, watering schedule AI assistant, suggestions, chat history Health dashboard, crop status, scan options Alerts by type & severity, timestamps Inspiration India’s farmers are increasingly surrounded by smartphones, cheap sensors, and government digital initiatives, yet most still rely on word-of-mouth or local traders for critical decisions like when to irrigate, sell, or apply for schemes.[web:18][web:21] We wanted to build something that feels like talking to a trusted village expert, but powered by structured data and a clean mobile UX. SmartKisan was born from the idea that farmers should be able to simply speak in Hindi/Hinglish and get clear, actionable answers instead of scrolling through confusing tables and PDFs. What it does SmartKisan is a mobile-first, voice-enabled assistant for Indian farmers. It lets farmers ask questions in Hindi/Hinglish using a global floating mic button and then routes those queries to features like mandi prices, government schemes, irrigation guidance, crop health, and alerts. The app tracks market prices (with trends and best mandi suggestions), helps farmers navigate government schemes with eligibility checks, provides a crop health overview with disease flows, and includes a smart irrigation module that can incorporate IoT sensor data (soil moisture, environment) where available.[web:18][web:16] How we built it We built SmartKisan as a React Native + Expo app using TypeScript, React Navigation, and i18n-js for bilingual support. The project is organized into screens (Dashboard, Market Prices, Schemes, Irrigation, Health, Alerts, Assistant), reusable components (like a global FloatingMicButton and VoiceModal ), and service modules for core logic ( intentRouter , mandiService , schemeService , voiceService , etc.). Voice input and TTS are handled using Expo’s audio and speech libraries, with a simple intent router that normalizes Hindi/Hinglish commands and maps them to navigation/actions. Data such as mandi prices, schemes, and farmer profiles are stored in JSON/TypeScript structures, with AsyncStorage used for caching and offline support. The irrigation and crop health modules are designed to consume either mock data or real sensor readings from IoT hardware via an API layer.[web:16] Challenges we ran into Designing for a voice-first, Hindi/Hinglish interface was harder than just adding speech on top of English UI strings. We had to handle mixed-language phrases (“wheat ka bhav”, “rog dikhao”), regional vocabulary, and short, command-style inputs in a way that still mapped reliably to intents. Balancing realism and scope was another challenge: true end-to-end disease detection, weather integration, and live IoT feeds require full ML pipelines and backend infrastructure, so we focused on a solid mobile app architecture with mocked but realistic data and clear extension points. Finally, building an offline-friendly experience for rural connectivity constraints forced us to think carefully about caching, fallback behavior, and keeping the UX simple enough that the user never feels “lost” inside the app.[web:21][web:18] Accomplishments that we're proud of We’re proud that SmartKisan feels like a cohesive product rather than a collection of disconnected screens. The voice assistant is tightly integrated into navigation, so farmers can truly drive the app by speaking instead of tapping through deep menus. The bilingual content, scheme eligibility logic, mandi price flows, and irrigation calculations all work together to provide context-aware help rather than just raw data. We’re also happy with how we designed for IoT from day one: even though the current build uses mock sensor data, the UI, services, and assets are aligned with actual field hardware integration.[web:16] What we learned We learned that building for farmers means prioritizing trust, clarity, and offline resilience over flashy features. Voice UX for Hindi/Hinglish users requires careful intent design and vocabulary mapping, not just generic NLP. Working with agricultural use cases also reinforced how important explainability is: showing trends, multipliers, or reasons for eligibility builds confidence in the system. On the technical side, structuring the app around services and mock data made it much easier to imagine how real APIs, ML models, and IoT streams would plug in later without a full rewrite.[web:18][web:21] What's next for SmartKisan Next, we plan to plug in real ML models for crop disease detection, integrate weather and market APIs, and connect actual field sensors (soil moisture, temperature, humidity) through a backend so irrigation and health logic can run on live data.[web:16] We also want to add more Indian languages, push notifications for critical alerts, and a basic backend (e.g., Firebase/Node) for syncing data and analytics. Finally, we aim to pilot SmartKisan with real farmers to validate assumptions, refine voice flows and thresholds, and iterate toward a tool that can be trusted in daily agricultural decision-making.[web:18] <div