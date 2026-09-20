---
slug: "rocketai"
url: "https://devpost.com/software/rocketai"
title: "RocketAI"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 977
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# RocketAI

> RocketAI blends web3 with OpenAI innovations for a new era in AI agent creation featuring a decentralized incentive system that rewards excellence with RAI tokens via Chainlink Automation & Functions.

[Devpost](https://devpost.com/software/rocketai) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**user** [[general_public]]
**substrate** [[financial_record]] [[sensor_telemetry]] [[video_visual]] [[web_dom]]

**stack** chainlink, chainlink-automation, chainlink-functions, next.js, openai, tailwind, thegraph, typescript

## How they structured the write-up

- description📜
- inspiration
- rocketai incentive mechanisms and chainlink integration✨
- 🧑‍💻technologies used 🤖
- smart contracts

## Body

Landing page Create Agent Explore Agents An agent on Avalanche Mainnet Leaderboard Rewarding System Agent Creation Flow Agent Subscriptions Flow Platform and Creators Income Flow Welcome to RocketAI Platform 🚀🧑‍🚀⚛ Description📜 RocketAI is a comprehensive platform for creating, fine-tuning, and engaging with specialized AI agents. By integrating OpenAI's GPT models with blockchain technology, it offers a unique blend of AI intelligence and decentralized functionality. Creators can design agents with specific skills, users can subscribe to these agents, and fine-tuners can enhance them, creating a collaborative and evolving AI environment. Deployed on Avalanche Mainnet website Authors: Dhruv-2003 Architsharma7 nijoe1 Inspiration Inspired by Snackprompt.com, RocketAI enhances this concept with a decentralized incentivization mechanism using Chainlink. Creator and User Benefits: Motivates creators to develop superior AI agents and rewards users for engagement, fostering a competitive and collaborative ecosystem. Goal: To build a community-driven platform where the focus is on creating top-quality AI agents and fostering active user participation. RocketAI Incentive Mechanisms and Chainlink Integration✨ Overview RocketAI leverages a hybrid system combining Chainlink Time-Based Automation, Chainlink Functions, and Chainlink Log Trigger Automation to incentivize agent creators and top users. Revenue and Fee Structure Agent Creators: Earn from subscriptions to their agents. Contributors: Take a percentage fee for fine-tuning models based on main agent subscriptions. Rewards Distribution using chainlink Key Chainlink Components Time-Based Automation: Regularly initiates the reward process on a set schedule (e.g., monthly). Chainlink Functions: Query the RocketAI server for top-performing agents or users, and stores them on-chain Log Trigger Automation: Listens for contract events post-query fulfillment to trigger the reward distribution. Top Agent Creators: Rewarded based on agent performance and user ratings within the platform. Top Users: Incentivized through engagement metrics like subscription levels. Modular Design: Supports various reward structures, adaptable to different market needs and use cases. Diverse Rewards: Includes scenarios like top-performing agents in specific campaigns (e.g., Twitter ads) or general platform engagement. Outcome Quality Enhancement: Motivates the creation of superior agents. User Engagement: Encourages active participation and subscription growth. Adaptability: Flexible to incorporate diverse rewarding strategies. The integration of Chainlink's diverse automation and function capabilities with RocketAI's modular reward system establishes a robust, dynamic, and equitable environment for all platform participants. Challenges Chainlink functions where able to only return the Encoded-Types ( String - Uint - Int ) That did not allowed us to return an array of agentIDs either an array of user addresses. The first thought was to just encode the arrays using ethers. But that solution created lengthy bytes streams which was a blocker because of the 256Bytes limit of the returned data in the chainlink functions. To pass those limitations we created a uint32[] encoder and a address[] encoder javascript encoders and also an on chain decoder for both cases solidity decoder library . This made our rewarding use case feasible. 🧑‍💻Technologies Used 🤖 OpenAI 🔮 OpenAI APIs : The core AI engine of the platform. OpenAI's GPT models provide the foundational intelligence for the agents. Creators can parameterize these models for a wide range of tasks, like natural language processing, image generation Creating Advertasments and more. Chainlink Protocol 💎 Chainlink Protocol : A critical component for integrating external data into the platform. Chainlink's decentralized oracle network enables the platform to securely and reliably bring in outside data, which is essential for automating the reward distribution process based on agents' performance and user feedback and engagement. TimeBased Automation keeper Keeper Best agent Ads creations Rewarding Keeper Most Active users Rewarding Keeper Ratings-Based agent Rewarding Chainlink Functions Subscription link Avalanche Subscription link Mumbai SmartContract Chainlink Consumer Log Triger Automation Keeper Keeper url TheGraph 🕸️ The Graph is used to index user interactions and contract events on the blockchain. It ensures that the platform's interface remains informative and user-friendly by providing quick access to data about agent interactions, subscriptions, and overall platform activity. RocketAI(Subgraph Code) RocketAI(Subgraph Avalanche) RocketAI(Subgraph Mumbai) Usage of the existing Unlock Protocol Subgraph on Avalanche Mainnet & Polygon Mumbai Unlock Protocol 🔓 Unlock Protocol : This protocol manages the subscription mechanics on the platform. It allows users to seamlessly subscribe to different AI agents, handling the access permissions and subscription durations. This integration ensures a smooth and secure transactional experience for users engaging with the agents but also acts as a revenue stream for agent creators, contributors and to our platform for a sustainable decentralized economy. Smart Contracts The RocketAI platform is deployed on the following blockchains: Avalanche Mainnet : Snowtrace Contract Link Polygon Mumbai Testnet : Mumbaiscan Contract Link Conclusion and Future Plans 🚀🌐 RocketAI focuses on fostering a dynamic AI ecosystem, emphasizing both creator innovation and user engagement. The platform's incentive layer and economy are built around a versatile reward system that benefits both AI agent creators and users. Add more agent actions and tools. Key Elements: Revenue Model: The platform sustains itself through a portion of subscription fees, while the remainder supports creators and users with revenue and RAI ERC20 tokens. Chainlink Integration: Utilizes Chainlink's Time-Based Automation in conjunction with Function and Log Trigger Automation. This setup ensures regular, automated reward distributions based on performance metrics and user engagement. Reward Distribution: Rewards are tailored to various categories, including top agent creators and active users, aligning with the platform's emphasis on quality and participation. Modular Reward System: Designed to accommodate diverse reward structures, it can adapt to different market needs and use cases, such as rewarding top-performing agents in specific campaigns or based on overall platform engagement. Future Ambitions: Post-hackathon, RocketAI aims to enhance the RAI token's economy, further incentivizing innovation and engagement. The goal is to cultivate a robust, equitable platform that rewards excellence and active participation, setting a new standard in the AI and blockchain space. This strategic approach not only incentivizes quality and innovation but also ensures a sustainable and expanding ecosystem, fueling RocketAI's vision of becoming a leading force in AI and blockchain integration. <div