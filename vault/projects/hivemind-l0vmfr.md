---
slug: "hivemind-l0vmfr"
url: "https://devpost.com/software/hivemind-l0vmfr"
title: "chook"
hackathon: "Hack Reddit 2025"
organization: "reddit"
winner: true
words: 792
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/agriculture_food"
  - "substrate/video_visual"
---

# chook

> How long can reddit keep a chicken alive?

[Devpost](https://devpost.com/software/hivemind-l0vmfr) · hackathon [[Hack Reddit 2025]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[agriculture_food]]
**substrate** [[video_visual]]

**stack** amazon-web-services, lambda, node.js, react, serverless, three.js, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chook

## Body

Inspiration I tried to pick a super simple concept so that I wouldn't overscope - Basically 'how long can reddit keep a chicken alive?'. I imagined it as a collaborative multiplayer game where you'd work with others, and have a single button to feed a virtual chicken whenever your cooldowns are available, to keep its decaying hunger/health bar up and prevent it from dying. The goal is to make the chicken walk as far as possible to reach a new hiscore. (work together!!) The chicken's speed is based on its health bar, which can overclock past 100%, resulting in some gnarly speeds, and massive distance if enough players are feeding him. However I did of course end up overscoping and now it starts as an egg, walks through a field of grass, with procedurally generated terrain and trees, and there are a couple of extra buttons, stats and hiscores. What it does Players join a public game available to everyone. The game begins as an egg, with a signpost showing the time it will hatch at (typically 13 minute incubation). You can nudge the egg to reduce its time to hatch. Other players can join and help along the process. Once the egg hatches, the game properly begins, and a health bar will be added to the game screen. Players must work together to keep this bar above zero, by feeding the chicken apples, and optionally petting it to reduce their feed cooldowns. The chicken gets hungrier and its rate of health bar decay increases the further it walks. When the chicken inevitably dies, the chicken is immortalized in the hiscores, and a custom post is created with its current leaderboard ranking, the distance it walked, and the top contributors names and avatars, plus a few other stats. I designed this so that only once instance of the game would really be running ever. It would be pinned at the top of the subreddit, and perhaps be regenerated every week to keep it fresh, appear in new feeds and reset weekly leaderboards etc. How we built it I decided to create a 3d game as I hadn't seen much of that in the past for reddit. I picked threejs because its nice and lightweight and i've used it before. The entire webroot build ended up being about 5mb which i'm pretty happy with! Challenges we ran into Testing locally was a lot more difficult than I expected, I had to mock up a local backend so that i could test and develop quickly, as uploading webviews to reddit to test my game each time would be super slow. I spent a lot of time on bugs that were local only because of this :( Also! Time constraints and overscoping. I thought a month was going to be far too much time and went pretty relaxed half way through, but a massive crunch at the end. I kept adding features and changing things to get the gameplay feeling better. I found using blocks a bit of a learning curve, but it wasn't too bad once I got used to it. It took me a while to wrap my head around which parts of the devvit code were technically considered the 'backend'. I also had some issues with originally wanting a game loop, but the best I could seem to get was a 1s cron, and then instead interpolating client values to make it seem like a realtime loop. Accomplishments that we're proud of Everything above!! I'm super proud of this game and how it turned out, even though the base concept is super simple, I learned a ton and am super happy to just be completed within the timeframe! What we learned Devvit api, a bit more threejs. I used aws lambda to generate the images which is pretty cool, so its a serverless solution since that endpoint only gets hit every few minutes at most (when a chicken has died and a post needs to be generated) What's next for chook Achievements!! I'd also like to introduce 'pet goals' which are periodic target goals that popup while the chicken is alive. if the community can pet the chicken n times and reach the target, the chickens base speed will get a boost. I also added 3d in game leaderboard that get updated with 3d text and show the snoovatars in the 3d world but i ran out of time to get it fully added to a degree of quality that i was satisfied with I'd like to also introduce more personalized 'incentives' for keeping that chicken alive. the current main one is that you'll get your snoo and username put on the leaderboard. but it'd be cool to earn other prizes! <div