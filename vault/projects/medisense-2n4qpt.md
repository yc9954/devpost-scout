---
slug: "medisense-2n4qpt"
url: "https://devpost.com/software/medisense-2n4qpt"
title: "MediSense"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 703
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# MediSense

> Tap, don't type—AI-powered symptom analysis that speaks your language and respects your heritage.

[Devpost](https://devpost.com/software/medisense-2n4qpt) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[elder_child_care]] [[health_clinical]]
**user** [[clinician]] [[educator_student]]
**substrate** [[geospatial]] [[structured_db]]

**stack** express.js, gemini, health, node.js, react, web

## How they structured the write-up

- summary
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for medisense

## Body

Landing Organ/Muscle Selection Symptom Selection Symptom Detail Medical History Follow Up Questions Results Medisense (Advanced AI-Based Symptom Analyzer) Summary An advanced AI-based symptom analyzer that revolutionizes how people assess their health concerns. By eliminating complex medical jargon and text-based inputs, we've created an intuitive, tap-based interface with interactive body diagrams. Our system intelligently gathers precise information through guided symptom selection, optional medical history, and smart follow-up questions, all powered by AI. The platform delivers comprehensive results, including potential conditions, severity assessments, and personalized recommendations from both modern medicine and Asian traditional healing systems (Sasang and Chinese Traditional Medicine), making healthcare guidance accessible across languages and cultures. Inspiration Existing symptom checkers felt like interrogations—users struggling to describe pain, not knowing muscle names, typing endless messages into chatbots that couldn't understand their urgency or language. We saw students suffering through late-night health anxieties, parents confused about their children's symptoms, the elderly managing chronic conditions without guidance, and rural communities traveling hours for basic consultations. But the real spark? Realizing that while AI promised a healthcare revolution, it was ignoring billions who don't speak English fluently and dismissing centuries of Asian medical wisdom. As someone from Pakistan, I wanted to build something that doesn't just diagnose—it bridges cultures, languages, and traditions. What it does Our symptom analyzer transforms health assessment into a simple, guided journey: Interactive Body Selection : Users tap on an anatomical diagram exactly where they feel discomfort—no need to know if it's the "trapezius" or "lumbar region." Intelligent Triage : Gemini AI instantly analyzes whether medical history is needed for accurate assessment Smart Follow-ups : Dynamic, contextual questions that gather precise information through simple taps and selections Comprehensive Analysis : Delivers detailed insights on potential conditions with severity levels Cultural Integration : Provides both modern medical guidance AND recommendations from Sasang Constitution Medicine and Chinese Traditional Medicine Bilingual Interface : Ensures accessibility for non-English speakers across Asia Everything happens through taps and selections—zero typing required. How we built it Frontend : React for an intuitive, responsive interface with interactive SVG body diagrams Backend : Node.js with Express for robust API handling AI Engine : Google Gemini (latest version) for symptom analysis and intelligent questioning Privacy-First Architecture : MERN stack with NO database connections all processing happens in real-time with zero data storage Localization : Bilingual system supporting English and regional languages Medical Integration : Custom algorithms combining modern diagnostic criteria with traditional medicine principles Challenges we ran into The biggest challenge was designing a workflow that balances simplicity with medical accuracy. We had to: Create an intelligent system that knows WHEN to ask for medical history vs. when symptoms alone suffice Map thousands of symptoms to body parts in an intuitive visual interface Integrate vastly different medical philosophies (Western, Sasang, TCM) into coherent recommendations Ensure the AI asks the RIGHT follow-up questions without overwhelming users Maintain complete privacy without database storage while still delivering personalized results Accomplishments that we're proud of 🎯 Eliminated the typing barrier —anyone, regardless of medical knowledge or language proficiency, can use it 🌏 Cultural bridge —we're the first to integrate Asian traditional medicine with AI diagnostics at scale 🔒 Privacy-perfect —zero data storage means users can assess sensitive symptoms without fear 🧠 Smart workflow —our AI doesn't just answer; it knows what questions to ask and when 🌍 Accessibility —bilingual support makes healthcare guidance available to billions What we learned Medical AI isn't just about accuracy—it's about meeting people where they are (linguistically, culturally, educationally) Privacy can be a feature, not a compromise Traditional medicine and modern AI aren't opposites—they're complementary when integrated thoughtfully The best UX eliminates choices users shouldn't have to make (like "how do I describe this pain?") Building for your own culture's needs often creates solutions that work globally What's next for Medisense Immediate Full deployment with expanded language support and refined traditional medicine recommendations Short-term Integration with telemedicine platforms for seamless doctor consultations Symptom tracking over time for chronic condition management Community health insights while maintaining individual privacy Long-term Partnerships with healthcare providers in underserved regions Expansion to other traditional medicine systems (Ayurveda, Unani) AI training on region-specific health patterns and conditions Making quality health guidance a fundamental right, not a privilege <div