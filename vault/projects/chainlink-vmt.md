---
slug: "chainlink-vmt"
url: "https://devpost.com/software/chainlink-vmt"
title: "VMTree"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 584
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "substrate/financial_record"
---

# VMTree

> Verifiable Merkle Trees: affordable privacy on-chain

[Devpost](https://devpost.com/software/chainlink-vmt) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**mechanism** [[structural_withholding]]
**substrate** [[financial_record]]

**stack** chainlink, circom, docker-compose, javascript, moralis, next.js, snarkjs, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vmtree

## Body

Our custom Chainlink job executes a SNARK computation and posts the result to our VMTree instance. Inspiration VMTree is inspired by Chainlink's work around math-based agreements, cryptographic truth, and abstraction of infrastructure complexity, and VMTree is inspired by Chainlink's position as an industry leader in novel but critical neutral blockchain infrastructure. This project aspires to be a new paradigm in verifiable computation powered by SNARKs, enabled and guaranteed by a hyper-reliable oracle network. What it does VMTree is a 10x gas optimization effort. We use out-of-the-box thinking to save on costs; instead of gas golfing for marginal savings, we apply a completely different conceptual framework for using the blockchain. That is, rather than using blockchain computations to directly update the state of a SNARK-friendly merkle tree, we use blockchain computations to verify a proof that a new state is valid according to the mathematics underpinning zero knowledge proofs, and if the proof is valid, then we simply accept the new state as true. This method of updating uses a cryptographic proof known as a Computational Integrity Proof (CIP). The problem of using CIPs in applications is that they require specialized infrastructure to operate, and this is the achilles heel of any censorship resistant application. With the reliability of Chainlink nodes, plus the SNARKs powering VMTree, users will reliably experience minimal transaction fees to deposit into privacy mechanisms that use SNARK friendly merkle trees. This is a core tool that will be useful for a multitude of zero knowledge proof applications. This project is the beginning of a new Chainlink Decentralized Oracle Network. The VMTree Chainlink integration is foundational to the fully realized version of the Twister Cash token anonymity protocol, which is a multi-chain stablecoin mixer that will have its foundation in Arbitrum much as many other multi-chain blockchain projects have their foundation in Ethereum. We are guaranteed a first customer for this new Chainlink DON wherever the Twister Cash protocol is deployed. How we built it Our team coordinated beautifully to pull off our shared vision. We had many meetings, defined short and long term goals, identified weaknesses and strengths, and executed on prioritized tasks according to a common consensus. Each of the team members contributed significantly to the project. This project was only made possible by the incredible Chainlink community that joined the Spring 22 Hackathon. Challenges we ran into This project was one of the most challenging implementations yet, but perhaps the hardest part was translating the idea from conceptual space to people space. As the project lead, I was incredibly fortunate to have teammates who helped me digest the craziness of VMTree and help me turn it into something I could never imagine existing. Accomplishments that we're proud of Having a top-to-bottom, fully tested implementation of the VMTree architecture using Chainlink. Coordinating four epicenters of individual, varied-skill action into a concrete instantiation of something highly conceptual. What we learned A team of strangers can share a common vision and coordinate to execute it in reality within a short time frame. There are many people out there in the blockchain community who are drawn to a higher calling. There is a high concentration of such individuals dispersed throughout the Chainlink ecosystem! What's next for VMTree VMTree will continue to be optimized until it is production-ready. There are a myriad of improvements to make, but it would take too much away from the current state of the project to state them here. Let's simply enjoy the implementation we have now :) <div