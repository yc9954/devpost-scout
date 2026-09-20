---
slug: "nomis"
url: "https://devpost.com/software/nomis"
title: "Nomis"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 718
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/financial_record"
---

# Nomis

> Nomis is an on-chain credit score protocol that helps developers build better DeFi products.

[Devpost](https://devpost.com/software/nomis) · hackathon [[EthCC Hack 2022]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]]
**user** [[developer]]
**substrate** [[financial_record]]
  <sub>weak: web_dom</sub>

**stack** c#, css, dockerfile, html, javascript

## How they structured the write-up

- video presentation is here ↓
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nomis

## Body

Video Presentation is Here ↓ Please visit our Notion page to check our video presentation out. Inspiration With enough collateral, anyone can have access to capital to do whatever they want. Capital lending is also no longer enjoyed only by the wealthy; everyone can contribute to a decentralized liquidity pool that borrowers can take from and pay back at an algorithmically-determined interest rate. In contrast to applying for a loan from the bank where there are stringent Know-your-customer (KYC) and Anti-money laundering (AML) policies, one only needs to provide collateral to take a loan in DeFi ('How to DeFi' by CoinGecko). One of the most significant barriers to entry and adoption of DeFi are the over-collateralized loans. Today mainstream borrowers are either not using DeFi loans due to their unattractiveness as a financial tool comparing to banks' ones or taking over-collaterized loans with unfair collaterals (>125%) and APRs. Banks, in their turn, overcomes this problem by hiring credit scores. Such tool may also be implemented in DeFi making crypto loans more accessible for fair users, cultivating trust and reputation-culture. Moreover, credit score negatively impact the number of crypto fraud cases by disincentivizing actors to play dirty. To sum up, the problem that Nomis is going to solve is the over-collateralization in DeFi borrowing which is an entry- and adoption barrier for mainstream borrowers. What it does Nomis is a crypto protocol based on a mathematical prediction and AI model enabling protocol users with a favorable on-chain credit score to borrow crypto with a fair collateral and APR on a case-by-case basis. On the other hand, Nomis is an open-source protocol that helps web3 developers (via API) both to build new on-chain solutions and use cases, and to balance already existing high-TVL protocols (NEXT STEP). Nomis brings two crucial competitive advantages to the DeFi credit scores' table: 1) Nomis is an open-source solution that helps web3 developers leverage credit scores building better on-chain products and communities (NEXT STEP). 2) Nomis offers the most robust financial snapshot of a potential borrower hiring hierarchy analysis as a scoring method. We believe that hierarchy analysis is the most reasonable method for solving multi-criteria problems in complex environments with both tangible and intangible factors. Nomis is at the MVP stage —please follow the link to check Nomis Score of your ETH wallet (based on your on-chain data only). How we built it To predict of crypto borrower’s reliability on the basis of wallet’s data and transactions history, it's proposed to hire a model of trained AI built on the hierarchy analysis and pairwise comparisons methods. The choice of these methods is justified by the data insufficiency of the crypto loan defaults for the development of forecasting mathematical models based on statistical approaches. The hierarchy analysis method seems to be more reasonable for solving multi-criteria problems in complex environments with hierarchical structures involving both tangible and intangible factors than the linear logic approach. Also, the method of hierarchy analysis is a closed logical construction providing, with the help of simple rules, the analysis of complex problems in all their diversity and leading to the best answer. Moreover, the application of this method enables including all the knowledge we have on the problem into the hierarchy. This approach, from our point of view, is a balanced way of solving a quite difficult problem: credit decision forecasting with insufficient statistical data. Challenges we ran into Choose and justify the appropriate methods for the model. Build the mathematical model for credit score calculation based on expert opinions. Find time to get together and crack the hack :) Accomplishments that we're proud of We are proud that we are already at the MVP stage. Moreover, we have already designed business model for Nomis and tested few product- and business model-related hypotheses. What we learned How to work with Etherscan's API. Deepen our knowledge about the Ethereum's sctructure. What's next for Nomis We are going to make Nomis self-sufficient by hiring the fee-charging business model (1% fee per API usage). Although, the long-term vision for Nomis goes far beyond credit scoring for DeFi. In the future, other dApps will use Nomis Score as a wallet qualifier for making job offers, for adding in whitelists, for offering special marketing terms, or just for inviting to a private party, etc. <div