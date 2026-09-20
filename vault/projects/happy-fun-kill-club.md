---
slug: "happy-fun-kill-club"
url: "https://devpost.com/software/happy-fun-kill-club"
title: "Happy Fun Kill Club"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 1160
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# Happy Fun Kill Club

> Multiplayer NFT card game where players have fun battling to the death! Play now for free. Or buy and open PACKS to unlock cards of varying rarity. Earn RedCoins and purchase rare NFT items.

[Devpost](https://devpost.com/software/happy-fun-kill-club) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** html5, javascript, php, web3js, web3php

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for happy fun kill club

## Body

Open PACKS of NFT Cards of Varying Rarity Determined by a VRF Request View Your Cards and Create Decks in the Deck Builder Earn RedCoins by Playing the Game and Spend Them at the RedCoin Shop RedCoin Shop Features Limited Edition NFT Items View Your Items and Characters on OpenSea Inspiration I wanted to make a fun, fast-paced online game using NFT cards . I have attempted this before but got lost in the complexity. This time around I wanted to keep things simpler, focus on execution, and actually make a fully playable game. I think I have accomplished that this time. What it does Happy Fun Kill Club is an online game where players battle in a futuristic arena and control the greatest warriors from across the Multiverse. Players take turns deploying these characters and choosing actions in an attempt to eliminate a rival player. The winner of the match earns 3 RedCoins . The loser also earns 1 RedCoin . RedCoins can be minted into the ERC-20 token RedCoin , which can be spent to acquire in-game NFT assets, such as armor or effect cards . In order to MINT RedCoins, the game uses Chainlink Functions to connect to an API and mint the amount of tokens that the player has earned. I wanted to design the experience to have as little friction as possible, so players can start playing with just a hot wallet, such as MetaMask. Every player receives 11 basic cards upon account creation. The player doesn't even have to arrange them. They will randomize if the player wants to jump right into the game. Alternatively, players can spend a lot of time arranging their decks with the deck builder program . Players who really like the game can BUY PACKS of cards and open them . PACKS are ERC-20 tokens that can be purchased for .1 testnet AVAX. These PACKS can be 'opened' which means they are sent to a contract that makes a Chainlink VRF request . The results of this request are used to MINT new NFT Cards that the player can use in-game. How I built it I built this game with the help of many awesome open-source projects . Here are some notable projects that I used: Web3JS - I used the Web3JS vanilla JS code base to interact with hot wallets like MetaMask. Happy Fun Kill Club would be a Web 2 application without Web3JS. Web3.php - I used the Web3p interface to connect to my endpoint to call contracts from my server. Happy Fun Kill Club cards are enumarated ERC 721 tokens, which means I can make a series of calls 1 , 2 , 3 , 4 to determine which tokens are owned by any particular wallet. ImpactJS - I used ImpactJS as my game engine, which is an awesome pure vanilla JS game engine for building HTML5 / JS games. Crypto Currency for PHP - I used the Crypto Currency for PHP library to verify user signatures on my server. Avalanche Fuji Testnet - I deployed the contracts for minting cards, buying items and PACKS tokens on the Avalanche Fuji Testnet . Chainlink VRF - I used Chainlink VRF to create provably fair card draws when the PACKS token is spent. Chainlink Functions - I used Chainlink Functions to query my server to determine how many RedCoins a player has earned and to MINT a corresponding amount of RedCoin tokens. Chainlink Automation - I used Chainlink Automation to manage scheduled updates to the RedCoin Shop. My Upkeeper calls a special function that updates the item URIs and costs. Midjourney - I also used Midjourney to create the amazing art for the cards. Challenges I ran into One issue that I ran into was that I had used Chainlink ANY API in the past . Last time I used this service, I had a single node query my server. I initially wrote my RedCoin minting scripts on these assumptions where the balance of the RedCoin would reset to ZERO after returning the answer to one query. When I used Chainlink Functions to perform the same task, the user's token balance was resetting to ZERO before the tokens were minted . I couldn't understand why. It took me a while to realize that Chainlink Functions uses a quorum of nodes to run this script, rather than a single node. I adjusted my script logic accordingly and everything works now. I learned that Chainlink Functions is AWESOME and much better than ANY API in several ways. Obviously the multiple nodes create greater security guarantees, but additionally, as a developer, I didn't have to go through the trouble of finding and defining JOB IDs, nor do I have to worry about the node operator shutting down and ruining my application. All those problems have been abstracted away and the experience was much smoother and better once I understood what was happening. Accomplishments that I'm proud of END-TO-END CRYPTOGRAPHIC GUARANTEES: One of the challenging thing about creating games using JavaScript is that much of the code is client side. One cannot trust any code that comes from the client as it may be tampered. For example a client can tamper with provider data from MetaMask to claim cards that they don't have. This application solves that problem by making a server-side connection to an external node synced to the Avalanche Fuji Testnet. The server then makes queries to the node to determine exactly which cards the player possesses. Since the user is also required to sign a message to begin playing the game, we can prove two things: The user definitely controls the wallet that signed the message. The user definitely owns the NFT cards that were submitted to the server. These are not assumptions. They are cryptographically proven truths. What I learned I learned that the Chainlink Subscription models are awesome . I learned that I CAN build a really cool multiplayer game that uses blockchain technologies to do unbelievable things. And I learned that cryptography makes amazing things possible . What's next for Happy Fun Kill Club I'd really like to bring the game to Mainnet . The game currently only has around 50 cards. I'd like to make 150 characters cards for the initial launch and line up 50 or so item cards to begin selling in the RedCoin Shop. I'd also like to create single-player versions of the game, perhaps a story mode , and maybe an online lobby world where the players can meet, mingle, and arrange matches in other ways. Also, the ability to play against a specific individual with custom matchmaking links . Of course more sound effects, animations, and other aesthetic tweaks would help. There are a few small bugs to work out but I think the game works pretty well considering the short amount of development time devoted to it so far. Thanks for checking out Happy Fun Kill Club ! <div