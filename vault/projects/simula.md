---
slug: "simula"
url: "https://devpost.com/software/simula"
title: "Simula"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 425
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# Simula

> Stake or deposit as your NFTs as collateral, a complete NFT utility platform

[Devpost](https://devpost.com/software/simula) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**domain** [[finance_payments]]
**substrate** [[document_pdf]] [[financial_record]]

**stack** chainlink, moralis, next.js, solidity, web3.storage

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for simula

## Body

Inspiration Suppose you own a pair of Jordan shoes in some metaverse and know you won't be entering metaverse anytime soon. So what's that dormant NFT doing in your wallet? This platform provides utility to your NFTs. What it does Get a utility for it at our platform, either giving it as collateral and taking some amount in stable coins or lending it to us and enjoying some interest monthly : ) List your NFT as collateral and get a loan upto 40% of NFT value from us in USDT . Once you hit the button, your NFT gets transferred into an escrow smart contract for the loan duration. Repay the loan after the duration with 4% interest in a duration of 1 month. If you default, our DAO can foreclose your NFT. Collateral duration can vary between 1 month to 4 months. This time period is decided to avoid NFT fluctuations. The amount is given in USDT for the same reason. Lend us your owned NFT and receive a regular monthly 4% to 7% interest. Once you hit the button, your NFT gets transferred into a smart contract. A DAO will now be able to access your NFT. It will be performing some businesses like renting your NFT to an exhibition or a user and yielding interest in it. It will cover the 7% provided to you and eventually try to earn more than that. The extra earnings of DAO will be divided among its members. A user can become a DAO member by stake 1 Matic. After your Lending duration, your NFT will be returned to you. Pdf of the project How we built it We built this using Next.js and solidity. Moralis is used for fetching Nfts. For storing the receipts data, web3.storage is used. And for getting external matic/usdt data on Mumbai blockchain, Chainlink is used. Challenges we ran into This project took me 4 weeks. The first challenge was to come up with the contract logic and to debug all errors on the way. Dealing with decimals inside contracts. Then while integrating the contract with the frontend, there were loads of functions fetching data from the contract so again there were lots of bugs in this process. Accomplishments that we're proud of Successfully implemented the idea within the hackathon time frame. What we learned I have learned about Chainlink. Also, a lot about the interaction between contracts and working with decimals inside them. What's next for Simula Will be extending the idea further to create a complete NFT utility. <div