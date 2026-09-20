---
slug: "toqen-factory"
url: "https://devpost.com/software/toqen-factory"
title: "Toqen Factory"
hackathon: "TRON Grand Hackathon - HackaTRON Season 6"
organization: "TRON DAO"
winner: true
words: 464
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
---

# Toqen Factory

> Streamlined React Components for BTTC Integration.

[Devpost](https://devpost.com/software/toqen-factory) · hackathon [[TRON Grand Hackathon - HackaTRON Season 6]]

## Facets

  <sub>weak: revocation_withdrawal</sub>
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** foundry, react, solidity, tailwindcss, wagmi

## Body

Create ERC20 Component Create ERC721 Component Mint/Swap ERC20 Component Mint ERC721 Component Approve All ERC721 Approve ERC20 Disapprove All ERC721 GitHub: https://github.com/toqenfactory NPN: https://www.npmjs.com/package/@toqen/react BTTC: https://testnet.bttcscan.com/address/0x3AE2475877243dD4331c51BABa39832450526597#code Inspiration The Toqen Factory project sprang from a personal desire to streamline the process of token and NFT creation within the blockchain ecosystem. As a developer passionate about blockchain technology, I found the repetitive tasks involved in smart contract interactions cumbersome and inefficient. I envisioned a tool that would not only simplify these interactions but also enhance the creativity and productivity of fellow developers. This vision led to the birth of Toqen Factory—a React component library designed to seamlessly bridge the gap between smart contracts and frontend applications. What I Learned Throughout the development of Toqen Factory, I deepened my understanding of React's capabilities in managing stateful interactions in a decentralized environment. I also honed my skills in Solidity for smart contract development, particularly in ensuring security and efficiency. The project was a valuable exercise in integrating frontend technologies with blockchain backends via smart contracts. How I Built It Toqen Factory was built using: React.js : For the frontend library, leveraging hooks and context for state management. Solidity : To write the ToqenFactory smart contract that handles ERC20 and ERC721 token functionalities. BitTorrent Blockchain : Deploying the smart contract on the BitTorrent test network to ensure it was fully operational in a controlled environment. WAGMI : To connect the React components with BitTorrent blockchain, allowing for smooth transactions and interactions. The core of the project involves 3 main components: Create Component : Allows users to create ERC20 tokens and ERC721 NFTs. Mint Component : Allows users to mint ERC20 tokens and ERC721 NFTs to specified addresses. Approve Component : Enables token owners to authorize other addresses to spend tokens on their behalf, increasing the flexibility and utility of the tokens. The smart contract has a creator-only method of withdrawing all BTT tokens, from the token contract, if at creation it set the sale of 1 token to be greater than zero BTT. Challenges Faced One of the main challenges was ensuring the security and efficiency of the smart contracts. Debugging and testing on the blockchain often proved time-consuming due to transaction confirmation times and the immutable nature of deployed contracts. Another challenge was creating a user-friendly interface that could handle the complex interactions in a straightforward manner, making blockchain operations accessible to developers with varying levels of expertise. Conclusion Toqen Factory is more than just a project, it's a tool that empowers developers to unleash their creative potential in the blockchain space without being bogged down by the technical intricacies of smart contract management. It was a journey of learning, building, and overcoming challenges that reinforced my passion for blockchain technology and its potential to transform industries. <div