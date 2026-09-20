---
slug: "calamus-finance-money-streaming-on-tron"
url: "https://devpost.com/software/calamus-finance-money-streaming-on-tron"
title: "Calamus Finance - Money Streaming on TRON"
hackathon: "TRON Grand Hackathon 2022"
organization: "TRON DAO"
winner: true
words: 923
team_size: 5
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Calamus Finance - Money Streaming on TRON

> Your decentralized crypto streaming platform - Automate real-time salary, startup vesting or any transactions with enhanced security and transparency

[Devpost](https://devpost.com/software/calamus-finance-money-streaming-on-tron) · hackathon [[TRON Grand Hackathon 2022]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]]
**user** [[developer]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]]

**stack** chartjs, javascript, moment.js, mongodb, nextjs, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for calamus finance - money streaming on tron

## Body

Dashboard Stream setting Outgoing stream - Cancel or Tranfer anytime Use Case Diagram Smart Contract Use Map Inspiration Currently, many platforms support payments with fiat money, which could be used for investing, payroll, purchases, etc. Nevertheless, these platforms encounter several shortcomings, including: Most platforms do not allow periodic automation of payments. Instead, users must manually transfer the money when the work is done. Workers always stand a risk of wage theft. Labour hirers might risk low-quality work, for example, if payment is made in advance. Workers have to wait for a specific date to receive/use the money, usually every month or after the contract ends. Most platforms do not support payment with tokens. Thus, to solve these issues, we have made use of blockchain and (the application of) tokens to create the very first crypto streaming protocol on TRON. At Calamus Finance, we aim to facilitate the process of constant payments and token vesting transparently and securely. We choose TRON because it is a comprehensive platform with TVM (highly compatible with EVM); thus, we can save time for R&D and focus more on building features instead. What it does Calamus Finance is a decentralized crypto streaming protocol that allows people to send/receive payments on any time basis and vest tokens automatically. Calamus Finance supports all TRC-10, TRC-20 tokens and the native token - TRX. Main functions: Payroll : Pay your employees by the second quickly. Company will have complete control over frequency, liquidity amount and duration. Cancellation is possible at any time by the payer and/or payee. Token Vesting : Reward your team, advisors and investors with tokens automatically without any fear of foul-play Multisig wallet (coming soon): Wallet is owned by many people, and transactions are only made under agreements from multiple owners. Users can: Connect their Tronlink wallet with the app Choose TRX or any TRC-10, TRC-20 tokens. Configure a payment frequency: per second, minute, hour, day, week, month or year. Most traditional companies would pay their employees by week or month. Set start and end time of payments Configure advanced settings like cancellation or stream transferring. Set total payment amount Fill in the recipient's address and extra information like email address, contract title, etc. Cancel stream at any time if mutual consensus is not met. Transfer the stream to a new recipient’s address. Set an initial release amount at cliff date (for startup vesting). Data from these features are validated at DApp and Smart Contract, hence minimizing human risk and improving security. How we built it We divided our journey into 3 phases: Build Smart Contracts, Build DApp and Deploy & Debug. To build Smart Contracts, we use: Solidity version 0.8.0 Open Zeppelin Smart Contracts Use map: Our tech stack: NextJS 12 and React 17 Shopify Polaris: a React UI component suitable for building admin apps. Tronweb Javascript library and Tronlink Javascript Object to interact with TronLink wallet and perform account-related actions. ChartJS to build reports on the dashboard. Moment JS to process stream time on the Frontend and contribute to data reporting. Mongo Atlas DB to store Recipient’s extra information because storing unnecessary information on-chain will increase fee when creating streams and sometimes exceed the logic limit of a Solidity Smart Contract. Tron Scan public API to collect user’s token balance on registered wallet address. Diadata (Oracle) public API with coinmarketcap as the data source to collect information about TRX to USD price, thus providing an insightful display for users. To deploy Smart Contracts on Testnet, we use TronBox, TronIDE and TronScan to deploy and debug Smart Contracts. Challenges we ran into Although the tech stack used inTRON is relatively basic for a Web3 developer, we encountered multiple technical problems which take quite some time to solve: Issue 1: Some OpenZeppelin's contracts had errors when compiled with TronBox. Thus, we had to customize the contracts by OpenZeppelin. Issue 2: TronBox cannot deploy contracts. We chose TronIDE and Tronscan to replace TronBox in deploying. Issue 3: Interacting with the wallet on Frontend. Some examples and sample codes do not run correctly, are hard to set up and use obsolete, incompatible libraries. Luckily, the team can still connect to the wallet by customizing these examples based on TronWeb's document. Issue 4: Smart Contracts failure. Some Smart Contracts, which can deploy on Ethereum Testnet, can fail on TVM due to various reasons, some of which relate to data type or using an external library. Accomplishments that we're proud of Build a Money Streaming protocol on a new platform and support all tokens available on TronLink. Overcome technical challenges to accomplish goals. Develop technical functions so that users on Tron Network can pay, receive and vest tokens easily. Gain a lot of in-depth knowledge about blockchain and finance. What we learned Throughout the journey, we have learned to Build a complete dApp on TRON. Deploy a Smart Contract and the concept of it on TRON Blockchain. Use the TronWeb library to interact with Wallets and Smart Contracts. Understand the Crypto Payment model & usage on a Defi app. General knowledge of libraries and APIs in various languages. Technical knowledge on how to solve existing problems of fiat payment systems. What's next for Calamus Finance - Money Streaming on TRON Go live on TRON mainnet. Multisig Wallet Integrate Invoice-related features when creating steam. Improve admin tools and interface to become a professional payment platform. Develop API for Developers to easily interact with our data. Muti-chain Integrate with more wallets, opening more choices for users. Issue tokens and set up tokenomics for Calamus Finance <div