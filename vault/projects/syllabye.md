---
slug: "syllabye"
url: "https://devpost.com/software/syllabye"
title: "Syllabye"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 635
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/document_pdf"
---

# Syllabye

> Say bye to syllabus's. Say syllabye

[Devpost](https://devpost.com/software/syllabye) · hackathon [[Student HackPad 2025]]

## Facets

  <sub>weak: realtime_stream, vision_ocr</sub>
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[document_pdf]]

**stack** claude, codex, docling, expo.io, fastapi, groq, mongodb, ocr, openai, python, react-native, websockets

## How they structured the write-up

- 🎯 inspiration
- 📘 what it does
- 🛠️ how we built it
- 🚧 challenges we ran into
- 🏆 accomplishments we're proud of
- 📚 what we learned
- 🔮 what’s next for syllabye

## Body

AI chat with calendar/task/syllabus Calendar Month View Calendar Day View Todo List View Syllabus AI Summary page Syllabus viewer and editor Sign in 🎯 Inspiration College students are overwhelmed with PDFs, slides, and cluttered syllabi. We kept hearing the same frustrations: “I didn’t realize the midterm was this week .” “I have all the materials but no idea how to pace myself.” We wanted a tool that goes beyond storing course info—something that actually transforms it into a clear, manageable plan. That idea became Syllabye : an AI-powered platform that turns any syllabus into a structured, adaptive study roadmap. 📘 What It Does Syllabye helps students shift from overwhelmed to organized by turning course documents into actionable daily plans. Upload or link your syllabus Supports PDFs, pasted text, or manual entry for assignments and exam dates. AI-powered syllabus parsing Automatically detects deadlines, topics, readings, and assessments. Personalized study schedule Breaks the course into small, manageable tasks optimally distributed across your calendar. Progress tracking & reminders Know what’s due today, what needs attention, and what’s coming soon. Multi-course balancing Syllabye distributes workload across classes to prevent overload on any single day. 🛠️ How We Built It Frontend Built with Expo / React Native for a clean, cross-platform mobile experience. Designed a simple, low-friction UI that makes “what’s next” instantly clear. Backend Node/Express (or your actual backend) handles authentication, uploads, schedule logic, and task generation. PostgreSQL / Firebase (based on your setup) for data persistence. AI & Parsing Pipeline We used a combination of industry-leading AI tools to handle complex syllabus parsing and schedule generation: ChatGPT Models (OpenAI) Used for understanding syllabus structure, extracting assignments, identifying deadlines, and generating logical task breakdowns. Claude (Anthropic) Helpful for long-context syllabus parsing, summarization, and resolving ambiguous course instructions. Windsurf Used for AI-assisted coding, refactoring logic, and accelerating development across both frontend and backend codebases. OpenAI Codex Used for generating boilerplate, debugging snippets, and speeding up repetitive parts of the development process. - Github Copilot Used to make the pull requests and commit messages. By combining these tools, we built a pipeline that’s accurate, flexible, and capable of handling many different syllabus formats. Scheduling Logic Custom-built algorithm that turns course structures into daily tasks. Respects deadlines, pacing preferences, and personal constraints like study hours or off-days. Collaboration & Tools GitHub for version control and pull request workflows. Expo for rapid testing and iteration with hot reloading. 🚧 Challenges We Ran Into Real-world syllabus inconsistency Different formats, vague instructions, missing dates—no two syllabi look alike. Balancing automation with control Early versions gave too much control to AI, so we added more user editing tools. Task distribution conflicts Ensuring workload balance across multiple courses was non-trivial. Limited development time Building a full AI pipeline + app required ruthless prioritization. 🏆 Accomplishments We're Proud Of A fully functioning product Students can upload a syllabus and instantly receive a detailed, personalized study roadmap. Reliable automated parsing Our AI stack handles a surprising variety of formats with high accuracy. A smooth, stress-reducing user experience Turning “I don’t know where to start” into a guided, simple workflow. Strong collaboration Our team worked efficiently across design, AI, backend, and frontend. 📚 What We Learned AI is powerful, but UX makes or breaks adoption The model’s output is only as helpful as the interface that presents it. Real data uncovers the real problems Testing with real syllabi showed edge cases we never expected. Scope control = success Cutting features early allowed us to ship polished core functionality. Cross-platform considerations matter Expo accelerated development but required performance tuning. 🔮 What’s Next for Syllabye Calendar sync (Google, Apple, Outlook) AI-powered personalization that adapts based on user study habits Class collaboration tools for shared task lists and planning Professors/schools integration for ready-to-use syllabi Web and desktop versions to extend beyond mobile <div