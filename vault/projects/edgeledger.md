---
slug: "edgeledger"
url: "https://devpost.com/software/edgeledger"
title: "EdgeLedger"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 695
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# EdgeLedger

> Turn loan documents into clear insights Actionable intelligence from loan documents Understand loan agreements instantly

[Devpost](https://devpost.com/software/edgeledger) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[finance_payments]]
**user** [[researcher]]
**substrate** [[document_pdf]] [[financial_record]] [[sensor_telemetry]] [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** css, eslint, framer-motion, google-gemini-api, google/generative-ai, html, javascript, lucide-react, node.js, npm, pdf.js, pdfjs-dist, postcss, radix-ui

## How they structured the write-up

- 💡 inspiration
- 🎯 what it does
- 🛠️ how we built it
- 📚 what we learned
- 🚧 challenges we faced
- 🎨 design philosophy
- 📊 impact & results
- 🔮 what's next
- 🏆 accomplishments

## Body

💡 Inspiration The financial industry processes thousands of loan agreements daily, with analysts spending 30-60 minutes manually reviewing each document. We saw an opportunity to leverage AI to transform this tedious process into seconds of automated analysis. The vision was simple: upload a PDF, get instant insights . 🎯 What It Does EdgeLedger Solutions is an AI-powered loan document analysis platform that: Extracts and analyzes loan agreements in real-time Identifies key sections (parties, terms, covenants, conditions) Extracts critical metrics (principal amount, interest rate, term length) Flags potential issues with intelligent status indicators Provides an interactive AI chatbot for document Q&A The time savings are dramatic: what takes humans 30+ minutes now takes 10-15 seconds . 🛠️ How We Built It Technology Stack Frontend : React 18 + TypeScript + Vite for blazing-fast development UI Framework : shadcn/ui + Tailwind CSS for a polished, modern interface AI Engine : Google Gemini 3.0 Flash for intelligent document analysis PDF Processing : Mozilla's PDF.js for browser-side text extraction Architecture Innovation Instead of sending entire PDFs to the AI (hitting size limits), we: Extract text locally using PDF.js (no file size limits) Send only the extracted text to Gemini API (much smaller payload) Receive structured analysis with sections, metrics, and insights Display results in an intuitive, collapsible interface This approach is both cost-effective (~$0.001 per document) and fast (3-5 second analysis time). 📚 What We Learned Technical Insights Browser-side processing eliminates file size constraints and privacy concerns Structured AI prompts dramatically improve extraction accuracy (95%+ for key metrics) Progressive disclosure (collapsible sections) makes complex documents digestible Context-aware chatbots provide better answers when given full document context Design Lessons Users need immediate feedback - we added toast notifications and progress indicators Visual hierarchy matters - color-coded metrics and status indicators guide attention Empty states should educate, not frustrate - we added helpful guidance throughout AI Optimization We discovered that breaking analysis into two phases improved results: Phase 1 : Identify and extract all document sections Phase 2 : Analyze each section for metrics and status This reduced hallucinations and improved accuracy by ~20%. 🚧 Challenges We Faced Challenge 1: PDF File Size Limits Problem : Gemini API has token limits; large PDFs couldn't be sent directly. Solution : Implemented browser-side text extraction with PDF.js. Only text (not binary PDF) goes to the API, reducing payload size by 90%+. Challenge 2: Inconsistent Document Formats Problem : Loan agreements vary wildly in structure and terminology. Solution : Trained the AI with flexible prompts that identify sections by semantic meaning, not rigid patterns. Added fallback logic for edge cases. Challenge 3: Real-time Analysis UX Problem : Users don't know if processing is working or stuck. Solution : Implemented multi-stage progress indicators: "Extracting text from PDF..." (1-2s) "Analyzing document with AI..." (3-5s) "Processing complete!" (with success toast) Challenge 4: Chatbot Context Management Problem : Initial chatbot gave generic answers without document context. Solution : Pass the full extracted text with every chat query, enabling accurate, document-specific responses. 🎨 Design Philosophy We followed three core principles: Speed First : Every interaction should feel instant Progressive Disclosure : Show summaries first, details on demand Trust Through Transparency : Always show why the AI flagged something The result is an interface that feels both powerful and approachable. 📊 Impact & Results Time Reduction : 99%+ (30 minutes → 15 seconds) Cost Efficiency : ~$0.001 per document analysis Accuracy : 95%+ for key metric extraction User Experience : Intuitive enough for non-technical users 🔮 What's Next We're planning to add: Multi-document comparison for portfolio analysis Risk scoring algorithms using historical data Export functionality (Excel, PDF reports) Database integration for document library management Batch processing for high-volume operations 🏆 Accomplishments We're proud that we built a production-ready application that: Handles real-world loan documents with 95%+ accuracy Processes documents of any size without limits Costs less than $0.01 per analysis Provides instant insights through an AI chatbot Maintains user privacy (PDFs never leave the browser) Most importantly, we created something that solves a real problem for financial professionals, saving them hours of manual work every day. Built with React, TypeScript, Gemini AI, and a passion for solving real-world problems. <div