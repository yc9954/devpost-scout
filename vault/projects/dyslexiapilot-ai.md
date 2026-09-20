---
slug: "dyslexiapilot-ai"
url: "https://devpost.com/software/dyslexiapilot-ai"
title: "DyslexiaPilot AI-The AI Companion for Student with Dyslexia"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 996
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/education"
  - "domain/mental_health"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# DyslexiaPilot AI-The AI Companion for Student with Dyslexia

> The AI-Powered Companion that helps students with dyslexia study smarter, faster, calmer and It comes packed with features designed to support student at every step of their literacy journey

[Devpost](https://devpost.com/software/dyslexiapilot-ai) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[structural_withholding]] [[vision_ocr]]
**domain** [[accessibility]] [[education]] [[mental_health]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[video_visual]]

**stack** gemini, genkit, next.js, react, shadcn-ui, tailwind-css, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what’s next for dyslexiapilot ai
- team members:

## Body

about page prompts in genkit flows in genkit mood check page Quiz Generate Page Rhyme Check Game Page Scan Class Note After Scan Note Reading Practice Writing Assistant Page Word Game Page Sound Match Game Setting Page DyslexiaPilot AI — The AI Companion for Students with Dyslexia A student-centric, multi-feature platform designed to make learning more accessible, confident, and stress-free. Inspiration Students with dyslexia face challenges that most others never see — slow reading speed, decoding difficulties, confidence loss, information overload, and high exam pressure. What started as a simple idea for a reading assistant grew into a mission: build a single AI-powered platform that understands dyslexic students and adapts to their learning needs. We were inspired by: Real challenges dyslexic students face in classrooms and exam preparation. The lack of unified tools that combine reading support, writing help, quizzes, summaries, notes, and mental wellness. The desire to make education more accessible, inclusive, and student-friendly. The hackathon theme: “Build tools that help students.” DyslexiaPilot AI is built by students, for students who deserve tools that empower—not overwhelm—them. What It Does DyslexiaPilot AI is a multi-purpose web app designed as a complete learning and wellbeing companion for students with dyslexia. Key Modules Adaptive Text Reader : Read any text with options to simplify complex language, generate summaries, and listen to an AI-powered audio narration. You can also scan text from an image. AI Writing Assistant : Get real-time help as you write. The assistant corrects spelling (including common dyslexic patterns like b/d reversals), explains grammar simply, and offers a voice-to-text option. You can also rephrase sentences to improve clarity. Reading Practice : Practice reading aloud and receive friendly, encouraging feedback from an AI coach designed to be emotionally supportive. Interactive Games : Engage in fun exercises designed to strengthen literacy skills in a low-pressure environment. Games include: Word Scramble : Unscramble letters to form a word. Sound Match : Listen to a word and choose the correct spelling from a list of homophones. Rhyme Time : Find and match pairs of rhyming words. Spell Check : Identify the correctly spelled word from a list of common misspellings. Letter Hunt : Find a specific target letter in a grid of distracting letters. Quiz Forge : Generate practice quizzes from any text to help you study and retain information. Mental Health Check-in : A private space to log your mood, get supportive suggestions from an AI coach, reflect in a private journal, and practice guided breathing exercises. Community Hub : A dedicated space to connect with peers and mentors who understand the journey with dyslexia. Personalized Settings : Adjust the theme (light/dark), font size, and line height to create the most comfortable reading experience for you. All modules work together to support reading, writing, studying, revision, and mental wellness. How We Built It Tech Stack Framework : Next.js (with App Router) UI Library : React Language : TypeScript Styling : Tailwind CSS UI Components : ShadCN UI Generative AI : Firebase Genkit Core Architecture +--------------------------------+ | Client (Browser) | | (Next.js, React, ShadCN UI) | +--------------------------------+ | | User Interaction (e.g., clicks a button) v +--------------------------------+ | Server (Next.js App Router) | | (Server Actions) | +--------------------------------+ | | Function Call (e.g., `simplifyText(text)`) v +--------------------------------+ | AI Layer (Genkit) | | (AI Flows) | +--------------------------------+ | | API Request v +--------------------------------+ | Google Generative AI Models | | (Gemini) | +--------------------------------+ AI Flows Built assist-writing : Analyzes text for spelling and grammar errors, providing corrections and simple explanations tailored for users with dyslexia. generate-audio-narration : Converts a string of text into a natural-sounding audio narration, which is used in the Adaptive Text Reader and the Sound Match game. generate-quiz-flow : Creates multiple-choice or open-ended quiz questions based on a provided block of text, powering the Quiz Forge. get-coping-suggestion : Provides a short, actionable, and empathetic suggestion based on a user's selected mood in the Mental Health Check-in. get-journal-feedback : Analyzes a user's journal entry to determine its sentiment and provides a supportive, non-judgmental reflection with gentle, actionable advice if the sentiment is negative. get-reading-feedback : Compares a user's spoken text against an original sentence and generates encouraging, emotionally supportive feedback for the Reading Practice feature. scan-and-convert-text : Uses Optical Character Recognition (OCR) to extract plain text from an uploaded image, allowing users to digitize text from books or documents. simplify-text-for-dyslexia : Rewrites complex text into a simpler format with shorter sentences and more common words to improve readability. summarize-text-for-review : Generates a concise summary of a long piece of text for quick review. Process We rapidly prototyped each module, integrated flows one by one, then polished the UI using accessibility-focused design (open dyslexic fonts, high contrast, larger spacing). Challenges We Ran Into Designing for accessibility while keeping the platform feature-rich Creating dyslexia-aware text simplification without losing meaning Combining multiple modules while keeping the app fast Genkit hot-reload conflicts with Next.js dev server Building a large multi-module app in less than 48 hours Accomplishments That We're Proud Of Built a complete accessibility-first AI platform during the hackathon Designed an experience that reduces cognitive load for dyslexic students Integrated 10+ AI-powered features into one seamless tool Created modules that support: reading writing studying revision exam prep mental wellness Delivered a project perfectly aligned with the theme: “Build something that helps students.” Students testing early versions said: “This is the first time studying feels less stressful.” What We Learned Building clean, scalable Genkit flows Designing dyslexia-friendly interfaces Importance of empathetic AI (especially for mental wellness) Accessibility requires iteration and listening What’s Next for DyslexiaPilot AI We plan to grow the prototype into a full learning companion with: Mobile App (Android/iOS) Chrome Extension for real-time reading help Real-time speech-to-reading coach Classroom dashboard for teachers Mindmap generator from PDFs Offline Mode for low-connectivity regions Student community for peer support Gamified learning milestones Long-term Goal ❗ Make learning accessible, inclusive, and empowering for every student with dyslexia. Team Members: Krushna Chandra Pradhan (Team Lead) <div