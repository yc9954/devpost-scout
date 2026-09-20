---
slug: "kanvas-in-game-dynamic-nfts"
url: "https://devpost.com/software/kanvas-in-game-dynamic-nfts"
title: "Kanvas | Customizable Dynamic NFTs"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 1057
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Kanvas | Customizable Dynamic NFTs

> Unlock boundless creativity in gamified dApps with Kanvas. Craft dynamic and customizable NFTs at the smart contract level.

[Devpost](https://devpost.com/software/kanvas-in-game-dynamic-nfts) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[video_visual]] [[web_dom]]

**stack** avalanche, chainlink, docker, firebase-storage, netlify, openzeppelin, polygon, thegraph, truffle, wagmi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- illustration
- challenges we ran into
- accomplishments that we're proud of
- why use kanvas?
- what we learned
- some use cases
- revenue models
- what's next for kanvas | in-game dynamic nfts
- networks (testnet)
- plans for dapps on subnet
- lastly, have fun ⚡

## Body

Homepage Illustration List of games Game dNFT templates Designing a dNFT template Create a new game Plans RockPaperScissors Game RockPaperScissors Game Result RockPaperScissors Game dNFT Illustration Functions CCIP Game Events Inspiration We conceived Kanvas with the aim of assisting web3 game creators in crafting compelling in-game items capable of adapting and functioning seamlessly across different blockchains. These items, referred to as dNFTs, have the ability to display real-time updates and can be personalized with players' names, scores, and other gaming information. What it does Kanvas harnesses the Avalanche C-Chain to facilitate the generation of dynamic in-game NFTs. As a game developer, you can seamlessly integrate Kanvas into your game smart contracts to generate dynamic and customizable NFTs for players at the smart contracts level. Your smart contracts simply need to extends and call the Kanvas smart contract with a payload to specify NFT customization details. Utilizing Chainlink Functions, Kanvas smart contracts then interacts with a remote image rendering server using the payload and also retrieves our game dNFT template you’ve created on the Kanvas dApp to compute a unique customized dNFT. The generated dNFT is then uploaded to a remote storage server, and the metadata URI is returned to the game contract via a callback function. For games supporting multiple chains, Kanvas enables the transfer of player-customized NFTs without losing the dNFTs data. For instance, you can commence playing GameA on Avalanche, earn in-game points, and then transfer your GameA dNFT from Avalanche to Polygon without resetting your in-game points and other positions. How we built it Kanvas Smart Contracts: The core smart contracts are deployed on the Avalanche C-Chain, with some also deployed on other chains like Polygon for cross-chain interoperability with CCIP. These core smart contracts play crucial roles in managing games, fees, and usage limits, cross-chain communications, and triggering off-chain components like the dNFT rendering servers. Kanvas dApp: A web application built for game developers with the capability to easily interact with the Kanvas core smart contracts on Avalanche (Fuji) to link the IKanvasGame to the Kanvas core contracts. It also provides a drawing canvas for designing dNFT templates that are later compiled into SVG formats and uploaded to a remote storage. Kanvas Subgraph: The subgraph component is built with and deployed on TheGraph network to index the events from the Kanvas core contracts. This is a crucial layer in the application that seamlessly provides the API for our different components to connect to each other. Kanvas Rendering Server: The server is triggered by the Kanvas core contracts with necessary parameters like the game address, player address, and customization details. It fetches the needed data, such as the template URI from the subgraph endpoint. It then uncompiled the SVG data from the template URI, replaces the fields in $string$ format with associated player property, compiles back the manipulated SVG, renders the SVG as a PNG format, and uploads it to a remote storage. The PNG is then used to compute an NFT metadata JSON, which is also uploaded to a remote storage. The JSON URL is returned back to the core contract with the help of Chainlink, and from the core contract to the game callback function with the playerId and URL to the NFT metadata. Therefore, the game contract has the flexibility of using it for any kind of operation, such as minting and NFT. Illustration Challenges we ran into During the development of Kanvas, we encountered obstacles in optimizing gas usage, ensuring secure data transfer between smart contracts, and efficiently managing dynamic NFT customization. Solving these challenges has helped us learn and gain experience in how interoperability works. Accomplishments that we're proud of We are immensely proud of successfully implementing real-time updates for in-game NFTs, achieving cross-chain interoperability with Chainlink's CCIP protocol, and deploying our own subgraph. Why use Kanvas? Feature Using Kanvas Using AI models Image output Full control Less control Time Avg. 4-10secs Avg. 40-120secs Cost Avg. $0.07 per request Avg. $0.12 per request On-chain Integration Beginner level Intermediate level Others Built-in cross-chain capabilities It's AI This table shows why you should use Kanvas to generate dNFTs over AI models. What we learned Throughout the development of Kanvas, we gained valuable insights into optimizing gas usage in smart contracts, implementing secure cross-chain data transfers, and leveraging Chainlink to call remote APIs for dynamic NFT generation. These learnings contribute to our continuous improvement and commitment to innovation. Some use cases Gaming: Creating personalized game experiences for gamers is a big win for game developers; the ability to create customized game NFTs for a single user can revolutionize the whole gaming industry. Social: Imagine a web3 streaming platform that can mint a unique NFT for its users customized with their listening time, number of likes, favorite album cover, and so on. RWAs: Most Real World Assets are not static in nature, so should the NFTs representing them. With Kanvas, dApps can reflect the changes of RWAs on the NFT metadata. Certification: Performance-based completion or authority-based approval can automatically generate immutable NFTs on the blockchain as credentials with the holder information. https://github.com/devarogundade/kanvas/tree/main/blockchain/contracts/use-cases Revenue models Name Cost Usage Starter 0.003AVAX per request up to 50 users. up to 3 dNFT templates. Business 0.003AVAX per request plus 5AVAX one-time fee up to 10,000 users. up to 10 dNFT templates. cross-chain support. Enterprise 0.003AVAX per request plus 20AVAX one-time fee unlimited users. up to 25 dNFT templates. cross-chain support. We profit by adding small fee on the amount needed to carry out an off-chain request or cross-chain messages. What's next for Kanvas | In-Game Dynamic NFTs As we look ahead, we plan to improve Kanvas by incorporating additional features such as enhanced customization options, batch updates for gas optimization, image rendering, and integration of Chainlink VRF for games relying on random values, such as lucky draws. These advancements will further solidify Kanvas' position as a comprehensive solution for web3 game developers seeking dynamic and customizable in-game NFTs. Networks (Testnet) Network Kanvas Address Avalanche C-Chain (main) 0x73351AA82c08630b10BCBe4896fdD1c17903b7C4 Polygon 0x6DbE734eAD4A25c2d48554df6d4c7196255cE251 Plans for dApps on subnet We believe Avalanche is the most suitable chain for game developers and with the power to run on a separate network for faster finality. We plan to collaborate with projects on subnets to integrate Kanvas into their dApps. Lastly, have fun ⚡ Play Rock, Paper, Scissors to earn your first customized NFT. <div