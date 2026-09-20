---
slug: "ustx-bond"
url: "https://devpost.com/software/ustx-bond"
title: "USTX - BOND"
hackathon: "TRON Grand Hackathon - HackaTRON Season 6"
organization: "TRON DAO"
winner: true
words: 475
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/climate_energy"
  - "domain/finance_payments"
  - "substrate/code_repository"
---

# USTX - BOND

> A bond emission - redemption mechanism for the USTX ecosystem to strenghten the project and provide a safety net for users.

[Devpost](https://devpost.com/software/ustx-bond) · hackathon [[TRON Grand Hackathon - HackaTRON Season 6]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[climate_energy]] [[finance_payments]]
**substrate** [[code_repository]]
  <sub>weak: web_dom</sub>

**stack** html, javascript, php, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ustx - bond

## Body

Inspiration The USTX ecosysten has been generating rewards for its users since 2021 through the several dApps developed over the years, like Staking, WARP, T-Boost and Ergon, but this has not meant a corresponding reflection on USTX token price. With Bond the aim is to create a safety net for all users by decreasing the sell pressure on the token and giving more confidence about the long term resiliency of the project. What it does It creates a decentralized framework for USTX bond emission and redemption Bond emission Every user can emit a new bond by committing a certain amount of USTX to the Bond dApp. The price is set automatically at 0.01USD (USTX launch price) An emitted bond can be withdrawn at any time by the user, without any penalty. Bond redemption Every user can redeem a bond, by purchasing the underlying USTX at 0.01USD value A tax of 5% will be applied to the bond emitter. So when a 10000 USTX bond is redeemed, the emitter will get 95USD and 5USD will be taken as fee. When there are pending bond emissions, 80% of USTX protocol rewards will be routed to bond redemption. Additional resources will be allocated by the team depending on pending amount When the bonds are redeemed by the team, the underlying USTX will be BURNED The bonds are redeemed based on time of emission, in FIFO order Risks As always, we want informed users, so here’s our risk assessment for Bond: smart contract risk: we carefully designed and tested the contracts on Nile and mainnet, but human error can never be excluded 100%; the time in which the bonds are redeemed depends on the amount of resources available. This is not financial advice, DYOR. How we built it The project core is a smart contract deployed on Tron blockchain. The UI has the same look and feel of other dApps in the USTX ecosystem to have a family feeling and easier learning curve. Development was made using Tronscan, TronIDE, Tronlink and HTML5 development tools. Challenges we ran into Creating a new smart contract that is easy to maintain and safe to operate. It's designed as an upgradeable contract to allow for improvement and maintenance. Accomplishments that we're proud of The team was able to release the demo version on Nile in time for the deadline. Soon our long time users will a have a strong safety net and support line on USTX price at launch level. What we learned Listen to users. The best ideas often are seeded by user requests or suggestions. Bond is no different. What's next for USTX - BOND Hopefully nothing. The best safety net is the one that is never used. Jokes apart, next steps are testing, testing, testing and mainnet deployment, regardless of hackathon results. USTX team is committed to delivering. Always. <div