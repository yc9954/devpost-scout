---
slug: "seekers-alliance"
url: "https://devpost.com/software/seekers-alliance"
title: "Flexible Hierarchical Drawing Pools by Seekers Alliance"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 1139
team_size: 5
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/legal_justice"
  - "user/developer"
---

# Flexible Hierarchical Drawing Pools by Seekers Alliance

> To improve fairness & design freedom, we created a flexible smart contract structure on top of ERC-1155 for our game, Seekers Alliance, using Chainlink VRF, CCIP, Automation & Data Feeds on Avalanche.

[Devpost](https://devpost.com/software/seekers-alliance) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**domain** [[developer_tools]] [[legal_justice]]
**user** [[developer]]

**stack** nextjs, raindowkit, redux, remix, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what's next for seekers alliance

## Body

Cross-chain purchases powered by CCIP; token exchange powered by Price Feeds Demo NFT Collection on OpenSea (Avalanche) Demo NFT on OpenSea (Avalanche) Smart Contract Design For Flexible Hierarchical Drawing Pools Please note that our art assets were taken from our game-in-progress and created prior to the Constellation Hackathon while our smart contract & front end code were done during the hackathon period. Inspiration Both digital and non-digital games such as trading card games (TCG), gacha games, dungeon crawlers, and even RPGs (think Pokemon Trading Card Game and Blizzard’s Diablo), rely on some randomized card-draw/loot system to incentivize players to spend more time and resources on the game for potentially high rewards. (After all, who doesn’t want to open the unique Magic the Gathering card “The One Ring” and sell it to Post Malone for $2 Million dollars ?) However, the RNG used by centralized Web2 companies severely lacks transparency and rates published by the gaming companies simply cannot be verified without a large amount of empirical data. Such non-transparent “randomized” card/loot systems and game designs have faced controversies and even resulted in legal actions. For instance, in 2017, Square Enix was sued in Japan over the discrepancy between actual and published “drop rates” in the game Hoshi no Dragon Quest where players sought 3,350,000 Japanese Yen (over $30K USD) in damages. And just this July, a popular KOL in Taiwan, DinTer (丁特), is due to receive 7.84 million TWD (over $260K USD) from Gamania Digital (遊戲橘子) in damages for a similar infraction in the game Lineage M . While Web3 games generally offer more transparency, they are not without their own set of challenges. Similar to their Web2 counterparts, without an impartial third-party, there is no way to guarantee that the “randomness” promised by the gaming projects is truly random. In addition to proving fairness, our team has identified these main issues with using the existing ERC-721 and ERC-1155 standards: Web3 pull rates are commonly dependent on the NFT supply count, resulting in fluctuating probabilities each time an NFT is drawn. For example, a player who bought a card pack expecting a 3% chance of pulling a Rare may consider it unfair if someone else beats them to it, reducing the pull rate of a Rare card to 2%. There is no easy way for different pull rates to be assigned to randomized “privileged” packs or special event rewards. New cards cannot be issued (for a game expansion or rebalancing, for example) without affecting the pull rates of other cards. Our team is currently working on an awesome Web3-native trading card game, "Seekers Alliance". We've designed it to have skill-based card battles with high-stakes jackpots starting out in the millions. Therefore, we must uphold fairness to the highest degree - and there's no better solution than using Chainlink VRF. What it does Our Hierarchical Drawing Pools architecture enables game developers to freely customize pool probabilities for each use case according to their game design while maintaining constant and fair pull rates using Chainlink VRF as a verifiable source of randomness to address any fairness concerns. The smart contract’s multi-layer design also allows for unlimited minting of common utility cards as well as launching rebalances and expansions without affecting the overall pull rates. In this demo project: Chainlink Price Feeds obtains the current exchange rates between tokens, allowing players to use a supported token of their choice when purchasing our card packs. Chainlink CCIP makes it convenient for players from other chains to be able to make cross-chain purchases, bypassing the need to bridge assets. Chainlink VRF plays an instrumental role in our project by providing a random number generator that is provably fair and verifiably random. Chainlink Automation monitors events from the relevant on-chain contract to automatically execute requests for time & cost savings. How we built it To address the fair-draw issues encountered in our upcoming game, the Seekers Alliance team proposed a flexible smart contract architecture built on top of the ERC-1155 standard using Chainlink Price Feeds, CCIP, VRF, and Automation. We chose Avalanche Fuji to deploy our demo due to its many benefits, including near-instant finality, affordable gas prices, high throughput, Chainlink support, and an overall awesome gaming ecosystem. Smart Contract Architecture on Avalanche Fuji & Chainlink Products Used Challenges we ran into Designing a flexible architecture that can meet the diverse needs of all types of games and be able to cover all edge cases was the main challenge. We wanted to make our Hierarchical Drawing Pools architecture as flexible as possible since we strongly believe that it will be useful to many others in the industry, and we want to promote it as a standard. (We plan to submit an ERC proposal in the near future.) In addition, efficient debugging proved crucial due to the mutual on-chain impact of multiple contracts. Lastly, as the types of prizes (TokenIDs) increased, we saw that the gas costs also rose dramatically. If relevant contract variables are stored in a conventional array structure, the cost would be prohibitively high. Accomplishments that we’re proud of We are extremely proud of our flexible hierarchical architecture, which allows game developers to customize the prize pool and probability at each level according to their game needs at launch, updates/rebalances, and new releases while maintaining constant and fair pull rates. Furthermore, we are proud of the gas cost optimizations we have achieved by using an octree data structure to store the variables, ensuring that the costs of interacting with the contract does not escalate significantly even with an increase in the types of prizes in the TokenID Pool. Also, we have expertly integrated Chainlink VRF, CCIP, Price Feeds and Automation to ensure the fairness, security, and stability of our smart contracts. What we learned We learned how to develop a smart contract standard from scratch and realized the importance of teamwork. More importantly, during this hackathon, we gained insights into how to leverage various products from Chainlink to expand the application scope of our project. Now that we better understand the products and services available from Chainlink, we are sure to integrate them as an integral part of our game design going forward. What's next for Seekers Alliance Seekers Alliance is currently in a fundraising round in order to acquire more resources to finish developing our card collecting & battling game. Here's a sneak peek: We want to submit our Hierarchical Drawing Pool architecture as an ERC proposal, so that other game developers with a need for randomness will benefit from its design and Chainlink products. We are confident that people will find it useful, and look forward to others' expansions on top of our original design. Then, finally, we have to complete game development and smart contract integration to prepare for our 2024 launch. Follow our progress at our Twitter/X ! <div