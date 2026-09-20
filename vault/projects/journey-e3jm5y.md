---
slug: "journey-e3jm5y"
url: "https://devpost.com/software/journey-e3jm5y"
title: "Journey"
hackathon: "TRON Grand Hackathon - Season 3"
organization: "TRON DAO"
winner: true
words: 1097
team_size: 3
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "user/developer"
  - "user/legal_professional"
  - "substrate/financial_record"
---

# Journey

> TRON-native quests platform built to onboard the next billion users into crypto through the TRON blockchain.

[Devpost](https://devpost.com/software/journey-e3jm5y) · hackathon [[TRON Grand Hackathon - Season 3]]

## Facets

**domain** [[finance_payments]]
**user** [[developer]] [[legal_professional]]
**substrate** [[financial_record]]

**stack** chakra, express.js, firebase, ipfs, nextjs, render, solidity, tronbox, trongrid, tronlink, tronweb, typescript, vercel, web3.storage

## How they structured the write-up

- deployed demo
- github repo
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for journey

## Body

landing page explore quests page quests detail page journey detail page Journey is a TRON-native quests platform built to onboard the next billion users into crypto through the TRON blockchain. This project was built specifically for the TRON Grand Hackathon: Season 3, hosted by the TRON Foundation. Deployed Demo https://tryjourney.dev Github Repo Main repo: https://github.com/iamminci/journey Inspiration One of the largest barriers to entry that newcomers face to decentralized finance is not knowing where to start their journey on-chain. We all have that friend who might own some crypto on a centralized exchange or read a few articles about yield farming or automated market makers, but all know too well that very few have actually gotten any hands-on experience engaging with on-chain protocols. What if there’s a platform that helps onboard new crypto users by rewarding them for engaging in on-chain activities with protocols in a sustainable manner that both benefits the users and the protocols themselves? What it does This is why we’ve built Journey. Journey is an on-chain quests platform built for the TRON blockchain where users can engage in on-chain tasks called “quests” and be rewarded for doing so in token rewards, NFT completion badges, and experience points on the platform. Our business model is that we partner with protocols in the TRON ecosystem who will fund and launch quests on our platform and help incentivize user engagement on their protocols (where we take a small fee for offering the service). By doing so not only do projects benefit from increase in engagement on their protocols, but this gamified learn-to-earn platform will help user seamlessly onboard into web3 - increasing the overall user base of the TRON ecosystem. We believe Journey will help: (1) onboard new users into web3, (2) increase user engagement during current market conditions from existing users, (3) help educate anyone about the TRON ecosystem through hands-on on-chain experiences. How we built it The main app was built with NextJS, Chakra UI, Express, Firebase, IPFS (Web3.Storage) and a custom TRON provider that facilitates the dapp <> TronLink connection. Verification Service We built a server that uses the Trongrid API to verify Journey's user transactions for quest completion by using the unique method hash of the on-chain transaction performed on a particular protocol contract. Rewards Payout In order to programmatically distribute rewards to quest completed users, we built an API that utilizes Tronbox and Tronweb to deploy TRC721 contracts and both send the specified token rewards and mint NFT badges to the users. Challenges we ran into Quest Verification One of the biggest challenges we ran into was building out an architecture that allows us to verify user completion of quests on the TRON blockchain. After finding the Trongrid API, we were able to build out a flexible server that was able to programmatically detect whether or not a user engaged with a particular protocol at a specified timestamp, which was a core breakthrough that enabled the platform. Rewards Payout Another challenge was utilizing new tools such as Tronbox and Tronweb (as none of us have built on the TRON ecosystem before) and creating a server that allows us to programmatically airdrop rewards to users who completed the quests. This involved writing our own custom TRC721 NFT contract and dynamically minting those with the specified token URI to the quest completed users. Lack of Testing With the limited time of this hackathon, we had to pour our efforts into ideation, design, building UX/UI + backend, and creating demo. This forced us to forgo other integral parts of the software development cycle such as writing tests. Had we had another couple weeks, having the space to write reliable tests would have helped mitigate a lot of challenges that ensued. But again, this is a hackathon submission so hopefully the judges will understand. Time and Role Management There's a huge leap from building a proof of concept geared towards a single demo video and building a prototype that actually works. By pursuing the latter as a small team, we learned the challenges of prioritization and effort estimation (frequently being too optimistic about our own deadlines), while juggling the roles of product manager, designer, fullstack engineer, solidity engineer, and sales. It was truly a taxing project that challenged our team in all directions but we learned a lot through the journey. Accomplishments that we're proud of We are extremely proud of simply having the app up and running. The fact that anyone is able to actually go onto the platform and complete a successful quest and claim the reward is a huge accomplishment that we didn't know we would achieve. It was a long "journey" for our team. What we learned When doing user research, we learned that there is a huge market demand for platforms that incentivize user participation in crypto - both from the user's side and the protocol side. Not only can an on-chain quests platform truly excite users to learn more about web3 in a hands-on manner, but provides a sustainable business model that allows the platform to generate revenue from protocol partners while providing real value to the partners by increasing engagement of their platforms. It's a win-win model that increases the pie for the entire TRON ecosystem. We are very excited to continue building this service out and onboarding more engineers to help us build the vision. As a team, there was a huge difference in building a proof of concept geared towards a demo and building a prototype that actually fully functions. We are very proud to have achieved the latter. It was truly a taxing project that challenged our team in all directions but we learned a lot about collaboration. What's next for Journey This was a proof of concept built in the span of a month. But we are interested in continuing to pursue this project. Our next steps are as follows: Implement a KYC user verification system via BrightID or WorldCoin to prevent sybil resistance on quests that offer limited token rewards from partners Find a launch partner protocol from the TRON ecosystem to help beta test the service on TRON mainnet Add more gamification and social features to increase engagement and stickiness in the platform Build a partner onboarding service to streamline the quest launch flow Better responsive UI support Testing and monitoring of service We're really excited to see a future where all new applications launching on the TRON blockchain issue their own quests on Journey in order to increase engagement on their platform and educate users about what value their protocols offer. <div