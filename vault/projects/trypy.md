---
slug: "trypy"
url: "https://devpost.com/software/trypy"
title: "TryPy"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 346
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "user/educator_student"
---

# TryPy

> TryPy is a browser-based Python learning app that makes coding fun with lessons, quizzes, and in-browser code challenges—no setup needed.

[Devpost](https://devpost.com/software/trypy) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]] [[educator_student]]

**stack** monacoeditor, netlify, pyodide, react, tailwindcss, typescript

## How they structured the write-up

- 🧠 inspiration
- 💻 what it does
- 🔧 how we built it
- 😵 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📘 what we learned
- 🚀 what's next for trypy

## Body

🧠 Inspiration We wanted to make Python less intimidating and more like a game. Too often, beginners are overwhelmed by setup, abstract theory, or dry tutorials. TryPy was born from one simple idea: What if learning Python felt like leveling up in a game instead of reading an encyclopedia? 💻 What it does TryPy is a browser-based Python learning platform designed to take absolute beginners from "What’s a variable?" to solving AtCoder ABC problems. Each course includes: Bite-sized explanations Quick quizzes Interactive coding practice with real-time feedback We rate your code (⭐️ 1–5) based on correctness and code length — just for fun. 🔧 How we built it Frontend : React + TypeScript + TailwindCSS (Neo Brutalist vibes for a bold learning feel) Code Editor : Monaco Editor with autocomplete and syntax highlighting Execution : Pyodide for secure, client-side Python execution Deployment : Netlify (one-click, zero tears) 😵 Challenges we ran into Matching user-submitted code outputs reliably without enabling cheating or false positives. Running Python entirely in-browser while keeping performance snappy. Designing a UI that’s both beginner-friendly and developer-respectful. Preventing Monaco Editor from auto-completing everything into chaos. (We love you, Monaco, but chill.) 🏆 Accomplishments that we're proud of 5 structured courses (3 basic + 2 advanced), carefully scaffolded to bridge theory and practice. Fun, minimal UI that feels more like a creative space than a coding bootcamp. Python execution inside the browser with no servers or installation — magic! 📘 What we learned Teaching Python is easy. Teaching it well — interactively, enjoyably, and accessibly — is a different beast. Writing a coding challenge grader that’s fair, fast, and fun is a design challenge in itself. Neo Brutalism is somehow perfect for education: bold, clear, unignorable. 🚀 What's next for TryPy Add leaderboards and XP to make learning more competitive AI-based code feedback and hints Public code challenges with live multiplayer coding duels Export progress to GitHub as proof of learning Expand into other languages (JavaScript, Go... maybe even Rust if we're brave) 🐍 TryPy — The only snake you’ll ever want to debug. <div