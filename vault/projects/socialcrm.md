---
slug: "socialcrm"
url: "https://devpost.com/software/socialcrm"
title: "socialCRM"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 586
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# socialCRM

> Turning creators into data-driven businesses through the power of AI.

[Devpost](https://devpost.com/software/socialcrm) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: graph_reasoning</sub>
**domain** [[accessibility]] [[developer_tools]]
**substrate** [[geospatial]] [[structured_db]]

**stack** javascript, node.js, openai, prisma, puppetlabs, react, shadcn, tailwind

## How they structured the write-up

- inspiration
- how it works and key features
- how we built it
- challenges we ran into
- what we learned
- what's next for creator intelligence?

## Body

Feature overview Instagram messy data ingestion Agentic command execution, including scraping and entity resolution with LinkedIn profiles AI marketing content suggestions Agentic Instagram profile research Manual audience management and database explorer Campaign analytics dashboard Campaign management Campaign analytics dashboard continued Inspiration Every day, millions of creators pour their hearts into building content and growing their presence, whether for personal expression or business. But when it comes to understanding their audience, they’re flying blind. While SaaS companies rely on CRMs and data dashboards, creators are stuck with surface-level platform insights. They can see follower counts go up or down—but not who , why , or what it means . Therefore, we asked: what if creators had a personal CRM , powered by AI, that helps them track engagement, flag churn risks, and identify revenue opportunities? That’s the goal of our project: to build an Agentic Creator Intelligence Platform that gives creators full control over their audience data and leverages autonomous agents to generate strategic insights and recommendations. How it works and Key Features Creator Intelligence is a platform that brings Agentic CRM vision to the content creation world. It is a web app that ingests user profile data and activates AI Agents to: Track audience engagement and churn Attribute follower changes to specific campaigns Parse public profiles into intelligent segments Recommend campaign strategies Help creators gain clarity from messy structured and unstructured data How we built it We have a Next.js + TypeScript frontend to power dashboards, analytics views, and interactive components styled with Tailwind CSS and the Shad CN library. We prototyped our designs in Figma initially. Our backend uses Next.js API routes to handle business logic, with Prisma as the ORM connecting to a lightweight SQLite database that stores profiles, campaigns, tags, and interaction events. Data ingestion happens through Node.js scripts and bulk upload endpoints, while AI features are supported by a mock classifier service (Python) and custom AI endpoints that generate campaign insights via Martian API keys. We also integrated Puppeteer for scripted profile ingestion and enrichment. To keep our workflow smooth, we used pnpm for package management, ESLint for linting, and Prisma Studio for database inspection. Challenges we ran into Parsing inconsistent Instagram exports: The raw data files had nested, irregular structures and missing fields, making it difficult to reliably extract and normalize user and event data for our database. Coordinating a multi-language stack: Integrating the TypeScript/Next.js frontend, Node.js/Prisma backend, and Python AI service required careful API design and debugging to keep data and state in sync. Concurrency and scaling issues: Processing thousands of profiles in parallel exposed race conditions and performance bottlenecks, so we had to optimize our queries and refactor our data flow for stability. What we learned Data normalization is critical: Building robust import pipelines for real-world social data requires handling edge cases, missing fields, and evolving formats up front. Clear API contracts save time: Defining strict interfaces between frontend, backend, and AI services early on helps prevent bugs and makes debugging much easier. Scalability needs planning: Even for prototypes, designing for concurrency and efficient data flow is important when working with large datasets or real-time processing. What's next for Creator Intelligence? In the future, we hope to expand beyond Instagram, integrating with other platforms to provide a unified, privacy-respecting CRM for creators everywhere. We envision Creator Intelligence as a core tool in the creator stack and strive to empower individuals to run their brand with the same data-driven precision, automation, and strategic insight as the world’s top businesses. <div