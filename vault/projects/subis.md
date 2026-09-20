---
slug: "subis"
url: "https://devpost.com/software/subis"
title: "Subis"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 855
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "user/small_business"
  - "substrate/financial_record"
---

# Subis

> zkSync ( Native AA ) Decentralized Subscription Service with Gasless Payments

[Devpost](https://devpost.com/software/subis) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]] [[small_business]]
**substrate** [[financial_record]]

**stack** hardhat, nextjs, solidity, zksync

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for subis
- deployed contracts

## Body

Subis - Decentralized Subscriptions with Gasless & Automated Payments ( zkSync Native AA and Price Feeds ) Inspiration As a developer who regularly works with centralized payment technologies, I've witnessed firsthand the challenges businesses face when relying on centralized subscription management services: High fees Risk of account blocking Limited control over funds These hurdles hinder growth and flexibility. This realization led to a vision in my head for the inspiration for Subis, which I saw as a decentralized, transparent, and cost-effective solution that would put the power back in the hands of businesses. At the same time, it would provide subscribers with a seamless and gasless experience through Native AA on zkSync. So, I took it up as a challenge to solve this problem. What it does Subis is built as a comprehensive subscription management solution that empowers businesses to: Create, manage, and automate their subscription plans effortlessly Set up monthly subscriptions Share a single link for users to subscribe and access services Have complete control over their plans Create and edit subscription plans Set prices in USD Sponsor and enable the gasless creation of smart accounts for subscribers Enable gasless subscriptions Automate charges Allow subscribers to switch plans seamlessly with proration By leveraging smart contracts, subscription data is securely stored on-chain, providing reliability and transparency. Integrating Subis into existing applications was designed to be quick and easy, allowing businesses to enable and manage subscriptions effortlessly using the on-chain data. How I built it Subis is built on the zkSync network, using the power of: zkSync's Native Account Abstraction (AA) Chainlink Price Feeds Native AA allows for the creation of smart contract wallets that enable advanced functionalities like: Gasless transactions Daily spending limits in USD Automated charges This eliminates the limitations of traditional accounts and provides a more user-friendly experience for subscribers. To ensure accurate and reliable pricing, I integrated Chainlink Price Feeds, which provide accurate USD prices directly on-chain. This enables businesses to set subscription plan prices in USD and automatically convert them to the equivalent amount of tokens based on real-time exchange rates. By basing itself on Chainlink's infra, Subis ensures high reliability of the pricing data. Challenges I ran into For executing transactions from the subscriber's smart account wallet, one significant challenge was figuring out how to handle EIP-712 transactions through the front end. EIP-712 is a standard for typed structured data hashing and signing, crucial for signing messages off-chain and executing transactions through smart contract wallets. With limited examples and documentation, I had to dive deep into the EIP-712 signer class to properly implement it in Subis. Finally, I figured it out after 2 days of tinkering around with the internal code of the class and I felt super happy about that, to the point that I screamed in my room after solving it and making EIP712 transactions through Smart Accounts work, haha. Accomplishments that I'm proud of I'm incredibly proud of building an end-to-end solution for decentralized subscription management in a short timeframe. Despite the complexities, I was able to make use of the capabilities of zkSync and Chainlink to create a functional platform. I dedicated the first 20 days to thoroughly studying the underlying technologies, being new to account abstraction I studied ERC 4337 in depth in the early days of the hackathon. Through Patrick Collins' 10-hour long lectures on Foundry, I gained knowledge about Chainlink. In the final 10 days, I utilized this knowledge to develop and deliver a working project, making the practical implementation of these cutting-edge technologies I spent time learning. What I learned Through the development of Subis: I gained valuable insights into Native Account Abstraction and its transformative potential. I discovered the power of smart contract wallets and how they can fully change the current paradigm of how the user interacts with decentralized applications. I explored Chainlink Price Feeds for the first time and understood how decentralized sources of truth can be seamlessly integrated into smart contracts, enabling intuitive and user-friendly pricing mechanisms. What's next for Subis As zkSync evolves, I am truly excited about the future prospects of Subis: I look forward to integrating Chainlink Automation to replace the centralized cron job with decentralized automation, further enhancing the platform's decentralization and reliability. I also look forward to integrating yearly, quarterly, half-yearly duration flexibility for plans ( as of now subis has only monthly subscription support ) I see great potential in applying Subis to real-world scenarios, such as SaaS platforms or freelance service marketplaces, and witnessing its impact on subscription management and user experience. On a personal level, the development of Subis has been an incredible learning experience, and I am eager to continue expanding my knowledge and skills in the realm of decentralized technologies. I believe that the combination of zkSync's Native Account Abstraction and Chainlink's decentralized oracle network holds immense promise, and I am excited to contribute further to this ecosystem. Deployed Contracts The Subis contracts are currently deployed on the zkSync Sepolia testnet. Here are the contract addresses: AA Factory: 0xcEa62E27DA26129CDAB1784Ea59F9ae4a39DdcE8 Manager Factory: 0x6367daDA707E978c3a050C74C5f1cC51001b0066 You can interact with these contracts using the zkSync Sepolia testnet and the provided addresses. <div