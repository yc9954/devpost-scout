---
slug: "journey-vzkr5l"
url: "https://devpost.com/software/journey-vzkr5l"
title: "Journey"
hackathon: "Fantom Hackathon Q1 2023"
organization: "Fantom Foundation"
winner: true
words: 1118
team_size: 2
has_repo: false
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

> Journey is a Fantom-native quests platform built to onboard the next billion users into crypto through the Fantom blockchain. This project was built specifically for the Fantom Q1 Hackathon.

[Devpost](https://devpost.com/software/journey-vzkr5l) · hackathon [[Fantom Hackathon Q1 2023]]

## Facets

**domain** [[finance_payments]]
**user** [[developer]] [[legal_professional]]
**substrate** [[financial_record]]

**stack** chakra, firebase, ftmscan, ipfs, nextjs, render, typescript, vercel, web3.storage

## How they structured the write-up

- live deployment
- github repo
- deployed contracts
- how you can test the project
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for journey
- disclaimer

## Body

Landing Main Quest Journey Profile Community Journey is a Fantom-native quests platform built to onboard the next billion users into crypto through the Fantom blockchain. This project was built specifically for the Fantom Q1 Hackathon. Live Deployment https://tryjourney.xyz/ Github Repo Main repo: https://github.com/0xdeadleee/journey Deployed Contracts JourneyRewarder.sol: 0xa44f2043a2df26737acc22a6b6de35280e8e2d6f JourneyNFT.sol: 0xe60841d51bbaad1ba3d9fec01f9d1c6a35b937e2 How you can test the project Connect to the platform via Metamask Try a quest (SpookySwap quest recommended) Complete and verify each on-chain task for the given quest Claim the token reward associated with the quest View your badges on “My Profile” View the community leaderboard Share any feedback or thoughts in the comments here Inspiration One of the largest barriers to entry that newcomers face to decentralized finance is not knowing where to start their journey on-chain. We all have that friend who might own some crypto on a centralized exchange or read a few articles about yield farming or automated market makers, but all know too well that very few have actually gotten any hands-on experience engaging with on-chain protocols. What if there’s a platform that helps onboard new crypto users by rewarding them for engaging in on-chain activities with protocols in a sustainable manner that both benefits the users and the protocols themselves? What it does This is why we’ve built Journey. Journey is an on-chain quests platform built for the Fantom blockchain where users can engage in on-chain tasks called “quests” and be rewarded for doing so in token rewards, NFT completion badges, and experience points on the platform. Our business model is that we partner with protocols in the Fantom ecosystem who will fund and launch quests on our platform and help incentivize user engagement on their protocols (where we take a small fee for offering the service). By doing so not only do projects benefit from increase in engagement on their protocols, but this gamified learn-to-earn platform will help user seamlessly onboard into web3 - increasing the overall user base of the Fantom ecosystem. We believe Journey will help: (1) onboard new users into web3, (2) increase user engagement during current market conditions from existing users, (3) help educate anyone about the Fantom ecosystem through hands-on on-chain experiences. How we built it The main app was built with NextJS, Chakra UI, Express, Firebase, IPFS (Web3.Storage) and RainbowKit (wallet aggregator). The contracts are deployed on Fantom Testnet using Hardhat and Ftmscan API. Verification Service We built a server that uses the Fantom Scan transaction API to verify Journey's user transactions for quest completion by using the unique method hash of the on-chain transaction performed on a particular protocol contract. Rewards Payout In order to programmatically distribute rewards to quest completed users, we built a server running on Hardhat that utilizes a custom built ERC721 NFT contract to mint NFT badges and send tokens to the users who completed quests. NFT Badges (Stable Diffusion) We used Stable Diffusion in order to create the generative artwork used in the NFT completion badges distributed to users who completed the on-chain quests. Challenges we ran into Quest Verification One of the biggest challenges we ran into was building out an architecture that allows us to verify user completion of quests on the Fantom blockchain. After finding the Ftmscan transaction API, we were able to build out a flexible server that was able to programmatically detect whether or not a user engaged with a particular protocol at a specified timestamp, which was a core breakthrough that enabled the platform. Lack of Testing With the limited time of this hackathon, we had to pour our efforts into ideation, design, building UX/UI + backend, and creating demo. This forced us to forgo other integral parts of the software development cycle such as writing tests. Had we had another couple weeks, having the space to write reliable tests would have helped mitigate a lot of challenges that ensued. But again, this is a hackathon submission so hopefully the judges will understand. Time and Role Management There's a huge leap from building a proof of concept geared towards a single demo video and building a prototype that actually works. By pursuing the latter as a small team, we learned the challenges of prioritization and effort estimation (frequently being too optimistic about our own deadlines), while juggling the roles of product manager, designer, fullstack engineer, solidity engineer, and sales. It was truly a taxing project that challenged our team in all directions but we learned a lot through the journey. Accomplishments that we're proud of We are extremely proud of simply having the app up and running. The fact that anyone is able to actually go onto the platform and complete a successful quest and claim the reward is a huge accomplishment that we didn't know we would achieve. It was a long "journey" for our team. What we learned When doing user research, we learned that there is a huge market demand for platforms that incentivize user participation in crypto - both from the user's side and the protocol side. Not only can an on-chain quests platform truly excite users to learn more about web3 in a hands-on manner, but provides a sustainable business model that allows the platform to generate revenue from protocol partners while providing real value to the partners by increasing engagement of their platforms. It's a win-win model that increases the pie for the entire Fantom ecosystem. We are very excited to continue building this service out and onboarding more engineers to help us build the vision. What's next for Journey This was a proof of concept built in the span of a month. But we are interested in continuing to pursue this project. Our next steps are as follows: Implement a user verification system via BrightID or WorldCoin to prevent sybil resistance on quests that offer limited token rewards from partners Find a launch partner protocol from the Fantom ecosystem to help beta test the service on Fantom mainnet Add more gamification and social features to increase engagement and stickiness in the platform Build a partner onboarding service to streamline the quest launch flow Better responsive UI support Testing and monitoring of service We're really excited to see a future where all new applications launching on the Fantom blockchain issue their own quests on Journey in order to increase engagement on their platform and educate users about what value their protocols offer. Disclaimer The projects showcased in our demo video and slides (e.g. SpookySwap, etc.) have no affiliation with this hackathon project. They are simply shown to help share our vision for the Journey platform as a proof-of-concept. Although we would be more than happy to follow-up with any of the projects when we launch on Mainnet:) <div