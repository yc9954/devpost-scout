---
slug: "rocket-ball"
url: "https://devpost.com/software/rocket-ball"
title: "Rocket Ball: Holiday Season"
hackathon: "Meta Horizon Creator Competition: Mobile Innovation"
organization: "Meta"
winner: true
words: 888
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/developer"
  - "substrate/video_visual"
---

# Rocket Ball: Holiday Season

> Rocket Ball delivers fast, high-energy 4v4 arcade soccer where every player is strapped into a giant rolling ball. It’s all momentum, teamwork, and pure arcade fun.

[Devpost](https://devpost.com/software/rocket-ball) · hackathon [[Meta Horizon Creator Competition- Mobile Innovation]]

## Facets

**user** [[developer]]
**substrate** [[video_visual]]

**stack** 3ds-max, metahorizon, substancepainter, typescript, vscode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for rocket ball

## Body

Thumnail Inspiration Being long-time fans of competitive, skill-based games, we wanted to bring our own take on a true skill-driven experience to Horizon Worlds. The core mechanics are built around a simple game of soccer — except you’re physically rolling around in a ball. We took inspiration from Rocket League, where mastery of physics and precise controls creates real competitive depth. We also see how players on Horizon Worlds form friend groups and want our world to function as a social space: somewhere players can hang out between matches, watch games from the lobby, and feel part of a community. What it does Rocket Ball is a competitive 4v4 arena game where players control themselves inside rolling, impact-resistant balls. Movement, Rocket Boosting, and aerial control are intuitive to pick up but hard to master, keeping the game accessible while still rewarding high skill. We also take advantage of player scale, allowing spectators to physically stand over the arena and watch matches like a futuristic tabletop game. It’s also a social venue: chat in the hub, hang out with friends, and jump into short, high-intensity matches whenever you like. The world is currently themed as a cosy winter cabin for the holidays, giving players a festive setting to enjoy. How we built it Rocket Ball was built with physical motion at its core. We wanted players to genuinely feel the sensation of rolling, jumping, and boosting across the pitch. The project began on the foundation we created for Hamster Ball Battle, but we expanded it heavily to support far more advanced movement. We added new systems for controlled dashing, boosting, ball-cam, team flow, and on-arena UI for both VR and mobile. For the interface, we used Noesis Studio to design and implement our UI, creating separate layouts for each platform so mobile players get a clean, readable HUD while VR players get an immersive, unobtrusive experience. We also developed an art pipeline that bakes lightmaps directly into textures instead of relying solely on Horizon’s vertex-based lighting. The pitch uses a Vertex Color material, allowing us to reuse textures across both halves while tinting them based on team color. This approach delivers much higher visual quality than Horizon typically allows while staying performance-friendly. All gameplay is written in TypeScript, and building Rocket Ball significantly deepened our understanding of both the Horizon desktop editor and the Noesis UI workflow. We also made use of Meta’s AI tools for rapid prototyping, select sound effects, and certain art elements such as the skybox. Challenges we ran into We hit several major engine-level limitations that shaped the project: Player avatars cannot be disabled. Since players are physically inside a ball, seeing their avatar clip through the shell breaks immersion. Horizon Name tags cannot be hidden, which is a problem as we have custom name tags when players are in game to match our game style more closely and because we hope to one day be able to disable avatars. Scaling players up breaks several core systems (name tags, cameras, portals), and since our spectator mode depends on avatar scaling, we had to engineer some creative fixes to keep everything working. Because we scale up avatars for spectating, the camera’s far-clipping distance became a hard limit. We had to keep the environment smaller than we wanted, pushing it to the absolute maximum the engine would allow and even rounding the room’s shape to squeeze out every extra metre of view distance. Noesis Studio bugs / limitations, especially around animation triggering and binding workflows, slowed UI development. Building for mobile-first gameplay required major adjustments to camera smoothing, controls, and performance budgeting to ensure the experience stayed responsive. We gained an audience fairly quickly and balancing our time between quality of life improvements for our players and developing new features for the competition was challenging. Developing this world is something we do alongside our full-time day jobs so its been a struggle in terms of time management and sticking to tight deadlines while also striving for the highest quality we can. These challenges forced us to get creative with presentation, physics, and UI to deliver a polished competitive game despite the restrictions. Accomplishments that we're proud of Creating a fully competitive, replayable sports experience that works fluidly on both mobile and VR. Building a social hub + arena that feels alive, not just a menu system. Achieving high-quality visuals. Expanding our physics systems into something that genuinely captures the feel of Rocket League within Horizon. Seeing a real community form around the game, with players improving, returning daily, and creating their own competitive culture. What we learned Deep expertise in the Horizon desktop editor, especially the limitations and how to creatively work around them. Stronger skills in TypeScript, physics design, UI workflows, and mobile performance tuning. A clearer understanding of how to build games that support spectatorship, social interaction, and repeat play—not just one-off experiences. What's next for Rocket Ball Rocket Ball is planned to grow into a live service experience with seasonal updates, new arenas, cosmetic progression, and in-game leagues and competitions. We’ll continue optimising the mobile experience, and we intend to port the world to the Horizon Studio Editor when it becomes available. We also plan to shape future updates around player feedback, ensuring the game evolves in line with what our community wants. <div