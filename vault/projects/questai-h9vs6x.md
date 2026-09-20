---
slug: "questai-h9vs6x"
url: "https://devpost.com/software/questai-h9vs6x"
title: "QuestAI"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 869
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# QuestAI

> High school is tough, but QuestAI makes it a game. It’s the AI planner that schedules your passions first and breaks goals into daily levels, so you can ace your classes and keep your life.

[Devpost](https://devpost.com/software/questai-h9vs6x) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[geospatial]] [[sensor_telemetry]]
  <sub>weak: web_dom</sub>

**stack** css, google-cloud, google-gemini-api, html, javascript, node.js, react, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for questai

## Body

Login Screen Loading Screen Task Description Screen Task Report Task Journey Example Inspiration I finished my homework by 7pm. Then I spent three hours scrolling because nothing told me what to do next. By Friday I felt like I'd done nothing that week except study and scroll. That was me, sophomore year. I had big goals, like extracurriculars, college prep, things I actually cared about, but absolutely no system to hold them together. I tried todo lists, calendars, every productivity app I could find. None of them worked. Not because I was lazy, but because they were all built for people who already knew how to manage their time. They organized tasks, but didn't create motion. The real enemy wasn't my schedule. It was friction , the paralyzing feeling right before you start. I didn't need a pusher, I needed something that made it easier to push myself. 1 in 3 high schoolers feel overwhelmed balancing academics and personal life. The #1 reason students quit extracurriculars isn't loss of interest; it's academic pressure. And 73% abandon productivity apps within the first week. I built QuestAI because I was all three of those statistics, and I didn't want to be. What it does QuestAI is an AI-powered planning app that treats your week as a journey to complete, not a backlog to clear. You tell Quest your goals and tasks for the week, then AI breaks them into daily levels : 20–30 minute, fully-described sessions you can tap through without ever deciding what to do next. "Study for AP Calc" becomes four levels: review derivatives, practice integration, work through past problems, review mistakes. // AI task decomposition — turning vague goals into completable levels const levels = await decomposeTask({ task: "Write history essay", available_minutes: 120, context: { student_grade: 10, subject: "AP US History" } }); // → ["Outline thesis and 3 arguments (25 min)", // "Draft introduction and body paragraph 1 (30 min)", // "Body paragraphs 2 & 3 (30 min)", // "Conclusion + first edit pass (25 min)"] ` ` ` How we built it QuestAI is a full-stack web application built with modern JavaScript tooling and a deliberate AI architecture. Frontend : React + Vite for fast builds and a smooth, level-based UI Backend : Node.js with a TypeScript server (server.ts) handling API routing, AI orchestration, and output validation AI Layer : Google Gemini API for two specific jobs, weekly plan generation and task decomposition. Everything else (streak tracking, level completion, leaderboard logic, mascot state) is deterministic code. Hosting : Deployed on Google Cloud The AI drafts the plan. The backend enforces it. The student just taps through their day. Challenges we ran into Connecting the Gemini API was the steepest learning curve. Getting the API correctly wired into the Node.js backend produced a cascade of errors — CORS issues, malformed request bodies, authentication failures — all of which had to be debugged from first principles with no prior API experience. Prompt engineering for personalization was the second major challenge. Early versions of the AI returned nearly identical journey breakdowns regardless of what the student inputted. Solving this required redesigning the prompt structure to inject specific user context — goal type, time available, subject — so the model couldn't fall back on generic output. The difference between a prompt that produces one generic plan and one that produces a genuinely tailored journey is subtle, and finding it took real iteration.Connecting the Gemini API was the steepest learning curve. Getting the API correctly wired into the Node.js backend produced a cascade of errors — CORS issues, malformed request bodies, authentication failures — all of which had to be debugged from first principles with no prior API experience. Accomplishments that we're proud of Shipped a working AI-powered web app: my first time ever integrating a live AI API into a production project, end to end Solved a problem I actually lived: Quest isn't a hypothetical. It's the tool I needed sophomore year and didn't have Built a complete full-stack product solo: React UI → TypeScript backend → Gemini API integration → Google Cloud deployment Designed an AI architecture that uses the model only where language understanding genuinely matters, and deterministic code everywhere else What we learned How to integrate AI APIs into a real application: authentication, request shaping, response parsing, error handling Prompt engineering: how small changes to instructions dramatically shift AI output quality and specificity UI/UX principles: what makes an interface feel motivating versus overwhelming, and why the Duolingo journey format works psychologically Full-stack development workflow from local build to cloud deployment How to architect an app so AI is a specialist tool, not a dependency for things code handles better What's next for QuestAI Calendar sync: integrate with Google Calendar to automatically block time for each journey level, so the plan lives in the student's real week Todo list integration: connect with Notion, Todoist, or Google Tasks so Quest fits into workflows students already use Higher-quality AI models: upgrade to more powerful Gemini models for richer task decomposition and smarter weekly plan generation Social accountability: let students see each other's journey progress, turning "what are you working on" into a shared metric instead of a vague check-in <div