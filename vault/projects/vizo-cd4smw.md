---
slug: "vizo-cd4smw"
url: "https://devpost.com/software/vizo-cd4smw"
title: "Vizo"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 1045
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Vizo

> Vizo is AI enhanced edtech platform

[Devpost](https://devpost.com/software/vizo-cd4smw) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[education]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** gemini-api, lanngchain, next-js-15, openstack, pgvector, postgresql, stripe, supabase, taikwind

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for vizo

## Body

Vizo AI provides curated Youtube video recomendation Inspiration Nagaland has roughly 440,000 students, and a huge share of them don't speak Hindi as a first language. Yet most STEM content on YouTube—the de facto free tutor for Indian students—is made by mainland creators teaching in Hindi who aren't aware we exist. For a student in this unrepresented areas trying to learn outside of their classroom to learn online, that's a wall before the lesson even starts. Quality syllabus-aligned teaching exists locally, but it's scattered, undiscoverable, and has no platform to scale. I wanted to build something that closes that gap: an AI tutor that explains concepts clearly regardless of language background, paired with a way to surface video lessons from local teachers who actually understand the curriculum and the students. What it does Vizo AI lets a student type or photograph any Physics, Chemistry, Biology, or Maths problem and get a complete, step-by-step solution in seconds—properly typeset with KaTeX, not garbled plain-text math. Behind the scenes, every question is run through a RAG pipeline that searches a knowledge base built from NCERT, CBSE and OpenStax textbooks using pgvector semantic search. That retrieved content, combined with curriculum-aware learning objectives (so the tutor knows what prerequisites a student should already have), is fed to the AI model to generate a deeply contextual, Socratic-style explanation rather than a generic answer. After solving, Vizo recommends curated, unlisted YouTube videos mapped to the exact chapter and concept—this is where local teachers' content gets surfaced to the students who need it most. Students also get a mastery tracker that follows them through a prerequisite chain (e.g., you can't master Newton's Second Law without "forces" and "free-body diagrams"), interactive virtual labs for hands-on simulation, and a searchable solution history. Vizo AI also provide virtual lab enhancing students learning by allowing them to experiment practicaly ,and a structured learning management with mastery tracking. The free tier gives 30 problems a month, no card required—paid tiers unlock photo upload, virtual labs, and unlimited problems. How I built it The frontend is Next.js 15 (App Router) with TypeScript, Tailwind, and Framer Motion on a pastel design system, built mobile-first since most students in Nagaland access the internet via phone. For the RAG layer, I chunk NCERT/CBSE/IGCSE/AP/IB/OpenStax textbooks into ~300-word semantic segments, generate embeddings, and store them in Supabase with pgvector, using ivfflat indexing and a match_knowledge_chunks() function with a cosine similarity threshold to filter noise. On top of that sits a curriculum graph—curricula → courses → units → learning objectives → lessons—so the system knows prerequisites, difficulty, and mastery thresholds for every concept. When a student asks a question, I generate an embedding, retrieve the top-5 matching chunks, pull their current learning objectives and mastery state, and assemble all of that into a prompt for the Gemini API, streaming the response back so KaTeX can render equations live as they arrive. Video recommendations are handled via a videos table indexed on (class_level, subject, chapter) for fast lookups against concept tags after a solve completes. Auth, RLS, subscriptions (Stripe), and email (Resend) round out the production stack, deployed on Vercel. Challenges I ran into Getting RAG retrieval to actually be useful—not just technically working—took a lot of tuning. Early on, the similarity threshold either let in irrelevant chunks that confused the model's explanations or filtered out everything, leaving no grounding context at all. I landed on a 0.65 cosine similarity threshold plus a fallback "ALL curriculum" bucket for cross-cutting formula sheets. Designing the curriculum graph was harder than expected—prerequisites in real syllabi aren't a clean tree, they're a tangled web (e.g., "vectors" feeds into both kinematics and electromagnetism). Modeling that as a many-to-many graph while keeping mastery tracking simple enough for students to actually understand took several iterations. Streaming the AI response while simultaneously rendering KaTeX in real time also caused rendering glitches—partial LaTeX expressions would render as broken syntax mid-stream before completing. I had to build buffering logic to hold incomplete math blocks until they were syntactically complete. Finally, mapping unlisted local-teacher videos to precise concept tags at scale, while keeping lookups fast, required building a composite index and a separate ingestion script rather than relying on ad-hoc tagging. Accomplishments that I'm proud of I'm proud that Vizo isn't just "ChatGPT with a math skin"—it's a genuinely curriculum-aware system that knows what a student should already know before explaining something new, and adjusts accordingly. The RAG pipeline grounds every answer in real textbook content across six major curricula, so explanations stay syllabus-relevant rather than generically "correct but irrelevant to what's being taught." I'm also proud of building a real path for local educators' content to reach the students who most need it, in a state that's been largely invisible to mainstream EdTech. And I shipped a production-grade stack—RLS-secured database, Stripe billing, rate limiting, atomic usage counters—solo, with the whole thing live at vizo.ai. What I learned I learned that language and curriculum alignment matter just as much as raw model intelligence—an objectively "correct" explanation can still fail a student if it assumes a curriculum context or vocabulary they've never encountered. I also learned a lot about the practical tradeoffs in RAG systems: chunk size, similarity thresholds, and embedding choices all have real, felt effects on whether a tutor's explanation actually lands. On the engineering side, I got much more comfortable with pgvector at scale, designing graph-like data models in PostgreSQL, and handling the UX challenges of streaming AI responses alongside real-time math rendering. What's next for Vizo My immediate priority is partnering directly with local teachers in Nagaland to build out a much larger library of unlisted, syllabus-aligned video content—turning Vizo into a real distribution channel for educators who've never had one. I also want to expand the RAG knowledge base to include regional board curricula beyond NBSE, add more languages and dialectal explanation styles for students who think in Nagamese or tribal languages even when writing in English, and grow the virtual labs library across all four subjects. Longer-term, I want to bring Vizo into classrooms directly, working with schools across Nagaland and the wider Northeast to make AI tutoring a standard part of how students learn—not a substitute for teachers, but a way to make sure every student has support between classes. <div