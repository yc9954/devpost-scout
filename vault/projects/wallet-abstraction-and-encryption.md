---
slug: "wallet-abstraction-and-encryption"
url: "https://devpost.com/software/wallet-abstraction-and-encryption"
title: "Wallet Abstraction and Encryption"
hackathon: "Privacy4Web3 Hackathon"
organization: "Oasis Foundation"
winner: true
words: 732
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/privacy_tech"
  - "domain/developer_tools"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Wallet Abstraction and Encryption

> Abstracting wallets and encryption for users to allow for private transactions and encrypted data transfer.

[Devpost](https://devpost.com/software/wallet-abstraction-and-encryption) · hackathon [[Privacy4Web3 Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[privacy_tech]]
**domain** [[developer_tools]]
**substrate** [[financial_record]] [[video_visual]]

**stack** amazon-web-services, hardhat, node.js, postgresql, python, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for wallet abstraction and encryption

## Body

Inspiration Our inspiration was finding a simple way to enable non-sapphire users to get the privacy and security benefits of the Sapphire Paratime. Some of the conditions we wanted to maintain was that users did not need to disconnect their browser extension from their current network, would be able to get end-to-end encryption, and would get trustless relaying for all actions other than relaying the host blockchain's state (which can be trust-minimized via a messaging bridge). What it does The Project demonstrates a fully privacy preserving implementation on Arbitrum that uses Sapphire as its privacy layer. In addition, we used the lessons learned in implementing this to put together a reference implementation for wallet abstraction on sapphire. The wallet abstraction builds on top of the tooling developed as we built the privacy preserving ERC20 implementation. How we built it This was built from scratch, utilizing OpenZeppelin for the ECDSA and EIP712 libraries and the Sapphire libraries for Ethereum and Sapphire signing. The rest was done by designing and implementing an end-to-end encrypted pipeline for building on top of Sapphire while remaining connected to an external blockchain. We tested on a local Sapphire instance using the private docker image, and were able to deploy our application on Arbitrum and Sapphire mainnnet. The trustless relaying utilizes AWS with API Gateway and Lambda. We used the sapphire SDK for our Javascript relayers, for encryption and signing. We have a couple lambda functions using API Gateway on AWS that allow for trustless relaying of encrypted user actions. Challenges we ran into Building this so we weren't susceptible to griefing attacks was a challenge. There's a lot of things that become much simpler if you aren't concerned about this type of attack vector. For example, it's easy to encrypt a user transaction, but if you encrypt it and trustlessly relay it with no information, you could potentially be exposed to griefing by being tricked into relaying a pointless transaction. At the same time, it's important to encode a way that Sapphire can verify the transaction has some direct benefit to the relayer without exposing anything about the transaction. To mitigate this we created a custom End to End Proxy that only allowed for invocations to specific methods on a specific address. Accomplishments that we're proud of We accomplished our goals and built a working prototype that brings fully trustless transactions to Sapphire without the user ever needing to disconnect from the host chain. We found that we were able to provide a fairly low friction use case for EIP712 that allowed for encrypted, trustless relaying. This information helped us build an additional wallet abstraction framework that we hope to continue developing. What we learned A lot about EIP712, Deoxys-II, ethereum signing, and building multichain applications. We did a lot of experimentation with user experience to find an end to end experience that meets the security and usability requirements. We also learned a lot about how Sapphire works, and were able to better understand the way Sapphire makes eth_call invocation secure and how to locally deploy a test instance of the Sapphire chain. Likewise we figured out a strategy for user specific message encryption, trustless relaying, and preventing replays and griefing attacks when building on Sapphire and using the Privacy Layer. We were able to develop some strategies to minimize the complexity and remove the trust requirements, so our applications maximize the benefits to potential relayers. In doing this we only require unidirectional bridges to Sapphire, and are able to provide a seamless user experience. What's next for Wallet Abstraction and Encryption We want to build a larger framework for the wallet abstraction and encryption. Now that we have a good end to end implementation for the privacy preserving transactions, we have the knowledge and understanding to enable much more progressive use cases. We're excited to continue developing in this direction and think there's a lot of really exciting tools that will be unlocked when users are able to trustlessly delegate their funds to an external party and provide policies for management of this wallet. It turns the wallet into a regular Solidity objects that can be programmed just like anything else in DeFi. Likewise, now that we have a way for users to trustlessly interact with Sapphire, we think there's a lot of cool applications we'd like to build on top of the privacy preserving technologies. <div