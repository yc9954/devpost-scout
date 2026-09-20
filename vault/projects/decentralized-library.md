---
slug: "decentralized-library"
url: "https://devpost.com/software/decentralized-library"
title: "LEBIUM"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 554
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "user/general_public"
---

# LEBIUM

> A decentralized web3 private library where digital items in ones private library can be put up for sale on the public marketplace, when bought a copy of the item is made to the buyers own library

[Devpost](https://devpost.com/software/decentralized-library) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]] [[general_public]]

**stack** chainlink, chainlinkdatafeeds, hardhat, infura, ipfs, javascript, react.js, solidity, yarn

## How they structured the write-up

- inspiration
- what it does
- how we built it

## Body

home page Public Market Place Private Libruary Inspiration We wanted to build the largest Private and public decentralised digital items store that promotes freedom, direct interaction with lovers of your work, and having direct connection to digital item sales like ebooks, videos, audios, certificates in the fastest way possible We wanted people to have a safe secure private and permanent place to store private digital items like files, secretes etc, we also wanted people to be able to make money of the digital items they wish to make public, hence the public library market. We see this being used in the meta verse too, where do we want to store our files when in the metaverse? Lebium! What it does LEBIUM is a platform that helps store your files on the blockchain with the help of ipfs and lit protocol(we are still researching lit protocol to encrypt the ipfs cid). These files can be shared publicly to everyone in the world for free, files can also be uploaded privately and shared to another user, and lastly private files can be put up for public sales. How we built it We wrote a smart contract which contained the following:- A privateUpload function, for uploading contents privately, which takes in a name, link, description and category, which is then pushed to the private library array. A publicUpload function, for uploading contents publicly, which takes in a name, link, description and category, which is then pushed to the public library array. A share function, for sharing private library content, which takes in an array of addresses of receivers, and the item ID. A publicSale function, for putting up contents of your choice from your private library for sale publicly, takes in the array ID, and the price in USD (for user ease) you want to sell the content for. And the buyItem function, the most interesting part, which takes in the array ID of the content you want to purchase passed by the front end. For this, the payment is made in ether, even though the price in the publicSale function inputed is in dollars. We've achieved that by using the latest price of ETHUSD from the Chainlink Price feed to help us convert and always keep updating the price ## Challenges we ran into When we started using the Chainlink Price feed, we had to find a way to use int256 and uint256, as we were not used to using int256 from before, then we had to keep trying to figure the proper calculations to best use the latest price of ETHUSD ## Accomplishments that we're proud of We have learned a lot of things, and it's amazing that we were all able to come together to work on something that can be used by people in real life. We're most proud of our personal growth as developers ## What we learned We have learnt about ipfs , int, and the Chainlink Price Feed data ## What's next for LEBIUM We want to see how we can make this a more stable and efficient library. Perhaps become the biggest decentralised digital items store. We also want to perfect the litprotocol as a middle ware for encripting and decripting the ipfs content Id , that way it becomes completely private(reaserch is currently on going for this). <div