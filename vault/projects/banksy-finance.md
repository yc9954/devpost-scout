---
slug: "banksy-finance"
url: "https://devpost.com/software/banksy-finance"
title: "Banksea Finance"
hackathon: "IGNITION | A Global Solana Hackathon"
organization: "Solana Capital"
winner: true
words: 827
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# Banksea Finance

> NFT Pool-based Lending, Convenient NFT collateralized loan to keep your funds fully liquid.

[Devpost](https://devpost.com/software/banksy-finance) · hackathon [[IGNITION - A Global Solana Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]]
**substrate** [[code_repository]] [[financial_record]]

**stack** rust

## How they structured the write-up

- inspiration
- what is banksea?
- how we built it?
- achievements we are proud of:
- what's next for banksea?

## Body

Inspiration NFT has great growth potential. According to NonFungible.com, up to now, there are 4.98 million transactions in the NFT market with a total transaction volume of approximately $134.9 million. 88,700 transactions with a transaction volume of $8.42 million have been completed within just a month. Defi has made it possible for decentralized financial entities to replace traditional ones. The integration of Defi and NFT has set off a new wave of trends in the whole encryption market. At present, NFT lending accounts for less than 1% of the NFT market cap, so it is obvious that NFT lending has become the next rising star in the field of decentralized finance. Most active NFT lending platforms in the market such as NFTfi, UpShot One, and NFT20 adopt the P2P trading model, these platforms require users to collateralize their NFT and both borrowers and lenders need to evaluate the NFT to reach a consensus before the transaction can be realized. This model is not capable of providing enough liquidity for the NFT market and fails to effectively improve the asset utilization ratio of NFT holders, and the lenders can even suffer the risk of capital loss. What is Banksea? Banksea Finance is committed to building the first NFT AI Oracle protocol and NFT Pool-based lending platform, helping to solve many problems that occurred in the NFT lending market, for example, the lack of NFT valuation mechanism, low asset utilization ratio of NFT holders, and the lack of guarantee for the safety of lenders' funds. To deal with this, the team has developed an NFT valuation mechanism based on AI technology, providing an NFT pool-based lending solution for the market. What distinguishes Banksea from the traditional P2P lending model is that Banksea creates this brand new NFT-pool based lending model where lenders can put their assets into the fund pool and obtain the corresponding yield while borrowers collateralize their NFT and then evaluates its mortgage rate and interest rate to complete the transaction. During the whole process, NFT valuation is provided by AI Oracle. Banksea, the first NFT pool-based lending platform, adopts a safe, convenient, and reliable lending model to increase NFT liquidity and improve capital utilization, which will greatly improve the integrated development of Defi + NFT and bring changes to the whole NFT lending market. Banksea fully considers the risks that both borrowers and lenders may bear in NFT transactions we adopt a multi-AI algorithm architecture to build risk control models before, during, and after loans to fully guarantee the security of the platform's funds. At the same time, the NFT AI oracle outputs the NFT price, risk value, and other data in real-time and provides standard API services for the NFT ecosystem. To deal with possible bad debts, we have established an efficient liquidation mechanism. Part of the collateral is sold below the market price in way of pre-payment and pre-liquidation and discount auctions, so that borrower can receive principal and interest that are supposed to return to the fund pool. In this way, the fund pool continues to operate healthily. We have also established a safe fund pool to deal with the occurrence of shortfall events and alleviate the pressure of fund shortage. A portion (40%) of the interest rate fees will be deposited into the Safety Fund Pool. In a shortfall event, Safety Fund Pool will kick in to pay back the bad debt and maintain the liquidity in the protocol. If the Safety Fund Pool fund has been exhausted, Backstop Module will kick in to sell KSE reserves and pay back the loan. The faster the Safety Fund Pool exhausts, the faster the Backstop Module will prepare to activate. How we built it? We use the anchoring framework to develop the RUST on-chain program, and then deploy it to the Solana chain. The front end is developed with React and uses the interface encapsulated anchor to access the Solana network to complete the call and interaction with the on-chain program. Banksea Dapp has applied on interacting to the front-end and smart contracts of Solana. Implement with NFT creation, trading, and auction in the marketplace. Achievements we are proud of: Product development: • AI Oracle beta test network release. Implement with the function of NFT evaluation in the whitelist. • Solana technology study completed. Refer to the article of Solana Study. https://link.medium.com/n5oB9DY62jb • The Implementation Of English Auction On Solana: https://link.medium.com/LJjn3ioNqkb • Marketplace trading function implemented. Grant & Hackathon: • Filecoin Hackathon 2nd place and jury award • NEAR MetaBUIDL Hackathon 3rd Prize We have built a strong and active community across the world. • Twitter: more than 21k unique followers • Telegram: more than 13k unique members • Discord: more than 15k unique members What's next for Banksea? We will empower the machine learning module for more range of NFTs. According to the roadmap, we will focus on the implementation of the risk control system and Banksea V1 with pool-based NFT lending. <div