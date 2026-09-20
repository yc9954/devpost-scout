---
slug: "toshimon"
url: "https://devpost.com/software/toshimon"
title: "Toshimon"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 1259
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Toshimon

> Toshimon is a retro style trading card game that utilizes NFTs as in-game assets. Users collect Toshimon cards that come to life in game to participate in pvp battles with on-chain settlement!

[Devpost](https://devpost.com/software/toshimon) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[general_public]]
**substrate** [[code_repository]] [[financial_record]] [[video_visual]]

**stack** react, solidity, unity, web3, webgl

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for toshimon

## Body

Toshimon Toshimon Pack Game Lobby Battle Menu Legendary Card Ultra-Rare Card Rare Card Uncommon Card Toshimon Banner Toshimon Logo Inspiration Toshimon is inspired by a variety of classic trading card games and retro role playing games, such as Pokemon and Yu-Gi-Oh. Many participants in blockchain grew up enjoying such games so we were inspired to create a game that encompasses our favorite aspects of the classics whilst tying in blockchain, decentralization and game economies. What it does Toshimon is a browser-based, PvP battling game that utilizes NFTs as in-game assets. Users open packs and collect cards to build a deck of five Toshimon to bring into battle. Once connected to the game lobby (using wallet connect, metamask, etc), Toshimon cards take on the form of in-game sprites. There are 14 types of Toshimon, and each type has different strengths and weaknesses. It is up to you to decide how to best assemble your team to be prepared for any challenger. Once you have assembled your team, you can battle with your Toshimon against other users or NPCs in the turn-based arena. Each player takes turns attacking the other player using their Toshimon. The winner is the last player with Toshimon remaining in their deck. How we built it Toshimon was founded in late 2020 and was originally launched on Ethereum. The umbrella of assets consisted of Generation One Toshimon NFTs (packs/cards) in the ERC-1155 standard, $TOSHI token —a hard currency in the ERC-20 standard, and ToshiCash —a soft currency in the ERC-20 standard. $TOSHI was distributed via airdrop to early supporters. In order to incentivize liquidity provision, users were able to lock TOSHI/ETH in the pool and exchange the corresponding LP tokens for NFTs that yield ToshiCash . Users could use this currency to acquire packs. When opened, each pack is burned and eight Toshimon cards are minted to the user's wallet based on randomness and rarity. All smart contracts were developed by our wonderful web3 dev/CTO, @BlueDerpyfi . The Toshimon Beta game is built on Unity WebGL. Challenges we ran into Technical Challenges With so many moving parts, Toshimon presented quite a few challenges. The primary roadblock, however, was the gas fees on Ethereum. Opening packs became an extremely expensive process—sometimes costing upwards of $150 per pack in gas fees. Polygon was an amazing solution for this and resulted in Toshimon becoming multi-chain as it is today. While the packs are already in circulation on Ethereum, they can be opened to Polygon for as little as 10 cents in gas fees. Opening to Polygon means that that the Toshimon cards you get will be on Polygon which also makes it cheaper and faster to buy/sell/trade cards with other users. This, however, created another issue—having assets on two different blockchains. A bridge to move assets seamlessly between Ethereum and Polygon was a simple solution! Another substantial challenge that we faced was recording game actions on-chain. Our goal is not just to integrate NFTs and other tokenized assets into a game economy, but rather to integrate a game and all of its aspects into a blockchain. We envisioned PvP battles taking place entirely on-chain to promote security and decentralization. After all, if we are going to call ourselves a "blockchain game", then the gameplay better be on-chain. This proved to be extremely complicated, especially when taking deployment costs and user-end gas fees into consideration, but we are getting close to completing a unique solution to facilitate on-chain settlement of every battle! Leadership Challenges Following the early success of Toshimon, the founder/CEO began acting maliciously within his role. The developers and community members came to an agreement to push the founder out of his role and consolidate the project assets. This created a lot of unknowns for the future of Toshimon, but fortunately the rest of the team was commited to following through. Regardless, the previous actions of the founder hurt Toshimon's image. The new CEO instilled lots of hope in the community, but hope was not enough as development slowed and funds dried up. Eventually, this CEO decided to part ways with the project, leaving just a developer and the social media manager to decide Toshimon's fate... Accomplishments that we're proud of Primarily, we are extremely proud of Toshimon's resilience. After almost two years and multiple leadership changes, Toshimon has finally found stability. Led by newly appointed CEO, Jake Lubin , and CTO, @BlueDerpyfi , Toshimon has secured the funding required to continue development temporarily. We are also very proud of our commitment to decentralization and education in the space. We advertise ourselves as being 'decentralized' and 'on-chain', and our current stage of development is going to make this happen. By utilizing state channels, PvP battles take place between players in a completely private, p2p space in which they must agree on game rules. This is how we commit to decentralization. What's even cooler is that every action performed in these state channels is settled on-chain. This means that all game records will be secure and verifiable on the public ledger! Some other achievements that we'd like to note are as follows: 670+ ETH in NFT trading volume 60+ ETH locked as liquidity for $TOSHI $20million+ in trading volume on $TOSHI 1,500+ NFT holders and 400+ $TOSHI holders Toshimon NFTs on Ethereum and Polygon ! Beta game live on Toshimon.io 3D/AR-rigged NFT upgrade What we learned Our time in the space has showed us the importance of sustainability in gaming. Since Toshimon has been around we have seen a multitude of conceptually similar games fail due to poor allocation of funds, tokenomics that resemble ponzi schemes, unbalanced game economies, rug-pulls, and so on. We learned what causes these flaws, how to avoid them, and how to create a sustainable, well-balanced game economy that is focused on providing users with an entertaining gaming experience. The #1 goal of a game is to be fun!! We want our users to have the opportunity to be rewarded for playing, winning battles, and collecting Toshimon, but this needs to be done in a sustainable way. This means NOT devaluing the assets by minting more and more. Instead we made sure that $TOSHI and Toshimon NFTs are deflationary thanks to their use in ToshiFusion (fusing Toshimon together to form a stronger mon). What's next for Toshimon Currently, Toshimon is a simple battle arena/lobby where players can congregate and battle with each other or against NPCs. While this is plenty fun, it is not enough. The current stage of development, once completed, will facilitate PvP battles with on-chain settlement, the ability to conduct peer-to-peer wagering on battles, and the option to customize the rules of battle. Following the core backend blockchain development, we will be integrating the full scope of ToshiFusion which will allow players to evolve, or upgrade, their Toshimon by fusing them together whilst promoting deflation. Players can also expect the Toshimon lending platform to be released shortly after this. Lending will allow players to lend their Toshimon NFTs to other players at an agreed upon earnings split. This can be a fixed fee or a percentage of profits from wagering and/or play-to-earn activities. Beyond the tech functionality, we are putting a huge focus on FUN! We plan on expanding Toshimon to be more than just a battle arena/game lobby. The world of Toshimon will include in-game marketplaces, trading stations, tournaments, random monster spawning, single player quests/challenges, and more! A second generation of Toshimon card packs along with a in-game avatar collection will be released following the expansion of the Toshimon game functionallity. <div