---
slug: "fury-racing"
url: "https://devpost.com/software/fury-racing"
title: "Fury Racing"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 1299
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "substrate/financial_record"
---

# Fury Racing

> Fury Racing is an on-chain racing manager strategy game leveraging Chainlink VRF V2.5, Chainlink Functions, and Chainlink Automation. Currently deployed on Avalanche Fuji.

[Devpost](https://devpost.com/software/fury-racing) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**substrate** [[financial_record]]

**stack** amazon-web-services, babylon.js, catapulta, chainlink, chakraui, express.js, foundry, nextjs, openzepellin, rainbowkit, solidity, typescript, vercel, viem

## How they structured the write-up

- problem
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fury racing

## Body

Fury Racing Logo Home page Car attributes selection Race animation FURY RACING | CAR MANAGER Problem Web3 gaming has been hyped from the start, with many exciting use cases that could enhance the player experience. However, blockchain technology comes with significant drawbacks: it is slow and expensive (storage and transaction fees). Many major Web2 companies are struggling to adapt to these new limitations, despite the attractive potential. It is unrealistic to expect Web3 games to compete with traditional Web2 games, which have decades of experience and face no constraints other than server costs. And it shouldn't. Web3 gaming is complementary to traditional gaming. It is not meant to replace it, just to offer different experiences, in addition to it. The crypto space is growing rapidly. Tools, wallets, and libraries are improving, and scalability is less of an issue than it used to be. Web3 gaming has a lot to offer and holds exceptional promise, with themes like player-owned assets, transparency, and inter-game marketplaces. The key to success is to invent new mechanisms and logic tailored to blockchain, rather than "forcing" existing web2 games onto it. This is what Fury Racing is about, exploring new ways of playing, crafted for web3. In this vein, Chainlink products are a blessing: Chainlink VRF allows for the introduction of randomization, overcoming blockchain determinism. Chainlink Functions enable querying APIs directly from a smart contract in a decentralized manner. Chainlink Automation removes the need for cron jobs (and private keys!) from AWS and other centralized third parties. Inspiration This game is inspired by GOO-Racing which is itself inspired by the well-known 0xMonaco blockchain contest. However, while this inspiration gave a starting point, the smart contracts have been entirely revamped and enhanced into a fully operational on-chain game. Chainlink VRF 2.5 , Chainlink Functions , and Chainlink Automation have been integrated on top of that to provide additional features while keeping everything decentralized. A front-end has been specially built for the occasion to allow any web3 users to interact with the smart contracts in an easy and friendly way. Some animations built with the Babylon.js engine have also been added to make the whole game even cooler! What it does Fury Racing is a car manager game (you do not drive the car yourself), based on strategy (about 90%) and a bit of luck (about 10%). Concept: The concept is simple: you must select a car and optimize its attributes to make the best time against another player. The time is automatically calculated based on the selected attributes, the circuit characteristics, and the real-time weather of the circuit's location. This is where all the strategy comes in (See the backend README.md for more information about the calculation process). In addition, a luck mechanism has been introduced to add some spicy to the game. This luck comes from 2 different sources: 1. Luck Attribute The luck attribute relies entirely on you. The luck attribute will vary depending on how many points you allocate to it, as shown in the table below: 1 2 3 4 5 6 7 8 9 10 -4% -3% -2% -1% 0% +1% +2% +3% +4% +5% If you do not allocate any points to the luck attribute, all your other attributes will get a default -4%. On the opposite side, if you allocate 10 points there, you will get a default +5% to all other attributes. So you will get a percentage ranging from +4% to +5% that will either increase or decrease all your other attributes. While it could be tempting to go for the max bonus, keep in mind that the points you allocate there do not count in your car performance... 2. Luck Factor The second source of luck comes from Chainlink VRF V2.5 . As soon as the race starts, an additional random percentage ranging from -5% to +5% is also applied to your other attributes! You could get lucky while your opponent isn't or... the other way around! The 2 luck sources add to each other, giving a potential bonus or malus ranging from -9% to +10% in total! This doesn't make it any less interesting since it won't be enough to reverse the best settings for the race. It does however help "leveling" the field a bit and may push players to play more to try to get lucky and win the weekly tournament! Race Mode: Three different modes have been implemented: Solo , Free , and Tournament . Training / Solo : You play against a computer with randomly generated attributes. You can play for free, without waiting, and without pressure, at any time. Free Play : You play in a synchronous 1v1. You race for free, but you may have to wait a bit for another opponent to join. You do not have to wait if it takes too long as the race will complete without you as well, but you won't be able to start a new race as long as the previous one hasn't started. Tournament mode : The gameplay is the same as in Free mode. However, you have to pay a small entry fee to participate. The winner of the race will take all the money, minus 5% that will be added to a weekly prize pool. You also gain points that will allow you to climb the leaderboard. And every 7 days, the leader of the leaderboard wins the prize pool! (The prize pool can be sponsored by anyone to attract more players!) How we built it The tech stack chosen to develop Fury Racing is the following: Smart contract : Solidity + Foundry framework + Chainlink VRF/Functions/Automation + Slither + Avalanche Fuji network; Front-end : TypeScript + Next.js full-stack framework + Babylonjs + Viem/Wagmi + RainbowKit + ChakraUI; Back-end : Node.js + Express.js + Viem + AWS Lambda + Serverless; Then, we split the task this way: Pierre : Smart contracts & Front-end & Backend race result calculation; To bootstrap the project, I used the following Foundry template provided by Patrick Collins and my personal web3 boilerplate . Both open source and MIT license. Jean : Display and animation of 3D content using the BabylonJS engine; David : Design, branding, assets, documentation, video; Joseph : Backend starter code; Challenges we ran into The 3 main challenges we faced were: The Babylon.js animations. It requires a lot of manual adjustments (vectors) compared to a complete game engine like Unity. Click here for more information about the frontend and the 3D animation implementations . The backend in charge of the race result calculation. It was supposed to be based on OpenLAP-Lap-Time-Simulator , but we have had to simplify the logic. Click here for more information about the time result calculation . The Chainlink Functions integration. The difficulty came from the fact that each call triggers another call, so the user only has a single transaction to play. EOA => Racing.sol => Chainlink VRF => Racing.sol => Chainlink Functions => Racing.sol This was difficult to test, especially since I discovered the Chainlink Functions mock contract afterward! Click here for more information about the smart contracts implementation . Accomplishments that we're proud of The 3D animations, which look super cool and evolve in real-time with the weather! The smart contracts and the Chainlink integration, working like a charm! The time result calculations and the attributes interactions. To complete everything in time as it was a lot of work! What we learned Babylon.js Chainlink Functions (We can write JavaScript code inside a solidity contract!) Chainlink Automation What's next for Fury Racing 5v5 tournament; Add more circuits and handle weather updates accordingly; Add more cars; Add more attributes to increase the strategy part of the game even further; Implement the OpenLAP-Lap-Time-Simulator to make the game even more realistic; NFT customizable cars (like skins)? <div