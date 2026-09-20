---
slug: "gostables"
url: "https://devpost.com/software/gostables"
title: "goStables"
hackathon: "TRON Grand Hackathon - Season 3"
organization: "TRON DAO"
winner: true
words: 816
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# goStables

> Decentralized Stablecoins For The Caribbean

[Devpost](https://devpost.com/software/gostables) · hackathon [[TRON Grand Hackathon - Season 3]]

## Facets

**mechanism** [[on_device_local]] [[simulation_digital_twin]]
**domain** [[finance_payments]]
**substrate** [[financial_record]] [[video_visual]]

**stack** bootstrap, exchangerate.host, javascript, netlify, plox.host, react, solidity, tron

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gostables

## Body

Landing Swap Vaults Wallet Inspiration We desired to enable new business models and opportunities for many on Tron through the creation of decentralized, collateral backed stablecoins for countries within the Caribbean. The result is The goStables Protocol, which enables anyone to mint, trade and earn from gStables which are a collection of USDD backed, Caribbean stablecoins pegged to their real world exchange rates using price oracles. There are many in the Caribbean region experiencing difficulties to access foreign currencies due to foreign banking de-risking policies and other FX issues. However, using gStables pegged to the real world, allows anyone holding that gStable to redeem that USDD anytime at the market rate. The existence of such locally pegged stablecoins can also facilitate greater blockchain user onboarding, by bridging the gap between digital currencies, national/cultural familiarity and context. While CBDCs may expand further within the region in the near future, there is still a need Now, for decentralized stablecoins as they can provide many, with options for economic growth and inclusion. This can enable greater propensity fueling an innovation and adoption wave on publicly accessible blockchains. Tron Blockchain, known for its speed and very cost effective transactions is already home to many US dollar pegged stablecoins. The introduction of USDD enabled a means for us to ideate/develop solutions like goStables Protocol on top of this over-collateralized stable asset (USDD). What it does The protocol has 3 core features for users: Swap - Users can swap USDD to mint a variety of supported gStables with more options in the future. Swap them back at anytime to USDD at real world market rates. The latter action burns the gStable. Vaults - Users can stake USDD in vaults to support their favourite gStable to proportionally earn 40% of protocol fees. Deposits are frozen for 72 hours and can be un-staked anytime after. Wallet - Users can view their gStable and Vault balances as well as claim gStable Vault rewards every week. The protocol has 2 core means of generating revenue while strengthening its USDD collateral reserve over time: Protocol Fees: There is a fee of 0.3% in USDD per swap. 40% of this is distributed in gStables to Vault users every week. JustLend: USDD received via Swap and Vaults are supplied via their respective smart contracts, to JustLend’s USDD Market. 70% yields generated are provisioned to the goStables swap to increase collateral beyond 100% to cover more USDD redemptions during possible exchange rate fluctuations due to real world market forces. Additional strategies will be employed in the future. How we built it Reactjs and Bootstrap with customizations for frontend. The off-chain price data is currently fetched via Exchangerate.host's API by our custom built nodes which automatically broadcasts the current market rate directly on-chain, to the relevant gStable Swap contracts. Currently, this occurs every 60 seconds. If the rate has changed the contracts are updated. As there was no official instance of JustLend on Nile, we created a mock contract that replicated the core mainnet USDD market contract functions to simulate the supply/withdraw from JustLend. . We also created a mock USDD token contract for the faucet which has no mint limit. Other projects can use this for building new stuff on Nile. Challenges we ran into Getting up to speed on how to buidl dapps on Tron. We wanted to build a fully integrated unified wallet/dashboard-like experience but the number of contract calls would cause some slow down to the UX. We managed to speed it up a bit but there needs to be more datapoints displayed in the future. So we decided to stick with the simple wallet in the screenshot for now till better infrastructure exists to support this. See our TronDAO forum post for an idea of what the dashboard is shaping up to be like. Accomplishments that we're proud of Translating an abstract idea into a simple usable MVP on Tron blockchain that enables everyone to use and benefit. Building a protocol that can serve as a foundational "Lego" block in Tron's growing DeFi Infrastructure and expanding decentralized stablecoins beyond USD. As far as we can tell, we'll be the first to bring real world currency data on-chain on Tron. We can spin off our oracle tech into a separate product offering to service other projects that require more on-chain data from off-chain sources, broadcasted to their contracts/dapps. It's nice to see Caribbean currencies being represented on a public blockchain. What we learned How to build on Tron blockchain. The strengths, current weaknesses and opportunities of building on Tron blockchain. How to bring real world data on-chain. What's next for goStables Mainnet Launch (gTTD, gXCD, gBBD, gJMD...) - Q1 2023 Dashboard UI - View gStable info on one page - Q1 2023 Integrating gStables with existing projects - Q1 2023 Building and promoting new products/use cases for gStables - Q2 2023 Protocol governance - Q2 2023 <div