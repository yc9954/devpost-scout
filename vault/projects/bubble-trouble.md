---
slug: "bubble-trouble"
url: "https://devpost.com/software/bubble-trouble"
title: "Bubble Trouble"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 502
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# Bubble Trouble

> Cat Shower: You've got to be kitten me.

[Devpost](https://devpost.com/software/bubble-trouble) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

  <sub>weak: realtime_stream</sub>
**substrate** [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** bolt.new, css, html, javascript, reddit, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bubble trouble

## Body

Start Screen – Game title, start button How to Play – Instructions, cat types, and game mechanics Main Gameplay Screen – Real-time bath scene with chaotic controls Inspiration Our inspiration came from a place of shared, universal frustration and mild terror: trying to give a cat a bath. Anyone who has ever attempted this knows the deal. You start with a cute, fluffy companion, and within seconds, you're wrestling a furious, water-averse demon with razor-sharp claws. We wanted to capture the sheer unpredictability and absurdity of this experience without anyone getting hurt. The "Useless Sh!t Challenge" felt like the perfect home for an idea that had absolutely no practical value but was deeply relatable and, most importantly, funny. What it does The bubbletrouble is a chaotic bath-time game where you try to keep a cartoon cat clean — but the controls have a mind of their own. After each round, players see how long they lasted, where they rank in their continent, and how their continent stacks up globally. They can share results straight to Reddit, fueling memes, rivalry, and chaotic fun beyond the game. How we built it We built this project with a focus on speed and simplicity, using two core components: Bolt.new : The entire frontend and application logic were built using Bolt.new. Its rapid-prototyping environment allowed us to go from concept to a working application very quickly. Reddit API : To get an endless supply of unpredictable cat reactions, we integrated the Reddit API. The app calls specific subreddits (like r/cats , r/catmemes , and r/angrycatpics ) to fetch a random post. Challenges we ran into Filtering API Content : Ensuring fetched content was always relevant and SFW required refining API calls and building robust error-handling logic. Designing for "Uselessness" : Creating a UI for an intentionally pointless app while conveying its chaotic/humorous tone was a unique challenge. Feature Creep : Resisting the temptation to add scores, levels, or tools to maintain the core joke and beautiful simplicity. Accomplishments that we're proud of Successfully turning a simple, funny idea into a functional and stable app that gets laughs. Clean integration with the Reddit API, forming the backbone of the game's unpredictability. Creating something purely for fun—a project that doesn't take itself seriously and exists only to provide relatable humor. What we learned Rapid prototyping and deployment using Bolt.new . Valuable hands-on experience integrating and handling the Reddit API (authentication, data parsing). The most engaging projects aren't always the most complex; a simple, relatable joke can be powerful and memorable. What's next for Bubble Trouble While the beauty of the app is its simplicity, we have a few "useless" ideas: "Shampoo" Selector : Different "shampoo" options pulling images from specific subreddits (e.g., "Calming Lavender" → r/sleepingcats , "Angry Chili" → r/angrycatpics ). The "Dryer" Mode : A second button showing a GIF of a very fluffy or static-filled cat. Reaction Leaderboard : A meaningless leaderboard ranking users based on an absurd algorithm determining the "type" of cat reaction. <div