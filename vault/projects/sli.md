---
slug: "sli"
url: "https://devpost.com/software/sli"
title: "SLI"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 1354
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# SLI

> Protocol offers slashing insurance for Ethereum stakers. Uses Aave to fund payouts so deposits are refundable to stakers. Chainlink Oracles and AWS used to make beaconchain information available.

[Devpost](https://devpost.com/software/sli) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[revocation_withdrawal]] [[simulation_digital_twin]]
**domain** [[finance_payments]] [[security_privacy]]
**substrate** [[financial_record]] [[structured_db]]

**stack** amazon-web-services, chainlink, ipfs, react, solidity, truffle

## How they structured the write-up

- inspiration
- what it does
- slieth
- math
- malicious actors
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sli

## Body

Inspiration Validators on the Ethereum network can face penalties for certain actions, such as double signing attestations or proposals. Accidental slashing can occur due to technical issues or human error. Slashing insurance can help validators protect themselves financially against such accidental slashing incidents. Ideally, validators who maintain a proper setup and do not engage in malicious behavior should not have to be concerned about facing slashing penalties. However, in practice, a notable number of honest validators have experienced slashing incidents (outnumbering those who intentionally engage in malicious activities). This can be attributed to various factors, including human error, software bugs, and the effectiveness and security of backup systems. The slashing of well-intentioned validators, highlights the need for continuous vigilance and thorough preparations to ensure the security of staked assets. Slashing insurance allows validators to mitigate the financial risks associated with slashing. It is our hope that by providing insurance coverage for slashing, validators may feel more confident and secure in participating in the network. This increased participation can enhance the overall security and decentralization of the Ethereum network by encouraging more validators to stake their assets. What it does SLI leverages the power of decentralized finance (DeFi) to allow validators to protect themselves from the losses associated with slashing penalties at no cost to themselves. To qualify for insurance, validators deposit ETH into the SLI PremiumGenerator Contracts, which, in turn, deposit the ETH into the Aave lending protocol. The Aave lending protocol generates a passive rate of interest on the deposited assets by lending them out in the form of collateralized loans. The interest earned is used to cover losses for any slashing penalties for members. When validators choose to withdraw their staked ETH from the network, they can terminate their insurance benefit by withdrawing their deposit. The validator's deposit is returned in full. sliETH To build the reserve and fund initial payments the protocol introduces a tokenized derivative representing a share of the SLI claims fund called sliETH. Deposits in the insurance contract, combined with premium deposits, generate interest from Aave. This interest serves two main purposes. First, it covers slashing insurance claims, which are infrequent and average penalties of 1-2 ETH, but can be higher depending on network conditions (around 250 slashing events since December 2020). Second, any surplus interest earned beyond the insurance claim requirements is accrued to sliETH holders. This surplus interest acts as a value accrual mechanism, increasing the value of sliETH tokens and benefiting those who hold them. The surplus interest serves as a mechanism for sliETH holders to participate in the positive performance of the underlying protocol. Math Does all this even work? Now for some math (sorry), The population of validators grew linearly from 21,000 to 600,000 from December 2020 to June 2023. Slashing has occurred 250 times over that time period. What are the odds of slashing happening to one specific validator in the population over that time. To calculate the odds of the event happening to one specific validator in the population over the given time period, we can use the following formula: Odds = Number of events / Total population over the time period To calculate the total population over the time period, we can use the average population: Average population = (Initial population + Final population) / 2 Then, we can calculate the odds: Odds = Number of events / Average population In our case, the average population is 310,500 and the number of slashing events is 250. Odds = 0.000805 = 0.0805% The expected value (EV) is calculated by multiplying the probability of the event by its associated value. In this scenario, the value associated with the event is a 1-2 ETH loss. EV = Odds * Value of the event EV = 0.000805 * -2 ETH = -0.00161 ETH This indicates that, on average, you can expect to payout approximately 0.00161 ETH per validator over the given time period due to slashing. However, it's important to note that validator premium deposits will also be earning interest from Aave and contributing it back to the protocol. The APY on Aave's ETH/WETH pool fluctuates due to market demand but has a floor of approximately 1% (yielding much more at times) aavescan . Let's assume a premium deposit of 1 ETH earning at 1% APY. This would yield 0.01 ETH per validator per year. Over the course of the 2.5 years (December 2020 to June 2023) each validator would theoretically yield ~0.025 ETH. Given the discrepancy in protocol earnings versus payout per validator, the protocol should be sustainable from a funding perspective. Please note this is a rough estimation. This calculation assumes that the event occurrence is evenly distributed among the population and that there are no other influencing factors. Malicious Actors Slashing is designed to discourage malicious or incorrect behavior by validators. Therefore, it is imperative that any insurance mechanism include punitive measures for such actors. When a covered validator initiates a claim, they undergo a waiting period of two weeks (or one day for testnets). During this time, the multisig has the authority to pause and reject any claim if it is determined that the validator has engaged in malicious activities. In the case of a denied claim, the validator not only loses their ability to claim losses but also forfeits the reimbursement of their premium deposit. *It should be noted that the majority of slashing incidents on the beacon-chain have resulted from human errors and faulty backup systems. How we built it This project is part of the Chainlink 2023 Spring Hackathon. We deployed a Proof of Concept on the Matic Mumbai network. Our project uses AWS to host the API and Chainlink Functions to make the data available to our contracts. The app uses Create-React-App and Truffle as a development environment for testing and deployment tasks. Due to the availability of testnet tokens and Aave test contracts we opted to build on Mumbai Matic. In order to closely emulate the Ethereum network, the contracts transfer MATIC (native token) and interact with the Aave MATIC/WMATIC lending pool. We set up a simulated API that feeds validator information to the oracle, simulates slashing, and allows us to add and remove validators from the set. This server is set up on AWS at => https://flask-servicecors.rfqbhr834qlno.us-east-2.cs.amazonlightsail.com/ Sample API response 50001 . *Please be aware that intermittent failures may occur when attempting to withdraw MATIC (native token) from the Aave MATIC/WMATIC lending pools testnet contracts on the Aave testnet. These issues are related to the nature of testnets and liquidity constraints. This would not occur in production. Challenges we ran into It is difficult to obtain testnet tokens on any network. We built on Mumbai-Matic because this was the most accessible way to get the amount of test tokens we needed. Time was also a challenge. It was a lot to build and put together in a short period of time. Accomplishments that we're proud of We are proud of the hard work and hours we put into the project. It is a unique use case and we are proud of that as well. What we learned Previously we have not worked with AWS. We learned a significant amount by working with docker and deploying the server API. What's next for SLI Improve front end UI Look deeper into contracts for edge cases / vulnerabilities / gas optimization We also need to explore front running with providing insurance to the claims fund. A bonding period or some other feature may be needed to prevent front running. Explore sliETH token holders being members of a DAO that has various governance rights over the protocol (such as control over the multisig, power to deploy protocol controlled value outside of Aave lending, security, etc.) The withdrawal address associated with an Ethereum validator cannot be changed once set. Our contracts actually rely on this fact to function properly. However, this creates a circumstance where validators will be reticent to sign transactions with their withdrawal address. Thus, we would like to implement a feature where the validator can sign a validity proof offline showing ownership of said address. <div