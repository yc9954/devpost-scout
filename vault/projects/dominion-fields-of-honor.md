---
slug: "dominion-fields-of-honor"
url: "https://devpost.com/software/dominion-fields-of-honor"
title: "Dominion: Fields of honor"
hackathon: "DeveloperWeek 2026 Hackathon"
organization: "DevNetwork"
winner: true
words: 645
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/web_dom"
---

# Dominion: Fields of honor

> Dominion: Fields of Honor – a browser‑based, chess‑inspired war tactics game where smart terrain, unit strategy, and adaptive AI turn every match into a fast-thinking battle for the command post.

[Devpost](https://devpost.com/software/dominion-fields-of-honor) · hackathon [[DeveloperWeek 2026 Hackathon]]

## Facets

**domain** [[developer_tools]]
**substrate** [[web_dom]]

**stack** css, flask, git, github, html, javascript, python, visual-studio-code

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dominion: fields of honor

## Body

Sign up Login Home page Guide Player Records (Admin Version) Player Records (User Version) FAQ Battle match About page Inspiration Dominion: Fields of Honor was inspired by the deep, turn‑based tactics of chess and the modern war‑strategy feel of the mobile game World Conqueror 3. I wanted to create a digital battlefield that combines chess‑like clarity and positioning with modern units, terrain effects, and objective‑based victory conditions instead of just capturing a single piece. The result is a web‑based turn‑based war‑tactics game where every tile, unit type, and move feels meaningful. What it does Dominion: Fields of Honor is a browser‑based, turn‑based strategy game where two sides—player and AI—deploy units on a 10×10 grid and fight to control the battlefield. Players place a commander and supporting units on the back two rows, then take turns moving and attacking while respecting terrain rules (for example, mountains block movement). The game ends when one side either captures the enemy command post or eliminates both enemy commanders, providing a clear, objective‑driven win condition that feels closer to modern strategy games than classic chess. How we built it We built Dominion: Fields of Honor as a web application using HTML, CSS, and JavaScript for the frontend and Python with Flask for the backend logic and state management. The board is represented as a 2D grid, with each tile storing terrain type and unit information, while JavaScript handles player input, unit placement, movement, and combat. We used Git and GitHub to version our code and VS Code as our main editor, allowing us to iterate quickly and keep the project organized as features like AI behavior, modals, and win‑condition checks were added. Challenges we ran into We faced several technical and design challenges. One major hurdle was debugging logic errors in movement and combat, where units would sometimes move illegally or victory conditions would not trigger correctly. We also struggled with layout and UI consistency, especially when the board and unit‑selection bar would misalign or create awkward gaps on different screen sizes. Another challenge was implementing a strong AI that felt smart without being overwhelming, which required multiple iterations of rule‑based heuristics and careful balancing of unit stats and terrain effects. Accomplishments that we're proud of We are proud that Dominion: Fields of Honor successfully blends chess‑style tactics with modern war‑game mechanics into a coherent, playable experience. We’re also proud of how far we pushed our web‑development skills, going from basic HTML/CSS pages to a full‑featured interactive game with persistent state, modals, and an AI opponent. The project demonstrates that a small team can build a polished strategy game from scratch using standard web technologies, and it serves as a solid foundation for future improvements and expansions. What we learned Through this project, we learned how to design and structure a complete web application, from layout and styling with HTML and CSS to interactive behavior with JavaScript and backend coordination with Python and Flask. We also learned how to organize data—representing the board, units, and game state in a way that makes logic and debugging easier—and how to treat errors as learning opportunities by reading console logs, inspecting elements, and testing small changes incrementally. Overall, Dominion: Fields of Honor taught us how to turn an idea into a working product through iteration, problem‑solving, and disciplined code organization. What's next for Dominion: Fields of honor Going forward, we plan to improve the AI logic, so the opponent feels even smarter and more challenging. One key direction is to upgrade the AI from simple rule‑based heuristics to A* search for movement, allowing the AI to find optimal paths around terrain and toward objectives. We also want to experiment with minimax‑style decision‑making so the AI can look several turns ahead and choose moves that maximize its chances of winning, making Dominion: Fields of Honor a much tougher and more rewarding strategy experience. <div