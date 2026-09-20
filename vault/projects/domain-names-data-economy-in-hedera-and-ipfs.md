---
slug: "domain-names-data-economy-in-hedera-and-ipfs"
url: "https://devpost.com/software/domain-names-data-economy-in-hedera-and-ipfs"
title: "Domain Names & Data Economy In Hedera and IPFS"
hackathon: "Hedera22: Hello Smart Contracts"
organization: "Hedera"
winner: true
words: 250
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# Domain Names & Data Economy In Hedera and IPFS

> Link domain names to blockchain addresses. Be "yourwebsite.com" on the blockchain, allowing: -Identity -Secure data sharing & monetization without oracles -SSL-like verification of IPFS content

[Devpost](https://devpost.com/software/domain-names-data-economy-in-hedera-and-ipfs) · hackathon [[Hedera22- Hello Smart Contracts]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[web_dom]]

**stack** hardhat, javascript, node.js, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for domain names & data economy in hedera and ipfs

## Body

Inspiration We think Web2 data contains various hidden gems which can be verified without oracles. Before this project, I was wondering the utility of verifying SSL certificates could be. Turns out, it can solve a significant part of the oracle problem, while improving data markets' efficiency and enabling more institutional adoption. Importantly, it can also enable signing of statically-hosted IPFS content. Upon discussing this with Caleb, we decided it would be perfect to build for this hackathon on Hedera, where the fees are low and the institutional adoption is growing. What it does It enables domain names to be linked with Hedera address by verifying SSL certificates. How we built it We used Solidity and plenty of EVM assembly Challenges we ran into Parsing ASN.1 DER SSL certificates is difficult in Solidity. So is verifying an RSA signature using the 0x05 modular exponentiation precompile. Anti-frontrunning was also an obstacle, which we overcame via a commit-reveal cryptographic scheme. Accomplishments that we're proud of -Solving part of the oracle problem -Becoming proficient in EVM assembly -Writing well-organized code -Enabling a technology with significant potential to change the how organizations and website-owners interact with Web3 What we learned -Math behind RSA signatures -Familiarity with EVM assembly What's next for Domain Names & Data Economy In Hedera and IPFS There are a few short-term goals for this: Writing better documentation Enabling Web2 developers to communicate with the blockchain from their website's URLs using familiar programming languages Spreading the word about this new tech <div