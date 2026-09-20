---
slug: "wisebets"
url: "https://devpost.com/software/wisebets"
title: "WiseBets"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 738
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "user/general_public"
  - "substrate/financial_record"
---

# WiseBets

> Give opinions & trade through Frames

[Devpost](https://devpost.com/software/wisebets) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**mechanism** [[provenance_signing]]
**user** [[general_public]]
**substrate** [[financial_record]]

**stack** ccip, chainlink, farcaster, frames, nextjs, solidity, typescript

## How they structured the write-up

- 💡inspiration
- 😃 what wisebets does
- 🔧 how we built wisebets
- 💪 challenges we ran into
- 🙌 accomplishments that we're proud of
- 📚 what we learned
- 💭 what's next for wisebets

## Body

💡Inspiration With over 200k monthly active users on Farcaster, we've found the perfect distribution layer to bring WiseBets to the masses. 📈🚀 Whether you're a seasoned crypto trader or just starting your journey, WiseBets makes it easy and fun to participate in the world of decentralized opinion trading. 😃 What WiseBets does The users can create exciting proposals or campaigns on various topics, from sports matches to crypto price predictions. All you need to do is choose your side, place your bets using USDC tokens, and wait for the outcome. The more accurate your predictions, the bigger your rewards. But wait, there's more! WiseBets is breaking down barriers and embracing the power of cross-chain interoperability. Thanks to the amazing Chainlink CCIP, you can now place bets from the Avalanche/Polygon Amoy network and have your tokens & bets seamlessly transferred. WiseBets is also deployed on the zkSync, Scroll, Polygon Cardona and Moonbeam networks, unlocking more liquidity on the platform. As Chainlink CCIP expands its support, we'll be right there, ready to bring you a truly multi-chain opinion trading experience. 🔧 How we built WiseBets We built this user-friendly UX using NextJS, React and TailwindCSS. Behind the scenes, typescript connects those functions which handle the multichain token transfer and place bet. The smart contract is written in Solidity to develop the functions that securely store campaigns and distribute rewards once the deadline is reached. It is deployed on multiple networks including Polygon Amoy, Avalanche Fuji, zkSync Sepolia, Scroll Sepolia, Polygon Cardona, and Moonbeam. This multi-chain approach ensures a wide reach and accessibility for our users. The goal is to provide simple UI and efficient channels for bridging liquidity and placing bets on any network. For reliable and tamper-proof price feeds, we integrated Chainlink Price Feeds into our smart contracts. This enables accurate settlement of prediction markets based on real-world data. To enhance the user experience and facilitate seamless token transactions, we integrated Batch Transactions with Moonbeam. This allows users to perform multiple actions in a single transaction, improving efficiency and reducing gas costs. Avalanche Fuji CCIP Bridge Polygon Amoy CCIP Bridge Base Sepolia CCIP Bridge Polygon Amoy WiseBets Contract Polygon Cardona WiseBets Contract Scroll Sepolia WiseBets Contract Avalanche Fuji WiseBets Contract Moonbeam WiseBets Contract zkSync Sepolia WiseBets Contract 💪 Challenges we ran into Our main challenge is to build the best user experience (UX). To address this issue, we have developed a farcaster frame that provides users with a seamless experience for bridging and betting on-chain effortlessly. We encountered some difficulties while building a transaction frame as it supports a limited number of chains. Another challenge for us is to provide users with a seamless multi-chain experience. To achieve this, we have built an easy-to-use bridge and a farcaster frame, which anyone can utilize to bridge USDC easily from one chain to another. 🙌 Accomplishments that we're proud of We are proud of successfully building a decentralized opinion market place that leverages the power of cross-chain interoperability. By deploying our smart contracts on multiple networks and integrating with Chainlink CCIP, we have created a platform that is accessible to a wide range of users and enables participation from various blockchain ecosystems. We are also proud of our integration with Chainlink Price Feeds, which ensures reliable and tamper-proof data for settling prediction markets accurately. Additionally, our integration with Batch Transactions on Moonbeam enhances the user experience and improves the efficiency of our platform. 📚 What we learned We utilized Chainlink's Cross-Chain Interoperability Protocol (CCIP) to bridge from one blockchain to another. For this, we learned how to incorporate CCIP into smart contracts. We acquired knowledge on how to utilize Chainlink's data feeds to obtain live ETH/USD pricing. We have employed Chainlink data feeds both on-chain and off-chain. We gained insights into working with multiple chains and making our decentralized application (dApp) multi-chain compatible. Additionally, we explored how transactions function on Farcaster frames as we integrated CCIP and on-chain betting into Farcaster frames as well. 💭 What's next for WiseBets As we grow, we'll be exploring the exciting concept of Futarchy, where collective wisdom can help guide decision-making on a larger scale. Imagine a world where your opinions not only earn you rewards but also contribute to shaping policies and governance! We will take feedback from the consumers and include the nitty gritty details over the iterations. We would like to add more features and improve user experience on the platform. <div