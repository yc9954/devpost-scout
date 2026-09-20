---
slug: "storychain"
url: "https://devpost.com/software/storychain"
title: "StoryChain"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 894
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "substrate/video_visual"
---

# StoryChain

> StoryChain is a multi-level AI based dapp where users collaboratively create a stories that have unique chapters and arts using Language AI, Image AI, NFTs and Chainlink functions for AI moderation

[Devpost](https://devpost.com/software/storychain) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**domain** [[civic_government]]
**substrate** [[video_visual]]

**stack** ai, amazon-web-services, chainlink, chainlinkfunctions, chatgpt, javascript, leonardoai, react, solidity

## How they structured the write-up

- inspiration
- what it does
- technologies
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for storychain
- repos

## Body

https://storychain.ai Inspiration Always wanted to participate on chain stories where different users write paragraphs combining into a collaborative story; but I lacked the writing or drawing skills. Thanks to the development of AI this is no longer a problem as a language AI can write a story, image generation AI can create the art and Chainlink functions can moderate the prompt for me. The system supports multiple AI alternatives for users to choose from, creating a dynamic ecosystem. For consistency reason, once a story is created with a specific AI, it continues using it. What it does StoryChain , a new take on the ages old classic chain of stories, where different users collaboratively create stories. Using this dapp, users create stories that have unique chapters and arts using web3, AI, NFTs, IPFS and Chainlink functions for moderation. Each page can belong to a different user. Once a user creates a story, they define the category (such as if it is a childrens' story), select the story AI and also the image generation AI. Once the story is created, users simply read the previous chapters and enter a prompt however they wish to continue. So a story is created collaboratively by the users and each page belongs to one user with unique story and art. More if it, this page itself is minted as an NFT for the user; which can be visited on OpenSea. Technologies Chainlink Functions using ChatGPT for AI moderation Solidity / Chainlink Functions Smart Contract Starter Kit ChatGPT for AI Story Generation LeonardoAI / Gencraft / StableDiffusion / OpenJourney for AI Image Generation AWS for hosting NodeJS backend React for frontend How I built it When user enters a prompt, the contract uses Chainlink Functions to check if this prompt is suitable for the selected category, using ChatGPT. For an example if it's a children's story and the user asked the character to burn down a forest, the prompt is rejected by Chainlink Functions. Once the prompt is approved, NodeJS backend server running on AWS catches the emitted events from the contract and applies multiple steps on it; It gets the latest story data from IPFS , Providing entire story to chatgpt, asks to create a new chapter that would fit the continuity, and also create a prompt for ai image generator AI Image generator generates an image for our chapter Then we upload the image to IPFS Upload the entire story with new chapter and the image to IPFS Then submit these IPFS hashes to the contract And finally the contract mints an NFT for the author of the new chapter The metadata for the NFT items is stored on-chain and IPFS. After an update on the story, user's chapter now have the story and the image, and this chapter also belongs to the author as an NFT. We can also view this NFT or other chapters or other books on OpenSea. The story metadata on IPFS is also available to view. Another option for creating a story is using the voting mechanism . When creating a story, user can select if the future entries to the story requires voting. This way each story becomes a DAO itself. When a user wants to continue to the story, they enter their prompt, which is also safety checked by Chainlink Functions. Only if approved, it ends up on the voting list. Then in a certain period, NFT owners submit their votes to their favorite prompt, creator having an extra half vote to break the equal votes. At the end of the voting period, prompt with the highest vote is used to continue the story, minting the NFT to the elected prompt owner. This way as the story grows, a larger community forms within, increasing the chance of higher quality prompts to be entered. Other users can choose to buy NFTs from the authors to have a vote in the decision. Challenges I ran into This was the first time I used Chainlink Functions , so it took some time to get used to it; but after getting used to it, it allowed the key aspect of this project, prompt moderation . The challenge of using AI on Chainlink Functions is, especially Image Generation tooks longer than 10 seconds. So image generation had to be handled by the backend server. Accomplishments that I'm proud of I always wanted to participate in chain stories but always lacked the talent. This time while developing this project I had tremendous fun. I believe chain stories, blockchain, Language AI, Image Generation AI and Chainlink Functions are direct fit to each other. What I learned I used many different tools for this project. Learning AI prompts, language AI API, Image Generation API and their prompt engineering was a challenge. As well as using Chainlink Functions to handle the moderation. I believe the project has huge potential on using full version of Chainlink Functions in the future. What's next for StoryChain The project can only go forwards. Of course many aspects of the project depends on the improvements of AI models, especially the speed of image generation; but the project still have some way to go. Such as trying to use better prompts on handling consistence character arts between pages and better story telling prompts. Repos Demo: https://storychain.ai Github (Contracts, Frontend, Backend): https://github.com/cemleme/storyChain Contract: https://mumbai.polygonscan.com/address/0x1865e27501253FD07F87DC2D4d74f0f6ee894617 OpenSea: https://testnets.opensea.io/collection/storychain-9 <div