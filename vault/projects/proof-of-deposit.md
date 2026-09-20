---
slug: "proof-of-deposit"
url: "https://devpost.com/software/proof-of-deposit"
title: "Proof-of-Deposit: A Risk-Free Rate on Stablecoins"
hackathon: "Celo's Make Crypto Mobile Hackathon"
organization: "Celo"
winner: true
words: 1062
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Proof-of-Deposit: A Risk-Free Rate on Stablecoins

> What if block rewards can be paid on stablecoins?* amplify demand for Celo and stablecoins* creates a risk-free rate (application for monetary policy / CBDCs)* taps into largest userbase

[Devpost](https://devpost.com/software/proof-of-deposit) · hackathon [[Celo-s Make Crypto Mobile Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
  <sub>weak: civic_government</sub>
**substrate** [[geospatial]] [[web_dom]]
  <sub>weak: financial_record</sub>

**stack** latex, python, react, solidity

## How they structured the write-up

- smart contracts ( located here )
- webapp ( located here )
- analysis ( located here )
- mainnet deployment
- cbdc

## Body

How Proof-of-Deposit works Amplified demand for CELO and stablecoins UI UI What is Proof-of-Deposit? Proof-of-Deposit is a game-changing innovation that gives L1 blockchains with built-in stablecoin mechanisms a competitive advantage that is unavailable to other blockchains. The core idea behind Proof-of-Deposit is simple but profound: What if block rewards can be paid on stablecoins? (e.g. cUSD and cEUR) The significance of this lies in the fact that block rewards comprimise minted CELO and fees from the entire on-chain economy! This will create a significant market for stablecoins (if not the biggest one by far!). Proof-of-Deposit achieves this by allowing the "staking" of, not one, but multiple tokens. One of those tokens must be CELO whose value is strongly coupled to the network (to serve as strong Sybil-defence), but the other tokens can be stablecoins! When block rewards are distributed, it creates in-effect a "risk-free" rate on stablecoins. Benefits of Proof-of-Deposit Proof-of-Deposit brings significant benefits that complements Celo's philosophy of providing accessible, mobile-first payments in a token that maintains stable purchasing power: Tapping into the biggest and most important userbase: those that cannot or do not want take risk with their money such as regulated custodian, banks and risk-averse individuals. These users, by increasing the liquidity of the stablecoins, help to stablise the peg as the liquidity serves as a buffer when sell-offs occur. The reason that these users will hold cUSD, cEUR, etc is due to the APY offered by Proof-of-Deposit (users will deposit if they deem APY to be attractive, and withdraw if they deem it too low). Amplifying demand for CELO and stablecoins Unlike lending protocols, Proof-of-Deposit gives a "risk-free" rate where there is no risk of losing your principal. Unlike swap protocols, Proof-of-Deposit pays rewards from newly minted CELO (as opposed to a separate token) and from a transaction fees paid by the entire on-chain economy. As users who deposit stablecoins earn a passive income paid in CELO, this creates a positive feedback loop: i. CELO price increase -> APY on stablecoin increases ii. Demand for stablecoin increases (to deposit in order to receive the APY) -> CELO price increases (due to CELO being used as collateral for stablecoin mechanism) A new tool for central banks: monetary policy with configurable discretion By providing a risk-free rate in a decentralised setting, Proof-of-Deposit enables central banks to choose to limit their discretion over monetary policy. Remarkably, (and perhaps counterintuitively) choosing to limit discretion in this way can greatly strengthen the de facto independence of a central bank. Benefits to strong independence include: i. Enhanced credibility (particularly valuable for e.g. emerging economies, as it may permit borrowing in a currency that they issue (on affordable terms). ii. Incomplete independence has been shown to cause a down trend in interest rates, which leads to rates eventually hitting zero, whereupon the effectiveness of monetary policy is severely impaired ( see our paper summary for detail ). Overview of Implemented Functionality Smart Contracts ( located here ) For this hackathon, we sought to showcase how Proof-of-Deposit could be integrated with Celo. To achieve this, we isolated and made modifications to the following Celo Governance Smart Contracts : LockedGold.sol (our abstract version is called LockedToken.sol ) i. Modified lock and withdraw to be compatible with any ERC20 token (e.g. cUSD, and cEUR) ii. Modified the constructor to LockedToken to be instantiated with a particular ERC20 token and other initial parameters iii. Removed unnecessary dependencies for our proof of concept Election.sol i. Modified the constructor to allow Election.sol to be instantiated with multiple LockedTokens (e.g. our proof-of-concept uses LockedCGLD , LockedCUSD and LockedCEUR ) along with other initial parameters. ii. Extended most class variables to be mappings where the key is a LockedToken address (such as LockedCGLD , LockedCUSD , etc) iii. Modified almost all functions to include a address token parameter, where a specific LockedToken address needs to be provided. (e.g. function vote(address token, address group, uint256 value, ...) needs to define which LockedToken is being used to vote) iv. Implemented functions to introduce "normalised votes" (e.g. getGroupTotalVotesNormalised(address token, address group) ), where a normalised vote is the fraction of votes from a particular LockedToken for a validator. v. Implemented functions to introduce "influence" (e.g. getGroupInfluenceFromTotalVotes(address group) ), where influence is calculated as the min over all normalised votes from different LockedTokens for a validator. vi. Modified distributeEpochRewards so that we can showcase how epoch rewards are distributed amongst multiple LockTokens . vii. Removed unnecessary dependencies for our proof of concept WebApp ( located here ) We used plock.fi as a "SDK" to showcase a possible UI to interact with Proof-of-Deposit : Proof-of-Deposit overview page that shows all of a user's Lockable tokens, and their respective stats (e.g. average APY): Lockable token management page that allows a user to Lock/Unlock/Withdraw their tokens, Vote with Locked Tokens, as well as see validator group stats (e.g. APY): Analysis ( located here ) We formally analysed the increased demand for CELO and stablecoins that Proof-of-Deposit You can view a forecast of the marketcap calculated by our model on our live WebApp . Next Steps For this hackathon we have implemented a proof of concept version to showcase our tech, and have provided preliminary analysis. Next steps are divided between mainnet deployment and CBDC routes: Mainnet Deployment Towards the goal of getting this live: Stringent analysis on the economic and security implications of our tech (e.g. contracting https://chaoslabs.xyz/ ) Thorough investigation of breaking changes in the wider ecosystem that can come from modifying Election.sol and LockedGold.sol (e.g. other smart contracts, wallets, celo-tools , etc). Collaborate with cLabs and Mysten Labs to test/architect/develop our tech with a clear phase-in plan. (Unclear if modification/integration of existing governance smart contracts is best way forward) Seek to modularise the "risk-free" rate tech such that it can be used for simulations (e.g. economic analysis) as well as potentially packaging it into a marketable product. CBDC Continue our collaboration with economists at IMF, ESM and BoE Advisory Group to produce papers on how blockchains allow for monetary policy with configurable discretion. Collaborate with CBDC team at cLabs Lots of presentations and talks... (its the long game with Central Banks) URLs Our Github Live WebApp Video Demonstration Presentation Slides Our Whitepaper - A Market Determined Risk Free Rate Our Analysis - A MarketCap Model for Proof-of-Deposit Our Summary on CBDCs - Monetary Policy with Configurable Discretion <div