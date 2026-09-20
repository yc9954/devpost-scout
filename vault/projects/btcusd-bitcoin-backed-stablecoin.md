---
slug: "btcusd-bitcoin-backed-stablecoin"
url: "https://devpost.com/software/btcusd-bitcoin-backed-stablecoin"
title: "BTCUSD: Bitcoin-Backed Stablecoin"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 571
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# BTCUSD: Bitcoin-Backed Stablecoin

> Turn idle Bitcoin into yield-generating stablecoin! Deposit BTC, mint BTCUSD at 150% collateral ratio, earn 8% APY through automated Vesu farming on Starknet's lightning-fast network.

[Devpost](https://devpost.com/software/btcusd-bitcoin-backed-stablecoin) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[agriculture_food]] [[finance_payments]]
**substrate** [[financial_record]]

**stack** atomiq-bridge, braavos-wallet, cairo, expo.io, javascript, react-native, starknet, starknet.js, vesu-protocol

## How they structured the write-up

- 💡 inspiration
- 🎯 what it does
- 🏗️ how we built it
- 🚧 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🚀 what's next for btcusd

## Body

BTCUSD: Bitcoin-Backed Stablecoin 💡 INSPIRATION Bitcoin holders face a fundamental dilemma: keep their Bitcoin and earn zero yield, or sell it for yield-bearing assets and lose Bitcoin exposure. With over $1 trillion in Bitcoin sitting idle, we saw an opportunity to solve this with Starknet's ultra-low fees and Bitcoin's emerging DeFi ecosystem. BTCUSD enables Bitcoin holders to maintain their exposure while earning yield through automated farming on Vesu protocol - turning idle Bitcoin into productive capital. 🎯 WHAT IT DOES BTCUSD is a Bitcoin-collateralized stablecoin that automatically generates yield: Deposit Bitcoin → Atomiq bridge converts to wBTC on Starknet Mint BTCUSD → 66.67% LTV (150% collateral ratio) for safety Earn Yield → Collateral auto-deposited in Vesu for 8% APY Harvest Rewards → 70% to users, 30% to protocol sustainability Key Features: 🔒 Real Bitcoin collateral via Atomiq's trustless bridge 💰 Automatic yield farming on Vesu protocol ⚡ Lightning-fast transactions on Starknet 📱 Mobile-first interface with Braavos integration 🛡️ Overcollateralized design with flash loan liquidations 🏗️ HOW WE BUILT IT Smart Contracts (Cairo) 5 interconnected contracts power the system: BTCUSDToken - ERC-20 stablecoin with vault-only minting controls BTCUSDVault - Core collateralization logic with 150% minimum ratio YieldManager - Vesu integration with custom lending hooks AtomiqAdapter - Bitcoin bridge monitoring and wBTC management VesuHook - Auto-compounding yield strategies and flash loans Mobile App (React Native + Expo) Mobile-optimized interface featuring: Beautiful gradient design with Bitcoin orange branding Braavos wallet integration for Bitcoin support Real-time position monitoring with health indicators One-tap yield harvesting with visual feedback Starknet.js integration for seamless blockchain interaction Technical Architecture Bitcoin → Atomiq Bridge → wBTC → BTCUSD Vault → Vesu Yield ↓ ↓ ↓ ↓ ↓ User BTC → Trustless → Collateral → Stablecoin → 8% APY 🚧 CHALLENGES WE RAN INTO Cairo Version Compatibility - OpenZeppelin contracts had breaking changes between versions. Solved by creating simplified, custom implementations. Mobile Bridge Integration - Connecting Bitcoin wallets to React Native required careful Starknet.js configuration and wallet adapter patterns. Yield Hook Complexity - Integrating with Vesu's lending hooks while maintaining gas efficiency required custom Cairo implementations. Liquidation Safety - Designing flash loan liquidations that protect both users and protocol required careful economic modeling. 🏆 ACCOMPLISHMENTS THAT WE'RE PROUD OF ✅ Complete End-to-End System - From Bitcoin deposit to yield harvesting, fully functional ✅ Advanced Cairo Contracts - 5 interconnected smart contracts with proper security ✅ Mobile-First UX - Beautiful, responsive interface optimized for mobile DeFi ✅ Multi-Protocol Integration - Deep integration with Atomiq, Vesu, and Braavos ✅ Prize Strategy - Designed to win $15,000+ across 6 sponsor tracks ✅ Real Utility - Solves genuine problem for $1T Bitcoin ecosystem 📚 WHAT WE LEARNED Starknet Scaling - Experienced firsthand how ultra-low fees enable complex DeFi operations Bitcoin DeFi - Understood the technical challenges of cross-chain Bitcoin integration Mobile DeFi UX - Learned what it takes to make DeFi accessible to mainstream users Cairo Development - Gained expertise in Cairo smart contract patterns and optimization Protocol Integration - Mastered integrating with multiple DeFi protocols simultaneously 🚀 WHAT'S NEXT FOR BTCUSD Phase 1 (Next 3 months) Mainnet Deployment with security audits Starknet Foundation Grant application Partnership discussions with Atomiq, Vesu, Braavos Phase 2 (6 months) Multi-asset collateral (ETH, STRK support) Advanced yield strategies (multiple Vesu pools) Mobile app on iOS/Android app stores Phase 3 (12 months) Cross-chain expansion to Bitcoin L2s Institutional partnerships for large-scale adoption $100M+ TVL target with governance token launch <div