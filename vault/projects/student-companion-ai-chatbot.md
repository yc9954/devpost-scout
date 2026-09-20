---
slug: "student-companion-ai-chatbot"
url: "https://devpost.com/software/student-companion-ai-chatbot"
title: "Student Companion AI Platform"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 836
team_size: 3
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Student Companion AI Platform

> Student Companion AI Platform - is an ai-driven student support platform that streamline easy access to academic resources, information and opportunities 24/7 around the clock.

[Devpost](https://devpost.com/software/student-companion-ai-chatbot) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[education]]
**user** [[developer]] [[educator_student]] [[researcher]]
**substrate** [[structured_db]] [[video_visual]]

**stack** amazon-dynamodb, amazon-web-services, amazone-opensearch, anthropic, bun, claude, claude-api, docker, github, google-sheets, google-sheets-api, hugging-face, python, react

## How they structured the write-up

- inspiration
- what it does
- how we use claude
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for student companion ai chatbot

## Body

Student Companion AI Logo with name Logo without name Inspiration At African Leadership University (ALU), students from across the continent learn through a self-directed model. Although ALU has a robust support system, that support is scattered across different platforms that students navigate from day one. The questions students need answered most often aren't about course content; they're about the learning system itself. Where to find what? How to find it? Who can we reach out to? How do we reach out? These answers exist, but they're scattered across emails, forms, Zendesk, tech support, student life platforms, and more. Some students lose hours hunting for them. Worse, students living far from campus don't always have someone to talk through a stuck assignment with, or to think out loud at 2am before a deadline. What it does ALU Student Companion is a Claude-powered, AI-driven companion platform built specifically for ALU undergraduates. It supports three dimensions of the university journey: Academics — coursework explanations, assignment breakdowns, writing feedback, study planning Campus life — navigating ALU's systems, policies, and processes Personal growth — reflection, self-direction, and the everyday questions of being a young adult away from home It runs at alustudentcompanion.vercel.app — no app download, designed for the cheap data and intermittent connections common across the continent. How we use Claude Claude is not a chatbot wrapper here — it is the reasoning core of a retrieval-augmented system grounded in ALU's actual context. When a student sends a message: The query hits our Hugging Face Space backend , which orchestrates the response. The backend performs vector retrieval over a ChromaDB index that is continuously synced from a curated Google Sheet. The most relevant rows are stitched into a carefully engineered system prompt and sent to the Anthropic Claude API . Claude reasons over the retrieved context and responds in a tone that fits a peer-companion, not a corporate chatbot. The Google Sheet is the canonical knowledge store — easy for non-engineers to maintain, easy to expand, and free. This is what turns Student Companion from a generic AI into something that actually knows ALU . How we built it Frontend: React + TypeScript, Vite, Tailwind CSS, shadcn/ui — deployed on Vercel Backend: Dockerised service on a Hugging Face Space , orchestrating retrieval and Claude API calls Knowledge base: Google Sheets as the ALU knowledge store, queried at runtime AI: Anthropic Claude API Workflow: Bun, ESLint, GitHub for version control and CI One of the more meta moments of the build: we used Claude itself to design the prompt framework that connects our Google Sheet data to the chatbot — a one-page prompt scaffold we ended up calling "The Killer Bean Prompt." Building with Claude and building with Claude's help made the whole sprint possible. Challenges we ran into The biggest infrastructure decision was how to ground the chatbot in ALU's knowledge. We initially wanted to explore a full AWS stack — managed vector store, embeddings pipeline — but with limited resources, we quickly realised it would consume the entire hackathon window before we shipped a single working response. The pivot was to ask Claude itself to help us design a leaner architecture, which we named "The Killer Bean Prompt." The output was a one-page prompt-and-retrieval framework that let us use a Google Sheet as the knowledge store and a thin retrieval layer to feed it into Claude. We went from "months of infra work" to "shipping in a day." That decision — choosing the simplest thing that could work — is the single most important call we made. Accomplishments that we're proud of Shipped a working, publicly accessible MVP within the hackathon window Built by ALU students for ALU students — the user research is our lived experience An architecture that any team member, technical or not, can maintain (anyone who can edit a spreadsheet can improve the bot) Anchored to a real institution rather than chasing false generality Production-grade frontend, typed end-to-end, on free-tier infrastructure What we learned Continuous learning and persistence get results. We hit dead ends — the AWS detour, prompt iterations that didn't land, retrieval mismatches. Each one looked like a wall and turned out to be a redirect. The pattern that worked: ship the smallest version, learn from how it behaves, iterate. We also learned that the right prompt is worth more than the right infrastructure — at this stage. A well-engineered system prompt and a curated knowledge sheet can outperform a half-built vector database every time. What's next for Student Companion AI Chatbot Launch an open beta to a wider ALU cohort with structured feedback collection Expand the Google Sheet knowledge base to cover the full ALU handbook, course catalogue, and learning model documentation Multimodal support — voice and image — for students primarily on phones Move retrieval from keyword matching to embeddings as the knowledge base grows Expansion beyond ALU to other African universities via the broader Student Companion AI platform Integration with SCA Opportunities to bridge academic support and post-graduation pathways <div