---
slug: "metacraft"
url: "https://devpost.com/software/metacraft"
title: "MetaCraft"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 1517
team_size: 6
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# MetaCraft

> Truly decentralized, multi-chain, cross-platform, community-driven & developed play-and-earn gaming metaverse platform.

[Devpost](https://devpost.com/software/metacraft) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[developer_tools]] [[housing_homeless]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** amazon-web-services, aurora, back4app, java, minecraft, near, react, rust, solidity

## How they structured the write-up

- inspiration
- what it does
- 1. project introduction
- 2. nft
- 3. staking
- 4. $build tokens
- 5 how to play in metacraft
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for metacraft

## Body

Blockhead NFT MetaCraft map MetaCraft player onboarding website screenshot website screenshot in game screenshot in game screenshot Inspiration In traditional games, games are played for pure pleasure with no real-world reward structure for the end users playing the games. We saw players passionate for the new Play-2-Earn blockchain games and the financial incentives. While most blockchain games focus on Play-2-Earn, we want to focus on the fun of playing and offer real-world rewards as part of in-game achievements. This creates more stable in&out-game economic systems and thus a more sustainable game. With this background, we started MetaCraft to create a truly decentralized, multi-chain, community-driven virtual space where players can play, build, own, trade, and profit through skilled gameplay and contribution to the ecosystem. MetaCraft is built on the backbone of the all-time most popular game Minecraft. Utilizing its proven success, strong community and open source ecosystems, we can expand quickly and to the decentralized gaming metaverse of MetaCraft. This project is inspired by Minecraft and on-chain GameFi projects such as NFT worlds, Genesis critterz, sandbox, and many others. Our team has significant experience working in different tech companies based in the Bay Area and New York. We have also collectively spent over 10,000 hours in Minecraft since its launch in 2009. What it does We have the following sections: Project Introduction NFT Staking $BUILD Tokens How to play in Metacraft 1. Project Introduction Fully on-chain NFTs enabling P&E on Minecraft The MetaCraft NFT Project is a multi-chain game on the Near/ Aurora/ Ethereum blockchain to enable Play-and-Earn on Minecraft. You can stake your Blockhead to generate in-game currency $BUILD and use $BUILDs to purchase Blockhead NFTs / Plots / various in-game props to enhance the playing experience. Features of ownership include: Fully on-chain NFTs that live on the Near/ Aurora Blockchain forever. Stake Blockhead to access an exclusive Minecraft world. Generate $BUILD tokens by playing Minecraft. Use $BUILDs to claim Plots of land in Minecraft as NFTs. 2. NFT 2.1 Blockhead NFT BlockHead NFTs are generated on-chain, which each one uniquely randomized created when the NFT is minted. This means that instead of relying on third-party servers like IPFS, users’ NFTs are stored directly on the Near blockchain. This guarantees that users’ Blockhead will never disappear as long as the Near network is up. Each BlockHead NFT is a 64 x 64 pixel art, which also works as a Minecraft skin. 2.2 plot map The Minecraft server world consists of 12 x 18 plots, where each plot is 512 x 512 blocks. The map includes various biomes. 3. Staking 3.1 Mechanics to unlock Blockhead NFTs provide various utilities and mechanics through staking. Users can access Blockhead after connecting his/her wallet to interact with these mechanics. The main mechanisms that staking unlocks are: Access to the Blockhead Minecraft world. Generating $BUILDs using in-game playtime. Renting out unused staked Blockhead to other players for a share of their $BUILDs generation. These mechanisms are only accessible when Blockheads are staked. Users will lose access to them if they unstake their Blockhead. 4. $BUILD Tokens 4.1 $BUILD token generation $BUILD tokens that are generated with in-game activity in Minecraft and staked Blockhead. To achieve this, we had to build a custom oracle to compute $BUILDs generated based on playtime and bridge onto the Near blockchain without incurring high gas fees for the player. $BUILDs generation is influenced by two factors: play time and build factor. 4.2 $BUILD claiming $BUILD tokens are claimed on our $BUILD claiming dashboard. Under the hood, a query is sent to the oracle to get the amount of $BUILDs claimable along with a signature. This information is then used to claim $BUILDs from the contract. 5 How to play in Metacraft 5.1 Joining the world Instructions for joining the MetaCraft Minecraft Server are in the https://metacraft.netlify.app/ . Upon joining the server, players are asked to type /verify in the chat and open the in-game link. The link will ask the player to connect to Near wallet/ Metamask, after which their account will be connected. Anyone can access the server, but only players with at least one staked (and verified) Blockhead can access the main world to start generating $BUILD with in-game time. All players are required to have a legitimate version of Minecraft 1.18 Java Edition to play. 5.2 Minecraft Server Gameplay The Minecraft server is a survival mode server on Java Edition 1.18. Upon joining, players are placed in a cool glass lobby before they verify their wallets and staked Blockhead with the /verify command. When players are verified, they are instantly teleported to the main survival world. How we built it Frontend: ReactJS, NearAPI for wallet and contract integrations Metamask RPC API “eth_requestAccounts” for connecting to metamask and running on ETH/Aurora testnet. Smart contract: We deployed 2 near rust smart contracts. BlockHead NFT contract (NEP-178 standard): this contract stores metadata about the blockhead on-chain. The nft must be staked to enable players to play on our server. BUILD FT contract (NEP-141 standard): tokens player earned during gameplay. The $BUILDs are generated proportional to the accumulated playtime for a player. Database: We built Back4app relational databases to store user verification status and accumulated playtime. Minecraft mod: We built a Minecraft server mod using Forge to support the login lobby, communication with the database, and user verification logic. The login lobby is a custom Minecraft structure made of custom indestructible glass blocks, to enforce that the user must connect to a NEAR account in order to play. The mod sends HTTP requests to the database to query the user’s verification/stake status. If the user is verified, the mod teleports the user out of the lobby so that they can start playing. The Minecraft server is hosted on a AWS EC2 machine. Challenges we ran into Frontend: The challenges with frontend was using Near-api to integrate with blockchain. We spent a lot of time figuring out what api methods we should use to retrieve data from the blockchain. Smart contract: Rust has a quite steep learning curve, learning the language and being able to fully understand the near example contracts are challenging. Near blockchain has some fundamental differences compared to Ethereum. For example, there are no distinction between contract and external owned accounts. Also the account storage deposit concept. One challenge we faced is that we mint tokens to a user account and check there is a balance for this user in the contract. However, the balance is not showing in the user’s near wallet. Later we found out that we need to initiate a user storage deposit in the contract in order to show the balance. (discussion regarding this issue ) Minecraft mod: The most challenging part of our mod was ensuring the custom login lobby structure is generated during world generation and making its location known to the login logic. Custom structure is one of the hardest topics in Minecraft modding, requiring advanced APIs like ChunkGenerator (for associating the structure configuration with world generation) and techniques like Access Transformers (for changing Minecraft’s private methods at the bytecode level). The custom indestructible glass blocks also posed issues on lighting, since we want sunlight to pass nicely through the lobby walls. On top of that, Minecraft modding changes significantly for each new Minecraft version, and there aren’t many great tutorials for the latest version. The Forge modding API has very little documentation. Often, the functionality of an API can only be inferred from its name. Database: Hiding the master key in the gaming server would be the challenging part since we don’t want to expose our secret keys in the code. Accomplishments that we're proud of We accomplished a complicated system integrating frontend, Minecraft server mod, database, and near contract end to end. This gives players a smooth onboarding experience and enables players to play&earn in Minecraft!. What we learned Writing and deploying nft and ft smart contracts on NEAR NEAR javascript sdk interaction with wallet and contracts Setting up and customizing Minecraft server mod Minecraft command line control and communication with the near wallet End-to-end development of an on-chain game Tokennomics / finance models from other great crypto games Setting up database and integrating frontend and game server with the database What's next for MetaCraft Knowing the importance of a stable economic system for the game, we have spent a great amount of time on designing the in&out game economy and project roadmap. Key milestones include: Implementing renting feature allowing user to rent out their BlockHead NFTs, Plots and other NFTs will significantly lower entry fees for new players, add a passive revenue stream to existing players and thus increase active usage of in-game items Tokenomics designed to develop deflationary in-game currency that provides utilities for gamers. DAO to allow users to vote on in-game development and directions of the project. Partnership with existing minecraft servers / communities (e.g. Blockeley ) Built out cross-chain compatibility allow Minecraft assets from other chains to be used within our ecosystem Follow us on Twitter: https://twitter.com/MetacraftDAO Follow us on Youtube: https://youtu.be/-yTRfY-PJBU Follow us on Telegram: https://t.me/MetacraftDAO Check our Website: https://metacraft.netlify.app/ <div