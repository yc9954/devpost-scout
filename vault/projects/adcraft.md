---
slug: "adcraft"
url: "https://devpost.com/software/adcraft"
title: "Adcraft"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 1031
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Adcraft

> AdCraft is a platform that allows users to create TikTok ads with generated images, tagline and characters using AI Generation , and post them to TikTok directly.

[Devpost](https://devpost.com/software/adcraft) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[finance_payments]] [[security_privacy]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** chainlinkccip, chainlinkfunctions, chatgpt, dall-e, ethers, figma, hardhat, ipfs, javascript, nextjs, polygon, python, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for adcraft

## Body

Inspiration Our app’s innovation extends beyond creating TikTok ads; it intertwines the burgeoning world of NFTs with digital advertising. By linking ads to NFTs, users gain the ability to stake on these ads, creating an unprecedented fusion of digital assets and marketing. Imagine this: a user-generated ad gains traction, amassing a significant number of impressions. At this juncture, an NFT associated with the ad becomes activated. Staking on this NFT signifies confidence in the ad’s performance. As impressions soar, the NFT accrues value, translating to tangible rewards for the ad creator. Essentially, this incentivizes creators to craft engaging, high-impact ads, fostering a symbiotic relationship between content quality and profitability. This innovative concept capitalizes on the inherent potential of NFTs and leverages the evolving dynamics of digital advertising. It revolutionizes how we perceive ad value by transforming impressions into quantifiable assets. Through this fusion, our app not only pioneers a new era in advertising but also democratizes earning potential, empowering creators within the digital ecosystem. What it does AdNFT Creation Admins can create new AdNFTs, each representing an advertisement, using the createAdNFT function. The created AdNFTs store engagement data and total staked amount. Staking and Rewards Users can stake their tokens on specific AdNFTs using the stakeOnAd function. Stakers earn rewards based on their stake and the engagement score of the associated AdNFT. Rewards can be claimed through the claimRewards function. Chain Compatibility The contract supports compatibility checks for different blockchain networks using the supportedChains mapping. Admins can update chain compatibility using the updateChainCompatibility function. Cross-Chain Movement AdNFTs can be moved to compatible blockchains using the moveToChain function. This function triggers a CCIP message through the sendMessagePayNative function, enabling NFT transfer across chains. Oracle Integration The contract interacts with a Chainlink Oracle to fetch engagement data for AdNFTs. Admins can request engagement data using the requestEngagementData function. NFT Binding Admins can bind AdNFTs for staking using the bindAdNFT function. Users can check the binding status using the getBindingStatus function. Pause and Unpause The contract can be paused and unpaused by admins using the pause and unpause functions. How we built it Tech stack: Smart Contract: Chainlink CCIP, Polygon, Solidity, Foundary, chainlink functions, Javascript, Hardhat, Ethers AI Backend: javascript, Dall-E, Chatgpt, IPFS Frontend: Typescript, NextJS, Web3Auth Challenges we ran into getting the engagement data from tiktok for the ads created, still in progress, some devs dropped out which was discouraging Accomplishments that we're proud of Innovative Integration of AI with Smart Contracts: Our achievement lies in seamlessly integrating cutting-edge AI technology, specifically DALL·E 3 and GPT-4, with the robustness of smart contracts. This fusion enables the creation of AI-powered NFTs for advertising on TikTok. Revolutionizing Advertising with NFTs: We've pioneered a groundbreaking approach by tethering ads to NFTs, empowering users to stake on these NFT-bound ads. This unique model ties ad engagement to tangible rewards, incentivizing creators to craft compelling and high-impact advertisements. Facilitating NFT Movement Across Compatible Chains: Our accomplishment extends to enabling the smooth transfer of ad-related NFTs between compatible blockchains. This interoperability expands the reach of our platform and the potential audience for these AI-powered ads. Enhancing Security and Functionality: By leveraging OpenZeppelin contracts and access control mechanisms, our smart contract ensures secure operations and offers functionality for NFT creation, staking, reward calculation, and chain compatibility checks. Utilizing Chainlink Oracles for Real-World Data: Integration with Chainlink Oracles marks a significant stride, enabling the acquisition of real-time engagement data for ads. This seamless integration facilitates the update of ad engagement scores, crucial for rewarding stakers accurately. Establishing Roles and Permissions: We've implemented role-based access control, delineating specific administrative roles like admin and owner. This hierarchical structure ensures secure access to critical functions within the contract. Pioneering CCIP Messaging for Asset Transfers: Our implementation of CCIP messaging protocol stands as an accomplishment, allowing the transfer of assets, such as NFTs and payments, across compatible chains, thereby expanding the utility of AI-generated NFTs. What we learned AI Integration Insights: Understanding and integrating AI technologies like DALL·E and GPT into smart contracts was a challenging yet enlightening process. We learned about the capabilities, limitations, and potential applications of AI in generating content for NFTs. NFT Functionality Mastery: Developing NFT functionalities within smart contracts taught us about the intricacies of token creation, management, staking mechanisms, and the significance of linking real-world engagement to token value. Smart Contract Security: Ensuring the security and robustness of smart contracts demanded a deep dive into secure coding practices, access controls, and thorough testing methodologies to prevent vulnerabilities. Oracle and Real-World Data Integration: Working with Chainlink Oracles enlightened us about the criticality of real-time data in smart contract operations. We learned to leverage Oracles effectively to fetch external data and update contract states accordingly. Interoperability Challenges: Facilitating NFT movement across different compatible chains highlighted the complexities of interoperability standards. We gained insights into cross-chain communication protocols and their role in expanding the platform's reach. Role of User Engagement in Ad Valuation: Understanding user engagement metrics and their correlation with ad value emphasized the importance of quantifying engagement for rewarding stakeholders accurately. CCIP Messaging for Asset Transfer: Exploring and implementing CCIP messaging protocols deepened our understanding of cross-chain asset transfers, fostering interoperability and expanding the utility of AI-generated NFTs. Contract Management Features: Implementing pausing functionality taught us about the significance of contract management features, enabling controlled halts for maintenance or emergencies without affecting critical functionalities. What's next for Adcraft Expansion of AI Capabilities: We aim to integrate advanced AI models, enhancing content generation capabilities beyond DALL·E and GPT. This includes exploring newer AI advancements to diversify content creation options for ads. Improving Engagement Analytics: Enhancing our analytics capabilities to provide more comprehensive and real-time insights into user engagement with AI-generated ads. This includes refining metrics for better assessment of ad performance. Scaling NFT Integration: Expanding the utility and interoperability of AI-generated NFTs across multiple compatible blockchain networks. This involves ensuring seamless movement and utilization of NFTs on various blockchain ecosystems. Mobile Application Development: We're venturing into mobile app development to offer a user-friendly interface for creating, managing, and tracking AI-powered advertisements and NFTs. The mobile app will provide a convenient platform for users to access AdCraft's functionalities on the go. <div