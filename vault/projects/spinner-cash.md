---
slug: "spinner-cash"
url: "https://devpost.com/software/spinner-cash"
title: "Spinner Cash"
hackathon: "Supernova "
organization: "DFINITY Foundation"
winner: true
words: 1207
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "mechanism/structural_withholding"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# Spinner Cash

> Safe guard your financial privacy with zero-knowledge proofs

[Devpost](https://devpost.com/software/spinner-cash) · hackathon [[Supernova]]

## Facets

**mechanism** [[revocation_withdrawal]] [[structural_withholding]]
**user** [[general_public]]
**substrate** [[code_repository]] [[financial_record]]
  <sub>weak: web_dom</sub>

**stack** canister, html, internetcomputer, javascript, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for spinner cash

## Body

Inspiration Privacy has always been on the mind of real crypto punks. We firmly believe that privacy is knowledge, and knowledge is the one thing that everyone can have and no one can take away. While there are existing layer-1 solutions such as Zcash or Monero, they do not have smart contracts. Bringing smart contracts and private transactions together was our initial motivation. In the past few years we have seen many innovations in the zk-SNARK landscape. Layer-2 projects on Ethereum, such as Aztec Network and Tornado Cash, gave us a lot of inspiration and leverage. Spinner is an extension of this evolution onto the latest blockchain technology that is the Internet Computer. With the upcoming threshold ECDSA support, the Internet Computer will be the only platform where we can bring zk-SNARK based private transactions directly to Bitcoin, with no trusted intermediaries or bridges. Everything will be controlled by autonomous smart contracts running on the Internet Computer blockchain. This not only opens up an opportunity to implement private transactions for bitcoin as a "Layer 2" solution, it also means we could facilitate private exchanges between tokens on different chains. All assets can now by managed by the same smart contract on the Internet Computer, without having to deploy separate contracts on different chains that can't talk to each other. What it does Spinner Cash implements a private ledger on which all transactions are 100% private. It does not reveal the sender or receiver of a transaction, nor the amount of tokens being transferred. Therefore, transactions conducted on the private ledger is 100% private. Similar to UTXOs, Spinner's ledger stores private notes instead of account balances or user address. Only a note's owners know the secret and can prove their ownership. To spend a note (for example, sending tokens to another account), a user has to first prove that she is the owner of the input note. The Spinner ledger will verify this proof before approving the transaction. The proof has to show that the amount of input tokens is equal to the output tokens, because otherwise it is not a legit transfer. Thanks to zero-knowledge techniques, the verification of such a proof does not need to see the actual amount. The Spinner ledger only stores the hashes of inputs (notes that are spent) and the outputs (notes that are created). So users can safely transact on the Spinner ledger with full privacy. Of course, for deposits and withdrawals, they still have to go through a public ledger which, depending on the token type, is either the ICP ledger or the Bitcoin network. The public ledgers will only see that tokens are moving in and out of the Spinner's smart contract addresses. These withdrawals cannot be linked to deposits in any meaningful way, making it also resistant to chain data analysis. How we built it Zero knowledge proofs may seem like a secret sauce if one is not familiar with the technique behind them. It has been extensively researched in recent years, and there are prior projects from which we can drew inspirations from. Thanks to high quality tools and libraries that are made available by the open source community around zk-SNARK, it was relatively easy to bootstrap ourselves from the ground. Building on the Internet Computer has many interesting characteristics, one of them is stable memory. We came up with a unique solution of storing binary Merkle Trees efficiently in the stable memory that can grow on demand. This is already open sourced as part of our Rust library . Also, the Internet Computer offers atomicity at per-call level, but not across calls. We have found that implementing transactions across canisters wasn't as hard as we thought. We have a multi-canister architecture, one canister serving each token pool, and each pool can manage its ledger spanning multiple canisters. Challenges we ran into One of the challenge building on the Internet Computer is how to convince people that a project is launched with maximum security and verifiability. Being privacy focused, we understand that without security there is no privacy. Security requires maintenance and upgrade, therefore we must solve the verifiability problem while considering upgrades. After analyzing the design and implementation of the Internet Computer blockchain, we proposed an innovative solution called LaunchTrail and spent some time to work on it as a side project. Essentially we don't want users to trust our claims, we want them to be able to verify and convince themselves that using Spinner Cash is safe. This means not only our source code must be open, but also what is deployed has to match the code, and every upgrade and every configuration ever done must be tracked and fully verifiable. It is correctness by construction. Our users don't have to to trust us because they can go to LaunchTrail and verify everything, not as an afterthought but beforehand. This is much in the same spirit of zk-SNARK: with math and rigor, everything is verifiable even when the actual data is private. Accomplishments that we're proud of We started with a public command line beta in March 2022. In the two months that follows, we rolled out a web UI, a side project, and a major upgrade to V2, supporting fully private transfers. Using Spinner Cash is really simple -- it doesn't require using a wallet or even login. One can just go to https://spinner.cash , launch the app and start transacting. There is no barrier to entry as long as you already know how to send or receive ICPs. It may be too simple to realize there is actual complex math and logic going on behind the scene, safeguarding your financial privacy. But that is the whole point of it, privacy and security don't have to be complex. What we learned Our plan is to first build a robust and secure foundation, starting with private transactions for ICP first, and then for BTC when ICP-BTC integration is ready. Transacting ICP or BTC privately is only the beginning. IC's unique technology also means we can bring these tokens together through the same set of smart contracts! Soon users will be able to trade between tokens securely and privately. This will set us apart from other L2 privacy projects. They are restricted by what their L1s can do, or bridges, which as we all know by now, is terribly insecure. So what we are building is really a protocol, through which token liquidity can flow freely, securely, and privately. What's next for Spinner Cash Support for BTC is well underway, and once ICP/BTC integration lands on the Internet Computer main net, we'll start beta testing. Decentralization has always been our goal as well. We have a small team, and we can't control and run everything. In fact, we don't want to. Our role is to eventually lead the project to a DAO structure, our users are owners and we become a facilitator to the DAO. Next on our roadmap is private swap, allowing users to atomically swap between different private ledgers. A native privacy token call SPNR will be introduced as an intermediary to facilitate private swaps. This is something really exciting and we can't wait to share with our users when it is ready. <div