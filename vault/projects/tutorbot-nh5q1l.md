---
slug: "tutorbot-nh5q1l"
url: "https://devpost.com/software/tutorbot-nh5q1l"
title: "TutorBot"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 444
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

# TutorBot

> Your AI-Powered Study Coach Instantly turn any topic into personalized lessons, quizzes, flashcards, and summaries to learn smarter and faster.

[Devpost](https://devpost.com/software/tutorbot-nh5q1l) · hackathon [[Code with Kiro Hackathon]]

## Facets

**domain** [[education]]
  <sub>weak: finance_payments, scientific_research</sub>
**user** [[educator_student]]
**substrate** [[document_pdf]]
  <sub>weak: geospatial, sensor_telemetry, structured_db</sub>

**stack** groqcloud, kiro, next.js-api-routes, pdf-lib, prismjs, react, tailwind, typescript

## Body

💡 Inspiration As AI tools become more powerful, most of the focus has been on chat-based help. We wanted to explore structured, personalized education – something that lets anyone learn a new topic like they had a tutor. Kiro's spec-driven AI development gave us the perfect base to turn that vision into a working product. 🤖 What It Does TutorBot is an AI-powered educational app that turns any topic into a full learning module. Here's what it generates from a single user input: 📚 Interactive Lessons with explanations and code samples 🧠 Quizzes with MCQs and short-answer questions 📇 Flip Flashcards for memorization 📄 PDF Summaries for printing or saving offline 🔄 Export Options: Flashcards to CSV, JSON, or Anki All content is created by AI using structured prompts and validated JSON. 🛠️ How We Built It Tech stack: Next.js 14 (frontend and backend) TypeScript for type safety and clean dev flow OpenAI GPT-3.5 Turbo for content generation pdf-lib for PDF creation PrismJS for syntax highlighting Tailwind CSS for responsive UI Kiro was core to development: .kiro/specs/ to define API contract early .kiro/hooks/ to automate unit test generation, PDF exporting, and flashcard formatting .kiro/steering/ to enforce dev best practices and prompt structure 🧱 Challenges We Ran Into Prompt formatting: Getting AI to return reliable, parseable JSON for lesson content took a lot of tuning. Token limits: Generating long-form content often hit GPT-3.5 limits, which we had to optimize for. Testing AI workflows: We needed consistent, testable logic despite GPT’s randomness. PDF layout: Making exported documents readable, responsive, and printable was more complex than expected. 🏆 Accomplishments We're Proud Of We shipped a production-ready, full-stack educational tool in a short amount of time. Seamlessly integrated multiple learning formats in one flow — lesson, quiz, flashcards, summary. Used Kiro specs and agent hooks to automate repetitive tasks like test writing and PDF creation. Designed a responsive and polished UI that works across devices. 📚 What We Learned How to design for AI from the start using structured specs and output validation. How Kiro can simplify test generation, response structure enforcement, and AI dev workflows. The power of combining UX with AI logic — the experience matters just as much as the output. Building with AI requires reproducibility, not just generation — and Kiro helped us do that. 🔮 What's Next for TutorBot User accounts for saving and reviewing progress Daily Study Plan Generator using AI Support for more media formats (videos, audio summaries) Topic difficulty levels Community-contributed topics and sharing Multilingual support We also want to explore more fine-tuning and educational metrics, turning TutorBot into a smart study coach for schools, bootcamps, and lifelong learners. <div