---
slug: "nft-royalty-distribution"
url: "https://devpost.com/software/nft-royalty-distribution"
title: "Flexible NFT Royalty Distribution"
hackathon: "Hedera22: Hello Smart Contracts"
organization: "Hedera"
winner: true
words: 544
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/legal_justice"
  - "user/developer"
  - "user/legal_professional"
  - "substrate/financial_record"
---

# Flexible NFT Royalty Distribution

> Providing a more flexible rate based NFT Royalty Distribution process for stakeholders based on Smart Legal Contracts to assign distribution proportions based on the transfer value of the token

[Devpost](https://devpost.com/software/nft-royalty-distribution) · hackathon [[Hedera22- Hello Smart Contracts]]

## Facets

**domain** [[developer_tools]] [[legal_justice]]
**user** [[developer]] [[legal_professional]]
**substrate** [[financial_record]]

**stack** ergo, go, javascript, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nft royalty distribution

## Body

Inspiration While working with NFTS using the Hedera Tokenisation service we saw a need for the existing royalty distribution approach to be extended to deal with more real-world scenarios of distribution and allow for royalty distribution logic to change over the lifetime of the asset as royalties are renegotiated and new stakeholders added and removed. What it does This approach allows a more realistic and complicated distribution flow of royalties when transferring NFTs. Our approach takes the essence of a legal contract, represented in a Smart Legal Contract, that defines the terms and parameters of a royalty agreement that supports different percentages to be divided between multiple stakeholders dependant on the amount the token is transferred from. This approach allows NFT Royalty logic on Hedera to more fully represent the complexity involved in asset royalties and supporting intermediaries such as different rights holders and publishers and also the scope for this to change over time, for example if an NFT becomes a massive success and the terms are renegotiated, or certain rare NFTs or elements of a collection, are more valuable than others. How we built it Using a combination of HTS, Solidity Smart Contracts and Smart Legal Contracts and built using the Accord Project Smart Legal Contract platform. This platform facilitates building executable contract clauses which we use to determine the appropriate royalties based on the rates card defined in a legal agreement. We used the Go SDK initially, then finally we implemented everything in the JavaScript SDK. Challenges we ran into Lack of Oracle Support in Hedera Integration of Smart Legal Contracts with Smart Contracts Issues with deployment of large Smart contract binaries Getting access to token balances for non ERC-20 compatible tokens Lack of HCS integration with smart contracts as this wold have been a benefit Accomplishments that we're proud of The real world applicability of this approach for the legal industry when interacting with Hedera Applications allowing lawyers and developers to co build legally complex solutions involving a range of Hedera services. Bridging the intricacies of some of the realities of the legal world into something that can be reflected in a DLT implementation. What we learned We were familiar with HTS and HCS having represented a Smart Legal Contract as an NFT using HTS but we learned loads about how Hedera supports Solidity and how it differs from the Ethereum Ecosystem, while retaining lots of the familiar concepts for developers Hedera is like Ethereum on rails! The speed up is amazing and it really reduced development cycles having contracts deploy that quickly and transactions to finalise in such a short space of time. There are still some challenges ahead with lack of an ecosystem to provide secure off chain access via Oracles, hoping this will come over time. Maybe we can help! What's next for NFT Royalty Distribution We feel this lays the ground for more complex and robust integrations with Smart Legal Contracts and Hedera which can be a great combination. This also allows for a more flexible NFT ecosystem for token owners and other stakeholders. We hope to build on this and some of our other work in representing Smart Legal Contracts as NFTs on Hedera and look at other tokenised asset classes with legal complexity <div