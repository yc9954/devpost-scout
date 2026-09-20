---
slug: "socratic-xu768i"
url: "https://devpost.com/software/socratic-xu768i"
title: "Socratic"
hackathon: "ConUHacks X"
organization: "HackConcordia"
winner: true
words: 399
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
---

# Socratic

> Copying code gets you through the assignment. Understanding code gets you the job. Socratic is a VS Code mentor that guides with questions so you actually learn while you build.

[Devpost](https://devpost.com/software/socratic-xu768i) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]]
  <sub>weak: voice_speech</sub>
**domain** [[education]]
**user** [[educator_student]]

**stack** elevenlabs, gemini, javascript, mongodb, rag, typescript, vs-code

## How they structured the write-up

- mlh challenges

## Body

Level up skills and get skills packages from Sponsors or Courses Marketplace of Mentors with personalities, voices ( ElevenLabs) and knowledge Smart Popups based on your skill level and your goals Chat to ask specific questions but while learning and not letting the ai do it for you. RAG capabilities to add context Mentors about topics you want to learn about Inspiration Traditional coding assistants give you answers directly, which can hinder true learning. Socratic was inspired by the Socratic method, teaching through questions and guided discovery, to help users build real problem-solving skills, not just copy solutions. What it does Socratic is a VS Code extension that acts as a coding mentor. Instead of giving direct answers, it guides users with adaptive help modes, AI-powered teachers, skill tracking, and encouragement features. Users can choose their preferred teaching style and level of help, track their progress, and receive motivational feedback. How we built it TypeScript for extension logic VS Code Webview API for the sidebar UI Google Gemini for AI-driven guidance ElevenLabs for text-to-speech encouragement MongoDB for cloud-synced user data and analytics. Local JSON for offline teacher customization Modular architecture with clear separation of services, UI, and data layers MLH Challenges See how we completed the MongoDB, ElevenLabs and Google Gemini challenge in our github video Challenges we ran into Balancing cloud (MongoDB) and offline (local JSON) data for flexibility and reliability Designing adaptive help modes that encourage learning without frustrating users Integrating real-time AI feedback and voice encouragement smoothly into the VS Code workflow Ensuring a seamless user experience across different teaching styles and modes Accomplishments that we're proud of Created a unique learning experience that prioritizes understanding over rote answers Built a flexible system for adding new AI teachers and help modes Implemented real-time skill tracking and visual feedback Integrated voice encouragement, including fun modes like “Sergeant Synthax” What we learned The importance of user-centric design in educational tools How to leverage AI and TTS APIs for interactive learning Best practices for hybrid cloud/local data management in VS Code extensions The value of modular, maintainable code for rapid iteration What's next for Socratic Expanding the teacher marketplace with more personalities and languages Adding support for more programming languages and skill categories Deeper analytics and personalized learning paths Community features for sharing progress and custom teachers Continuous improvement based on user feedback# Accomplishments that we're proud of <div