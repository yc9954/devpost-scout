---
slug: "ggquest"
url: "https://devpost.com/software/ggquest"
title: "ggQuest"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 794
team_size: 5
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/web_dom"
---

# ggQuest

> ggQuest is a platform where gamers can play in a safe & cheat-free environment. We're developing a set of anti-cheat tools linked to a reputation system for blockchain games.

[Devpost](https://devpost.com/software/ggquest) · hackathon [[EthCC Hack 2022]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** amazon-web-services, css, css3, html, html5, javascript, jsonfiles, next.js, react, selfmadeapi, solidity

## How they structured the write-up

- inspiration
- what it does
- current functionality:
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ggquest

## Body

Inspiration We’ve seen a lot of abuse and exploits in video games during our time as professional gamers. We believe, as many in our industry, that games can benefit a lot from blockchain technology. Web3 games can be more effective at creating game economies and give the ability to monetise in new ways (NFT’s, tokens). This means new types of incentives for the player and thus more incentives to try and exploit the games (especially with our web3 hacker mentality). We are creating a platform where gamers can play in a safe and cheat-free environment. To do this, we’re creating different tools in the form of a reputation system, on-chain analytics and more. Next to that, we’ve been fascinated by on-chain activity and we’re considering using on-chain data to create rich worlds. Imagine using wallet data (tokens, NFTs & activity logs) to develop social networks and matchmaking services. What it does We’re building an on-chain reputation system called Quest ID that will act as your web3 gaming passport. Your Quest ID will act as your Unified ID across chains and crypto games. You can use the Quest ID to apply for Guild Memberships, Alpha and Beta access web3 games, and display your priceless game assets, badges, and achievements you’ve collected from games across several chains. Current Functionality: Users can see on the products all the quests created by games. When a quest is completed, the player can claim the reward associated with it, which is a reputation increase and additional rewards from the game developers (skin NFT, tokens…). Each quest is linked to a smart-contract which will make all the verifications and distribute the rewards to the player if the quest is completed. A reputation score is built with SBT contracts. Players can check their reputation scores as well as the leaderboard. How we built it The website is divided in two parts : front-end and back-end. The front-end is built with ReactJS. It displays all the information for the player and allows them to claim their quest rewards. It communicates with the back-end through a Rest API. The back-end is built with NodeJS for the rest API, and solidity for smart contracts. Its role is to read on-chain smart-contracts to provide relevant and computed data to the front-end through the Rest API. Challenges we ran into We would have been happy to integrate multi-chain mechanisms with Abacus, but we didn’t have enough time. After a lot of design discussions, the main issues were linked to the front-end and the design. Accomplishments that we're proud of Finding a congruent team that can deliver a product from front to back end. What we learned We have learned a lot from the possibilities from the protocols sponsoring the event. What's next for ggQuest We intend to develop an SDK that will give you access to anti-cheat tooling and enhanced reputation data that you can use to create tools on-top of our existing reputation network (e.g., matchmaking plugin, leaderboards, mini-games, import blocklists of exploiter wallets, etc.) The Quest ID will exist as a multichain SBT network that gathers your in-game experience (e.g., hours/matches played, KD ratio, in-game ranking, badges, achievements, guilds associated with, match-making tags) Use cases for the Quest ID network Anti-cheat tools Integrations to implement traditional web2 anti-cheats: We import off-chain actions (in-game) as +ve or -ve reputation points. Off-chain cheating example: Aimbot in ev.io, marked wallets will get restricted by game developers. Onchain cheating example: game developers can publish restricted actions (e.g., botting breeding in CryptoUnicorn) and penalize players for performing the restricted action. Onchain Monitoring: smart contacts, malicious wallet detection) Help game developers monitor Smart contracts, token flow, and other game-related on-chain activity in real-time. The main product will be to develop an easy-to-use monitoring platform similar to Fort (Or in partnership with Forta??) Our team must constantly add new rules and patterns we identify in other games and blockchain ecosystems. Game developers will get the chance to review and manually improve actions (such as restricting botting wallets) Reputation System (Omnichain Steam ID) The Reputation System, or as we call it, Quest ID: Will be a collection of SBTs implemented across several chains (ETH, Polygon, BSC, Solana, etc.) and help players track their reputation score badges, rewards, assets, guild memberships, and social connections. What can the reputation system be used for? Anticheat (mark wallets participating in exploits and clear cases of cheating. Gate experiences to wallets that have a certain level of reputation and badges, guild or esports memberships It will make on-chain monitoring easier because of rich data through SBTs (hours played, off-chain activity, badges, rewards, etc.) Create a social matchmaking tool where the SBTs are used to filter and perform matchmaking for players, guilds, and esports tournaments (online open tournaments <div