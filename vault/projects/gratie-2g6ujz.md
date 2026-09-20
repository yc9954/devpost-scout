---
slug: "gratie-2g6ujz"
url: "https://devpost.com/software/gratie-2g6ujz"
title: "Gratie"
hackathon: "Fantom Hackathon Q2 2023"
organization: "Fantom Foundation"
winner: true
words: 1013
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Gratie

> Step into the Future: Supercharge Your Business with Blockchain Rewards and Real World Assets

[Devpost](https://devpost.com/software/gratie-2g6ujz) · hackathon [[Fantom Hackathon Q2 2023]]

## Facets

**domain** [[developer_tools]] [[education]] [[finance_payments]]
**substrate** [[code_repository]] [[financial_record]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** alchemysdk, amazon-web-services, api, css, html, mongodb, node.js, rainbowkit, react, solidity, thirdweb, typescript, wagmi

## How they structured the write-up

- inspiration
- what it does
- existing problems
- solving challenges with innovative solutions: the gratie approach
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gratie

## Body

Logo Our project roadmap and vision Business profile creation flow, they can store their assets and valuation on chain in IPFS Post successful business profile creation they can create their own tokens based on the assets pegged Businesses can manage and add new users ( customers and employee's ) at ease Post claiming rewards from the companies the profile of ecosystem members Inspiration After exploring numerous products in the web3 industry, we noticed a significant gap. None of these products were effectively utilizing the technology to assist businesses in enhancing their customer and employee retention. We interacted with several service providers in the shared economy business and discovered that they lacked knowledge about financial tools. Additionally, they desired more incentives from businesses in order to remain engaged within their ecosystem. These observations inspired us to create a product that addresses these challenges and aims to attract a large number of web2 users. What it does We are building Gratie, our platform that empowers businesses to securely store their assets and valuations on the blockchain, known as RWA (Real World Assets). Through this process, businesses can issue their own cryptocurrency rewards to engage customers, retain employees, and foster ecosystem sustainability. These rewards serve as a valuable tool for analyzing customer behavior, retaining talented individuals, and fostering collaborations with other services. By leveraging this technology, businesses can establish a stronger foundation for achieving long-term success and growth. Existing problems Implementing a decentralized web3 rewarding ecosystem is complex and expensive. Not all service providers have financial literacy to invest in company shares, and some companies lack ESOPs for their service providers. Customer and employee retention is a continuous challenge for companies. There is currently no platform for leveraging web3 and rewarding mechanisms to reduce customer acquisition costs (CAC) in a mutually beneficial way. Maintaining a sustainable ecosystem poses difficulties for companies. Solving Challenges with Innovative Solutions: The Gratie Approach Businesses can easily create and set up their own reward ecosystem without extensive blockchain and web3 expertise. Storing Real-World Assets on blockchain through our platform implies directly pegged company rewards as an ESOP Alternative. Token-based rewards significantly boost employee and customer retention by 50%. Leveraging web3 and token-based rewards attracts more customers to new businesses and provides a compelling use case for the rewarded token. The reward system is transparent, efficient, and provides clear analytics for companies. How we built it We utilize the Hardhat framework and Solidity 0.8.9 for contract development and deployment. Integration of wallets is achieved through RainbowKit and Wagmi. Data storage, including logos, images, and NFT metadata, is facilitated by IPFS with the assistance of ThirdWeb.ThirdWeb, IPFS , RainbowKit, Wagmi, AWS Lambda, KMS, Framework Motion library. Backend integration involves utilizing EVM event listeners to securely store transaction details in our database. Alchemy SDK is employed for the detection of user NFTs. Our platform adheres to Ethereum standards, such as ERC-721 and ERC-1155 for NFTs, ERC-20 for custom tokens, ERC-1167 for reward token proxy deployment, and ERC-1967 for upgradable contracts. On-chain authorization is implemented through ownership and role-based access management. The platform supports networks such as Filecoin Calibration and Goerli. We ensure the security of admin private keys and generate EIP-712-based signatures using AWS Lambda and KMS encryption. Our backend is powered by Node.js, MongoDB, and AWS. The frontend is developed using React.js, Material UI, and the Framework Motion library. Challenges we ran into Integrating blockchain, frontend, and backend posed significant challenges for us. Our design system requires improvement; we aimed for simplicity and effectiveness in V1. Integrating social logins was part of our plan, but time constraints hindered its implementation. Dynamic reward distribution to multiple individuals proved challenging, but we successfully resolved it using specific distribution techniques. Accomplishments that we're proud of We're really excited about the awesome community we've built on Discord. Through a few successful campaigns, we've managed to attract over 2,000 members to our Discord server. We've also reached out to more than 15 web2 businesses to discuss a basic Product-Market Fit (PMF) strategy. The good news is that six of these businesses have shown great interest and have responded positively. They could potentially become our future customers. We're proud to say that we've achieved a decent version 0.1 of our product. It has a lot of useful features, such as allowing businesses to create NFTs (non-fungible tokens) using the ERC 721 standard. It also enables them to add users to their ecosystem and reward them using the ERC 1155 standard. What we learned We encountered numerous challenges and moments of discouragement while dealing with the complexity of our problem statement and the global scale approach. Communication issues and team members joining and leaving midway added to the difficulties. However, our team's unwavering belief in the core idea fueled our determination to give our best. Despite the setbacks, we pushed through and released this version of our product. Building on our experiences, we evolved it into "Gratie," an enterprise-level solution. We learned from our mistakes, constantly improve ourselves, and remain committed to the grind of building a successful product. What's next for Gratie We are planning to give our website and web app a complete makeover, improving the user interface and making it visually appealing so that it effectively communicates with our target users and showcases the product we're building. We will incorporate a DAO (Decentralized Autonomous Organization) component into our protocol. This will provide a verification process for businesses to register based on their assets and valuations. We will actively engage with more web2 businesses to establish a strong Product-Market Fit (PMF) and collaborate with web3 ecosystem partners to ensure that our product is fully functional and ready for users. We aim to simplify user login by implementing social login through web3Auth. Additionally, we will enable businesses to purchase our products using traditional currencies (Fiat) by integrating with payment gateways like MoonPay or Transak. We will introduce a staking model for businesses, allowing them to participate in ecosystem creation services. This model will enhance the utility of their tokens and provide support to other businesses in the ecosystem. <div