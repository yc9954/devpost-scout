---
slug: "wobble-clash"
url: "https://devpost.com/software/wobble-clash"
title: "Wobble Clash"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 535
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "substrate/geospatial"
---

# Wobble Clash

> A Snap-powered AR battler where friends clash in turn-based combat using unique characters, items, and terrain bonuses.

[Devpost](https://devpost.com/software/wobble-clash) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

**mechanism** [[deterministic_policy]]
**substrate** [[geospatial]]

**stack** javascript, lensstudio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for wobble clash

## Body

Inspiration Wobble Clash was inspired by turn-based strategy games that focus on positioning, terrain interaction, and tactical decision-making, such as Baldur’s Gate 3 and Divinity: Original Sin 2 . These games demonstrate how terrain bonuses, action economy, and careful planning can significantly influence combat outcomes. At the same time, the project was inspired by asynchronous multiplayer experiences and the way Snapchat enables fast, playful interactions between friends without requiring them to be online simultaneously. The goal was to bring deep, tactical gameplay into a lightweight, social AR experience. What it does Wobble Clash is a Snap-powered, asynchronous AR turn-based battler where friends clash in tactical combat. Players choose one of four unique characters called Wobblers, each with distinct stats and abilities, and select four items before the match begins. Battles take place on an AR hex-based battlefield composed of different terrain types, such as grass or sand, each providing terrain-specific bonuses. Players take turns using a limited number of Action Points to move, attack, use items, or end their turn. After ending a turn, the current game state is sent to the opponent via Snap, allowing the match to continue asynchronously until one Wobbler’s health reaches zero. How we built it The game was built using Lens Studio, which allows rendering a hexagonal battlefield in the real world through AR. The core gameplay logic is deterministic and turn-based, ensuring consistency between players devices. A lightweight game state system was designed to serialize all relevant data (positions, health, items, and turn state) and transfer it through Snap messages. This approach enables asynchronous multiplayer gameplay while keeping matches fair and predictable. Character abilities, items, and terrain bonuses were carefully designed and balanced to create meaningful tactical choices within the constraints of limited Action Points. Challenges we ran into One of the biggest challenges was designing an asynchronous multiplayer flow that feels clear and engaging despite players not being online at the same time. Ensuring that each turn accurately reflects the game state was critical. Balancing strategic depth with accessibility was another challenge. The game needed to be easy to understand for new players while still rewarding smart positioning, terrain usage, and item selection. Working with AR also introduced challenges related to battlefield placement, scale, and readability across different physical environments, requiring multiple iterations and testing. Accomplishments that we're proud of Successfully creating an asynchronous turn-based multiplayer experience where players exchange turns via Snap. Combining AR with a hex-based tactical combat system. Designing distinct characters, items, and terrain bonuses that meaningfully affect gameplay. Building a social game flow that encourages friendly competition at a flexible pace. What we learned Through building Wobble Clash, we learned how to design and implement asynchronous multiplayer mechanics, manage shared game state across devices, and balance turn-based combat systems. We also gained hands-on experience with AR gameplay design, especially in making strategic mechanics readable and intuitive in real-world environments. What's next for Wobble Clash Next steps for Wobble Clash include adding new Wobblers with unique abilities, expanding the item pool to enable more diverse builds, and introducing different map types with new terrain layouts and tactical possibilities. Future improvements may also focus on balancing, visual polish, and refining the overall player experience. <div