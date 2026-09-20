---
slug: "aa3-wallet"
url: "https://devpost.com/software/aa3-wallet"
title: "AA3 Wallet"
hackathon: "Fantom Hackathon Q2 2023"
organization: "Fantom Foundation"
winner: true
words: 294
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/deterministic_policy"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "substrate/financial_record"
---

# AA3 Wallet

> World's first Account Abstraction wallet on Fantom

[Devpost](https://devpost.com/software/aa3-wallet) · hackathon [[Fantom Hackathon Q2 2023]]

## Facets

**mechanism** [[cross_origin_web]] [[deterministic_policy]] [[simulation_digital_twin]]
**domain** [[developer_tools]]
**substrate** [[financial_record]]

**stack** amazon-web-services, covalent, erc-4337, solidity, svelte, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for aa3 wallet

## Body

Inspiration On 1-Mar-2023, Ethereum Foundation announced the launch of account abstraction on Ethereum at WalletCon 2023. They deployed a feature known as “account abstraction”, the new standard ERC-4337 standard. That was the beginning Era of Smart Accounts, I think. What it does AA3 Wallet is the first-ever Chrome extension wallet for account abstraction feature support Fantom Network, built on top of @aa3/smart-contract-sdk - an infrastructure to simplify Account Abstraction development. Features Self-custodial wallet, the private key is constructed by Torus decentralized network. Seamless onboarding experience for users by login with social like Google, Facebook... Create wallets at addresses that can be deterministically calculated. Send a batch of transactions. Integrate with multiple swap platforms: Uniswap, SushiSwap, SpookySwap, SpiritSwap. Light/Dark mode. How we built it The Chrome extension is built with SvelteJS, picocss, and @aa3/smart-contract-sdk Entry Point, Paymaster contracts follows the official ERC-4337 contracts developed by eth-infinitism/account-abstraction Singer account - behind wallet smart account contract - is controlled by Web3Auth - self-custodial Wallet-as-a-service infrastructure. Utilizing Web3 data service Covalent to get historical balances, and prices and interact with DEXs/AMMs Using AWS EC2 to deploy Bundler replayer server which was developed by etherspot/skandha and Covalent proxy server. Challenges we ran into Almost bundlers are required debug_traceCall RPC API to simulate operations, Fantom nodes are run with go-opera which does not support debug_traceCall . Covalent is not compatible with Chrome extension, I have to build a simple proxy to serve data. What we learned Deeply understanding of account abstraction concept, especially smart account ERC-4337. Learned Svelte a lot - an open-source frontend javascript framework -simple, less code, build super fast. What's next for AA3 Wallet Improve UI/EX Support more EVM-based chains Gasless / Sponsored transactions Gas Fee Token Flexibility FIAT On/Off-ramping Social Recovery Session keys for games <div