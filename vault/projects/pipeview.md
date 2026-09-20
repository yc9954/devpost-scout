---
slug: "pipeview"
url: "https://devpost.com/software/pipeview"
title: "Notable"
hackathon: "HackUTD 2024: Ripple Effect"
organization: "hackutd"
winner: true
words: 746
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "user/developer"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Notable

> Capture Ideas, Create Clarity, Powered by AI.

[Devpost](https://devpost.com/software/pipeview) · hackathon [[HackUTD 2024- Ripple Effect]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]] [[education]] [[labor_employment]]
**user** [[developer]] [[educator_student]]
**substrate** [[document_pdf]] [[structured_db]] [[transcript_audio]]

**stack** databricks, fastapi, llama, python, react, sambanova, supabase, tailwind, terraform

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for notable

## Body

Inspiration As students and developers, we've experienced firsthand the challenges of taking effective notes during lectures and technical discussions. Traditional note-taking apps lack the intelligence to help organize and enhance content in real-time. We envisioned Notable as a bridge between conventional note-taking and AI-powered assistance, inspired by the potential of large language models to understand and enhance educational content. What it does Notable is an intelligent note-taking application that transforms how users capture and interact with information. It features real-time lecture transcription, AI-powered content enhancement, and automatic diagram generation from text descriptions. Users can edit their notes using natural language commands, share notes with unique links, export them to PDF format, and even generate diagrams. The app also includes a context-aware voice AI assistant that can answer questions about the notes and suggest improvements to the content. How we built it We developed Notable using a modern tech stack that prioritizes performance and user experience. The frontend is built with React and TypeScript, utilizing Vite for fast development and building. We implemented a clean, responsive UI using TailwindCSS and custom components. The backend is powered by FastAPI and crucially integrates with SambaNova's API, whose exceptional inference speed was vital for our real-time transcription feature. Since we have such large context windows due to the additional information that we pass in traditional LLMs did struggle with our latency requirements for our real-time application, but SambaNova's architecture allowed us to process and enhance lecture content with negligible delay, making the experience truly seamless for users. It is crucial that we add value to the user besides basic LLM functions. Towards these goals we utilized crewAi to add context from websites and other contexts to add more information through Agentic AI. We presist these contexts and notes for the user with ChromaDB and sqlite to connect the users notes to give an better and bigger picture of the topics at hand. We used Supabase for authentication and database management, and deployed our infrastructure using Terraform on AWS, leveraging services like S3 for static hosting and SageMaker for AI model deployment. Challenges we ran into Our initial challenge was finding an AI solution capable of handling real-time transcription with the speed and accuracy our application demanded. SambaNova's fast inference capabilities were game-changing here - where other solutions introduced noticeable delays that broke the user experience, SambaNova's API allowed us to process speech-to-text-to-edit and enhance content in near real-time. This was crucial for students taking notes during live lectures, where even small delays could mean missing important information. We still had to carefully optimize our state management and API calls to maintain this performance. Another significant challenge was integrating the AI diagram generation feature, which required careful prompt engineering to generate accurate Mermaid diagrams from natural language descriptions. We also faced interesting technical hurdles in implementing the floating toolbar for text selection and ensuring consistent behavior across different browsers. Accomplishments that we're proud of We successfully created a seamless integration between note-taking and AI assistance, making it feel natural and intuitive. The real-time transcription feature works smoothly, and the diagram generation capability produces surprisingly accurate visualizations. We're particularly proud of our clean, responsive UI design and the implementation of the share functionality that generates unique links for notes. The application's architecture is scalable and maintainable, with clear separation of concerns and type safety throughout. What we learned This project taught us valuable lessons about integrating AI services into web applications and the importance of user experience in productivity tools. We gained deep insights into working with the SambaNova API and learned how to effectively prompt large language models for specific tasks. The project also improved our understanding of React's performance optimization techniques and the benefits of using TypeScript for large-scale applications. Infrastructure-wise, we learned a lot about using Terraform for AWS resource management and the importance of proper CI/CD pipelines. What's next for Notable We have exciting plans for Notable's future. We want to implement collaborative editing features, allowing multiple users to work on notes simultaneously. We're also planning to add more AI-powered features like automatic summarization, topic extraction, and study guide generation. On the technical side, we aim to implement offline support using service workers and add real-time collaboration using WebSocket connections. We're also exploring the possibility of creating mobile applications to make Notable accessible on all devices. Finally, we plan to enhance our AI models' understanding of technical content and improve the accuracy of our diagram generation feature. <div