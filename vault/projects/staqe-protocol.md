---
slug: "staqe-protocol"
url: "https://devpost.com/software/staqe-protocol"
title: "Staqe Protocol"
hackathon: "TRON Grand Hackathon - HackaTRON Season 6"
organization: "TRON DAO"
winner: true
words: 453
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "substrate/video_visual"
---

# Staqe Protocol

> Non-castodial pools for NFT and token staking.

[Devpost](https://devpost.com/software/staqe-protocol) · hackathon [[TRON Grand Hackathon - HackaTRON Season 6]]

## Facets

**mechanism** [[provenance_signing]]
**substrate** [[video_visual]]

**stack** foundry, nextjs, plasmo, solidity, typescript, wagmi

## How they structured the write-up

- inspiration
- what i learned
- how i built it
- challenges faced
- conclusion

## Body

Pool Rewards Panel User Dashboard Pool (Staker) Pool (Admin) Launch New Pool Staqe Contract: https://testnet.bttcscan.com/address/0x9cbd0a9d9fb8e8c1baa4687e4e8068ada57a220f Github: https://github.com/staqeprotocol Inspiration The inspiration for Staqe came from recognizing a gap in the decentralized finance (DeFi) ecosystem for a flexible, user-driven approach to staking NFTs and ERC20 tokens. We noticed that most staking platforms were rigid, offering little to no control over the terms and conditions of liquidity pools. We aimed to empower users by enabling them to create and manage their own staking pools with custom settings, enhancing both the accessibility and utility of NFTs and tokens in the DeFi space. What I Learned Throughout the development of Staqe, I learned a great deal about smart contract development, particularly in designing non-custodial, decentralized protocols that are both secure and efficient. I deepened my understanding of the BTTC blockchain, the ERC721 and ERC20 standards, and how to interact with BTFS for decentralized storage. The integration of these technologies was crucial in allowing for a robust and flexible platform where metadata and assets could be managed transparently and reliably. How I Built It Staqe was built using Solidity for the smart contracts, providing the backbone of the protocol on the BTTC blockchain. For the front-end, React combined with the WAGMI library was used to create a responsive and intuitive interface that interacts with the blockchain. We used IPFS/BTFS for storing off-chain metadata securely, ensuring that data such as pool descriptions, logos, and images are decentralized and tamper-proof. The process involved: Designing and deploying smart contracts for creating and managing staking pools. Integrating these contracts with a front-end using React to provide a seamless user experience. Setting up IPFS/BTFS for off-chain metadata storage to comply with the ERC721 standard. Implementing extensive testing to ensure security and functionality across all features. Challenges Faced One of the major challenges was ensuring that the platform remained fully non-custodial while providing the necessary flexibility and control to the pool creators and stakers. Balancing security, usability, and decentralization required careful planning and numerous iterations. Another challenge was the integration of both on-chain and off-chain data, which had to be seamless to ensure a smooth user experience while maintaining the integrity and decentralization of the data. This was particularly complex when handling uploads and retrievals from IPFS. Lastly, educating users about the new concepts introduced by Staqe, such as creating their own liquidity pools and the significance of non-custodial staking, was an ongoing effort. Conclusion Building Staqe has been a profoundly enriching experience, filled with learning and overcoming complex challenges. It stands as a testament to the potential of decentralized technologies to provide more control and flexibility to users, paving the way for innovative uses of NFTs and ERC20 tokens in the DeFi ecosystem. <div