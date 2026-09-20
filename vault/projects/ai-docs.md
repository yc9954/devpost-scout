---
slug: "ai-docs"
url: "https://devpost.com/software/ai-docs"
title: "AI Docs"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 458
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# AI Docs

> Making Google Docs (file storage, text editor) better with AI

[Devpost](https://devpost.com/software/ai-docs) · hackathon [[Cal Hacks 12.0]]

## Facets

**substrate** [[document_pdf]] [[structured_db]]

**stack** react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ai docs

## Body

Inspiration As people who use Google Docs for almost everything from writing college essays to class notes to spontaneous poetry, we’ve found it restrictive in its ability to enhance a user’s experience. We've decided to reimagine popular word processors and integrate them with AI beyond just grammar checks and sentence suggestions. What it does AI Docs is an all-in-one file system that allows you to organize your files and edit them. Its high-level features include an AI-powered search bar for easy access to files and a background AI agent that reads your files to generate workflows and to-do actions for you immediately. For the actual word processor, we're reimagining what it means to write and create. Instead of having a single document and a sidebar for static comments, we extended it to a single document for writing the raw notes, and a dynamic sidebar that allows you to organize your comments/content and prompt AI (and see its responses), having all your notes in one place. This reimagines word processors and sees how AI can truly supplement all forms of writing and creation. How we built it On the frontend, we used React 18, React Router for navigation, React Quill for rich text editing, Axios for API calls, and Vite for build tooling. On the backend, we used Express.js, OpenAI API for intelligent search and document analysis, CORS enabled, and databases. Challenges we ran into Some challenges we ran into were finding cohesion in our vision. Our general topic is broad: word processor, and we had to work together to narrow it down into what we wanted our product to do and how we wanted to utilize AI in the background to have it be effective but also efficient. Accomplishments that we're proud of We're proud of having a working MVP (haha!) but also when our team came together with a vision, it was scattered, and we all had a lot of inputs/ideas that we wanted to implement. We're just super proud that we were able to implement the core features we were looking for and supplement it with a lot of details that enhance the user experience. We are also proud of how this solution solves the problem we've been facing with existing word processors! What we learned We learned a lot: coding in a fast paced environment with a narrow deadline, collaboration, and coming up with an idea and building it end to end with no other guidance than our minds and a collective vision that we share. What's next for AI Docs Next for AI Docs is to include more workflows that integrate across different writing formats such as creative writing and essay writing to allow it to cater to anyone who uses the platform. <div