---
slug: "let-me-cook-m3ry50"
url: "https://devpost.com/software/let-me-cook-m3ry50"
title: "Let Me Cook!"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown"
organization: "Meta"
winner: true
words: 673
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Let Me Cook!

> Play this multiplayer cooking sim where trial and error is on the menu. Chop and throw it in the pot! Prove your skills in the kitchen and CLAIM YOUR PRIZE!

[Devpost](https://devpost.com/software/let-me-cook-m3ry50) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown]]

## Facets

**mechanism** [[simulation_digital_twin]]
**substrate** [[structured_db]] [[video_visual]]

**stack** blender, google-sheet, metahorizonworldsdesktop, photoshop, pro-tools, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for let me cook!

## Body

Inspiration I’ve always been a fan of simulation games, and I love cooking through experimentation. So I combined the two! No matter the culture or the dish, celebration often happens around a shared meal—and I wanted that feeling of community and discovery to be the reward for culinary exploration. My goal was to maximize the number of recipes players could discover, and I’m proud to say I met that goal. Playing the Sims growing up, I learned to appreciate a skill progression built around learning and unlocking. With that in mind, I created a progression that allows you to unlock more ingredients and recipes the more you cook, eat and clean. What it does Let Me Cook is a multiplayer cooking sim where trial and error is the main ingredient. Players grab ingredients from the pantry and test different combinations at cooking stations to see what they create. Need a hint? The cookbook includes 40+ discoverable recipes. When players land on a successful combo, the result is a serving dish they can plate up and enjoy together at the dining table. Game Loop Mechanics [ ] Pick from a selection of ingredients that alternate each day [ ] Chop ingredients that require some prepping at the chopping board [ ] Cook up ingredients starting with the outdoor cooking pot and progressing to the stone oven [ ] Serve up your successful meals and celebrate by sharing with friends [ ] Eat at the round table as you chat with friends [ ] Compost any leftovers [ ] Clean up empty dishes and you're ready to do it all again! How we built it I created all the assets in Blender and used vertex colors to hand-paint them—helping optimize performance by reducing texture load. All scripting was done in TypeScript to take full advantage of mobile features. I designed the scripts to be modular, allowing multiple items to behave slightly differently based on context. UI elements and the game logo were created using Photoshop. That, along with extensive recipe planning in a spreadsheet, made the large number of recipes possible. Challenges we ran into The kitchen layout started as a VR art challenge, which presented navigation/flow issues on mobile. To address this, I added a fast travel system and gave players an apron. The apron enables instant pantry access and allows mobile users to carry up to three ingredients—bypassing the one-item grab limit on mobile interactions. Accomplishments that we're proud of Learning how to implement mobile-focused interactions was a huge win. Many of the features were new to me and required lots of trial, error, and research—but they’re now some of my favorite parts of the game. I’m excited to continue refining and building on them. What we learned This project was a deep dive into mobile-first development. I had to understand and work within the limitations of mobile interaction systems, which made every feature—from picking up items to navigating menus—a learning opportunity. I also learned how to create cutscenes using the camera API and leveled up my UI skills. The final result includes a scrollable recipe list, a Q&A-based "How to Play" section, and a dynamic pantry display. What's next for Let Me Cook! Players earn a currency called Threads as they play. They can currently collect their Threads from a dispenser outside of the Shop. Soon, they’ll be able to visit the in-game shop, and use their Threads to purchase cosmetic items like aprons and chef hats. The goal is to keep expanding both the gameplay and the sense of personality and customization in the experience. If this world does well, I'd like to make it a series of worlds and refine the layout and game loop of this initial world more. New TS features came out (like the bounding box functionality) that would improve some of the mechanics I had already built from scratch (like the plate stacking mechanic). Given more time, I'd like to update the logic to use these new features, but time did not allow for it. <div