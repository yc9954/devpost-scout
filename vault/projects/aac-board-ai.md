---
slug: "aac-board-ai"
url: "https://devpost.com/software/aac-board-ai"
title: "AAC Board AI"
hackathon: "Google Chrome Built-in AI Challenge 2025 "
organization: "Google"
winner: true
words: 492
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/mental_health"
  - "user/developer"
  - "substrate/structured_db"
---

# AAC Board AI

> AAC Board AI is a local-first communication board for people who cannot rely on speech. It works with or without AI, using Chrome’s on-device models to proofread, rephrase, and translate privately.

[Devpost](https://devpost.com/software/aac-board-ai) · hackathon [[Google Chrome Built-in AI Challenge 2025]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[accessibility]] [[developer_tools]] [[mental_health]]
**user** [[developer]]
**substrate** [[structured_db]]
  <sub>weak: code_repository</sub>

**stack** indexeddb, mui, openboardformat, proofreader, react, rewriter, speechsynthesis, translator, typescript, zod

## How they structured the write-up

- recent updates
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aac board ai

## Body

Source code: github.com/shayc/aac-board-ai Recent updates Since the original challenge submission, AAC Board AI has gained: PWA support for installation and offline use Keyboard-accessible grid navigation Automated unit and end-to-end tests Inspiration Communication is a basic human need, yet for people who can't rely on speech, even building a short sentence can take immense effort. I wanted to explore how Chrome's built-in AI could make that process faster, more expressive, and more personal — all while keeping data private and on-device. What it does AAC Board AI is a communication board for people who cannot rely on speech, including some people with ALS, autism, or cerebral palsy. It lets users tap pictograms to build messages — like any AAC board — but it goes further, bringing those messages to life with Chrome's on-device AI: Proofreader API refines telegraphic utterances (e.g., “I want go grandma”) into more natural phrasing (“I want to go to Grandma’s”). Rewriter API adjusts tone — neutral, formal, casual, or custom (e.g., “playful and polite”). Translator API translates the same message into supported languages and speaks it using an available system voice. How we built it AAC Board AI is built with React 19, Vite, and Material UI 7, using IndexedDB for fully local data storage. At its core is a schema-validated Open Board Format (OBF) importer written in TypeScript with Zod, ensuring compatibility with community-authored AAC boards. Imported boards are unpacked into an on-device database ( aac-board-db ) with structured tables for boardsets, boards, and symbol assets. On top of that, a collection of typed React hooks orchestrates Chrome’s Built-in AI APIs — Proofreader, Rewriter, and Translator — allowing messages to be corrected, rewritten, and translated instantly and privately, all locally. Challenges we ran into I experimented with the Prompt API to generate sentence completions based on the current message and available words. It worked about 80% of the time and was impressive when it did — but the remaining 20% produced illogical results (“I eat ocean”). For an assistive communication tool, that margin of error is too high. Accomplishments that we're proud of The project is designed to reduce effort, increase speed, and help people express personality. It also helps speech therapists translate and reuse existing boards instantly. The open-source implementation serves as a transparent learning resource for developers building accessible, privacy-respecting AI tools. What we learned Built-in AI enables a new class of applications that are private, fast, and expressive. I'm continuing to explore how these models can enhance assistive communication tools. What's next for AAC Board AI Prompt API Revisit the Prompt API to predict what users might want to say next, based on context such as: Current sentence Available words Past messages Time of day Library View Add a library view for all imported boards, allowing users to search, filter, and manage their board sets more easily. Continued UX & Accessibility Continue refining the interface and expanding accessible input options based on real-world feedback. <div