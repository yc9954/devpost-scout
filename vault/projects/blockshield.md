---
slug: "blockshield"
url: "https://devpost.com/software/blockshield"
title: "Blockshield"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 1000
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/finance_payments"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# Blockshield

> We protect your RWA tokens. Blockshield assures your investments, guaranteeing the face value of your RWA crypto assets from default risk on its debt obligations. Invest without any worries.

[Devpost](https://devpost.com/software/blockshield) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[finance_payments]]
**substrate** [[code_repository]] [[financial_record]]

**stack** alchemyapi, ccip, chainlink, chainlink-automation, docker, ethers.js, functions, hardhat, javascript, mongodb, nextjs, react, solidity, springboot

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for blockshield
- deployed contracts

## Body

BlockShield, Insurance for RWA tokens Project Summary BlockShield Platform Project architecture Blockshield Workflow BlockShield is Blockchain agnostic, thanks to Chainlink Our team Inspiration In the rapidly evolving world of blockchain and cryptocurrency, we believe the potential for growth and innovation is limitless. However, the volatility and risk of scams have created a barrier to mass adoption, hindering the widespread acceptance of cryptoassets. At Blockshield, we're committed to bridging this gap by harnessing the power of insurance and banking expertise to create innovative solutions that reduce these risks. Our goal is to empower individuals and institutions to confidently invest in the crypto-asset market, knowing that their assets are protected and have the proper transparency assured. Our project, Blockshield, is designed to provide peace of mind for RWA crypto-asset holders, safeguarding their investments against the credit risk related to default events on its debt obligations, and ensuring the integrity of the market. By leveraging blockchain technology and our expertise in insurance and banking, we want to create a safer and more reliable environment for the growth of the RWA cryptoasset ecosystem. What it does The platform's landing page is the list of RWA tokens already evaluated by BlockShield and for which we offer insurance cover against the risk of default. We believe that tokenization platforms will proactively seek us out, as having this quality seal from BlockShield will improve the initial sales and liquidity of RWA tokens. On the platform, the user connects their digital wallet, where we identify the assets it contains that are insured, and the cost of the fee required for coverage. By activating the buy button, the customer signs a transaction in their digital wallet to authorize the exchange of the original RWA token for an insured RWA token issued by BlockShield, plus a fee payment transaction in USDT. Once the transaction is finalized, the platform identifies that the client has the secured RWA token and lists the transactions the client has. We issue the insured RWA token via an ERC-20 contract adapted for insurance operation (the coverage amount, issuance limited to the supply token of the original RWA token, sending the balance to the Reserves Vault, multichain interactions, and with Chainlink services). This method of insurance coverage, by issuing a new token mirroring the original RWA token, aims to maintain the customer's freedom to sell their RWA token whenever they want, and the new owner will maintain the insurance coverage. The smart contract Vault was created to collect the fees raised to build up a fund. This fund will be used to pay off any defaults on the original RWA tokens. The smart contracts that generate the insured RWA are programmed to monitor the original tokens using Chainlink functions and Automation, and when they identify an event of default, they request payment from the Vault smart contract. We also issued the project token (BSD), with its value backed by the reserve accumulated in the Vault. The purpose of this token is to share risks with investors interested in receiving a share of the income from the insurance sold. To this end, we have created a BSD/USDT liquidity pool. Expected cycle of RWA token insurance: Customer purchases insurance on the platform --> Chainlink functions monitor the original RWA token on the tokenizer's platform --> Chainlink Automation triggers the smart contract of the insured RWA on the maturity date. Case 1 - If the real-world debt has been paid, terminates the smart contract of the insured RWA and appropriates the fee as revenue. Case 2 - Otherwise, the insured RWA smart contract calculates the total indemnities, withdraws the amount from the Vault contract, transfers it to the insured RWA token holders, and closes the insured RWA smart contract. How we built it The web frontend is developed using Next.JS and ethers.js, bootstrapped with create-next-app; The insurance smart contracts are written in Solidity using HardHat, with Openzeppelin for standard contracts; Chainlink contracts, including Data Feed, Functions, Automation, and CCIP, are integrated; The backend of the insurance operation was created with Bootify.io, Spring Boot for Transactions through APIs, and MongoDB to store metadata. Challenges we ran into Chainlink's products were initially complex, leading to numerous errors. Eventually, we managed to get them working; An insurance operation is naturally complex, but we have succeeded in developing a functional and viable prototype, running entirely on the blockchain; It was also challenging to integrate various smart contracts cohesively; Despite the diverse team, none of us is strong in frontend. Even so, we managed to put together a functional and intuitive platform. Accomplishments that we're proud of The idea itself, which we believe is something new and viable, was generated jointly, a real team effort. A great start for a strong team of founders; Teamwork also has its challenges, a lot of pressure, different personalities, and yet we still manage to maintain the atmosphere of friendship and unity; We learned how to develop a functional and intuitive frontend; It was another opportunity to put into practice the knowledge acquired in bootcamps. We're proud to have used this knowledge to collaborate with the new tokenized economy. Finally, we created the project without using any artificial intelligence tools, even to create the pitch video. This was a great victory for us, being able to present something we have so much faith in without it being in our native language What we learned We gained significant knowledge of Chainlink, especially CCIP, UX, and advanced programming in smart contracts; We have improved our business development capacity, showing that the proposed product is viable and profitable; We improved our team collaboration and optimization skills. What's next for Blockshield Improvements to the developed set of smart contracts before its mainnet launch and seek smart contract audit support; Enhancements in user experience are planned; Roadmapping BlockShield between tokenization platforms. Deployed Contracts Ethereum Sepolia name address VAULT 0xcc9201f2Ad1Ae21388c8966D84cBE37f38dfC457 RWA FIT08 0xEec13d981FE3d0CA258F46070360b4BC1B0FBb38 RWA NAG134 0xF3b179356fd1d8377E70CCf9930645Ee473E0669 RWA FOCUS26 0x912b805acDF64e21f617A4a7d900248995F40E8C RWA RFDCS32 0xF0f6fa10458677934b5a81900060b65405f91076 Polygon Amoy name address blockshield.FOCUS26 0xD5b5f8062cD1B88F6b41BF252B14976fD07fbb2F blockshield.FIT08 0x3fd55F3419fa09780eaD6E1Cf8B9916d8DbDc021 blockshield.RFDCS32 0x1EA3bb98302017B94fDbC4b6C5Fc263bBd3955f8 blockshield.NAG134 0x550a2dE08180a5a8613226a8746A5a63a108d7B6 <div