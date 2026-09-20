---
slug: "quizzex-realtime-quizzes"
url: "https://devpost.com/software/quizzex-realtime-quizzes"
title: "Quizzex - Realtime Quizzes"
hackathon: "Zero to One Hackathon by Convex"
organization: "Convex"
winner: true
words: 676
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# Quizzex - Realtime Quizzes

> Play fun games with other players in REAL TIME right in your browser! Choose from a selection of games, join or host an online, real time battle, and look back on your victories!

[Devpost](https://devpost.com/software/quizzex-realtime-quizzes) · hackathon [[Zero to One Hackathon by Convex]]

## Facets

**mechanism** [[realtime_stream]]

**stack** convex, react, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for quizzex - realtime quizzes

## Body

Main Thumbnail Home Page List Battle Trivia Battle Unravel Battle Result Profile Page Inspiration When I saw one of the categories for this hackathon was "Multiplayer App" and that Convex is all about real-time updates, I knew I had to make a game out of Convex. Making online battle-style games on the browser where the players are actually participating in real-time concurrently has always interested me. This is why I made Quizzex. What it does Quizzex is a center for online games where players/users can battle each other virtually in real time. This means all participating players in a game/battle will actually be playing at the same time. I have made a few selections of real-time games, which are: List Battle Two players are given a category, and they will simultaneously attempt to list things that fit in that given category. Whoever racks up the most points before the timer runs out will win. Trivia Battle Two players will fight to answer a series of trivia questions given randomly. Whoever answers correctly the most will win. Unravel Battle Two players are given a hidden word. They take turn. They can either guess a character or guess the whole word. Whoever guesses the real word will win! Battle structure On each "battle page" there will be three distinct panels: Main panel: this will be the main content of the battle will be. For example, on trivia battles, this will be where the question goes. PLAYER panel: this will show general information about the game and the player, for examples the timer and how many points the player currently has. Opponent panel: the opposite of the player panel. Only this time it will be about the opponent. For example, how many points the opponent currently has, and, during list battles, how many items they have guessed. This panel will be vague to avoid cheating. All of these panels will be updated in real time as user actions are performed by either players. How we built it Building this was a lot of fun, having been provided with Convex's convenient real-time features. This was especially useful during particular parts of development, namely implementing the turn-based aspect of the Unravel Battle game and implementing a fair timer for all players. Generally, developing was very straight-forward, as I never had to think about updating the UI after a certain action has been performed by either player, which is a very important aspect in an online battle game. So I was able to focus on making the ideas I had for real-time games come to live. I mainly used Convex's queries and functions. I used queries to fetch "battle" data so that any action performed by participating users will immediately be reflected in all participants' screens. And to perform those actions, I used mutations. Challenges we ran into I unfortunately started this 2-month long hackathon very late. I only started brainstorming 7 days before the deadline. So a major concern for me was having to read and learn the docs in a very short time-span. However, the docs were very clear, and the React template provided many useful examples. Though I had a short development time, I managed to develop at least the main ideas I had for Quizzex. Accomplishments that we're proud of Overall, I'm really proud to have made 3 functioning reactive games in a short span of time. I learned a great deal in designing for live games. It was very fun figuring out optimal schemas that would best fit real-time games like these. What's next for Quizzex - Realtime Quizzes As mention, I didn't get a lot of time to further develop my initial ideas during the submission period. However, I'm going to list them here: User-generated content: Users will be able to create their own lists and trivia questions. A rating system will be implemented to prevent bad actors from creating bad/malicious content. Invite codes: invite specific players to a game by giving them battle codes More game types: family-feud style games, codenames, etc Follow/friends system <div