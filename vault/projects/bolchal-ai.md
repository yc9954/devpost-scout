---
slug: "bolchal-ai"
url: "https://devpost.com/software/bolchal-ai"
title: "bolchal.ai"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 735
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "substrate/transcript_audio"
---

# bolchal.ai

> Focus on your work, conversation and let AI handle the rest.

[Devpost](https://devpost.com/software/bolchal-ai) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**substrate** [[transcript_audio]]

**stack** amazon, aws-polly, bedrock, boto3, deepgram, docker, fastapi, livekit-(webrtc), next.js, nova-lite, pinecone, postgresql, python, react

## How they structured the write-up

- inspiration
- what bolchal.ai does
- how it works
- technology stack
- the ai meeting companion concept
- challenges we faced
- what we learned
- what's next
- tagline

## Body

bolchal.ai How It Works Join Meeting Here Video Conferencing Interface Chat Functionality AI Takeover Return To Lobby Bolchal.ai 👻 The Video Meeting Platform with an AI Meeting Companion Inspiration Modern teams rely heavily on video meetings to collaborate, brainstorm, and make decisions. However, one recurring problem we noticed was context loss . People often: Join meetings late Temporarily step away from meetings Miss important decisions or action items When someone returns, they usually ask: "What did I miss?" This disrupts the flow of the meeting and wastes time repeating information. We asked ourselves a simple question: What if meetings had a memory? This idea led to Bolchal.ai — a video conferencing platform with a built-in AI meeting companion that listens, understands, responds when needed, and summarizes discussions so anyone can instantly catch up. What Bolchal.ai Does Bolchal.ai is a real-time video conferencing platform with an AI Meeting Companion that can be toggled on or off during meetings. The AI works like an invisible teammate — keeping track of everything happening so you never lose context. Core Capabilities Feature Description 🎥 Real-time Video Meetings Built-in video conferencing for seamless collaboration 🤖 AI Meeting Companion An AI assistant that joins the meeting and listens to conversations 🔁 Temporary AI Takeover Step away and let the AI listen, respond, and track decisions on your behalf 📝 Smart Meeting Summaries Structured summaries of everything that happened while you were away ⚡ Instant Context Recovery Return to any meeting fully caught up — no need to ask others to repeat How It Works Bolchal.ai combines real-time communication infrastructure with AI-powered conversation understanding . Participants → Video Meeting (WebRTC) ↓ Audio / Conversation Stream ↓ AI Meeting Companion Engine ↓ Speech → Text → Context Analysis ↓ Action Items + Summary Generation ↓ User Returns → Instant Catch-Up The AI continuously processes meeting context but only actively interacts when enabled by the user . Technology Stack Frontend React / Next.js Tailwind CSS Real-time UI updates for live meeting state Real-Time Communication LiveKit for WebRTC-based video conferencing WebSocket signaling for low-latency communication Backend Node.js services Meeting session management AI processing pipelines AI Layer Speech-to-text transcription Natural language understanding LLM-based summarization and response generation Data Storage Meeting transcripts AI-generated summaries Action items and key discussion points The AI Meeting Companion Concept The AI companion acts as a context-preserving layer inside meetings , modeled as: Meeting Intelligence = Speech Recognition + Context Understanding + Knowledge Extraction Speech Recognition — Converts meeting audio into text in real time Context Understanding — Interprets topics, decisions, and conversation threads Knowledge Extraction — Generates summaries and surfaces key insights This transforms raw, unstructured conversations into structured knowledge that anyone can quickly consume. Challenges We Faced 1. Real-Time Communication Infrastructure Handling stable video conferencing required implementing WebRTC with low latency and reliable signaling. Integrating this alongside an AI processing pipeline — without degrading meeting performance — was a significant engineering challenge. 2. AI Context Understanding Meetings are often non-linear. Conversations jump between topics, people interrupt each other, and decisions are made implicitly. Designing prompts and pipelines that extract meaningful summaries from messy, real-world discussions required multiple iterations. 3. Seamless AI Interaction The AI needed to feel helpful but not intrusive . We solved this with a toggle-based assistant model — users activate the AI only when they need it, keeping it invisible during normal flow. 4. User Experience A key UX challenge was making context recovery feel instant and intuitive — not like reviewing a transcript, but like being briefed by a smart colleague. What We Learned Building Bolchal.ai deepened our understanding of: How WebRTC-based video communication platforms are architected The challenges of real-time audio processing at scale How to design AI systems that assist without interrupting human workflows The value of structured, scannable AI outputs over raw transcripts We also realized that the future of meetings isn't just better video — it's intelligent collaboration systems that help teams retain and act on information. What's Next Roadmap Item Description 🤖 Q&A over meetings Ask the AI anything about a past or ongoing meeting 📊 Meeting Analytics Productivity insights, talk-time breakdowns, topic tracking 🔗 Integrations Slack, Notion, Jira, and project management tools 🌍 Multilingual Support Meeting understanding across languages 📅 Auto Task Tracking Automatic follow-ups and action item assignment Our long-term vision: make Bolchal.ai the AI brain for every meeting . Tagline Bolchal.ai — Your AI Meeting Ghost. 👻 <div