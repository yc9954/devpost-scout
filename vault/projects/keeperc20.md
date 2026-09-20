---
slug: "keeperc20"
url: "https://devpost.com/software/keeperc20"
title: "KeepERC20"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 551
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# KeepERC20

> Keep your ERC20s safe through Chainlink Automation. ERC20s are internally wrapped into KeepERC20s, which support scheduled transfer, recoverable transfer, and expirable approval.

[Devpost](https://devpost.com/software/keeperc20) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**domain** [[finance_payments]]
**substrate** [[financial_record]]

**stack** automation, chainlink, ethers, firebase, hardhat, javascript, polygon, solidity, vue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for keeperc20

## Body

Title Motivation Proposal Contributions Structure Overview Keep your ERC20s safe through KeepERC20, powered by smart contract and Chainlink Automation . Inspiration Truly decentralized finance requires decentralized banks and decentralized wallets. We are already familiar with decentralized, non-custodial wallets such as Metamask. But what about decentralized banks? Unfortunately, the blockchain does not have and should not have a centralized player. Therefore, blockchain users cannot get convenience from the centralized institution, such as scheduled transfer and mis-transferred asset recovery. What it does To provide security and convenience without compromising decentralization, we propose KeepERC20, a distributed bank-and-wallet based on smart contracts and Chainlink Automation. Currently, KeepERC20 offers three novel functions: Scheduled Transfer Recoverable Transfer Expirable Approval We will continuously add more convenient and secure functions. Scheduled Transfer The scheduled transfer is a function that automatically transfers ERC20 tokens after a few blocks. A series of bytes can be transferred together, so the contract call is also possible. It is monitored and managed through the Upkeep of Chainlink Automation. A predefined fee is collected as an ERC20 token when requesting a scheduled transfer. Recoverable Transfer The recoverable transfer can be treated as a kind of insurance because users can use it to prepare for mispayment. When the tokens were sent to an address where the private key didn't exist or sent to the wrong contract, there was no way to recover them before. However, if you use KeepERC20's recoverable transfer, you can get them back completely. Except for some fees. The asset transfer through this function is finalized only when the receiver publishes an unwrap transaction. If tokens are sent to the wrong address so no one can access them, they will automatically return to the sender through Chainlink Automation after the expiration. Expirable Approve ERC20's Approve is often the target of attack. The expirable-approve reduces the possibility of the hack by automatically canceling approval. Since the increase and decrease in ERC20's Allowance is a function that only the token owner can call, a contract wallet is created internally to control it with the KeepERC20 contract and Chainlink automation. How we built it The user can participate in the KeepERC20 system with any ERC20 token. The sender's ERC20 tokens are internally wrapped into KeepERC20 tokens to benefit from various functions through a smart contract and Chainlink Automation. KeepERC20 tokens are internally unwrapped into ERC20 tokens, so the receiver can easily use received tokens for other Dapps. Challenges we ran into Some tasks may be impossible with just simple token wrapping, such as ownership-related function calls. In that case, the KeepERC20 system creates a safe contract wallet internally and provides those functions seamlessly. Accomplishments that we're proud of High quality of contracts and webapps. Beautiful and sophisticated frontend. Online&Onchain non-stop Live Demo: Live Demo Mumbai testnet is used for a concrete example. The faucet for Test ERC20 (TERC20) tokens is available! First, click the "Connect Wallet" button. Then, click the "Faucet" button appearing at the same location. Chainlink Automation KeepERC20-TERC20 Upkeep Register New Upkeep What we learned How to implement Chainlink Automation powered contract. How to register and manage Chainlink Automation Upkeep. What's next for KeepERC20 Fix some minor bugs on contracts and webapp. Deploy KeepERC20 on multiple chains. Develop various convenience and secure-enhancing functions. Find the best fee on scheduled transfer and recoverable transfer. <div