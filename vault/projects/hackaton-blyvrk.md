---
slug: "hackaton-blyvrk"
url: "https://devpost.com/software/hackaton-blyvrk"
title: "FocusHub"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 837
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/document_pdf"
---

# FocusHub

> All your study tools. None of the distractions.

[Devpost](https://devpost.com/software/hackaton-blyvrk) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[education]] [[labor_employment]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[document_pdf]]
  <sub>weak: web_dom</sub>

**stack** claude, css, groq, html, javascript, perplexity, vscode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for focushub
- contributors

## Body

Task dashboard Music Player Ai Assistant Browser Notes Whiteboard Focus hub Inspiration FocusHub emerged from our need for a unified study workspace. We noticed students juggling multiple disconnected tools—note apps, timers, music players—losing focus switching between them. As a three-person team, we envisioned a platform that seamlessly integrated AI assistance , music, and resource creation into one cohesive environment. We wanted to eliminate context-switching overhead and help students build sustainable focus habits. Our inspiration came from understanding that deep work requires both external structure and internal motivation. We aimed to create a study companion that adapts to individual workflows, making learning less fragmented and more rewarding. FocusHub represents our commitment to supporting focused, intentional study sessions. What it Does FocusHub is a task-centric web application designed for focused study sessions. Users create timed tasks and enter dedicated workspaces equipped with integrated tools: a rich note editor with PDF import/export, a digital whiteboard for visual thinking, and an embedded browser for research. Each task workspace includes a customizable Pomodoro timer, music player for ambiance, and an AI-powered study assistant . The platform supports real-time formatting, citations, diagram creation, and PDF document management. Users track daily study goals with visual progress tracking and session statistics. The music module provides curated playlists through open embeds. All features maintain task isolation—notes and diagrams save per-task for organized workflow management and distraction-free focus. How We Built It We developed FocusHub using responsive front-end architecture with robust client-side state management to deliver a fluid, multi-module experience. The music player uses direct YouTube and Spotify link embeds—no external music APIs since platforms restrict third-party access through commercial agreements. Our single external API is the Groq Mixtral model powering our AI study assistant, requiring sophisticated conversation history management. The note editor, PDF handler, and all text processing work entirely client-side using PDF.js for file parsing. The digital whiteboard uses HTML5 canvas with pencil, eraser, and shape tools. We implemented task-specific countdowns with state transitions between work and break phases, managing pause/resume functionality and precise calculations. User authentication and task persistence use client-side memory storage. Navigation features include the logo button always returning to the dashboard. All processing remains local, ensuring data privacy and offline capability. We used Perplxity to help us plan the idea and Claude Haiku 4.5 to built in VsCode chat to help us code. Challenges we ran into Implementing reliable AI conversations within our app proved significantly harder than expected. We struggled maintaining context coherence, handling edge cases, and ensuring responses stayed relevant to study topics. The note module's PDF integration demanded expertise with file parsing, browser compatibility, and cross-format conversion—exporting rich-text to PDF while preserving formatting required multiple iterations. Browser limitations imposed by private companies severely restricted our vision. Search engines and content providers enforce strict embargoes on embedded access, forcing us to simulate browser results rather than display real data. The whiteboard module's canvas state synchronization and drawing performance optimization consumed substantial development time. Managing data isolation across tasks while maintaining seamless module switching required architectural refinement. Accomplishments that we're proud of We successfully integrated seven distinct modules into a cohesive, single-workspace environment. Our note editor uniquely combines rich formatting, citations from research, diagram embedding, and dual-format export (TXT and PDF). The AI assistant seamlessly contextualizes study queries within active tasks. We implemented a functional Pomodoro timer with customizable rounds and break periods. The digital whiteboard supports multiple drawing tools, color selection, and persistent diagram storage. Throughout development, we maintained a clean, intuitive interface that works across themes and device sizes. We prioritized data privacy by keeping all processing local. Most significantly, we proved that three developers could build a comprehensive productivity platform addressing real student pain points. What we learned Collaborative development under technical constraints taught us invaluable lessons about problem-solving and creative adaptation. We gained deep expertise in browser APIs, particularly File handling, Canvas manipulation, and local storage optimization. Integrating third-party AI required understanding API limitations and designing robust error handling. We learned the realities of platform restrictions—why major companies protect their ecosystems—and how to work within those boundaries. Building complex state management across multiple modules improved our architecture understanding. We discovered that user experience consistency matters more than feature quantity. The project reinforced the importance of clear communication within small teams and pragmatic prioritization. We now appreciate why scalable systems require thoughtful data structures from inception. What's next for FocusHub Our roadmap includes cloud synchronization enabling task persistence across devices and user accounts. We plan collaborative study spaces where teams tackle projects together with shared notes and real-time whiteboard updates. Advanced analytics will track focus patterns, identify productivity trends, and suggest personalized study schedules. Enhanced AI integration will provide adaptive study plans and intelligent resource recommendations. We're exploring expansions to the music module and third-party tool integrations. Community features—shared study templates, difficulty ratings, and peer recommendations—will foster engagement. Long-term, FocusHub aims to become the ecosystem for building sustainable focus habits, supporting students and professionals seeking meaningful, distraction-free learning environments. Contributors Jorge Córdova Israel Alcántara Carlos Bernaus <div