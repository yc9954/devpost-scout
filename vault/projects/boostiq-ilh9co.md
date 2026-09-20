---
slug: "boostiq-ilh9co"
url: "https://devpost.com/software/boostiq-ilh9co"
title: "BoostIq"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 687
team_size: 0
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "user/educator_student"
---

# BoostIq

> BoostIQ is an AI-powered learning tool that enhances memory retention (turn knowledge into memory) using spaced repetition, retrieval practice, and personalised study aids generated from any content.

[Devpost](https://devpost.com/software/boostiq-ilh9co) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]]
**user** [[educator_student]]

**stack** firebase, gemini, lovable, react, sm2-algorithm

## How they structured the write-up

- 🌟 inspiration
- 🧠 what i built
- 💡 what i learned
- 🛠️ how i built it
- 😅 challenges i faced
- 💥 final thoughts

## Body

🚀 About the Project — BoostIQ 🌟 Inspiration As someone who loves to learn and is deeply curious about how the mind works, I’ve always been fascinated by memory: Why do we forget? Why do some ideas stick, while others vanish? When I came across the theme of this hackathon — “Using AI to improve focus, memory, and critical thinking” — I instantly knew I had to build something that answered this question. So I started asking: What if AI could turn raw information into memory magic? What if studying felt more like storytelling — personal, funny, and sticky? That’s when BoostIQ was born. It’s an AI-powered tool that helps learners convert complex ideas into Memory Snapshots — highly digestible, recallable, and retainable bites of knowledge, designed with brain science in mind. 🧠 What I Built BoostIQ empowers learners to create “Snapshots” — personalized learning cards generated using AI. Each snapshot contains: ✅ A summary of the concept ❓ A question and answer for active recall 🔁 A Spaced Repetition review date, calculated using the SM-2 algorithm (used in tools like Anki) 🔊 An audio version for auditory reinforcement (dual coding) 💡 An analogy that explains the concept in simpler terms 🤪 A funny mnemonic — sometimes even customized to match the user's interests (e.g. music, football, tech) In short, it transforms what you learn into how your brain wants to remember it . 💡 What I Learned I learned that AI is incredibly powerful, but it needs guidance. I had to deeply refine my prompts to make Gemini return consistently useful outputs — especially for analogies and mnemonics. I learned how to use the SM-2 algorithm to schedule reviews in a way that mimics the brain’s natural forgetting curve — spacing out learning over time for long-term retention. I gained experience debugging complex Firebase issues, optimizing data flow between Firestore , Auth , and client state using Zustand . And I got to build something that truly reflects my passion for cognitive science + technology . 🛠️ How I Built It Frontend : React (Vite) + TypeScript + Tailwind + shadcn-ui Backend : Firebase (Authentication, Firestore, and Storage) State Management : Zustand Text-to-Speech : Web Speech API Theming : Custom Dark/Light mode toggle AI : Google Gemini, using chain-prompting to create summaries, analogies, mnemonics, and snapshot content Review Logic : Implemented the SM-2 algorithm to calculate next review intervals based on user performance Snapshot Persistence : Snapshots are stored in Firestore and tagged by topic for easy recall I also used rapid prototyping tools to build the MVP quickly, then went in and polished the UI, animations, and error handling manually for a smoother experience. 😅 Challenges I Faced API Integration : Getting Gemini to respond with consistently structured output was challenging. I had to tweak prompts multiple times and build in fallbacks. State + Firebase Sync : I ran into issues with new users not syncing properly, or data not being available on first load. I had to implement defensive logic for loading, state persistence, and fallback states. Theming & UI Polish : My first UI version was very basic. I later upgraded it with gradients, avatars, dashboard cards, and a much smoother user experience — while ensuring accessibility on both light and dark themes. Audio & Accessibility : Text-to-speech worked well, but browser inconsistencies forced me to fine-tune settings to make the voice smooth, natural, and useful for learning. Mnemonic Personalization : This was the most fun and the most chaotic — I asked the AI to generate funny mnemonics tailored to interests like "soccer", "anime", or "Islamic themes". It worked beautifully once I structured the prompts right. 💥 Final Thoughts Building BoostIQ taught me that learning doesn’t have to be boring — or hard. With the right prompts, the right logic, and the right design, we can make knowledge memorable, personal, and even funny. BoostIQ isn’t just a memory tool — it’s a smart, lovable companion for learners who want their knowledge to stick. Insha’Allah, I hope this makes a meaningful impact — because remembering what matters should feel joyful, not stressful. <div