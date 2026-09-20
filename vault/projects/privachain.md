---
slug: "privachain"
url: "https://devpost.com/software/privachain"
title: "Privachain"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 472
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# Privachain

> A zk-powered privacy parachain (Circom-R1CS-On chain verifier) to ensure transaction confidentiality.

[Devpost](https://devpost.com/software/privachain) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[developer_tools]]
**substrate** [[code_repository]] [[financial_record]]

**stack** circom, go, javascript, polkadot-sdk, rust, snarkjs

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for privachain

## Body

Inspiration The blockchain gives power back to the people and that freedom has changed the way the world works. However, while my team and I were trying to solve some transaction issues with local products, we realized the system has to be a lot simpler and privacy was a major factor. Can I make a transaction to my immediate neighbor without having to tell everyone. Can we basically just exchange value just with the paper system? What it does Privachain is our first attempt at a paper based blockchain system. It uses zk snarks as the decentralized system still needs to keep a ledger of transactions else no record keeping, double spending and others. However, it doesn't expose information like sender, recipient, value. Users simply shield their notes (create commitments on chain), can "burn" and transfer commitments and unshield later. How we built it Our system is built to use proper structures like merkle trees to ensure the chain isn't bloated by commitments. A typical 1 billion commitments calculated will keep an onchain 100gb of data. Instead, the chain stores the root around 32bytes. An indexer can then keep a proper tree to help the wallet (light clients) generate proofs for proofs, pun intended. We have carefully designed constraints to ensure commitments are true and transactions are indeed valid. Encrypted notes help broadcast transaction across wallets so recipients can decrypt using what I like to call double edged private key encryption which is just an extension of the Diffie-Hellman encryption. Challenges we ran into Building more knowledge on zero knowledge to be able to understand the maths behind it. Designing and verifying the constraints took a long while. Loading the verification key bin on chain. We still have a few components to resolve like the indexer, compiling the pallet and running a full wallet-wallet test. However, we've been testing each component as we build and we're sure we have a runnable system. Obviously, we'll still look extensively at loopholes. Accomplishments that we're proud of We've been able to learn a lot on zk proofs and how it truly works. Took reading books, scheming through chains like zcash (zebra repo), and other blogs. We've built a functional privacy pallet that can be reused. Even contributed to the polkadot sdk while learning and realizing how flexible the system's design is. Building core systems in a short time. What we learned Zk-proofs, circom circuits, merkle tree indexing, pallet development and integration. What's next for Privachain As mentioned earlier, this is just the first attempt. The next thing is to fully develop this solution, check round for more use cases and continue with other exciting features we have planned. Even to extend the way transactions work to a truly offline with more advance commitment schemes with optimistic commitment acceptance. Then we're looking at private interoperability. <div