---
slug: "polyfaucet"
url: "https://devpost.com/software/polyfaucet"
title: "Polyfaucet"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 1172
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Polyfaucet

> Devs need test eth to play around with. We drop NFT art to people who give test eth to testnet faucets.

[Devpost](https://devpost.com/software/polyfaucet) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[general_public]]
**substrate** [[financial_record]] [[video_visual]] [[web_dom]]

**stack** css3, dalle, flask, html5, jinja, python, solidity, tailwind

## How they structured the write-up

- inspiration & background knowledge
- what it does & how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for polyfaucet
- links

## Body

Inspiration & Background Knowledge Testnets drop test matic and it's nice to send it back when you're done playing with it. Developers need test matic to build things. Testnets have faucets that drop these test matic when requested. These need to be mined, and there are very few miners as there is little economic incentive to mine test matic . This means that sybil attacks are easy because it's easier to get consensus. Also, since transaction costs are zero, long-running spam attacks are possible if one has a lot of test matic. This lead to some killjoys abusing testnets. They were hoarding test matic and then performed spamming or sybil attacks. To prevent this, testnets require Proof of Work and mining, and have some form of captcha or other spam filter. This also means that they tend to be low on matic , as there are few miners. The easiest way to help a fellow dev is do donate test matic to the testnet. This will save the dev the work needed for PoW. Now it's turn for us to give back to these donors who have saved us all the PoW work. What it does & How we built it First, we attempted to donate on Ethereum, but gas fees were way to high. Instead of airdropping, we decided to create a whitelist of eligible wallets using Merkle trees. Very cool technique, but unfortunately, wallet holders would not really know that this was available to them. We messaged a few faucet managers and had a positive response, but most of these holders cannot be traced easily. So we were left unsatisfied, because there was not much interaction. Therefore, we decided to airdrop the NFTs on Polygon. The cool thing was that once we've airdropped, people started interacting with them immediately, as you can sea on OpenSea (click link on https://polyfaucet.xyz/ or go directly to https://opensea.io/collection/polyfaucet ) We first comb through mountains of data on Polygon testnets to identify which wallets donate back to testnet faucets. We do a lot of analysis here, such as removing filtering out addresses that are smart contracts or that do not have any activity on Polygon mainnet. Once the analysis is finally done, we encode those addresses into a highly compressed data structure called a merkle tree, and deploy a modern ERC721 using the merkle tree as a fancy whitelist. It’s worth noting that any given address can only mint once, and that these mints are free (excluding gas costs). This is not for profit. The NFTs in the smart contract are AI generated images, using a state of the art diffusion model to create them. This is computationally quite expensive, but the end result is very satisfying. These images are then stored ipfs and pinned with Filecoin, to ensure they’re never lost. They are, truly, decentralized. The last part of the equation is the frontend, the website where all comes together. We let top donors mint cool NFT art with water droplets. To do that, waterdrop does three things: Whitelisting on-chain Gets the list of top 1000 donors to generate a whitelist analysis of gazillion blocks exclude smart contracts (Bonus) publishes leaderboard on our website that anyone can view (flask, tailwind, jinja2) Creates a merkle tree where the rootnote allows to check for eligibility for the mint Generating the NFT art and publishing it to IPFS Runs an AI model to generate thousands of images from text snippets about water drops (Dalle Mega) Minting the NFTs Creates a frontend where unique waterdrop NFT art can be minted by whitelisted wallets Deploying a smart contract that checks wallet against whitelist Challenges we ran into The largest challenges were the gas cost and the blockchain data analysis. Initially, we thought about dropping NFTs to top donors, but gas was prohibitively expensive, so we understood we had three options: deploy on Polygon merkle trees and letting donors mint their NFTs instead of dropping them We decided to go with the first options as it would be a nicer gesture. The blockchain data analysis was difficult because of the ~15GB of data on the testnets and because most of it are not donations. On top of that, most interactions are smart contracts, not wallets, so these had to be filtered out as well. And lastly, we wanted to filter for wallets that also were active on L1, so that was an added complexity. Generating interesting art also turned out to be more challenging than expected. Konrad started off with mathematical, procedurally generated art. The idea was to use variables such as donation size to determine the look and complexity of the artwork. However, it quickly turned out that it the artwork tended to look relatively similar. That's why we decided to use our expertise in AI to leverage it to create an AI-generated NFT collection, because there is much greater variety there. However, it took many many hours of computation. Smaller challenges: Getting comprehensive list of faucets required a surprising amount of manual digging Integrating the entire pipeline (Solidity, Backend, Frontend, AI & Data) was not at all trivial In particular, dealing Solidity versioning and merkle tree proof formats was a PITA smaller frontend issues Accomplishments that we're proud of We’re very proud that we can give back to our wonderful community. We find rewarding merit through retroactive public goods to be a very attractive concept. Testnets are a great way of testing whether someone is a good or bad actor, because they provide no external incentive. You stand nothing to gain or lose from donating or hoarding or attacking a testnet. Rewarding those who donate their test eth back will not tip the scales, but it’s a nice gesture, just like their donation was a nice gesture. We are also proud of the pace of progress. Hugo ran the entire backend ops on his own, and also created the entire gallery of art. Konrad had zero programming skills and understands the basics of frontend now and expanded his stack stack by VSCode, git, tailwind, flask, jinja in just 3 days. What we learned Hugo learnt: Applying data analysis skills to on-chain data The beauty of Merkle trees Optimizing gas costs AI image generation using diffuse models Secure, decentralized permastorage on IPFS/Filecoin how to survive a trip through frontend hel Konrad learnt everything from scratch. His previous experience was only some basic html and CSS ages ago. He learnt: using VSCode the basics of git python flask tailwind Perlin noise, procedurally generated art Together, we learnt about Kanbans, project management, collaborating using git. What's next for Polyfaucet Hopefully we inspire other projects to care about the public good, and incentivize more good actors in the space to appear. Regarding polyfaucet, the address list for for airdops is updateable. Taking another snapshot at a future point in time, or even at regular intervals, is an option. Of course, the fundamentals behind waterdrop can also be applied to many other topics, not just testnet ether donations. Links https://polygonscan.com/address/0x616d197a29e50ebd08a4287b26e47041286f171d https://opensea.io/collection/polyfaucet https://rarible.com/collection/polygon/0x616d197a29e50ebd08a4287b26e47041286f171d <div