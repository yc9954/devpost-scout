---
slug: "toba-token-bound-accounts-on-tron"
url: "https://devpost.com/software/toba-token-bound-accounts-on-tron"
title: "TOBA - Token Bound Accounts On Tron"
hackathon: "TRON Grand Hackathon - HackaTRON Season 6"
organization: "TRON DAO"
winner: true
words: 833
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# TOBA - Token Bound Accounts On Tron

> Discover new way to interact with NFTs and expand its capabilities beyond simple static collectibles, now any TRC-721 asset can be a token-bound account.

[Devpost](https://devpost.com/software/toba-token-bound-accounts-on-tron) · hackathon [[TRON Grand Hackathon - HackaTRON Season 6]]

## Facets

**substrate** [[financial_record]] [[video_visual]]

**stack** nextjs, solidity, tailwind, tronweb

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for toba - token bound accounts on tron
- test instructions

## Body

landing user's wallet token-bound account transfer assets from the tba deploy a tba game front gameplay with habilities Inspiration The inspiration behind the project to bring a new way to interact with NFTs on the TRON network was driven by the desire to expand the capabilities of these assets beyond traditional static collectibles. By introducing token-bound accounts for TRC-721 assets, the project aimed to revolutionize the way users engage with NFTs, allowing for more dynamic and interactive experiences. The implementation of token-bound accounts not only enhances the functionality of NFTs but also opens up a myriad of possibilities for advanced use cases, unlocking a new realm of potential for these digital assets within the TRON ecosystem. What it does Following the recommendations of the ERC-6551 standard for the implementation of Token-Bound Accounts in Ethereum VM-compatible networks, contracts have been deployed to enable the creation and management of TBAs within the TRON blockchain, then, a dApp has been developed to facilitate the creation, management and administration of Token Bound Accounts using a friendly interface where users can interact directly with the assets within their NFTs, being able to transfer them to different accounts, either EOAs or TBAs. Imagine transfer a group of assets just by doing one transaction, well, something like that is what happens when you send an NFT (who has a TBA) to another wallet, you are transferring the ownership of the TBA too, and in the practical sense you didn’t had to make X number of transactions to move all the assets, that’s the power of this implementation. To demonstrate the practical application of Token Bound Accounts (TBA), we have developed a captivating mini-game that showcases the unique capabilities of TBAs within the TRON ecosystem. The mini-game creates the profiles as NFTs that have a TBA and as the user gains skills (represented as NFTs) they are transferred into it. This makes the player's profile status completely on-chain and it can be exchanged between different wallets without losing the progress of the game account. By integrating TBAs with NFTs, players can experience a new level of autonomy and interactivity, allowing them to trigger on-chain actions and unlock special features tied to their NFTs. This innovative approach not only enriches the gaming experience but also highlights the potential for leveraging TBAs in various use cases across different industries. How we built it TOBA’s project is made up of three parts: the Smart Contracts for the Registry and the Accounts implementation which are made in Solidity following the standard ERC-6551 and deployed over Tron network, the frontend made with NextJS, TronWeb and is using TronLink to interact with the user’s wallet. Finally the minigame was developed using PhaserJS Challenges we ran into The difference in the deployment of proxy contracts compared from EVM to TVM is something minimal but essential to get the desired behavior when generating the new addresses, and the encoding of functions using Javascript for the EVM is pretty straight forward with libs like Viem but for the TVM Tronweb didn’t have those easy methods, so we had to go deep down in docs to implement that function. Accomplishments that we're proud of Deploy, adjust and test the required contracts for the implementation of token-bound accounts on the Tron Virtual Machine (TVM) Make the dApp frontend to create and manage the token-bound accounts Make the mini game Bring to the Tron network a new wave of advanced use cases for NFTs What we learned Smart contracts in Tron and interactions with TRC20 and TRC721 standards. The key differences between the EVM and TVM The logic behind the ERC-6551 standard What's next for TOBA - Token Bound Accounts On Tron Deploy the contracts and dApp to the mainnet after testing and feedback phases Test Instructions To test you will need to have the TronLink wallet extension installed in your browser. Once you have the wallet you must be conected to the Nile testnet and get some TRX from this faucet https://nileex.io/join/getJoinPage , then go to https://tobaontron.xyz In the landing you can press the button "try it with your NFTs" and that will take you to your wallet's view (It will only show TRC721 assets). If you don't have assets a button to mint some test NFTs will show, then after mint you will be able to generate token-bound accounts by accessing to the details of the token. After the creation of the TBA you will be able to send tokens and collectibles into those accounts using the address that appears in the NFT details. You can transfer out the assets from the TBA using the transfer button at the right of each asset. You will be able to access the mini game by clicking in the image on the bottom of the landing page and mint a game profile by clicking in the "Profile" button. Then you can play and collect power-ups for your character by getting high scores and those NFTs will be shown in the TBA view too. <div