---
slug: "stemate"
url: "https://devpost.com/software/stemate"
title: "STEMate"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 384
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# STEMate

> Your AI tutor for every STEM subject, every grade, every doubt.

[Devpost](https://devpost.com/software/stemate) · hackathon [[DSH Hacks V1]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]]

**stack** axios, bcrypt, css3, express.js, groq, javascript, llama-3.3, mongodb, mongoose, node.js, react-markdown, react-router, react.js

## How they structured the write-up

- 💡 inspiration
- 🔨 how i built it
- 📚 what i learned
- 🚧 challenges i faced
- 🎯 what's next

## Body

Landing page 1 Landing page 2 Landing page 3 signup login dashboard AI tutor AI tutor 2 Quiz generator Doubt solver doubt solver2 Roadmap Chat history light mode dashboard light mode landing page light mode landing page 2 light mode landing page 3 💡 Inspiration As a CSE student, I've seen many of my classmates struggle with STEM subjects — not because they aren't smart, but because they don't have access to personalized help. Textbooks are boring, YouTube videos are generic, and private tutors are expensive. I wanted to build something that gives every student their own AI tutor — one that understands their grade level and answers their specific doubts. 🔨 How I Built It STEMate is a full stack MERN application: Frontend — Built with React.js, using React Router for navigation and Axios for API calls. I used React Markdown to render AI responses beautifully. Backend — Node.js and Express.js handle all API routes for authentication and AI features. Database — MongoDB with Mongoose stores user accounts and chat history. AI — Groq API with LLaMA 3.3 70B model powers all AI features including topic explanations, quiz generation, doubt solving and study roadmaps. Auth — bcrypt for secure password hashing. The app has two servers running simultaneously — React on port 3000 and Express on port 5000, communicating via REST APIs. 📚 What I Learned Building a complete MERN stack application from scratch Integrating AI APIs into a real web application Managing state in React with useState and useEffect Designing grade-adaptive AI prompts for different student levels Handling full conversation history for multi-turn AI chat 🚧 Challenges I Faced AI response formatting — Getting the AI to return clean, well-structured responses took careful prompt engineering. I used React Markdown to render the responses properly. Grade-based prompting — Making the AI truly adapt its explanation style for a 6th grader vs a 12th grader required fine-tuning the prompts. Chat history — Implementing save and delete functionality while keeping the conversation context intact was tricky but rewarding. Dark/Light mode — Making all components respect the theme using CSS variables across the entire app took careful planning. 🎯 What's Next Mobile app version Support for more subjects beyond STEM Teacher dashboard to assign topics to students Offline mode for students with limited internet access <div