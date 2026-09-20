---
slug: "capybara-cafe"
url: "https://devpost.com/software/capybara-cafe"
title: "Capybara Cafe"
hackathon: "Meta Horizon Creator Competition: Short Loop Mobile Worlds"
organization: "Meta"
winner: true
words: 629
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/supply_logistics"
  - "substrate/video_visual"
---

# Capybara Cafe

> Serve snacks, explore, and care for adorable capybaras in Capybara Café! Play solo or with friends on mobile or VR, combining fun challenges, teamwork, and relaxation in a magical forest world!

[Devpost](https://devpost.com/software/capybara-cafe) · hackathon [[Meta Horizon Creator Competition- Short Loop Mobile Worlds]]

## Facets

**domain** [[supply_logistics]]
**substrate** [[video_visual]]

**stack** 100%typescriptcode, adobesubstancepainter, blender, horizon, horizontypescriptcameraapi, horizonworlds, meta, metahorizon, metahorizondesktopeditor, quest, quest3, questpro, typescript, vscode

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for capybara cafe

## Body

Inspiration Capybara Café was inspired by the global love for the wonderfully chill, meme-worthy creatures. With their calm, quirky charm and natural ability to spark joy, capybaras felt like the perfect stars for a wholesome, feel-good game. But this project wasn’t just about celebrating the internet’s favorite giant rodents—it was also a personal quest. I wanted to reimagine a memory-recall, time pressure game, transforming it from a source of stress into an opportunity for joy. The idea? Make rushing to complete tasks not just bearable but genuinely fun by tying it to the happiness of our adorable capybara friends. At its heart, the game taps into the player’s empathy and nurturing instincts. What it does Capybara Café is a cozy mobile and VR game where you serve treats to adorable capybaras in a magical forest retreat. Race to complete orders, collect rewards, and tackle fun challenges that test your speed and memory. Play solo or with friends to explore, compete on leaderboards, and share the joy of making capybaras happy! How I built it The game was built with Blender, Adobe Substance Painter, Meta Horizon Desktop Editor, and 100% Typescript code. Typescript Camera API was used to optimize the mobile experience. Mobile player’s POV changes to 1st person view inside the cafe to make it easier to find and grab snacks. The POV changes to 3rd person orbit view once the player leaves the cafe. This view makes it easier to roam between capybaras and explore. Typescript is also behind the Mobile UI in this game. Mobile players are exposed to a robust UI inventory - up to 5 snacks that a player can carry at a time. The UI also shows the remaining time, number of remaining capybaras that need to be fed, and player’s xp. Avatar collapse animation is used when the mobile player runs out of time. VR players use a more subtle, unobtrusive HUD, and important game notifications are sent via popups. Challenges I ran into The main challenge in Capybara Cafe was to learn how to bifurcate mechanics based on the player’s device type and how to utilize the Typescript Camera API to optimize the experience for searching and grabbing items inside the cafe and for roaming outside the cafe. The bifurcated mechanics had to account for VR players grabbing and handing the snacks to capybaras with their hands, while Mobile players loading their trays with up to 5 items and delivering snacks by simply getting close to their customers. Designing the UI inventory system that allows a mobile player to fill 5 available spots with an infinite combination of snacks was a fun undertaking. Accomplishments that I'm proud of It was a fun challenge to design a game where VR and Mobile players could play side by side in a memory recall and speed competition. At the end I feel that Capybara Cafe makes for quite an organic experience that is satisfying to both groups. I feel that the work that went into character rigging and animation also paid off. There’s something undeniably rewarding about seeing a capybara’s contented smile, knowing it’s your effort that made it happen. What I learned I feel much more comfortable building engaging experiences with bifurcated mechanics that appeal to both Mobile and VR players. Learning the Typescript Camera API was very rewarding. I am looking forward to making more Mobile/VR experiences in Horizon Worlds. What's next for Capybara Cafe The main next step is to track the user experience and tweak the difficulty level of the game to make it both challenging and fun. Additionally, upcoming features will be unlocking special café items, and secret cafe areas for VIP/top players. Eventually, I’d like players to be able to serve not just capybaras but also other players. <div