---
slug: "provit"
url: "https://devpost.com/software/provit"
title: "Provit"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 608
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
---

# Provit

> AI-powered study tool that builds 5-lesson courses from your notes and locks the next lesson until you can actually explain the last one

[Devpost](https://devpost.com/software/provit) · hackathon [[DSH Hacks V1]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]]

**stack** express.js, html5, localstorage, node.js, openrouter, quickdb, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for provit

## Body

Inspiration I used to think I was studying. I would open up an AI chatbot, ask it to explain a topic, read through the response, and feel like I understood it. Hours of notes summarized. Concepts explained. Flashcards generated. But when the exam came, nothing. Blank. The problem was not the tools. The problem was me. I was consuming information and calling it learning. I was letting AI do the thinking for me, then convincing myself I had done the work. It felt productive. It looked like studying. It was not. I was not learning. I was just reading. That realization is what inspired Provit. What it does Provit turns your notes into a 5 lesson course and locks the next lesson until you can actually explain the last one in your own words. You paste your notes, upload a PDF, or type any topic. Provit structures it into 5 focused lessons with no filler and no fluff. After each lesson you have to explain it back in your own words. AI grades your explanation. If you cannot prove you understood it, the next lesson does not unlock. The AI is not doing the thinking for you anymore. It is holding you accountable. How we built it Provit is built with React and TypeScript on the frontend. For AI I initially tried Groq but ran into reliability issues, so I switched to OpenRouter which gave me much more stable access to language models for both lesson generation and answer grading. Course progress is stored in localStorage so students can pick up where they left off without needing an account. The app is deployed on QuickDB. Challenges we ran into The biggest challenge was building the AI grading engine. Getting it to evaluate a student's free text explanation fairly was harder than expected. It needed to check for real understanding rather than just keyword matching, and finding that balance took a lot of iteration. Switching from Groq to OpenRouter mid build was also a challenge but ultimately the right call. It made the whole system more stable and reliable. The other challenge was resisting the urge to make it too easy. Every instinct said add hints, add retries, make it forgiving. But that would have recreated the exact problem I was trying to solve. The friction is the feature. Accomplishments that we're proud of Getting the locked progression system to actually work felt like a big moment. When a student genuinely cannot move forward until they prove they understood something, the whole experience changes. It stops feeling like passive reading and starts feeling like real learning. Also proud of how fast the onboarding is. No signup, no setup. You drop your material and you are learning in under 60 seconds. What we learned I learned that the most important thing in an edtech product is not how much content you deliver but how much understanding you verify. Most tools optimise for engagement. Provit optimises for retention. Those are very different goals and they lead to very different product decisions. I also learned that switching infrastructure mid build, while painful, is sometimes the right move. Groq was fast but unstable for my use case. OpenRouter solved that and unblocked everything else. What's next for Provit The next step is adding support for more input types including YouTube videos and lecture recordings so students can learn from any format. After that, spaced repetition so Provit resurfaces lessons you struggled with at the right time. And eventually a classroom mode so teachers can assign topics and track which students actually proved they understood the material, not just who clicked through it. <div