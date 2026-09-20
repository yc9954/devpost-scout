---
slug: "bitlend-ws5c3u"
url: "https://devpost.com/software/bitlend-ws5c3u"
title: "BitLend"
hackathon: "Bitcoin 2025 Official Hackathon"
organization: "Bitcoin++"
winner: true
words: 670
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# BitLend

> The first transparent Bitcoin-backed lending protocol on exSat Network.

[Devpost](https://devpost.com/software/bitlend-ws5c3u) · hackathon [[Bitcoin 2025 Official Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]]
**substrate** [[financial_record]]

**stack** exsat, rebar-data

## How they structured the write-up

- project overview
- 🔧 technical innovations
- 📋 components
- 🏆 hackathon submission

## Body

landing page XBTC Bridge BitLend: Trustless BTC Lending Protocol on exSat The first transparent Bitcoin-backed lending protocol on exSat Network. Leverage Bitcoin UTXOs for verifiable collateral and borrow stablecoins with complete transparency. 🔑 Key Features Bridge BTC to XBTC: Seamlessly move assets between Bitcoin and exSat Network Collateralized Lending: Use your XBTC as collateral to borrow stablecoins UTXO-Based Proof of Reserves: Verify collateral directly using Bitcoin's UTXO data Liquidation Protection: MEV-protected liquidations using Rebar Shield Market Analytics: Real-time Bitcoin analytics powered by Rebar Data Project Overview BitLend is a permissionless lending protocol built on exSat Network that allows Bitcoin holders to collateralize their BTC to borrow stablecoins or XSAT tokens. The platform leverages exSat's UTXO data synchronization and EVM compatibility to create a seamless, trustless lending experience with transparent proof of reserves. Smart Contracts BitLendBridge.sol : Integrates with exSat's bridge for BTC to XBTC conversion BitLendVault.sol : Manages loan positions, collateral, and borrowing BitLendPriceOracle.sol : Provides price feeds with Rebar Data integration BitLendLiquidator.sol : Handles liquidations with MEV protection via Rebar Shield BitLendProofOfReserves.sol : Verifies collateral using exSat's UTXO data 🔧 Technical Innovations UTXO-Based Proof of Reserves BitLend implements a transparent proof of reserves system using exSat's on-chain UTXO data. This allows users to: Verify their BTC collateral is backed 1:1 with actual Bitcoin Track UTXO confirmations for enhanced security Prove solvency of the lending platform at any time Our system connects directly to exSat's UTXO Management Contract to access real-time Bitcoin data for verification. Rebar Data Integration We leverage Rebar Data for enhanced market insights and security: MEV Protection : Submit liquidation transactions through Rebar Shield's private mempool Market Analytics : Display real-time Bitcoin network statistics Liquidation Risk Monitoring : Alert users when their positions are at risk of liquidation Mempool Analysis : Optimize transaction fees based on current network conditions 📋 Components Smart Contracts BitLendBridge.sol : Integrates with exSat's bridge for BTC to XBTC conversion BitLendVault.sol : Manages loan positions, collateral, and borrowing BitLendPriceOracle.sol : Provides price feeds with Rebar Data integration BitLendLiquidator.sol : Handles liquidations with MEV protection via Rebar Shield BitLendProofOfReserves.sol : Verifies collateral using exSat's UTXO data Frontend Dashboard : Displays positions, health factors, and available actions BridgeModal : Interface for BTC to XBTC conversion with UTXO verification LoanManagement : Components for deposit, borrow, repay, and withdraw actions RebarAnalytics : Shows market data and liquidation risks from Rebar ProofOfReserves : Visual verification of collateral using UTXO data Architecture Overview BitLend leverages exSat Network's unique hybrid consensus mechanism and Bitcoin UTXO indexing capabilities to create a truly transparent and trustless Bitcoin lending protocol. The architecture is designed with four main layers: 🟠 Bitcoin Ecosystem Layer Real-time Bitcoin Data : Direct connection to Bitcoin network for live transaction and UTXO monitoring Mempool Analysis : Integration with Bitcoin mempool for liquidation risk assessment Block Verification : Continuous validation of Bitcoin block data through exSat's synchronizers 🔷 exSat Network Infrastructure Hybrid Consensus : Combines Bitcoin's PoW security with exSat's PoS efficiency UTXO Management : On-chain indexing of Bitcoin UTXOs for transparency Cross-chain Bridge : Secure, decentralized bridge for BTC ↔ XBTC conversion Validator Network : Dual validation system (BTC validators + XSAT validators) 💰 BitLend Protocol Layer Position Management : Sophisticated collateral and loan tracking via BitLendVault Price Oracle Integration : Multi-source price feeds including Rebar Data for accuracy MEV-Protected Liquidations : Rebar Shield integration prevents front-running Proof of Reserves : Real-time UTXO verification for complete transparency So I have already created a ProofofReserve contract that in future would utilise the exsat query on evm side. This custom oracle would: Run as an off-chain service that listens for verification requests from the EVM contract Query the exSat native (EOS) layer for UTXO data using the eos contract as you said above. then Submit the verification results back to the EVM contract 🏆 Hackathon Submission This project is a submission for the Bitcoin Hackathon 2025, targeting the following challenge tracks: Best use of exSat - $10,000 in Bitcoin prize Best use of Rebar Data - $7,000 in Bitcoin prize <div