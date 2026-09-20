---
slug: "clever-course-9lc0aw"
url: "https://devpost.com/software/clever-course-9lc0aw"
title: "CleverCourse"
hackathon: "United Hacks V6"
organization: "Hack United"
winner: true
words: 499
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/accessibility"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# CleverCourse

> Education wasn't built for ADHD. We're fixing that. Bite-sized learning for distracted minds.

[Devpost](https://devpost.com/software/clever-course-9lc0aw) · hackathon [[United Hacks V6]]

## Facets

**domain** [[accessibility]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** drizzle, framer, gamification, gemini, next.js, radix, react, tailwind, turso(sqlite), zustand

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for clever course

## Body

course eagle view course home, an analytics page course home A sample article A sample article A course section's mindmap A course section's flashcards A course section's flashcard A course section's true or false A course section's true or false A course section's true or false A course section's fill in the blanks Kindly view the demo. Don't miss the the trailer!! Inspiration Traditional online courses are built for neurotypical learners. They're long, linear, and assume you can sit through hours of content without losing focus. For people with ADHD, this just doesn't work. We wanted to build something that actually respects how our brains function - short bursts of content, instant feedback, and enough dopamine hits to keep us coming back. What it does CleverCourse takes any topic you want to learn and generates a complete personalized course using AI. Each course includes articles broken into small pages, flashcards, interactive mind maps, and quizzes. There's a full gamification system with XP, levels, streaks, and achievements designed to trigger the reward mechanisms that ADHD brains crave. How we built it We used Next.js 15 with React 19 for the frontend, Drizzle ORM with Turso (SQLite) for the database, and Google Gemini 2.0 Flash for AI course generation. The gamification system uses variable rewards inspired by research on ADHD and dopamine. State management is handled by Zustand. The UI is built with Tailwind CSS, Radix UI, and Framer Motion for animations. Challenges we ran into Getting the AI to generate consistent, structured course content was tricky. We had to iterate on prompts a lot and build a section-by-section generation system to avoid hitting context limits. The gamification math took some tuning to feel rewarding without being exploitative. Also, migrating from local SQLite to Turso for deployment was a last-minute scramble. Accomplishments that we're proud of The course generation actually works well. You can input any topic and get a legitimate learning experience out of it. The gamification feels genuinely motivating without being annoying. Users will also be able to use the Podcast feature, which lets them easily navigate through an article with the help of sound and highlighting. And honestly, we're proud we shipped a complete product with auth, database persistence, and a polished UI in hackathon time. What we learned A lot about prompt engineering and how to structure AI outputs reliably. Also learned that gamification is harder to balance than it looks - too little and it's boring, too much and it feels manipulative. We also got way more comfortable with server components and server actions in Next.js. What's next for Clever Course We want to add spaced repetition for flashcards, collaborative courses where multiple users can learn together, and mobile push notifications for reminders. Also thinking about letting users upload their own materials (PDFs, notes) and having the AI build courses around that content exclusively. Long term, we'd like to add support for different learning disabilities beyond ADHD. Google Drive Link for demo & trailer: https://drive.google.com/file/d/1BsCLnGss61hHbmAKxZOyZ3yuUygdx7jf/view?usp=drive_link <div