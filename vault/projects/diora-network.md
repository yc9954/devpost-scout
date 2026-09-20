---
slug: "diora-network"
url: "https://devpost.com/software/diora-network"
title: "Diora Network"
hackathon: "Polkadot Hackathon: North America Edition"
organization: "AngelHack"
winner: true
words: 596
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/developer"
  - "substrate/financial_record"
---

# Diora Network

> Diora Network is a incentivized smart contract parachain, utilizing advanced PoSM with Double Validation & Randomization for security guarantees.

[Devpost](https://devpost.com/software/diora-network) · hackathon [[Polkadot Hackathon- North America Edition]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[finance_payments]] [[transportation]]
**user** [[developer]]
**substrate** [[financial_record]]
  <sub>weak: web_dom</sub>

**stack** api, polkadot.js, react-native, rust, solidity, substrate, web3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for diora network
- moving forward
- things to note
- diora devnet

## Body

Website Info Documentation Basic Block Explorer Tx page Testnet Faucet Custom Substrate UI On-Chain Governance Metamask Fork Defiscan DioraDAO Inspiration Diora Network is a incentivized smart contract parachain The main goal of Diora Network is to foster an array of diverse and sustainable cross-chain applications by empowering and rewarding developers that build on the network with baked in incentives and rewards. More specifically, we are constructing an efficient and fully decentralized consensus protocol. We strive to create a financial system that is accessible to anyone with an internet connection. We believe in a world where value flows freely, regardless of one’s geographic location. We believe our blockchain finance platform will not only unlock opportunities for blockchain companies, but also for traditional financial institutions building bridges to the new digital economy. Diora relies on a system of 150 Masternodes with Proof of Stake Masternode (PoSM) consensus that can support low transaction fees and fast transaction confirmation times. Security, stability and chain finality are guaranteed via novel techniques such as double validation, staking via smart-contracts and true randomization processes. What it does Diora is built with Substrate which natively supports EVM, WASM and a multi-layer sharding scaling solution if needed. Baked into the network itself, Diora rewards developers based on the value and impact of their dapp rather than their close association or connections to capital. Unlike existing versions of older layer 1s, where tokens are mostly concentrated in the hands of the first few early participants, Diora is designed to be shared across all contributors, users and stakeholders. Diora’s native token is not just a fee and staking token. Rather, it will be the one the first tokens on an EVM that drives governance outcomes for the EVM. But it also serves as a vehicle to determine future economic outcomes that align the three main actors (Developers, Users, and Validators). How we built it Diora Runtime Frame cumulus-pallet-parachain-system cumulus-pallet-xcm cumulus-pallet-dmp-queue parachain-info: nimbus-primitives: pallet-author-inherent: pallet-author-slot-filter: pallet-balances pallet-collective: pallet-democracy: pallet-randomness-collective-flip pallet-session: pallet-treasury: pallet-timestamp: pallet-transaction-payment pallet-ethereum-chain-id: pallet-evm: pallet-ethereum: pallet-dynamic-fee: pallet-evm-precompile-simple: fc-db: fc-rpc: pallet-parachain-staking pallet-dapp-staking orml-xcm-support: orml-xtokens: pallet-xcm: Challenges we ran into After stage 1, We moved onto upgrading our chain into a parachain, since we are using the Nimbus consensus framework upgrade for diora, we had to completely rebuild our blockchain which cost us some valuable time. Accomplishments that we're proud of A working EVM-Compatible PoS Parachain on Rococo testnet Incentivised Governance mechanism Learning about substrate and rust Networking with the community Dex, Wallets, Faucet What we learned Substrate dependencies can be nightmare when upgrading to the latest version and the polkadot community has been very helpful at every sage of the development process What's next for Diora Network Moving forward We will be showcasing some more information about our overall concept and plans of the Diora Network. After we believe diora is stable enough, we will start onboarding users onto our chain and growing our community & social presence. Things to note We had a little trouble finding which category we should enter Diora in, since our chain covers 4/5 category's. After some short discussion we decided that "DAO" would be the best fit. From our incentivised on-chain governance mechanism, decentralized masternode election system & how we are replacing the traditional core foundation with a web 3 development dao, Diora is designed at every stage to be one big DAO. Diora Devnet Specifications Chain id: 201 RPC Endpoint: https://testnet.diora.network WebSocket Endpoint: https://devnet.diora.network Consensus: DPoS (not PoSM enbaled) Block finality: >95% Consensus nodes: privately run by DioraDAO Smart contract creation fee: gas price 450 Gwei, gas limit >= 1000000 <div