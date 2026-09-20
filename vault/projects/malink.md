---
slug: "malink"
url: "https://devpost.com/software/malink"
title: "MaLink"
hackathon: "TRON Grand Hackathon - HackaTRON Season 7"
organization: "TRON DAO"
winner: true
words: 822
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "domain/transportation"
  - "user/general_public"
  - "substrate/financial_record"
---

# MaLink

> Managed your assets with crypto automation

[Devpost](https://devpost.com/software/malink) · hackathon [[TRON Grand Hackathon - HackaTRON Season 7]]

## Facets

**domain** [[finance_payments]] [[security_privacy]] [[transportation]]
**user** [[general_public]]
**substrate** [[financial_record]]

**stack** bttc, nextjs, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for malink

## Body

Homepage Setup Add New Group Add Account Details Inspiration The MaLink project addresses a major pain point in the cryptocurrency ecosystem: the loss of assets due to forgotten seed phrases, wallet inactivity, or sudden events like the death of the wallet owner. Because of this existing problem according to the U.S. blockchain research firm Chainalysis, about 20% of the existing 18.5 million bitcoins, which were worth around US$140 billion then, were lost or stuck in accounts that could not be moved. In the current decentralized landscape, only the seed phrase holder has control over the assets, and once lost, the assets are often unrecoverable. Many media also report that there are many cases of users losing/forgetting their private keys, causing funds to be locked up. Another issue we see in the current adoption of cryptocurrencies is that reduced options of payment methods that usually can be used in traditional transactions (e.g. recurring payments, payment schedules) lead to less flexible transactions that can be made. What it does MaLink tries to eliminate the worries of many crypto users by creating a protocol that can make automatic transfers according to a predetermined time. In addition, the use of this protocol is also very broad, you can use it to make scheduled payments such as paying monthly subscriptions, monthly groceries, or even transferring salaries for your employees every month. By creating this protocol in the blockchain ecosystem, we ensure that we can reduce the number of lost crypto assets due to forgotten private key, seed phrases, or sudden emergencies. How we built it Frontend with NextJS Typescript framework Smart Contract with solidity and help of the BTTC(BitTorrent) network Challenges we ran into Security Ensuring the security of MaLink’s automated transfer protocol was one of the biggest challenges. We needed to build a robust smart contract system that could handle sensitive functions like automatic transfers without exposing users to vulnerabilities such as reentrancy attacks, overflow/underflow issues, or unauthorized access. Thats why we did a lot of auditing and layered testing to minimize every errors that can occur Accessibility We want MaLink to be a platform that removes the barrier to entry from the public to start using cryptocurrencies due to concerns of transfer errors if using crypto. For that, we realize that there will be many users who are not familiar with crypto transfers so we try to develop our product to be user friendly.. Accomplishments that we're proud of User-Friendly We’re particularly proud of how intuitive MaLink is for users, regardless of their level of crypto knowledge. By focusing on accessibility, we’ve made it possible for people who are unfamiliar with blockchain technology to securely manage their assets. We even tested our design on a 70-year-old user even though we still had to introduce him to the concept of crypto first. Running layered testing process Before releasing MaLink on the mainnet, we’ve gone through multiple layers of testing, from internal audits and code reviews to extensive user testing on the testnet. Our stress tests have demonstrated that the platform can handle high traffic while maintaining performance and security, which gives us confidence that MaLink can serve a growing user base without issues. What we learned The user research process is the most important stage in building a product. When we first initiated the development for MaLink, we had tons of ideas to implement but it turns out that after doing user research and really understanding the needs of users we decided to do development on the initial MVP first and we will make improvements to features that are felt to be disruptive / helpful in our main business process, namely transfer automation based on the feedback obtained from our users. What's next for MaLink Here is our roadmap for MaLink Development : August & September 2024 User research and project initialization Conduct market research and gather feedback in ideation process Designing system requirement to detailed project scope and technical requirements Design UI and running UT for validate ease of interaction September 2024 User research and project initialization Set up blockchain infrastructure (e.g., using Tron blockchain) for smart contract deployment. Start development on MaLink’s smart contract Create the User Interface (UI) front-end and test the early prototype with internal teams October 2024 Testnet launch and collect user feedback Launch project on Testnet Collecting community feedback to improve feature in the next iteration Perform stress testing November 2024 Launch project on Mainnet Fixing bug and improve feature based on user feedback Officially launch MaLink on Mainnet to the public with full functionalities Initiate user acquisition strategies and partnership program After Development : We also want to integrate out platform to other service to enable our partner service to have recurring payment method, because we see the opportunity that with the system that we have currently built, we believe that we can provide a better experience than the existing payment methods in the world of cryptocurrencies today. <div