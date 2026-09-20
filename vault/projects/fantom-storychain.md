---
slug: "fantom-storychain"
url: "https://devpost.com/software/fantom-storychain"
title: "Fantom StoryChain"
hackathon: "Fantom Hackathon Q2 2023"
organization: "Fantom Foundation"
winner: true
words: 741
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "substrate/video_visual"
---

# Fantom StoryChain

> Fantom StoryChain is a multi-level AI based dapp where users collaboratively create stories that have unique chapters and arts using Language AI, Image AI and NFTs.

[Devpost](https://devpost.com/software/fantom-storychain) · hackathon [[Fantom Hackathon Q2 2023]]

## Facets

**domain** [[civic_government]]
**substrate** [[video_visual]]

**stack** ai, amazon-web-services, chatgpt, covalent, fantom, leonardoai, nft, node.js, react, solidity

## How they structured the write-up

- inspiration
- what it does
- technologies
- how i built it
- challenges i ran into && what i learned
- accomplishments that i'm proud of
- what's next for storychain
- repos

## Body

Inspiration Always wanted to participate on chain stories where different users write paragraphs combining into a collaborative story; but I lacked the writing or drawing skills. Thanks to the development of AI this is no longer a problem as a language AI can write a story and image generation AI can create the art. The system supports multiple AI alternatives for users to choose from, creating a dynamic ecosystem. For consistency reason, once a story is created with a specific AI, it continues using it. What it does StoryChain , a new take on the ages old classic chain of stories, where different users collaboratively create stories. Using this dapp, users create stories that have unique chapters and arts using web3, AI, NFTs, IPFS. Each page can belong to a different user. Once a user creates a story, they define the category (such as if it is a childrens' story), select the story AI and also the image generation AI. Once the story is created, users simply read the previous chapters and enter a prompt however they wish to continue. So a story is created collaboratively by the users and each page belongs to one user with unique story and art. More if it, this page itself is minted as an NFT for the user; which can be visited on NFTSCAN or PAINTSWAP. Technologies Fantom Blockchain ChatGPT for AI Story Generation LeonardoAI / Gencraft / StableDiffusion / OpenJourney for AI Image Generation AWS for hosting NodeJS backend Covalent API to get contract events React for frontend How I built it Once the prompt is entered, NodeJS backend server running on AWS catches the emitted events from the contract and applies multiple steps on it; Uses Covalent API to get contract events Checks if the prompt is suitable for the category (For an example if it's a children's story and the user asked the character to burn down a forest, the prompt is rejected) It gets the latest story data from IPFS , Providing entire story to chatgpt, asks to create a new chapter that would fit the continuity, and also create a prompt for ai image generator AI Image generator generates an image for our chapter Then we upload the image to IPFS Upload the entire story with new chapter and the image to IPFS Then submit these IPFS hashes to the contract And finally the contract mints an NFT for the author of the new chapter The metadata for the NFT items is stored on-chain and IPFS. After an update on the story, user's chapter now have the story and the image, and this chapter also belongs to the author as an NFT. We can also view this NFT or other chapters or other books on NFTSCAN / PAINTSWAP. The story metadata on IPFS is also available to view. Another option for creating a story is using the voting mechanism . When creating a story, user can select if the future entries to the story requires voting. This way each story becomes a DAO itself. When a user wants to continue to the story, they enter their prompt. Then in a certain period, NFT owners submit their votes to their favorite prompt, creator having an extra half vote to break the equal votes. At the end of the voting period, prompt with the highest vote is used to continue the story, minting the NFT to the elected prompt owner. This way as the story grows, a larger community forms within, increasing the chance of higher quality prompts to be entered. Other users can choose to buy NFTs from the authors to have a vote in the decision. Challenges I ran into && What I learned I used many different tools for this project. Learning AI prompts, language AI API, Image Generation API and their prompt engineering was a challenge. Accomplishments that I'm proud of I always wanted to participate in chain stories but always lacked the talent. This time while developing this project I had tremendous fun. What's next for StoryChain The project can only go forwards. Of course many aspects of the project depends on the improvements of AI models, especially the speed of image generation; but the project still have some way to go. Such as trying to use better prompts on handling consistence character arts between pages and better story telling prompts. Repos Demo: https://storychain.ai Github (Contracts, Frontend, Backend): https://github.com/cemleme/fantom-storyChain Contract: https://ftmscan.com/address/0xcD2cf70Ab89b16b972D6b1119AAd51A32A97Ec73 NFTSCAN: https://fantom.nftscan.com/0xcD2cf70Ab89b16b972D6b1119AAd51A32A97Ec73 PAINTSWAP: https://paintswap.finance/marketplace/fantom/collections/0xcd2cf70ab89b16b972d6b1119aad51a32a97ec73/nfts <div