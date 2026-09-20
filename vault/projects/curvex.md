---
slug: "curvex"
url: "https://devpost.com/software/curvex"
title: "CurvX"
hackathon: "Fantom Hackathon Q2 2023"
organization: "Fantom Foundation"
winner: true
words: 895
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/security_privacy"
  - "substrate/financial_record"
---

# CurvX

> CurvX is the Dapp for bonding curve-based token issuance and management on the Fantom blockchain.

[Devpost](https://devpost.com/software/curvex) · hackathon [[Fantom Hackathon Q2 2023]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[security_privacy]]
**substrate** [[financial_record]]

**stack** amazon-web-services, hardhat, javascript, react, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for curvx

## Body

Launchpad User Dashboard Buy Withdraw Inspiration In the realm of Decentralized finance (DeFi), we aspire to create a revolutionary tool for every DeFi user on the Fantom network. Token distribution platforms have gained immense prominence, driving the evolution of the financial landscape. Our goal was to implement this by crafting an innovative solution that leverages token issuance and management. Traditional token-issuing techniques are associated with several drawbacks and restrictions. They offer limited flexibility in designing tokenomics and issuance parameters. Furthermore, they have often struggled to establish initial liquidity, making it challenging for token holders to trade or access liquidity. Most notably, Some individuals are frequently impacted by pump-and-dump schemes that often favor early participants and can lead others to a disadvantage. Bonding curves aim to address these problems by providing continuous liquidity, fair and transparent price discovery, and customizable token economics. With that in mind, we draw inspiration from bonding curves that establish a relationship between the token supply and its price. In a bonding curve, the price typically rises as the token supply expands and typically falls as the token supply diminishes. CurvX lets users create and manage their own tokens. Users can participate in existing token pools created by other users in the platform to maintain liquidity or contribute to market growth of any other tokens. Users can choose the curve type that best suits their desired tokenomics and project requirements. In addition to that, for the sake of users we employed token vesting. Those who have locked up their tokens can take advantage of the opportunity to sell at an increased rate once the lock-up duration has passed, encouraging them to potentially earn profit as the token value rises. Fantom is a desirable option for us as we attempt to construct an effective bonding curve-based token issuance system due to its scalability, low transaction fees, ecosystem support, interoperability, security, and supportive community. What it does It lets users create, customize & manage their own tokens. Users can take part in token pools that have already been setup by other users on the site to maintain liquidity or help other tokens' markets flourish. Lets users choose the bonding curve type that best suits their desired tokenomics and project requirements. Users can potentially sell their tokens at a higher price after the lock-up period ends, resulting in a profit. How we built it Developed the Solidity smart contract from scratch to implement the functionality for managing different types of bonding curves. This involved writing code to handle token creation, bonding curve calculations, and interaction with the blockchain. Built the main application using ReactJS which provided a robust and flexible framework for creating a responsive and intuitive user interface for CurvX. Deployed and thoroughly tested the smart contracts on the Fantom Testnet and Mainnet using Hardhat, a development environment for Ethereum-like networks. This allowed us to validate the functionality of the contracts, test different scenarios, and ensure the security and reliability of the system. Challenges we ran into Understanding and implementing complex mathematical formulas of different bonding curves, particularly the S-Curve and Sub-linear curves. Dynamic rendering of price and purchase estimation using charts in the user interface, which required extensive coding and integration with data sources to provide real-time and visually appealing representations of token prices and purchase estimations. Fine-tuning the user experience to strike the right balance between simplicity and functionality, ensuring that users can easily navigate and understand the various features and options available in CurvX. Testing and optimizing the performance of the application to handle large-scale token deployments, pools, and transactions, ensuring scalability and reliability for users. Incorporating security measures to safeguard user assets and protect against potential vulnerabilities or exploits, ensuring a secure and trustworthy environment for token creation, management, and trading. Despite these challenges, our dedicated team overcame each obstacle with perseverance and innovative solutions, resulting in a robust and user-friendly platform for token management and investment. Accomplishments that we're proud of CurvX stands as a groundbreaking decentralized application (Dapp) at the forefront of innovation, revolutionizing the landscape of token management on the Fantom blockchain. By harnessing the power of blockchain technology, CurvX offers an unparalleled user experience, enabling individuals to create, customize, and manage their own tokens with the utmost ease and flexibility What we learned Deepened our understanding of Solidity math, enabling us to effectively implement complex mathematical formulas and algorithms required for various bonding curve types in CurvX. Familiarized ourselves with the intricacies of interacting with the Fantom Ecosystem, such as working with Fantom wallets, utilizing Fantom-specific tools and resources, and leveraging the network's unique features and advantages. Developed a strong understanding of decentralized finance (DeFi) principles and the role of bonding curves in token economics, enabling us to design and deploy robust and innovative solutions for token creation and management. What's next for CurvX Focus on improving the user experience (UX) to create a seamless and intuitive token management platform for users. Optimize gas consumption to reduce transaction costs and improve overall efficiency on the blockchain. Conduct comprehensive security audits and implement necessary measures to ensure the robustness and integrity of the CurvX smart contracts. Explore additional features and functionalities to expand the capabilities of CurvX, such as integration with other DeFi protocols or cross-chain compatibility. Conduct user feedback sessions and actively engage with the community to gather insights and suggestions for further enhancing CurvX. <div