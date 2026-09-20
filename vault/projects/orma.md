---
slug: "orma"
url: "https://devpost.com/software/orma"
title: "Orma"
hackathon: "Google Chrome Built-in AI Challenge"
organization: "Google"
winner: true
words: 534
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/educator_student"
  - "substrate/structured_db"
---

# Orma

> Orma is your browser's memory layer that transforms how you learn online. Instantly capture, understand, and chat with your browsing history using AI, making digital knowledge truly personal.

[Devpost](https://devpost.com/software/orma) · hackathon [[Google Chrome Built-in AI Challenge]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[supply_logistics]]
**user** [[developer]] [[educator_student]]
**substrate** [[structured_db]]

**stack** chrome, googlenano, openai, react, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for orma

## Body

The Story Behind Orma Inspiration As a passionate learner who spends hours browsing the web, I found myself constantly struggling with the same problem: I would discover amazing information, only to forget where I found it days later. Browser bookmarks became a graveyard of forgotten tabs, and note-taking apps felt disconnected from my browsing experience. I wanted something that could remember not just what I saved, but understand it, connect it, and help me learn better. That's when I had the idea for Orma (meaning "Memory" in Malayalam) – a browser extension that would act as my digital memory, understanding and connecting everything I learn online. What it does Orma is a sophisticated memory layer for your browser that transforms how you capture and interact with online information. Using AI, it automatically processes and connects your browsing history, allowing you to: Save anything with one click Search using natural language Chat with your browsing history Generate smart summaries Create project workspaces automatically Enhance AI tools like ChatGPT with perfect context How we built it I built Orma using a carefully selected stack to ensure both performance and elegance: Frontend : React 18 with TailwindCSS for a native-feeling interface AI Processing : Google Nano AI for lightning-fast local processing Memory Storage : IndexedDB via Dexie for reliable vector storage Search : Vector search powered by OpenAI Embeddings Extension : Chrome Extensions Manifest V3 The architecture focuses on offline-first capabilities while maintaining real-time responsiveness. Every interaction is designed to provide immediate feedback with smooth animations. Challenges we ran into Vector Storage : Implementing efficient vector storage in IndexedDB was tricky. I had to carefully optimize the storage and retrieval mechanisms to maintain performance with growing data. Real-time Processing : Balancing immediate user feedback with AI processing was challenging. I solved this by implementing a queue system with visual feedback. Context Management : Ensuring that saved memories maintained their original context while being useful for AI interactions required several iterations of the embedding pipeline. Extension Performance : Keeping the extension lightweight while handling complex processing was tough. I leveraged Chrome's built-in AI capabilities to reduce the load. Accomplishments that we're proud of Built a fully functional memory system that actually enhances learning Achieved near-instant search across thousands of memories Created a natural chat interface for browsing history Implemented smooth, real-time updates with beautiful animations Designed an intuitive interface that gets out of your way What we learned Deep insights into vector databases and embeddings Techniques for efficient browser extension development Strategies for combining local and cloud AI processing The importance of user feedback in memory management systems Methods for maintaining context in AI-powered applications What's next for Orma Collaborative Memory Spaces : Enable teams to build shared knowledge bases Advanced Learning Analytics : Provide insights into learning patterns Cross-browser Support : Expand beyond Chrome Offline AI : Enhance local processing capabilities API Ecosystem : Allow developers to build on top of Orma Orma is more than just a project – it's a step toward enhancing human memory with AI in a way that feels natural and empowering. We believe technology should enhance our natural abilities, not replace them, and Orma is our contribution to this vision. <div