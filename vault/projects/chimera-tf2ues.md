---
slug: "chimera-tf2ues"
url: "https://devpost.com/software/chimera-tf2ues"
title: "Chimera"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 529
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/media_journalism"
  - "user/legal_professional"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Chimera

> A frankenstack of your digital footprint with a spooky twist.

[Devpost](https://devpost.com/software/chimera-tf2ues) · hackathon [[Kiroween]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[media_journalism]]
**user** [[legal_professional]]
**substrate** [[transcript_audio]] [[video_visual]]

**stack** elevenlabs, framer-motion, raindrop, react, strands-agents, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chimera
- testing credentials

## Body

Feed the Footprint - 2 Feed the Footprint - 1 Front Page Processing Front Page- Ready to Listen Inspiration We were inspired by the idea of a "digital memory monster" - what if your personal data could be resurrected and queried in an interactive, slightly spooky way? The concept of Frankenstein's creature learning from the world around it became our metaphor for an AI system that absorbs your digital footprint and surfaces forgotten memories on demand. What it does Chimera is a voice-activated digital memory retrieval system that queries across your personal data sources (Gmail, browser history, photos, and audio recordings) using natural language. Users speak a query into the microphone, and Chimera's Strands Agent processes the request across multiple data sources, retrieving relevant memories and articulating responses through an AI voice powered by Elevenlabs. The interface features a Halloween-themed design with spooky animations, making the experience of excavating your digital past feel appropriately eerie. How we built it We constructed Chimera using React + Vite for a responsive frontend with Framer Motion for smooth, theatrical animations. The RAG (Retrieval-Augmented Generation) pipeline is powered by Raindrop platform, which handles indexing and semantic search across diverse data sources. We integrated Amazon's Strands Agents SDK to orchestrate queries and Elevenlabs integration that provides the natural-sounding voice synthesis for the monster's responses. The entire stack is containerized with Docker. Challenges we ran into Multi-source data normalization : Consolidating data from Gmail, browser history, photos, and audio into a unified format for the RAG pipeline required careful design. Voice synthesis latency : Balancing real-time responsiveness with high-quality audio generation from Elevenlabs. State management complexity : Coordinating multiple async operations (listening → processing → audio playback) while maintaining smooth UI feedback. Spooky UX that still works : Making the interface visually Halloween-themed while keeping it intuitive and functional. Accomplishments that we're proud of Successfully integrated three complex external services (Raindrop, Strands Agents, Elevenlabs) into a cohesive workflow. Created a polished, animated UI that feels both fun and functional - the visual feedback during processing states really sells the "monster working" concept. Built a production-ready containerized deployment that can be instantly shared and demoed. The audio visualizer and real-time status updates create genuine engagement when the system is "speaking." What we learned Orchestrating multiple AI/ML services requires careful attention to async flows and error handling. Framer Motion is incredibly powerful for creating engaging, theatrical UX that actually improves usability. The "spooky theme" isn't just cosmetic - it makes the data retrieval experience feel more memorable, turning a potentially creepy concept into something delightful. RAG pipelines work best when data sources are well-structured and semantically consistent beforehand. What's next for Chimera Expanded data sources : Integration with Spotify listening history, social media archives, and calendar events. Pattern memory : Storing and learning from query patterns to improve future retrievals. Multi-voice mode : Different monster personalities with distinct voices for different data sources. Mobile app : Bringing Chimera to iOS/Android for on-the-go memory resurrection. Collaborative mode : Sharing memories and queries with friends, building a "collective digital consciousness." Fine-tuning : Training custom voice models to make output even more character-appropriate. Testing Credentials Email: judge@kiroween.com Password: chimerakiro <div