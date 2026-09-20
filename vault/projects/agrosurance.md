---
slug: "agrosurance"
url: "https://devpost.com/software/agrosurance"
title: "AgroSurance"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 1189
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "user/frontline_worker"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# AgroSurance

> Insure your crops the smart way

[Devpost](https://devpost.com/software/agrosurance) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[agriculture_food]] [[finance_payments]]
**user** [[frontline_worker]]
**substrate** [[code_repository]] [[geospatial]] [[web_dom]]

**stack** chainlink, hardhat, javascript, react, solidity, typescript

## How they structured the write-up

- project overview
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for agrosurance

## Body

Home Page Farmer Dashboard About Us Vision Staker Dashboard Project Overview The Agrosurance project is an innovative platform that aims to revolutionize the agriculture industry by providing a transparent, reliable, and decentralized solution for agricultural insurance and liquidity management. What it does Agrosurance enables farmers and agricultural stakeholders to access fair and transparent insurance coverage. The platform calculates insurance premiums and verifies claims using on-chain code stored securely on the blockchain. By fetching real-time data from trusted external sources using Chainlink functions, the platform accurately determines premiums and validates claims based on predefined rules and triggers. The platform also offers a staking mechanism where investors can stake their Matic tokens and earn Agrocoin as staking rewards. By participating in the staking program, investors contribute liquidity to the platform and help secure the network. Staking rewards are distributed periodically, providing an incentive for long-term participation and fostering a vibrant community. How we built it Agrosurance is comprised of five smart contracts, each serving a specific purpose within the platform: AgroCoin: The AgroCoin smart contract represents the ERC20 token used within the Agrosurance ecosystem. It allows for the transfer and management of AgroCoins among users. The contract also includes governance support, providing a foundation for future protocol governance mechanisms. AgroSuranceLand: The AgroSuranceLand smart contract is responsible for tokenizing users' land into non-fungible tokens (NFTs) with on-chain metadata. This contract allows for the representation and management of land assets within the platform. Users can tokenize their land and utilize it as collateral for insurance coverage or other purposes within the Agrosurance ecosystem. FundManager: The FundManager smart contract serves as a centralized repository for managing the funds within the Agrosurance platform. It securely holds the Matic tokens received from the InsuranceManager and the StakingManager contracts. The FundManager ensures proper allocation and distribution of funds for insurance claims, staking rewards, and other financial operations. StakingManager: The StakingManager contract enables users to stake their Matic tokens and receive AgroCoins as staking rewards. It handles the staking process, tracks users' staked amounts and rewards, and ensures the proper distribution of AgroCoins to stakers based on predefined rules and mechanisms. This contract incentivizes liquidity provision and community participation within Agrosurance. InsuranceManager: The InsuranceManager contract facilitates the insurance-related functionalities within Agrosurance. It allows users to obtain insurance quotes, purchase insurance policies, and file claims. The contract calculates insurance premiums based on predefined algorithms and verifies claim eligibility based on predefined rules. The InsuranceManager plays a critical role in providing transparent and efficient insurance coverage for users' agricultural assets. These smart contracts work together to create a robust and comprehensive platform for agriculture insurance and liquidity management. They tokenize land assets, handle the staking mechanism, manage insurance-related operations, and ensure proper fund allocation within the ecosystem. Through these smart contracts, Agrosurance aims to provide farmers, investors, and other users with a transparent and reliable platform for agricultural risk management and participation in the agrosurance economy. Frontend UX optimizations: We implemented a custom built cache on the frontend to ensure that the user gets a smooth experience whenever an API call is being made. The only API calls we make are to get the location from coordinates to display on the lands page. Moreover the design of the website is structured in an easy to navigate and user experience friendly manner. Challenges we ran into Developing Agrosurance was not without its challenges. Here are the main struggles we encountered and successfully resolved: Learning Curve with Chainlink: Our initial experience with Chainlink presented a learning curve as we familiarized ourselves with the technology. However, with determination and by utilizing available learning resources, we quickly overcame this hurdle and integrated Chainlink functions effectively. Integration Complexity: Integrating multiple components and functionalities within Agrosurance proved to be time-consuming due to the complexity involved. Despite the challenges, we persevered and successfully integrated the necessary features. However, due to time constraints during the hackathon, we were unable to complete the integration of the Kleros Protocol. Nonetheless, this obstacle has provided us with valuable insights for future development. Accomplishments that we're proud of We take great pride in the accomplishments we have achieved with Agrosurance. Here are the key aspects we are proud of: Seamless Integration with Chainlink Functions: Despite being our first time working with Chainlink, we quickly embraced the learning curve and successfully integrated their functions into our platform. This demonstrates our ability to adapt and learn new technologies efficiently. Transparency and On-Chain Storage: By storing the insurance premium calculation and claim verification codes on the blockchain, we have established a transparent and immutable system. This ensures that all participants can access and audit the code, fostering trust and transparency within the platform. User-Friendly Interface: We have invested significant effort into creating an intuitive and user-friendly interface for Agrosurance. Our goal was to make it easy for farmers, investors, and other users to navigate the platform, stake their Matic tokens, and manage their insurance policies effortlessly. Addressing Liquidity Concerns: We have taken a proactive approach to address liquidity concerns within the agrosurance industry. By implementing a staking mechanism, we incentivize investors to contribute liquidity to the platform while earning Agrocoin as rewards. This is a significant achievement in ensuring the sustainability and success of the project. What we learned Throughout the development of Agrosurance, our team has gained valuable knowledge and insights. Here are some of the key learnings we acquired during the project: Chainlink Integration: We had the opportunity to explore and integrate Chainlink functions into our platform. This experience taught us about decentralized oracles and how they enable secure and reliable data retrieval and off-chain computations. We learned how to leverage Chainlink to fetch real-world data and integrate it into our smart contracts. Liquidity Management: Developing the StakingManager and FundManager contracts allowed us to understand the complexities of managing liquidity within a decentralized ecosystem. We learned about the importance of proper fund allocation, transparent reward distribution, and the challenges associated with maintaining adequate liquidity levels. Time Management and Prioritization: Throughout the project, we faced time constraints and had to prioritize certain features over others. We learned how to effectively manage our time, make informed decisions, and ensure that the core functionalities were implemented within the given timeframe. What's next for AgroSurance Integration of Kleros Protocol for Dispute Resolution: The project plans to integrate the Kleros Protocol to provide a fair and efficient mechanism for resolving disputes. Farmers or policyholders will be able to file disputes if they believe their claims were wrongly denied. The Kleros Protocol will facilitate an independent jury process where jurors review the evidence provided by the farmer to make an impartial decision. Resolving Liquidity Issues: While the staking function addresses liquidity concerns to some extent, the project acknowledges the need to further improve liquidity management. Future plans involve exploring partnerships with liquidity providers, implementing decentralized lending protocols, or integrating liquidity pools to enhance availability and stability. The Agrosurance project is committed to continuously improving and expanding its capabilities to provide reliable insurance coverage and liquidity management for the agriculture industry. By integrating the Kleros Protocol and addressing liquidity issues, the project aims to enhance trust, fairness, and sustainability. <div