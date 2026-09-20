---
slug: "meeple-buddy"
url: "https://devpost.com/software/meeple-buddy"
title: "Meeple Buddy"
hackathon: "Alexa Skills Challenge: Alexa Conversations"
organization: "Amazon"
winner: true
words: 1003
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# Meeple Buddy

> Meeple Buddy helps tabletop gaming enthusiasts decide which game to play. Add games to your collection, then ask Meeple Buddy to pick a game for your based on the number of players and complexity.

[Devpost](https://devpost.com/software/meeple-buddy) · hackathon [[Alexa Skills Challenge- Alexa Conversations]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[structured_db]]

**stack** ask, conversations, javascript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for meeple buddy

## Body

Meeple Buddy in Action Inspiration I am a tabletop game enthusiast and like to play tabletop games with my family and friends as often as I have opportunity. But the one challenge we always have is deciding which game to play. Nobody wants to commit to any specific choice and generally says "I don't know, you pick." But then when I pick a game, they're not sure that's what they want to play. I needed a better way. What it does Meeple Buddy solves the problem of what game we will play. Using Meeple Buddy, I can load games that I own into my Meeple Buddy "game collection". Then whenever we're ready to play a game, I can ask Meeple Buddy to find a game given the number of players and a complexity (easy, medium, difficult, or any). Meeple Buddy will pick a matching game from among the games in my collection and suggest it for us to play. How I built it I developed Meeple Buddy as an Alexa-hosted skill, using the new Alexa Conversations to drive the dialogs for adding games and picking games. Because I also intend to support conventional request handlers in this skill for other purposes later, I'm not using Conversations as the default dialog manager, which means I needed to delegate between standard intent handlers and Conversations. I did much of the work in the browser-based forms and code editor, despite the fact that I typically prefer working completely local with VSCode to edit all skill artifacts. I chose to work in the browser-based forms, however, for two reasons: To gain the experience of working in that model and because on at least one occasion my attempt to deploy my code via the ASK CLI broke my interaction model underlying my Conversations model. Challenges I ran into The biggest challenge I faced was that there is no way of defining a Conversations model in JSON or some other data structure outside of the developer console. I found working in the browser-based forms cumbersome. But even more troubling is that because there are no file artifacts associated with the Conversations models, there was no way to manage my work in source code control and thus no way to roll back my work to the last known working state when I made mistakes. Another huge challenge that I faced is that when there are two or more slots of the same type and similar utterances being gathered in the course of a dialog, there exists ambiguity and the answer to one prompt might populate the wrong slot. For example, in my skill a game can have a minimum and maximum number of players, both expressed as slots of type "AMAZON.NUMBER". While I can define utterances for each to avoid ambiguity (e.g., "at most {maxPlayers}" or "no less than {minPlayers}"), it's more likely that the user will simply answer with a number, requiring me to define utterances such as "{minPlayers}" and "{maxPlayers}". Since both are of the same type, the utterances are ambiguous. I found that when Alexa would request the maximum number of players, both the minimum and maximum slots would be filled with the same value. I worked around that issue by creating request-args slots that asked for both minimum and maximum to be given in a single utterance (e.g., "{minPlayers} to {maxPlayers}"). This works, but occasionally, it will ask for the number of players twice (I presume that it's once when the dialog is requesting the minimum and once when requesting the maximum). This is non-ideal, but based on discussions in the Slack channel, there appears to (at least for now) be no other way. I also found it inconvenient that I couldn't test the Conversational part of the skill using ask dialog . And there were several other minor challenges, such as how to ensure that the session is closed after the dialog completes, but I found help for those things in the Slack channel. Accomplishments that I'm proud of Quite simply, I'm proud that I was able to build a complete and useful skill using Alexa Conversations in spite of the aforementioned challenges. I'm also proud of the fact that as I was developing it, I demonstrated my work to my non-technical friends and family and I could see their faces light up---they "got it" and could see how this skill would be useful. What I learned The most basic thing I learned was how to work with Alexa Conversations and to see its potential for future projects. What's next for Meeple Buddy There are several things I have in mind for Meeple Buddy going forward that just didn't make it into the version that was submitted for the challenge. These include: Creating a database full of tabletop games to draw upon so that if the user wants to add a known game to their collection, they can bypass the dialog that prompts them for complexity and minimum/maximum players. The Conversations-based dialog created for the challenge would still come into play for games that are not known in the database. Although I did some minimal APL so that users with screen-enabled devices wouldn't be looking at a blank screen, I have bigger plans to make those screens more animated and interesting. Perhaps showing box artwork for the suggested games. I would like to add a way of recommending games to users based on the games in their collection and possibly offer them for purchase through the skill. This might be tricky, however, because as far as I know, there's no way to sell Amazon-fulfilled products through custom skills. (I could be wrong.) I'd like to consider a way of treating game expansions as separate concepts to the base games and provide some useful interactions for choosing which expansions to play with a game, if there are any available for the chosen game. As I created the video for submission, I discovered several opportunities to improve the interaction model that I didn't catch while testing. <div