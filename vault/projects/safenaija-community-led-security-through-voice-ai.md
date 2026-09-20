---
slug: "safenaija-community-led-security-through-voice-ai"
url: "https://devpost.com/software/safenaija-community-led-security-through-voice-ai"
title: "SafeNaija: Community-Led Security"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 658
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/legal_justice"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# SafeNaija: Community-Led Security

> AI-powered crime reporting for Nigeria. Voice, photo, and text evidence captured, analysed, and dispatched to your community in real time.

[Devpost](https://devpost.com/software/safenaija-community-led-security-through-voice-ai) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[legal_justice]] [[transportation]]
**substrate** [[geospatial]] [[transcript_audio]] [[video_visual]]

**stack** amazon-nova, amazon-web-services, node.js, twilio, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for safenaija: community-led security

## Body

SafeNaija Inspiration The idea for SafeNaija was born from a real incident. One of our team members' sisters' colleagues was kidnapped at a bus stop near Area 11 FCDA junction in Abuja at 6 pm on a regular weekday. Like most crimes in Nigeria, it happened fast, left little evidence, and the response was slow. We kept asking ourselves what if someone nearby had a tool to capture that moment, alert the community, and notify authorities instantly? That question became SafeNaija. What It Does SafeNaija is an AI-powered crime reporting platform that turns any smartphone into a first-response safety tool. Users can report an incident using voice, photo, or text or all three at once. Amazon Transcribe converts spoken witness accounts into structured text, Amazon Nova Lite analyses crime scene photos to identify suspects, vehicles, and weapons, and Amazon Nova Sonic powers a real-time safety chatbot that guides users through the process during an emergency. Every report is synthesised into a structured incident and simultaneously dispatched as a WhatsApp alert, a social media post, and a law enforcement notification in seconds. How We Built It We built SafeNaija as a full-stack web application with React on the frontend and Python FastAPI on the backend. Amazon Bedrock sits at the core of the AI layer, connecting Amazon Nova Lite for visual analysis, Amazon Nova Sonic for real-time conversation, and Amazon Transcribe for speech-to-text. All media files are stored in Amazon S3, incident records are persisted in MongoDB Atlas, and the platform is deployed on Render. The backend orchestrates a multimodal pipeline that processes voice, image, and text inputs in parallel and merges them into a single structured incident report before triggering the report engine. Challenges We Ran Into The biggest technical challenge was building the multimodal pipeline, getting voice, image, and text inputs to be processed in parallel and merged coherently into a single report in real time. Coordinating three different AWS AI services through a single FastAPI backend, handling async responses, and ensuring the final report was structured and readable took significant iteration. We also had to carefully design the UI for high-stress scenarios; the app needs to work for someone who is panicking, so every flow had to be fast, forgiving, and require as few taps as possible. Accomplishments That We're Proud Of We are most proud of the fact that SafeNaija works end-to-end as a real product, not just a demo. A user can open the app, record a voice note in pidgin English, upload a photo, and receive a fully structured AI-generated incident report with visual analysis, transcribed audio, and GPS coordinates all within seconds. We are also proud of building something that feels genuinely relevant to the Nigerian context, from the pidgin English transcription support to the WhatsApp alert integration and the Abuja-specific incident map. What We Learned The most important thing we learned is that AI is most powerful when it removes barriers rather than adds complexity. In a country where emergency lines rarely connect and surveillance infrastructure is almost nonexistent, the value of SafeNaija is not the technology itself it is that the technology gets out of the way and lets people act. We also learned that designing for crisis scenarios demands a completely different mindset to designing for normal use every extra step, every loading screen, every unclear label costs real time in a real emergency. What's Next for SafeNaija: Community-Led Security In the short term we are integrating WhatsApp as a direct reporting channel, so users can submit incidents without downloading the app, and expanding language support to Hausa, Yoruba, and Igbo. In the longer term, our vision is to scale SafeNaija across West Africa, starting with Ghana and Cameroon adapting the platform to each country's language, legal context, and security landscape. For 2.7 billion people in the developing world who live without reliable public safety infrastructure, SafeNaija is a blueprint for what community-led, AI-powered security can look like. <div