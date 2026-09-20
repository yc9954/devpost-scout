---
slug: "in-game-hype-trains"
url: "https://devpost.com/software/in-game-hype-trains"
title: "Ride the Hype Train (Literally)"
hackathon: "Twitch Streamer Tools Hackathon"
organization: "Twitch"
winner: true
words: 461
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
---

# Ride the Hype Train (Literally)

> All aboard! Reward Hype Train supporters by featuring them on an in-game train using Crowd Control!

[Devpost](https://devpost.com/software/in-game-hype-trains) · hackathon [[Twitch Streamer Tools Hackathon]]

## Facets


**stack** amazon-dynamodb, c#, lambda, sst, typescript, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ride the hype train

## Body

Inspiration Bringing Twitch events into games has been something the Crowd Control team and I have been passionate about for years. We've been recently thinking of new Twitch-centered interactions and ways for them to be triggered and figured that a train in a game is a perfect way for the creator to stay informed of a Twitch Hype Train happening while bringing a new level of interaction to their streams. What it does When a Hype Train is activated on a Twitch channel and they are playing a supported game, a train will spawn in the game along with the top contributors names and what they've done to contribute to the hype train! The level will determine the speed of the train, so as the hype train grows, the train becomes faster! How we built it It's a mix of Twitch APIs using the Twitch Event Sub on Hype Train events, and our own backend code for Crowd Control to determine active sessions playing the supported games. We also built a custom Unity Project that we're able to add to our existing Crowd Control mods that will make it easy to bring this asset into other games to extend the reach this can have. Challenges we ran into Bringing scripts and 3rd party assets into an existing game can have issues if you're unable to match the exact settings, and versions for the project. Building our Unity asset to work with multiple version of Unity, and rendering methods was a bit of a challenge that we ran into but we've been able to get it into many multiple games now and are working on stylizing the asset to match more with those games aesthetics. Accomplishments that we're proud of Accomplishing this with a short timeframe between other projects ending and starting. We only had a limited time to work on this, and the goal was to get it 3 games supported within a week after the vision for the idea so that it could be done in time for submission while still giving users time to test it out and provide feedback. What we learned Bringing more interactions like this into more games is something we're going to explore with other Twitch events including raids, gift subs and more. Every chat that we saw this triggered in saw increases in bits and subs after the first train, which really showed off the power to of bringing viewers together. What's next for Ride the Hype Train Bringing support to more games in our library of over 150+ games, making hype trains a new staple that we try to have for each new game as. As well as adding customization options for train settings like personalized sound effects, and additional asset spawning. <div