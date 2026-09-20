---
slug: "universal-trusted-cross-chain-bridge"
url: "https://devpost.com/software/universal-trusted-cross-chain-bridge"
title: "D-Hub from Dante Network"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 990
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/code_repository"
---

# D-Hub from Dante Network

> D-Hub implements the protocol stack of Dante Network that attempts to enable various public chain resources in the web3 world to interconnect into a collaborative network of services worldwide.

[Devpost](https://devpost.com/software/universal-trusted-cross-chain-bridge) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**substrate** [[code_repository]]

**stack** cpp, node.js, rust, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for d-hub from dante network

## Body

D-Hub Technical Architecture Inspiration We think there should be a kind of infrastructure that can provide consistent and convenient cross-chain interoperability for Dapps in Web3 so that they can focus on their application business which can serve the whole web3 market instead of staying in some certain ecosystem. In our idea, we think different public chains are like realms in mythology. There are barriers for users to have universal transportation to travel around the different realms. And there is Bifrost to open a teleport between realms, but it is neither cheap nor easy. So inspired by this, we want to grow a “World Tree” that supports opening and collaborative ecosystems in web3. It can take roots into the computing resources and storage infrastructures in web3 and web2 to provide orderly resource scheduling. And it can grow by offering non-differentiated data collaboration services for Dapps in web3 and providing valid resources. This is why we have Dante Network. D-Hub, as the project we take to this Hackathon, is a submodule of Dante Network. What it does D-Hub is an implementation of Dante Network's underlying protocol stack for completing multi-chain interactions and collaborations. It is a standard framework that attempts to enable various public chain resources in the web3 world to interconnect into a collaborative network of services worldwide. D-Hub can realize the non-differentiated message transmission and cross-chain contract invocation among different public chains. In this Hackathon project, we deployed D-Hub on the test net of Near Protocol, PlatON, and Avalanche, realizing the cross-chain message transmission and smart contract invocation among these three chains. How we built it D-Hub adopts a decentralized witness mechanism to realize cross-chain operations, mainly including Heuristic Random Selection, Faith Aggregate Verification, Node Credibility Assessment, Challenge Mechanism, and Economic Incentive. The cross-chain operations will be executed together by the multiple open-ended off-chain nodes and smart contracts that are deployed on different chains. Heuristic Random Selection: The handling of each cross-chain message is completed by a random subset of all cross-chain nodes in the network to avoid collusion between nodes. Belief Verification: Each message will have multiple message copies carried by multiple cross-chain nodes. We will compare and process multiple message copies to get the most trusted message content. Commitment Verification: Sometimes, Node Credibility Assessment: According to the verification results, we will evaluate the credibility of cross-chain nodes. Nodes with higher credibility will have a higher possibility to deliver cross-chain messages. Challenge Mechanism: we have set up a mechanism to challenge cross-chain operation. The user can set a confirmation window for cross-chain messages. In this time window, the challenger can challenge the abnormal behavior. At this time, the cross-chain contract will randomly select multiple other nodes to confirm the challenge. Unless all nodes in the network are malicious nodes, otherwise we can effectively avoid the actual loss. Economic Incentive: Nodes need to stake tokens to execute cross-chain tasks, and successful cross-chain operations can obtain token incentives. If the operation fails to pass the verification, the staked token will be slashed according to the situation. Token incentive and slashing mechanisms related to D-Hub are part of the whole tokenomics of the Dante Network. At the same time, we have established a standard cross-chain service protocol to support undifferentiated cross-chain messaging and cross-chain contract invocation. The protocol includes a standardized way of organizing data, SQOS (security quality of service) for messages and contract invocations, etc. Challenges we ran into The biggest challenge we met during designing and implementing D-Hub is how to prevent the misbehaviors of the nodes. We have designed Economic Incentive and Challenge Mechanism to deal with it. Economic Incentive ensures that every misbehavior of a node will be punished on the token once it is found. At the same time, we can get effective incentives for correct behavior. The main purpose of the Challenge Mechanism is to once again increase the difficulty and cost of misbehavior nodes. It enables us to avoid losses caused by some uncertain situations by refusing. Especially when dealing with important cross-chain information like cross-chain assets transferring, this is another guarantee for us to avoid asset loss. Accomplishments that we're proud of We completed the deployment of the D-Hub cross-chain protocol on Near Protocol, PlatON, and Avalanche test net in less than one month. These three public chains basically cover all the technology stacks developed by the web3 smart contract. The subsequent migration towards other public chains will be completed more quickly. We are very proud of the work and our team. Without their hard-working, due diligence, and smart brains, we cannot have done this. What we learned In this Hackathon project, we found out that Near’s sharding mechanism is perfectly combined with its consensus mechanism. NEAR scales horizontally and almost infinitely by distributing calculations across multiple parallelized shards. NEAR uses the Nightshade algorithm to reach a consensus on the network operation nodes that constitute the shards. These provide an efficient and secured collaboration mechanism. Meanwhile, the smart contract on Near made us have a really good development experience. There is very clear guidance in Near Docs, where we learned a lot, which is also one of the important reasons why we can finish D-Hub within a month. What's next for D-Hub from Dante Network For D-Hub, we will take a valid decentralized mechanism of trust to optimize and improve it, including the implementation of adding Node Credibility Assessment, optimizing Node Selection algorithm, and the implementation of Challenge Mechanism. Economic Incentive will be implemented in the construction of the Dante Network. Meanwhile, we will fulfill the D-Hub developing docs in order to make others users learn and use them. Our test network will be coming soon. The protocols and mechanisms of Dante Network will be continuously improved and refined in the test network. After that, a protocol stack analogous to “OSI” which especially serves for interactions between multi-chains in the web3 world will be published along with the launching of the main net. <div