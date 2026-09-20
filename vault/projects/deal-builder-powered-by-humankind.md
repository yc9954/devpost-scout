---
slug: "deal-builder-powered-by-humankind"
url: "https://devpost.com/software/deal-builder-powered-by-humankind"
title: "Deal Designer, powered by HumanKind"
hackathon: "Hedera22: Hello Smart Contracts"
organization: "Hedera"
winner: true
words: 544
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/financial_record"
---

# Deal Designer, powered by HumanKind

> A low-cost, easy-to-use platform for creating highly-customizable product offers that incentivize sharing and give back to the community with HumanKind's transparent, decentralized charitable match.

[Devpost](https://devpost.com/software/deal-builder-powered-by-humankind) · hackathon [[Hedera22- Hello Smart Contracts]]

## Facets

**domain** [[retail_commerce]]
**user** [[small_business]]
**substrate** [[financial_record]]

**stack** amazon-web-services, hashconnect, hashpack, hedera-consensus-service, hedera-contract-service, hedera-distributed-identity, hedera-file-service, hedera-token-service, node.js, postgresql, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what we learned
- challenges we ran into
- accomplishments that we're proud of
- what's next for deal designer, powered by humankind
- closing thoughts

## Body

Inspiration Currently, for someone who owns a small business, creating product offers and coupons is probably a loss leader; meaning they’re likely losing money in hopes of gaining customers through return business or in-store purchases. Whether they’re using traditional coupons, inserts, social media, or apps like Groupon and uber eats, all of them come with a major price tag and take a lot of time to get right. And all that’s wasted if the marketing doesn’t work. What it does The HumanKind Deal Designer is a low-cost, easy-to-use platform for creating highly-customizable product offers--offers that incentivize sharing and are behaviorally driven, have ZERO transaction fees, and best of all, continuously give back to the community with HumanKind's transparent, decentralized charitable match. See the video: link How we built it Our solution is architected using a hybrid-dApp approach, with the foundation being laid on Hedera's high-speed, low-cost decentralized services infrastructure. Our interaction layer for the hashgraph is composed of React, NodeJS and PostgreSQL, and allows merchants and users to register on the platform and create accounts with Hedera Distributed Identity and Verifiable Credentials . Wallets are linked using HashPack's HashConnect , allowing merchants and users to securely interact and provide approval of transactions. Merchants can use our Deal Designer to create rule-based offers, leveraging our Hedera Smart Contract 2.0 built with Solidity and deployed using the Hedera File Service . Users can find and purchase offers, sending USDC minted using Hedera Token Service , to the smart contract. As milestones of the offer are met, the smart contract automatically transfers volume discount and donation funds back to the user and charity. The offers, purchases and donations are timestamped using Hedera's Consensus Service ; providing a layer of trust, with the data immutable, verifiable and fairly ordered. What we learned Minting tokens using Hedera Token Service and automatically facilitating transfers between merchants, users and charities worked great within the EVM-compatible ecosystem. Challenges we ran into Our vision for what we want HumanKind and the Deal Designer to become is very ambitious and so far, our biggest challenge has been time. Ideas can sometimes come quickly, but the true value of the idea is only realized through thoughtful execution of design, development and marketing; and those in aggregate always seem to take longer than expected. Accomplishments that we're proud of We’re thankful to have such a diverse team, with a broad breadth and depth of knowledge and experience across industries. The accomplishment we're most proud of is preparation, dedication, focus and tenacity we all exhibited to design, develop and deliver a functional version of our concept in such a short period of time, and we're looking forward to seeing the positive impact it can provide in the wild. What's next for Deal Designer, powered by HumanKind We’re obsessed with bringing this to market, and next we’d like to focus on establishing key partnerships with businesses that believe in our cause-based foundation of kindness, and work to deliver natural and seamless end user experiences. One example in taking this next step is working with a partner to implement Fiat-to-USDC settlement during transactions; bridging the gap between the future of how business will be conducted and the usability expectations of our mainstream audiences. Closing thoughts HumanKind. Be Both. <div