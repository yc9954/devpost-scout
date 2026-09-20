---
slug: "nexusai"
url: "https://devpost.com/software/nexusai"
title: "Nexusai"
hackathon: "Google Cloud Gemini Hackathon"
organization: "Google"
winner: true
words: 350
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/security_privacy"
  - "substrate/geospatial"
---

# Nexusai

> Nexus helps businesses and individuals to transform communication by boosting sales with intelligent AI assistants, securing calls from scammers, and offering 24/7 support all in one platform.

[Devpost](https://devpost.com/software/nexusai) · hackathon [[Google Cloud Gemini Hackathon]]

## Facets

**mechanism** [[human_in_the_loop]] [[realtime_stream]] [[voice_speech]]
**domain** [[security_privacy]]
**substrate** [[geospatial]]

**stack** elevenlab, firebase, gemini, node.js, postgresql, react, twilio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nexusai

## Body

Home page Dashboard Inspiration With scammers going after vulnerable people and businesses overwhelmed with customer inquiries, we wanted NexusAI to be a tool that screens unknown calls, helps spot suspicious ones, and makes handling support calls way easier. What it does NexusAI is a virtual assistant for safer communication. It handles unknown calls by asking key questions, giving users a heads-up afterward with sentiment insights and suggested actions. It’s even smart enough to escalate to a human for sales calls and offers an embeddable chatbot so businesses can provide real-time customer support on their sites. How we built it NexusAI was developed by combining Google Gemini’s AI (Google AI Studio) processing with Twilio for phone number management and call routing. ElevenLab’s advanced text-to-speech was integrated to provide realistic voice responses, while Firebase handles caching for audio files to manage latency. We also used PostgreSQL with a pgvector extension for semantic and sentiment-based call insights. The integration of Google OAuth enables secure user authentication, and Twilio allows call forwarding to seamlessly route unknown callers through NexusAI’s interaction workflow. Challenges we ran into Latency was a pain—initially, it took up to 20 seconds to respond! Switching TTS providers and caching audio helped, but there's still room for improvement. Balancing automated responses with the right timing for human escalation also took a lot of tweaking. And, of course, making sure the whole setup was secure and efficient with Google OAuth was a must. Accomplishments that we're proud of Getting NexusAI ready to launch despite technical challenges and busy schedules (exams & 9-5 job) was a big win. Seeing it handle calls smoothly while providing insights and support really validated my hard work. What we learned I learned how crucial it is to strike the right balance between AI and human support; AI is great, but seamless human handoffs in sales calls make all the difference. Tackling response time gave me a new respect for real-time applications. What's next for Nexusai I am planning to expand NexusAI to more platforms, improve response times, and add even richer analytics to make support even smoother. <div