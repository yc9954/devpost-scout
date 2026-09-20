---
slug: "posttoearn-automated-reward-deployment-with-chainlink"
url: "https://devpost.com/software/posttoearn-automated-reward-deployment-with-chainlink"
title: "postmint - refLINK"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 1248
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# postmint - refLINK

> Revolutionize your affiliate marketing with refLINK: trust-minimized conversion tracking for smart contracts, powered by Chainlink Functions.

[Devpost](https://devpost.com/software/posttoearn-automated-reward-deployment-with-chainlink) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]] [[general_public]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]]

**stack** express.js, mongodb, node.js, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for postmint - reflink

## Body

refToEarn Campaign Details Campaign Dashboard Leaderboard with referral volume RefToEarn landing page Inspiration Firmly convinced of the premise that most future economic and non-economic transactions will benefit from the trust-minimized, automated, and disintermediated properties of smart contracts, we're striving to advance this transition. Despite its potential, many web2 users remain hesitant to try web3 products due to a knowledge gap about their usage and advantages over centralized alternatives. We at postmint view high-quality content as a vital element in onboarding the next billion users to the realm of trustless applications through education. Our initial product, PostToEarn, allows web3 marketers to boost awareness and engagement by providing an infrastructure that effectively coordinates community content creators to generate and disseminate high-quality content on Twitter. Now, with the introduction of refLINK, we are enriching our product suite by incorporating conversion tracking. refLINK presents a robust method to gauge the effectiveness of educational content by tracking the smart contract transactions it prompts. The affiliate marketing industry is large and growing, with estimates predicting it to reach $8.2 billion by 2022 in the U.S. alone. Despite its size and relevance, the industry faces significant challenges, including trust issues between parties, difficulty in tracking and attributing sales, and discrepancies in payment systems. Our refLINK product is designed to address these challenges. As firm believers in Chainlink's vision that decentralized smart contracts require decentralized data input, we've designed refLINK with Chainlink functions. This results in a truly trust-minimized experience for the affiliate industry, offering a solution to existing issues and leading the revolution in affiliate marketing. What it does The final goal of postmint's refLINK is to allow the incentivization of any smart contract transactions. In the initial implementation constructed during the hackathon, we enabled the tracking of transactions on Uniswap's exchange contract for a defined trading pair. Campaign creation : Whitelisted projects can deploy a refLINK campaign on the postmint web app and tied to a reward pool. This pool holds the incentive tokens to be paid out for successful referral conversions. Link Creation : Eligible affiliates, termed as publishers, can participate in the campaign and create a referral link tied to their 0x address. Referral Mapping : A publisher disseminates an informative blog post that, for example, analyses the whitepaper and tokenomics of campaign projects, and includes a refLINK to the trading pair at the end. An informed reader who clicks the link gets redirected to a landing page offering information on the campaign and referrer. The referral signs in, providing her 0x address to postmint, which facilitates mapping the relationship between the referrer and referral, and is redirected to the Uniswap landing page. Conversion tracking : The referral may choose to execute a swap transaction on the Uniswap contract. Transactions are monitored, by Chainlink's DON based on the logic specified on the function. Score calculation: Happening on the Function using on-chain data such as the volume of a transaction and the referral bonus in % specified by the campaign creator. Root deployment : The Merkle Root hash gets deployed from the Chainlink DON to the Campaign Smart Contract of the refLINK campaign. The referrer can then claim their reward. How we built it refLINK - refToEarn is a new product (improvement) completely built during the hackathon, but based on the existing postmint protocol. Existing elements: postmint web app (campaign creation form, dashboard, details template) postmint campaign smart contract (holding rewards and allowing for merkle root claiming) Elements built during this hackathon: Affiliate campaign details (create referral link) Link creation, wallet mapping Chainlink functions for monitoring Uniswap tx, interacting with postmint BE, scoring transaction, uploading merkle root for reward distribution) Consumer contract, interface for Chainlink functions We built refLINK using Chainlink Functions, smart contract interfaces, and postmint-based link tracking. The Postmint system tracks referrers and their referrals. This data is provided to the Chainlink Functions in order to calculate score based on their behaviour on-chain. Using the Functions we decentralise the scoring process and allow permissionless execution on a protocol level. The Functions return back the calculated Merkle root and the Interface contract uploads the root to the appointed Campaign Smart Contract The Postmint system is a system designed to track referrers and their referrals. It collects and records data about the individuals who refer others to a particular campaign or affiliate program. This data is crucial for calculating a score based on the referrers' behavior on the blockchain. To facilitate the scoring process, the Postmint system utilizes Chainlink Functions. Chainlink is a decentralized oracle network that connects smart contracts with real-world data and off-chain computation. The Functions provided by Chainlink allow for the decentralized execution of the scoring process on the protocol level, ensuring permissionless access and transparency. The Consumer contract, which acts as an intermediary between the Postmint system and the Campaign Smart Contract, receives the calculated Merkle root from the Chainlink Functions and is responsible for uploading the Merkle root to the appointed Campaign Smart Contract. The Campaign Smart Contract, which represents the affiliate campaign being run on the blockchain, receives and stores the Merkle root uploaded by the Interface contract. This ensures that the calculated score and the associated data are securely stored on the blockchain, providing an immutable record of the referrers' performance. By utilizing the Postmint system, Chainlink Functions, and the Campaign Smart Contract, the scoring process is decentralized and transparent. It removes the need for centralized authorities or intermediaries to calculate and store scores, enabling trustless interactions and promoting fairness within referral-based campaigns or programs. Challenges we ran into One of the primary challenges we faced was library restrictions, specifically the inability to import libraries into functions. Ideally we would want the Chainlink Functions to be able to include crypto libraries such that they can generate the Merkle root themselves. Limited Functionality: The inability to import libraries into Chainlink Functions can limit the available functionality for performing complex cryptographic operations or other advanced computations. This constraint might require developers to find alternative approaches or workarounds to achieve the desired functionality within the limited scope of the available functions. Increased Complexity: Without the ability to import libraries, developers might need to implement custom algorithms or cryptographic functions from scratch within the Chainlink Functions. This can increase the complexity of the codebase and its size which is valuable for the request. To overcome these challenges, alternative approaches were considered, such as precomputing certain cryptographic operations outside the Chainlink Functions and passing the results as inputs. This was the case for generating the Merkle root. Accomplishments that we're proud of We are immensely proud that our postmint community marketing tournaments have proven to be a highly effective new channel for web3 marketeers and communities. Our first campaigns achieved up to 700k impressions within only 7 days and a CPMs 2.30 USD, which is remarkable achievement for a User Generated Content campaign. Further, are delighted to provide established web3 pioneers like ShapeShift a tool that leverages their community to create content around their value-aligned web3 product. What we learned How to build a trust minimized scoring and root uploading system for postmint with Chainlink functions. What's next for postmint - refLINK We plan to expand the refLINK product to serve a broad range of smart contract transactions. These include, but are not limited to, buying a smart contract-based insurance policy like Etherisc, purchasing goods and services in the metaverse and websites from providers like Dispatch and Boson, securing open and permissionless networks via staking, and interacting with DeFi applications. <div