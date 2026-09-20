---
slug: "codemafia"
url: "https://devpost.com/software/codemafia"
title: "CodeMafia"
hackathon: "ConUHacks X"
organization: "HackConcordia"
winner: true
words: 645
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
---

# CodeMafia

> Among Us meets competitive programming! Developers race to fix bugs while an impostor secretly sabotages their code.

[Devpost](https://devpost.com/software/codemafia) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]] [[developer_tools]] [[finance_payments]]
**user** [[developer]]

**stack** framer, partykit, pyodide, python, react.js, typescript, zustand

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for codemafia

## Body

Main Menu Lobby Problem Category Vote You are the impostor! You are a civilian... Civilian View Impostor View Code Editor EMERGENCY MEETING! SOMEONE'S SUS lmao ;-( Impostor W Inspiration We love the popular video game "Among Us" and we love coding challenges, so we thought: why not combine them? The idea came from late-night LeetCode sessions where we'd joke about how one wrong semicolon could sabotage an entire solution. We wanted to create a game where debugging isn't just a chore but the actual gameplay, and where you have to question whether your teammate's "fix" is helping or hurting. What it does CodeMafia is a multiplayer social deduction game for 3-5 players. Everyone joins a lobby and works together to fix broken Python code by completing TODOs and passing test cases. But here's the twist: one player is secretly an impostor whose job is to sabotage the code without getting caught. Civilians win by completing all tests or voting out the impostor. The impostor wins by completing their sabotage tasks or surviving until time runs out. Players can call emergency meetings to discuss suspicious behaviour and vote people out, just like in "Among Us". How we built it We built the frontend with React, TypeScript, and Vite, using Zustand for state management and Framer Motion for animations. The real-time multiplayer is powered by Partykit, which handles WebSocket connections and keeps game state synchronized across all players. We integrated Monaco Editor (the same editor VS Code uses) for the coding interface, complete with syntax highlighting and collaborative editing. The most interesting technical challenge was running Python tests directly in the browser using Pyodide, which compiles Python to WebAssembly. This lets us validate code changes instantly without needing a backend server. Challenges we ran into Getting multiplayer synchronization right was harder than we expected. We had bugs where the game would end incorrectly, infinite test loops that caused flickering, and a frustrating cursor jumping issue that made typing nearly impossible. The cursor problem took multiple attempts to fix because we were fighting against the editor's internal state management. We also had to figure out how to verify impostor sabotage tasks accurately, ensuring they actually broke the code in specific ways rather than just any random breakage. Debugging a game about debugging code created some amusing meta moments. Accomplishments that we're proud of We're really proud of getting real-time collaborative code editing working smoothly across multiple players. The Python-in-browser testing system is surprisingly fast and reliable. The game actually feels balanced, with both roles having clear win conditions and strategic depth. We also added some delightful polish like animated weather effects on the main menu (wandering animals, flying birds, rain effects) that make the game feel more complete. Most importantly, it's genuinely fun to play, even after testing it dozens of times. What we learned This project taught us a lot about real-time multiplayer architecture and the importance of server-authoritative state. We learned that browser-based code execution is not only possible but practical with modern WebAssembly tools. We also gained experience with complex state management in React and discovered that sometimes the best solution is to stop fighting the framework and work with it (like making the editor uncontrolled instead of controlled). On the non-technical side, we learned how to scope features for a hackathon and prioritize polish over perfect implementation. What's next for CodeMafia We want to add more programming languages beyond Python, starting with JavaScript and Java. A ranked matchmaking system would make the competitive aspect more engaging. We're also thinking about adding more impostor abilities like temporarily disabling someone's editor or planting fake test results. User-generated content would be huge, letting players create and share their own coding challenges. Finally, we'd love to add voice chat integration since text chat during emergency meetings doesn't quite capture the chaos of arguing about who's the impostor. <div