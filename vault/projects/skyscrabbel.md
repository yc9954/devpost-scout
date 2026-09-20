---
slug: "skyscrabbel"
url: "https://devpost.com/software/skyscrabbel"
title: "Skyscrabbel"
hackathon: "Reddit and Kiro: Community Games Challenge"
organization: "reddit"
winner: true
words: 806
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "substrate/geospatial"
---

# Skyscrabbel

> A global multiplayer clicker where players mine, craft, and build a shared endless tower. Automate, defend, or raid as the world climbs higher together.

[Devpost](https://devpost.com/software/skyscrabbel) · hackathon [[Reddit and Kiro- Community Games Challenge]]

## Facets

**domain** [[finance_payments]] [[labor_employment]]
**substrate** [[geospatial]]

**stack** devvit, elevenlabs, phaser.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how to play
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for skyscrabbel

## Body

Cover Mine rock and build tower automate mining purchase upgrades attack other's tower in global tower build the tallest tower among all! Defend your tower Draw on the floor wall Inspiration Skyscrabbel is a clicker game inspired by the Tower of Babel, hence Skyscrapper + Babel. The art style is inspired by 1-bit style game. What it does Skyscrabbel is a persistent multiplayer incremental game where players: Construct floors by mining rock -> crafting bricks -> placing bricks. Automate building by hiring automated miners Upgrade by purchasing click multipliers Collaborate by building the global tower alongside with others player. Reach the milestone together and everyone will get rewarded! (Levels in global tower is synced and randomized every hour) Disrupt other's building progress by deploying pest. By disrupting a player's progress, you're also disrupting the height of the global tower! Scribble on your wall, show your arts :) How to Play Getting Started Launch the Game : Click "Start Building!" on the Reddit post splash screen Mine Your First Rocks : Tap the stone in the center to mine rocks (watch it cycle through 4 states) Craft Bricks : Once you have 10+ rocks, click the furnace to craft bricks Build Your First Level : Click the ghost level outline to place bricks (10 bricks completes a level) Resource Management Rocks : Primary resource obtained by clicking stones or through miner minions Bricks : Crafted from rocks (10:1 ratio), used to build tower levels Gold : Earned by completing levels (10 gold per level) and clearing pests Tower Building Complete Levels : Fill the ghost level with 10 bricks to complete it Choose Level Type : Click completed empty levels to select: ⛏️ Miner Level : Generates rocks over time 🔨 Builder Level : Generates bricks over time Add Minions : Click miner/builder levels to open the minion management grid Hire Workers : Spend 10 gold per minion slot (up to 12 per level) Navigation & Features 🌍 Globe Button : View the global collaborative tower 📊 Leaderboard Button : See top 10 players by tower height 🛒 Shop Button : Purchase upgrades with gold 🔊 Sound Button : Toggle game audio on/off Scroll : Drag or use mouse wheel to view taller towers Advanced Gameplay Pest Combat : Click red triangular pests to clear them and earn rewards Upgrade Strategy : Prioritize click multipliers early, then automation Minion Management : Balance miners vs builders based on your playstyle Global Competition : Your completed levels contribute to the shared global tower. You may choose to infest a tower to disrupt other's tower height. Mobile Optimization Portrait Mode : Game is optimized for vertical phone orientation Touch Controls : All interactions designed for finger taps Smooth Scrolling : Swipe to navigate tall towers easily Visual Feedback : Clear animations show all resource gains and actions How we built it Skyscrabbel is devloped using Phaser.js, Devvit and Typescript with the help of Kiro. Following Devvit services are used: Devvit Redis: To store all data Devvit Blocks: Customized Splash Screen with dynamic global tower height Devvit Realtime: Update leaderboard in realtime Devvit Scheduler: Sync all personal towers with global tower every hour Devvit Action: For leaving comments when global tower is synced Other technology used: Tiled - base map for the tower Elevenlabs - sound effects Google Imagen + Photopea - Main cover of the game Credits to: @danimaccari and @adamatomic for the tileset andorios for the background music Challenges we ran into Time constraint: Initially, the idea was something similar to Agar.io. However, due to constraint of devvit server, we decided to switch the idea when there were 5 days left. We also took sometime to familiarize ourselves with Kiro. Initially, we tried Kiro "plan-first" prompt but the outcome deviates from our desired output. Hence we redo the project from scratch and made Kiro the "co-pilot" instead. Server architecture: Syncing is the major issue as we need to ensure that data is saved to backend and displayed at frontend properly without interrupting the game flow (the satisfaction when clicking) Accomplishments that we're proud of The 1-bit style visuals is exactly what we pictured when we were brainstorming the idea. We also didn't expect we manage to deliver most of the game feature that we had in our mind in such short period. What we learned How to use hooks, steering, mcp in Kiro to facilitate the process of development. Learned to use Devvit Realtime service for realtime leaderboard updates Backend syncing architecture for a clicker game that handle rapid clicks and data update What's next for Skyscrabbel Customizable tower - Add decorations to tower More levels type - Thieves academy, Inventor workshops, etc. More Upgrades - upgradeable miner/builder, clicks upgrade Assets update - Improve game background, tower presentation Milestone - Unlock events when global tower reach x floors <div