---
slug: "kings-over-aces"
url: "https://devpost.com/software/kings-over-aces"
title: "Kings over Aces"
hackathon: "Amazon Alexa Skills Challenge: Multimodal"
organization: "Amazon"
winner: true
words: 781
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "substrate/structured_db"
---

# Kings over Aces

> A multi-modal Alexa card game that's easy to play, yet almost impossible to master.

[Devpost](https://devpost.com/software/kings-over-aces) · hackathon [[Amazon Alexa Skills Challenge- Multimodal]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]]
**substrate** [[structured_db]]

**stack** amazon-alexa, amazon-web-services, dynamodb, javascript, lambda, node.js, ssml

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for kings over aces

## Body

Building your high score A wrong guess Checking scores Inspiration Kings over Aces is a modern take on Higher or Lower - a familiar card game that's played every day in the home, at large gatherings, parties and fundraiser events, and even on TV. What it does Kings over Aces is a card game that's easy to play, but almost impossible to master. You can play it by voice on an Amazon Alexa device or app, or if you have a compatible display device, such as Echo Show or Echo Spot, you can also enjoy the game's visual and touch interfaces, and move seamlessly between voice and display to control the game. The game is based on a simple playing card game known as Higher or Lower, Play Your Cards Right and other variants. Our dealer, Brian, turns over one card, ranging from Ace, 2, 3, 4, 5, etc. up to Jack, Queen and finally King. You start playing by guessing whether the next card turned over will be higher or lower than the current one. To do this, you simply say Higher or Lower when Brian asks for your guess. If you are correct, you gain a point and you can keep playing. You continue guessing Higher or Lower until you guess incorrectly, decide to stop (by saying Stop), or save your score if it's a good one. SCORING The game can record your Best Score, but only if you tell it to (say "Save my Score"). So that it's not too easy - saving your score also ends your current game, so to improve on it, you'll first have to equal it again! Other things that end your current game Guessing incorrectly (e.g. you said Higher and the next card was not higher) Two same-value on consecutive turns, e.g. a Four followed by another Four Turning over a Joker. However, this is extremely rare. It sounds easy, and just playing the game is indeed east. But you might find building up a really good Best Score more challenging than you think. You'll have to practice! Things to Remember Aces are always the lowest value cards in Kings over Aces, and Kings are the highest. Hence the name. Suits don't matter. The ten of hearts and the ten of diamonds are still tens. Don't get them one after the other! You can say Help at any time. Brian (Alexa) will read some instructions, and send them to your Alexa app as well for reference. If you have a display device, you'll also see a summary of commands on your screen. On your first turn, if you don't like the card you can change it , only once. Just say "Change Card". Good luck, and thanks for playing Kings over Aces . How I built it I built this skill entirely using the ASK CLI in Visual Studio Code on Macbook Pro. VScode's ask-cli extension makes this a natural environment, and the dev-test-deploy cycle is much quicker than other environents I've used, including the Alexa console and various builder tools like the now-defunct Storyline. While platforms will no doubt be used for a lot of this kind of work, I wanted full access to every feature Alexa and its APIs have to offer. Challenges I ran into I had to learn a few new techniques to complete this project. I hadn't used the APL before, and it's quickly become a large piece of the Alexa puzzle. Time learning this was very well spent however. I had to figure out a way to store users' scores in a database in such a way that if the skill became popular I had an efficient way of calculating a leaderboard, rather than having to perform large queries, which would slow the skill down. Accomplishments that I'm proud of Figuring out TouchWrappers and the rest of the touch interface from the docs... there aren't many examples or tutorials out there yet because the APL is so new. What I learned There's nothing more valuable than help from other like-minded developers. I try to help where I can and I've been on the receiving end this time because I started late in the Challenge and needed to get up to speed quickly on APL. What's next for Kings over Aces I plan to enhance the gameplay and the leaderboard so that users can see how well they're doing against players regionally and globally. If the skill proves popular, I intend to get it translated (it's only in English-speaking locales initially) and publish in the other skill store regions. I will also be looking into modularising my leaderboard - I've already had interest from other developers. <div