---
slug: "0xdeadlist"
url: "https://devpost.com/software/0xdeadlist"
title: "0xDeadList"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 746
team_size: 3
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "substrate/web_dom"
---

# 0xDeadList

> 0xDeadList collects the "dead" address with leaked private key. Users lock/bury wallet and get NFT for reporting leaked private key. Dapps can block those compromised wallets with on/off-chain APIs.

[Devpost](https://devpost.com/software/0xdeadlist) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[provenance_signing]]
**substrate** [[web_dom]]

**stack** alchemyapi, amazon-web-services, polygon, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for 0xdeadlist

## Body

0xDeadList Burier NFT Tombstone SBT the 'deadlist' is maintained on the github by periodically dump dead addresses into it Inspiration When we say that an Ethereum account has been lost, it refers to two cases: The owner forgets the private key, which means the assets are permanently lost. The owner leaks the private key, which means anyone with the private key can act the same as the original account owner. Our project aims to protect account owners of the latter case, which is very dangerous: the account owner loses the exclusive right to use the account, which indicates the account is not secure anymore. For leaked accounts, DApps should be aware of them on time to protect the original owners of these accounts. For example, when one reports that her account is leaked: Multi-signature wallets (e.g., Gnosis Safe ) should ban this account. Web3 email providers (e.g., MetaMail ) in which users log in with signatures should suspend everybody's access to emails of this account to protect the privacy of the original owner. Electronic agreements based on ETH accounts (e.g., ETHSign ) should disqualify this account to sign new agreements. Because the new agreements signed may not be authorized by the original owner. To solve the above problems, we propose the 0xdeadlist.io project to maintain a list of addresses whose private keys have been leaked. By rewarding the burier NFT (Non-fungible token), 0xDeadList encourages users and hackers to report accounts with leaked private keys, and stores the information of these leaked accounts on the chain to facilitate DApps project parties to query these insecure accounts. What it does 0xDeadList is a public good which encourages users to collect and report addresses whose private keys are leaked. Users can directly log in to 0xdeadlist.io to report the leaked address. The main contract of 0xDeadList provides two steps ( lock address and bury address ) to report leaked address under the following considerations: Preventing the reporter's NFT reward from being stolen by front-running attacks . Ensuring the reporter has enough time before the private key of the leaked address is fully disclosed. In step 1, the reporter locks the address to be buried, and the contract records the address of the reporter. At this time, the private key of the locked address will not be disclosed. In step 2, the user uploads the private key of the locked address in step 1, and the reporter address recorded in the contract will receive an NFT reward, indicating that the address is buried, and the buried (or say, leaked) address will receive a tombstone SBT (Soul Bound Token), which is not transferable. In step 2, the private key of the buried address will be made public (recorded on-chain), ensuring the leaked address is indeed leaked. The 0xDeadList project is fully open-sourced, and here are some resources: Website: https://0xdeadlist.io Github: https://github.com/0xDeadList Contracts: 0x59451a98d772f2a53ca2241a884b1703f8c55218 The NFT and SBT can both be viewed in OpenSea, the following are some examples: How we built it Contract: We write contract code with replit and deploy it on Polygon chain. Frontend: We use React framework. The code is hosted on Github and deployed on AWS using CodePipeline, S3 and Cloudfront. Backend: We use alchemy API to access blockchain. We use github actions to periodically dump dead address into deadlist.txt . Design: We use Figma for UX design. Challenges we ran into High Gas: One core process of the contract is to generate address based on the private keys (Elliptic Curve Digital Signature Algorithm operations). This process is computing intensive and needs a lot of gas. Luckily, gas price on Polygon is rather low. This significantly reduces the gas fee. Avoid Front-Running: In the first version of contract, it only needs one step to bury an address: simply writing private key to contract to get NFT. However, this may cause front-running issue. We designed the Lock-and-Bury pattern to address this issue. Accomplishments that we're proud of We have successfully implemented the contract, design, and frontend work from zero. This project is highly completed. 0xDeadList is supported and used by MetaMail and EthSign . What we learned There are much more dead addresses in reality than we expected before. Keep potential attack models in mind while designing the project. What's next for 0xDeadList Collect more leaked addresses (estimated over 200k). Use ChainLink to provide on-chain API for other chains (e.g., Ethereum Mainnet). Apply for grants from DApps, rewarding reporters based on the value of the reported addresses. <div