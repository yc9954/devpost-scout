---
slug: "daily-spell-craft"
url: "https://devpost.com/software/daily-spell-craft"
title: "Daily Spell Craft"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 520
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# Daily Spell Craft

> Your daily dose of word wizardry.

[Devpost](https://devpost.com/software/daily-spell-craft) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

**mechanism** [[realtime_stream]]

**stack** cloud, javascript, lenscloud, lensstudio, persistent, persistentstorage, storage

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for daily spell craft

## Body

Game Ui Showing A Unique Daily Puzzle For Users To Solve, The Daily Puzzle Is Same For All The Snapchat Users, New Puzzle Every Midnight Goal is to type in words using the letters and the word should include the central letter, minimum word length is 3 words, gives you 3 point Complete the score to make streak and share it with your friends, Winning Game Ui, Also Lens Reopen Ui Inspiration I’m a huge fan of the NY Times Spelling Bee, The inspiration for Daily Spell Craft came from the idea of the "Digital Ritual" that we follow daily. I’ve always admired how the NY Times Spelling Bee creates a shared daily moment for millions, but I noticed that most word games feel disconnected from where we actually communicate—our social apps, that' why I wanted to take that sophisticated, minimalist puzzle experience and "craft" it specifically for the Snapchat community What it does Daily Spell Craft is a minimalist 2D word-puzzle Lens that challenges players to "craft" as many words as possible from a daily set of seven letters. Using a classic hive layout, players must find words that include the mandatory center letter. The experience features a built-in streak system that tracks consecutive days played, encouraging a daily mental ritual. With a fresh puzzle every 24 hours, users can sharpen their vocabulary, maintain their streaks, and share their progress with friends via Snap How we built it I developed Daily Spell Craft using JavaScript in Lens Studio to power the core game logic, specifically managing "Hive" mechanics, center-letter requirements, and dictionary validation. I focused on a clean, 2D Screen Transform layout to ensure a native Snapchat feel, utilizing a high-contrast aesthetic for maximum readability. Finally, I implemented a daily refresh system to synchronize new word sets for all players every 24 hours. Challenges we ran into I have made this lens to store each and every word user enters, if users cant complete the daily puzzle in a single go, they can come back later and see their progress and words there even if they close snapchat, this was a little challenging for me but help from some best community members made me overcome this challenge, another technical challenge was implementing a reliable streak and save system using Persistent Storage. I had to ensure that player progress and daily streaks were accurately tracked and stored across different sessions without resetting. Accomplishments that we're proud of I’m proud of successfully engineering the JavaScript backend to handle complex word validation and mandatory-letter constraints in real-time, ensuring the gameplay feels snappy and responsive. What we learned I gained a deep understanding of how to use Persistent Storage in Lens Studio to bridge the gap between sessions, moving beyond simple filters to create a truly persistent gaming experience. What's next for Daily Spell Craft I plan to integrate Snapchat’s Leaderboard Component so users can compete directly with their friends to see who can "craft" the most words each day, I also want to add a "Blitz Mode" where users race against a 60-second timer to find as many words as possible. <div