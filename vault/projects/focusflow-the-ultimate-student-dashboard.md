---
slug: "focusflow-the-ultimate-student-dashboard"
url: "https://devpost.com/software/focusflow-the-ultimate-student-dashboard"
title: "FocusFlow: The Ultimate Student Dashboard"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 714
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/web_dom"
---

# FocusFlow: The Ultimate Student Dashboard

> FocusFlow: The all-in-one student productivity dashboard. Manage tasks with kanban boards, smart calendars, study analytics, flashcards, and a music player. Powered by FastAPI for cloud data sync.

[Devpost](https://devpost.com/software/focusflow-the-ultimate-student-dashboard) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[web_dom]]

**stack** fastapi, html5, inter-font, javascript-(es6+), latex, markdown, tailwind-css

## How they structured the write-up

- 🌟 inspiration
- 🚀 what it does
- 🛠️ how we built it
- 🏃 challenges we ran into
- 🏆 accomplishments that we're proud of
- 🧠 what we learned
- 🗺️ what's next for focusflow

## Body

Main page of FocusFlow Flashcard Section Example Productivity Section (Pomodoro) Task Section Example Music Section Grade Tracker Section Profile Section FocusFlow: The Ultimate Student Dashboard A single, unified productivity app to organize your entire semester. 🌟 Inspiration Every semester, students juggle deadlines, notes, grades, and resources across half a dozen apps and platforms. I wanted a single unified tool that would not only organize this chaos but also actively motivate—integrating analytics and streak-based achievements into the everyday workflow. 🚀 What it does FocusFlow is a unified productivity dashboard for students. It delivers all key features in a single, fast-loading page: Task Management: Organize tasks in three distinct layouts: a drag-and-drop Kanban Board , a full-page Calendar , or a dense, sortable List View . Study Analytics: Track your Pomodoro sessions with a custom-built bar chart. A Study Streak tracker and Achievement system motivate you to stay consistent. Flashcard Decks: Create and study your own flashcard decks, complete with an answer-checking study mode. Grade Tracker: A simple, powerful calculator to track assignments and weighted grades by course. Persistent Music Player: Upload your favorite study music, which persists between sessions, and control playback while you work. Calm UI: A beautiful, responsive interface with full Light and Dark Mode support. All data is instantly persistent , saving every change directly to a dedicated backend. 🛠️ How we built it Frontend: Built as a single index.html file using Vanilla JavaScript (ES6+) for all logic. The UI is crafted with Tailwind CSS for a responsive, modern component-based design. Backend: A lightweight FastAPI (Python) server handles all persistence. It serves the index.html file and provides API endpoints for saving and loading data. Data Persistence: All app state (tasks, grades, goals, etc.) is serialized and sent to the backend via fetch API calls , where it's stored in a single data.json file. This provides a single source of truth and ensures all progress is saved. Music Player: The music player uploads audio files directly to the FastAPI backend , which stores them in a /music/ directory. The player then streams the audio from those file URLs, ensuring the playlist is always available. Analytics: The study analytics chart is built from scratch with zero dependencies , using only styled div elements to render a dynamic bar chart. 🏃 Challenges we ran into Client-Server Architecture: The biggest challenge was moving from a simple (and failing) localStorage / IndexedDB model to a robust client-server architecture. This involved refactoring every save/load function to be an async fetch call. CORS & URL Resolution: Debugging a host of network errors, including net::ERR_FAILED (from CORS), 400 Bad Request (from faulty security logic), and 501 Not Implemented (from a missing python-multipart library). Data & Path Mismatches: We had to squash several subtle bugs, including a time zone mismatch (UTC vs. Local time) that made the analytics chart fail to update, and a file path mismatch (relative vs. absolute) that broke the "delete music" security check. UI "Leak" Bugs: Patched subtle issues where modules could overlap or fail to hide properly during rapid navigation between tabs. 🏆 Accomplishments that we're proud of Completely refactored the app for bulletproof persistence . All data now correctly saves to and loads from the backend. Built a true “all-in-one” dashboard that remains lightweight and fast (a single HTML file + a simple Python server). Created a beautiful, responsive UI supporting both light and dark themes . Integrated achievement popups (toasts) and a motivator section that dynamically responds to the user's study streak. Successfully debugged complex, full-stack issues spanning from frontend JavaScript, to network policies (CORS), to backend Python logic. 🧠 What we learned We learned the critical importance of a single source of truth for data. Debugging this project taught us how a single "frontend" error can actually be a backend security rule, a network policy, or a data serialization mismatch. We also learned how to build a complex, reactive-style app in vanilla JavaScript and how flexible FastAPI is for rapid backend development. 🗺️ What's next for FocusFlow Real-time collaboration with classmates for shared boards and messaging. AI-powered assignment reminders and study recommendations. Integration with learning management systems (LMS). Cross-platform mobile apps using React Native or Flutter. More advanced analytics and gamification features. Integrating an LLM for making flashcards and a chatbot assistant. <div