---
slug: "llamas-finance"
url: "https://devpost.com/software/llamas-finance"
title: "Llamas Finance"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 602
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Llamas Finance

> Fixed Annuities — lower fees, more trust, less complex, full equality

[Devpost](https://devpost.com/software/llamas-finance) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[finance_payments]]
**user** [[small_business]]
**substrate** [[financial_record]] [[structured_db]]

**stack** alchemyapi, chainlink, hardhat, moralis, nextjs, polygon, thegraph

## How they structured the write-up

- inspiration
- what it does
- how does it work
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for llamas finance

## Body

Landing Marketplace Propose annuity agreement View annuity agreement details (Annuitant/Lender) View annuity agreement details (Provider/Borrower) FAQ #1 FAQ #2 Graphic Slide Slide Deck #1 Slide Deck #2 Overview Slide Deck #3 Problems Slide Deck #4 Fees Slide Deck #5 Mistrust Slide Deck #6 Complexity Slide Deck #7 Inequality Case Study Inspiration We wanted to fix the broken annuity industry. What it does A fixed annuity is a contract between you and an insurance provider. It can act as a safe place for cash to accumulate interest tax deferred. You pay a lump sum of income, and in exchange, the insurance provider guarantees your principal plus a minimum interest rate fixed over a multi-year time horizon. At the end of the annuity agreement’s period, you can withdraw your initial principle plus the accumulated interest. How does it work An “annuitant” proposes to the market an annuity agreement that specific their initial USDC deposit, the period of the agreement, and the fixed annual interest rate they want to earn over that period. “Providers” view proposed agreements to find opportunities for extremely low interest rate loans. When they find an agreement they like, they’ll “activate” it by overcollateralizing the future value (principal + accumulated interest) with ETH in exchange for the ability to borrow the annuitant’s USDC deposit. While an annuity agreement is active, providers may invest the USDC in other markets (like an S&P 500 index fund or a small business) where they expect to earn a yield that outweighs their borrowing cost. Providers are not required to pay any interest until the end of the annuity period, but they can if they wish. If the value of a provider’s ETH collateral nears the agreement’s future, then they will be automatically liquidated so that the annuitant is guaranteed the principal and interest that the agreement spelled out. Otherwise, if the provider repays the agreement’s future USDC value and they don’t get liquidated, then they’ll get their ETH collateral returned to them. How we built it Hardhat smart contract development environment React-nextjs frontend environment Chainlink price feeds and keepers to manage auto liquidations Moralis web3uikit, react-hooks, api, and database to help develop the frontend Deployed on Polygon The Graph to explore the smart contract and save metadata like events and transactions. Challenges we ran into Martin says : Working with the information that comes from the smart contracts and learning to use Moralis hooks Himanshu says: Limitations of solidity and how to overcome those , deploying a subgraph , general idea of defi , communicating with teammates etc. There were some challenges too like working with typescripts , GraphQL , building the logic for smart-contract. Colin says : Structuring the smart contracts initially Collaborating across timezones and different languages Managing time Accomplishments that we're proud of Colin says: Putting together a full stack application Creating something with real potential utility value Himanshu says: Working in this project was super fun…. Overall I have gained much more experience and realized that there's a lot to learn and understand from here on. Marin says: Design of the application What we learned Colin says: Developing with Chainlink and Moralis Working as a team with different skillsets and background Improved our smart contract development skills Martin says: I learned about frontend web3 libraries and how to work with smart contract functions in the frontend. Himanshu says: I learned so much about how the smart-contracts works. What's next for Llamas Finance Keep working on fixed annuities and then branch out to bring more traditional finance products into web3 Find customers Make the product easier and more friendly to use <div