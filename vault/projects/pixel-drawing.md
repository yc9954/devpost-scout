---
slug: "pixel-drawing"
url: "https://devpost.com/software/pixel-drawing"
title: "Pixel Art: Doodle Dash"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown"
organization: "Meta"
winner: true
words: 822
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Pixel Art: Doodle Dash

> Run across the canvas to draw pixel art! A collaborative party game.

[Devpost](https://devpost.com/software/pixel-drawing) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown]]

## Facets

**user** [[educator_student]]
**substrate** [[geospatial]] [[video_visual]]

**stack** adobe, blender, css, customui, davinciresolve, figma, horizon, shapesxr, typescript

## How they structured the write-up

- welcome to pixel art: doodle dash, a collaborative art experience created for the meta horizons mobile genre showdown.
- how to play
- how we built it
- challenges
- custom ui
- art library
- what we learned
- next steps/future plans

## Body

Welcome to Pixel Art: Doodle Dash, a collaborative art experience created for the Meta Horizons Mobile Genre Showdown. How to Play Pick up your paintbrush and choose from a variety of timed-pixel art challenges! You and your friends race against the clock to replicate the drawing as accurately as possible by running across the Canvas. Free Draw Mode lets you draw with no time limit to create your ultimate masterpiece. We're entering Pixel Art: Doodle Dash in the Party Games category because we believe it promote collaborative fun with friends. The short 1-5 minute rounds and flexible gameplay choices enable everyone to have a fun and social experience. How We Built It We used Figma, ShapesXR, Blender, and the (Horizon) Worlds Desktop Editor to prototype and create our final project. Design and Prototyping We used Figma to store research and brainstorming. For 3D prototyping, we used Blender and ShapesXR before transitioning to the Worlds Desktop Editor. We later returned to Figma to design the CustomUI. Code The pixel art images were converted into a numerical format in P5.js, transferred to Horizon Worlds and rebuilt in TypeScript and CSS to control all elements and interactions. The Horizon TypeScript event system was particularly useful for communicating between local and server assets and Custom UI elements. Lastly, the Dynamic List was helpful in creating the image selection menu and optimizing the pixels grids. Art Direction We love the aesthetics of "lo-fi" (the music genre) and brought our world to life with a cozy color palette and 3D assets inspired by it. We later used this color palette throughout our CustomUI and video. For the music and sound design (licensed), we chose to include lo-fi, but also 8-bit to highlight our focus on pixel art. Challenges Something we're proud of: how we assessed scope and transitioned smoothly from research to prototyping in a timely fashion (as designers, we often get caught up in research). That being said, we still faced plenty of technical challenges, including version control, code merge conflicts, importing assets (Sarah confesses: it took an embarrassingly long time to learn to import a Custom Model), optimization, and more. However, the biggest challenge of all: The Color Matching Fiasco: The Challenge that Almost Ended Our Project The drawing Canvas was not always a CustomUI. For the majority of the project, it was actually an array of quads, each tinted to match a corresponding pixel in the reference image. In the final week of the project, we discovered that all colors were washed out/muddy, and most importantly: not matching our pixel art at all. For a color-matching game, this was a pretty big issue. We discovered this occurred even on Unlit objects, and was likely limitation of how Tint is calculated for most colors. To circumvent this limitation, we turned the drawing Canvas itself into a Custom UI ensuring all colors were displayed as precisely as possible. This had a performance impact, but we feel that accurate colors are the most important feature for players to succeed at our party game . Custom UI We used CustomUI for everything: the Tutorial Sticky Notes, Pixel Art selector, Stats Display, and even the drawing grid ("Canvas") itself. In short, our project is only possible because of CustomUI, especially because it allows for perfect color accuracy. We combined the CustomUI with background assets designed in Figma so we could have a higher degree of customization. Additionally, this allowed us to develop the code and visuals for the UI simultaneously whilst avoiding merge conflicts. Art Library 30+ (and counting) original pixel illustrations, featuring cute animals, delicious food, and suggestions from the community. What We Learned User (and Platform) testing Although we tested frequently on Horizons in-browser and in-editor, we realized we did not spend as much time testing on Mobile as we should have. Trust and Collaboration Throughout the challenge, we often had individual, sporadic schedules, so we had have self-accountability, and trust in eachother to deliver on our respective expertises. Technical Upskilling This was some of our team's first time using certain tools. Some highlights: Using the Worlds Desktop Editor for the first time Kate's first time prototyping for Horizon Worlds Learning CustomUI Sarah learning CSS John's first time on Figma! First mobile game! Next Steps/Future Plans Progression We already track (and display) per-game and lifetime stats! We want to implement a progression system so you can unlock exclusive art and customizations based on your achievements. Self expression We'll be adding cosmetic options, so players can choose between drawing with a brush, pen, pencil... or rocket ship? Themed releases Do you like sea creatures? Outer space? Cars, trains, and planes? We plan to release sets of themed pixel art, celebrated with customization options (maps? hats? stickers?) that match the theme. Optimization There is some drawing delay as a result of heavy CustomUI usage, especially when the maximum number of players are drawing. We hope to decrease the latency. <div