---
slug: "reddictionary"
url: "https://devpost.com/software/reddictionary"
title: "Reddictionary"
hackathon: "Reddit’s Games with a Hook Hackathon"
organization: "reddit"
winner: true
words: 294
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/civic_government"
  - "substrate/video_visual"
---

# Reddictionary

> Reddit writes the dictionary.

[Devpost](https://devpost.com/software/reddictionary) · hackathon [[Reddit-s Games with a Hook Hackathon]]

## Facets

**domain** [[civic_government]]
**substrate** [[video_visual]]

**stack** devvit

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for reddictionary

## Body

About the project Inspiration I thought it would be amazing to let Reddit write its own dictionary, with the community choosing the definition and photo for each finalized entry. I saw it as both a broader Reddit game and a useful tool for individual subreddits, which is why I made it publicly installable. What it does Reddictionary lets someone propose a word, then the community submits and upvotes definition and photo comments. When voting closes, the winners become a permanent, searchable dictionary entry. The app has a dedicated community at r/reddictionary, but it can also be installed in any subreddit so that community can build its own dictionary. Its settings let moderators adapt the experience to their community's needs. How I built it I built Reddictionary as a Devvit web app using React, Tailwind CSS, TypeScript, and Reddit's API. Reddit comments handle submissions and voting, while Redis stores subreddit-scoped state, cached leaders, finalized snapshots, and the searchable dictionary. Challenges I ran into The biggest challenge was keeping voting fresh without calling Reddit's API too often. I built shared caching, adaptive polling, and scheduled final snapshots to manage this efficiently. Accomplishments that I'm proud of I'm proud that I made something flexible enough for communities to adapt and run with, while still being simple enough to produce some hilarious results. What I learned I learned how important it is to design around Reddit itself instead of treating it like a generic host. Comments, votes, community identity, caching, and Devvit's inline constraints all shaped the final product. What's next for Reddictionary Next, I want to grow the dictionary, improve moderation tools, add more ways to discover entries, build retention tools for power contributors, and keep refining the experience based on how real communities use it. <div