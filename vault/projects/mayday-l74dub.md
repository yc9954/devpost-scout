---
slug: "mayday-l74dub"
url: "https://devpost.com/software/mayday-l74dub"
title: "MayDay"
hackathon: "UC Berkeley AI Hackathon 2025"
organization: "Cal Hacks"
winner: true
words: 668
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/disaster_emergency"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# MayDay

> MayDay is the co-pilot and second brain for air traffic control (ATC) powered by AI agents that understand live ATC audio and coordinate real-time suggestions, alerts, and emergency response.

[Devpost](https://devpost.com/software/mayday-l74dub) · hackathon [[UC Berkeley AI Hackathon 2025]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[voice_speech]]
  <sub>weak: simulation_digital_twin</sub>
**domain** [[disaster_emergency]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[structured_db]] [[transcript_audio]]

**stack** claude, fastapi, fetchai, gemini, nextjs, uagents, vapi, websocket

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mayday

## Body

Dashboard Simulated pilot emergency, ATC may dispatch first responders Flight info "End shift" sidebar tab (Letta memory) MayDay diagram Inspiration MayDay was born out of both personal experience and global urgency. With recent aviation incidents and runway incursions on the rise, the need for safer, more robust air traffic communication infrastructure has never been more pressing. One of our team members, Mizan, is a certified private pilot since July 2024 who has spent time inside actual ATC towers in Hayward and Oakland. He’s witnessed firsthand how overwhelming it can be for a single controller to manage communication with dozens of aircraft at once. These real-world experiences helped us better understand the pressure points of current ATC workflows and inspired us to build a solution that directly addresses both human limitations and operational inefficiencies in the control tower. What it does MayDay is a voice-augmented ATC intelligence platform designed to act as a second brain for air traffic controllers -- not a replacement, but a powerful layer of support. It listens to live ATC data , transcribes it using a fine-tuned Whisper model built specifically for aviation communications, and then parses it into structured data using LLMs. From there, autonomous agents analyze the data to detect anomalies, identify conflicts, surface urgent events, and even notify first responders. The goal is to alleviate the intense cognitive load and operational stress on ATC personnel who often juggle dozens of simultaneous instructions, planes, and situations. By providing a clear, intuitive interface that highlights key events and supports handoffs with full context, MayDay offers an extra layer of safety, intelligence, and peace of mind in the tower. How we built it Multi-Agent Architecture : Built on Fetch.ai uAgents, AgentVerse, and ASI:One to create distributed, intelligent agents that handle transcription, parsing, and emergency detection workflows in real-time ATC Transcription Pipeline : Integrated pre-defined English-speaking ATC audio datasets through the fine-tuned jacktol/whisper-medium.en-fine-tuned-for-ATC model with Groq's fast inference Real-time Audio Processing : Python-based FastAPI backend with WebSocket support that streams live ATC audio , processes 5-second chunks, and maintains persistent connections for immediate data flow Emergency Detection Engine : Monitors for anomalies (i.e., runway incursions, communication anomalies, etc.), triggering instant alerts and first responder preparation via Vapi phone call. Frontend : Next.js-powered radar-style interface with real-time WebSocket updates, visualizing aircraft positions, emergency alerts, and communication logs for ATC personnel through multi-agent architecture Challenges we ran into Using and incorporating a wide array of AI products into our project proved to be a big challenge as we had to go through new documentation and concepts quickly. Navigating the different APIs and libraries - from Fetch.ai's uAgents framework to Groq's transcription services to VAPI's voice integration - required rapidly understanding diverse implementation patterns and authentication methods. Coordinating multiple agents communicating via REST APIs and WebSockets while maintaining real-time performance was particularly complex. Managing live audio streams from LiveATC while ensuring consistent processing across varying network conditions and audio quality presented significant technical hurdles. Accomplishments that we're proud of We successfully built a fully functional, real-time ATC monitoring system that listens to live aviation radio traffic, transcribes it accurately, parses it into structured data, and surfaces urgent or anomalous situations using intelligent agents — all within a single integrated platform. We engineered seamless interoperability between multiple cutting-edge technologies, including Groq, Fetch.ai, Gemini, Claude 4, Vapi, and Letta, into a real-time, agentic system, managing live data flows with stability and precision. What we learned This project taught us the complexity of integrating multiple AI services in real-time applications where latency and reliability are critical. We gained deep appreciation for the cognitive load that ATC personnel handle daily and learned to design AI systems that augment rather than replace human decision-making in safety-critical environments. What's next for MayDay ATC System Integration - Deep integration with existing tower infrastructure and communication systems Enhanced Data Integration - Live radar feeds, weather data, and flight plan databases for comprehensive situational awareness Regulatory Approval - Work with aviation authorities toward certification for commercial deployment <div