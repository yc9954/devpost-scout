---
slug: "zktrace-629hxs"
url: "https://devpost.com/software/zktrace-629hxs"
title: "zkTrace"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 1000
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/civic_government"
  - "domain/supply_logistics"
  - "user/general_public"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# zkTrace

> A privacy supply chain management protocol

[Devpost](https://devpost.com/software/zktrace-629hxs) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[civic_government]] [[supply_logistics]]
**user** [[general_public]] [[small_business]]
**substrate** [[financial_record]] [[video_visual]]

**stack** chainlink, hard-hat, ipfs, ipld, javascript, merkle-tree, solidity, zero-knowledge, zokrates

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for zktrace

## Body

Order review ZK proof sent to supplier Verifier addresses added Inspiration Supply chain management has been difficult to manage over the couple of years, from small businesses down to the large corporations. And within the last few years, so many companies having gotten knee deep into the blockchain space, have been skeptical about introducing their businesses to the blockchain, as it risks leaking sensitive data and requires some high level management, on any of the public blockchains available. Difficulties and hinderances like these are caused by: • privacy • a lot of bureaucracy and gas between levels in the system • difficulty in tailoring out a supply chain management solution (joining a common network) • requiring advanced setups Alternative solutions have been provided like: • Developing a custom solution for each party of exchange. Con: This is rather expensive to develop and scale when new players join. Leading them to develop their own custom solution to join in. • Using a centralized system to store records and agreements between companies since its easier. Con: There exists one-sided control and access to data. Introducing a neutral party is expensive and still gives more systems access to sensitive data. • Using enterprise blockchain networks. This helps in access restriction, decentralization and necessary integration. Con: It lacks in security, privacy and performance standards. Hence, this is why we built zkTrace, a blockchain supply chain management protocol that permits companies to provide private and safe business operations. What it does zkTrace is a protocol that combines the power of blockchain for trustlessness, and zero knowledge for privacy, to provide safe and confidential business processes, correctly order events and increase work flow at no cost (gasless). The protocol provides an implementation after a common frame of reference has been agreed between businesses, validating private collaborations between companies without leaking sensitive data. It is built to ensure easy and trustless agreement between corporations and entities. zkTrace allows you to customize and describe business processes, regardless of how complex they are, using smart contracts. How we built it Unlike other systems, zkTrace is built to have the frame of reference immutable and resistant to tamper once the state (handshake) has been established. First, we make reference to the Buyer system and the Supplier system. The Buyer requests for a quotation from a specific supplier, detailing the items needed, quantity, dates, etc). The supplier receives and reviews the request. They then send back their proposed terms including prices, discounts, availabilities of products etc. (These details are used to create the Trace Agreement) The Trace Agreement contains the overall details of the transaction and the number of levels within a particular supply chain management. The buyer then receives the proposal and either agrees or declines, requesting for adjustments. Agreement between the Buyer and the Supplier is called a "handshake", in literal representation of an agreement ( state ). After the handshake, a cryptographic proof (zero knowledge proof & nullifier) that confirms the proper business logic and commercial data application, is generated and sent to the Supplier and the Buyer consecutively. The cryptographic proof is created using, a random number generator built with Chainlink VRF, to generate a nullifier (after hashing) and zero knowledge circuit to generate zk proof. The two cryptographic proofs are used to create the Trace Agreement, which is the smart contract that controls every state of the supply chain and contains details of each transaction. Each supply chain is a unique transaction and the Trace Agreement represents each. The Trace Agreement helps with verification for the different stages of the supply chain. When the Buyer is ready to begin the process, they initialize the order after updating the supply chain stages & addresses and input the cryptographic proof generated for verification. The Supplier is then notified to confirm the execution of the order by verifying his cryptographic proof. Once this is done, the Trace Agreement is open. Each stage, the movement and state of the transaction is seen on chain. The verifier addresses for each stage of the transaction have to sign consecutively, confirming the state of the transaction before going to the next. The verifier addresses are used to create a merkle tree and the merkle root is saved on the smart contract. Tools Used: • Chainlink VRF : is used to build our random number generator which returns an array of numbers. The seed (a number in the array) is used to create nullifier used and the array of numbers is used in the zero knowledge circuit to generate zero knowledge proof. The zero knowledge circuit is designed to compare the pre image of the generated random number. • Chainlink External adaptor running on a Chainlink node for on chain zero knowledge verification. The adapter verifies the proof generated and is used to connect to the zero knowledge engine we built via its API for easy on chain zero knowledge verification. • Merkle tree : used to save the list of verifier addresses for easy verification • IPLD (inter planetary link data) : used to save the meta data of the Trace agreement the list of verifier addresses (data persistence). • web3storage : used to pin the meta data on IPFS. Challenges we ran into • Understanding how zero knowledge proof works and implementing it in the protocol • Lack of resources for building private E2EE on-chain messaging protocol Accomplishments that we're proud of • Understanding how to build zero knowledge circuits. • Finding solutions to making supply chain gasless using relayers. • Increasing privacy through the combination of zero knowledge proof and merkle tree. • Building a supply chain protocol What we learned • create a privacy mechanism for supply chain management and agreement between corporation on a public blockchain. • work with zero knowledge, zokrates, zk SNARK and Merkle Tree. What's next for zkTrace • Further looking into building our own efficient private E2EE on-chain messaging protocol (using Tendermint). • intense marketing and full documentation. • properly integrating this into businesses. <div