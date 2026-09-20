---
slug: "notebot-6xj542"
url: "https://devpost.com/software/notebot-6xj542"
title: "Notebot"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 493
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/structured_db"
---

# Notebot

> The ultimate student OS built for hackathon. AI-powered summaries & quizzes. Quick Connect: Temporary, no-login group chat for study sessions. Library for saving and reviewing notes.

[Devpost](https://devpost.com/software/notebot-6xj542) · hackathon [[Student HackPad 2025]]

## Facets

**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]] [[researcher]]
**substrate** [[structured_db]]
  <sub>weak: code_repository, transcript_audio</sub>

**stack** mern, socket.io

## How they structured the write-up

- 🧠 ai tools disclosure
- 🧑‍💻 team members

## Body

Landing Page 🤖 NoteBot: The AI-Powered Student OS NoteBot is a cohesive, two-part application suite built to tackle the biggest pain points in student life: information overload and collaboration friction. Built entirely during the 48-hour "Student Hackpad" hackathon, NoteBot provides robust, smart tools that truly make student life better. What We Built: NoteBot (AI Learning Engine): The core platform where students upload or paste lecture notes, dense textbook passages, or raw class transcripts. Using the Gemini API, NoteBot instantly processes this raw data and generates two crucial study tools: Proportional Summaries: Detailed, bulleted summaries that automatically scale in length based on the size of the input text, preventing key details from being lost in short outputs. Custom Quizzes: Unique practice questions generated directly from the content to facilitate active recall and test comprehension. Knowledge Vault: A secure, personalized library where students can log in and save their generated study sessions for long-term review. Quick Connect (Ephemeral Chat): A zero-friction communication tool designed for temporary study groups. It allows any student to instantly create a room with a shareable link without needing to log in or sign up. These rooms are designed to expire, minimizing the digital clutter and commitment associated with standard communication apps. Why It Matters (Impact & Innovation): Student life is often defined by frantic studying and disjointed communication. NoteBot provides a single platform to solve both: Impact: We directly address the inefficiency of manual note-taking and the isolation of studying. By making summaries instant and collaboration effortless, we save students dozens of hours over a semester, contributing directly to better time management and mental well-being. Innovation: We achieved sophisticated integration between transient communication and permanent learning. When a user shares a NoteBot session link into a Quick Connect chat, the app renders a rich, contextual preview , allowing students to discuss the content rather than spending time copying and pasting it. This demonstrates a seamless data flow, transforming the two apps into a single, cohesive Student OS. The futuristic, low-light "Neo-Academic" design ensures maximum focus, making NoteBot a complete, ready-to-use solution that elevates the student study experience. 🧠 AI Tools Disclosure We extensively leveraged three different large language models (LLMs) to maximize efficiency and achieve complex functionality during the limited hackathon timeline. Tool Purpose How It Was Used Gemini 2.5 Flash API Core Product Functionality Used directly within the backend code to execute complex tasks: 1) Generating detailed, length-proportional summaries, and 2) Creating contextual quiz questions from raw input text. Claude AI Frontend Design & Component Scaffolding Used as an advanced assistant to generate detailed, futuristic CSS and component structures based on specific thematic and layout descriptions (e.g., the "Neo-Academic" split-pane editor and the color palette). ChatGPT Backend Utility & Code Debugging Used for rapidly generating boilerplate code for non-core features (e.g., initial Express server setup, database models for the Library) and for quick debugging of authentication logic and API call structures. 🧑‍💻 Team Members Solo Developer: [Muhammad Rohan] <div