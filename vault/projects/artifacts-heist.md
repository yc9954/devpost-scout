---
slug: "artifacts-heist"
url: "https://devpost.com/software/artifacts-heist"
title: "Artifacts Heist"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 680
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/immigration_refugee"
  - "substrate/geospatial"
---

# Artifacts Heist

> Infiltrate an Art Gallery! Steal up to 9 artifacts while dodging security. Reach the exit within 6 mins to score. One mistake resets the heist. Take the risk or play it safe for the leaderboard?

[Devpost](https://devpost.com/software/artifacts-heist) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

**domain** [[immigration_refugee]]
**substrate** [[geospatial]]

**stack** bitmojisuite, blender, javascript, lensstudio, snapgenaisuite

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- what i learned
- what's next for artifacts heist

## Body

Game Lens Preview 1 GIF This Artifact is familiar ! Blender Behind The Build 1 Game Lens Preview 2 GIF Just Hanging around Blender Behind The Build 2 Lens Studio Behind The Build Preview Inspiration As a gamer, a digital artist and a daily Blender user, I wanted to merge the adventurous atmosphere of the Uncharted game series with the ruthless stakes of Alice in Borderland . For my first Devpost hackathon, I set out to turn any physical environment into a high-security Art Gallery where the player’s greed is their own worst enemy. My background in gaming drove me to create a "one more try" experience that challenges the player's skill and nerves. What it does Artifacts Heist is a Game Lens that challenges players to infiltrate an Art Gallery and steal up to 9 masterpieces. Interactive Stealing : To steal an artifact, the Bitmoji must be close to it. A "Grab" button dynamically appears in the UI next to the jump button, tapping it collects the item and removes it from the scene. The button automatically hides when the player moves away or completes the action. Bitmoji Integration : To fully immerse the player, I used the Bitmoji Suite to automatically outfit the player's avatar in a "thief" costume all black clothing and an eye mask. This ensures that every player fits the theme. Players decide their own level of risk; you can head for the exit at any time, but more artifacts mean a higher score.The gallery is protected by dynamic security systems. If you are detected or the 6-minute timer hits zero, the heist fails and the entire game state resets.The final score is calculated by balancing the value of stolen artifacts against the speed of the escape using the following formula: $$TotalScore = \sum(ArtifactPoints) + (RemainingSeconds \times 0.1)$$ Choice Driven Level Design : The gallery features branching paths. While a main exit is clearly signposted, players can discover a "Secret Exit" via a platforming challenge. Risk vs Punishment : Greed triggers environmental changes. If a player steals the final masterpiece (Artifact 9), the primary exit is permanently blocked by a room-lock mechanic, forcing a high-stakes escape through a hidden, difficult upper level route. Complete Game Cycle : I customized the core platforming framework to include a tailored Start Screen with clear game instructions and an explanation of the Total Score logic. EndGame Logic : Upon reaching the exit, players are greeted with a personalized endScreen that displays their score alongside a Global leaderboard . How i built it I used Blender to create and optimize the gallery assets, ensuring they maintained high visual quality within the constraints of mobile AR. To handle the logic, I utilized the Lens Studio GenAI Suite to help manage and refine the complex scripts required for the global timer, collision-based resets, and scoring math. This AI assisted workflow allowed me to troubleshoot and polish the game's code much faster and easier. Framework & UI : I utilized the Lens Studio Platformer Template as a foundation. I heavily modified the UI and UX flow, building custom instruction sets for the start screen and refining the end-state logic to ensure players understood the "Risk vs Reward" scoring mechanics. Avatar Customization : I implemented the Bitmoji Suite to override default outfits. Challenges i ran into Optimization was the most time-consuming part of the build. I had to delete and re-import my 3D models several times to fix several issues and ensure the overall scale felt natural in an AR space. I eventually rebuilt and updated the entire Lens to ensure a perfect polish and look. What i learned Through this project, I learned to leverage AI assisted scripting to polish intricate game logic. I focused heavily on calibrating the 3D physics to ensure that navigating the gallery's security felt rewarding, making those high stakes "close-call" moments feel earned. What's next for Artifacts Heist I aim to build more complex game mechanics, such as interactive puzzles. I also plan to introduce more varied gallery layouts to keep the challenge fresh for the community. <div