---
slug: "shoe-shark"
url: "https://devpost.com/software/shoe-shark"
title: "Shoe Shark"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 923
team_size: 6
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Shoe Shark

> ShoeShark is a decentralized platform for sharing travel inspirations.

[Devpost](https://devpost.com/software/shoe-shark) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**domain** [[civic_government]]
**substrate** [[financial_record]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** chainlinkautomation, chainlinkfunction, chainlinkvrf, geth, go, gsap, langchain, next.js, python, wagmi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for shoe shark

## Body

NFT Market travel inspiration plaza token swap home page travel assitant Shoe Shark Inspiration The inspiration for this project came from a love of travel. Travel is an integral part of everyone's life, and sharing travel experiences can inspire others to explore. However, while using traditional platforms to share travel content, we felt that content creators did not own their content and lacked sufficient motivation. We wanted to combine blockchain technology with travel experiences through this project, creating a vibrant travel community that encourages users to record and share their travel experiences while providing personalised AI travel planning services. The platform's name is a tribute to the famous Chinese traveller Xu Xiake. What it does The primary functions of the platform include: Content publication and management Users can post travel photos, videos, and notes to the on-chain contract. After AI review, the content is recorded on the blockchain to ensure authenticity and immutability. Users can view, edit, and delete their published content, and accept rewards from other users for their content. AI personalised services The AI assistant generates optimised travel itineraries based on user time, location, budget, and interests, including transport, accommodation, activity arrangements, and weather information. Users need to pay platform tokens or hold platform NFT to use this service. Token System Users earn points by posting content or signing in, and the platform automatically distributes tokens periodically based on the proportion of points. Tokens can be used to pay for AI services, reward articles, purchase NFTs, and token flash exchanges. Sharing and interaction Users can share their travel experiences and photos, browse other users' content, and gain travel inspiration. Users are allowed to reward content, and creators can accept corresponding rewards. NFT function NFT casting based on Chainlink VRF service, as long as users have points on the platform and have interaction records, they can cast NFT once. Create and manage NFTs related to travel experiences, and provide an NFT market for transactions. How we built it We used the following key technologies and tools: Chainlink Services : Use Chainlink VRF service for NFT casting, and Chainlink Automation service for regular token distribution. Front-end and on-chain interaction : The front-end uses Next.js framework and Wagmi development to realise interaction with smart contracts. AI technology : Use Langchain to implement travel planning, and use Chainlink Function to conduct content review on the chain. Back-end development : Developed using Go language, managed APIs with the Gin framework, interacted with smart contracts via Geth, and performed database operations using Gorm. Challenges we ran into During the project development, we encountered a few challenges: Content management contract design : When using smart contract solutions to ensure the permanence and tamper-resistance of content data, we encountered the problem of high gas wastage. To solve this problem, we continuously optimised the data storage structure and combined it with IPFS to implement the content management smart contract. Decentralised content review : It is very challenging to integrate AI technology into smart contracts. Fortunately, Chainlink Function provides the function of calling off-chain APIs, which enables us to use AI to implement decentralised content review. Web page design and NFT image design : As there are no designers in the team, we have spent a lot of time conceiving and implementing the design of the web page and NFT with the help of AI. Points system : Frequent operation of points on-chain will lead to poor user experience and higher cost. Therefore, we use the backend service and smart contract with Chainlink Automation to regularly batch points on-chain and regularly settle points for tokens. Accomplishments that we're proud of We are proud of the following achievements: Successfully developed and deployed a smart contract for content management : Ensuring the authenticity and immutability of data by recording and managing content on the chain. Integration of AI technology : Successfully developed an AI assistant that generates personalised travel plans and uses AI to review the content published on the chain. Implementation of NFT features : Successfully implemented NFT casting based on Chainlink VRF service and developed an NFT market for users to trade. Token and points system : Built a complete token economy system. Users have multiple ways to use platform tokens and can earn points by participating actively. The contract uses Chainlink Automation to automatically distribute tokens based on the proportion of points. What we learned During the project development, we learned a lot: Experience and application of Chainlink services : We deeply felt the technical advantages of Chainlink services and their advantages in practical applications. Integration and optimisation of AI technology : Mastered how to use AI technology to develop personalized services, and learned to call it in contracts. System integration and stability optimization : Learned how to integrate different complex technical systems together and ensure their stable operation. What's next for Shoe Shark We are full of expectations for Shoe Shark's future, and the next plan includes: Expand platform functions : Add more practical functions such as voting, regular lottery draws, etc. Optimise AI services : Continuously optimise the AI assistant to make it smarter and more personalised, and improve the user experience. Expand the token and NFT ecology : Introduce more partners, enrich the use scenarios of platform tokens and NFTs, and increase user activity. Global expansion : Promote the platform to more regions and provide high-quality travel services and experiences for more users. Community construction : Enhance the interactivity between users, build an active user community, and continuously improve and perfect the platform through user feedback. <div