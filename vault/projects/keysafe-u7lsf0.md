---
slug: "keysafe-u7lsf0"
url: "https://devpost.com/software/keysafe-u7lsf0"
title: "Keysafe Protocol"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 515
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/structural_withholding"
  - "domain/security_privacy"
  - "user/general_public"
---

# Keysafe Protocol

> Keysafe protocol is the missing layer between Web2 and Web3 that connects Web2 and Web3 accounts in a decentralized and trustworthy way.

[Devpost](https://devpost.com/software/keysafe-u7lsf0) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[provenance_signing]] [[structural_withholding]]
**domain** [[security_privacy]]
**user** [[general_public]]

**stack** bls, c++, polygon, rust, secretsharing, smartcontract, tee

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for keysafe protocol

## Body

Keysafe is the missing layer between Web2 and Web3 that connects users' Web2 and Web3 accounts in a verifiable and private way. Inspiration Background 1: Managing Web3 accounts could be cumbersome, unfriendly to users, and vulnerable to hacking. Based on research by ChainAnalysis, the number of lost bitcoins due to account loss reached 3.79 million($150 billion). Background 2: Web3 Dapps cannot access users’ Web2 profiles and social graphs in a decentralized, verifiable, and private way. The key problem: account systems in web2 and web3 are natively separate, technically unconnected, and even inherently in conflict with their value . What it does Keysafe Protocol is the missing layer between Web2 and Web3 that connects users' Web2 and Web3 accounts in a decentralized, verifiable, and private way. With the connection, users can leverage the linkage to authorize DApps to access their own Web2 data through the Web3 account signature in a trustless and verifiable way. Reversely, users can also manage and restore their Web3 keys through the Web2 verification. How we built it On-chain Keysafe deployed smart contract on Polygon networks. The contract provides the registration function of the Keysafe node. The public key of the node's TEE environment can be verified on the contract. If the node has any misconduct, the contract will also deduct the node pledge accordingly. At the same time, users can authorize Web2-Web3 Profile in the Keysafe contract. Off-chain The Keysafe protocol uses Secure Multi-party Computation (MPC), Threshold BLS Signatures, and Trusted Execution Environment (TEE) technology to manage private keys and allows owners to access with a customized combination of Web2 third-party authentication services including SMS, email, Google, and even Web3 address. Keysafe created Decentralized OAuth by combining TEE MPC and OAuth technologies. We named it “DAuth”. DAuth allows users to complete the authentication of profiles such as Google, Twitter, Github, etc., and bind them to the user's Web3 account in a decentralized way. The binding information is encrypted by TEE and stored in Filecoin/IPFS. Github: https://github.com/keysafe-protocol/ShuttleRun Challenges we ran into To let more Web3 projects adopt and integrate Keysafe to form an ecosystem and hence gain a huge user base gradually; To maximize the value of user profile data in Web3 while ensuring users’ data security and privacy; Accomplishments that we're proud of We are successfully applied for Web3 Foundation Grants We got a 3-rd prize in Web3 Hackathon We have won the 1st Prize in the Boba Network x DoraHacks hackathon . What we learned We talked to lots of Web3 native projects of DID and Web3 social. They are looking forward to integrating with Keysaf with a lightweight decentralized Social KYC verification service at the beginning. Decentralized social KYC does not touch the user's private key, it is easier to promote. What's next for Keysafe Protocol We will design and implement an on-chain tokenomics system to incentivize necessary parties in the protocol. Support more TEE implementations, such as Trusted Zone of ARM, and SEV of AMD to level up the security; Explore more possibilities in the composable Web3 Lego, including DID integrations, Web3 social graph, and Web3 Advertisement. <div