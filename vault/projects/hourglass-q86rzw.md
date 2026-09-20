---
slug: "hourglass-q86rzw"
url: "https://devpost.com/software/hourglass-q86rzw"
title: "HourGlass- Financial derivatives to stratify Time Preference"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 551
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/scientific_research"
  - "substrate/financial_record"
---

# HourGlass- Financial derivatives to stratify Time Preference

> HourGlass produces financial derivatives that allows speculators to stratify their preference for time. It is built on top of Buttonwood's Mooncake App and the Ampleforth Protocol.

[Devpost](https://devpost.com/software/hourglass-q86rzw) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

  <sub>weak: simulation_digital_twin</sub>
**domain** [[developer_tools]] [[education]] [[scientific_research]]
**substrate** [[financial_record]]

**stack** amazon-web-services, chainlink, ethers, hardhat, javascript, materialui, mooncake, nextjs, react, solidity, uniswap, web3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hourglass

## Body

dApp Page dApp mobile Page Home Page Exchange Rate Simulation Tool GitBooks Documentation Inspiration We were very inspired by the vision for the future of DeFi and E-Fi (Elastic Finance) from both the Ampleforth (AMPL) team and the Prometheus Research Labs (PRL) team. Ampleforth's ability to act as a cross chain building block got our creative juices flowing with ideas for a wide number of financial derivatives - but we decided on one to move forward with. What it does HourGlass is a collateralized borrowing platform built on top of the collateralized borrowing platform Mooncake, which is built on top of the risk-tranching protocol ButtonTranche. HourGlass lets users borrow USDT, using their cryptocurrency holdings as collateral, at a fixed borrowing rate with no liquidation. In fact, HourGlass lets users borrow more USDT than on Mooncake. HourGlass achieves this as follows: HourGlass produces two assets that change value over time: A-Prime, that earns a fixed interest over time as well as a variable interest over time, Z-Prime, that pays a fixed interest over time to A-Prime. How we built it We built the front end with React which talks directly to the ETH network and our contracts. No additional API's were created. Challenges we ran into Our two biggest challenges were: Debugging Solidity problems with our contracts after reverted transactions. We found you really need to understand your contracts to debug them properly because there isn't going to be an existing stack-overflow question for a custom contract you're developing Revising our economics so that they made sense for our end users Accomplishments that we're proud of Having a functioning dApp on Testnet with a slick front-end is something we're very proud of. We're also proud of learning how to integrate with a few different technologies (Ampleforth, Chainlink Keepers, and Mooncake). We were at pretty surprised with what we were able to complete. For total strangers to come together across the globe and rock out this project, it's pretty impressive and we are very proud of ourselves. Some of us were going to bed as others were just waking up. We literally worked as a team 24/7 on this. We are very proud of just trying our best and getting as far as we did. What we learned What didn't we learn ha! Seriously though- we put so many hours into this project and we learned so many things over that time its hard to know where to start. When we started none of us had experience developing on ETH or using web3 and solidity, but we learned them all in and out over the last few weeks. For the first few days went spent a lot of time in the school of hard knocks, but we came out of it stronger and even more eager to continue developing. We also learned a ton about economic incentives - which is a topic that continues to fascinate us. Finally, we learned a lot more about how Mooncake and Ampleforth work under the hood. We hope to continue working with them both going forward to help build the future of E-Fi (Elastic Finance). What's next for HourGlass We've been discussing several HIPs (HourGlass Improvement Proposals) before we launch on Mainnet. More on that Soon TM . We're also going to MARZ. See ya there. <div