---
slug: "web3patreon"
url: "https://devpost.com/software/web3patreon"
title: "Web3Patreon"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 693
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Web3Patreon

> We want to offer a steady economy + Data ownership bypassing the middle man for Creators.

[Devpost](https://devpost.com/software/web3patreon) · hackathon [[EthCC Hack 2022]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[financial_record]] [[video_visual]] [[web_dom]]

**stack** celo, ceramic, cronos, gnosis, ipfs, next.js, orbis, polygon, privy, rainbow, sismo, solidity, vercel, wagmi

## How they structured the write-up

- inspiration
- what it does
- how we built it（technical）
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for web3patreon

## Body

Web3Patreon Our Value Position How We Built① How We Built② ※I am interested in continuing this project after the hackathon. Inspiration 1.After coming from Japan to Europe and Paris, I was very impressed by many artistic works and architecture and such history by artists. 2.Having heard that the creators of Patreon are really incurring a lot of fees to receive money from fans. Platform Margin is Expensive (8%) Payment processing fee (5% + $0.10 per transaction) Payout fees (1% per 1 transaction) Currency Conversion Fee (2.5% per 1 transaction) Cash-out takes a long time. No payments way for unbanked. 3.The knowledge of Ceramic and Orbis, a decentralized storage and social mechanism that does not belong to any other blockchain. What it does Creator can literally own contents. Steady Revenue by low transaction fee and cost. Innovation It is the encryption of content submitted by creators. To do this, we use Orbis and Lit Protocol technologies; existing similar services such as Unlock.Protocol only lock content, not encrypt it. If it is not encrypted, it is more centralized. Improved STEADY ECONOMY for creators through subscription NFT. Traditionally, using NFTs for membership was a "yes or no" proposition. A person who owned an NFT for a project had access to the benefits and community of that project for as long as he or she owned the NFT. From a creator's standpoint, this was OK, but not great: each NFT sold effectively gave the NFT holder "lifetime access." Web3Patreon innovates a membership NFT with an expiration date that takes into account the concept of time. Creators can issue NFTs that grant membership for any period of time. Use Case Sustainability The market is certain to continue to grow significantly in the future. Even without the value of the token economy, Crypto Payment and smart contract alone have value to customers, so there is reason to continue using blockchain-based Web3 products. It is a business model that is easy to monetize. We are very alining with our user very well. How we built it（Technical） Subscription NFT = Smart contract creation The app consists in 2 smart contracts, one is an implementation of ERC1155 from Openzeppelin, with the Ownable library to manage permissions, the other is a simple ERC1155 factory, called "CreatorFactory" to deploy instances for each new registered creator, those instances keep track of patron subscriptions, expiry times, and tiers edition (tiers are not available in the frontend, but the contract has the feature) smart contracts verifications for polygonscan: -> link -> link Low transaction fees = Usage L2 Chains (Polygon Mumbai, Celo, Cronos, Gnosis) Gated community to discuss with your best creators & connect with your followers = Orbis with Ceramic data network Attestation of creator = Using Sismo tech When a fan becomes a fan of a creator or decides to pay for a subscription, they are always concerned about the creator's track record. However, in the traditional world, creators could lie; in the Web3 world, it is easier to prove track record because data can be put on the on-chain, but the problem at this time was that creators had to expose their own Wallet Address. Sismo solved this problem by allowing creators to prove their achievements in the form of badges without exposing their wallet addresses. Upload images format for creators = IPFS Tech « Roadmap » Notification system via email without privacy risk = Using Privy tech Challenges we ran into Implementation of a Token Gateway feature that will allow fans to view closed content from creators when they actually purchase NFTs with cryptopayments. Accomplishments that we're proud of Launched the product on actually website and main net on the blockchain and ceramic. What we learned Using Orbis.SDK based on Ceramic Network will best way to build Web3 Social. What's next for Web3Patreon Gather 10 web3builders and creators to recruit test users. Use Privy.io to implement notifications of posts. Livepeer and others to support a variety of submission formats. Support for a variety of payment methods using Crypto.com, etc. Refine the design of the flow from user onboarding to submission. Refine the editor's experience when creators submit their work. Mobile App Released <div