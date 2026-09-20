---
slug: "sylly"
url: "https://devpost.com/software/sylly"
title: "Sylly"
hackathon: "ShellHacks 2025"
organization: "init"
winner: true
words: 476
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/document_pdf"
---

# Sylly

> Sylly is a smart academic organizer that centralizes courses, assignments, and syllabi, making it easy to upload, share, search, and download materials in one place.

[Devpost](https://devpost.com/software/sylly) · hackathon [[ShellHacks 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[document_pdf]]

**stack** auth0, node.js, prisma, react, vite

## How they structured the write-up

- 🌟 inspiration
- 📌 what it does
- 🛠️ how we built it
- ⚡ challenges we ran into
- 🏆 accomplishments that we're proud of
- what we learned
- what's next for sylly

## Body

Dashboard My Syllabi Planner Chat Shared Syllabi 📖 About the Project 🌟 Inspiration The inspiration for Sylly came from the struggle that students face when juggling multiple courses, syllabi, and deadlines across different platforms. We wanted to build a centralized workspace where all academic tasks could live together — making it easier to plan, stay on track, and succeed. 📌 What it does Sylly is a student-focused academic planner that allows users to: Upload and store syllabi 📄 Automatically extract and organize assignments and due dates ⏳ Preview syllabi PDFs side-by-side with extracted information 👀 Manage all their courses and deadlines in one place 📚 Securely log in with Auth0 🔑 The goal is to help students reduce stress and focus on learning rather than administrative tasks. 🛠️ How we built it We built Sylly with a modern web stack : Frontend: React + TypeScript (Vite for bundling) UI: Bootstrap and custom CSS for responsive design Auth: Auth0 for login/logout and token management State management: React Context API for handling courses and assignments File handling: File upload & preview for syllabi PDFs The app is designed with scalability in mind, so new features (like calendar sync) can be added easily. ⚡ Challenges we ran into Every project comes with hurdles. Some of ours included: Getting the navbar to be responsive while maintaining a full-width layout Handling PDF preview rendering consistently across browsers Debugging authentication flows with Auth0 tokens Managing state synchronization when adding courses and assignments Balancing feature scope with the time constraints of a hackathon 🏆 Accomplishments that we're proud of We’re proud that we were able to: Create a clean, intuitive user interface that feels natural to use Successfully integrate Auth0 authentication Build a PDF viewer that displays syllabi alongside extracted data Develop a working course/assignment management system in a short timeframe Collaborate effectively as a team under time pressure What we learned This project helped us grow in several areas: Structuring a React + TypeScript project for long-term maintainability Using React Context to share state across complex components Leveraging Bootstrap’s responsive utilities while still customizing styles Improving debugging skills for async flows and UI rendering The importance of clear planning and teamwork in hackathons What's next for Sylly Collaboration tools — group planning for projects and study sessions Analytics dashboard — track progress, deadlines, and workload trends over the semester Smart reminders — personalized notifications before due dates or study sessions Cross-platform sync — seamless experience across web, mobile, and tablet Resource hub — attach lecture slides, readings, or notes directly to each syllabus item Instructor integration — professors can share official syllabi and updates in real time Focus mode — distraction-free study view with timers and task tracking Multilingual support — making Sylly accessible for international students Sylly helps students stay on top of their academics, one syllabus at a time. <div