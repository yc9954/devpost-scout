---
slug: "prisnr-games"
url: "https://devpost.com/software/prisnr-games"
title: "prisnr.games"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 967
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# prisnr.games

> Head-to-head strategy game invoking the prisoner's dilemma

[Devpost](https://devpost.com/software/prisnr-games) · hackathon [[Cosmos HackAtom VI]]

## Facets

**domain** [[civic_government]] [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[document_pdf]] [[financial_record]]
  <sub>weak: video_visual</sub>

**stack** cosmwasm, rust, secretd, secretjs, svelte, typescript

## How they structured the write-up

- game
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- giving back to the community
- what's next for prisnr.games

## Body

Screenshot of two players in the same game side-by-side Updated UI showing badge NFT Power-up NFTs! Game prisnr.games is a two-player game implemented on Secret Network inspired by the classic game theory game Prisoner's Dilemma where two players must decide to collaborate or not based on limited information. In prisnr.games you join a game by making a wager of 1 SCRT, and then an arbiter (the contract), you, and one other player are each given a random chip with a unique color (red, green, blue, black) and shape (triangle, square, circle, star), and it is your goal to try and guess the chip possessed by the others. The odds of any given color/shape combination are secret parameters of the contract set by the developers during initialization. In addition to your chip, you are given a random hint about the state of the game that helps you deduce what the arbiter or your opponent might have. In successive turns, players are forced to share two assertions with each other about their own chip or the hint they have been given. Players can choose to lie or tell the truth. However, if the contract deduces that an assertion is provably false and the receiver would know it's a lie, then the game instead reveals one of the offending player's secrets, penalizing them for getting caught in a lie! After both players make their two assertions, the game requires them to guess the chip possessed by either the arbiter or the other player. If one guesses correctly and the other guesses incorrectly, the winner gets the wagers. If both are incorrect, the wagers go into a jackpot pool of SCRT. If both are correct, or both abstain, the game goes to a reward round. Here, each player is given a choice about a reward: a jackpot equal to half of the current pool, or a special NFT badge minted with the unique game number. But there’s a catch! If both players pick the same reward, then neither gets it and the wagers are refunded to the players. This is a game with incomplete information that could only be built on Secret Network. How we built it We split up the development of the game for the hackathon with Ben focusing on the development of the back-end contracts and Blake designing and developing the front-end web application. The contracts were written in Rust using CosmWasm, and included a number of key features: Query permits are used to query the state of the game. A private entropy pool is maintained that is updated with every transaction. A SNIP721 NFT Minter is used for minting game badge NFTs with the unique game id and random colors that are Stashh metadata compliant. 10% of minted badges are also Insurance power-up NFTs . In a new game, these can be sent to the game contract before the first assertion by the player. If the player loses the game, the contract will burn the power-up NFT and will override the player losing their wager, instead refunding their wager back to them. The front-end was developed using Svelte+Typescript and three.js for the graphical UI, and query permits are saved to local storage in an encrypted format. The UI polls the state of the game and executes compute transactions in a robust manner that can handle page reloads, timeouts, contract errors and transactions errors gracefully. Challenges we ran into Implementing the contract logic to correctly handle all game stages was a challenge. We eventually had to scale down our ambitions in order to implement everything for the hackathon (e.g., originally we had two rounds of assertions/guessing). Handling timeouts for players was also a challenge. We chose to implement a force_endgame message that allows a player to end the game once 100 blocks (~10 minutes) have passed without a response from the other player. We had great ambitions for the NFTs which we simply ran out of time for, including many different kinds of power-up NFTs in addition to the Insurance power-up we did implement. The idea for these power-ups is that they can be burned in game to reveal additional hints/secrets or give its user unfair advantages in the game! Finally, just getting everything working on the Pulsar-1 testnet, including setting up a CORS proxy for the requests, and gracefully handling slow node response times took a fair bit of effort! Accomplishments that we're proud of Simply getting smooth interaction between the web application and the contract for a game with several states was very exciting, and we were particularly happy about a number of new features on both the front-end and back-end. We think we’ve created a unique on chain game experience that utilizes both randomness and user-provided information. Building the NFT reward component, we’ve provided a template for minting NFTs based on accomplishing a task (such as winning a game), rather than simply being the quickest purchaser. We were really proud to get a working example of a power-up NFT in the contract and have it work with the overall game logic. Giving back to the community We have open-sourced the entire game including the contracts and webapp :) What's next for prisnr.games For the hackathon we focused on a minimum viable product, but in the planning stage of this project we created a multi-page document of many additional features for prisnr.games which we plan to implement going forward! Perhaps what excites us the most are our plans for all of the intricate power-up NFTs ! Disclaimer: we decided to publish the demo version of prisnr.games on a private testnet since we were facing frequent network congestion and reliability issues on pulsar-1 that detracted from the game's user experience. We set up a 🚰 faucet and everything so that people can try out the game. <div