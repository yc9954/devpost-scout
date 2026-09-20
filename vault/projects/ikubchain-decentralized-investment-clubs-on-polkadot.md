---
slug: "ikubchain-decentralized-investment-clubs-on-polkadot"
url: "https://devpost.com/software/ikubchain-decentralized-investment-clubs-on-polkadot"
title: "IkubChain - Decentralized Investment Clubs on Polkadot"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 477
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "substrate/financial_record"
---

# IkubChain - Decentralized Investment Clubs on Polkadot

> Democratizing collective investing through Polkadot DAOs. Transform investment clubs into transparent, cross-chain communities with trustless treasury management.

[Devpost](https://devpost.com/software/ikubchain-decentralized-investment-clubs-on-polkadot) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[provenance_signing]] [[vision_ocr]]
**domain** [[civic_government]]
**substrate** [[financial_record]]

**stack** ipfs, nextjs, on-chain, polkadot, substrate, tailwindcss, typescript, xcm

## How they structured the write-up

- inspiration
- what it does
- how we built it

## Body

Inspiration Traditional investment clubs and community savings groups—known as Ikub in Ethiopia, Tandas in Latin America, and Susu in West Africa—have empowered communities for generations. However, these models face critical challenges: trust issues with fund management, geographic limitations, opaque decision-making, and limited investment opportunities. We believed blockchain technology could solve these problems while preserving cultural wisdom. Polkadot's cross-chain capabilities presented the perfect foundation to build IkubChain —honoring tradition while introducing unprecedented transparency. What it does IkubChain transforms traditional investment clubs into decentralized autonomous organizations (DAOs) on Polkadot. The platform enables communities to create investment clubs with customizable governance, pool funds into multi-signature treasuries, submit and vote on investment proposals using quadratic voting, and execute investments across multiple blockchain networks. Returns are automatically distributed based on contribution ratios using the formula: $$ \text{Member Share} = \frac{\text{Individual Contribution}}{\text{Total Treasury}} \times \text{Investment Returns} $$ How we built it We developed a custom Substrate parachain with specialized pallets for club management, governance, and treasury operations. The frontend uses Next.js with Polkadot.js API for wallet integration. Cross-chain capabilities are implemented through XCM messaging. #[pallet] pub struct IkubClubs { #[pallet::storage] pub type Clubs<T> = StorageMap<_, Blake2_128Concat, ClubId, ClubInfo>; #[pallet::call] pub fn create_club(origin: OriginFor<T>, name: Vec<u8>) -> DispatchResult { // Club creation logic } } ## Challenges we ran into Mastering XCM for cross-chain operations was particularly challenging, requiring deep understanding of message formatting and error handling. Gas optimization across multiple chains presented significant hurdles, as we balanced functionality with transaction costs: $$ \text{Total Cost} = \sum_{i=1}^{n} (\text{Base Fee} + \text{Byte Fee}_i) $$ Creating intuitive interfaces for complex financial operations while maintaining security was another major challenge, especially for users new to blockchain technology. ## Accomplishments that we're proud of - Delivered a functional MVP within the hackathon timeline - Implemented quadratic voting to prevent whale dominance in governance - Achieved seamless cross-chain investment execution via XCM - Created an intuitive frontend that makes DeFi accessible - Successfully blended cultural traditions with cutting-edge technology - Built a foundation that demonstrates real-world impact potential ## What we learned We gained deep expertise in Polkadot's XCM and cross-chain messaging, advanced Substrate pallet development, and the importance of user-centered design in DeFi applications. The project taught us how to balance decentralization with practical usability and revealed the power of community governance in financial decision-making. We also learned that making complex blockchain operations approachable requires careful attention to user experience and progressive disclosure. ## What's next for IkubChain - Decentralized Investment Clubs on Polkadot Our roadmap includes mobile application development for emerging markets, integration with real-world asset protocols, advanced risk management features, and regulatory compliance frameworks for different jurisdictions. We plan to expand to additional blockchain ecosystems and develop white-label solutions for enterprise investment clubs. The long-term vision includes creating a global network of transparent, community-powered investment DAOs that make collective wealth creation accessible to everyone, everywhere. <div