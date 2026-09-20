---
slug: "asd-4sn7l5"
url: "https://devpost.com/software/asd-4sn7l5"
title: "StudyReels"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 270
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

# StudyReels

> Turn any topic into an engaging AI-generated study reel with gameplay visuals, character dialogue, and TTS. Learn faster with short, fun, auto-generated videos built in minutes.

[Devpost](https://devpost.com/software/asd-4sn7l5) · hackathon [[Student HackPad 2025]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]]

**stack** css3, ffmpeg, node.js, react, tailwind, ts, tts, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the project

## Body

Inspiration Studying today still means long PDFs, boring text, and zero engagement. Meanwhile, students spend hours consuming short-form videos. We wanted to merge education with entertainment and make learning feel as fun as watching reels—fast, visual, and memorable. What it does Our tool turns any topic into an engaging AI-generated study reel. It: Creates a dialogue-based explanation using AI Adds character voices using TTS Uses gameplay/background footage Generates subtitles automatically Exports a fully edited reel in minutes How we built it Frontend: React + TypeScript Backend: Node.js + Express Script Generation: Gemini API Voice Generation: Hugging Face (Dia 1.6B TTS) Video Processing: FFmpeg for merging audio, video, and subtitles Built a pipeline: Topic → Script → Voices → Subtitles → Final Reel Challenges we ran into Getting natural-sounding, stable TTS voices Syncing subtitles accurately with dynamic dialogue timing FFmpeg rendering issues and audio–video alignment Making the workflow fast enough for a live demo Managing multiple AI outputs smoothly Accomplishments that we're proud of Fully automated script-to-video generation within 24 hours Achieved clean dialogue + synced subtitles Stable video rendering pipeline with no manual editing Delivered a polished, demo-ready MVP Made studying actually fun for users who tested it What we learned Integrating multiple AI models in one pipeline Handling TTS delays, audio normalization, and timing Advanced FFmpeg processing and automation Rapid prototyping and MVP building under time pressure What's next for the project More character voices + personality styles Customizable templates for different subjects Auto-generated quizzes based on the generated reel Launching a mobile app version Social sharing & community-driven study reels Scaling for long-form explainers and YouTube channels <div