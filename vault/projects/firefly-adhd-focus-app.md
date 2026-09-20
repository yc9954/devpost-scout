---
slug: "firefly-adhd-focus-app"
url: "https://devpost.com/software/firefly-adhd-focus-app"
title: "Firefly - ADHD focus app"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 469
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "substrate/structured_db"
---

# Firefly - ADHD focus app

> Firefly helps ADHD users overcome task paralysis by turning goals into 60-second starter steps with AI guidance and a big visual timer, so they can start meaningful work in seconds.

[Devpost](https://devpost.com/software/firefly-adhd-focus-app) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[accessibility]] [[developer_tools]]
**substrate** [[structured_db]]

**stack** bun, google-gemini-ai-api, next.js, postgresql, react, supabase, tailwind-css, typescript, vitest

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that we're proud of
- what i learned
- what's next for firefly - adhd focus app

## Body

logo capture the goals Inspiration Firefly started with my own struggles. Living with ADHD means I often freeze when I see a big task. Either I overestimate how much effort it will take, or I underestimate the time and end up frustrated. That cycle leads straight to procrastination and guilt. I tried a bunch of productivity apps. Some were decent, but most either locked key features like sync and stats behind a paywall or didn’t really help me with the core problem. I didn’t need another checklist. I needed something that could help me start, right now, with one small step. That idea became Firefly. What it does Firefly is a web app designed to help people with ADHD get moving when tasks feel impossible. It focuses on three things: AI task breakdown: Type in a big goal, and Firefly gives you an immediate first step you can take in under a minute. It also generates an editable action plan with realistic time estimates. Visual focus timer: A shrinking disc timer makes time visible, tackling time blindness head on. Breaks are built in to keep momentum steady. Dashboard and analytics: Signed-in users get a simple dashboard that tracks focus time, streaks, and session history, offering encouragement without judgment. How I built it The frontend runs on Next.js 14 with Tailwind CSS. Supabase handles the database and Google authentication. For the AI, I used Gemini to power the task breakdown feature. A big shoutout to Kiro, the agentic IDE I used. Its structured workflow helped me stay on track and actually finish this within the hackathon window, even while working solo. Challenges I ran into Wearing all the hats at once was tough. Getting the timer to run with perfect accuracy took more debugging than I expected. Crafting prompts for reliable time estimates was also tricky, since small wording changes made a huge difference. Accomplishments that we're proud of I’m proud that I shipped this app on my own. The AI breakdown feature in particular feels like a personal win, because it directly solves the problem I’ve wrestled with for years. Seeing it actually work gave me a lot of confidence that Firefly can help others too. What I learned This project taught me a ton about Supabase and Gemini, but more importantly it taught me how to build with neurodiverse users in mind. Designing something that lowers friction for people with ADHD was eye-opening, and it’s a lesson I want to carry into future projects. What's next for Firefly - ADHD focus app I want to keep developing Firefly beyond this hackathon. First up is improving the dashboard with more useful analytics. Long term, I’d like to grow a user base, collect feedback, and eventually turn Firefly into a sustainable product that supports itself while helping more people. <div