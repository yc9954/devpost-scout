---
slug: "luffy-protocol"
url: "https://devpost.com/software/luffy-protocol"
title: "Luffy Protocol"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 1184
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/immigration_refugee"
  - "domain/security_privacy"
  - "user/general_public"
  - "substrate/financial_record"
---

# Luffy Protocol

> Private and transparent fantasy sports solution using zero knowledge cryptography

[Devpost](https://devpost.com/software/luffy-protocol) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[immigration_refugee]] [[security_privacy]]
**user** [[general_public]]
**substrate** [[financial_record]]

**stack** graphql, javascript, nextjs, noir, solidity, typescript

## How they structured the write-up

- problem
- solution luffy provides
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for luffy protocol
- deployments
- important links
- some cool information

## Body

Problem Fantasy sports betting applications are one of the biggest markets in the world with over $30.95B TAM and 2.2B MAU. These platforms are fully centralised which creates a lack of transparency, privacy and data ownership. Most of these platforms scam users by running automated bots. Players share their squads to the platform when they play the game. Fantasy sports being a game of skill and not a game of luck, the prediction data is not owned by the users as they are open sourced and shared with the platform and everyone. Transparency and data privacy concerns are widespread in the sports betting industry, affecting user trust and competition integrity. Platforms like Fantasy Premier League concentrate user squads, making them exposed to breaches and untrustworthy approaches. Such breaches can lead to the unauthorized disclosure of personal data or retroactive changes to team makeup, changing competitive dynamics and harming the confidence of users. Solution Luffy Provides There is a need for a transparent and private fantasy sports betting application. Luffy is 100% on chain which makes it completely permissionless and transparent. Users can now trust the system/logic without having to trust the platform. The points for each match is computed on-chain using an algorithm which is verified and executed trustlessly via Chainlink Functions. Users have complete control over their funds as they interact with the code that governs the protocol and not an entity or an organization. Users can claim points and rewards on-chain without revealing their squad to anyone (not even Luffy) using zero knowledge proofs. This creates a new possibility of incentivisation for the users who can now sell their squad as keys to other users(bet on betters). With the help of Worldcoin/Gitcoin passport, we have on-chain verifiable credentials which is used as an anti-bot solution. How we built it Initially, we wanted to build a MVP and ship it within the first two weeks of the hackathon. We successfully did and spent a week marketing and selling it to people collecting feedback. Reflecting on the inputs, we designed a completely new product from scratch and built in the last 3 weeks of the hackathon. We spent so much attention to detail in the entire process of designing the frontend, contracts, circuits, indexers, demo video and marketing. We pitched our product to Aztec, Secret Network, Chiliz, Sindri, Dynamic and Chainlink. We applied for Arbitrum Grants Program after we built our V1 but failed to get into it. With the completion of our V2, we applied for AllianceDAO and OrangeDAO accelerator programs. We focused on utilising the Chainlink Services to it's fullest. We integrated all the Chainlink Services efficiently and effectively with a proper utility to back it. We built 5 subgraphs to index 5 different chains using which we were able to provide clean and seamless transaction UX. We integrated Account Abstracted Social Login using Dynamic wallet. We used Sindri to generate our Noir zk Proofs that greatly improved the UX of the application. We designed our frontend in Figma and built it entirely using Next.js/TailwindCSS. We used Dynamic/Viem as our web3 provider. We used RapidAPI for the sports statistics data in our application. We used Supabase for some more external data storage. We ran our express server in Adaptable primarily as helpers to our Chainlink Functions to perform some cryptographic functions which were not possible to be run on the Functions because of Service limits. Challenges we ran into We struggled and spent a lot of time optimising our Chainlink Functions to run on chain. We had to cut down on compute and external node packages and come with an efficient algorithm that runs on Chainlink without running out of service limits. Special thanks to the Adam from the Chainlink Team who was prompt with his replies and helped us debug the issues. I struggled with Chainlink VRF 2.5 Direct Funding in Avalanche Fuji and Arbitrum Sepolia because of automatic gas estimation issues where I had to configure manually to make it work. The most hard and complex part was designing our zero knowledge circuit. It took almost 2 weeks of our time to make our circuit work and another 1 week of time to complete a full proving and verifying cycle in our application. Special thanks to Sindri using which we were able to speed up the proof generation process by 120x. Accomplishments that we're proud of We launched two versions of the product in this hackathon and we hit our first 120 users! Over the period, we built partnerships with Aztec and Sindri. This gives us an upper hand over other companies that try to replicate this solution. Platforms like Rollbit and Sorare make millions selling web3 prediction markets and fantasy sports. Even though they are fully centralised, people trust these applications with their money. When people understand and realise the importance of this product, they would start migrating towards applications that better value their data ownership and privacy. I believe Luffy can transform the dynamic of the fantasy sports gaming industry. What we learned It was the biggest learning experience of our lives. We built many many things, brainstormed and experimented all the Chainlink Services and integrated everything seamlessly with strong utility and need behind each implementation. From Full stack development, Smart Contract Development, Zero knowledge Cryptography, Business, Video editing to Presentation, it was a complete experience for every one of us. Integrating multiple Chainlink Services into one contract was exciting and challenging at the same time. What's next for Luffy Protocol The distribution strategy will be a multi-channel approach. We'll utilize digital marketing channels like social media ads, SEO, and content marketing to reach users online. Initially we need a good trust and reputation in the web3 market and we will build it by collaborating Luffy with other web3 protocols and companies. With Chiliz, we will build partnerships with actual sports teams and offer real world rewards/perks and create awareness about the product and the problem it solves. Since it is a consumer game, we will be on the lookout to partner with relevant influencers and online communities which will help us expand our reach. Referral programs and Twitter campaigns to expand the social media community. We will have a token drop associated with our product launch. Deployments LuffyProtocol (Main Deployment in AvalancheFuji) 0xc8BcE37c917571237aeC37f957E9E80f56122221 Luffy Crosschain (Ethereum Sepolia) 0xCBe49DBE7bf83f8238b4Ae89c1c67Af17b48D526 Luffy Crosschain (Arbitrum Sepolia) 0xB096d51062F906c4f72d394fe522C845c377370D Luffy CrosschainNoVRF (Base Sepolia) 0xE54b2A824E59890183E9a6e50911aDee6A587a7B Luffy CrosschainNoVRF (OP Sepolia) 0x0C29b8C5121a4a72E9D623eFe418875fc7E3Dd15 Important Links Extended Demo Video => Luffy V2 (Try it out!) => https://app.luffyprotocol.com/ Landing => https://luffyprotocol.com/ Luffy V1 => https://ipl.luffyprotocol.com/ Github => https://github.com/luffyprotocol/ Instagram => https://www.instagram.com/luffyprotocol/ Linkedin => https://www.linkedin.com/company/luffyprotocol/ Twitter => https://x.com/luffyprotocol Some Cool Information Yes we did a market study. The biggest market is the US and Canada and the biggest user base is from the US and India. The current market valuation is $25 billion and is expected to reach $55 billion in the next 8 years. We are targeting the US and Canada market initially because according to a study around 23% of Americans/Canadians take part in fantasy sports betting and 65% of them make more than $50,000 a year. <div