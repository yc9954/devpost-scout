---
slug: "stayking"
url: "https://devpost.com/software/stayking"
title: "Evmos StayKing House"
hackathon: "Evmos Momentum Hackathon led by Web3Scholarships (Deployment required for prize)"
organization: "Huobi"
winner: true
words: 1098
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Evmos StayKing House

> Leveraged staking service solely for EVMOS holders

[Devpost](https://devpost.com/software/stayking) · hackathon [[Evmos Momentum Hackathon led by Web3Scholarships -Deployment required for prize-]]

## Facets

**domain** [[developer_tools]]
**substrate** [[financial_record]] [[video_visual]]

**stack** awsacl, awsalb, awscloudfront, awsecr, awsecs, awsroute53, contextapi, cosmossdk, docker, evmosjs, golang, hardhat, nextjs, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for evmos stayking house
- project media

## Body

Inspiration Problem Ecosystem activation achieved by increase of transaction and TVL number is a main problem to solve for early-staged blockchains such as EVMOS. Lack of stakers shows nascent state of EVMOS chain. After analyzing in perspective of users, we’ve concluded that EVMOS holders has a need to invest in attractive DeFi services which creates synergy effect with various protocols in Cosmos ecosystem. Solution We’ve figured out this problem could be solved by taking advantage of key EVMOS features; EVM –compatibility and scalability via IBC protocol. Based on our team’s past experience, we’ve verified that DeFi users are willing to invest in protocols which maximizes their profit, and using leverage is an efficient way to achieve this. Therefore, our team decided to build a service which leverages high EVMOS staking APY to create potential inflow of users and multichain assets, consequently leading to the transaction and TVL growth of entire ecosystem. What it does EVMOS StayKing House is a decentralized finance protocol that allows stakers to maximize their yields and lenders to earn stable profit by lending their assets to stakers using leverage. We aim in creating better and wider profit – generating opportunities for all participants. Main Functions : Leveraged Staking : Leveraged stakers can borrow asset from lenders and have a leveraged exposure in order to earn higher yields. They can take their profit to a higher level via adjusting their leverage level by adding collateral or adding debt value. As they are borrowing assets from the pool, they are accordingly exposed to liquidation risk. Since the main goal of DeFi investors is to take advantage of high APY, this function is an attractive option for EVMOS holders, along with the fact that they are available of automatically reinvesting their asset. Lending : Lenders can lend their assets to generate a relatively stable and low-risk profit. Lenders could freely deposit and withdraw their assets regardless of 14 days of unbonding period. We are coming up with some various ways to able lenders to claim additional rewards other than high lending yields. Multichain Staking (Coming Soon) : Stakers are available of gaining staking and Defi yields across IBC protocol by this function. This function will work as a trigger to create an multichain asset inflow into StayKing, also work as an addition factor to increase user profit. How we built it Token Flow When Lender Bob deposits in USDC lending pool, ibToken is minted and given to Bob. ibToken is a tradable interest-bearing token which acts as a proof of ownership. As Bob lends his asset to the pool, staker Alice can borrow assets from lending pool and leverage it with supplying EVMOS. The borrowed USDC is traded by DEX and converted to EVMOS and merged with the EVMOS equity value Alice have provided. The protocol delegates the total stake Alice have provided to EVMOS validators, and automatically reinvests the rewards claimed. The protocol receives 30% of total rewards claimed as a performance fee, returns borrowing interests to lenders, and automatically restakes the remaining rewards. When Alice unstakes her position, staking profits and her initial equity value are returned to Alice. When position of Alice gets liquidated, protocol returns the supplied equity value after deducing 5% of the total position as a liquidation fee. Technical Architecture The kill bot liquidates positions of users which exceeds 75% debt ratio. Rewards claimed after 14 days of unbonding period is transferred to master wallet. Then the event watcher bot transfers unbonded stakes to uEVMOS in order to return it to users , It also transfers borrowing interest and accrues performance fee. Then the rewards after deducing borrowing interest and performance fee is automatically reinvested by the reinvest bot every day. Also, please note that we are planning to add delegating reward optimizer and multichain staking function, which will cause in greater increase of user profit. Tech Stack [Front-End] Typescript, React, ContextAPI, NextJS Javascript libraries Ethers to interact with smart contracts and MetaMask wallet and deployed smart contracts. MUI Framework highly suitable for building DeFi web service. [Back-End] Solidity, Hardhat, Golang, Typescript, NodeJS(NestJS), cosmos sdk, evmosjs, etc Automatically run Delagation Tx, Reward Distribution TX while subscribing to Cosmos block events and our contract events emit (such as AddPosition, Accrue event etc) deployed in EVMOS Transactions of Unbonding and Liquidation are running in batches according to specific time schedules [CI/CD tool] Github Action (yml) Automatic deployment scripts are written in Github Action yml files to support each module deployment [Infrastructure] Docker, AWS ECR, AWS ECS(Fargate), Route53, ALB, ACL, etc Supported to build and deploy docker images to AWS ECR and replace latest version in AWS ECS automatically ( ~ < 2min ) Challenges we ran into Designing tokenomics of the protocol : There were a lot of numeric values to deal with when designing a protocol, such as Borrowing interest / APY / Performance fee / Liquidation fee. We’ve went through this problem by researching other protocols’ values and referencing them. Also, deep contemplation and discussion about how the established value will effect users were one of the ways we dealt with this issue. Management of security level : When operating a service, one of the inevitable challenges we face is service security issue. We’ve figured out the best solution for this problem by numerous code review and contract audit by our teammates and security team. Staking profit verification : Based on the technical architecture we’ve made, there is a problem that it cannot be verified if all of the profit stakers have staked is delegated properly. To solve this problem, we’ve came out the process of oracle- based verification to verify the transactions and confirm that the total staked amount is actually delegated properly. Accomplishments that we're proud of Introducing first leveraged staking service in EVMOS chain Successfully hypothesizing and testing a certain way for the ecosystem to expand and create opportunities for other protocols to enter What we learned Working knowledge and understanding of key infrastructures and components of EVMOS chain in order to build dApp How to interact and communicate with each team member and manage the whole team efficiently Experienced process of identifying potential target users’ needs and adding functions for user satisfaction What's next for Evmos StayKing House Addition of user-friendly functions such as Oauth login (Google, Facebook, Github) : Planning to split and store private keys in cloud storage and 3rd party KMS, merging them in TEE in the case of signing transactions Swap Optimizer Delegating reward optimizer Oracle-based verification support Addition of lending pools Multichain staking (Support of cross-chain functionality) Project Media Project Media <div