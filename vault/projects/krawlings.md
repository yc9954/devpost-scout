---
slug: "krawlings"
url: "https://devpost.com/software/krawlings"
title: "krawlings"
hackathon: "The Reddit Daily Games Hackathon"
organization: "reddit"
winner: true
words: 495
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# krawlings

> Feed in your feed! Take care of your bird and other's birds. Daily interactions and streaks grant unlockables. Explore and create hundreds of unique platformer levels!

[Devpost](https://devpost.com/software/krawlings) · hackathon [[The Reddit Daily Games Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** godot, rust, three.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for krawlings

## Body

My krawling is well fed GIF Inspiration My main inspo is the Chao garden from sonic adventure, Mario 64 and the customizability of reddit avatars What it does A virtual pet game supporting custom colors, unlockable hats, daily care-taking and social micro-interaction. For depth, immersion and recurring play, a platformer minigame with a level editor is embedded, featuring your krawling. When taking care of other birds, you can "wave" at them which comments a unique gif of your krawling. Micro interactions have designated leaderboards, to check up who's at the top of the flock! How we built it For the inline webview I am using threejs and react. The platformer game is made with Godot. For both, I am using the devvit express backend and redis. The characters are hand modelled, rigged and animated by me. Music and audio are purchases from humble and itch. Challenges we ran into Responsiveness across platforms was tricky. Also on iPhone an issue persists where the wardrobe cannot be scrolled, I don't have an iPhone to test with. Generally debugging on phone was a bit annoying which is why I added a secret dev console. I needed to squeeze as much data into the post-data as possible, for the levels. I run brotli compression on an encoded level and it works. Threejs does not offer a spring-bone system which had to be created for special hats to feel wobbly and fun. Devvit in line webviews must be fast to load, so time to first draw had to be optimized. A custom loading spinner makes the wait more fun. Godot is heavy on the web and needed a custom export pipeline and custom compiled export templates which I have made available to other participants in the devvit discord. Accomplishments that we're proud of I wanted the birds to serve as profile pictures in the ecosystem, with 1:1 correspondence on how they look like in the game. Since I can't run threejs webgl renderer on the devvit backend, I wrote my own simple raytracer to create the gifs from a threejs scene using rust and wasm-pack. Then it turned out, reddit doesn't like richtext gif embeds as a comment posted by a user. So for now, the gifs are just a link. That was a bit sad but hopefully changes in the future. A github issue is open. What we learned I learnt a lot about 3d animation and getting a character to feel "squishy". Also I have gotten much better in creating composable rigs, I haven't before created 3d characters with interchangeable pieces. What's next for krawlings I want to make the interactions between birds more meaningful and the level completion more rewarding. I am thinking of an ingame currency and gems to unlock special cosmetics and backgrounds. An XP/level up system for every micro-interaction will make your personal progression more tangible. The editor UX needs a serious overhaul as it has been mostly built from a developer perspective. <div