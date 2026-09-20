---
slug: "a-porting-of-metamask-keyringcontroller-for-hedera-hashgraph"
url: "https://devpost.com/software/a-porting-of-metamask-keyringcontroller-for-hedera-hashgraph"
title: "A porting of Metamask KeyringController for Hedera Hashgraph"
hackathon: "Hedera22: Hello Smart Contracts"
organization: "Hedera"
winner: true
words: 150
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "substrate/code_repository"
---

# A porting of Metamask KeyringController for Hedera Hashgraph

> A module for managing groups of Hedera Hashgraph accounts called "Keyrings" adapted from MetaMask's Keyring Controller.

[Devpost](https://devpost.com/software/a-porting-of-metamask-keyringcontroller-for-hedera-hashgraph) · hackathon [[Hedera22- Hello Smart Contracts]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]]
**substrate** [[code_repository]]

**stack** javascript, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for a porting of metamask keyringcontroller for hedera hashgraph

## Body

Jest Test Result Inspiration This is a module for building a robust client-side, browser extension that enables the creation of decentralized applications on Hedera. What it does The KeyringController has three main responsibilities: Initializing & using (signing with) groups of Hedera Hashgraph accounts ("keyrings"). Keeping track of local nicknames for those individual accounts. Providing password-encryption persisting & restoring of secret information. How we built it I forked a MetaMask/KeyringController codebase and port all ETH functions using the hethers.js wrapper. Challenges we ran into KeyringControler codebase is non-trial. Lots of internal and external dependencies made porting difficult. Accomplishments that we're proud of Managed to build a working module for a robust client-side, browser extension. What we learned Managed to review the entire codebase of Metamask and its architect. What's next for A porting of Metamask KeyringController for Hedera Hashgraph Porting of all remaining controllers and Metamask Extension for Hedera Hashgraph. <div