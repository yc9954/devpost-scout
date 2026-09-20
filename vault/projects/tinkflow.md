---
slug: "tinkflow"
url: "https://devpost.com/software/tinkflow"
title: "TinkFlow"
hackathon: "LaunchHacks IV"
organization: "LaunchHacks"
winner: true
words: 529
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "user/educator_student"
  - "substrate/geospatial"
---

# TinkFlow

> TInkFlow - The Best AI Educational MindMap Builder

[Devpost](https://devpost.com/software/tinkflow) · hackathon [[LaunchHacks IV]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: developer_tools, education</sub>
**user** [[educator_student]]
  <sub>weak: developer</sub>
**substrate** [[geospatial]]
  <sub>weak: structured_db, video_visual</sub>

**stack** firebase, gemini-api, groq, react, react-flow

## Body

Inspiration I was heavily inspired by the developers of the open-source reactflow framework What it does TinkFlow is a revolutionary educational mind-mapping tool designed to supercharge learning and creativity. It empowers students, educators, and life-long learners to visually organize complex information, brainstorm new ideas, and connect concepts in an intuitive and dynamic workspace. At its core, TinkFlow integrates a powerful AI assistant that can expand on ideas, generate related topics, and help users overcome creative blocks, making it the ultimate tool for studying, lesson planning, and project management. How we built it TinkFlow is built on a modern, serverless architecture to ensure scalability and speed. The backend logic is powered by Firebase Cloud Functions , written in TypeScript , providing a robust and scalable API. For our core AI features, we integrated the Groq API , leveraging the speed and power of the Llama 3 model to provide real-time content generation and brainstorming assistance directly within the mind map. The frontend is a highly interactive single-page application (SPA) designed to provide a seamless and fluid user experience for creating and manipulating mind maps. Challenges we ran into One of the main challenges was ensuring extremely low latency for the AI-generated suggestions. The goal was for the AI to feel like a natural extension of the user's thought process, which required optimizing our calls to the Groq API and efficiently handling the data stream. We also invested significant effort in designing a user interface that could gracefully handle complex, deeply nested mind maps without sacrificing performance or usability. Finally, configuring secure and reliable communication between our frontend and the Firebase backend, especially handling CORS policies for a web application, required careful implementation. Accomplishments that we're proud of We are incredibly proud of creating a tool that genuinely enhances the learning process. The seamless integration of the Groq AI is a key accomplishment, setting TinkFlow apart from traditional mind-mapping software. We successfully built a fast, reliable, and scalable application using a modern serverless stack. The positive feedback on the intuitive design and the "magical" feel of the AI-powered suggestions has been a huge validation of our efforts. What we learned This project was a deep dive into the power of serverless architectures and the practical application of Large Language Models (LLMs). We learned how to architect and deploy scalable backend services using Firebase Functions. A major takeaway was the art of prompt engineering—crafting the right queries for the Groq API to get back structured, relevant, and creative content that fits perfectly into the context of a mind map. What's next for TinkFlow The journey for TinkFlow has just begun! Our roadmap includes: Real-time Collaboration: Allowing multiple users to work on the same mind map simultaneously. Advanced AI Features: Introducing AI-powered summarization, quiz generation from mind maps, and image generation for nodes. More Customization: Offering a wider range of themes, node shapes, and connection styles. Mobile Apps: Developing native iOS and Android applications for on-the-go mind mapping. Integration with other platforms: Connecting with tools like Google Drive, Notion, and other educational platforms. Built With AI: Groq API (Llama 3) Backend: Firebase Cloud Functions Language: TypeScript Framework: Node.js Database/Hosting: Firestore, Firebase Hosting <div