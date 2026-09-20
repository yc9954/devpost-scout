---
slug: "memory-palace-qyat7g"
url: "https://devpost.com/software/memory-palace-qyat7g"
title: "Memory Palace"
hackathon: "OpenAI Open Model Hackathon"
organization: "OpenAI"
winner: true
words: 1066
team_size: 0
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/video_visual"
---

# Memory Palace

> An offline-first AI companion that helps those with memory loss reconnect with their memories and their families.

[Devpost](https://devpost.com/software/memory-palace-qyat7g) · hackathon [[OpenAI Open Model Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[health_clinical]]
  <sub>weak: elder_child_care</sub>
**user** [[patient_family]]
**substrate** [[video_visual]]
  <sub>weak: structured_db, transcript_audio</sub>

**stack** apple-vision-framework, axios, better-sqlite3, blip, coqui-tts, express.js, face-recognition, fastapi, git, github, gpt-oss-20b, ios, javascript, node.js

## Body

Welcome Screen Family Hub Chat Interface Voice Chat Image Chat Chat History Proactive Memory Cinematic iOS App Photo Memory Memory Detail Face Tags - Preview Video Memory Audio Memory Note Memory Photo Memory Detail People Settings 1 Settings 2 Inspiration The inspiration for Memory Palace is deeply personal. It comes from watching a loved one navigate the quiet, frustrating journey of memory loss. Seeing the moments of confusion where a familiar face in a photograph becomes uncertain, and the sadness that follows, is heartbreaking. We realized that while we have decades of photos, videos, and stories saved on our phones, there is no gentle, private, or intelligent way to share them with those who need them most. We wanted to build more than just a photo album; we wanted to build a compassionate AI companion that could bridge the gap between a fading memory and the love of a support network, using technology that respects a family's absolute right to privacy. What it does Memory Palace is a complete, private, and offline-first AI ecosystem that acts as a compassionate companion for individuals experiencing memory loss. It transforms a lifetime of scattered digital memories into interactive, narrative experiences. The system has two parts: For Family & Caregivers: A simple iOS app allows the user's support network to collaboratively build a rich, multimodal library of photos, videos, voice notes, and text stories. This happens on their private home network, with no cloud uploads. For the Patient: A gentle, accessible React web interface becomes their personal "Palace." Here, they can converse with an AI companion, powered by gpt-oss , that not only answers questions but proactively surfaces relevant memories. Its key feature is the "Cinematic Memory Journey," where the AI acts as a storyteller, weaving multiple memories into a single, cohesive narrative with synchronized narration, helping to rebuild the context and emotion of moments that might have been forgotten. How we built it Memory Palace is a full-stack application built with a privacy-first philosophy, designed to run entirely on a local home network. The AI Core (The "AI Director"): The heart of the system is the gpt-oss-20b model, which runs locally via Ollama . We don't use it as a simple chatbot; we've architected it as an "AI Director." It receives structured data about memories and user context, and its primary job is to reason, orchestrate, and generate the final narrative experience, deciding between simple text responses and complex "Cinematic Shows." The Specialist "AI Crew": To support the director, we built a pipeline of specialized models: Whisper for accurate audio transcription. BLIP for visual captioning of photos. Sentence-Transformers for creating vector embeddings for semantic search. Coqui TTS for generating a warm, natural voice for the AI companion. The Backend Hub (Node.js & FastAPI): We used a hybrid approach for maximum reliability. A Node.js server handles the family-facing API, file management, and a real-time WebSocket server for proactive notifications. It communicates with a FastAPI service that manages the AI pipeline and model inference. The Applications (iOS & React): The family-facing app is a native Swift/SwiftUI app that leverages Apple's on-device Vision Framework for private face detection. The patient's interface is a clean, accessible React web application designed for large screens and simple, intuitive interaction. Challenges we ran into The "AI Orchestra" over the "AI Monolith": Our initial ambition was to use a single, powerful multimodal model for everything. However, we quickly realized that running a model of that scale locally with our desired performance was unfeasible. This led us to our strongest architectural decision: the "AI Orchestra." By positioning gpt-oss as the conductor and using smaller, specialized models as the crew, we created a system that was more performant, more modular, and ultimately more effective than a single-model approach. The Home Network Hurdle: Building a system that reliably works across different home network configurations is notoriously difficult. We found that our Python-based AI service struggled with network discovery and firewall issues. Our solution was the hybrid backend, using Node.js for its robust and mature networking libraries to act as the stable, public-facing gateway for the entire ecosystem. Accomplishments that we're proud of A Truly Private, Local AI Agent: From memory submission to AI inference, not a single byte of personal data ever leaves the user's home network. This fulfills the promise of a truly private AI, making it a perfect example of a Best Local Agent . More Than a Chatbot - An AI Storyteller: We successfully moved beyond a simple Q&A paradigm. By using gpt-oss for high-level reasoning and orchestration, we've created a system that proactively tells stories and creates entirely new, narrative experiences, showcasing a novel application of the model. A Complete, Deployable Ecosystem: In a short timeframe, we built four distinct, interconnected applications (iOS, React, Node, Python) that work together seamlessly. This isn't a script or a prototype; it's a production-ready system that demonstrates a balanced and thoughtful design. Technology with a Heart: We are most proud that this project directly addresses a profound human need. It is a clear candidate for the For Humanity category, designed from the ground up to bring comfort, joy, and connection to those on a difficult journey. What we learned The "AI Orchestra" is a Powerful Pattern: We learned that the true power of a large reasoning model like gpt-oss can be unlocked when it's allowed to focus on what it does best—reasoning and language—while directing a crew of specialized tools. The Local-First Mindset Changes Everything: Designing for an offline-first environment forces you to make smarter, more resilient architectural choices from day one. Privacy isn't a feature; it's the foundation. Design for Compassion: Building for users with cognitive challenges taught us the importance of simplicity, gentleness, and proactivity in UX design. The best interface is often the one that anticipates your needs before you have to act. What's next for Memory Palace The vision for Memory Palace is just beginning. Our future roadmap includes: Cross-Platform Expansion: Building an Android and a web-based uploader to ensure the entire support network can contribute memories. Compassionate Fine-Tuning: Creating a safe, anonymized dataset of ideal interactions to fine-tune gpt-oss , making it an even more empathetic and effective companion, a strong candidate for the Most Useful Fine-Tune category. Smart Home Integration: Exploring ways to proactively surface memories on smart home displays and speakers, making the Memory Palace an ambient part of the user's environment. <div