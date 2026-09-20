---
slug: "novaxflow"
url: "https://devpost.com/software/novaxflow"
title: "NOVAXFLOW"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 651
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# NOVAXFLOW

> NovaGPT is an AI assistant using Amazon Nova on AWS Bedrock. Users can chat, upload images or documents, and interact via text or voice to receive AI-powered answers and content analysis.

[Devpost](https://devpost.com/software/novaxflow) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**substrate** [[document_pdf]] [[video_visual]]
  <sub>weak: structured_db, web_dom</sub>

**stack** amazon-nova-2-lite, amazon-nova-api, amazon-web-services, amazon-web-services-(aws), aws-bedrock, aws-lambda-(serverless-functions)-deployment-&-dev-tools:-github, css, docker-other-technologies:-vector-embeddings, html, javascript, mongodb, multimodal-ai-processing, node.js-(express), nova-2-sonic

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for novaxflow

## Body

NovaXFlow is an AI assistant enabling chat, voice interaction, and document/image analysis using Amazon Nova on AWS Bedrock. Inspiration Daily life often involves managing many small but important tasks—meetings, reminders, documents, and schedules. People usually rely on multiple apps to keep everything organized, which can become confusing and inefficient. The idea behind NovaXFlow came from the need for a simple and intelligent assistant that can understand natural language and help users manage these responsibilities easily. Instead of manually setting reminders or searching through calendars, users should be able to talk to an AI and instantly receive help. The availability of Amazon Nova models on AWS Bedrock inspired us to explore how generative AI can act as a real personal assistant capable of understanding conversations, organizing information, and assisting with everyday productivity tasks. What it does NovaXFlow is a conversational AI assistant designed to help users manage schedules, reminders, and documents through natural language interaction. Users can chat with the assistant to check their daily schedule, create reminders, or organize tasks without navigating complex menus. The system can also process uploaded files and provide summaries or insights from documents. By connecting with calendar systems, NovaXFlow can add events, show upcoming schedules, and send notifications to ensure users never miss important tasks. The assistant is designed to make life administration easier by combining conversational AI with real productivity tools. How we built it The project was developed as a full-stack web application using modern JavaScript technologies. The frontend interface was created using React and Next.js, providing a clean chat-based environment where users interact with the AI assistant. The backend was built using Node.js and TypeScript, which handles API communication and connects the system with Amazon Bedrock. NovaXFlow uses Amazon Nova 2 Lite as the main reasoning model to understand user requests and generate responses. The assistant also supports document understanding through multimodal capabilities. A multi-agent structure was designed to separate responsibilities, such as scheduling tasks and organizing information. For real-world functionality, the application integrates with Apple Calendar via CalDAV, allowing reminders and events created through the assistant to appear directly in the user’s calendar. Challenges we ran into One major challenge was integrating AI reasoning with external services like calendar systems and document processing. Ensuring that the assistant correctly interprets user commands and converts them into structured actions required careful prompt design and validation logic. Another challenge involved managing secure authentication and API communication with cloud services such as AWS Bedrock. Additionally, maintaining smooth user interaction while handling asynchronous AI responses required thoughtful backend architecture and error handling. Accomplishments that we're proud of We successfully built a working AI assistant that combines conversational interaction with real-world task management. NovaXFlow demonstrates how generative AI can go beyond simple chat responses and perform meaningful actions such as scheduling events and organizing information. Integrating Amazon Nova with a modern web interface and real calendar synchronization was a significant milestone for our team. The project shows how AI-powered assistants can simplify everyday productivity. What we learned Through this project, we gained valuable experience working with Amazon Bedrock and Nova models, especially understanding how AI systems can interact with tools and APIs. We learned how to design prompts that guide AI reasoning, build multi-agent workflows, and integrate external services like calendars into AI-driven applications. The project also helped us improve our skills in full-stack development, cloud integration, and designing user-focused AI systems. What's next for NOVAXFLOW The next step for NovaXFlow is to expand its capabilities and make the assistant more powerful and accessible. Future improvements include adding voice interaction using Nova Sonic, enabling real-time spoken conversations with the assistant. We also plan to improve document understanding with advanced multimodal embeddings and build smarter scheduling features such as automatic task prioritization and proactive reminders. In the future, NovaXFlow could integrate with more productivity tools, allowing users to manage emails, tasks, and documents from a single intelligent assistant. <div