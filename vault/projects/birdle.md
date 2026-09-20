---
slug: "birdle"
url: "https://devpost.com/software/birdle"
title: "Birdle"
hackathon: "Chirp Developer Challenge"
organization: "Twitter"
winner: true
words: 524
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
---

# Birdle

> Birdle puts a new perspective on the day's tweets - it turns them into a game. It turns otherwise uninspiring tweets, into a message that is inspiring and uplifting.

[Devpost](https://devpost.com/software/birdle) · hackathon [[Chirp Developer Challenge]]

## Facets

**substrate** [[structured_db]]

**stack** google-cloud, nextjs, storybook, supabase, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for birdle

## Body

GIF Inspiration I was inspired by the success of Wordle and the newfound popular interest in shareable word games on the web. I got the idea for this project when I was browsing my Twitter timeline and realised that, particularly when it comes to news accounts that I follow, the impact on my state of mind was generally negative. I began to see if there was a new way to put a spin on the traditional timeline that would leave you with a positive or inspiring message that you can carry with you during your day, and in the meanwhile, introduce you to new Twitter accounts that you might not follow yet. What it does On a daily basis, uses the Twitter /search API to grab a bunch of the day's tweets from the preceding 24 hours. It then runs an algorithm on those tweets that selects 4 of them, removes one word from each such that the missing words collectively spell out a mystery phrase. That phrase is deliberately uplifting and inspiring! The puzzle is then presented every day in the form of a web app: https://birdle.art How we built it Next.js for the client localStorage API to save user's daily state Supabase (a cloud-based Postgres service) to store and manage: daily Tweets list of verified user accounts to get Tweets from list of possible "mystery phrases" metadata about the day's puzzle Google cloud scheduler to manage daily CRON jobs Challenges we ran into using user's local storage as a potential source of truth in addition to the main SQL database, particularly when it comes to server-side rendering and hydration on the client ensuring that the "daily mystery phrase" does not repeat on consecutive days ensuring that it works well on mobile testing, given that the app is reliant on window programmatic scroll behavior (e.g. scrollTo() API is not implemented in JSDOM) Accomplishments that we're proud of Posted on HackerNews and stayed on the main ShowHN page for a few consecutive days Got some great comments like: "Really good animations! Hoping we can play past games or at least generate new phrases after completing the day's puzzle because this is somewhat entertaining and dopaminergic for some odd reason." "Cool idea. I wish I could be notified when tomorrow's game is ready." "Wow! I really enjoyed it. Hoping to play more." Amplitude tells me I have a regularly returning cohort of ~10 users daily across USA, Australia, India, NZ What we learned how to build a comprehensive suite of E2E tests using Storybook ( https://storybook.js.org/ ) the caching solutions provided by Next.js / Vercel, which meant that my Postgres instance is not hit more often that needed What's next for Birdle enhanced "shareability": right now the share text mimics Wordle but I think that that Twitter-based nature of this puzzle has more potential for interesting sharing options currently there is a limited list of Twitter accounts that the daily Tweets are grabbed from: I would like to expand this to feature a more diverse array of voices. I have an "admin" app that somewhat controls this, but I plan to develop this further. <div