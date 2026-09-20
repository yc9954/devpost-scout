---
slug: "play-pi"
url: "https://devpost.com/software/play-pi"
title: "Play-PI"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 399
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
---

# Play-PI

> Fancy a game of chess in the postman app?

[Devpost](https://devpost.com/software/play-pi) · hackathon [[The Postman API Hack]]

## Facets

  <sub>weak: web_dom</sub>

**stack** css, handlebars.js, html, javascript, postman

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for play-pi

## Body

Chess in play Minesweeper - losing :-( Minesweeper - winning! Chess instructions response Minesweeper instructions response Inspiration I have always loved using postman, and it seems to be becoming more and more powerful with every new feature. I figured I'd like to try something different, so I posed myself question... Can I play chess using postman?? This turned out to be very possible, so it turned into more of a challenge. The idea is that the community can use this workspace to see what they can create, finding new things they can do through experimentation. Hopefully it will allow extra creativity to flow into their use of postman for more serious API's and use the visualization tools to help their collections be understood. What it does It's one thing to create a game of chess over API. I wanted to do more than that so I set some rules: It should be easy and pleasant to play It should visual and pretty It should prioritize postman features over javascript and other non postman tools It should use a third party API and highlight it's use so people are aware of it. How I built it It took a lot of experimenting, but utilizing the handlebars template language and postman's powerful API I was able to implement any of the features I wanted. Challenges we ran into Making it easy for people to understand how to use and play the games was always going to be difficult. I decided to take advantage of postman's mock servers to provide instructions as a response, and handle the call to the API in pre-request scripts. Now that's obviously not how you are supposed to do things but this is a hack afterall :-) Accomplishments that we're proud of I really like how easy it is to understand what's going on because of the friendly responses you get when making a call. And the fact postman's visualizer works so well meant I could create some pleasing graphics for the games. What we learned I learnt a lot about the postman API and how flexible the application is in terms of what you can do. What's next for Play-PI I'd like the community to take on the challenge of creating some crazy things in postman. It's less about the games and more about saying, "Hey, did you know you could do this in postman??" <div