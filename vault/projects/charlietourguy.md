---
slug: "charlietourguy"
url: "https://devpost.com/software/charlietourguy"
title: "CharlieTourGuy"
hackathon: "The AI Champion Ship "
organization: "LiquidMetalAI"
winner: true
words: 610
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# CharlieTourGuy

> CharlieTourGuy is an immersive 3D travel companion that turns Google Maps into a real-time voice conversation with a context-aware local guide. If you need something, Charlie is there to help you!

[Devpost](https://devpost.com/software/charlietourguy) · hackathon [[The AI Champion Ship]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** elevenlabs, gemini, google-maps, javascript, liquidai, raindrop, vultr, vultrserverlessinference

## How they structured the write-up

- inspiration
- what it does

## Body

Active location tracking and Clear Conversation floating Bar Automated Discovery Route Suggestion Location Ex1 Location Ex2 Inspiration We wanted to create a travel companion that feels less like a database and more like a local friend. Traditional travel apps give you lists and ratings, but they lack the conversational warmth and immediate context of a real guide. Inspired by the desire to make exploring new cities more immersive and accessible, we built CharlieTourGuy —an AI persona that can walk you through the streets, tell you the history of a building you're looking at, and chat with you in real-time. What it does CharlieTourGuy is an interactive, voice-enabled tour guide web application. Interactive Map : Users can explore a 3D map of San Francisco. Real-time Voice Conversation : You can talk to Charlie (our AI guide) naturally. Ask "What's that building?" or "Tell me a fun fact about this place," and Charlie responds with a unique voice. Visuals : As you explore, the app updates with relevant images and street views of the locations discussed. Smart Recommendations : Charlie remembers your conversation context to provide personalized suggestions. ## How we built it We built CharlieTourGuy using a modern, AI-first stack: ### Backend (Raindrop Framework) We leveraged the LiquidMetal Raindrop framework to deploy our services. SmartBucket : Used for storing and retrieving rich tour data. SmartMemory : Implements semantic memory so the AI remembers the conversation context across turns. SmartSQL : Allows natural language querying of user preferences. Hono.js : For building our lightweight, fast API endpoints. ### Frontend Built with React for a responsive user interface. ### AI & Integrations ElevenLabs : Powered the lifelike voice of our guide, Charlie. Google Maps Platform : Provided the base maps, markers, and Street View imagery. Vultr Inference : Used for high-performance LLM inference to generate tour content. OpenAI : Assisted with conversational logic. ## Challenges we ran into Deployment Coordination : Coordinating the deployment of a separate backend (on Raindrop) and frontend (on Vercel) while managing environment variables and CORS policies was tricky. We had to ensure the frontend could securely and reliably talk to our live backend services. Voice Latency : Ensuring real-time voice responses felt natural required optimizing our API calls to ElevenLabs and managing the state of the audio player in React to avoid overlaps or delays. Context Management : Keeping the AI "aware" of where the user is looking on the map vs. what they are asking about required careful synchronization between the map state and the conversation history stored in SmartMemory. ## Accomplishments that we're proud of Full-Stack AI Integration : We didn't just wrap an API; we built a system where the map, voice, and text all work together. LiquidMetal Implementation : Successfully implementing the Raindrop framework with its "Smart" features (Memory, Bucket, SQL) to create a robust backend. Immersive UX : Creating a smooth interface where users can seamlessly switch between looking at a map and "walking" through Street View while listening to a guide. ## What we learned The Power of Semantic Memory : We learned how much more natural a conversation feels when the AI has "memory" of previous turns (via SmartMemory) rather than just being a stateless request-response loop. Cloud Deployment Nuances : We gained deep experience in configuring production environments, handling cross-origin requests, and managing API secrets securely across different platforms. ## What's next for CharlieTourGuy [ ] AR Integration : Bringing Charlie into the real world via mobile AR. [ ] User Accounts : Leveraging SmartSQL further to save customized tour itineraries for users. [ ] More Cities : Expanding the dataset in SmartBucket to cover cities beyond San Francisco. <div