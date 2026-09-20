---
slug: "rankkit"
url: "https://devpost.com/software/rankkit"
title: "Hightier"
hackathon: "Hack Reddit 2025"
organization: "reddit"
winner: true
words: 828
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/video_visual"
---

# Hightier

> Elo-based Tier List Battleground where submissions face off in head-to-head battles for the glory.

[Devpost](https://devpost.com/software/rankkit) · hackathon [[Hack Reddit 2025]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[video_visual]]

**stack** devvit, emotion, motion, react, redis, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for hightier

## Body

Feed call to action Real-time tier list changes User achievements Tier list modal Head to head battles Real-time activity feed Inspiration When r/place launched during 2017 April Fools' I was awe-inspired and that experience has stayed with me ever since. When Reddit announced this Hackathon I decided to take the leap and learn Devvit and make something April Fools-ish. That is, a massively multiplayer experience where communities can come together and share an experience. I ended up creating an app that I'm calling Hightier . What it does Hightier is an Elo-based Tier List battleground where every vote has a real and lasting effect on the final rankings. Submissions face off head-to-head where one gains Elo for winning, while the other loses. Getting past a certain Elo threshold ranks up the submission. For this hackathon I decided to focus on the Fighting Game community and the Comic-book/Superhero fanbase, where the "battleground" concept fits perfectly. Hightier could of course also be used for non-literal battlegrounds, where, for example, TV shows or books fight head-to-head for the S-tier. How I built it Hightier was no small feat since I didn't know anything about Devvit going in. It was born as a prototype using "Blocks" but before long the app graduated to Web Views, which offered me the tools to build a richer experience capable of complex animations and layouts. Challenges I ran into So. Many. Challenges. Performance and User experience I set myself a goal of <100KB gzipped final bundle and wanted to keep external dependencies to an absolute minimum, which was a challenge. Once I had designed an acceptable user experience in Figma I realized that I needed a couple of tools to realize my vision: React, Motion (animation engine) and Emotion (CSS-in-JS). Those three dependencies got me through to the finish line but pushed me slightly over my 100KB target. This meant I had to (ok wanted to) write everything else by hand. Timers, modals, popovers, tooltips etcetera. Balancing the Elo scoring system Creating a well-balance Elo scoring system was tricky to get right. Imbalanced and unfair matchups need to affect Elo minimally and the Tier shifting thresholds need to be well balanced. There exists a nice middle ground where it's not too difficult and not too easy to move between tiers which I hope I have found. Redis Although I'm most comfortable in the front-end, I had some Redis experience. Not having access to all Redis commands was a difficult challenge but in the end I loved the minimalism and performance that I got from these constraints. Real-time I knew my app would need to push real-time to the limits for the experience to feel "social". Everything updates in real-time. From the blocks view to the web view - the Elo, the feed, the achievements (which I call milestones ) and the battle counts had to update simultaneously and instantly to satisfy the original vision. Submissions Authoring a tier list means preparing hundreds of images in the correct size and making sure they are compressed as much as possible without losing fidelity. I originally thought I would let the users create the submissions, but when I saw how much art direction was involved with making everything look and perform nicely, and how good the mod tools needed to be to prevent spam and indecent entries, I took a step back. In this version of the app all submissions are mod submitted through a mod-only submission form. Accomplishments that I'm proud of I set out with a certain vision and I'm extremely proud of how close this Hackathon version is to my original vision. The app is simple to use, simple to grasp and, I must say, a pleasure to use. If I had another week or two I would polish the animations' look and feel, timings and easings, but it's still very close to what I set out to do. I have a 13 year old son that is very much into superheroes, so I made the first Hightier post be "Comic Book Superheroes". The feedback I got was "Dad, this rocks!". What I learned My original goal was to learn Devvit and have fun. I learned it and I had so much fun. I also got a lot more comfortable with Redis which I'm happy about. What's next for hightier I'm full of ideas. Make each Hightier post have a (custom) time limit. I can envision the final hour being frantic, as people try to get their favorites to the highest Elo. As it stands, the posts stay live forever. More mod tools. Make it easy to change a submission name (fix typos), change a submission image, ban malicious users and revert their effects on the tier list. Make the app installable on other communities, give communities the power to customize the app to their liking: the colors, copy writing and milestones. Experiment with Reddit Gold where users can put "medals" on their favorite submissions. <div