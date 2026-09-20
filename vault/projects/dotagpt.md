---
slug: "dotagpt"
url: "https://devpost.com/software/dotagpt"
title: "DotaGPT"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 410
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "substrate/geospatial"
---

# DotaGPT

> AI learning assistant for Dota 2 built with Gemini 2.5 Flash

[Devpost](https://devpost.com/software/dotagpt) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]]
**substrate** [[geospatial]]

**stack** mongodb, nextjs, node.js, nosql, npm, restful, steamwebapi, tailwind, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dotagpt

## Body

Inspiration As avid Dota 2 players, we noticed how overwhelming the game can be for newcomers - with so much things to learn making it the hardest MOBA game as of now. We wanted to create an AI-powered learning companion that breaks down these concepts into digestible, beginner-friendly content. What it does DotaGPT is an AI-powered chatbot designed specifically for new Dota 2 players. Using Gemini 1.5 Flash, it provides real-time answers to beginner questions about the 5 core positions (Carry, Mid, Offlaner, Roaming Support, Hard Support), role responsibilities, item recommendations, and basic gameplay mechanics. The chatbot serves as a personalized learning companion that helps newcomers understand complex Dota 2 concepts through interactive conversations. How we built it Frontend : Next.js with TypeScript for fast development and great developer experience Styling : TailwindCSS for responsive, mobile-first design Backend : Node.js API routes with MongoDB for storing position guides and chat responses AI Chat : Integrated Gemini 1.5 Flash for real-time responses to beginner questions about Dota 2 positions and gameplay Deployment : Vercel for seamless CI/CD integration Challenges we ran into Content curation : Distilling complex Dota 2 mechanics into truly beginner-friendly explanations without oversimplifying AI prompt engineering : Fine-tuning Gemini 1.5 Flash prompts to provide accurate, beginner-focused Dota 2 advice within our domain Token limitations : Limited Gemini API tokens affected development pace, requiring careful testing and optimization of chat features Mobile optimization : Ensuring the chat interface works smoothly across devices, especially for gaming content API rate limiting : Managing Gemini API calls efficiently during development and testing Accomplishments that we're proud of Created comprehensive position guides that genuinely help beginners understand their roles Successfully integrated Gemini 1.5 Flash to provide intelligent, contextual responses about Dota 2 positions Achieved excellent mobile responsiveness for both guides and chat interface Delivered a polished, AI-powered educational tool within hackathon timeframe What we learned The importance of user-centered design when tackling complex gaming concepts How to balance technical complexity with user simplicity Effective content strategy for educational applications Modern web development best practices with Next.js and MongoDB integration What's next for DotaGPT Enhanced AI context : Train custom models or fine-tune prompts with more specific Dota 2 knowledge Hero recommendations : AI-powered hero suggestions based on position and beginner skill level Interactive tutorials : Hands-on learning modules with AI guidance Advanced conversations : Multi-turn chat sessions with memory for personalized learning paths Community features : AI-moderated beginner forums and Q&A sections <div