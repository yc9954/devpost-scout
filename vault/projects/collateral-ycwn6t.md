---
slug: "collateral-ycwn6t"
url: "https://devpost.com/software/collateral-ycwn6t"
title: "Collateral"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 833
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# Collateral

> Collateral is a platform that allows users to post their NFTs as collateral for Ether-backed loans. It connects borrowers and lenders to create fair lending terms.

[Devpost](https://devpost.com/software/collateral-ycwn6t) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[finance_payments]]
**substrate** [[financial_record]]

**stack** chainlink, daisyui, dedication, ethereum, etherscan, hardhat, javascript, love, nft, node.js, nuxt, opensea, solidity, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for collateral
- contacts

## Body

Inspiration Over the past two years, the NFT market has grown exponentially, breaking into the mainstream and influencing millions. This fast-evolving space has gained widespread popularity among not only art lovers and those involved in crypto, but common folk and celebrities too. NFTs are a unique and innovative notion that may only continue to grow. However, as many NFT owners may concur, many NFTs today function as nothing more than collectibles. They’re cool to show off, especially on twitter, but offer little to no utility compared to their towering sale prices. We recognized this problem, and in the past few weeks, sought out to build something to unlock value within every NFT. What it does Collateral provides an easy way to match potential borrowers with lenders. Borrowers can choose an NFT to use as collateral, along with the terms of their proposed loan (the amount they'll receive, the duration of the loan, and the amount they'll repay). Upon proposing a loan, borrowers' NFT collaterals are locked in the contract and can be retrieved by borrowers by either retracting their loan (before a lender accepts the terms) or by paying off their accepted loan in full. Lenders see proposed loans and can accept them based on their terms. Should the duration of the loan expire without the borrower paying the lender back in full (the borrower defaults), the lender has the option to liquidate the loan, at which point the borrower's collateral is transferred to the wallet of the lender. Based on the floor price of the NFT (if it exists), loan pricing may also be restricted for fairer loaning and allow for early liquidation. How we built it We built the smart contracts with Solidity and the Hardhat framework. We used Nuxt.js/Vue.js, and Tailwind CSS to create a visually pleasing web interface for users to interact with the contracts. To connect the two, we utilized ethers.js To mint, find, and access NFTs/NFT info, we used OpenSea/OpenSea API We used Chainlink’s contract library and oracles to request off-chain data, which allows us to access the floor price of NFTs (if they exist) to restrict loan pricing and allow early liquidation. Challenges we ran into Frontend web development: Though we are all proficient in blockchain development, none of us were especially experienced in frontend development. Within a month, we had to teach ourselves the Vue framework and Tailwind CSS to be able to build an elegant frontend for our DApp. For us, time was a huge limitation. The tight window of the hackathon meant we had to work more hours than usual. Additionally, we learned to prioritize, as the few weeks did not lend enough time for us to make every part of our project as perfect as we would like before the deadline. Our team was distributed, and had to work remotely from different time zones. Sometimes, it was difficult to find meeting times that worked for everyone—which further worsened our time crunch. Near the end of the project, the OpenSea testnet API was unresponsive for quite a while, which halted our progress with running our code for the night. Unable to work on that part of the code base, our team had to regroup and redefine goals for the session. Fortunately, we were still able to make great progress! Accomplishments that we're proud of We began with just an observation, followed by a roughly formulated idea. We never expected to be able to bring it to reality in a mere few weeks—but it turns out that all it took was passion, efficient teamwork, and lots of overtime. We’re very grateful for our team members, as well as Chainlink for this amazing experience and competition. What we learned As mentioned above, we learned the entire Vue.js framework within this month to build our web interface. We learned about the inner workings of NFTs and their standards, along with how to initiate and track NFT transactions with the OpenSea API.. We learned how to use Chainlink contract libraries and oracles to fetch off-chain data, as well as how to integrate with the OpenSea API. As team members, we learned how to work together as optimally as possible – prioritizing team members’ productivity is just as important as prioritizing your own. When a team member needed assistance, we always hurry to offer assistance. What's next for Collateral Implementation of "soulbound" (non-transferrable) NFTs that will be minted to the wallets of those borrowers who have defaulted on their loans. This will act as a credit score of sorts and follow the users around the blockchain to indicate that they may be untrustworthy. Mint nfts to the lenders as proofs of the loans. Along with the soulbound NFTs mentioned above, we are able give rating to the loans (AAA … D) and build a secondary market for active loans. Going beyond a hackathon project, we plan to continue working on Collateral, and turn it into a VC-backed startup. Contacts Alan Wu: lunw1024@gmail.com Tiger Che: tigerche207@gmail.com jomahe: https://twitter.com/0xJomahe <div