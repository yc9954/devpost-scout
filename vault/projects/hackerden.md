---
slug: "hackerden"
url: "https://devpost.com/software/hackerden"
title: "HackerDen"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 754
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# HackerDen

> What do hackers want? Like all craftsmen, hackers like good tools. Good hackers find it unbearable to use bad tools. They'll simply refuse to work on projects with the wrong infrastructure.

[Devpost](https://devpost.com/software/hackerden) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]] [[legal_professional]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[video_visual]] [[web_dom]]

**stack** appwrite, canvasapi, gemini, kiro, netlify, oauth, radix/ui, react, shadcn/ui, tailwind, vite, websockets

## How they structured the write-up

- inspiration
- what it does
- development journey and challenges i ran into
- accomplishments that i'm proud of
- what’s next for hackerden

## Body

Landing Page Login/Signup Page User Console Team Dashboard Kanban Board Team Chat Shared Document Team Vault - Files Team Vault - Secrets Whiteboard Team Submission Page Submission page for Judges Inspiration I was inspired by a quote from Paul Graham "What do hackers want? Like all craftsmen, hackers like good tools. In fact, that's an understatement. Good hackers find it unbearable to use bad tools. They'll simply refuse to work on projects with the wrong infrastructure." After participating in several hackathons, I noticed a major frustration: teams were constantly switching between tools. Someone would message in Slack, then we'd jump to Trello for tasks, then Google Docs for planning, then Discord for voice chat. All this context switching was killing our momentum and breaking that crucial flow state you need to build something amazing in 24-48 hours. That's when I realized: what if there was one platform that did it all? HackerDen was born from this simple idea—to keep hackathon teams in their flow by giving them everything they need in one place. What it does HackerDen is basically your hackathon team's command centre. Instead of juggling five different apps, everything happens in a single, unified workspace. Your Hackathon HQ: A clean dashboard shows all your hackathons—what's happening now, what's coming up, and what you've already crushed. Team Formation Made Simple: You can create a team and get a 6-character code to share. Task Management: A Kanban board with drag-and-drop functionality that updates in real-time. When someone moves a task, everyone sees it instantly. Chat That Keeps You Connected: The real-time team chat uses automatic notifications when tasks are created or completed. File Sharing Without the Hassle: You can upload images, documents, and code files (up to 10MB) Collaborative Whiteboard: Brainstorm and plan with your team on a real-time drawing canvas. Judge-Ready Submissions: Build your submission page as you go, and when judging starts, you get a public URL that judges can access without needing to log in. Team Vault: Store API keys and other sensitive information securely with proper access controls. Dark Mode That Doesn't Hurt Your Eyes: The entire platform is built with a clean, professional dark theme for those late-night coding sessions. Development Journey and Challenges I ran Into Overcoming Development Friction: Services kept trying to import each other in circles, resulting in a messy early codebase. I solved this by implementing a BaseService architecture with dependency injection patterns and dynamic imports. This breakthrough taught me that a clean service layer is crucial for a scalable and maintainable codebase. Learning to Work with Kiro: Initially, communicating with Kiro was a significant challenge, and I had to restart the project multiple times. However, by working with Gemini, I learned to refine my prompts, which made the development process much smoother. This experience taught me that effective communication with an AI model is a skill in itself. Creating a Modern User Experience: I realised that hackathon UX is different. Teams need features like simple join codes, role-based permissions, and clear progress visualisation. I learned that small details can make a huge difference in team coordination. I built HackerDen with a modern stack, including React 19, Vite 7.0, and shadcn/ui, which helped me create a fluid, professional, and intuitive experience. Real-World Validation: I am proud to announce that students in my college are already using HackerDen for the SIH (Smart India Hackathon 2025). One team even used our platform for a national-level ODOO hackathon. This real-world usage proves that our solution addresses a genuine pain point in the hackathon community. Accomplishments that I'm proud of Real-Time That Actually Works: The WebSocket-based subscriptions ensure that when someone moves a task or sends a message, everyone sees it instantly. Complete Hackathon Journey: From signing up to final submission, everything flows naturally. This includes secure OAuth authentication, easy team formation with join codes, real-time collaboration, and judge-ready submissions with public URLs. Judge-Friendly Submissions: Teams can build their submission as they go and get a public URL when judging starts, eliminating last-minute panic with auto-aggregated project data. What’s Next for HackerDen HackerDen’s mission is simple: eliminate every bit of hackathon friction. We’re building towards: An AI teammate: like a digital H.E.R.B.I.E., handling docs, reminders, and repetitive tasks. Deep integrations: GitHub, GitLab, Vercel, Slack, Discord—HackerDen connects where hackers already live. Judging reimagined: real-time analytics, rubric scoring, embedded live demos. Organiser power tools: multi-event management, enterprise support, global timezone sync. And beyond hackathons, HackerDen grows into the go-to tool for any short-lived, high-energy project—from college fests to startup sprints. <div