---
slug: "research-compass"
url: "https://devpost.com/software/research-compass"
title: "Research Compass"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 710
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# Research Compass

> Stop hunting, start researching: AI that finds opportunities and opens doors

[Devpost](https://devpost.com/software/research-compass) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]]
**domain** [[agriculture_food]] [[developer_tools]] [[education]] [[labor_employment]]
**user** [[educator_student]] [[researcher]]
**substrate** [[code_repository]] [[structured_db]]

**stack** alembic-(database-migrations), brightdatamcp, claude, composiotoolrouter, creao.ai, docker-(for-postgresql-with-pgvector), fastapi, javascript/react, openai-api-(embeddings-&-text-generation), openai-embeddings-(text-embedding-3-large-or-similar), pydantic, python, python-dotenv, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for research compass

## Body

Research Compass Inspiration The genesis of Research Compass emerged from a conversation with a senior researcher at OpenAI about breaking into academic research. This revealed a systemic challenge: despite abundant opportunities at leading institutions, critical information remains fragmented across hundreds of disparate university portals in inconsistent formats. 86% of students invest weeks manually aggregating contacts and crafting outreach communications. We recognized this as a tractable problem at the intersection of data engineering, AI, and UX design. Research Compass reimagines this workflow, transforming weeks of manual labor into an intelligent, automated system that democratizes research access. What It Does Research Compass is an end-to-end AI-powered platform that compresses the multi-week opportunity search into minutes: Intelligent Aggregation: Autonomous web scraping continuously harvests research programs and lab openings from top-tier universities globally Semantic Matching Engine: AI-powered vector similarity search matches students with opportunities based on deep contextual understanding of interests, skills, and academic background Automated Outreach Generation: LLM-powered email composition creates highly personalized, professional correspondence highlighting relevant qualifications Application Intelligence: Real-time analytics tracking email delivery, open rates, reply sentiment, and follow-up orchestration The result: Students connect with exponentially more relevant opportunities while maintaining authenticity at scale. How We Built It Backend Infrastructure FastAPI for our REST API backend PostgreSQL with pgvector extension for vector similarity search OpenAI embeddings for semantic matching between student profiles and opportunities Anthropic Claude for generating personalized emails Composio for Gmail integration and email tracking Python web scraping tools to aggregate opportunities from university websites Frontend React with TypeScript for type safety Creao.ai to accelerate UI development and component generation TailwindCSS for styling Vite for fast development and builds Challenges We Ran Into Heterogeneous Data Unification: Universities structure their research pages completely differently. Some use tables, others use narrative text, and formats vary wildly. We built flexible scrapers that can adapt to different layouts while maintaining data quality. Vector Search Setup: Getting pgvector working across different development environments was technically challenging. We had to carefully configure the database extension and optimize query performance. AI Email Quality: Getting AI-generated emails to sound genuine and personalized rather than generic was difficult. We experimented extensively with different prompts, examples, and parameters to achieve natural-sounding output that students would actually want to send. Frontend-Backend Integration: Connecting our React frontend with the FastAPI backend required careful API design and handling asynchronous operations properly to keep the UI responsive. Accomplishments That We're Proud Of Creao.ai Integration: We used Creao's AI-powered development tools to rapidly build our frontend interface, which let us iterate quickly on the user experience and focus more energy on the backend challenges like semantic search and email generation. Functional Semantic Search: We successfully implemented vector embeddings and similarity search that actually returns relevant matches. Students can describe their interests in natural language and get meaningful opportunity recommendations. End-to-End System: We built a complete working application from authentication through opportunity discovery to email sending and tracking. All the pieces work together to deliver a cohesive user experience. What We Learned Full-Stack Development: We gained hands-on experience building a complete application where frontend, backend, database, and external APIs all need to work together seamlessly. Working with AI APIs: We learned how to integrate multiple AI services (OpenAI, Anthropic, Composio) and handle their different requirements, rate limits, and response formats. Database Design: We learned about both traditional relational data and vector embeddings, understanding when to use each approach and how to combine them effectively. Rapid Prototyping: Using tools like Creao.ai showed us how AI-assisted development can speed up certain parts of the development process without sacrificing quality. What's Next for Research Compass Scale and Intelligence Expand to more universities and research institutions Add support for international opportunities Improve matching algorithms based on user feedback Parse uploaded resumes to automatically populate student profiles Community Features Enable direct messaging between students and researchers Create student communities around research areas Add success stories and application outcome tracking Enhanced Functionality Track full application lifecycle from initial contact to acceptance Smart notifications for new opportunities and follow-up reminders Advanced filtering by location, funding, remote options, and time commitment Save opportunities and manage multiple applications simultaneously Our ultimate vision: Eliminate systemic barriers in research access, ensuring every student, regardless of institutional prestige, location, or network, can engage in meaningful research. <div