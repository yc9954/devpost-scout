---
slug: "nft-exchange-for-near"
url: "https://devpost.com/software/nft-exchange-for-near"
title: "NFT Exchange for NEAR"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 999
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# NFT Exchange for NEAR

> NFT Exchange is a digital marketplace that lets you trade NFTs with a community of collectors.

[Devpost](https://devpost.com/software/nft-exchange-for-near) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**mechanism** [[simulation_digital_twin]]
  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]] [[finance_payments]] [[legal_justice]]
**user** [[developer]]
**substrate** [[document_pdf]] [[financial_record]]

**stack** assemblyscript, near, nextjs, react, typescript

## How they structured the write-up

- what it does
- motivation
- features
- how we built it
- process flow
- technologies
- challenges we ran into
- what we learned
- future work
- live product preview

## Body

Main Page Creating a listing Viewing a listing Making an offer User Dashboard Listings User Dashboard Offers What it does Discover and trade amazing NFTs NFT Exchange is a digital marketplace that lets you trade non-fungible tokens (NFT) with a community of collectors. You can list your tokens up for trade and start receiving offers, and the exchange takes place when you accept an offer. The platform is entirely decentralized and is open source, you can be rest assured that your transactions are safe and trustless. Motivation While it is common for non-fungible tokens (NFT) to be sold for cryptocurrencies instead, a service to swap a pair of NFT directly opens up other possibilities. For collectors or long term holders who wish not to sell their collection for money, but would be open to exchange them for other desirable tokens, NFT Exchange would be the perfect place to start. Also, with the adoption of blockchain technologies becoming more mainstream, NFT could someday represent physical assets like cars and real estate, or important legal documents. In which case direct exchange of NFT would be appropriate; buying a house could mean exchanging mortgage binding agreement between a bank and a purchaser. Features Interactive web user interface accessible from any device. Put any NFT (NEP-171 compliant) up for trade by creating a listing, with the option to write what you're looking for in return. Browse other listings to discover interesting NFTs for trade. See an NFT you like? Offer up your own NFT to exchange for it. Manage your listings and offers through your personal dashboard. All transactions happen in the blockchain. How we built it We wanted to build a digital marketplace that supports a wide range of NFTs. Hence, we designed the Exchain smart contract to be separated from the NFT contracts where interactions would happen through cross-contract calls. This meant that we needed to call functions that is sure to exist on the NFT contracts. For this, we relied on the NEP-171 standard interface which is adopted in NEAR today. We limit contract calls to only two functions: nft_transfer and nft_tokens_for_owner , to verify the owner of an NFT and to make transfers. The Exchange smart contract itself is only responsibile for markerplace functionalities like listings and offers management, and the swap/exchange transaction. Process Flow Seller creates a listing by transferring their NFT to the exchange smart contract. The exchange contract creates a listing record tied to the receiving NFT and the seller account ID. Buyer make an offer on a listing by transferring their NFT to exchange smart contract. The exchange contract creates an offer record tied to the receiving NFT and the buyer account ID. If seller accepts the offer, the exchange contract transfers the offer NFT to the seller and the listing NFT to the buyer. If seller cancels a listing, the exchange contract refunds the listing NFT back to the seller and deletes the listing record. If buyer retracts an offer, the exchange contract refunds the offer NFT back to the buyer and deletes the offer record. Technologies Web Application (UX) The frontend web application is developed in React using the NextJS framework. Integrates with NEAR blockchain via the near-api-js SDK, on two different smart contracts. Blockchain Smart Contract Exchange Contract : NEAR Smart Contract writen in AssemblyScript repesenting the exchange contract. This contract is responsible for the marketplace functionalities including listing, offering, transactions and accounts management. See NFT Exchange Contract functions for functions. NFT Contract : The official NEP-171 compliant NFT contract from https://github.com/near-examples/NFT . We are using this contract as a starting point for building the exchange marketplace based on the NEP-171 specifications. Exchange Contract Functions Function Description CreateListing Creates a listing of an NFT token making it available for receiving offers. CancelListing Cancels a listing. Caller must be the creator of this listing. MakeOffer Makes an offer for a listing, providing an NFT token as the offer item. CancelOffer Cancels an offer. Caller must be the creator of this offer. AcceptOffer Accept an offer and executes the exchange transaction. getListings Gets all open listings. getListing Gets a single listing. getOffers Gets all open offers. getOffer Gets a single offer. Challenges we ran into As this was the first time developing on NEAR blockchain and having no prior experience on Rust or AssemblyScript, we had to spend some initial time learning the platform and AssemblyScript language. There were fewer examples of NEAR AssemblyScript projects as compared to Rust. Had to go through many trial and errors to get Cross-Contract Call working; such as running out of Gas, and NFT transfer requiring exactly 1 yoctoNEAR, predecessor ID and authorization. Initially we created several subaccounts to simulate different users on our platform, but later found that we couldn't login to them on NEAR wallet because we don't have the secret phrase. What we learned After trying out several blockchains, we learned that NEAR platform is the easiest to get started on, especially for developers that may be new to blockchain development. From wallet and authentication management to invoking contracts Being able to create testnet and development accounts with preloaded GAS is extremely helpful since there is no need to request for GAS before we can even deploy our smart contract. AssemblyScript is a new language we picked up, and knowing an additional programming language is definitely something we are proud of. Future work Prepare a strategic roadmap of the project which will include development and marketing efforts. User experience refinement to incude NFT categories and better seller and listings information. Improve smart contract for better integration. Decide on a monetization strategy. We recognize that being open to supporting multiple blockchains is important for eventual growth. Therefore, we want to include the possibility of expanding support to different chains. Live Product Preview Alpha Preview: nftexchange.vercel.app This is a pre-alpha version of the application. The smart contracts are deployed to the following accounts on NEAR testnet: nft.jeffreylewis.testnet - the NFT contract exchange.jeffreylewis.testnet - the exchange contract <div