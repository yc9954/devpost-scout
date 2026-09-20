---
slug: "launchpie"
url: "https://devpost.com/software/launchpie"
title: "LaunchPie"
hackathon: "Zero to One Hackathon by Convex"
organization: "Convex"
winner: true
words: 508
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# LaunchPie

> Fair equity distribution made easy. LaunchPie uses realtime tech, AI and industry best practice to ensure startups grow together transparently and justly

[Devpost](https://devpost.com/software/launchpie) · hackathon [[Zero to One Hackathon by Convex]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
  <sub>weak: government_staff</sub>
**substrate** [[document_pdf]] [[structured_db]] [[transcript_audio]]

**stack** blocknote, clerk, convex, langchain, nextjs, nivo, openai, replicate, shadcn, whisper, zod

## How they structured the write-up

- inspiration
- what i learned
- how i built the project
- challenges faced
- feature list

## Body

Inspiration I started LaunchPie after seeing too many startup founders worry about unequal contributions from their partners. This worry often leads to disputes and can ruin relationships and the company's future. My goal was to build a tool that avoids these issues by making equity distribution clear, fair, and tied to what each person actually does. What I Learned Building LaunchPie taught me a lot. It's not just about fair calculations for equity distribution; it's about how these calculations create trust and clarity in a team. Using the Slicing Pie model as a base, I had to figure out how to apply its concepts in a software that updates in real-time. I saw how crucial managing data on the fly is and how AI can help make complex decisions automatically. The biggest takeaway? Clear communication and valuing every team member's input are essential for a startup's success. How I Built the Project Creating LaunchPie involved careful integration of technology and equity calculation principles: Tech Stack : I used Convex for its live database updates and queries, OpenAI for automation, Next.js and React for the frontend, with Tailwind CSS and Shadcn for design, and NivoCharts for visualizing data. Replicate and WhisperAI were crucial for converting speech to text. Blocknote was used to build the text editor. For the Convex integration in LaunchPie, I utilized a comprehensive range of features: This included the use of queries and mutations for real-time data updates, actions and internal functions for automating equity calculations, and scheduling functions. Additionally, I leveraged Convex's indexing, vector search and full-text search for efficient data retrieval, along with its built-in file storage for document management. Critical to maintaining the integrity and usability of the system were Convex's argument validation and error handling, which safeguarded against invalid data inputs and managed system errors gracefully. The opt-in Node.js runtime environment further enhanced the project by enabling server-side operations and integrations, ensuring LaunchPie operated smoothly and efficiently. Slicing Pie Integration : I adapted the Slicing Pie model for our digital platform to ensure equity shares truly reflect each person's input. Challenges Faced The main hurdles were: Data Visualization : Making the complex data of equity distribution understandable required clever use of NivoCharts for real-time, easy-to-understand visuals. Function Call Optimization : I had to make sure our backend, especially parts handling live data and equity math, was fast and reliable. This meant getting the most out of Convex, fine-tuning our system for the best performance and user experience. Feature List Real-Time Equity Dashboard : Shows up-to-date equity stakes and contributions. Contribution Tracking : Users log contributions, which then adjust equity shares automatically. Document Management : Simplifies document upload and provides instant summaries. Meeting Management : Supports recording meetings with auto-generated transcriptions and agendas. AI-Enhanced Text Editor: Aids content creation with dynamic, AI-generated assistance. Interactive Chatbot : Offers quick access to company info, tasks, and documents. Efficient Data Handling : Employs Convex for data storage, retrieval, and live updates. Equity Distribution Calculations : Applies the Slicing Pie model for fair, real-time equity adjustments. <div