---
slug: "word-finder"
url: "https://devpost.com/software/word-finder"
title: "Word Finder"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 617
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/video_visual"
---

# Word Finder

> A famous tactile word puzzle experience featuring daily progression, where you connect the letters on the wheel to fill the board and master new levels over time.

[Devpost](https://devpost.com/software/word-finder) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[video_visual]]

**stack** gemini, javascript, lensstudio, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for word finder

## Body

Inspiration With the return of game development to Snapchat, I looked at the platform and saw a missing piece. While there are plenty of quick-play no-brainer experiences, I felt a gap for the kind of game you play to unwind the digital equivalent of a Sunday morning crossword. I wanted to bring that classic, tactile puzzle experience to the Snap Games era. My goal wasn't to reinvent the wheel, but to perfect it for the platform: a cozy, brain-teasing game that respects the player's time and encourages them to come back daily. "Word Finder" is my answer to that, a camera-off, "Longform" experience designed to test your vocabulary in a warm, wooden aesthetic. What it does Word Finder is a vocabulary puzzle game where players connect letters on a dynamic wheel to build words and fill a crossword-style grid. It is designed as a Longform experience, utilizing time-gating mechanics to drive retention. Players choose between three difficulty tiers : Easy, Medium, and Hard. As you solve a level, you don't just mindlessly binge the next one; the game utilizes persistent storage to unlock new challenges in 3-hour intervals based on real-world time. This turns the game into a daily ritual. To help with the harder puzzles, there is a hint economy where players earn assistance by finding "bonus words" that are valid but not part of the main grid, rewarding deep vocabulary knowledge. How we built it This project was a development effort supercharged by AI collaboration. I built the experience in Lens Studio using JavaScript for the game logic, but the content pipeline was built externally. I worked alongside Gemini like a pair programmer to develop a Python script that parses a dictionary of over 25,000 common English words. We wrote algorithms to filter out obscure "Scrabble junk" to keep the game fun, and then procedurally generated the intersecting grids, exporting them as JSON like formatted data that the Lens can read. On the frontend, I focused heavily on the "feel." The game features a dynamic UI controller that mathematically resizes the letter wheel and connection lines based on whether there are 3 letters or 8, ensuring the layout always looks polished. The visual style is grounded in a tactile wooden board aesthetic, no flashy shaders, just the satisfying "clack" of a tile filling an empty slot. Challenges we ran into Fine-tuning the "Fun" factor was difficult. Early versions of the dictionary generator prioritized valid grids over common words, leading to frustrating levels. I had to iteratively refine the Python scoring algorithm to prioritize words people actually use in daily conversation. Accomplishments that we're proud of I am incredibly proud of the robust state management system. Handling a local economy of hints, tracking progress across three separate difficulty tiers, and managing time-gated unlocks required strict data serialization. I’m also proud of my teammate, the seamless AI collaboration, using Gemini wasn't just about generating code; it was about debugging complex logic flows and optimizing the grid generation algorithms. It feels like working with a senior developer who was always available to brainstorm. What we learned I gained a deep appreciation for the constraints of Snap's Persistent Storage system. With a limit on data size, I learned to be efficient with how I stored player progress. The importance of sound and haptic design and the smooth lerping animations that make connecting letters feel satisfying for users. What's next for Word Finder The foundation is set for a long-term game. The next steps include adding visual unlockables (like different themes), implementing a "Social Streak" where you can share your daily victory with friends, and expanding the Python generator to support Spanish and French dictionaries for a localized experience. <div