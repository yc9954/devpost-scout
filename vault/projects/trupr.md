---
slug: "trupr"
url: "https://devpost.com/software/trupr"
title: "TruPr"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 494
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
---

# TruPr

> TruPr is a platform that allows for trustless advertising agreements (a brand mention in a Twitter post for example). Funds are locked in the smart contract and Chainlink oracles verify the agreement.

[Devpost](https://devpost.com/software/trupr) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**substrate** [[structured_db]]

**stack** avalanche, chainlink, express.js, hardhat, moralis, node.js, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for trupr

## Body

Inspiration The blockchain space is rapidly developing and marketing has become a key aspect that can spell either success or failure for many projects. Although it is a crucial aspect, the tools to make it easier, more accessible, and trustless, are lacking. As NFT creators we've come into contact with our own fair share of trouble when looking for marketing, that inspired us to create TruPr. TruPr takes trust out of the equation and lets everyone focus on what they do best, be it creating, developing, or marketing. What it does TruPr offers the creation of decentralized and trustless marketing agreements between two parties, as well as the publishing of "Public" agreements which can be fulfilled by anyone who meets the requirements. How we built it The solution consists of: 1) The TruPr Smart Contract This is the main part of the platform. The contract manages all agreements, their balances, calls the chainlink nodes, and pays out rewards. The smart contract is deployed on the Avalanche Fuji Testnet and the Kovan Testnet. 2) The Chainlink node and External Adapter The external adapter makes calls to social media APIs (currently only Twitter) and checks if the required post has been made and how it is performing. It then returns that information to the smart contract. We are currently running our own nodes as well as the adapter. 3) The database We are using Moralis to authenticate users and as our database, to store information that would be inefficient to store on-chain. 4) The UI The UI is a React app deployed on Netlify, with a Node JS proxy server deployed on Heroku for making Twitter API calls. The server is there so users can get information if they have met the requirements of the promotion without expending gas, it is only informational and has no function in the logic of the application or smart contract. Challenges we ran into Deploying our own nodes and external adapter on multiple chains Ensuring that users can't fulfill public agreements multiple times with the same accounts Figuring out how to authenticate users Twitter accounts in a permissionless manner Accomplishments that we're proud of We're proud of what we've managed to accomplish during this Hackathon. This project was full of firsts for us, we've: Deployed our own Chainlink node Built our own External Adapter Developed the smart contract Developed the UI and the server Interacted with a bunch of different APIs Made and successfully fulfilled the first trustless and decentralized marketing agreement What we learned How to run a Chainlink node How External Adapters work How to use Moralis for authentication and DB How to build a full-fledged Dapp from the ground up What's next for TruPr Decentralizing (even more) the EA and CL Node logic, so anyone can run their own Implementing fuzzy text recognition to allow for more flexibility Adding support for Discord, Instagram, and many more Adding different kinds of rewards (ex. NFT rewards) for agreements <div