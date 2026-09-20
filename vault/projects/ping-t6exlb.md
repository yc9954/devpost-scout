---
slug: "ping-t6exlb"
url: "https://devpost.com/software/ping-t6exlb"
title: "Chores.gg"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 274
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# Chores.gg

> Chores.gg is a passthrough-powered lifestyle app that gamifies chores using AI.

[Devpost](https://devpost.com/software/ping-t6exlb) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

**substrate** [[video_visual]]

**stack** braincloud, c#, gemini, meta, passthrough, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chores.gg

## Body

Inspiration Conway had the idea to help with his ADHD by taking some psychological concepts like variable reward and combining them with vision AI to create a game that makes doing IRL boring tasks like chores more fun. After he posted a demo of this on Twitter, Hayden noticed it and had the thought to rebuild the general idea from scratch for the Quest platform for the hackathon. We then joined forces to elevate the project further! What it does Chores.gg detects chore activity and awards XP for it, making chores more fun! How we built it In Unity, we use the Meta Passthrough Camera API and Google Gemini API to determine chore activity and award points through a brainCloud backend. We also use hand tracking and head tracking to place content in the world. Challenges we ran into At one point we placed spatial anchors at detected chore locations that would track progress and completion. However, we could not get consistent-enough results from Gemini to reliably support this feature, so we pivoted back to a purely activity-based experience. Accomplishments that we're proud of In addition to the MVP, we also managed to include features such as a daily streak score and a leaderboard! What we learned AI pairs very well with passthrough, and this synergy will continue to unlock new use cases over time in the near future! What's next for Chores.gg We will continue to polish and iterate based on feedback and then release as a free-to-play app. Additionally, Conway has been working on custom VLMs, and we plan to fine-tune vision models to detect progress, completion, and more specific milestones. <div