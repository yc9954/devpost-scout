---
slug: "thetafans"
url: "https://devpost.com/software/thetafans"
title: "ThetaFans"
hackathon: "Theta Network 2023 Hackathon"
organization: "Theta Labs"
winner: true
words: 1013
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/revocation_withdrawal"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# ThetaFans

> ThetaFans: NFT-powered video platform. Unlock exclusive content through subscription tiers, while revolutionizing content monetization. Plus, gain complete control over your profile data as a creator.

[Devpost](https://devpost.com/software/thetafans) · hackathon [[Theta Network 2023 Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[revocation_withdrawal]]
**domain** [[civic_government]] [[developer_tools]] [[finance_payments]]
**user** [[developer]] [[general_public]]
**substrate** [[financial_record]] [[video_visual]] [[web_dom]]
  <sub>weak: geospatial</sub>

**stack** ethersjs, javascript, next-js, solidity, theta-blockchain, theta-nfts, theta-video-api

## How they structured the write-up

- technology stack & tools
- upload video mechanisms

## Body

Explore Creators Content Creator Profile Content Creator Signup Page Before Subscription Creator Page Subscribe to a content creator After Subscription Creator Page Admin Fee Withdrawal restricted to Admin Only Admin Fee Withdrawal (Only Admins) Video Upload restricted to content creators only Video Upload Page (Only Content Creators who are owner of the contract) 1. Problem Costly intermediaries in content monetization. Thetafans solves the problem of costly intermediaries in content monetization by leveraging blockchain technology, enabling direct and secure transactions between creators and fans without the need for intermediaries, such as payment processors, resulting in increased revenue for creators. 2. Solution: Thetafans and What it does Thetafans, a platform built on the Theta blockchain and powered by the Theta Video API, offers a range of exciting features. Creators can monetize their content through membership tiers, providing exclusive perks and rewards to their fans. The platform utilizes NFT ownership, allowing creators to gate their videos behind unique digital assets, creating a sense of exclusivity. Additionally, Thetafans operates without any fees, ensuring that creators retain more of their earnings. With Thetafans, content creators can engage with their fans, build a loyal community, and revolutionize the way content is monetized, all supported by the secure and efficient infrastructure of the Theta blockchain and its powerful Video API. 3. Architecture & Technology Stack For smart contract development, Thetafans utilizes Remix IDE, providing an intuitive and feature-rich environment. Remix IDE streamlines the creation, testing, and deployment of Ethereum smart contracts, ensuring efficiency and reliability. To ensure robust testing and deployment of smart contracts, Thetafans relies on Hardhat, a comprehensive development environment. Hardhat offers powerful tools for Ethereum development, enabling thorough testing and seamless deployment of smart contracts on the Theta blockchain. For the frontend development of the Thetafans website, Next.js is employed. Next.js, a React framework, enables server-side rendering and optimized routing, delivering fast page loads and an interactive user experience. It ensures that Thetafans offers a responsive and engaging interface for content creators and fans. To enhance video streaming capabilities, Thetafans harnesses the Theta Video API. This specialized API, provided by the Theta blockchain, optimizes video content delivery, ensuring high-quality streaming experiences. The Theta Video API empowers Thetafans to provide a seamless, scalable, and secure platform for creators and fans to enjoy immersive video streaming. Technology Stack & Tools IDE: Visual Studio Code Remix IDE Web Frontend Next.js Ethers.js Rainbowkit Wagmi.js Moralis Upload Video Mechanisms When a creator uploads video content, the portal will send an HTTP Post request to the Web API with the title of the video, description, and the video file itself to the Web API. The Web API will process the data received from the portal and posts the public link the smart contract. After the public link has been stored into a new video struct inside of the smart contract. The video along with its information can then be retrieved by entering the index of a creator's content via video structs. The public link is read by the front end website, and is shown if a user has access to the video (via NFT ownership + active subscription). Note, we had originally planned for videos to be gated behind specific NFT ownership, but THETA BRM API is not featured in the THETA Testnet. We have opted for mappings inside of the contracts to determine a users subscription level and duration Users who own the NFT, and have an active subscription are permitted to watch the locked content. 5. Features For Platform: We charge creators 20% of their subscription fees, which helps incentivize the developers and owners of the platform to put more effort and time in improving, and maintaining the platform further. For Creators: Content Monetization: Monetize your content through paid subscriptions, exclusive content, and fan donations. Subscription Tiers: Create multiple subscription tiers with different pricing and benefits to cater to various fan preferences. Exclusive Content: Offer exclusive content, behind-the-scenes footage, bonus videos, or early access to engage and incentivize subscribers. User Profiles: Showcase your content, provide descriptions, and engage with your fan base through personalized user profiles. Transparent Analytics: Access detailed analytics and insights about content performance, subscriber growth, and revenue to optimize your strategy. Secure Transactions: Ensure secure and fair compensation for your work with blockchain technology and smart contracts. Direct Fan Interaction: Engage with fans through comments, likes, and shares, fostering a sense of community and connection. Streamlined Video Integration: Seamlessly integrate with the Theta Video API for high-quality and uninterrupted video streaming experience. For Users: Access to Exclusive Content: Subscribe to creators and gain access to exclusive content, creating a unique and personalized experience. Direct Interaction: Interact directly with creators through comments, likes, and shares, fostering a sense of community. Multiple Subscription Tiers: Choose from different subscription tiers with varying benefits to suit your preferences and support your favorite creators. Discover New Creators: Explore a wide range of creators and discover new talent within the ThetaFans community. Enjoy Seamless Video Streaming: Experience high-quality video streaming without interruptions or buffering issues. Secure Transactions: Benefit from secure and transparent transactions enabled by blockchain technology. User-Friendly Interface: Enjoy a user-friendly platform interface that is easy to navigate and interact with. 6. Value to Theta Ecosystem ThetaFans is a valuable addition to the Theta Ecosystem, offering content creators the opportunity to monetize their work directly. By providing a platform for creators to earn revenue through subscriptions, exclusive content, and donations, ThetaFans incentivizes the production of high-quality content within the Theta network. This engagement and revenue generation not only benefit creators but also foster a strong sense of community, encouraging active participation and interaction between creators and fans. Moreover, ThetaFans plays a crucial role in driving the adoption and usage of Theta tokens (TFUEL) within the ecosystem. Creators receive TFUEL as payments, which increases the circulation and demand for the tokens. As the platform attracts more creators and users, it creates network effects, strengthening the overall ecosystem's value and utility. Additionally, the diversification of content and the technological advancements driven by ThetaFans further enhance the appeal and innovative nature of the Theta Ecosystem. <div