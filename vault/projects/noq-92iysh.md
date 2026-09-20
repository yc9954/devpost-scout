---
slug: "noq-92iysh"
url: "https://devpost.com/software/noq-92iysh"
title: "Noq"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 302
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "substrate/web_dom"
---

# Noq

> AI-Powered Real-Time Note Taker

[Devpost](https://devpost.com/software/noq-92iysh) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
  <sub>weak: voice_speech</sub>
**domain** [[education]]
**substrate** [[web_dom]]

**stack** chromadb, groq, next.js, tailwind, whisper

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for noq

## Body

Inspiration Our team has consistently tried to improve our personal school experiences slowly but surely by optimizing every small process we can. This tool takes it to the next level and completely streamlines the learning process up to the point where you can start studying! What it does Noq listens into your lecture, compiling and categorizing all of the lecture’s most important points for you. They are automatically expanded and revised, separating all the different ideas to be ready for vectorization. Once entered into the vectorstore, the RAG search engine allows for context-driven searching through your notes to easily find what you need. You can also generate diagrams for specific lines within a note, easily visualizing what has been summarized for the user. How we built it Using Groq as the main infrastructure behind our application, we leveraged its highly fast speeds to run multiple inference calls in our backend AI agent network almost instantly. ChromaDB also served as the vectorstore to store the notes and run our semantic search engine for easy querying. Our actual website was also built in Next.js and Tailwind. Challenges we ran into It was hard creating a complex real-time app without streaming with minimal delay and having AI agents acting in the background Accomplishments that we're proud of Being able to integrate external tools and technologies such as embedding models with Groq, as well as maintaining multiple servers interacting with each other to create a seamless and extremely fast interaction What we learned Frontend is hard What's next for Noq Completely integrate it with personal calendars and email, using tool calling for extracting upcoming events and deadlines and automatically creating reminders for those. This is a product we could easily see becoming a staple in our daily lives, and will definitely continue improving upon it! <div