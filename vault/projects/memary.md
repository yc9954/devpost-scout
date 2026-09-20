---
slug: "memary"
url: "https://devpost.com/software/memary"
title: "MemARy"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 571
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/elder_child_care"
  - "domain/housing_homeless"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# MemARy

> MemARy: AR Glasses for Alzheimer's. See, hear, remember.

[Devpost](https://devpost.com/software/memary) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[vision_ocr]] [[voice_speech]]
**domain** [[elder_child_care]] [[housing_homeless]]
**substrate** [[structured_db]] [[video_visual]]
  <sub>weak: financial_record</sub>

**stack** chatgpt, chromadb, fastapi, gemini, lensstudio, livekit, llama, pokemcp, postman, python, react, reka, snapar, spectacle

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for memary

## Body

MemARy MemARy in Action Problem Statement Team Tech Stack User Experience Future Plans Inspiration Over 7 million Americans over 65 live with Alzheimer’s today, a number set to double by 2060. 1 in 9 older adults already face fading memories, and by 85, that risk climbs past 1 in 3. But memory loss isn’t inevitable, it’s a gap in design. We’re building MemARy, an AI wearable that sees what you see, hears what you say, and remembers what matters. Since most old people already wear glasses, why not wear it like Tony Stark. And for every Tony Stark who never forgets, MemARy will be the Jarvis for billions. What it does Memary is an AI-powered wearable interface that transforms visual and auditory inputs into structured, retrievable memory. Every few seconds or for every trigger (button press or saying the word, the device captures a frame from the user’s perspective, processes it through Reka's vision language model to extract semantic information: objects, spatial relations, colors, and contextual cues, and encodes that data into vector embeddings stored in a ChromaDB-based memory system. Users can interact with Memary through natural language, either by voice or text, to recall or store information, such as where they left important items. The system retrieves semantically relevant entries using vector similarity search, merges them with timestamped metadata, and returns precise and context-aware responses. Memary’s pipeline combines computer vision, LLM-based scene summarization, semantic embedding, and memory indexing, creating a continuous cognitive layer that enables human-like recall through AI. How we built it We engineered Memary as a modular, microservice-based system combining real-time perception, semantic understanding, and long-term memory storage. Using SnapAR and Lens Studio, we integrated our AI pipeline directly with Snap Spectacles, enabling the glasses to capture image frames, visualize UI for memory recall, and stream them to our backend. Each frame is processed by Reka’s Llama Vision Model, which generates a structured natural language summary that identifies objects, positions, specific characteristics, and contextual cues. The summaries are then embedded and stored in ChromaDB, our vector database layer, which enables high-speed semantic retrieval using cosine similarity. A FastAPI service mediates all data ingestion and querying, ensuring clean abstraction and multi-tenant control. On the client side, a React frontend provides the user interface for memory review and session selection along with memory dashboards, while PokMmCP powers semantic queries and synchronization between the phone and glasses. We also integrated LiveKit for low-latency speech-to-text processing, allowing users to add or recall memories through natural voice interaction. Together, this stack forms a continuous AI memory loop that enables real-time recall, just like having a grandmaster-level memory.. Challenges we ran into Complex idea in a short timespan, the documentation of SnapAR being quite the challenge but rewarding at the end, rigorous execution websocket approach to video and audio input into the Spectacle device Accomplishments that we're proud of Our idea, being broken down into smaller work functions, that when combined together as a group of microservices, produces an efficient and synergized product. What we learned Twinkling with a whole new development and product architecture in Snap Spectacles, the use of fabulous technologies by the sponsors that leveled up our production quality, and most importantly, thoughtful discussions makes complex missions possible. What's next for memARy Make it adaptable in any contextual use and eventually go beyond the market of old people with Alzheimer to everyone that does not want to forget anything, ever. <div