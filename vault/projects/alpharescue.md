---
slug: "alpharescue"
url: "https://devpost.com/software/alpharescue"
title: "AlphaRescue"
hackathon: "UC Berkeley AI Hackathon 2025"
organization: "Cal Hacks"
winner: true
words: 729
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/disaster_emergency"
  - "domain/health_clinical"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# AlphaRescue

> First to know, First to act!

[Devpost](https://devpost.com/software/alpharescue) · hackathon [[UC Berkeley AI Hackathon 2025]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[disaster_emergency]] [[health_clinical]]
**user** [[frontline_worker]] [[general_public]]
**substrate** [[geospatial]] [[transcript_audio]] [[video_visual]]

**stack** fetch.ai, gemini, google-maps, groq, mapbox, node.js, python, rag, react.js, supabase, tailwindcss, v0.dev, vapi, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for alpharescue

## Body

Dashboard Inspiration In moments of emergency, every second counts. We were inspired by the idea that AI should be the first to know and the fastest to act . From natural disasters to critical medical needs, we envisioned a system that could assist first responders with intelligent decision-making. Thus, AlphaRescue was born — a smart, responsive, and location-aware emergency dispatch assistant. What it does AlphaRescue is a fully autonomous, AI-powered first responder system that listens to live distress calls, understands the situation, and intelligently coordinates with emergency authorities to dispatch help. A distressed user initiates a call through VAPI , our voice-based AI assistant trained specifically to handle emergency situations and provide immediate, scenario-based guidance. The voice transcripts from VAPI are summarized in real time using Gemini , converting lengthy, unstructured conversations into concise, actionable incident briefs while also detecting potential false alarms. A network of specialized Fetch.ai uAgents then takes over, interacting with each other to evaluate the situation, assess real-time authority availability, and formulate a coordinated plan of action. Each agent is designed to reason, communicate, and make independent decisions — working together to ensure the most effective response is triggered. The agents use a Retrieval-Augmented Generation (RAG) pipeline with Gemini to identify and rank the nearest, most appropriate hospital based on the emergency type and geographic location. Supabase serves as our real-time backend, storing both vector embeddings and structured facility data to support fast, intelligent retrieval. Our specialized agents also use Groq’s ultra-fast LLM to classify the ambulance type required — BLS, ALS, or CCT — ensuring the right unit is dispatched to the scene. These fully autonomous AI agents , built using uAgents , manage the entire downstream flow: summarizing transcripts, selecting facilities, and using VAPI to notify the appropriate authorities — all in a seamless, hands-free manner. A live dashboard , built using Vercel's v0.dev and Mapbox , provides real-time visualization of incidents, responders, and dispatch outcomes. AlphaRescue transforms emergency calls into immediate, intelligent action — combining voice, geospatial reasoning, and autonomous agents to reduce response time and save lives faster. How we built it Agent-based architecture built with Fetch.ai uAgents leveraging AgentVerse platform to simulate communication between emergency dispatch agents. AI-powered classification using Groq's LLM to determine the type of ambulance needed (BLS, ALS, or CCT). AI based summary Leveraged Gemini to summarize verbose VAPI voice call transcripts in real-time. These concise summaries were then fed directly to the uAgents to enhance decision making and reduce cognitive load on the system. Geolocation-based facility selection using geopy and Supabase, built a RAG to find the closest, most suitable facility. Supabase as a real-time backend for storing facility data. Asynchronous system using Python, pydantic , and modern microservice principles. Challenges we ran into Syncing communication between multiple agents in a multi-process async environment . Managing agent registration and compatibility with the Almanac contract . Identifying false spam calls with the help of Gemini and reacting based on it, ensuring genuine calls does not go unattended. Handling LLM classification edge cases and ensuring consistent ambulance type decisions. Real-time Supabase query performance and ENUM filtering . Accomplishments that we're proud of Designed a seamless end-to-end emergency dispatch pipeline powered by AI agents and real-time data. Enabled real-time summarization of live voice calls using Gemini, dramatically reducing LLM input size and improving response latency. Successfully integrated Groq’s blazing-fast LLM to classify medical emergencies with high accuracy. Achieved fast and accurate ambulance dispatch using geospatial filtering and facility prioritization logic. Built a plug-and-play agent ecosystem that can be extended to police, fire, or disaster response domains. ## What we learned How to orchestrate autonomous agents in a distributed, real-time environment using uAgents. Real-world challenges in LLM usage like hallucination, consistency, and prompt design. Importance of summarization pipelines when dealing with long-form audio transcripts in high-pressure scenarios. How to build scalable geolocation-aware search using PostgREST and Supabase. The power of combining structured backend logic with reasoning-driven LLM decision-making. What's next for AlphaRescue Integrate a trust and reputation layer to evaluate and ignore prank/spam calls automatically. Add support for multi-modal inputs like images/videos from users to enhance context and classification accuracy. Extend to support fire and police emergencies with role-specific uAgents and classifiers. Deploy a mobile-first frontend for citizens and responders with real-time tracking and notifications. Train an internal model using fine-tuned incident data for higher accuracy and offline deployments. <div