---
slug: "golfddit"
url: "https://devpost.com/software/golfddit"
title: "Golfddit"
hackathon: "Reddit and Kiro: Community Games Challenge"
organization: "reddit"
winner: true
words: 397
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# Golfddit

> Build-your-own arcade golf game.

[Devpost](https://devpost.com/software/golfddit) · hackathon [[Reddit and Kiro- Community Games Challenge]]

## Facets

**substrate** [[video_visual]]

**stack** express.js, kaplay, react, redis, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for golfddit
- acknowledgements

## Body

Sample course 1 Sample course 2 Level editor Level editor (empty) Try it for yourself! Subreddit Inspiration The inspiration for this game was Pixelary, a cool pixel art style drawing game. Redditors are given a prompt and draw pixel art for other Redditors to guess what the prompt was. What it does Golfddit is a build-your-own arcade golf game for Reddit. Redditors can build their own golf courses, play other Redditor's golf courses, and compete on the leaderboard for the best score. Features Building your own golf courses. Playing other users's golf courses. Leaderboard system per golf course. Remixing other user's golf courses. Mobile-first design with touch friendly controls. Seamless experience. Can play directly on the page. How we built it Frontend (ReactJS + Kaplay) Used ReactJS + Kaplay (game library) for displaying the game canvas and multiple pages (game, build, leaderboard, etc). Backend (ExpressJS + Reddit API + Redis) Course information is saved in the postData of each post. Leaderboard information and stroke stats for each course is saved in Redis. Challenges we ran into One of the biggest challenges when building this project is designing the game to be mobile-first and trying to fit as much information as possible in such a tiny space. What's next for Golfddit Features Add audio and audio controls. Post courses under Redditor's username and allow course author to add custom messages on course start. Replay system with a "ghost" ball, so you can compete with previous Redditors that have completed a level. Being able to search for your own and other user's courses within the app. Add more block and floor types (i.e. trampoline wall, moving walls, etc). Live play with other Redditors/friends. Global leaderboard or leveling system for who played the most courses, who made the most strokes, who made the most popular courses, etc. Polish Between page transitions. Add loading icons and error toasts when doing long running tasks like submitting a course or submitting a score. Make the UI more understandable for first-time users. Some users I tested the game with got confused on the "Build your own course!" screen. Fix the preview image generation. Fix some collision issues with the ghost block. Acknowledgements Thank you DeJotaK for the block pixel art. https://dejotak.itch.io/8bit-autotile-platformer-blocks Thank you Isaac T, Justin J, Hardeep B, and Bryant Z for helping me test out the game and giving me feedback. <div