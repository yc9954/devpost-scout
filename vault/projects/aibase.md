---
slug: "aibase"
url: "https://devpost.com/software/aibase"
title: "aibase"
hackathon: "Zero to One Hackathon by Convex Vol 2"
organization: "Convex"
winner: true
words: 334
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/finance_payments"
---

# aibase

> Never rewrite your prompts again, build a library of custom prompted AI helpers and quickly use them anywhere.

[Devpost](https://devpost.com/software/aibase) · hackathon [[Zero to One Hackathon by Convex Vol 2]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[finance_payments]]

**stack** convex, framer-motion, nextjs, node.js, polar, react, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aibase

## Body

Overview Theme-picker Bot details Inspiration Working with LLMs has become a big part of my daily routine. I use various apps for different tasks, and some tasks, like checking text for grammar errors, are repeated multiple times throughout the day. We all know that context switching negatively impact our productivity, and jumping between tabs and apps only amplifies that effect. I wanted something always close by, so I could stay immersed in my tasks and avoid losing focus. This idea has been on my mind for a while, and thanks to this hackathon, I finally had the perfect opportunity to bring it to life. So, I built AIBASE. What it does AIBASE is primarily a desktop app(also available on the web) that allows users to create a set of pre-configured AI helpers or bots. These bots are powered by top-tier LLM providers, ensuring that whenever a new model is released, users won’t need to search for a new app. How we built it Built using Electron with Vite, Typescript, React and of course Convex on the backend. On the front-end we used Radix Themes as the main UI library, animations using Framer-motion, toasts from Sonner and payment via Polar. Challenges we ran into I initially set out to build the desktop app using Tauri, and overall, I was quite happy with the experience. However, I realized that the build, deploy, and distribution process was somewhat cumbersome. Just a few days before the deadline, I decided to port the app to Electron, which also came with its own setup challenges. Despite that, I’m extremely happy with the end result. Accomplishments that we're proud of Making my first "production"-ready desktop app. What we learned A new paradigm of building front-end + backend, type-safety all the way through via Convex. What's next for AIBASE More LLM models, advanced memory(vector stores) for the bots, channel/groups for multiple helpers at once and overall adding more capabilities for the AI's. I am also very much open to feedback, cheers! <div