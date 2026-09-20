---
slug: "risk-it"
url: "https://devpost.com/software/risk-it"
title: "RISK IT"
hackathon: "Meta Horizon Creator Competition: Elevate Your Mobile World"
organization: "Meta"
winner: true
words: 668
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/code_repository"
---

# RISK IT

> Risk It is a fast-paced multiplayer dice game in Horizon Worlds. Bet your points, test your luck, and race to 100 to win. Easy to play, thrilling to master!

[Devpost](https://devpost.com/software/risk-it) · hackathon [[Meta Horizon Creator Competition- Elevate Your Mobile World]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[code_repository]]

**stack** typescript

## How they structured the write-up

- inspiration
- what it does
- how to play
- core mechanics
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next for risk it

## Body

RISK IT: The Multiplayer Dice Game for Horizon Worlds Inspiration The inspiration for RISK IT came from classic dice games and the thrill of pushing your luck. I wanted to capture that heart-pounding moment where a single roll could turn everything around, and bring that energy into a multiplayer VR experience. The idea was to create something instantly approachable, but layered with strategic decisions that keep players coming back. What It Does RISK IT is a fast-paced, multiplayer dice game built in Horizon Worlds . Players compete to be the first to reach 100 points by rolling dice, making strategic bets, and deciding when to risk it all or play it safe. The game supports up to 8 players, with real-time UI feedback, dynamic betting, and persistent player stats and leaderboards. How to Play Join the Game: Up to 8 players can join each session. Players can enter or leave the game at any time before it starts. Rolling Phase: On your turn, roll the die. If you roll a 1, you lose your turn and any points you risked this round. Any other number adds to your turn total. Roll the same number twice in a turn? That’s a multiplier: your turn total doubles! Roll the same number a third time? You bust and lose your turn points. Risk or Keep: After every successful roll, decide: “Keep It” (bank your turn points and pass) or “Risk It” (roll again to stack more points—if you dare!). Bets & Wagers (Multiplayer): Non-rolling players place bets on what number the roller will hit, or if they’ll bust. Wager your points for bigger potential rewards—correct bets can swing the game! Winning: First player to reach 100 points wins. Win or lose, you’ll earn “Biscvits” (persistent currency) for every game—track your progress on the leaderboard. Core Mechanics Push-Your-Luck Dice Rolling: Every turn, weigh the risks—play it safe or stack up points for a huge lead. Live Betting: Non-rollers stay engaged by betting on every turn. The more you wager, the more you can win (or lose). Multipliers: Rolling the same number twice doubles your gains. Rolling it a third time means you lose everything for that turn. Bust and Timeout Handling: Fast-paced flow, with built-in timeouts to keep the game moving and kick idle players. Persistent Progress: Player stats, win counts, and earned Biscvits are stored and tracked across all sessions. How We Built It The project was built from scratch using TypeScript and the Horizon Worlds scripting API. All gameplay logic, UI systems, and triggers are custom-scripted, with persistent storage for player stats and leaderboard integration. Special attention was given to mobile/VR parity, smooth game flow, and scalable code architecture to handle up to 8 players per session. Challenges We Ran Into Prop Management: Horizon Worlds requires hundreds of prop connections. Organizing and wiring up 500+ props for UI, triggers, and SFX/VFX was a major time sink. State Synchronization: Keeping every player’s UI, score, and betting state perfectly synced in a fast-paced environment took serious debugging and iteration. Persistent Variables: Updating and retrieving player-specific stats and preferences reliably, especially across different sessions, required deep dives into the storage APIs. Optimization: Making the codebase efficient and maintainable under tight world capacity limits was an ongoing challenge. Accomplishments We’re Proud Of A seamless multiplayer experience that’s fun and fair, regardless of platform. Fully persistent leaderboards and player stats, adding replay value and bragging rights. Highly modular, reusable code that could serve as a template for future party games in Horizon Worlds. What We Learned How to optimize large-scale TypeScript projects for Horizon Worlds’ unique environment. Best practices for user state management, persistent storage, and live UI in VR. The value of thorough planning, iterative prototyping, and obsessive testing. What’s Next for RISK IT Adding new custom game modes and rule variants. More social features, like player profiles and friend challenges. Visual upgrades, new VFX/SFX, and seasonal events. Try RISK IT now in Horizon Worlds, and see if you can handle the pressure! <div