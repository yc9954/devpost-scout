---
slug: "foxic"
url: "https://devpost.com/software/foxic"
title: "FoxIC"
hackathon: "Supernova "
organization: "DFINITY Foundation"
winner: true
words: 585
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
---

# FoxIC

> A tool allowing MetaMask users to enter IC ecosystem

[Devpost](https://devpost.com/software/foxic) · hackathon [[Supernova]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** love, metamask, rust, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for foxic
- instructions on how to use foxic

## Body

Cover Inspiration We love and hate MetaMask. While some MetaMask problems such as its security issues have been long known, it is still very popular with a tremendous user base . There is Internet Identity on IC, as well as a few wallets. However, none of them get close to a fraction of the popularity of this little fox on the browser toolbar. Therefore we are building FoxIC, a tool that will allow users to use their most familiar wallet MetaMask to interact with Internet Computer. What it does FoxIC allows users to use MetaMask to sign IC messages and interact/control a wallet canister to send ICP transactions, and display ICP balance inside MetaMask, as well as transaction history. IC messages are signed inside MetaMask, not within a WebApp's frontend page. So it's more secure and the same usage pattern that users are already familiar with. The user's private/public key pair i.e. identity, stored in MetaMask, is used directly for the signing function, just like any extension crypto wallet. The identity then can be used to interact with canisters, and even control the user's own canisters. With this MetaMask/IC signing integration, building a frontend IC wallet app becomes straightforward, allowing MetaMask users to own and control their canister wallets. How we built it We use MetaMask Flask , a MetaMask developer distribution, to build FoxIC. We developed a separate package called ICSnap which is used to interact with the MetaMask Flask environment and provide APIs to the adapter. We have an adapter installed in the FoxIC frontend and combine it with a wrapped identity, which is used to interact with canisters. We have a factory canister to provide registry service and install wallet canister for users. We have a standard wallet canister for every user, and set users to be controllers/owners. We use HTTP response and heartbeat features. Challenges we ran into Learning MetaMask Flask development took some effort. To confirm window pop-ups each time when signing, we have to find a way to authorize once and allow signing without pop-ups. Building canisters is fun, but managing them needs to be careful. Users would expect MetaMask to display and refresh ICP balance. Many blockchain projects have some configuration methods, but it doesn't work for IC. So we do not use RPC calls. Accomplishments that we're proud of Signing with MetaMask Flask works. Build a wallet factory canister and every user can adopt one. Simulate RPC call (mainly Ethereum RPC request/response) and get correct results according to ICP definitions. Heartbeat function works correctly to refresh balance in time. What we learned Canisters are powerful, really pushing the boundary of blockchain technology. Users controlling and owning their canisters ( Self-Sovereign Canister ) is a very powerful design pattern. FoxIC won't be possible to send ICP transaction without it. Security comes first, usability is important too, and mass adoption is the catalyst. Keep BUIDLing. What's next for FoxIC Make ICP transaction happen inside MetaMask. Display transaction history and contact books for the user (one option is to store them in the canister and sync from it). Support IC tokens and NFTs. Upon the BTC/ETH integration, extend the ECDSA signing feature to the FoxIC wallet canister. So BTC/ETH will be supported, as well as transaction on other EVM-compatible chains. Instructions on how to use FoxIC Install MetaMask Flask If MetaMask is installed in the same browser, please disable MetaMask first (turn off at the extension control panel) Visit FoxIC and click "Connect to FoxIC" to see the magic. <div