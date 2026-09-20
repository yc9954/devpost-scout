---
slug: "cyberquestjr-ayzhc4"
url: "https://devpost.com/software/cyberquestjr-ayzhc4"
title: "CyberQuestJR"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 426
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/structured_db"
---

# CyberQuestJR

> CyberQuestJR is an interactive, story driven cyber safety lab that teaches kids how to stay safe online through text, missions, and rapid fire quizzes, all running 100% in the browser.

[Devpost](https://devpost.com/software/cyberquestjr-ayzhc4) · hackathon [[Student HackPad 2025]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[structured_db]]

**stack** lucideicons, react, reactrouter, tailwindcss, typescript, vite

## How they structured the write-up

- about the project
- inspiration
- how i built it
- what i learned
- challenges
- ai tools disclosure

## Body

Module Selection Page. Landing Page. Interactive Game Page. Content Page. About the Project I, Aarav, the sole member of team has made CyberQuestJR. CyberQuestJR grew out of a simple observation: most cyber safety material for kids either feels too technical or too boring. I wanted something that looked and behaved like the apps teens actually enjoy, while still teaching fundamental online safety skills. That idea slowly evolved into a fully story driven learning lab where each concept is taught through narrative scenes, detective style prompts, and several inline quizzes. Inspiration I have always been fascinated by how interactive interfaces shape understanding. When younger students told me they found typical cyber safety lessons hard to remember, I started sketching a comic styled format that could make concepts stick. The project became a way to combine my interest in front end development with real world digital safety. How I Built It CyberQuestJR is a pure frontend application that runs entirely in the browser. I structured the project around React 18 with TypeScript to keep components predictable and easy to scale. Tailwind CSS handled theming and neon accents, while React Router kept navigation light. All story text, missions, quizzes, and coach questions live in simple data files, and chapter progress is tracked through a small custom hook that writes to localStorage. The entire build is a static Vite bundle. It can be deployed to any CDN, which makes it easy for classrooms and parents to access without setup. What I Learned I learned how much design decisions influence comprehension. Crafting a readable neon theme took several iterations, especially ensuring high contrast without tiring the eyes. I also gained experience structuring multi chapter educational content as data rather than hardcoding components. Finally, building quiz interactions taught me to think about accessibility features, focus states, and keyboard navigation. Challenges The biggest challenge was finding a balance between aesthetics and clarity. Neon themes can become crowded quickly, so I had to strip away anything that distracted from the story. Another challenge was building quizzes that felt smooth and immediate while keeping everything local. Since I avoided backend services and database calls, the progress system had to be compact and reliable. Ensuring consistent state across pages using only localStorage required careful testing. AI Tools Disclosure I used Claude Sonnet 4.5 to help refine written explanations, improve clarity in technical descriptions, and review code structure for readability. All design, logic, story content, and implementation were created manually. AI assistance was limited to drafting and reviewing non critical text and summarizing documentation and comments. <div