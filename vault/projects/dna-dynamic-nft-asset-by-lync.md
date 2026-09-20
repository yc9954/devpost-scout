---
slug: "dna-dynamic-nft-asset-by-lync"
url: "https://devpost.com/software/dna-dynamic-nft-asset-by-lync"
title: "DNA - Dynamic NFT Asset by LYNC"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 612
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/genomic_bio"
---

# DNA - Dynamic NFT Asset by LYNC

> Enabling dynamic NFTs as in-game assets for the masses

[Devpost](https://devpost.com/software/dna-dynamic-nft-asset-by-lync) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]] [[genomic_bio]]

**stack** c#, chainlink, ipfs, javascript, keeper, lighthouse, node.js, react, solidity, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dna - dynamic nft asset by lync

## Body

DNA - V1 : Dynamic NFT Asset by LYNC Inspiration NFT as an upgradable in-game asset hasn't been explored much because of its complexities and simplified infrastructure is missing atm. Most traditional game developers are unable to list their in-game assets and customizable/upgradable assets as NFT. Our aim is to remove this friction so that web2 and web3 game developers can push their in-game assets in mins. What it does DNA - V1 allows game developers to create upgradable NFT as in-game assets. It allows true digital ownership to the gamers where they can upgrade their collected skins or assets as NFT in real time. It provides the same gaming experience and allows digital assets to get upgraded on completing specific milestones. With DNA-V1 SDK game developers can integrate and list their in-game assets as upgradable NFT in hours than months. How we built it We started with the ideation of making in-game assets as upgradable NFTs without disturbing the gaming experience. We then did several meetings with web2 and web3 game studios and developers. We came up with the idea of DNA (Dynamic NFT Assets) to solve this issue and share another possibility of NFT with everyone. We started with keepers for the automation of smart contracts to check on upgrading NFT. We converted the ERC-721 NFT contract to dynamic NFT which can be used as an in-game asset inside the game. NFT getting minted from the game engine itself and once the player reaches a milestone that allows them to upgrade to a new character they can upgrade the NFT as an in-game asset from the game engine directly. Keepers checks every second if the condition matches it will run perform upkeep Challenges we ran into We started with a basic ERC-721 NFT contract and wanted to have those NFTs upgraded when a user inside the game reaches a certain milestone or completes a level or acquires another in-game asset that can be a part of the character. But the biggest challenge was to automate this process and make it possible that smart contract interactions are happening via the game engine itself, and for that, we created our own Metamask SDK that can be integrated inside game engines, too in less than 30 secs and we have the account address that connected the wallet to check if that user can even proceed with the transaction to go forward and upgrade. Keepers or Smart contract automation played a major role in the creation of dynamic and upgradable NFTs which can be used inside a game as in-game assets. As through keepers, we have the possibility to check if the XP/Level of the user increased and if yes, how to intensive them. Accomplishments that we're proud of So far the scope of NFT as in-game upgradable assets was not being achieved and we are proud to take the initiative and solve this issue with Chainlink's KEEPER. What we learned We explored another possibility of chainlink's keeper and learned more about upgradable NFTs and in-game assets and their importance and possibilities. What's next for DNA - Dynamic NFT Asset by LYNC In the upcoming versions of DNA, we will be optimizing the smart contract and making a simplified dapp where game developers can list their in-game assets as upgradable NFTs and also set the milestones where the evolution of digital assets will take place. As it is the first version of DNA, in the upcoming version our main goal is to work on the SDK and make it live for the masses. In the upcoming version we will allow animations and skills to get upgraded in a truly decentralized manner via DNA. <div