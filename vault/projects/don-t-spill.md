---
slug: "don-t-spill"
url: "https://devpost.com/software/don-t-spill"
title: "Don't Spill!"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 396
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "substrate/video_visual"
---

# Don't Spill!

> Don’t Spill! is a fast, turn-based Snapchat mini-game: tilt your bottle to fill the glass, but don’t overflow. Outplay a friend in quick rounds, with a clear winner and instant replay.

[Devpost](https://devpost.com/software/don-t-spill) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

**mechanism** [[deterministic_policy]] [[vision_ocr]]
**domain** [[developer_tools]]
**substrate** [[video_visual]]

**stack** figma, javascript, lensstudio, snapchat

## How they structured the write-up

- features
- inspiration
- what it does
- how i built it
- problems
- accomplishments that you are proud of
- what’s next for don’t spill!

## Body

Don’t Spill! is a turn-based Snapchat Lens game where two players take turns carefully pouring into a shared glass. Hold to pour, release to stop—push your luck, but if you overflow, you lose, and the other player is shown as the sole winner. Features Turn-based multiplayer with a shared glass level that persists across turns. Hold-to-pour mechanic with smooth tilt animation and clear water meter feedback. Overflow detection that can exceed 100% to make the losing moment obvious. Winner-only Game Over screen (only the victor is shown). Continue/Restart flows designed to match Snapchat’s capture + turn progression. Lightweight, mobile-friendly UI over the camera feed. Inspiration Social media challenge videos where friends take turns doing “don’t spill” style challenges together, escalating the tension for fun and bragging rights. The idea of a snackable, social mini-game that fits Snapchat’s fast back-and-forth sharing. What it does Player 1 pours into a shared glass and ends the turn with a snap. Player 2 receives the same glass state, decides how risky to play, and pours next. The first player to overflow loses; the other player is declared the winner. Players can restart and replay quickly, encouraging rematches. How I built it Designed the 2D UI and bottle/glass visuals in Figma and imported them into Lens Studio with ScreenTransforms and scene objects. Implemented a simple state machine (idle/tilt/pour/return/gameover) to control animation, pouring, and scoring. Used global shared variables to sync glass level, game-over state, and winner between two devices. Tuned performance by minimizing startup work and limiting per-frame updates to only when needed. Problems Debugging was a pain: Lens Studio would crash when I tried to inspect certain debug states, so local debugging wasn’t reliable. To properly test turn-sync behavior, I had to publish repeatedly and debug with two phones and two accounts. Sadly, it couldn’t realistically be done without publishing—hopefully Lens Studio adds a smoother multiplayer debugging workflow soon. Accomplishments that you are proud of A responsive, intuitive hold-to-pour mechanic that feels good on mobile. Clean winner-only end screen that makes results clear and shareable. A complete turn-based experience that feels native to Snapchat’s capture-and-send flow. What’s next for Don’t Spill! The mechanic can be re-skinned for any beverage—coffee, soda, energy drinks, milkshakes—without changing the core game. It’s highly brandable and ready for commercialization: custom bottles/cups/UI for campaigns, from Starbucks-style seasonal cups to major beverage launches and limited-edition promos. <div