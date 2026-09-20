---
slug: "zk-2fa-infinito-labs"
url: "https://devpost.com/software/zk-2fa-infinito-labs"
title: "zk 2FA | Infinito Labs"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 658
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "substrate/financial_record"
---

# zk 2FA | Infinito Labs

> Making hot wallets safer to use using zk based two-factor authentication.

[Devpost](https://devpost.com/software/zk-2fa-infinito-labs) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[developer_tools]]
**substrate** [[financial_record]]

**stack** abstraction, account, chainlink, polygon, solidity, testnet, typescript, vrf, zk

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for zk 2fa | infinito labs

## Body

Inspiration The hot Wallets of both Rishabh and I have been compromised, and the hacker stole all our funds. In fact, billions of dollars have been stolen from hot wallets . But people still end up using hot wallets for convenience , which comes at the cost of security. Since hot wallets are always online, it's more convenient to use. To do the same action by cold wallet, users need to find a device (typically a computer) in which to plug their cold wallet, then move the requisite amount of cryptocurrency to a hot wallet, and then perform the action. In addition, while hot wallets are usually free, cold wallets can cost you between $50 and $200. What it does We are enabling users to authenticate transactions with a second layer of security while maintaining privacy. Users have to provide a second factor in the form of a pin generated on google authenticator to validate a transaction. So even if the private keys of the user are compromised, the hacker will not be able to execute any transaction. User flow Setup : Start the setup process by confirming a tx. A secret key is generated with a Merkle tree. Scan the generated QR code using google authenticator. Tx authentication : After the user initiates a tx in the wallet, and if the tx involves a value to be sent. Open the Google Authenticator app to get the 6-digit pin The user is prompted to enter the 6-digit pin and verify How we built it We are enabling these features using a smart contract wallet, ERC 4337 describes a way how we can have account abstraction in the current Ethereum protocol without making changes to the consensus layer. And account abstraction allows us to implement all sorts of arbitrary and custom logic into our wallets compared to what’s currently possible with just a standard private key or seed phrase. Two-factor authentication is done by providing a Zero Knowledge Proof-based two-factor authentication system. The advantage of using ZKP is that we can proof of our identity without revealing the secret information we have (here, secret info is OTP) to the verifier system. We can prove that we know the information, and verification of the proof takes place on the chain. Then, a secret is generated in the front end using ChainLink VRF. This secret is now used to generate two things: The QR code displayed in the front end: This QR code is scanned by the user using his Google Authenticator to generate time-based OTP every thirty seconds. Leaf nodes of a Merkle Tree(MT) which is used to generate the full Merkle tree. MT is a hash function which is used to verify the information stored in leaf nodes in an efficient manner. When OTP is entered in future the Merkle root is calculated in a ZK manner. This root value is now stored in the smart contract wallet and verified along with the proof generated. After this gets verified, the user can make his transaction. Challenges we ran into The Bundler provided by the eth-infitism team was broken, and it was really challenging to set up a local RPC bundler. It took a lot of conversations with people of the ETH Foundation to figure out how it would be working. Various ZK libraries like snarkjs were giving a lot of errors in the frontend. It took a lot of time and extensive research to find how every component would work together. Lack of proper documentation of Account abstraction SDK made it a lot difficult to interact with the abstract ether provider and signer. Accomplishments that we're proud of The earlier version of the project won 2 prizes in ETH-ONLINE 2022 What we learned Account Abstraction, Smart contract wallets, ERC 4337 Importance of security Zero-knowledge proofs What's next for zk 2FA | Infinito Labs We want to build a metamask snap of zk-2fa and launch it for our users. <div