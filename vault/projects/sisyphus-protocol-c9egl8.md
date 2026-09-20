---
slug: "sisyphus-protocol-c9egl8"
url: "https://devpost.com/software/sisyphus-protocol-c9egl8"
title: "Sisyphus-protocol"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 1234
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/simulation_digital_twin"
  - "domain/civic_government"
  - "domain/education"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Sisyphus-protocol

> Sisyphus Protocol is a decentralized social protocol based on blockchain technology, to help self-improvement and encourage creators' economy.

[Devpost](https://devpost.com/software/sisyphus-protocol-c9egl8) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[simulation_digital_twin]]
**domain** [[civic_government]] [[education]]
**user** [[educator_student]] [[legal_professional]]
**substrate** [[financial_record]] [[video_visual]]

**stack** chainlink-automation, hardhat, ipfs, nft.storage, openzepplin, quicknode, react, solidity, tenderly, typescript, wagmi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- new feature on this hackathon
- accomplishments that we're proud of
- what we learned
- what's next for sisyphus-protocol

## Body

My activities (ongoing) My activities (finished) All (ongoing) Details Check-in Claim Claim-host Challenge-vote Moment Inspiration We found that as there are more and more things that we can do, it becomes increasingly difficult to focus on one thing. Whether it's learning a new language or just keeping exercising, it's very easy to give up. There are now many communities that are trying to bring people together to do something, but due to the lack of incentives and penalties, most people cannot stay with it. So we wanted to make an on-chain protocol and also a community to help people persevere! What it does Sisyphus-protocol can be divided into four parts: teaming, staking, recording, and rewarding. Users will form their own teams and stake stablecoins into the pool. Each time they complete a task, they have to record and upload it to the blockchain. At the end of the activity, those who successfully complete the task will share the stable coins from those who fail to complete the task and also get our platform tokens. First of all, it is necessary to form a team to start an activity. Here are two ways, one is to organize activities as a host, and the other is to participate in activities organized by others as a participant. To Host an activity, it is necessary to submit a proposal on the blockchain and receive votes from users with governance tokens and get more than half of the votes in favor. In the early stages of the project, since no one has the governance token, a more centralized process, which is a project-side review will be used to restrict the qualifications of the hosts in order to control the quality of the activities on the platform. From the day the activity begins, all the members need to upload the records every day. These records will be used as credentials on the blockchain. We will use optimistic proof to identify cheating. It means that all the credentials are valid at the beginning, and are completely open and transparent for everyone to check. Everyone in the group has the right to challenge the others, and the rest of the group will vote on the validity of his/her challenge. If the challenge has been approved, the cheater will be immediately kicked out of the group, and all the voters will share the token he/she staked; if the challenge fails, the challenger’s reward will be decreased. In the end, the people who failed will lose all their money, and the people who succeeded in the activity will get back the staked stable coins and share the stable coins of the people who failed while getting the platform tokens SYP. In the present version, SYP token and SYS token are not yet available. Future development: an incubator for X-2-Earn and on-chain DAOs By using SYP tokens for liquidity mining, people can get a certain amount of SYS tokens. SYS token has two main roles, one is the governance of the vote, and the other is to provide paid services. In the period the paid service is provided, the staked SYS token will be burned constantly, if it is burned out, it is necessary to refill it. Others can use SYP tokens to purchase the paid services. How we built it Contracts Campaign Factory: Mange some privileges, and create a new campaign. It's AutomationCompatible and needs automation. Campaign: The core of the Sisyphus Protocol economy. It includes sign-up, admits, check-in, challenges, and votes. It's also AutomationCompatible Render: Render Campaign NFT in the way of on-chain SVG dynamic rendering. We use polygon mumbai as testnet, as polygon has a low gas fee and is fast. For test contract deployments, you can view on: https://github.com/sisyphusprotocol/contracts/tree/main/deployments/mumbai The following picture shows the relationship between campaign and campaign factory Integrate Chainlink Automation: Every time someone creates a campaign via the campaign factory, the factory will register a new automation for the campaign. Automation helps the campaign to update the epoch, judge challenges, and settle the campaign on time. Also, the campaign factory itself needs automation to feed the campaign that runs out of $link, cancel and withdraw automation after the campaign ends. These are shown in the following picture. The following picture shows how we integrate chainlink automation Front end As we think, check-in is a more frequent behavior on mobile phones. So we design it in a mobile way and users can run the dApp in their existing mobile wallet. For convenience on PC, we use an iframe and put content in a virtual mobile phone. The main tech stack is next.js and wagmi. Subgraph We use subgraph to index the on-chain data in contract. Transaction emit events and subgraph can handle it. We just set Campaign Factory as the data source. When new campaign is created, the factory will emit the address of new campaign and add the new campaign adress as new data source automaticlly. Content Storage A lot of data in our product must be on-chain but some not. For instance, campaign name and description, user's check-in record (text and image). We put them in IPFS via nft.storage and load them directly in front via nft.storage gateway. It's faster than we image. Challenges we ran into Time is limited. We do it part-time and most of us are students. We need to work or go to class by day and do hackathon projects by night and on weekends. It's troublesome to debug with external service. We need to deploy the contract, then call some method, then simulate failed transactions on Tenderly, then edit the code and re-deploy and run again. Our product depends on the time and multiple people interact. It's hard to reach some specific cases by ourselves, such as claiming the reward after keeping checking or claiming nothing after just forgetting once. As our product includes voting, you need to create many accounts to sign the campaign, check-in, start a challenge, then vote, and finally judge the challenge. For testing, we need to arrange each user's behavior and execute it on time. New Feature on this Hackathon Integrate with Chainlink automation to execute essential jobs, avoiding a crash. Implementation of challenge. It's the most important economic mechanism to make the system sustainable. UI and logic refactor of the front end. Implementation of moments, challenges, and votes. Switch from creating an entirely new contract to just creating a minimal proxy. It reduces gas costs to a large extent and leaves more space for contract logic. Accomplishments that we're proud of It's already closed-loop! A fully decentralized protocol and product. In this MVP version, we even don't have our self-hosted backend. A prettier user interface that we won't get tired of watching all-day. Solidity implementation of an on-chain closed-loop sustainable multi-people interaction system. What we learned Smart contracts can have a closed loop easily just via the test script, but the whole product can't. There are Sisyphean things to do on the front end. Many best practices to build a dApp. What's next for Sisyphus-protocol Integrate with any API to fetch data from external apps such as Github, and Keep. It's undone on this hackathon due to the time limit. Smart contract gas efficiency optimization and then request audits. More smooth animation on the front end. Welcome seed users on testnet. Seek opportunities to make us keep building the product, such as incubators and funds. <div