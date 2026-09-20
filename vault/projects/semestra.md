---
slug: "semestra"
url: "https://devpost.com/software/semestra"
title: "Semestra"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 330
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/document_pdf"
---

# Semestra

> Your semester, simplified. Semestra uses AI to read your syllabuses, organize deadlines, and forecast grades, all in one dashboard. Upload your syllabus, and watch your semester plan itself.

[Devpost](https://devpost.com/software/semestra) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[document_pdf]]

**stack** css3, deno, dotenv, express.js, fetch-api, framer-motion, gemini-api-(google-generative-ai), git, github, html5, javascript, json, netify, node.js

## How they structured the write-up

- check out the demo video here: https://www.loom.com/share/11d9696f818041b18c0fe7c9b9cfb794
- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for semestra
- ai-tools i used

## Body

Check out the demo video here: https://www.loom.com/share/11d9696f818041b18c0fe7c9b9cfb794 Inspiration Every semester, students scramble through chaotic syllabi, missed deadlines, and confusing grade breakdowns. I wanted to fix that, aka make managing classes feel seamless instead of stressful. Semestra was born from that frustration, turning messy PDFs into an intelligent academic hub. What it does Semestra uses AI to read your syllabus, extract every assignment, exam, and grade weight, and instantly build a personalized timeline, calendar, and grade predictor. If something is parsed wrong, the user can always manually add changes. There are other helpful features like a promodoro timer, and friendly competition with your friends. How I built it I built Semestra using React, Supabase, and Gemini’s text-understanding APIs. The PDF parser extracts structured data, which is then stored in Supabase and displayed through a dynamic, dark-mode-optimized interface built with Tailwind and Framer Motion for smooth interactions. Challenges I ran into Parsing academic syllabi was way harder than expected because every professor formats things differently. I had to combine AI parsing with regex fallback logic and handle CORS issues, Supabase schema errors, and edge function debugging just to get somewhat consistent results, it can always be improved on! Accomplishments that I am proud of I built a full-stack app from scratch while learning Supabase for the first time: setting up authentication, relational schemas, and real-time data syncing without relying on Firebase. I integrated Gemini for intelligent PDF parsing and built a responsive React interface with Tailwind and Framer Motion for smooth transitions. What I learned I learned how powerful AI becomes when combined with solid backend structure and great UX. I also learned that debugging at 2 AM with Supabase errors builds character. What's next for Semestra After fixing the rest of the smaller bugs and adding more features, I want to start expanding this in my college and see if it actually makes manually inputting stuff in calendars go away. AI-tools I used I semi-relied on codex, claude, and copilot. <div