---
slug: "nftbl"
url: "https://devpost.com/software/nftbl"
title: "NFTBL | Your Own Football Team"
hackathon: "TRON Grand Hackathon 2022"
organization: "TRON DAO"
winner: true
words: 467
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
---

# NFTBL | Your Own Football Team

> Web3 football game built around NFT players card collection. Gamers can manage their club, earn tokens, upgrade NFT's for them and battle in online P2P matches with each other

[Devpost](https://devpost.com/software/nftbl) · hackathon [[TRON Grand Hackathon 2022]]

## Facets

**mechanism** [[on_device_local]]

**stack** javascript, react, solidity, tron, tronlink, tronweb

## How they structured the write-up

- inspiration
- what it does
- p2p matches are here
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nftbl | your own football team

## Body

Your team Academy Marketplace P2P Matches Match result Inspiration We love football like many people around the world (hope, you too). Also, we like computer games and see how card collecting and card games is taking over the world last years. We decided to mix it :) We use opportunities of TRON protocol to create NFT Football game where gamers would be real owners and managers of their football club and players cards with online P2P matches and growing community. Also, we want to engage many new people in web3 economics through play2earn mechanics which are engageable and helpful in community building. What it does NFTBL is the game built around NFT players card collection. Each player's card has unique properties including upgradable Card Rating (and also looks good!). The game has an elaborate internal tokenomics. After getting an NFT gamer can stake it for getting fungible token BALL . BALL can be spent on P2P matches, sold in Marketplace or staked for second fungible token GOAL which using for NFT upgrade An upgraded NFT has better performance in P2P matches and emit a greater amount of BALL tokens when staked. All this logic is fully implemented in our smart contracts, more details in our GitHub . P2P matches are here P2P matches open for 5-players teams. Gamers set up a team from their cards trying to keep balance and win the game. Matches results depends on 2 sides: offense (scored goals) and defense (missed goals). Each position on the field influence on offense or defense. To play P2P match they pay entry fee. After match a winner automatically get sum of fees as a reward. In current MVP gamers will play vs bot if opponent is not found How we built it We developed smart contracts that implement industry standard interfaces such as ERC20 and ERC721. Those contracts communicate with each other, so players can stake, burn and upgrade their tokens. We used open zeppelin libraries, as they are thoroughly audited and battle tested. Hardhat was used to test smart contracts locally before deploying them on Testnet with Web Tron-IDE Challenges we ran into Most challenging thing was probably integration with smart contracts from frontend. Luckily Tron have some very convenient features like on-chain ABI, that made this process faster Accomplishments that we're proud of We built three token gaming system which promises to be very interesting to play with. We are excited to see how players would engage with it What we learned We learned a lot about how Tron works, why it need staking, energy and bandwidth. We would love to continue building on this chain What's next for NFTBL | Your Own Football Team Try our game (link below) and have fun! Note: Get 10,000 TRX (Shasta Testnet) from Twitter account @TronTest2 <div