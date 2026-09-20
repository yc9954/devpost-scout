---
slug: "snitch-ackp1s"
url: "https://devpost.com/software/snitch-ackp1s"
title: "Snitch"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 800
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/web_dom"
---

# Snitch

> Lock in or pay up.

[Devpost](https://devpost.com/software/snitch-ackp1s) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[realtime_stream]] [[vision_ocr]]
**domain** [[education]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[web_dom]]

**stack** discord.py, fastapi, gemini, mediapipe, python, react, sqlite, sqlmodel, stripe, tailwindcss, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for snitch
- figma make track

## Body

Timer with No Distractions Timer with Active Distraction Stats Summary Page Starting a Session from Discord An Active Session in Discord Browser Extension Browser Extension Blocking Popup Demonstration of the CV Models Running Architecture Diagram Inspiration As students, our group always joked about making bets on whether someone would turn in an assignment late, skip studying for a test, or get distracted when they were supposed to lock in. It was funny because everyone knew the pattern: someone says they are going to study, then ten minutes later, they are on YouTube, League of Legends, or their phone. That made us wonder: what if those bets were real? If your friends could actually benefit when you failed to focus, would that be enough pressure to keep you honest? Snitch is built for students who already know what they need to do. They have a deadline, an exam, or a goal. They just need a real reason to follow through. What it does Snitch is an accountability platform built for students without something on the line. Users create timed focus sessions, similar to pomodoro timers, but with real, self-imposed consequences. A user chooses how long they want to focus, how much money they want to put on the line, and which friends should receive the money if they fail. During a session, Snitch tracks distractions in multiple ways. The web app uses the webcam to detect signs of distraction, such as looking away, leaving the frame, or using a phone. A Chrome extension monitors visits to distracting websites and reports them as strikes during active sessions. Importantly, the extension does not block sites during a live session, because the point is to prove you can stay focused on your own. If the user reaches the strike threshold, they fail, and the money is paid out to the selected recipients (doubters, as we call them). If they finish the timer under the threshold, they keep their money. Snitch also includes stats, streaks, focus history, a Discord bot for creating sessions with friends, and Stripe-powered payment/payout setup. Demonstration of the CV models doing eye tracking, object detection (with the phone and person), and pose estimation How we built it Built the main app with React, TypeScript, Vite, and Tailwind CSS Used MediaPipe Tasks Vision for webcam-based distraction detection Detected focus signals like looking away, leaving the frame, and phone usage Built the backend with FastAPI, SQLModel, SQLite, and JWT auth Integrated Stripe and Stripe Connect for saved cards and direct payouts to friends’ accounts Created a Chrome extension to track visits to distracting sites and report them to the backend Built a Discord bot with discord.py so friends can create sessions, join as recipients, and watch live updates directly from the platform Used Server-Sent Events to stream session status and distraction counts back to Discord Challenges we ran into Making webcam distraction detection reliable enough with noisy browser-based computer vision Keeping session state consistent across page reloads, tab closes, Discord launch links, and extension messages Designing the Chrome extension so it tracks distractions without blocking sites during active sessions Linking Discord and Snitch accounts in an intuitive, easy-to-use manner Handling Stripe integration for a smooth onboarding experience and seamless payments Accomplishments that we're proud of Built an end-to-end session system that turns your failures into your friends’ financial gains Ran distraction detection locally using 4 computer vision AI models in parallel Integrated multiple surfaces, including the web app, backend, Chrome extension, Discord bot, and Stripe, into a cohesive system Made it through the night in the sleeping room What we learned Working around noise with 4 browser-based computer vision models to accurately detect distractions while preventing false positives (especially since money is on the line) Building across so many surfaces (web app, Chrome extension, Discord bot, backend) forced us to think carefully about shared state and event-driven architecture (SSE vs. polling) Learning how to integrate real payment flows with Stripe, from securely collecting payment methods to handling payouts and money movement between users What's next for Snitch Migrate to a desktop app/background process to simplify starting sessions, even when users leave the website Support WhatsApp or SMS-based session flows, for deeper integration into social networks beyond Discord Add recurring/scheduled sessions, study groups, friend/community leaderboards, and more to deepen retention within friend groups and keep the social stakes alive over time Figma Make Track We used Figma Make to give us inspiration for the frontend, specifically with A/B style testing. The AI agent allowed us to iterate through prototypes far faster than would otherwise have been possible, allowing us to easily determine what colors would work better, what design styles would fit better, what layouts would allow for better user experiences, and more. The whole design and interaction can be found here . <div