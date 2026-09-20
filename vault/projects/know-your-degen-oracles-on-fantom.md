---
slug: "know-your-degen-oracles-on-fantom"
url: "https://devpost.com/software/know-your-degen-oracles-on-fantom"
title: "Know Your Degen Oracles on Fantom"
hackathon: "Fantom Hackathon Q1 2023"
organization: "Fantom Foundation"
winner: true
words: 486
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/revocation_withdrawal"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
---

# Know Your Degen Oracles on Fantom

> Know Your Degen (KYD) Oracles allows your Fantom Smart Contract dodge transactions from addresses flagged with a pre-defined set of rules, i.e. addresses that have ever interacted with Tornado Cash 🛡️

[Devpost](https://devpost.com/software/know-your-degen-oracles-on-fantom) · hackathon [[Fantom Hackathon Q1 2023]]

## Facets

**mechanism** [[realtime_stream]] [[revocation_withdrawal]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]] [[regulation_legal_text]] [[structured_db]]

**stack** ethers.js, javascript, react, redstone, solidity, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for know your degen oracles on fantom

## Body

KYD Oracles on Fantom Demo Web App Three levels of verification on smart contract level Smart Contract extracting call-data package and deciding if to accept or dodge transaction Address illegible for transaction (not passed KYD) Examples of data sets that can be used for KYD Inspiration AML and KYC regulations are coming to DeFi & Web3, that's a fact. But can we minimise the risk of dirty money or even comply with regulations the degen way? Turns out we can! Explore Know Your Degen KYD Oracles on Fantom 👻 This tool can finally enable institutions to interact with DeFi, providing enormous liquidity & cash inflow as a consequence. On top of that crypto hedge funds, dApps, DAO and other organisations interacting with or launching Smart Contracts can eventually set their own rules on SC accessibility. What it does Every Smart Contract on Fantom with KYD Oracle integrated would doge transactions from addresses flagged with pre-defined rules, i.e. those that interacted with Tornado Cash or allowing only addresses that have gone through KYC with trusted parties such as Coinbase. The key design & UX advantage is that dApp users do not notice that their addresses are verified before transactions as that happens on the Smart Contract level and is abstracted away from end users. How we built it KYD Oracle is an implementation of RedStone infrastructure & database of addresses that have done withdrawals from Coinbase (so did KYC with them too). The speed, low transaction costs, and no throughput problems of Fantom make the KYD Oracle a perfect match for its Web3 & DeFi ecosystem. Challenges we ran into The major challenge has been around the integration of KYD Oracles on Fantom and making sure everything works stable & scalable in the Fantom ecosystem. Secondly, getting a dataset from Coinbase and making checks as close to real-time as possible was not a trivial task. Accomplishments that we're proud of KYD Oracles is available on Fantom mainnet and works stably 🥇 What we are really proud of is that the Coinbase demo is just the first idea of the KYC level. Users can implement their own rules for Smart Contracts protections as outlined in the video demo. What we learned Sometimes you need to do trade-offs to achieve efficiency and cope with limited time - therefore we had to refrain from adding other levels of KYC for now. But that's perfectly possible, together with the integration of forensic services such as Chainalysis or Elliptic. What's next for Know Your Degen Oracles on Fantom We are very keen on hearing feedback from hackathon organisers and the Fantom builders community about KYD Oracle. If we manage to win a prize, we definitely would have some points on our roadmap, including: Integration of new addresses databases, exploring cooperation with forensic companies that the Fantom ecosystem values, as well as tightening cooperation with the Fantom team & ecosystem developers 🤝 <div