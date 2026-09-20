---
slug: "the-future-of-france-web-3-learning-game"
url: "https://devpost.com/software/the-future-of-france-web-3-learning-game"
title: "The Future of France | Web 3 Learning Game"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 1317
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/revocation_withdrawal"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# The Future of France | Web 3 Learning Game

> RPG-style browser game where players learn to safely use Web 3 applications, secure digital wallets, and avoid scams while navigating a blockchain-based world.

[Devpost](https://devpost.com/software/the-future-of-france-web-3-learning-game) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**mechanism** [[provenance_signing]] [[revocation_withdrawal]]
**domain** [[developer_tools]] [[finance_payments]] [[security_privacy]]
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]] [[structured_db]] [[web_dom]]

**stack** html, impactjs, javascript, mysql, php, solidity, web3js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for the future of france
- project links

## Body

ChatGPTo connected Quizbots ensure that players understand critical subject matter. Players can deposit ETH and delegate credit to a contract that mints GHO and sends it across chains. Players must use CCIP to complete the first mission assigned by the Commissioner. In the second mission players turn their in-game coins into an ERC20 token called "Blue Coin" by using Chainlink Functions. Didn't build a mission here yet but wouldn't it be cool to teach the players how to buy, sell, and provide liquidity using a DEX? Inspiration I helped onboard a friend to the Web3 space recently and realized that our space has a problem with adoption . Many of the things that we take for granted are learned skills that we've been developing for years. Basic tasks like connecting to websites, signing transactions, and approving token transfers are confusing and scary for new users. Worse still, these simple actions are often risky and fraught with danger. One misstep and the user can lose all assets. Oh my! In order to onboard the next generation of users to safely interact in the Web3 space, I created The Future of France . What it does The Future of France is a gamified learning experience that eases players into the wild and wondrous world of Web3. I used a technique known as task-based scaffolding , which I learned during my time as an educator, to better prepare players to succeed. The protagonist of the game is a Web2 developer who entered a cryogenic freeze in 2008 . He wakes up in the future and must interact with his environment using the technologies of the present. Players begin in a military lab and must complete a series of training levels prior to entering into an open world adventure. The seven training levels start with the most basic tasks that a Web3 user must perform: installing a browser wallet and connecting to a website. As players progress through the training levels, the complexity of the tasks increases. By the time they graduate from the training levels, these players will be depositing and withdrawing tokens from contracts and making VRF requests to mint NFTs. Players interact with a variety of NPCs connected to ChatGPTo . Instead of traditional dialogue tree options, the AI receives agent prompts and delivers responses from the assigned persona. Players submit open-ended input to these characters, allowing them to ask questions about concepts with which they are struggling or just have interesting chats. This leads to an infinite amount of fun and engaging interactions. ChatGPTo is further utilized to ensure that players demonstrate and appropriate understanding of critical subject matter, such as the difference between a password and a seed phrase in a browser wallet. As players travel through the training levels, they will encounter Quizbots— NPCs that stand in their path and do not allow them the pass. These Quizbots ask questions related to the tasks at hand, requiring players to provide open-ended answers. For example, in level 3 they need to explain how to identify and avoid signature phishing attacks. This mechanism ensures that players grasp essential concepts before progressing further. Once players graduate from the training levels, they enter an open-world adventure where they explore a blockchain-connected city. This city features buildings dedicated to various DeFi and Web3 concepts such as GameFi, DAOs, yield farming, NFTs, and more. Players encounter many interesting and unique characters, including one called the Commissioner who assigns rewarding missions. In the first mission, players must go to the AAVE bank building and deposit Sepolia ETH into their account. Then they delegate borrowing power to a game contract that mints GHO and uses CCIP to transfer it across chains to Arbitrum Sepolia. It's a pretty cool experience. Ultimately, I believe that The Future of France could be a valuable learning tool to help safely onboard future generations of Web3 users. How I built it I used a variety of vanilla web languages and open source tools to develop this gaming experience. Additionally, I utilized AI tools to create game assets such as pixel-art spreadsheets. Here are some of the libraries and tools that I used extensively: Web3JS - I used the Web3JS vanilla JavaScript code base to interact with Ethereum RPCs on the client side. Simple Web3 PHP Interface - I used this PHP interface to create in-game ETH faucets. ImpactJS - I used ImpactJS as my game engine. ImpactJS is a pure vanilla JavaScript game engine for building HTML5/JS games. PixelLab - I used PixelLab, an AI-powered extension for Aseprite, to rapidly produce pixel-art sprite sheets for all the NPCs. Additionally, the project relied heavily on a full suite of Chainlink services. Chainlink Automation I used Chainlink Automation to trigger a withdraw function to send ETH back to the in-game faucet on a monthly basis. Chainlink Functions I used Chainlink Functions to verify that players completed graduation requirements prior to minting the graduation gift token. I also used Chainlink Functions to convert the Blue Tokens that players collected in-game into the ERC20 Blue Tokens. Chainlink VRF I used Chainlink VRF to mint randomized graduation gifts for players who reach level 7. Chainlink CCIP I used CCIP for the first task that the Commissioner assigns players once they graduate to the open-world adventure. Players go to an AAVE bank, deposit Sepolia ETH, delegate borrowing power to a game contract, mint $10 of GHO , and use CCIP to transfer it from Ethereum Sepolia to Arbitrum Sepolia . Challenges I ran into I've never built a top-down RPG style game. The characters essentially move like spaceships; however, maintaining the illusion of depth is more challenging than it seems . If one character moves to a higher position than another, the z-indexes need to adjust so that the graphics make sense spatially for players. This presented an interesting challenge that I believe that I solved fairly well. Another challenge I ran into was how to onboard new users who don't have any test ETH . I'm used to building applications for more advanced users who I presume have and can obtain their own ETH. But the premise of this game is to teach entirely new users about the world of Web3 . I solved this by using a simple web3 php interface to create an in-game ETH faucet. Accomplishments that I'm proud of I'm pleased with my ChatGPT integration. This is my first time using ChatGPT in a project , and I believe I've implemented it in a fun and useful way. I'm excited about the concept of integrating it into more projects I create, further unlocking its revolutionary potential. What I learned I believe this project is the culmination of everything I've been learning and building throughout my life. Though I've only spent around a month working it, I can see myself dedicating much more time to developing and refining The Future of France . It has the potential to be a truly helpful application that can have a significant impact on our space and the lives of many people. What's next for The Future of France If the project is well-received, I will continue building tasks in the open world for future players to complete. As our space grows and develops, the game content could grow alongside it. There is a potential monetization strategy in accepting sponsorships from Web3 companies eager to showcase their projects and technologies to new users. We could develop training missions for players that would encourage them to interact with these tools. The potential for The Future of France is boundless! Project Links Play Now at fofrance.com GitHub Repository Graduation Gift NFTs on OpenSea Chainlink Subscription Pages Chainlink Functions Chainlink VRF Chainlink Automation Verified Contracts: FOFBlueKeyToken FOFBlueKeyTokenVendor - CL AUTOMATION FOFBlueKeyTokenHolderContract FOFGraduationGiftNFTContract FOFGraduationGiftMintCheckCLF - CL FUNCTIONS FOFGradGiftToken FOFGraduationGiftMinterVRF - VRF FOF_GHOSender - CCIP CCIP_Token_Sender - CCIP Blue Coin Token Blue Coin Token Minter - CL FUNCTIONS <div