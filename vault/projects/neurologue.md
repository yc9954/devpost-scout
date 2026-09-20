---
slug: "neurologue"
url: "https://devpost.com/software/neurologue"
title: "Neurologue"
hackathon: "Hack the Northeast"
winner: true
words: 652
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/sensor_telemetry"
---

# Neurologue

> Neurologue - The Game That Plays You

[Devpost](https://devpost.com/software/neurologue) · hackathon [[Hack the Northeast]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[sensor_telemetry]]

**stack** emotiv, html5, http, javascript, json, mspaint, node.js, npm, phaser.js, websockets

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for neurologue

## Body

Game Menu First Scene Scene with Multiple Choices Sprites of main characters "The Psychiatrist" (above) and "Peter" (below) Flowchart of part of the story tree The good ending of the game Inspiration As we were all interested in psychological thrillers and interactive games that engage the player a lot, we decided to go into this theme adding our own twist to it. We believe that the problem with interactive games is the lack of real human connection. The player's character does not act as a true representation of the player, as some interactive games try to do. Passionate about neuroscience, we found a perfect way to combine this with the game design. What it does Neurologue is a psychological horror choose-your own-adventure game that follows the player's meeting with a slightly philosophical psychiatrist. Unlike traditional video games, the characters in Neurologue can sense exactly how the player is feeling in real-time. Using an electroencephalographic brain-computer interface, the game reads 7 major physiological metrics that determine the way that characters interact with you, the effect of your choices, and who you are as a player. Whether you are excited, focused, or relaxed, Neurologue makes the story as real as it gets. How we built it Using an Emotiv INSIGHT 5 Channel EEG, 7 physiological metrics are read from a user (namely engagement, excitement, long-term excitement, stress, relaxation, interest, and focus). These metrics are determined by analysis of physiological arousal, wave frequency, and wave morphology, using Emotiv's Cortex API in the back-end. The data is sent through a WebSocket as JSON-RPC where it is processed, and then to our Phaser.js project built with Node.js through an HTTP server. These values play into many variables that determine the interactions and results of the playthrough. All sprites, animations, background art, ending art, and other graphics were made with GameMaker Sprite Editor and MS Paint. Challenges we ran into All of us were very unfamiliar with game development before starting Neurologue, so it was a challenge to learn game development and Phaser.js. We had initially wanted to make the game in GameMaker Studio 2, but due to its incompatibility with the WebSockets that the Emotiv EEG uses, we switched over to Phaser.js. It was also a challenge to use both Emotiv and Phaser.js since the documentation for both is poor and online help is primarily for older versions of both. Another challenge that we faced was making the HTTP requests work for communication between the game and the server. We could not connect the game directly to Emotiv's WebSocket, so we had to improvise by connecting the WebSocket client to an HTTP server, and then the HTTP client to the game. Accomplishments that we're proud of We are proud of developing our first game using our own sprites and animations, and also of using an electroencephalographic brain-computer interface to make it as interactive as possible for users. We are also proud of learning game development, including Phaser.js, in a short amount of time for this hackathon, along with creating an engaging and fun game. The hurdles we overcame from poor documentation to HTTP request issues make us proud of our well-polished game. What we learned We learned Phaser.js for the game development process, as well as how to incorporate the Emotiv INSIGHT 5 Channel EEG into the game. By troubleshooting, we also learned more about how to work with HTTP requests, process JSON, follow the documentation, and learn some graphic design. What's next for Neurologue We are planning on adding even more animations and expanding the storyline further. Our current game has a complete storyline, but we could add even more branches and endings to increase the complexity and re-playability of the game. We hope to be able to publish this game so that anyone can play it from anywhere, though this may be challenging due to the need for a local WebSocket client for Emotiv. <div