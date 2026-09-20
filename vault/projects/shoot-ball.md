---
slug: "shoot-ball"
url: "https://devpost.com/software/shoot-ball"
title: "Shoot Ball"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 383
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
---

# Shoot Ball

> Shoot ball is a online multiplayer soccer game which allows 2-6 player to compete and bet by using their coins as enterance fee. A portion will be taken from the smart contract as service fee.

[Devpost](https://devpost.com/software/shoot-ball) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]

**stack** amazon-web-services, chainlink, chainlinkkeeper, moralis, photonnetworking, playfab, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for shoot ball

## Body

Title Screen GIF Game Play - Crazy Skill! Game Play Game Play - Boom! Game Play - Road Block? Inspiration Gaming is fun, and all members in our team are gamers. We want to create a new way for gameFi besides from play-to-earn style, and fun to play. Thats why we created a crazy soccer game, which has characters who can cast crazy skills! What it does Shoot ball is a online multiplayer soccer game which allows 2-6 player to compete and bet by using their coins as enterance fee. A portion will be taken from the smart contract as service fee. The winner of the game will share the pool of prize(all enterance fee - service fee). How we built it We use Unity as the game engine that we use to build our game, and we used Moralis and its Unity SDK to do the web3 interaction. For the smart contract, we use Chainlink Keeper and API request Job to communicate with our backend to achieve calling smart contract when game state update. Challenges we ran into time - since the time is limited, we wanted everything to be perfect, however, we dont have much time to polish everything in our project. Accomplishments that we're proud of chainlink keeper - The contract is built with Chainlink Keeper and API Request Job on Kovan. The contract will distribute the reward automatically to each team members equally based on the game result got from the API. After distributed all the reward to winning team, the contract would clean the records and restart for the next game. Moralis - we successfully implement the game with web3 by using moralis, which enable players to interact with smart contract, e.g. pay entrance fee, interact with the view function in smart contract, it makes our game has a good starting point. Unity multiplayer - we successfully make a multiplayer game which allows player to compete each other in real time. this really increase the excitement! What we learned A lot of blockchain related experience which you wont have before you actually implement it. What's next for Shoot Ball we can make the smart contract more flexible. For example, make the enterance price can be set by the players. Add more characterss for people to play with <div