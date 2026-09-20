---
slug: "ascendio-wallet"
url: "https://devpost.com/software/ascendio-wallet"
title: "Ascendio Wallet"
hackathon: "Building Privacy in Web3 - Powered by Partisia's MPC"
organization: "Partisia Blockchain Foundation"
winner: true
words: 238
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
---

# Ascendio Wallet

> Username-password and smart contract based wallet. Say goodbye to traditional seed phrases!

[Devpost](https://devpost.com/software/ascendio-wallet) · hackathon [[Building Privacy in Web3 - Powered by Partisia-s MPC]]

## Facets

**substrate** [[financial_record]]

**stack** partisia

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for ascendio wallet

## Body

Inspiration Traditional wallets require to store private keys and seed phrases. This can be very inconvenient and zillions of dollars are lost due to private key loss. Moreover, traditional wallets do not allow great control over funds, which was the reason of coining the term 'Account abstraction'. What it does Ascendio Wallet is a username password and smart contract based wallet allowing greater control over user funds and advanced features such as email recovery, freeze wallet, etc. User can choose a username and a password to create a wallet, and thereafter, the password is stored in the zk state. Whenver a user wants to send some tokens to another wallet, he just has to do a password verification to initiate the transaction. If password is correct, transaction will be executed. User also gives their recovery email, on which a secret code is sent. The secret code is also stored in zk state, so user puts the recovery code and new password, and the code is verified in zk, and password is updated. Wallet freeze means that nobody will be able to access wallet funds for a freeze period, this feature is also allowed. How we built it We used Partisia blockchain for its privacy features. Challenges we ran into Coding in rust was a challenge, but in the end everything worked out. What's next for Ascendio Wallet Even more advanced features like monthly limit, fingerprint verification, etc. <div