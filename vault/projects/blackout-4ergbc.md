---
slug: "blackout-4ergbc"
url: "https://devpost.com/software/blackout-4ergbc"
title: "Blackout"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 823
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/transportation"
  - "substrate/geospatial"
---

# Blackout

> AI That Works & Learns Even When the Internet Doesn't

[Devpost](https://devpost.com/software/blackout-4ergbc) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[retrieval_grounding]]
  <sub>weak: sensor_fusion</sub>
**domain** [[developer_tools]] [[disaster_emergency]] [[transportation]]
**substrate** [[geospatial]]
  <sub>weak: sensor_telemetry, web_dom</sub>

**stack** 2b, api, arize, css, dexie.js, docker, fastapi, gemini, gemma, git, github, google, html, indexeddb

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for blackout

## Body

Sign In Page Intelligence Hub Settings Page Offline Window Online Window Inspiration BLACKOUT was inspired by a simple but critical question: What happens when AI is needed the most, but the internet is unavailable? During natural disasters, infrastructure failures, remote travel, or emergency situations, connectivity is often unreliable precisely when access to information is most important. Most AI assistants become completely unusable without an internet connection. We wanted to create an AI system that gracefully adapts across the entire connectivity spectrum—using powerful cloud models when online, local language models when offline, and a growing knowledge base when no model is available. The goal was to ensure that users always have access to intelligent assistance, regardless of network conditions. What it does BLACKOUT is a connectivity-aware AI assistant that automatically adapts to changing network conditions. When internet connectivity is available, BLACKOUT uses Google's Gemini API to provide powerful cloud-based responses. If internet access is unavailable, it seamlessly switches to a locally running Gemma 2 2B model through Ollama. If neither cloud access nor the local model is available, BLACKOUT falls back to an offline knowledge base powered by retrieval-augmented generation (RAG). The system also collects user feedback through thumbs-up and thumbs-down interactions, allowing the offline knowledge base to continuously improve over time. This ensures that even in complete connectivity blackouts, users can still receive meaningful and contextually relevant assistance. How we built it BLACKOUT was built using a modern full-stack architecture. The frontend was developed with Next.js 14, React 19, and Tailwind CSS, providing a responsive chat interface and adaptive connectivity monitoring. The backend was built with FastAPI and deployed on Railway using Docker containers. For online intelligence, we integrated Google's Gemini API. Offline intelligence is powered by Gemma 2 2B running through Ollama. User feedback and synchronization data are stored using MongoDB, while client-side offline storage is handled through IndexedDB using Dexie.js. To overcome browser security restrictions preventing deployed websites from accessing localhost services, we developed a lightweight local proxy that bridges the deployed frontend and the user's local Ollama instance while supporting CORS and Private Network Access (PNA) requirements. The entire AI pipeline is monitored using Arize Phoenix, providing observability, tracing, and evaluation capabilities for both online and offline inference paths. Challenges we ran into One of the biggest challenges was Browser Private Network Access (PNA). Modern browsers block HTTPS applications from directly accessing localhost resources, preventing our deployed frontend from communicating with a user's local Ollama instance. Solving this required building a dedicated local proxy with proper CORS and PNA headers. We also encountered Gemini API rate limits that temporarily blocked online inference, forcing us to design more resilient fallback mechanisms. Another challenge involved integrating Arize Phoenix observability. Authentication and collector endpoint configuration issues required extensive debugging before traces could be successfully captured. Deployment also presented difficulties. Railway's port handling and Docker runtime behavior required careful configuration to ensure the application could correctly bind to dynamically assigned ports in production environments. Accomplishments that we're proud of We successfully built a true connectivity-spectrum AI system that continues functioning even when internet access disappears. BLACKOUT can automatically transition between cloud AI, local AI, and knowledge-base-powered responses without requiring user intervention. We also implemented a complete feedback-driven improvement loop that enables offline responses to become more useful over time. Another major accomplishment was overcoming browser security limitations to enable communication between a deployed web application and locally running AI models. This allows users to benefit from local inference while still using a cloud-hosted interface. Finally, we successfully integrated observability and tracing throughout the AI workflow, giving us visibility into how requests move across different intelligence layers. What we learned Throughout development, we learned that building resilient AI systems involves much more than integrating language models. We gained a deep understanding of browser networking constraints, Private Network Access policies, and cross-origin communication challenges. We also learned the importance of observability and monitoring in AI applications, especially when requests may follow multiple execution paths. The project reinforced the value of retrieval-augmented generation over model fine-tuning for offline improvement. Instead of retraining models, we discovered that intelligently retrieving and injecting knowledge can provide significant quality improvements while remaining practical for deployment. Additionally, we gained hands-on experience with containerized deployments, distributed architectures, authentication systems, and production-grade AI infrastructure. What's next for BLACKOUT Our next goal is to make BLACKOUT even more autonomous and resilient. We plan to implement automatic knowledge base growth powered by user feedback, enabling the system to continuously improve its offline capabilities. We also intend to expand support for additional local models and introduce smarter routing decisions based on response quality and resource availability. Future versions will include enhanced synchronization mechanisms, stronger observability through Arize Phoenix, and a simplified onboarding experience for users setting up local AI models. Ultimately, our vision is to create an AI assistant that remains reliable regardless of connectivity conditions—ensuring that intelligence remains available even when everything else goes dark. <div