---
slug: "ceptor-game-mechanics"
url: "https://devpost.com/software/ceptor-game-mechanics"
title: "Ceptor Game Mechanics"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 675
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "user/developer"
---

# Ceptor Game Mechanics

> We 🔧 aim to revolutionize tabletop RPGs by leveraging Chainlink, blockchain and AI! Create unique DND 5E characters in seconds with a quiz or two clicks randomness. Save time and immerse a new game!

[Devpost](https://devpost.com/software/ceptor-game-mechanics) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**domain** [[developer_tools]] [[labor_employment]]
**user** [[developer]]

**stack** chainlink, functions, nextjs, pricefeeds, react, scaffold-eth, scaffold-op, ttrpg, vrf

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ceptor game mechanics

## Body

Web app (landing) QWIZ - Character Sheet Generator QWIZ - Character AI User profile Inspiration Playing and scheduling a tabletop role-playing game is time-consuming. If you are a gamer, you understand the struggle of creating a unique character that is visually captivating and engaging. Maybe you’ve spent countless hours filling out character sheets. Maybe you’ve tried hiring an expensive game-master or even using generic character designs, only to end up with disappointing results. The process to participate in these types of games can feel daunting and never-ending for a new gamer. And, to make matters worse, once you have your character, having a place to schedule to play the game itself, requires yet another couple more days, weeks, or months of time. But with Ceptor Club Game Mechanics, we aim to save you time and get you into a game within seconds using our intelligent blockchain tools. What it does Ceptor Club Game Mechanics is forging a new era in the realms of tabletop role-playing gaming with the power of Chainlink blockchain and AI. It’s the antidote for gamers facing barriers in recruiting allies to quest with, as well as a haven for fantasy gamers and developers seeking a stage to play in their imaginative worlds. The core of Ceptor Club Game Mechanics is a choose your own adventure. Gamers can choose to take a simple quiz where users answer questions that draw upon real-world questions and get a DND 5E character. Or with the click of two buttons, it will generate a random, unique DND 5E character. After creating the character, the gamer will then save it to their wallet so that they quickly schedule a game. How we built it We built Ceptor Club Game Mechanics using Chainlink VRF (Verifiable Random Function) to ensure randomness in character generation. The smart contracts are written in Solidity and deployed on the Polygon Amoy Testnet. We used Chainlink data feeds to determine the cost of creating characters in LINK tokens based on a USD price. The characters are saved on the blockchain, and Chainlink Functions are used to send character details to GPT to generate additional character traits. We implemented Access Control using OpenZeppelin to manage player and gamemaster roles. Challenges we ran into One of the main challenges we faced was ensuring the accurate conversion of MATIC to USD using Chainlink price feeds and correctly calculating the cost of GamesTokens. We also had to manage access control effectively, ensuring only authorized players and gamemasters could interact with certain functions. Integrating AI for character trait generation and ensuring seamless interaction between the blockchain and off-chain services was another significant challenge. Accomplishments that we're proud of Alan rebuilt the quiz from scratch to be even faster and easier than before, and even deployed a smart contract to save the character. We are proud of successfully integrating Chainlink VRF for secure and random character generation. We implemented a decentralized system that allows for dynamic character creation and scheduling. We also developed a robust access control system using OpenZeppelin's libraries. Additionally, the seamless integration of AI to enhance character traits and the overall gaming experience is a significant achievement. What we learned Throughout the development process, we learned the intricacies of working with Chainlink services, including VRF and data feeds. We gained a deeper understanding of Solidity and smart contract development, particularly in managing access control and ensuring secure interactions between on-chain and off-chain components. We also learned about the challenges and best practices in integrating AI with blockchain technology. What's next for Ceptor Game Mechanics Next, we plan to further enhance the character generation process by integrating more sophisticated AI models to provide even richer character traits and backstories. We aim to expand our platform to support more types of tabletop role-playing games beyond DND 5E. Additionally, we will work on improving the user interface and experience, making it even easier for gamers to create, manage, and schedule their games. We also plan to explore cross-chain compatibility to allow for more flexibility and scalability in our platform. <div