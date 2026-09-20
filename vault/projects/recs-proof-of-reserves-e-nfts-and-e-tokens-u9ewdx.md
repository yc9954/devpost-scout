---
slug: "recs-proof-of-reserves-e-nfts-and-e-tokens-u9ewdx"
url: "https://devpost.com/software/recs-proof-of-reserves-e-nfts-and-e-tokens-u9ewdx"
title: "RECs Proof of Reserves / E-NFTs and e-tokens"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 1174
team_size: 6
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# RECs Proof of Reserves / E-NFTs and e-tokens

> IoT data-driven RECs (Clean Energy Certificates) Proof of Reserves 🌳 e-NFTs as RWA "solar bonds" for solar infra fractionalized ownership with e-token billing accruing to NFT per MWh ⚡

[Devpost](https://devpost.com/software/recs-proof-of-reserves-e-nfts-and-e-tokens-u9ewdx) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[climate_energy]] [[developer_tools]] [[finance_payments]] [[legal_justice]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[financial_record]] [[sensor_telemetry]] [[structured_db]]

**stack** amazon-web-services, ethers, iot, java, nextjs, node.js, raspberry-pi, redis, solidity, spaceandtime, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for recs proof of reserves / e-nfts and e-tokens
- references

## Body

Overview REC Proof of Reserves Page Energy Token Page Chainlink node jobs RECs data energy data GIF e-NFT art- "sergey_satoshi_nazarov_" Inspiration DREx is inspired by the concept of energy autarky described by Müller et al. (2011) as a programmatic vision in which energy services used for sustaining local consumption, local production and the export of goods and services can be derived fully from locally renewable energy resources in industrialized countries [1]. By creating a platform that aligns several stakeholders in a decentralized renewable energy supply-and-demand network on top of the rooftops of corporates in emerging markets, DREx advances the concept of energy autarky by having hyperlocal energy production financed by global investors for regional development of developing economies. The full potential of emerging economies is yet to come. Still, one of the largest remaining obstacles towards the clean-energy transition is the perceived risk associated with emerging markets, such as political volatility, creditworthiness and legal uncertainty. Investors, while aware of the economic potential of emerging markets, would rather de-risk their portfolios in the face of these overarching challenges [2]. What it does To address the above problem, we are building a platform that connects solar developers (parties who want to build solar projects), corporates (parties with space to build these solar projects) and investors (parties who have capital to fund these solar projects). We were privileged enough to procure a collaboration with a local operating solar plant in Ecuador, for a Proof-of-Concept (PoC) showcasing that we can (1) build an IoT device capable of tracing renewable solar energy and tokenize it on-chain, as well as create e-NFT bonds, which represents fractionalized ownership of a solar project and pays out dividends in DRX e-tokens - tokens representing energy (in MWh) produced over the lifespan of the solar plant, redeemable at a fixed price. And (2) generate renewable energy certificates (RECs) via Evident, a third-party provider, based on the energy production of said solar plant. We also show that we can tokenize these RECs for potential usage in on-chain markets and use Proof of Reserves (PoR) to maintain that the REC token balance is backed by the amount of RECs held in our Evident account. Creating a financial product with real-time traceability that by combining IoT + Blockchain for clean energy certificats and new-gen financial products, provides transparency to emerging market's investors, insurance against greenwashing critiques, and combats climate change. How we built it In collaboration with a local solar plant owner we connected an IoT device we built to their local solar grid infrastructure in Ecuador. This IoT device sent real-time energy metric reads from energy meter to our database, we used a combination of AWS and a SpacexTime (SxT) data warehouse for data management. In parallel, we also hosted a Chainlink node on our AWS instance to onboard the off-chain IoT and REC data to the Sepolia testnet. As stated, our project can be broken up into two distinct components: (1) the proof-of-reserves for REC tokenization and (2) the tokenization of renewable energy as a trustless settlement layer for solar investors. We note the distinction between tokenization of renewable energy and tokenization of RECs as two different things, which share the same underlying resource. While this resource (renewable solar energy) is used to mint REC tokens and DREX e-tokens, these are two assets used in very different contexts - the former being bought and sold in offset markets like Green Power Hub, and the latter being our personal redemption token, representing investor share of a solar project's energy production output over time. For the proof-of-reserves component of our project, the IoT data was sent via API and on an automated basis to Evident where requests were issued and approved for REC generation. We wrote an external adapter which allowed our oracle node to retrieve the amount of RECs generated from the Evident API, and tied this to a smart contract which would mint and burn corresponding REC tokens based off this amount. For the IoT component of our project, data was sent to a SxT API on AWS, which then stored the IoT data in a data warehouse. Off-chain data and blockchain indexing are managed in the data warehouse for consuming APIs. Endpoints were generated to allow for pulling of this data on-chain via the Chainlink oracle. Prior to any onboarding of energy data on-chain, smart contracts were written and deployed to manage all the business logic, from e-token traceability through e-NFTs to redemption of e-tokens. Challenges we ran into We have a large architecture, sometimes it is difficult to integrate new tech with it. SxT was definitely a challenge for us to integrate, we would have loved to get the energy tokens and raspberry pi connected directly but we ran into 32 and 64 bit incompatibilites, leading us to find a hack-y workaround to this issue by setting up a SxT API on our AWS instance. Accomplishments that we're proud of There's little documentation on PoR since it is quite new. It is fantastic to have fulfilled a working version of it with a real partnership in place. Something that we will definitely keep working on in the coming weeks. We are also very proud to have a working pipeline in place and to have, in essence, proved our concept in the sense that the pipeline is working (albeit suboptimally) as we intended it to. What we learned We need to improve upon basic ethers functionality and start exploring other methodologies. Our transactions are too slow and we need snappy interactions. Maybe it's because we are running on localhost, but there's definitely room for improvement in our frontend. We also learned a lot about the capabilities that SxT can afford us. It is a very real possibility that we may use it in the future. What's next for RECs Proof of Reserves / E-NFTs and e-tokens We want to create energy billing based on the e-token, using our Chainlink oracle to manage energy fees over time for every PPA (Power Purchase Agreement) so that if energy bills change we can provide discounts over market-energy fees. Also, we want to incorporate EIP-4337 account abstraction in order to limit the amount of Metamask interactions and sponsor gas fee's for users while allowing social logins and recoveries. We believe this project has a real-world use-case for blockchain tech and a business model, one which if put into practice can onboard non-Web native users for combating climate change in an smart way. For this we need to 'abstract' away the web3 interactions to a minimum. We also see great potential in bringing RECs on-chain and want to work on building a marketplace for them, as there are already thriving on-chain markets around carbon credits and offsets. References [1] Müller, M. O., Stämpfli, A., Dold, U., & Hammer, T. (2011). Energy autarky: A conceptual framework for sustainable regional development. Energy Policy, 39(10), 5800–5810. https://doi.org/10.1016/j.enpol.2011.04.019 [2] Hanna, D. (2020). The 50 Trillion Dollar Question: closing the emerging markets’ capital gap. Standard Chartered Bank. Retrieved November 24, 2022, from https://www.blackrock.com/corporate/insights/blackrock-investment-institute/financing-the-net-zero-transition#barriers-to-flows <div