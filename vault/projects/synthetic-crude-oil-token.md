---
slug: "synthetic-crude-oil-token"
url: "https://devpost.com/software/synthetic-crude-oil-token"
title: "Synthetic Crude Oil Token"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 658
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/security_privacy"
---

# Synthetic Crude Oil Token

> Tokenized Crude Oil project provides broader access to trading and investment opportunities

[Devpost](https://devpost.com/software/synthetic-crude-oil-token) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[security_privacy]]

**stack** chainlink, foundry, node.js, react, solidity, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for synthetic crude oil token

## Body

Project icon Main page | Deposit and Mint Health factor | Redeem and Burn Update price and liquidate Project Story Inspiration The idea for the Synthetic Crude Oil Token project was inspired by the emerging trend of Real-World Asset (RWA) tokenization. As traditional finance begins to integrate with blockchain technology, we wanted to create a project that exemplifies how this transition can be achieved. By tokenizing crude oil, a valuable and widely traded commodity, we aimed to provide broader access to trading and investment opportunities, enabling fractional trading, reducing barriers, and bypassing bureaucratic restrictions. What it does The Synthetic Crude Oil Token project tokenizes crude oil, creating an ERC-20 token backed by WETH and DAI with a requirement for 150% collateral. The system allows users to: Deposit collateral and mint synthetic crude oil tokens. Redeem collateral and burn tokens. Improve their health factor by depositing collateral without minting. Liquidate under-collateralized positions, rewarding liquidators with a 10% bonus. The token is available on Optimism, Avalanche, and Polygon networks, with cross-chain price updates facilitated by Chainlink CCIP. How we built it The project was built using a combination of smart contract development, front-end development, and extensive testing: Smart Contracts : Developed custom ERC-20 tokens to represent WETH and DAI, implemented the core functionalities of the Synthetic Crude Oil Token using OpenZeppelin libraries. Cross-Chain Integration : Deployed the main contract on Optimism Sepolia, with price feeds provided by Chainlink. Used Chainlink CCIP to relay Crude Oil prices to Avalanche Fuji and Polygon Amoy networks. Front-End Development : Created a user-friendly web interface to interact with the smart contracts, including functionalities for logging in, depositing collateral, minting tokens, redeeming collateral, and updating prices. Testing and Deployment : Extensively tested the contracts on test networks to ensure reliability and security, then deployed the contracts to multiple blockchains. Challenges we ran into The journey was not without its challenges: Cross-Chain Communication : Ensuring seamless and reliable communication between different blockchain networks was a complex task, requiring careful design to handle potential issues with price updates and message relays. Security Considerations : Implementing a secure system for collateral management and liquidation required rigorous testing and review to prevent vulnerabilities. User Experience : Creating an intuitive and user-friendly interface was crucial, leading to multiple iterations on the design and functionality to ensure accessibility for users unfamiliar with DeFi. Accomplishments that we're proud of Successfully implemented a cross-chain solution using Chainlink CCIP to update Crude Oil prices across multiple networks. Developed a robust and secure system for managing collateral and synthetic tokens. Created a user-friendly interface that simplifies interaction with complex DeFi functionalities. Demonstrated the potential of RWA tokenization, providing a practical example of how traditional finance can transition to blockchain technology. What we learned Throughout this project, we gained valuable insights into: Smart Contract Development : Advanced our understanding of Solidity and secure smart contract implementation. Cross-Chain Technology : Learned the intricacies of using Chainlink CCIP for reliable cross-chain communication. DeFi Concepts : Deepened our knowledge of collateral management, liquidation mechanisms, and maintaining healthy collateral-to-debt ratios. User-Centric Design : Emphasized the importance of creating intuitive and accessible interfaces for DeFi platforms. What's next for Synthetic Crude Oil Token Looking ahead, we plan to: Expand Network Support : Integrate additional blockchain networks to broaden access and improve liquidity. Enhance Security : Continuously audit and improve the security of our smart contracts. Improve User Experience : Further refine the user interface and add new features based on user feedback. Explore Partnerships : Collaborate with traditional financial institutions and DeFi platforms to expand the use and acceptance of synthetic crude oil tokens. Educational Outreach : Promote the benefits and opportunities of RWA tokenization to encourage wider adoption in the financial industry. We are excited about the potential impact of RWA tokenization and look forward to seeing how it evolves in the future. We hope this project inspires others to explore the possibilities of decentralized finance and blockchain technology. <div