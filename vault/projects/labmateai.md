---
slug: "labmateai"
url: "https://devpost.com/software/labmateai"
title: "LabMateAi"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 699
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "domain/mental_health"
  - "user/educator_student"
  - "substrate/geospatial"
---

# LabMateAi

> LabMate AI is an interactive, virtual science lab where students run real physics experiments and get instant AI-mentored feedback in-browser without hardware.

[Devpost](https://devpost.com/software/labmateai) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[simulation_digital_twin]]
  <sub>weak: voice_speech</sub>
**domain** [[education]] [[mental_health]]
**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** and-gemini-2.5-flash-api.-the-app-is-deployed-on-vercel-and-runs-fully-in-the-browser.-gemini-is-used-for-the-optional-ai-mentor, framer-motion, localstorage, react-18, recharts, tailwind-css, typescript, vite, vitest, web-speech-api-/-text-to-speech, zustand

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for labmateai

## Body

chemistry simulation lab for acid base bolt our app interactive AI character that helps user to interact with UI and gives Fact physics simulation of Ohm law Biology simulation for photosynthesis User report at the end of session of labs practical Our landing page Inspiration Many students learn science through theory, diagrams, and memorized formulas, but they do not always get access to real lab equipment. Physical labs can be expensive, limited, unsafe, or unavailable outside school. We wanted to make STEM learning feel more interactive, playful, and accessible — like Duolingo, but for science labs. That inspired us to build LabMate AI: a browser-based virtual science lab where students can experiment, make predictions, get instant feedback, and learn by doing. What it does LabMate AI is an AI-mentored, mission-based virtual STEM lab. Students complete interactive lab missions across Physics, Chemistry, and Biology. The main Physics mission, “Make the Bulb Glow Safely,” teaches Ohm’s Law using a real-time circuit simulation. Students can change voltage and resistance, then watch current, power, bulb brightness, heat, and safety status update instantly. If they push the circuit too far, the bulb burns out. The learning flow includes a mission map, lab brief, interactive experiment, prediction challenge, AI mentor explanation, quiz, XP rewards, and a saved progress report. The AI mentor, Volt, explains what happened using the student’s live experiment values. The app also works without an API key using a built-in fallback mentor. How we built it We built LabMate AI using React 18, Vite, TypeScript, Tailwind CSS, Framer Motion, Zustand, Recharts, and Gemini 2.5 Flash. The simulation logic is based on real equations such as Ohm’s Law and power dissipation. Voltage and resistance values are used to calculate current, power, brightness, heat, and safety status. Zustand manages lab state and progress, while localStorage saves XP, streaks, reports, and mission progress. The AI mentor was built as progressive enhancement. If a Gemini API key is available, Volt can generate live explanations. If not, the app still works using a rich hand-authored fallback mentor that uses the live circuit values. Challenges we ran into One challenge was making the app feel like a real interactive lab instead of a normal quiz app. We had to make the simulation visual, responsive, and understandable while still using real science. Another challenge was keeping the demo reliable for a hackathon. Since API keys and Wi-Fi can fail, we built the AI mentor so the app remains fully functional even without Gemini. We also had to optimize performance during slider interactions. Since the simulation updates in real time, we used Zustand selectors, lightweight animations, and browser-friendly motion effects to avoid unnecessary re-renders. Accomplishments that we're proud of We are proud that LabMate AI is more than a static educational app. It lets students interact with a real simulation, make mistakes, see consequences, and learn from them. The bulb burnout moment is one of our favorite parts because it turns an equation into something visual and memorable. We are also proud of the complete learning loop: mission, prediction, experiment, mentor feedback, quiz, XP, and report. We also made the project demo-safe by ensuring it works with or without an AI API key. What we learned We learned how important it is to make educational apps feel active instead of passive. Students understand concepts better when they can change variables and immediately see the result. We also learned how to combine deterministic simulations with AI. The simulation should be the source of truth, while the AI acts as a mentor that explains what happened. Finally, we learned how to design for reliability, especially in a hackathon environment where the app needs to work smoothly during a live demo. What's next for LabMateAi Next, we want to expand the Chemistry and Biology missions with deeper simulations, more experiments, and more mission paths. We also want to add student accounts, teacher dashboards, classroom assignments, leaderboards, and shareable progress reports. In the future, LabMate AI could support more STEM topics, adaptive difficulty, voice-based tutoring, and multiplayer classroom challenges. Our goal is to make virtual labs accessible to any student with a browser, whether or not they have access to physical lab equipment. <div