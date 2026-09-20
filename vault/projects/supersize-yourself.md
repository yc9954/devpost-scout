---
slug: "supersize-yourself"
url: "https://devpost.com/software/supersize-yourself"
title: "Tiny to Titan"
hackathon: "Meta Horizon Creator Competition: Elevate Your Mobile World"
organization: "Meta"
winner: true
words: 662
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# Tiny to Titan

> Eat to grow, grow to win! Race your friends in this fast-paced parkour race where you devour everything in sight to SUPERSIZE yourself before time runs out!

[Devpost](https://devpost.com/software/supersize-yourself) · hackathon [[Meta Horizon Creator Competition- Elevate Your Mobile World]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** adobe-audition, adobe-illustrator, blender, chatgpt, css, custom-ui, discord, google-docs, google-drive, google-sheets, leaderboards, maya-lt, meta-horizon-worlds-desktop-editor, mobile

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tiny to titan

## Body

Our Tiny to Titan Thumbnail! A Tiny Fella! A Titan Fella! Inspiration Tiny to Titan was inspired by games like Katamari Damacy, Agar.io, Hole.io, and all the other awesome games about getting big! We were especially seeking titles that focus on fast, satisfying progression that would translate well to a social multiplayer experience. The newly released avatar scaling feature in Horizon Worlds immediately stood out as a mechanic that could support this type of gameplay. Once we blocked in the basic scaling loop and tested it in a multiplayer context, it became clear there was something super fun and endlessly replayable there. Our goal was to build a game where progression happens at every layer: second-to-second, match-to-match, and over time through progression upgrades. What it does Tiny to Titan is a competitive multiplayer platform/racing game for up to four players. Players start small and grow larger by running over and “eating” objects in the world. The more they grow, the more they can consume. The gameplay loop centers around strategic movement, object collection, and managing growth to maximize score before the round ends. Players earn points by consuming objects, with bonus multipliers based on category-specific upgrades. At the end of each round, a podium ceremony displays the final rankings, and players can spend points on upgrade paths that enhance their performance in future rounds. How we built it We used Horizon Worlds Desktop Editor for world creation, scripting, and testing. Blender and Maya LT were used for 3D asset modeling, with Photoshop and Illustrator supporting UI and visual design. All code was written in TypeScript using Visual Studio Code. Additional tools included Adobe Audition for sound, ChatGPT for scripting support, and Google Drive for planning game logic and balance. Development was focused on mobile-first design, with regular testing on-device. We used Horizon’s tag system to categorize hundreds of interactable objects by type, which made it easier to scale the core mechanic and progression system. Challenges we ran into We were both new to Horizon Worlds and had to learn the platform’s tools, scripting model, and optimization workflows as we built. Designing a custom UI that worked cleanly on mobile required a lot of iteration. Building a world with a large number of interactive objects presented performance challenges, especially when balancing gameplay pacing across multiple players. Persistent variables were also a challenge to manage in multiplayer matches where players could enter and leave at any point. Structuring a codebase that handled all of this cleanly was a key learning curve. Accomplishments that we're proud of We were able to get the core gameplay working early in development, which gave us time to focus on polish. The HUD system, scaling mechanic, and post-match upgrade screen all came together well. We’re also proud of how we handled progression — not just within a single round, but across sessions through category-based upgrades and the rebirth system, which will later tie into cosmetic unlocks. As a team of two brand new Horizon Worlds developers, we're so proud that we were able to deliver such a feature-rich fully playable multiplayer experience so quickly. What we learned We learned how to design and script interactive systems in Horizon Worlds, with a focus on performance, mobile UX, and multiplayer logic. Creating a clean UI that adapts to player actions in real time gave us a better understanding of the platform’s limitations and strengths. We also learned how to structure a modular codebase that supports player persistence, data tracking, and post-match upgrades in a networked environment. What's next for Tiny to Titan We plan to expand the world with new levels, more object types, and additional upgrade categories. We’re also building a cosmetic unlock system tied to the rebirth mechanic. Other roadmap features include player customization, new quests, expanded leaderboard tracking, and maybe even potential VR support. The core systems are designed to scale, and we’re looking forward to growing the game further based on what players find most fun. <div