---
slug: "insight-ai-9hijxc"
url: "https://devpost.com/software/insight-ai-9hijxc"
title: "Insight.AI Version 2.0"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 782
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# Insight.AI Version 2.0

> Insight.AI is a Chrome extension that simplifies PDFs, videos, and web content into instant summaries, making research and learning faster than ever.

[Devpost](https://devpost.com/software/insight-ai-9hijxc) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]] [[education]] [[labor_employment]] [[supply_logistics]]
**user** [[developer]] [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[transcript_audio]] [[web_dom]]
  <sub>weak: code_repository</sub>

**stack** chrome, css3, gemini-api, html5, javascript

## How they structured the write-up

- inspiration
- team members
- what it does
- 📘 project description (what we built and why it matters)
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for insight.ai
- 🔗 github repository
- 🤖 ai tools disclosure
- 📝 post-event feedback

## Body

Inspiration As students, we often struggled with long PDFs, dense articles, and hour-long YouTube lectures just to extract a few key points. Switching between multiple tabs to search for explanations slowed down our workflow and made learning overwhelming. This inspired us to build InsightAI —a simple, fast, and intelligent assistant that provides instant understanding directly on any webpage. We wanted a tool that makes learning smoother, faster, and more accessible for students everywhere. Team Members Kumaraguru P – Developer & Core Architect Nithya Sri S – Research, Testing & Content Validation Pandeeswaran B – UI/UX, Documentation & Feature Design Together, we collaborated to design, build, and refine InsightAI into a polished and reliable learning assistant. What it does InsightAI is a powerful Chrome extension that helps users instantly understand any text they encounter online. Using the Google Gemini API , it provides: ✨ Explanations for complex terms or topics 📌 Summaries of long paragraphs or articles 🌐 Translations into simple, clear language 📄 PDF summarization through integrated PDF.js 🎥 YouTube transcript summarization 🔍 Right-click text summarizer 🎚️ Readability modes (kid, simple, bullet, one-line) It works directly on the page, making research, studying, and browsing effortless. 📘 Project Description (What we built and why it matters) InsightAI is a multi-modal Chrome extension designed to help students understand information faster by summarizing PDFs, YouTube transcripts, and webpage text instantly. Students often lose time switching between tabs to search for definitions or explanations, breaking the flow of learning. InsightAI solves this by providing direct, AI-powered understanding right where they need it. Using the Google Gemini API, InsightAI can summarize, explain, or translate any highlighted text. It includes a clean tooltip, a draggable response panel, PDF summarization via PDF.js, and YouTube transcript extraction for concise summaries and follow-up resources. With multiple readability modes—kid, simple, bullet, and one-line—the tool adapts explanations to the user’s preferred learning style. We built InsightAI using Chrome Manifest V3, JavaScript, content scripts, a background service worker, and custom UI components. The architecture ensures secure Gemini API requests, smooth content injection, and fast response rendering. We faced challenges such as parsing PDFs, inconsistent YouTube captions, prompt engineering for multiple content types, and ensuring that the injected UI did not interfere with webpage layouts. InsightAI matters because it transforms how students consume information. Instead of spending hours reading dense content, learners can instantly access key ideas. In a world where information overload is common, InsightAI helps students focus on understanding rather than searching—making learning more effective, enjoyable, and accessible. How we built it Chrome Manifest V3 JavaScript / ES6 Content Scripts for text detection and UI injection Service Worker for secure Gemini API communication PDF.js for extracting text from PDFs Custom UI Components for tooltips and floating result panels Prompt engineering for optimized summarization and explanations Content scripts capture text selections and communicate with the background service worker, which sends prompts to Gemini and returns structured responses displayed in a floating UI. Challenges we ran into Extracting clean text from PDFs using PDF.js Handling YouTube videos without consistent captions Designing UI that remains compatible across different websites Reducing API usage while maintaining fast responses Ensuring injected UI elements never overlap or break page layouts Crafting consistent prompts for webpages, PDFs, and transcripts Accomplishments that we're proud of Built a fully functional multi-modal learning assistant Integrated PDF + YouTube + webpage summarization into one tool Designed a smooth, intuitive floating UI Created customizable readability modes Greatly improved learning flow for students Delivered a tool that feels natural and supportive within everyday browsing What we learned Deep understanding of Chrome extension architecture (MV3) Secure API communication with service workers Prompt engineering techniques for various content types PDF parsing, transcript extraction, and text cleaning UI/UX design for browser-injected components Building tools that genuinely help users learn faster What's next for Insight.AI Automatic flashcard generation (Anki/Quizlet export) Concept-map visualization for articles and transcripts Offline caching for repeated summaries User accounts + cloud sync for history and settings A notes panel with auto-generated study notes Support for more browsers (Edge, Brave, Firefox) InsightAI will continue evolving into a complete learning companion that helps students understand information quickly—no matter where they find it. 🔗 GitHub Repository https://github.com/kumaraguru911/Insight.AI-extension 🤖 AI Tools Disclosure Google Gemini API – Used for summarization, explanation, translation, PDF analysis, transcript processing, and improving readability. ChatGPT (OpenAI) – Assisted in brainstorming ideas, refining prompts, debugging guidance, improving documentation, and structuring the project narrative. AI tools supported development but the build, logic, design, and code were manually created by the team. 📝 Post-Event Feedback We will provide detailed feedback on the AI tools we used through the official post-event survey to help sponsors improve and enhance their platforms. <div