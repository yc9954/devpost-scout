---
slug: "safe-alert-plg1so"
url: "https://devpost.com/software/safe-alert-plg1so"
title: "Safe Alert"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 889
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "domain/security_privacy"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Safe Alert

> Safe Alert is a dApp that protects the White Hats' interests by providing them with a secure way to alert protocols of detected bugs and a way to assess publicly their skills and contributions.

[Devpost](https://devpost.com/software/safe-alert-plg1so) · hackathon [[EthCC Hack 2022]]

## Facets

**domain** [[labor_employment]] [[security_privacy]]
**substrate** [[financial_record]] [[structured_db]]
  <sub>weak: code_repository</sub>

**stack** adobe-illustrator, alchemyapi, css, filecoin, ipfs, javascript, kleros, photoshop, polygon, privy, react, sismo, solidity, typescript

## How they structured the write-up

- 1) sending a secured bug alert through privy and ipfs
- 2) using kleros as a bug certifier to defend white hat's interests
- 3) providing white hats with sismo certification badges “proof of hat”

## Body

Safe Alert Logo Welcoming Page: Submit a bug Submit Bug Form Minting Sismo Certification "Proof of Hat" Badge Bug Submission Process Sismo "Proof Of Hat" Certification Badge Minting Process Kleros Bug Certifying Dispute Process Identified Problem Today's way for white hat to alert a protocol of a bug is to use traditional communication tools. The first problem is that the bug information is critical and they have to trust the security of the used communication tool. Secondly, there is no public fingerprint that could be used to certify the skills and contribution of the white hat (especially in the case where bug bounties are involved and that the white hat expects to be paid!). Thus, the white hack has no choice but to trust and rely on the company to assess their contribution. This also tends to increase the shortage of white hats and cybersecurity contributions because of that unbalanced relationships between white hats and protocols. What we Built to solve it We developped Safe Alert, a dApp that combines Privy, IPFS, Sismo, Kleros, Polygon and Alchemy technologies to create a secure way for white hats to create bug alert and to have a public certification of their skills and contribution. We have thus the three following properties: The bug information is secured by open source code so the integrity of the company is preserved The dApp provide the white hats with public assets (NFTs) to prove with Kleros their contributions in case of dishonest behaviour by the company Those public assets are a useful tool for white hack to showcase them and to establish their public and professional reputation How we built it 1) Sending a secured Bug alert through Privy and IPFS To secure the bug alert we integrated Privy and IPFS to Safe Alert so that the information filled by the white hat is encrypted and hosted on IPFS, and is only readable by the involved protocol. At the same time, we use NFT technology to mint a ERC-721 that contains within its metadata the link toward the encrypted data, a hash that acts as a proof that the encrypted data is unaltered, the blockchain address of the white hat alert creator, and a certification status that can take two values "certified" and "not certified". 2) Using Kleros as a Bug Certifier to defend White Hat's interests To enforce justice, if the white hat encounters a problematic situation with the involved protocol (protocol didn't pay the bug bounty, protocol didn't certify the NFT related to the bug detection) the white hat can open a Kleros dispute where jurists will be granted access to the encrypted data to investigate and give their verdict. The irrefutable asset the jurists will mainly use is the "proof of bug", filled initially by the white hat and contained in the encrypted data, that represents a set of actions that exploit the bug. Thus, that asset is providing an irrefutable and easy way for Kleros' jurists to give their verdict. Kleros' verdict is able to change the certification status of the NFT to "certified", thus publicly providing the white hacker with a proof of their skills and contributions. 3) Providing White Hats with Sismo Certification Badges “Proof of Hat” With those certified NFTs, white hats are able to use Sismo to mint a badge, on the blockchain address of their choice (because they might want to separate their address on which they receive bug bounties and the address that acts as a public professionnal profile). That badge can have three attributes (gold, silver, bronze) depending on the importance and on the quality of the work of the white hat. That badge assess publicly the skills and contribution of the white hat and is used to build a professionnal reputation. The dApp is built on top Polygon, and we used the Alchemy API to interact easily and seamlessly with the Polygon blockchain to deploy our NFT. Challenges we ran into We managed to integrate Privy and NFT technology together when Sending a Bug submission which was a challenge. We also had challenges with the Alchemy API to deploy our NFT related to unchangeable gas fees on Polygon that made the transaction pending without being processed. We solved it by resetting and changing the nounce! Accomplishments that we're proud of Integration of Privy on our dApp Functional NFT deployment that can be used as proof of white hat contribution Functional Sismo Badge minting (Bronze, Silver, Gold) Creating a super secure App in 2 days! What we learned Each member of the team enhanced their core skills related to their dedicated tasks (front, back, smart-contract, business strategy, project management). Most importantly, all of the members have learned a lot about cybersecurity, data encryption and transmission within Web3, thanks to Privy and IPFS. They have learned about decentralized justice with Kleros. And they have learned about the future of identity representation and social networks with Sismo badges! What's next for Safe Alert We plan on: Developping the features on hiring platforms and social networks to showcase Sismo reputation badges of white hats/developpers. We want to push further the social and identity representation within Web3 through Sismo badges. Challenge between white hats in relation to a bug bounty (thanks to the encrypted and safe Privy database that contains the lists of all the white hats addresses) <div