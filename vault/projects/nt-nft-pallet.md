---
slug: "nt-nft-pallet"
url: "https://devpost.com/software/nt-nft-pallet"
title: "Ventur NT-NFT Pallet"
hackathon: "Polkadot Hackathon: North America Edition"
organization: "AngelHack"
winner: true
words: 321
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
---

# Ventur NT-NFT Pallet

> Non-Transferable Non Fungible Tokens, can serve as technical certifications and proofs of membership for groups and organizations. Our project implements NT-NFT functionality as a Substrate pallet.

[Devpost](https://devpost.com/software/nt-nft-pallet) · hackathon [[Polkadot Hackathon- North America Edition]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** node.js, rust, substrate

## How they structured the write-up

- project summary
- team - ventur

## Body

NT-NFT Substrate Pallet Ventur NT-NFT Pallet Project Summary The NT-NFT pallet is a Substrate module that implements Non-Transferable Non Fungible Tokens. Problem NFTs have generated significant value by creating a decentralized distributed digital representation of ownership. While the conventional paradigm of NFTs has found great success as a solution for assets with transferable ownership like art and even real estate, it is not suitable for assets like credentials and memberships, which need to be tied to a specific entity. Assets such as these require the implementation of Non-Transferable NFTs (NT-NFTs). The need for NT-NFTs has been discussed in the crypto community; most notably Vitalik Buterin recently wrote about the concept under the moniker of Soulbound Tokens . Solution Our solution is to implement Non-Transferable NFTs within a Substrate pallet. At its core, our pallet is based off of Substrate's existing open source Uniques pallet . From Uniques' base NFT implementation, we stripped out transferability and have modeled functionality for proposing and accepting NT-NFT assignments. Proposals and acceptances are intended to prevent the assignment of unwanted spam NT-NFTs to individuals. Additionally, we have added an optional expiration value which is aimed specifically at supporting impermanent credentials and memberships. Next Steps Refine NT-NFT Pallets Implementation Develop starter implementations for basic certification and membership use cases Integrate the NT-NFT pallet into Ventur, a business process focused parachain Create a testnet for Ventur and NT-NFT functionality Pallet Details NT-NFT Creation and Assignment Certification Membership Functions create_collection destroy_collection freeze_collection thaw_collection mint_ntnft assign_ntnft discard_ntnft accept_assignment cancel_assignment force_create force_collection_status Hackathon Challenge Statement NFT Substrate Usage The NT-NFT pallet is built as a pallet for Substrate Nodes and should enable integration of this pallet into any Substrate based blockchain. Team - Ventur ventur@popularcoding.com Patrick Gryczka Solutions Architect and Software Engineer GitHub - https://github.com/Gryczka Maciej Zielonka Software Engineer and Developer GitHub https://github.com/maciekzielonka Joseph Murawski Cloud Security Engineer and Operations Specialist GitHub https://github.com/d-z-o GinSiu Cheng Cloud Solutions Architect GitHub https://github.com/GinSiuCheng <div