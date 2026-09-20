---
slug: "quizzr-prsxik"
url: "https://devpost.com/software/quizzr-prsxik"
title: "Quizzr"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 532
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Quizzr

> Quizzr is an app that enables students to efficiently learn and thrive by helping retention through flashcards and bite-sized quizzes for easy and convenient studying.

[Devpost](https://devpost.com/software/quizzr-prsxik) · hackathon [[Student HackPad 2025]]

## Facets

**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]]

**stack** next, nextjs, node.js, openrouter, postgresql, react, tailwind, typescript

## How they structured the write-up

- what we built and why it matters
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next for quizzr

## Body

What We Built and Why It Matters Studying is tough, and we need to change that. As students, we are expected to take notes in class, review them, and understand and apply those concepts on tests and assignments. It sounds simple, but in practice it can overwhelm anyone. The jump from messy notes to clear answers creates a real barrier for students who want to do well but struggle to organize what they learned. We saw how common this problem was among our friends and in our own experiences. That pushed us to think about the specific ways we lost track of information or forgot details right when we needed them. From that reflection came Quizzr , a tool that turns scattered class notes into strong study material. It uses AI to generate flashcards and free quizzes so students can learn efficiently without fighting through pages of disorganized text. We built Quizzr with technologies we enjoy working with, including Next.js, PostgreSQL, and Typescript. GPT 5.1 Codex helped with debugging and documentation, while Claude Sonnet 4.5 supported styling improvements. Notes can be imported from Google Docs or Quizlet, or typed directly after class when the ideas are still fresh. If someone misses a day, they can simply have a friend share their notes through the built-in sharing system. Bid adieu to the struggles of trying to decipher notes on archaic historical figures, and use Quizzr. Our free site can help numerous students with their studies and can improve their grades fairly and effectively. We built this application with the mindset to help students circumvent the monotony of studies and learn with a more interactive approach. Inspiration We wanted a study tool built by students who actually know what studying feels like. Our love of coding and our shared frustration with messy notes pushed us to build something better. What It Does Transforms raw class notes into flashcards Generates free quizzes tailored to the material Helps students learn faster and more confidently How We Built It Frontend: Next.js App Router with TypeScript, React Server Components, Tailwind CSS, and Radix-inspired UI primitives. Backend: Node.js 20 on Vercel/Next runtime with NextAuth, custom API routes, and OpenRouter for AI generation. Database: PostgreSQL (Docker/Postgres 16) orchestrated through Prisma ORM. Tooling: ESLint + TypeScript for safety, Turbo dev server, and OpenRouter SDK-free REST calls. AI tools: GPT 5.1 Codex for debugging and documenting code, and Claude Sonnet 4.5 for styling guidance Challenges We Ran Into Getting AI features to behave consistently Handling user login, authentication, and backend structure Balancing development with different team schedules Debugging issues that popped up close to deadlines (Still an issue) Sometimes it doesn't let you scroll, so you have to refresh Accomplishments We’re Proud Of Building a functional site in a short period of time Learning new concepts and solving real technical problems Turning a simple idea into something students can actually use What We Learned Strong time management Clear team communication How front-end, backend, and database layers work together What’s Next for Quizzr Adding more AI-powered study tools Improving the import system for notes Enhancing the user interface Introducing light ads or cost offsets so the platform can stay free for students <div