---
slug: "chatlas"
url: "https://devpost.com/software/chatlas"
title: "Chatlas"
hackathon: "Azure AI Developer Hackathon"
organization: "Microsoft"
winner: true
words: 480
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "substrate/structured_db"
---

# Chatlas

> Chatlas is inspired by the growing need for seamless communication in a globalized world where language differences often create barriers.

[Devpost](https://devpost.com/software/chatlas) · hackathon [[Azure AI Developer Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]]
**substrate** [[structured_db]]

**stack** azure, express.js, node.js, react, websocket

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chatlas

## Body

Homepage Contact Us Sign In Chat Tab Default Specific Chat Room & Shareable Invite Link Texts Translated to Preferred Language Joining Room: Waiting for Approval Admin View: Approve or Deny Join Request Inspiration Chatlas is inspired by the growing need for seamless communication in a globalized world where language differences often create barriers. We wanted to build a tool that connects people across languages - whether for casual chats, international collaboration, or community engagement - making it feel like everyone is speaking the same language. What it does Chatlas is a real-time group chat web application that automatically translates messages into the preferred language of each participant. Users can create or join chat rooms via unique invitation links and communicate freely, regardless of the language they use. Key features include: Auto-Translation: Messages are translated in real time using Azure AI Translator to match the recipient's language preference. Speech-to-Text: Users can convert their voice to text using Azure Speech Service. Secure Authentication: Sign-in and sign-up with Google OAuth, using JWT for session handling. Invite System: Every chat room generates a unique link that users can share to invite others. Persistent History: Rooms are persistent - users can leave and return later with full message history preserved. Lazy Load Messages: Older messages are loaded on scroll, improving performance and user experience, especially in large conversations. How we built it We developed Chatlas using a full-stack approach: Frontend: React (Vite) and Tailwind CSS for UI/UX. Backend: Node.js and Express.js handle the API and real-time socket connections. Database: Azure Cosmos DB for PostgreSQL stores user, room, and message data. Authentication: Google OAuth2 with JWT-based sessions ensures security. AI Services: Azure Translator for real-time multilingual support, Azure Speech Service for converting speech to text. We used GitHub Copilot throughout development to boost our productivity and streamline code generation. Challenges we ran into The app uses a Client-Server architecture, with WebSocket (Socket.IO) handling real-time communication. Each message is first stored in its original language, then translated and delivered to users in their chosen language. The system supports language preference changes mid-conversation, affecting only future messages. Accomplishments that we're proud of Successfully built a full-stack chat app with auto translation. Integrated Azure AI services for both text translation and speech-to-text. Achieved seamless sign-in/sign-up flow with Google OAuth and secure sessions. Built a robust invitation system with dynamic room links and user management. What we learned How to work with Azure Cognitive Services (Translation & Speech APIs). Setting up OAuth with secure session handling using JWT. Collaborative full-stack development using GitHub and Copilot. Handling WebSocket communication for real-time updates. What's next for Chatlas Add support for chat summarization using Azure OpenAI. Implement file sharing in rooms. (or emotes sending) Improve testing coverage and CI/CD pipeline. Add analytics to understand language usage and user behavior. Explore additional security enhancements and performance optimizations. Deployment on Azure with Docker containers. <div