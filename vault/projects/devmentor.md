---
slug: "devmentor"
url: "https://devpost.com/software/devmentor"
title: "DEVMentor"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 625
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "user/developer"
  - "user/educator_student"
---

# DEVMentor

> Devmentor is a non-profit social-fi dApp where students and mentors can connect to share their knowledge about web3, smart contracts, security and all EVM related subjects, while getting rewarded.

[Devpost](https://devpost.com/software/devmentor) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**domain** [[developer_tools]] [[education]] [[finance_payments]]
**user** [[developer]] [[educator_student]]

**stack** automation, chainlink, datafeeds, dotenv, env-enc, ethers, express-rate-limit, firestore, foundry, foundry-devops, functions, functions-toolkit, hardhat, nestjs

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i encountered
- accomplishments
- what i learned
- what's next for devmentor

## Body

Landing page Mentee's session form That's a match ! Matching mentors Give tips to your mentor Ready for next badge ! Mentee's profile page Redeemable reward Leaderboard Locking value to select a mentor Mentor's profile page Rating a session Session with locked funds Badge details Reward shop Inspiration The inspiration for DEVMentor comes from my personal journey. Having been a developer for a year, I've learned immensely from the wealth of resources available. Being driven by passion and curiosity, I've quickly faced higher challenges and many times I wished I had a kind senior engineer next to me or a clone of Patrick Collins to get me through the hardest concepts. The idea was cemented on October 23, when @Pashovkrum , a senior smart contract auditor, tweeted : " I truly believe one of the few secrets of success is having mentor(s)... Learn from people who have done what you would like to do. " What It Does DEVMentor is a social-fi dApp designed to connect beginners with experienced developers who are eager to teach. This connection can be a huge stress relief for beginners and guide them on a path to success, especially when paired with a learning platform like Updraft . It also allows experienced developers to reinforce their knowledge by teaching, share their passion and journey, and receive rewards for their engagement. How I Built It DEVMentor was constructed in three segments: Blockchain-Based Backend: Utilizing Solidity , the Foundry framework , Chainlink libraries , Functions-Toolkit , and the OpenZeppelin library for ERC1155, Ownership, and Reentrancy Guards. Front-End Development: Implemented with NextJS , TypeScript , Ethers library , UUID , and Tailwind . NestJS Backend: Comprising TypeScript , Firebase , Nodemailer , and Express-rate-limit . Additional tools included Chainlink services (VRF, Automation, Functions, and Data Feeds), Pinata IPFS and SendGrid . Challenges I Encountered One significant challenge was developing a system to match users effectively, incentivize teaching accuracy, and establish a feedback loop. Another was defining the project scope and prioritizing features for a later version, ensuring the core service embodied the intended idea and goals. Designing a logical and secure smart contract architecture, avoiding issues like "stack too deep" or contract size, and automating the distribution of external rewards (e.g., coupon codes from sponsors) in a safe, private manner were among the other challenges. Accomplishments I'm proud to have built a platform in my first Hackathon that addresses a personal need ! With just one year of experience, I managed to create a fun, engaging dApp that strengthens our community. This project allowed me to give back to the space and its people. Also I'm really proud that Chainlink is my first Hackathon, it means a lot to me. What I Learned I learned to leverage Chainlink Functions and Don-Hosted Encrypted secrets for secure user communication and off-chain rewards. I became more adept at contract architecture, avoiding common pitfalls. Undertaking this project solo taught me to design from scratch, anticipate issues, and secure a smart contract backend while providing a modern, engaging user interface. Finally, I've learned how powerful Chainlink services could be when combined in a meaningful way, and that we still have so much to learn / build playing with these tools. What's Next for DEVMentor Future enhancements for DEVMentor (V2) could include: Implementing OZ's AccessControl and Roles for multiple moderators to review mentor applications. Introducing ad placements for sponsors, with automated reward bundling for mentors. Providing rewards for mentees and a lottery system for larger prizes (like full-paid trip to the next big Web3 event ?) Deploying the app on a more cost-effective blockchain and using CCIP for cheaper computation. Allowing mentees to tip mentors in their preferred tokens and enabling mentors to select their preferred payment methods. <div