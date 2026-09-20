---
slug: "textura-2sygh1"
url: "https://devpost.com/software/textura-2sygh1"
title: "Textura"
hackathon: "Mind the Product presents World Product Day: Everyone Ships Now"
organization: "Mind the Product"
winner: true
words: 642
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/media_journalism"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Textura

> Textura — Bringing handwritten Greek history back to life through AI-powered transcription, modernisation, and translation of historical and family Greek documents.

[Devpost](https://devpost.com/software/textura-2sygh1) · hackathon [[Mind the Product presents World Product Day- Everyone Ships Now]]

## Facets

**mechanism** [[human_in_the_loop]] [[vision_ocr]] [[voice_speech]]
**domain** [[media_journalism]]
**user** [[researcher]]
**substrate** [[document_pdf]] [[transcript_audio]] [[video_visual]]

**stack** brevo, claude, cloudflare, next.js, node.js, react, replit, resend, stripe, supabase, typescript, uptime-robot, zoho

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next

## Body

Textura Logo Transcript screen screenshot Landing page screenshot Inspiration Textura began with my late grandfather. He left behind handwritten memoirs in Greek: pages filled with family history, memories, and personal stories that had become effectively inaccessible. The handwriting was difficult, parts were written in older forms of Greek, and some pages used polytonic orthography unfamiliar even to many native speakers today. I realised that countless families, researchers, and local archives face the same problem: historical documents survive physically but become unreadable over time. On World Product Day 2026, I decided to see whether modern AI could help unlock documents like these. One of the first lines I managed to translate from my grandfather's memoir read: "I got engaged on 17 October 1940. Eleven days later, the Greco-Italian War was declared." That moment changed how I thought about AI. Not as automation for its own sake, but as a tool for recovering memory, preserving culture, and reconnecting people with stories they otherwise could not read. What it does Textura helps users transform handwritten Greek documents into readable, searchable text. The platform currently generates three layers: A diplomatic transcription that preserves the original spelling and historical forms. A modernised Greek version written in contemporary Greek. An English translation. The goal is not simply transcription accuracy, but helping people understand historical documents again. How we built it The prototype uses Claude Vision as the transcription engine through a modular AI pipeline designed to support additional providers and models in the future. What started as a single prompt in Replit evolved into a complete AI product with authentication, billing, analytics, correction workflows, and human-in-the-loop learning. The workflow currently supports: document upload, AI transcription, human correction and editing, preservation of polytonic Greek, structured storage of corrections, modernisation, and translation. One important design decision was treating each output layer separately rather than overwriting previous versions. The original transcription always remains the source of truth, preserving historical fidelity while improving accessibility. Challenges we ran into The biggest challenge was reliability. Historical Greek handwriting creates problems that generic OCR systems struggle with: inconsistent handwriting, degraded scans, archaic spelling, and polytonic text. Modern AI models are powerful, but they often try to "help" by silently modernising text or inventing missing words. A large part of the project involved designing prompts and workflows that prioritise preservation over fluency. In uncertain cases, the system is instructed to return "[illegible]" rather than hallucinate content. Another lesson was realising that Textura is not really an OCR product. The real problem is accessibility: helping people reconnect with family history and historical documents that have become difficult to read. Accomplishments we're proud of We're proud of creating a workflow that preserves historical fidelity while making difficult handwritten documents accessible to modern readers. Highlights include: support for polytonic Greek and historical linguistic forms, separate diplomatic, modernised, and translated reading layers, a human-in-the-loop correction workflow where user edits become structured feedback for future transcriptions, and successful transcription of real archival family material. On a personal level, the most meaningful achievement was finally being able to read and share pages from my grandfather's memoirs. What we learned This project taught me that building an AI product is very different from simply using AI models. The real challenge is not generating output; it is defining quality, creating feedback loops, and designing systems where humans and AI work together effectively. More broadly, Textura reinforced something I find deeply exciting about this moment in technology: individuals can now build meaningful products that previously required entire teams. What's next The next step is improving transcription quality and making the onboarding experience simpler for non-technical users. Longer term, I want Textura to support historians, researchers, libraries, museums, family archives, and additional historical handwriting domains beyond Greek. The goal remains simple: To help preserve cultural memory by making historical documents readable, searchable, and accessible again. <div