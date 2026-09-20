---
slug: "haze-al0nsz"
url: "https://devpost.com/software/haze-al0nsz"
title: "Hazed"
hackathon: "Fantom Hackathon Q1 2023"
organization: "Fantom Foundation"
winner: true
words: 1105
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "mechanism/structural_withholding"
  - "domain/legal_justice"
  - "user/general_public"
  - "user/government_staff"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Hazed

> Anonymous and simple transfers on Fantom. Non-custodial solution using stealth addresses to hide your real account.

[Devpost](https://devpost.com/software/haze-al0nsz) · hackathon [[Fantom Hackathon Q1 2023]]

## Facets

**mechanism** [[revocation_withdrawal]] [[structural_withholding]]
**domain** [[legal_justice]]
**user** [[general_public]] [[government_staff]]
**substrate** [[financial_record]] [[web_dom]]

**stack** hardhat, react, solidity, typescript, wagmi

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what's next for hazed

## Body

Inspiration I have always been interested in anonymity in blockchains. There are many approaches to achieving it, from privacy-centered blockchains like Monero to methods implemented in commonly-used networks, such as the infamous Tornado Cash based on anonymity sets or zero-knowledge proofs solutions. While these approaches offer almost perfect privacy for both sides of a transaction, they require the use of specific tools or cost notably more than a direct transfer. The gap between costly and complex solutions and non-private transfers is still open. A few weeks ago, Vitalik published an article called "An incomplete guide to stealth addresses" . After thoroughly reading it, I realized that it completed the big picture in my head about a solution that would be simple enough, but still offer anonymous transactions, at least for the receiver. Thus, I decided to build a user-friendly tool using stealth addresses employing this idea. For its implementation, I selected Fantom as the initial network because of its fast, inexpensive transactions and Solidity support. That's also how I came up with the name Hazed, like a phantom in a haze. What it does Hazed.io uses an elliptic curve key pair with its public part as a Hazed ID (base58-encoded), which one can think of as a meta-address not bound to any real blockchain address. Once a user generates a Hazed ID (they can have as many IDs as they want), they should store its key for further use and they are ready to receive funds sharing only the Hazed ID without any additional blockchain-related information. The sender uses a specific Hazed ID and calculates a stealth address. It can't be predicted, and every transfer uses a new stealth address. The stealth address is built from the public key of the receiver (their Hazed ID) and the ephemeral private key from the sender, which is generated on-demand. Once ready, the sender sends a transaction to the Registry contract with their ephemeral public key. Funds are transferred to the precalculated stealth address in the same transaction. The receiver is continuously watching for new keys published to the Registry contract. Once a new key is received, they try to build a private key (and a corresponding stealth address) from it with their private part of the Hazed ID. If it results in an address with some funds, it should be the stealth address where the funds were sent. Then, the receiver can get the private key of the stealth address and use it in any wallet software or transfer funds from it further right from the website, i.e., to another counterparty, exchange, or cold wallet. If the receiver doesn't withdraw funds to their personal address, there's no way to see a connection between them and the sender. Available stealth addresses can even be considered somewhat like Bitcoin UTXOs, and perhaps one day, there will be a wallet able to use them in this way. How I built it To begin, I set up a standard Hardhat project and added some essential methods to the Registry contract. I intentionally didn't make the contract upgradeable to enhance its credibility since we don't have any on-chain governance at the moment. If an upgrade becomes necessary, I'll deploy a new version and provide the necessary client-side support. Then, I began building the UI/UX with React and Typescript. To ensure the project was user-friendly for both power and non-power users, I ordered a simple yet sleek design. Originally, I used ether.js to handle all blockchain interactions, but I soon discovered the perfect wagmi library, which made things much more convenient and simplified the process. There was also a lot of math involved with elliptic curves, but all the calculations were performed flawlessly and rather quickly with the elliptic library. Both elliptic and wagmi have Typescript typings, making working with them a pleasure. Challenges I ran into For the most part, working on the project went smoothly. However, the main challenge I faced was figuring out the best user experience I could offer, and I believe the current implementation is indeed user-friendly. Another challenge was finding a way to sign and send withdrawal transactions. These transactions should not be signed by the connected user wallet, so the common approach of using Metamask or Wallet Connect to sign the transaction was not suitable. I ended up creating a custom-built transaction broadcasted via public RPC urls. As it's the only type of transaction using public RPC, it doesn't create any notable load and won't lead to user bans. The solution works well. Accomplishments that I'm proud of I'm really proud of the whole project. It just works as intended and offers a pleasant user experience. I have many ideas for further development. What's next for Hazed Currently, Hazed.io only offers native coin transfers (FTM), since withdrawal transactions from the stealth address can cover the transfer fee with funds from the same stealth address and don't require FTMs from outside. However, adding support for tokens and NFTs would make this tool much more useful, so I will research it further. I'm thinking of implementing relayer nodes (which could be as simple as a Python script + smart contract) that would mint and sell notes as tokens (or NFTs) in exchange for covering user fees on transfers in the future. This way, the user still doesn't need to reveal their identity but uses their note tokens to ask a relayer to cover their fees and pay for the actual transaction. There can even be competition between different relayers, forcing them to keep transfer fees reasonable. Thanks to Fantom's compatibility with EVM, expanding Hazed to other EVM chains is quite simple. Once this is done, I'll research ways to perform cross-chain transactions, potentially using a third-party bridge. Additionally, there is a plenty of room for improvement in gas optimization in the Registry contract and its interaction with the receiving side. All of this will eventually be addressed. While Hazed doesn't use any kind of mixing or hiding transfers, it can still be questioned by regulators, so obtaining a legal opinion on this matter would be useful. Nevertheless, since the Registry is on the blockchain and all the code is available on Github, even if the website is shut down for some reason, the funds will remain available. Lastly, further UX improvements are planned, such as notifications when funds are received on a new controlled stealth address, or a mobile application (although the website works fine on mobile devices). The sky is the limit! Thank you for reading this lengthy post. Privacy is essential for every human being, so let's make anonymous transactions more convenient for everyday use. <div