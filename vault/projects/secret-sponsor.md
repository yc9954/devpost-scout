---
slug: "secret-sponsor"
url: "https://devpost.com/software/secret-sponsor"
title: "Secret Sponsor"
hackathon: "Privacy4Web3 Hackathon"
organization: "Oasis Foundation"
winner: true
words: 321
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Secret Sponsor

> Account Abstraction Secret Gas Sponsoring with Oasis Privacy Layer.

[Devpost](https://devpost.com/software/secret-sponsor) · hackathon [[Privacy4Web3 Hackathon]]

## Facets

**substrate** [[financial_record]] [[video_visual]]

**stack** accountabstraction, oasis, opl, sapphire

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for secret sponsor

## Body

screenshot 1 screenshot 2 diagram sapphire tx detail aa tx detail Inspiration Ensuring user privacy can be a complex challenge both technically and from a regulatory standpoint. Excessive privacy provisions can sometimes inadvertently enable undesirable activities such as money laundering. Consequently, smaller users find it difficult to maintain an optimal level of privacy. What it does Secret Sponsor offers a mechanism for anonymous gas-sponsoring, incorporating account abstraction and the Oasis Privacy Layer. Users can stay anonymous by: Initiate encrypted funding transactions in Sapphire. Bridge these funds to the Goerli account abstraction paymaster. Execute transactions without incurring gas fees. Moreover, because the system focuses solely on gas-sponsoring, it becomes difficult to associate it with illicit actions such as money laundering. This is optimal privacy tailored for smaller users, particularly NFT artists. How we built it We've implemented a funding manager within Sapphire using the Oasis Privacy Layer. Users can carry out encrypted privacy-funding transactions, which are then synchronized to the Goerli paymaster. In addition, we have set up the Account Abstraction infrastructure on the Goerli network, utilizing the secret fund for transactions. Challenges we ran into Working with the on-chain privacy layer was a new experience for me. Initially, understanding its function and application was challenging. Some preconditions were tricky to manage. I frequently sought help from the Oasis Discord community. Accomplishments that we're proud of I managed to integrate the Oasis Privacy Layer with an area I'm well-versed in - Account Abstraction. This showcased the immense potential of combining Account Abstraction with the Oasis Privacy Layer. What we learned On-chain privacy is truly invaluable! What's next for Secret Sponsor Although the funding transaction inputs are encrypted via Sapphire, there is room to enhance the pooling and synchronization mechanisms to fortify user-privacy. Our current focus is on a Proof of Concept (PoC) for secret funding with the Oasis Privacy layer, but our vision extends to developing and refining the infrastructure further. <div