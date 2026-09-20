---
slug: "universal-parametric-climate-insurance-utilizing-cbdcs"
url: "https://devpost.com/software/universal-parametric-climate-insurance-utilizing-cbdcs"
title: "Universal parametric climate insurance utilizing CBDCs"
hackathon: "Ripple CBDC Innovate "
organization: "Ripple"
winner: true
words: 903
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/climate_energy"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# Universal parametric climate insurance utilizing CBDCs

> Climate insurance is out of the reach of the majority of the world's population, particularly those in the Global South. We implement an efficient dapp for universal climate insurance using CBDCs.

[Devpost](https://devpost.com/software/universal-parametric-climate-insurance-utilizing-cbdcs) · hackathon [[Ripple CBDC Innovate]]

## Facets

**domain** [[agriculture_food]] [[climate_energy]] [[disaster_emergency]] [[finance_payments]] [[security_privacy]] [[transportation]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[web_dom]]

**stack** hardhat, javascript, python, react, satellite-data, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for universal parametric climate insurance utilizing cbdcs

## Body

UI Inspiration This solution was inspired by the recent heatwaves and floods in various places worldwide, as well as the droughts in parts of Africa. The number of people being affected by climate risks is skyrocketing every year. This is resulting in people losing their livelihoods, homes, and economic lifelines. Traditional insurance is too inefficient and thus expensive for most people, especially in the Global South which is highly vulnerable to climate risks. On the other hand, web3 technology allows for efficient and reliable parametric insurance driven which is fully automated, transparent, and thus affordable. The limitation that holds back web3-based insurance is the need to offramp from crypto to fiat. The utilization of CBDCs in smart contract-driven parametric insurance eliminates this challenge, by enabling the insured to get paid using their local currency in digital form. This highly efficient insurance framework can reduce insurance costs by 40% and can be used to provide universal climate insurance to at-risk communities., The goal is to enable vulnerable communities to better cope with risks, and to recover economically afterward thanks to the insurance payouts. What it does Our solution is made up of 2 components. The first part is the on-chain part of the solution, which is composed of smart contracts that drive the parametric insurance. The smart contracts have the logic that automates premium payments and policy payouts if the risk being insured for happens. The second part is the ecological data oracle, which reports the occurrence of a climate risk to the smart contracts. The oracle gets up to date data from NASA and ESA among other satellite providers. This remote sensing data is ingested by the oracle, analysed to determine real world conditions, and the data is then on-chained and fed to smart contracts. Through the oracle the smart contracts are able to have a window to the real world and reliably know when a climate risk occurs. The oracle deployed to power this solution is provided by Shamba Network, a leading provider of digital monitoring, reporting and verification solutions. The Shamba oracle can report on everything from wildfires, drought, air degradation, crop failure, lack of forage etc Through the data on-chained by the Shamba oracle the parametric insurance solution can be configured to address any type of climate risk. How we built it We developed a set of smart contracts to operate the parametric insurance solution, right from handling the payment of premiums all the way to handling the payouts in case of risk occurrence. This dapp basically automates the various processes that are typically manual in traditional insurance. We deployed these smart contracts on the XRPL EVM sidechain. We also bridged the class-leading Shamba ecological data oracle to the same network. This oracle was set up to report the occurrence of a specific climate risk to the smart contract deployed above. The smart contract would then trigger, completing the insurance workflow automation based on whether the risk occurred or not. The oracle keeps a full record of all the data it has provided on the IPFS system, making the reporting transparent and auditable. At the end of the day the insured would either get funds sent to their crypto wallet or not, all determined by a data driven dapp. Traditionally the crypto funds would have had to be off-ramped to fiat currency using crypto exchanges like Binance. However with the use of CBDCs in the insurance solution, which correspond to the national currencies where the solution is deployed, there is no longer a need for the extra task of off-ramping. The payouts from the insurance solution are made in CBDCs and so directly usable in economic activities by the insured. What makes the idea of parametric insurance driven by CBDCs on Ripple powerful, is that it is so cheap to create different insurance products. Any climate risk can be insured for any amount, no matter how little. The cost effectiveness of the automated system means it can be used to build a universal climate insurance scheme. Challenges we ran into The RPC URL provided for the XRPL EVM sidechain caused syncing issues for our Chainlink-based oracle. Basically the network node the URL was pointing to was falling out of sync with the oracle node. The XRP support team on Discord provided us with another XRPL EVM RPC URL to test, which also ran into the same issue. The support team promised to look into the issue with their RPC URLs and revert. Accomplishments that we're proud of Developing a proof of concept for how a universal climate insurance solution could be deployed on XRPL and tap into CBDCs to cross that last mile usually handled by off-ramping solutions. We show how CBDCs are particularly well suited to driving such climate adaptation solutions byremoving current bottlenecks with web3 based parametric insurance (off-ramping). What we learned We learned more about CBDCs and how they can be used in solutions that address emergencies. We think this might be a top use of web3 and CBDCs particularly in the Global South which is hard hit by climate change. What's next for Universal parametric climate insurance utilizing CBDCs We would like to release an open protocol for parametric insurance and develop a nice UI to make the user experience better. What we have is a diamond in the rough and if funded we could polish it and deploy a world-class dapp with massive impact. <div