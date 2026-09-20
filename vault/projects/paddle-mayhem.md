---
slug: "paddle-mayhem"
url: "https://devpost.com/software/paddle-mayhem"
title: "Paddle Mayhem!"
hackathon: "Meta Horizon Creator Competition: Mobile Innovation"
organization: "Meta"
winner: true
words: 288
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
---

# Paddle Mayhem!

> Paddle your physics-based boat through a chaotic obstacle course as you clumsily compete or ram into your enemies!

[Devpost](https://devpost.com/software/paddle-mayhem) · hackathon [[Meta Horizon Creator Competition- Mobile Innovation]]

## Facets

**substrate** [[geospatial]]

**stack** horizon, meta

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for paddle mayhem!

## Body

Inspiration Paddle Mayhem is inspired by Fall Guys but with even more chaos and unpredictable physics. What it does You paddle a physics-based boat through a wild obstacle course while competing or crashing into other players. The game is designed for mobile portrait mode. Tapping the left side of the screen paddles left, and tapping the right side paddles right. The ideal experience requires 4 players, but the match will automatically begin after 20 seconds if there are not enough players. You race to place first, second, or third, and you can also compete for the fastest times on the global leaderboard. How we built it The project was built using Meta Horizon GenAI, TypeScript and Blender. Challenges we ran into Water shader support is not available yet. The player's position does not update together with the physics boat, which causes the player to lag behind. Even with mentor assistance, we were not able to find the root cause. Animation masking is limited. Horizon currently supports masking only for the upper body, so I could not create proper paddle animations for the left and right sides of the body, as I need a right and left mask. Accomplishments that we're proud of Playtesting with four players created a lot of laughter! What we learned Creating a networked multiplayer game in Horizon is very fast, and publishing updates is extremely quick. What's next for Paddle Mayhem! I want to increase the player count to 32, which will require a larger map. I also want to add a mode where two players share one boat. One player paddles on the right and the other paddles on the left. This will create a new level of teamwork and social interaction. <div