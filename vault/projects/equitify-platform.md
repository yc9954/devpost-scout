---
slug: "equitify-platform"
url: "https://devpost.com/software/equitify-platform"
title: "Equitify Platform"
hackathon: "NEAR MetaBUILD III Hackathon"
organization: "NEAR Protocol"
winner: true
words: 573
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/web_dom"
---

# Equitify Platform

> Launchpad with tokenized IDOs. Tokenization of IDOs allows for the purchase of IDO positions as well as insurance to them, even before TGE, without trading the underlying tokens directly.

[Devpost](https://devpost.com/software/equitify-platform) · hackathon [[NEAR MetaBUILD III Hackathon]]

## Facets

**domain** [[finance_payments]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** near, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for equitify platform

## Body

Viewing list of NFTs IDO Page Accepting Insurance offer as an insurance provider Inspiration In recent times we see a lot of tokenization going on. For instance, tokenization of DeFi positions like on uniswap.org, and bumper.fi - they wrap your liquidity positions into NFTs, allowing you to trade them, or create options from them. NFT is a powerful tool in the way that it is a common interface for people to trade anything. So, even things like liquidity positions, or any "position" or "state" you have in any protocol allowing you to benefit from it - could be wrapped into an NFT and it would enhance the economics of the entire ecosystem of a blockchain because you could create insurance, trade, and do a lot of things with that NFT. It would allow the creation of protocols based on protocols, just as we did this month on this hackathon. What it does We saw that all the launchpads running on EVM and NEAR chains, run IDOs but don't mint NFTs for that. This creates a problem with liquidity - users can't sell their position, or buy insurance for it. Also, if a user's private key gets exposed, they can't transfer their IDO state to a safe account. We decided to change that architecture by minting an NFT for every IDO participation you make. If you get an IDO position, you should get an item representing that. This solves the problem with liquidity and safety - now users can trade their right to claim tokens from IDOs, and it creates a more fair market and also a more liquid market on the blockchain. Beyond that, users can now transfer IDOs to their other accounts in case they have problems with the security of their initial account. How we built it We decided to use TypeScript for both front-end and smart contracts. It's very cool that NEAR has support for TypeScript. We used React as well. We attracted our friend designer to design a good website, then wrote smart contracts and front-end for that. Challenges we ran into One problem that we saw in the NEAR ecosystem is that it doesn't have a similar to the EVM ecosystem's TypeChain. TypeChain is a thing that goes runs through a smart contract's code and generates ready-to-use functions in TypeScript. Had we had it, we would've speeded up the development a couple of times. But anyway, TypeScript smart contract is a great thing itself and I really fell in love with NEAR for that. Accomplishments that we're proud of We learned NEAR blockchain and smart contracts, and how it functions. Previously we were thinking it was too difficult and we didn't touch it xD. But it's incredibly simple (except for manual typing - TypeChain would be the #1 thing I would add to the NEAR ecosystem as an end programmer) What we learned There are a lot of things to enhance in each product, even if it's a ready product. For example, even if there are existing launchpads on NEAR - we can still build something better, for instance, tokenization in launchpads, etc. What's next for Equitify Platform It's a ready product from the development perspective. The next step is incubation, marketing, and business development. Receive feedback from the NEAR team Discuss potential partnership with NEAR blockchain and existing launchpads on NEAR; Launch the launchpad on NEAR and partner with startups that want to launch on it; <div