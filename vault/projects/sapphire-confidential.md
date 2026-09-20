---
slug: "sapphire-confidential"
url: "https://devpost.com/software/sapphire-confidential"
title: "Sapphire Confidential"
hackathon: "Privacy4Web3 Hackathon"
organization: "Oasis Foundation"
winner: true
words: 637
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "substrate/financial_record"
---

# Sapphire Confidential

> Make yours transactions private on web3 blockchains with the power of Sapphire.

[Devpost](https://devpost.com/software/sapphire-confidential) · hackathon [[Privacy4Web3 Hackathon]]

## Facets

**mechanism** [[privacy_tech]] [[provenance_signing]]
**domain** [[developer_tools]]
**substrate** [[financial_record]]

**stack** solidity

## How they structured the write-up

- inspiration
- what it does
- how it works
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sapphire confidential

## Body

App demo Standar solution As simple as a wallet exchange Steps Sapphire Confidential solution Inspiration I have been working on Mixer for Ethereum and were discussing with the oasis team to use Sapphire for more privacy on transaction. What it does Mixer 1.0 uses a central point, a centralized smart contact. That is good to obfuscate transaction but show who is using the mixer. In the recent work we got all the mixer user tagged and their address banned. Mixer 2.0 uses virtual address for the mixer flow. The flow is not visible and addresses being mixed cannot be tagged. Secure Hardware like TEE, HSM, Secure Enclave, gives the possibility to handle private key that are directly accessible by nobody (depending of the physical security of the hardware) and that can be used for detaining assets and signing transactions for the blockchain. Using virtual addresses is smoother for mixers and remove the constraint to have fix amount of asset locked and to have a long minimum time for waiting. Oasis Sapphire Blockchain give the possibility to manage private keys within a private smart contract where the data are kept private into the contract with secure enclave technology. and private exchange. How it works There are two flows, not to be able to retrieve information by timing. The first flow is used to transfer assets. The second flow is used to drive the mixer. The two flows should be independent with the user using two different addresses as identity. User generate a virtual address with the mixer using the second flow. User send token to the virtual address using the first flow. The mixer is informed that the virtual address is filled and list it as value to mix. When another user add an address with value, the minimum common is used between the two address to be mixed. When the amount of mixing is validated, the user can generate a transaction Sending the transaction to the main network wil send fount from an anonymous random address to the recipient. How we built it A simple smart contract and a nice UI from Sapphire doc templates. The app is connected with a first provider with the main address with metamask. A Sapphire wallet is generated to be used with the smart contract and stored inn the browser local data. It will trigger all step using one or the other provider when needed. The smart contract use the key pair generation as well as the signature feature in Sapphire. I have been removing all visible information to make sure it is not possible to deduce what is going on. As example the total balance cannot be know because it can be use to monitor the change with a transaction. Challenges we ran into With the Sapphire web3 api, read after a successful transaction does not reflect the new blockchain state, so i needed to trigger read on some smart contract state value that change with the transaction to know that the state is effective. Summarize it in 3 minuts Accomplishments that we're proud of It seams to work well. It was quite complex to design, but the main part is here and working. What we learned As a Validator, I'm happy to see how I can use Sapphire and how it can make a difference with other networks. I have learn the Sapphire SDK witch was rely useful in my case. What's next for Sapphire Confidential That is the basic, a Mixer in Sapphire has some use but adding an oracle for wallet balance and address nonce will give the ability to extend it to other web3 chains. The smart contract will remain within Sapphire but Virtual wallet could be used from any chain (Ethereum, Polygon, Celo, ...). It can also be seen as a bridge between chains. <div