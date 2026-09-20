---
slug: "cryptopasta"
url: "https://devpost.com/software/cryptopasta"
title: "Cryptopasta"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 1069
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# Cryptopasta

> A text-based adventure game that merges interactive storytelling with blockchain technology

[Devpost](https://devpost.com/software/cryptopasta) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[financial_record]]

**stack** chainlink, go, mongodb, next.js, openai, solidity, typescript, zksync

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for cryptopasta

## Body

Lobby Cryptopasta Mission Log GIF Mission Reentrancy Chaos The mining zombies The meme killer Inspiration The Challenge of Newcomer Onboarding Blockchain realms are often enigmatic, filled with complex concepts and terminology that can be challenging for newcomers. Despite the abundance of educational resources, they can be uninspiring and dry, making it difficult for users to retain information. As a result, many potential users are deterred from exploring the blockchain space, missing out on the excitement and opportunities it offers. The Appeal of Urban Legends As a fan of urban fantasy like SCP Foundation and Creepypasta , I wondered what makes people fascinated by these stories. I found that there are two key factors: Stimulation of Raw Emotions : These stories evoke human raw emotions like fear, curiosity, and excitement. Community-Driven Content : They provide a wealth of base content that can be expanded by anyone, leading to derivative works such as fan art, fan fiction, and games created by the community. These insights led me to consider how we could leverage these elements to attract more users to the blockchain space by entertaining and educating them with engaging content. The Idea of Cryptopasta Based on these insights, I decided to create a text-based adventure game that merges interactive storytelling with blockchain technology. By allowing users to craft their own stories and explore the blockchain realm, Cryptopasta makes learning fun and engaging. Our goal is to attract a wider audience to the blockchain space and inspire a new generation of blockchain enthusiasts. Furthermore, we aim to expand the world of Cryptopasta with derivative works created by the community. What it does 1. Accessibility Social Login : Users can log in using their social media accounts, simplifying access to the dApp. Account Abstraction : Users can create smart contract accounts and interact with the blockchain without needing to understand the underlying technology. Transaction fees can be sponsored by a Paymaster, making it easier for users to use the dApp. The native account abstraction (AA) of zkSync allows transactions to be processed at the protocol level without third-party involvement. User-friendly Interface : The UI is designed to be intuitive, guiding users through the game with ease. USD Pricing : Implement USD-based pricing leveraging Chainlink Price Feeds for transactions to enhance user convenience and reduce complexity associated with cryptocurrency price fluctuations. 2. Content User-generated Content : Users can create and share their own stories, contributing to the Cryptopasta lore and earning rewards for their creativity. Blockchain Integration : Each user-created story is tokenized and stored on the blockchain, ensuring transparency and immutability. Memorable game scenes can also be captured and stored as NFTs. Onboarding to the Blockchain : The game can introduce newcomers to blockchain concepts and terminology in an engaging and interactive manner. 3. Interactivity Interactive Storytelling : The game features an AI-powered, text-based adventure where users can craft their own stories and explore the blockchain realm. Each choice impacts the storyline, creating a unique experience for every player. Community Engagement : Users can share their stories within the community, rate and comment on others' stories, and participate in discussions. This fosters a sense of community and collaboration, encouraging users to learn from one another. Ownership and Rewards : Users retain ownership of their stories, which are tokenized on the blockchain. They can earn rewards for their contributions, such as creating popular stories or completing community challenges. How we built it We used a variety of tools and technologies to build Cryptopasta, including: Smart Contracts : Solidity, Hardhat, zkSync, Chainlink Frontend : Next.js, Chakra UI, Privy, Viem, GraphQL Backend : Go, zkSync-SDK, OpenAI API, JWT, MongoDB, Pinata Subgraphs : The Graph, GraphQL DevOps : Docker, Docker Compose, Make We've started by developing the smart contracts using Hardhat and zkSync, which is core to the entire project. We then set up the frontend using Next.js and Chakra UI, implementing social login with Privy. The backend was built using Go, integrating with zkSync-SDK for contract account deployment with jwt authentication of users. OpenAI API was used for the AI-powered text-based adventure game. The subgraphs were created using The Graph and GraphQL to query and index data from the blockchain. Challenges we ran into 1. Hardhat vs Foundry Challenge Attempted to use foundry-zksync for smart contract development. Required via-ir flag to compile, which is slow on my machine. Bytecode differs from that generated by Hardhat, causing the account abstraction contract to malfunction. Contract verification is not supported yet. Solution Chose Hardhat for stable smart contract development. Added missing features (e.g., safeTransfer Receiver, multicall) to the account abstraction contract to ensure proper functionality. 2. AI Integration with Blockchain Challenge Initially designed to integrate AI with the blockchain for transparency, immutability, and interaction cost tracking. This approach required users to pay for each AI interaction, which could be costly and deter gameplay. Chainlink functions is not supported on the zkSync Sepolia network, thus it is hard to use it and native account abstraction of zkSync together. Solution Decided to keep AI operations off-chain to reduce costs and improve user experience. The game is played off-chain, with only selected storylines tokenized and stored on the blockchain. This approach ensures users can enjoy the game without incurring high transaction fees, making it more accessible and engaging. What we learned Through this hackathon, I have spent a lot of time thinking about how to onboard Web2 users to Web3, and I have learned a great deal by implementing methods for achieving this. Additionally, by using L2 solutions like zkSync, I have gained insights into how to provide a better user experience for users. What's next for Cryptopasta Credits and Rewards System : Introduce a credit system to manage and limit the number of interactions a user can have with the game, preventing excessive resource consumption. Implement a reward mechanism where users receive incentives based on the quality and popularity of their stories, promoting creativity and active participation. Governance Mechanism : Establish a Decentralized Autonomous Organization (DAO) to allow the community to vote on qualified stories and manage reward distribution. This approach ensures transparency, fairness, and community involvement in decision-making processes. Community members can propose and vote on new features, improvements, and content. Community Discussions and Forums : Develop a dedicated platform for users to discuss stories, share tips, and collaborate on new ideas. This space would enhance community engagement, foster collaboration, and support the exchange of knowledge and experiences. <div