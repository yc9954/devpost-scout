---
slug: "fractron-fractional-nfts"
url: "https://devpost.com/software/fractron-fractional-nfts"
title: "Fractron - Fractional NFTs"
hackathon: "TRON Grand Hackathon - Season 3"
organization: "TRON DAO"
winner: true
words: 446
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/video_visual"
---

# Fractron - Fractional NFTs

> Are you priced out of buying a bored ape? Or maybe a cryptopunk? Look no further! With Fractron, anyone can create fractions of NFTs that are then tradeable. You can now own 1/1000 of a bored ape!

[Devpost](https://devpost.com/software/fractron-fractional-nfts) · hackathon [[TRON Grand Hackathon - Season 3]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[video_visual]]

**stack** javascript, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fractron - fractional nfts

## Body

Inspiration After seeing how expensive NFTs can get (especially in bull markets), we think that every crypto ecosystem needs to have platform for fractional NFTs. With everyone being able to own fractions of the most popular NFTs, everything gets more fun. Another inspiration was the idea of "NFT Index Funds", which we will explain down below. What it does In simple terms, you take one or more NFTs and divide them into fractions. More detailed, it goes like this: Alice buys a bored ape, but she later wants to sell parts of it. Alice goes to Fractron, and "splits" her Bored Ape (TRC721 token) into a "vault". When she does this, she is creating a TRC20 token that represent the bored ape. When creating the vault, she chooses the name, symbol and supply. As you might understand, the TRC20 supply is the number of fractions. Now this TRC20 representation of the bored ape is tradeable like a normal TRC20 token. This means that Alice can add liquidity for it on e.g sunswap, and now everyone can buy and sell the bored ape fractions! If she ever wants the whole bored ape again, she just needs to buy all the fractions, go to Fractron and "join" the vault! You are not limited to fractionalize a single NFT from a single collection, you can put multiple NFTs from multiple collections into your vault. Because of that, another thing you can do is: Create something we like to call "NFT Index Funds". Imagine that you are the fund manager, and you buy for example 5 bored apes, 5 crypto punks and 10 tronninjas. You can then fractionalize all of these NFTs, and sell the fractions to people that want exposure to your fund! How we built it We are a group developers that specializes across the whole stack, so everyone worked on everything. We are using solidity for our smart contracts, and react.js for the frontend! There is no intermediate backend involved, so everything is on-chain. Challenges we ran into There were no major challenges! Accomplishments that we're proud of That you can fractionalize multiple NFTs from multiple collections. This is what makes it possible to create these "NFT Index Funds". What we learned That the shasta testnet is to be preferred over the Nile testnet when dealing with NFTs. Mainly because it is what's supported by apenft. What's next for Fractron - Fractional NFTs Make it possible to fractionalize TRC1155 tokens. Make it possible to fractionalize INTO a TRC1155 token, instead of into a ERC20 token. This will make it possible for the vault to have an image representation. Work on the user interface. Gas-optimize the contracts. <div