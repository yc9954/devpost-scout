---
slug: "outstories"
url: "https://devpost.com/software/outstories"
title: "OUTStories"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 772
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# OUTStories

> Snap a photo, set the style, and let AI spin it into a fully-illustrated, professionally narrated book for your child

[Devpost](https://devpost.com/software/outstories) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]] [[retail_commerce]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]]

**stack** 21st.dev, bolt.new, elevenlabs, netlify, next.js, openai, supabase, tailwind

## How they structured the write-up

- 🌟 inspiration
- ⚡ what it does
- 🏗️ how we built it
- 🧠 architecture & project structure
- 🧗 challenges
- 🏆 what we’re proud of
- 📚 what we learned
- 🚀 what’s next

## Body

OnceUponATime (OUTStories) – Hackathon Build Recap 🚀 🌟 Inspiration My daughter recently entered the phase where every “Why?” becomes a deep, curious dive and generic search results just don’t cut it. So I asked myself: What if I could turn her specific question into a personalized story (featuring her favorite toy) that she’d actually want to revisit again and again? That became the idea behind OnceUponATime (OUTStories) a tool that enables any parent to transform a photo into a fully illustrated and narrated children’s book tailored to a specific topic, age range, and tone. ⚡ What it does OUTStories is an end-to-end platform for creating personalized children’s books: Snap & Style – Upload any image (a toy, snowman, household object, etc.) and select an art style. A reference character is generated and reused across all illustrations. Outline – Provide book-level metadata (title, moral, age group, number of pages). The app generates a complete table of contents. Story – The outline is expanded into structured, age-appropriate narrative text. Illustrations – Each page’s content is paired with a matching image featuring the character in context. Canvas Editor – Users can modify both text and images interactively within a visual editor. Audiobook – The final story is narrated with expressive text-to-speech using ElevenLabs. Final result : A downloadable PDF and MP3 audiobook — ready to share or print. 🏗️ How we built it We built OUTStories using a modular, event-driven architecture centered on Next.js 14 , Netlify Functions , and Supabase . AI services are integrated using GPT-4.1 for language and GPT-Image-1 for illustrations. Component Technology Purpose Frontend Next.js 14 Enables route groups, dynamic book pages, and modular layouts. API & Logic Netlify Functions All logic is serverless, with background processing for AI generation. Storage/Auth/DB Supabase Manages authentication, relational data (Postgres), and media storage. Image Generation GPT-Image-1 Produces consistent character visuals across all scenes. Story Pipeline GPT-4.1 + JSON Schemas Converts structured outline into narrative and prompt data. Narration ElevenLabs Adds high-quality, emotion-tagged speech for audio output. UI Components 21stdev Provides AI-generated production-ready React components. Hosting Netlify Handles deployment, preview branches, and background tasks. Development Workflow The development process leveraged AI-powered tools throughout: Bolt.new – Used for rapid prototyping of the core application structure and initial Netlify functions 21stdev – Generated production-ready components for complex UI elements Cursor IDE – Provided debugging, automated testing assistance, and function validation and fixing during development. Moreover i used Supabase MCP via Cursor since Bolt.new lacks native Next.js + Supabase integration 🧠 Architecture & Project Structure The app uses a decoupled frontend/backend model and a feature-based directory structure : /app – Next.js routes, layouts, and API endpoint definitions (mapped to backend functions via netlify.toml ). /netlify/functions – TypeScript serverless functions (standard and background) for tasks like outline generation, image rendering, and TTS. /components – Organized by feature ( /components/book-editor , /components/audiobooks , etc.). /hooks – Custom React hooks for data fetching, state sync, and background job tracking. /lib/utils/*-events.ts – Event emitters ( audiobook-events.ts , background-jobs-events.ts ) decouple UI from backend state updates. We use event-driven state updates via Supabase real-time and custom emitters to ensure responsiveness without unnecessary re-renders or polling. 🧗 Challenges Bolt.new GitHub integration issues – For several days, Bolt.new would lose the GitHub connection every time I refreshed the page. I had to create a new project and re-import the GitHub repo daily just to continue working. The issue eventually disappeared, but it was a major early blocker. 🏆 What we’re proud of Fully functional end-to-end pipeline – During hallway testing, first-time users created both e-book and audio output in under 15 minutes. Character consistency – Children immediately recognized the character from their original photo across all pages. No prompts or code for users – The entire AI pipeline is abstracted behind structured inputs and forms. 📚 What we learned This was our first time working with Bolt.new, Next.js 14, Netlify, and 21stdev as a combined stack. All proved highly productive: Bolt.new : Zero-config full stack ideal for hackathon speed. Next.js 14 : App Router enabled modular layouts and dynamic page logic with minimal overhead. Netlify : Preview branches helped avoid environment drift during collaboration. 21stdev : Non-trivial UI components. 🚀 What’s next Canvas 2.0 – Collaborative editing with live cursors, layer masks, filters, and version history. Cost optimization – Explore more image generation models for draft rendering; batch GPT calls. UX improvements – Better drag-and-drop, autosave, layout grids. Stripe integration – Per-book checkout and subscription plans for families. Company formation – Incorporate, secure initial funding, and formalize safety and moderation systems. OUTStories – Because every child deserves a story set in their own world. <div