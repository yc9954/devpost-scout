---
slug: "trishna-climate-smart-kisan-companion"
url: "https://devpost.com/software/trishna-climate-smart-kisan-companion"
title: "Trishna: Climate-Smart Kisan Companion"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 1460
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/agriculture_food"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/clinician"
  - "user/frontline_worker"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Trishna: Climate-Smart Kisan Companion

> Trishna: Multilingual AI super-app for farmers & gardeners. Get hyper-local weather alerts, instant plant disease diagnosis, and personalized crop calendars to tackle climate change sustainably.

[Devpost](https://devpost.com/software/trishna-climate-smart-kisan-companion) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[voice_speech]]
**domain** [[agriculture_food]] [[climate_energy]] [[developer_tools]] [[health_clinical]] [[labor_employment]]
**user** [[clinician]] [[frontline_worker]] [[researcher]]
**substrate** [[geospatial]] [[video_visual]]

**stack** emailjs, google-gemini-api, lucide-react, openstreetmap, react, tailwind-css, typescript, vite

## How they structured the write-up

- elevator pitch
- inspiration
- what it does
- gemini integration & features
- how we built it
- built with
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for trishna: climate-smart kisan companion

## Body

GIF Introducing Trishna -AI companion in the field as every farmer deserves guidance that understands their land, their season, and their voice. Grow with Confidence — your AI companion for every harvest. Weather alerts, disease diagnosis & expert care in your language Welcome back to your climate-smart assistant. Sign in to Trishna and keep growing with confidence Tell us who you are — Farmer or Gardener? Personalised AI recommendations tailored to your growing journey Set your location & language. Get hyper-local weather alerts and crop advice in the tongue you speak best Almost there! Tell us about your garden — balcony or backyard, potting mix or soil. Personalised care starts here Real-time weather for your exact location. Humidity, UV index & 7-day forecasts to plan your perfect harvest Live mandi prices at your fingertips. Know when to sell — rising or falling trends for crops near you Smart Care Schedule — personalised watering reminders & weather alerts tailored to your crops & local conditions Smart Plan — AI-curated crop suggestions for your season, soil & space. From Okra to Chilli, grow what thrives Eco-friendly fertilizer guides with schedules, best practices & AI packet scanning. Grow organic, grow smart Crop encyclopedia with local names — know your Pui Shak from seed to harvest. Water, duration, yield & season info Plant Doctor — snap a photo, get instant AI diagnosis. Your crops' health expert in your pocket, anytime Learn on the go — curated video guides in your language. From organic fertilizers to pest control, master new skills Your Trishna, your way. Switch languages, toggle dark mode & manage your profile — farming made personal Your farming identity, defined. Switch between Farmer or Gardener, update your details & location anytime Build your digital farm. Add crops, set your space, soil & water — Trishna tailors advice to your exact setup Trishna speaks your tongue — 7 languages and counting. Farming wisdom without the language barrier Your voice shapes Trishna. Rate us, report bugs, or suggest features — built by farmers, for farmers Trishna — your climate-smart Kisan companion. Weather, AI diagnosis, crop planning & local language support Trishna: Climate-Smart Kisan Companion Elevator Pitch Trishna is a multilingual, AI-powered super-app that bridges the gap between traditional farming and modern technology. It empowers farmers and home gardeners with hyper-local weather alerts, instant plant disease diagnosis, and personalized crop calendars—helping them navigate climate change with confidence and sustainable abundance. Inspiration I grew up in a farmer's family in India, where agriculture isn't just a livelihood — it's the heartbeat sustaining over a billion lives. I watched my grandparents and parents toil endlessly, wrestling with erratic climate change, crumbling soil health, and that crushing frustration of needing answers right now — but finding none. The high-tech solutions existed, sure. But they were built for agri-corporations, not for us — too complex, too English-heavy, too expensive. I saw smallholder farmers and home gardeners left behind while the world talked about 'AI revolution'. That's when I felt it — Trishna (तृष्णा). In Hindi, it means 'Thirst' — that deep, burning desire for something better. Not just water for crops, but knowledge when you need it, in your language, for your soil, your season, your plot size. I built Trishna to be that bridge — from our ancient farming wisdom to Generative AI's power. Not an app that spits data, but a companion that understands your context and chats back like a trusted friend in the field. Because the future of farming shouldn't be a privilege. It should be a right. What it does Trishna is a comprehensive, multimodal AI assistant designed for both commercial Farmers and home Gardeners. It leverages the Google Gemini API to provide: Smart Weather Alerts: Beyond simple forecasts, Trishna analyzes weather data to generate actionable agricultural advisories (e.g., "High humidity detected; watch out for fungal infections in your tomato crop"). AI Plant Doctor: Users can snap a photo of a sick plant or a soil sample. Trishna analyzes the image to diagnose diseases, identify pests, or evaluate soil texture, offering organic and chemical remedies. Fertilizer Label Scanner: A safety-first feature where users upload photos of pesticide/fertilizer packets. The AI extracts dosage instructions and safety warnings, translating them into simple local language. Context-Aware Crop Planning: Based on the user's soil type (e.g., Red Soil), land size (e.g., 2 Acres vs. Balcony), and water source, it generates a personalized crop calendar and sustainable fertilizer schedule. Multilingual Support: The entire app, including complex AI analysis, works in 10+ Indian languages (Hindi, Marathi, Tamil, etc.) and offers voice-to-text support for accessibility. Market Intelligence: Provides insights on current mandi (market) prices and trends for local commodities. Gemini Integration & Features Trishna is built upon the Gemini 3 architecture ( gemini-3-pro-preview ), leveraging its advanced reasoning and multimodal capabilities to deliver a "Climate-Smart" experience: Multimodal Vision Analysis: We utilize Gemini's vision capabilities for the Plant Doctor and Soil Analysis features. The model processes raw image inputs (leaves, soil texture, fertilizer labels) alongside textual user context (location, season) to provide agronomic diagnoses. Google Search Grounding: To ensure farmers receive the most up-to-date information, we use the googleSearch tool. This is critical for fetching real-time Market Rates (Mandi Prices) and finding relevant, recent educational videos, reducing AI hallucinations regarding dynamic data. Native JSON Output: The application relies heavily on Gemini's responseMimeType: "application/json" capability. This allows us to transform unstructured agricultural advice into strict, type-safe JSON schemas that directly power our UI components (Weather Widgets, Crop Cards, and Advisory Panels). System Instructions & Persona: We leverage Gemini 3's strong instruction-following abilities to switch personas dynamically—acting as a "Meteorologist" for weather, an "Agronomist" for crops, and a "Market Analyst" for prices—while maintaining a localized, empathetic tone suitable for rural users. How we built it We built Trishna as a Progressive Web App (PWA) concept using a modern tech stack: Frontend: React 19 with Vite for a blazing-fast performance. Styling: Tailwind CSS for a responsive, mobile-first design that looks beautiful on low-end devices. We used glassmorphism and organic animations to make the UI feel alive and welcoming. AI Engine: Google Gemini API . We utilized its multimodal capabilities extensively: Text-to-JSON: For generating structured crop plans and weather insights. Vision-to-Text: For the Plant Doctor and Soil Analysis features. Location: Integrated the Browser Geolocation API with OpenStreetMap (Nominatim) for reverse geocoding to provide hyper-local data without needing complex map SDKs. Accessibility: Integrated the Web Speech API for speech-to-text, allowing farmers to ask questions vocally. Built With React - Frontend framework Vite - Build tool and development server Tailwind CSS - CSS framework for styling Google Gemini API - Generative AI model TypeScript - Programming language Lucide React - Icon library EmailJS - Email service OpenStreetMap (Nominatim) - Geocoding API Challenges we ran into AI Hallucinations vs. JSON Structure: Getting the LLM to consistently return valid JSON data for the UI components (like the weather widget and crop cards) was difficult. We had to refine our system prompts significantly to ensure strict schema adherence. Multilingual Nuance: Direct translation of agricultural terms often loses meaning. We had to tune the AI to use colloquial/local agricultural terminology rather than formal dictionary definitions. Image Analysis Latency: Uploading high-res images for analysis can be slow on rural networks. We optimized the prompt engineering to ensure the analysis focuses only on the relevant parts of the image to speed up processing. Accomplishments that we're proud of The "Label Scanner" Feature: We are particularly proud of this safety feature. Misuse of pesticides is a huge health risk; having an AI that can read a label and scream "Wear Gloves!" or "Don't spray near water" in the farmer's native tongue is a potential life-saver. Dual-Persona UX: Successfully creating a UI that adapts its advice based on whether the user is a "Farmer" (Acres, Tractors, Yield) or a "Gardener" (Pots, Aesthetics, Home Care). Visual Design: Creating an interface that feels premium yet accessible, with dynamic weather animations that change based on the data. What we learned Prompt Engineering is Logic: We learned that writing a prompt is like writing code. You need error handling, fallbacks, and strict type definitions within the natural language prompt itself. Empathy in Design: Designing for a farmer requires different priorities than designing for a tech user. Large buttons, voice input, and visual icons are not just "nice to have," they are requirements. What's next for Trishna: Climate-Smart Kisan Companion Offline Mode: Implementing Service Workers to allow farmers to access their crop schedules and saved guides even without an internet connection. Community Grounding: Connecting the AI insights with a "Community" tab where farmers can validate the AI's advice with peers. IoT Integration: In the future, we want Trishna to connect directly to soil moisture sensors to trigger the "Watering Alerts" automatically. <div