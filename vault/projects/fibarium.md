---
slug: "fibarium"
url: "https://devpost.com/software/fibarium"
title: "Fibarium"
hackathon: "Privacy4Web3 Hackathon"
organization: "Oasis Foundation"
winner: true
words: 649
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "substrate/sensor_telemetry"
---

# Fibarium

> Fibarium - web3 solutions for secure storage of on-chain identities

[Devpost](https://devpost.com/software/fibarium) · hackathon [[Privacy4Web3 Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[provenance_signing]]
**domain** [[developer_tools]]
**substrate** [[sensor_telemetry]]

**stack** docker, evm, golang, javascript, postgresql, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

Architecture of creating and storing user profile Inspiration The amazing world of web3 apps makes you dive headfirst into various decentralized applications, meta-universes, games, financial tools. Simplicity, flexibility and convenience that are hidden behind complex math and cryptography surprises and impresses. We wanted to make a new product that allows you to easily connect to new web3 projects without complex knowledge and theories about blockchain, security and cryptography. Identity and personal data are closely linked to the user and are moving from the off-chain world to the on-chain world. Our project allows you to manage this identity and personal data, provide information to third-party applications or reject their requests, and not worry about security and your privacy. All privacy user data is stored encrypted inside the Sapphire blockchain. The user is free to manage their data through a browser extension and cryptographic keys. He can create new data, delete it or share it with the requesting party. All the complex processes are hidden behind cryptography and math. The user only controls the process of working with personal data. What it does Before you start working with Fibarium extension you need to create an SBT profile , which will store all necessary meta-information (checksum for encrypted data, by whom issued, when issued, when expires, NFT attributes) and the personal data itself in encrypted form (currently we additionally encrypt with AES-256 and a private account key). After the user selects the properties of his profile (web2 social networks, on-chain metrics, NFT collections, etc.) he MINT his profile in the selected host blockchain network. Metadata is stored publicly within the host blockchain, while private data is transferred via OPL to the Sapphire Blockchain , where it can be retrieved by a direct call to a contract with a given signature. When a user authorizes or registers on a third-party web3 application, the service can request the user's personal information (social networks, on-chain metrics, etc.), and the user can provide it or refuse to provide it. Every time profile information is requested in fibarium extension we pull data from the blockchain and decrypt it. We do not store the data locally and cannot recover it if the private key is lost. How we built it The project consists of two parts - Fibarium Web3 dApp , which is a user-friendly UI for creating, editing and interacting with the profile (mint/burn) and Fibarium extension - a browser extension that interacts with the blockchain, stores private keys, user identity and allows fast interaction with third-party applications via our own SDK. These two parts do not interact with each other directly through the API, but only through the SBT user profile. Challenges we ran into Oasis Sapphire turned out to be a very interesting and impressive technology for us. At first it was difficult for us to understand the OPL mechanism and the principle of Celer bridge operation, but later we were able to understand, study and test our prototype. Our solution was easily connected to our product through a so-called cartridge (conventionally, a type of data storage). Prior to working with Oasis Sapphire, we stored encrypted (AES-256) private data inside the host blockchain and used this option as the only one available. Accomplishments that we're proud of We've revised our application architecture. Previously, we only supported one way to store personal data, and that was inside the smart contract variable of the host blockchain. The addition of a new solution in the form of Oasis Sapphire forced us to rethink our earlier choice. We added the ability to connect different data stores without having to change applications, in the current form we can support an "infinite number" of data stores and change them on the fly. What we learned We have discovered an amazing technology and of course we will use it in our product as one of the key for storing private data. <div