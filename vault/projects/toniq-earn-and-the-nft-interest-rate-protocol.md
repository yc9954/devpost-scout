---
slug: "toniq-earn-and-the-nft-interest-rate-protocol"
url: "https://devpost.com/software/toniq-earn-and-the-nft-interest-rate-protocol"
title: "Interesting NFT Protocol & Toniq Earn"
hackathon: "Supernova "
organization: "DFINITY Foundation"
winner: true
words: 953
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "substrate/regulation_legal_text"
  - "substrate/sensor_telemetry"
---

# Interesting NFT Protocol & Toniq Earn

> A decentralized interest rate protocol where users can borrow ICP using NFTs as collateral, or earn interest (or discounted NFTs) for ICP deposited into the protocol.

[Devpost](https://devpost.com/software/toniq-earn-and-the-nft-interest-rate-protocol) · hackathon [[Supernova]]

## Facets

**domain** [[finance_payments]] [[legal_justice]]
**substrate** [[regulation_legal_text]] [[sensor_telemetry]]

**stack** motoko, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for interesting nft protocol & toniq earn

## Body

Inspiration There are only a few places you can put your ICP to earn: (1) the NNS, (2) Sonic, or (3) flipping NFTs. The NNS provides a decent rate for your ICP, but it locks up your ICP for a long period of time so it is no longer liquid, Sonic doesn’t offer very high yield rates on their liquidity pools, and flipping NFTs means you are putting a substantial amount of your ICP into less liquid NFTs that you may or may not be able to sell. Toniq Earn’s goal is to provide yield in a more liquid form than the NNS, provide interest rates that are substantially higher than Sonic’s liquidity pools, and give NFT accumulators a place to go to leverage their NFTs for additional liquidity. What it does Toniq earn is powered by the Interesting NFT Protocol, a decentralized interest rate protocol. Here’s how it works: Alice decides she needs more ICP to take advantage of a new NFT collection coming up, and wants to lock up her BTC Flower to get 200 ICP for the next month, so she fills out an Earn Request and says she’ll pay 10% interest. Bob loves the BTC Flower collection, and has been wanting to earn a good yield on some extra ICP, so he accepts Alice’s protocol contract and his ICP is sent to Alice via the protocol. At this point, one of two things could happen depending on whether Alice repays her contract in time or not. If Alice repays her contract (plus interest) which in this case would be 220 ICP, then she gets her BTC Flower back, Bob gets the 220 ICP, and everyone is happy. If Alice can’t repay her contract, or decides not to, then the BTC Flower NFT is sent to Bob and the contract is fulfilled. The beautiful thing about an over-collateralized contract like this is it removes default risk. Bob knows that at the end of the contract, he is either going to get 220 ICP or a BTC Flower, and either one of those scenarios feels really good to Bob. Same story with Alice. Alice knows that she can get additional liquidity now, and if she pays it back with interest she keeps her NFT, or if she doesn’t pay it back, she can keep the originally acquired ICP at the expense of losing her NFT. How we built it We built Toniq Earn and the Interesting NFT Protocol using a canister controlled escrow system based on sub-accounts. Users transfer NFTs to the canister and the canister holds them in escrow for the duration of the contract. The canister is blackholed, and thus completely decentralized, which is important as there are significant legal challenges to releasing a product like this. Toniq Earn could be viewed as a sort of peer-to-peer lending tool, but we prefer interest rate protocol over peer-to-peer lending as there is no trust required between two parties to interact with a decentralized protocol where outcomes are known and governed by code. Challenges we ran into Releasing a product and a decentralized protocol is a big undertaking. There are security concerns, spam/protocol abuse concerns, cycles funding concerns, etc. Our biggest challenge was ensuring we were building a secure, safe protocol that anyone could use. Up until this past week, we were still finding small edge cases where Accomplishments that we're proud of Building one of the first (if not the very first) functional lending solutions on the #IC feels like an amazing accomplishment. We know there are other groups working on lending tools, but this will at least be one of the first. And being able to use NFTs as collateral for these loans feels extra good because we are so deep on everything to do with NFTs. It was about time we added a DeFi feature to Entrepot. We specifically don’t call this a lending tool because of the current regulatory environment, which is why we refer to it as an interest rate protocol. What we learned We learned that one does not simply release a peer-to-peer lending product in the US. There are massive regulatory issues. Peer-to-peer lending is a highly regulated industry, so we had to position and build our product in a way that was legally compliant, yet still functional and easy to use for our users. The safest and best solution was (1) repositioning the protocol as an interest rate protocol rather than a lending platform, (2) fully decentralizing the protocol and building a frontend for Toniq Earn, and (3) blocking US IP addresses from using the Toniq Earn features. We would have liked to include all IP addresses, but unfortunately it is not wise to do so right now. We will continue to adjust our policies as we learn more over time from legislators about US crypto regulation. What's next for Interesting NFT Protocol & Toniq Earn Right now the Interesting NFT Protocol (the decentralized blackholed backend protocol) does not have a controller. This means it cannot be updated or adjusted. We would eventually like to decentralize the protocol via the SNS into a DAO, so the DAO would be governing the protocol. This enables updates and changes not possible with a blackholed canister. We also have a whole set of new features that we would like to add, assuming we push out a second version of the protocol. For example, including multiple NFTs in the same protocol contract at the same time, incorporating NRI or other rarity metrics in our NFT collection floor evaluations, or expanding the protocol to include pools of NFTs and ICP for immediate swapping rather than having to wait for liquidity in contracts (as in the current implementation). <div