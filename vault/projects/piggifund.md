---
slug: "piggifund"
url: "https://devpost.com/software/piggifund"
title: "PiggiFund"
hackathon: "Hack to the Future 4"
organization: "Finastra"
winner: true
words: 642
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "substrate/financial_record"
---

# PiggiFund

> A crypto fundraising platform for the masses! Visualize deposits and withdraws into customizable fundraising contracts which utilize a use a fair, time based protocol to mobilize contributions.

[Devpost](https://devpost.com/software/piggifund) · hackathon [[Hack to the Future 4]]

## Facets

**mechanism** [[revocation_withdrawal]]
**substrate** [[financial_record]]

**stack** ethers.js, javascript, material-ui, react.js, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for piggifund

## Body

Inspiration I wanted to build a dApp which could help people and can have an immediate real world impact. Part of my inspiration was the conflict and Ukraine and how people in need were requesting crypto as funds for aid. Moreover, I was motivated to incorporate what I see as one of the most understandable components of Web3; specifically, crypto wallets which interact with the web browser and can provide personalization to an application interface and the actions available to a user. What it does PiggiFund is made of 3 separate tools bundled into the dApp. There is the PiggiFund Maker which allows non-devs to mint PiggiFund contracts. PiggiFund contracts themselves follow a protocol which makes use of time based fundraising. This can be seen in the second tool, the PiggiFund UI which people can use to interact with the PiggiFund contract and visualize deposits in and out of a contract, as well as a timer to visualize movement towards the end of a fundraising campaign. The final tool within PiggiFund is PiggiFund Contracts, a search tab, where people can transparently search all of the PiggiFund contracts by way of the contract description which have been deployed on chain. How we built it I built the dApp with Solidity smart contracts on the back end. There is an original PiggiFund contract which outlines the base protocol for the time constrained fundraising concept- in conjunction with a PiggiFund factory contract for customizing PiggiFund contract agreements. The front end is build out using React.js, Ethers.js and I used styling components from the Material UI library. Challenges we ran into I ran into all sorts of challenges which required adapting the original solidity contracts on the back end. This involved adding in additional emitter events so that the front end could pick up on all the needed data for a user. The front end also had its challenges with picking up on the transaction confirmations when a deposit or withdraw is made and updating all of the UI components accordingly. With the backend being completely on chain, I also had to figure out time conversions for block.timestamp from epoch time into human readable time within various parts of the app which was tedious. Accomplishments that we're proud of I'm proud of putting the dApp together, as one person working alone, because I visualized the concept in my mind and I had a lot of fun actualizing the idea over a period of 10 days using what I know about Solidity and React.js. What we learned I learned a lot about the Material UI library and I am much better with using functional components and hooks in React.js. I also learned about the challenges of having 100% of the back end of a dApp on chain- especially when it comes to confirming the actual time for a block timestamp or confirmation about transactions going though. As far as Solidity, I also learned a lot more about working in Gwei, Wei and Eth values and the math around conversion. Also I learned more about using emitter events to structure out my front end. What's next for PiggiFund For now I'm resting, but I have an ambition to grow the dApp. Ideally I'd love to get the smart contracts audited and then deployed to the Ethereum Mainnet. I'd also like to discuss the fundraising protocol and get additional ideas on how to make fundraising campaigns more engaging and fair. I'd like to improve the front end so the visualizations are not just bars going up and down but rather, something a lot more engaging and impactful. Moreover, eventually PiggiFund should be able to interface with more crypto wallets than MetaMask alone. Furthermore, the functionality of sending the "Golden Doner" a crypto based reward (like an NFT) through the PiggiFund platform would be an excellent feature to add. <div