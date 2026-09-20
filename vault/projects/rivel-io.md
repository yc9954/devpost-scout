---
slug: "rivel-io"
url: "https://devpost.com/software/rivel-io"
title: "Rivel.io"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 1029
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "domain/retail_commerce"
  - "user/developer"
  - "user/general_public"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
---

# Rivel.io

> A set of tools to make recurring payments in crypto easy.

[Devpost](https://devpost.com/software/rivel-io) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[immigration_refugee]] [[retail_commerce]]
**user** [[developer]] [[general_public]] [[small_business]]
**substrate** [[financial_record]] [[sensor_telemetry]]

**stack** amazon-web-services, chainlink, javascript, mongodb, node.js, react, sequence, solidity, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for rivel.io

## Body

Inspiration It all started on a vacation in Hungary and paying for an accommodation with crypto. A great experience that felt even easier than paying with a credit card. After a long day of traveling and arriving in Budapest, Mico decided to treat himself to an episode of Stranger Things. During all the mayhem in Hawkins and a Soviet prison, it struck him: why couldn’t he pay for my Netflix with crypto as well? Recurring payments with crypto - a perfect idea for a hackathon. What it does Rivel aims to make recurring payments easy for merchants and customers, regardless of their knowledge of crypto. You can be a well-versed Web3 dev or a Mom ’n’ Pop Shop owner - we want to make the process of integrating payments as simple as possible. For the hackathon we built a merchant dashboard along with a no-code checkout to accept recurring payments in a few clicks. We allow both parties - merchant and the user - to choose their preferred payment token and our contract handles swapping between them automatically. Through the dashboard, you can create a merchant account, api keys, and products. The dashboard provides statistics on the performance of your product. When creating a product, the merchant can specify the token they wish to settle payments in. When customers go to purchase a subscription, they can use any token with sufficient liquidity, as long as a price oracle can be found on the chosen blockchain. For the purpose of the hackathon, we limited support to 4 tokens. How we built it The smart contract is utilizing Chainlink Oracles to determine exchange rates between two different tokens and token swaps are handled using Uniswap. The v3 router allowed us to use multihopping, where we can move between liquidity pools to ensure the swap to the output token set by the merchant. For tooling, we used hardhat and ethers. To make the user experience fast and allow ourselves a bit more freedom when working with data, we decided to introduce some centralization to the project. We built a backend running on Node, Typescript and MongoDB for querying product data, payments, subscriptions and other important metrics for merchants using Rivel. Styling was done with Tailwind CSS. The backend is directly interacting with the blockchain and we are using AWS Lambda to process user’s subscriptions. Our contract is designed with security in mind, and if our backend was compromised, no abuse can be done to subscribers. Rivel’s no-code checkout page is hosted on Spheron Network. Challenges we ran into Solidity Debugging - we work with solidity often, yet the debugging process is always disheartening. We ran into issues surrounding the calculation of exchange rate on our contract. We failed to account for some factors impacting our calculations, including ERC20 contract decimals, float support, and path generation for the swap router. Many of these issues are not recognized by the compiler, and required detailed testing. With simpler contracts, it’s great because you can deploy to a VM - however, due to external contract calls, we have to do our testing on Polygon, which took some time to approve transactions. The process took longer than anticipated. Crazed by hackathon magic, we were thinking of expanding our subscription processor with complex features, such as automatic cross-chain swapping. The challenge was not of a technical type, but a business problem: if Rivel was to be a viable product, we couldn’t handle all the gas fees added by all this functionality without being too expensive for merchants. A difficult decision had to be made: we decided to cut a cool feature out in favor of business. Accomplishments that we're proud of We discovered the hackathon late, joining roughly a month in. Since our start, it's been a fast-paced development sprint full of disappointments and joys. It would be lying to say it’s not the whole project - recurring payments truly accessible on-chain. We also cracked a very important problem that many merchants are afraid of when accepting crypto: volatility. As a merchant, you want to allow payments in crypto, but not necessarily take the risk of the asset’s price going down. Instant swaps allow merchants to accept payments in a stablecoin, but users can pay in another token. It truly is something to be proud of. What we learned A product for everyone is a product for no one. When ideating, we knew early we wanted to focus on a payment processor solution. After much thought, it became clear we needed to specialize and focus on 1 feature (subscriptions) before branching out into other offerings. Don’t jump straight to building the car In the beginning, we had big visions for what we wanted the product to be. We certainly underestimated the development process and could have saved time by starting small. You can’t build the final product from the beginning, you have to start with an MVP. Spend the extra time Whether it was writing tests, code, or ideating, we often paid a price for cutting corners. For example, with testing the contract, we were in a rush to see if it was working. Writing quality tests would have taken extra time upfront, but saved time that was then spent debugging. What's next for Rivel.io What started as an idea for a hackathon, formed to be a project that can really grow to be a great business. As developers it’s very easy to get caught up on technical details, but to be frank, all the important next steps are business decisions: how to get merchants using Rivel and accepting recurring payments like never before. It is clear to us that the hackathon is not the end of the story for Rivel. Next Steps Short Term Debug our current MVP and bring it to a consumer friendly state Expand token catalog - (simple data-entry) Deploy our SDK Reach out to merchants, offering free use of our platform Incorporate feedback into redesign Deploy plug-in/app to major no-code marketplace builders Long Term Build a payment system for single-time payments Integrate fiat currency into both ends of our system Cross chain swapping Google Chrome widget for converting crypto into Visa card <div