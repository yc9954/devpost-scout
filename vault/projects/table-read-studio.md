---
slug: "table-read-studio"
url: "https://devpost.com/software/table-read-studio"
title: "Table Read Studio"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 369
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/document_pdf"
---

# Table Read Studio

> Table Read Studio lets you run scenes with AI voices instantly - whether you’re a writer testing dialogue or an actor recording a self-tape.

[Devpost](https://devpost.com/software/table-read-studio) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**substrate** [[document_pdf]]

**stack** elevenlabs, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for table read studio

## Body

Inspiration As a screenwriter and filmmaker, Vaiga often needed to hear her scripts read aloud to get a sense of pacing, tone, and character dynamics. But organising table reads takes time, and actors aren’t always available — especially during early drafts. We also noticed a recurring issue when requesting self-tapes from actors: many needed a few days because they didn’t have a scene buddy to read with. This simple gap in the creative process inspired us to build Table Read Studio — a fast, flexible tool for writers and actors to run scenes using AI voices. What it does Table Read Studio is a web app that turns any screenplay into a live table read using realistic AI-generated voices. Upload scripts in .fountain or .pdf format Auto-detects characters and scene structure Assign characters to either yourself or an AI voice Filter and preview AI voices from the ElevenLabs library Optionally record the read using your webcam and microphone It’s designed for screenwriters testing dialogue and actors recording self-tapes — even when they don’t have a scene partner. How we built it We scaffolded the app using Bolt , and built it with React and TypeScript . We integrated the ElevenLabs API to provide AI voice generation and used the browser’s native media capabilities to handle video recording. The key steps: Parse and structure screenplay files client-side Let users assign voices to characters through a simple UI Preload and cache AI audio for smooth playback Enable optional recording via the File System Access API Everything runs in the browser — no server required. Challenges we ran into Building a clean, intuitive UX under time pressure Making the playback feel natural and responsive Parsing and formatting the screenplay into standard script structure Accomplishments that we're proud of A smooth, usable experience for both writers and actors Realistic-sounding table reads using AI voices A simple and clean UX What we learned How to integrate and use the ElevenLabs voice API effectively How to quickly build and iterate using Bolt What's next for Table Read Studio AI voice direction and tone control Voice cloning or upload support for actors' own voices A tailored version for casting directors to review self-tapes more efficiently <div