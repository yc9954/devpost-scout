---
slug: "strangears"
url: "https://devpost.com/software/strangears"
title: "StrangEars"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 698
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/mental_health"
  - "domain/security_privacy"
  - "substrate/video_visual"
---

# StrangEars

> StrangEars: An anonymous platform connecting people who need to vent with empathetic listeners. Get things off your chest safely in one-on-one chats without judgment. Fresh perspectives, real support.

[Devpost](https://devpost.com/software/strangears) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[mental_health]] [[security_privacy]]
**substrate** [[video_visual]]

**stack** express.js, node.js, react, redis, render, socket.io, sql, tailwind, typescript, vercel, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what we learned
- what's next for strangears

## Body

Landing page Profile Role selection Waiting Room Chat Interface Mood board The Story of Strange Ears Inspiration The idea for StrangEars was born from countless late-night conversations on Discord servers and across the internet. I found myself naturally gravitating toward people who needed someone to listen—and in the process, I made genuine friendships through these vulnerable moments of connection. But I noticed something was missing: there wasn't a dedicated platform specifically designed for this kind of emotional support. Sometimes you need to talk through your problems with multiple people to gain different perspectives. Even after confiding in friends, thoughts can keep circling in your mind, creating an urgent need to process them with fresh ears. I realised that existing platforms were either built for general chatting or offered group-based venting—but there's something powerful about one-on-one conversations where someone can focus entirely on you. As someone who genuinely enjoys listening and helping others find solutions, I envisioned a platform where people could choose their role: those seeking support could find dedicated listeners, while those wanting to help could offer their time and empathy. What it does StrangEars creates a safe, anonymous space where people can connect for meaningful emotional support. Currently in its initial stage, the platform matches users who want to vent with volunteer listeners through our chat interface. We prioritise anonymity by encouraging usernames instead of real names, with gentle reminders throughout the registration process. Users can add profile pictures to personalise their experience, though we advise against using real photos. We're planning to implement age-based matching criteria to connect people with similar life experiences. For now, we've focused on text-based chat to maintain safety—video and voice features could potentially be abused and harm vulnerable users. Our safety measures include a report button that sends session IDs directly to our team, with plans to add detailed reporting categories in future updates. How we built it Our tech stack includes: Frontend: React 18 with TypeScript, Tailwind CSS for styling, Socket.IO client for real-time communication, and Vite for build tooling Backend: Node.js with Express, Socket.IO for WebSocket management, Redis for session storage, and SQLite for minimal persistent data storage My teammate, Sanyam, handled the backend development while I managed the frontend. We collaborated closely on design, UI, and UX decisions. Over three intensive weeks, we brought StrangEars from concept to working prototype. Accomplishments that we're proud of The moment our chat interface came alive was absolutely electrifying. Seeing real-time messages flow between users for the first time felt magical—weeks of planning and coding suddenly transformed into something tangible and meaningful. We're incredibly proud of how quickly we moved from idea to implementation. Watching our designs transform from mockups to a functioning platform was deeply satisfying. When we demonstrated StrangEars to our friends, their reactions exceeded our expectations. They were genuinely surprised and excited to see it working live, offering valuable feedback and encouragement. Their enthusiasm validated what we've been building. Most importantly, we're excited about the potential for StrangEars to foster a healthy, supportive community where people genuinely help each other through difficult moments. What we learned This project dramatically expanded our technical knowledge. We explored new concepts, including WebSockets, Redis Cache, Vite, and JSX—skills that will serve us well beyond this competition. We gained crucial insights about user safety and privacy in digital platforms. Building features like report buttons and easy exit options isn't just good practice—it's essential for protecting vulnerable users who need to feel safe while sharing personal struggles. What's next for StrangEars We are excited to make it public! The need for a platform like StrangEars feels genuine and urgent—if we receive encouraging feedback, we're open to taking this further. We're eager to incorporate user suggestions and implement the features we've envisioned, including age-based matching and comprehensive reporting systems. The possibility of mobile app development intrigues us, though it's not currently prioritised. Personally, I believe StrangEars addresses a critical gap in today's digital landscape. Mental health support and emotional connection are more important than ever, and I genuinely hope this project grows into something that makes a meaningful difference in people's lives. My fingers are crossed that we're building something the world truly needs. <div