---
slug: "refinelab"
url: "https://devpost.com/software/refinelab"
title: "RefineLab"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 562
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# RefineLab

> A writing growth engine for students that analyzes essays, teaches skills, tracks growth, and helps understand grading patterns: all while maintaining strict academic integrity.

[Devpost](https://devpost.com/software/refinelab) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]] [[researcher]]
**substrate** [[document_pdf]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** gemini-api, mammoth, next.js, nextauth.js, pdf-lib, postgre, prisma, react, recharts, restful, shadcn, tailwaind, tesseract, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- ai tools disclosure
- team

## Body

Profile Dashboard Metrics Home Content RefineLab Inspiration As students navigating the challenging world of academic writing, we noticed a critical gap: while AI writing assistants are abundant, tools specifically designed for analyzing and improving academic essays according to rigorous standards like AP Language & Composition are virtually non-existent. We were inspired to create RefineLab—a platform that doesn't just check grammar, but deeply analyzes thesis clarity, argument depth, evidence quality, and rhetorical sophistication. Our goal was to build a tool that helps students become better writers by understanding the why behind good writing, not just the what. What it does RefineLab is a comprehensive academic writing analysis platform that provides: AI-Powered Essay Analysis : Upload essays and receive detailed feedback based on AP Lang's 6-point rubric, analyzing thesis clarity, argument development, evidence quality, sophistication, structure, and sentence variety Live Essay Editor : A distraction-free fullscreen editor with real-time metrics tracking word count, reading level, vocabulary diversity, transition word usage, and academic tone—plus instant writing suggestions for passive voice, weak qualifiers, repetitive words, and paragraph structure Essay Comparison Tool : Side-by-side comparison of multiple essays with performance deltas and visual metrics to track improvement over time Structure Visualization : Interactive flow maps showing essay organization with color-coded paragraph analysis and expandable content Writing Lessons : Structured curriculum covering thesis development, argument construction, evidence integration, and rhetorical analysis Progress Tracking : Dashboard with growth charts, recent essay history, and personalized improvement recommendations How we built it Frontend & Framework: Next.js 16 with App Router and React Server Components for optimal performance TypeScript for type safety and better developer experience Tailwind CSS v4 with custom animations and gradient effects shadcn/ui component library for consistent, accessible UI Recharts for data visualization Dark mode support with next-themes Backend & Database: PostgreSQL via Neon for reliable, scalable data storage Prisma ORM v6 for type-safe database operations NextAuth.js v5 for authentication with Google OAuth via Firebase RESTful API routes with Next.js API handlers AI & Document Processing: Google Gemini 2.0 Flash Lite for essay analysis and grading pdf-lib for serverless PDF processing (replaced canvas-dependent libraries for Vercel compatibility) mammoth for .docx conversion tesseract.js for OCR on images Challenges we ran into 1. Serverless Deployment Compatibility Our initial PDF processing relied on pdfjs-dist and canvas , which required native dependencies incompatible with Vercel's serverless environment. We solved this by switching to pdf-lib combined with Gemini AI for text extraction—a creative solution that actually improved reliability. 2. Real-time Metrics Performance Calculating live metrics (vocabulary diversity, transition words, academic tone) on every keystroke initially caused lag. We implemented debouncing and optimized string processing algorithms to maintain 60fps typing experience. What we learned How to architect serverless applications for production deployment Advanced Next.js 16 features including App Router, Server Components, and async params Integrating AI APIs (Google Gemini) with custom prompts for domain-specific tasks Building real-time features with debouncing and performance optimization Working around platform constraints (no canvas/native deps on Vercel) AI Tools Disclosure We used a combination of self-programming, GitHub Co-Pilot with Claude 4.5 Sonnet, and Gemini to create this application. Team Naitik Gupta - Main Coder/BackEnd Gavyn Liu - UI Julain Juan - Deployment / Coding Leila Liu - Presentation RefineLab aims to become the definitive platform for academic writing improvement —combining AI-powered analysis, real-time feedback, structured lessons, and progress tracking to help students at all levels become confident, sophisticated writers. <div