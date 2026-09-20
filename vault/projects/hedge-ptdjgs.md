---
slug: "hedge-ptdjgs"
url: "https://devpost.com/software/hedge-ptdjgs"
title: "Hedge Finance"
hackathon: "IGNITION | A Global Solana Hackathon"
organization: "Solana Capital"
winner: true
words: 1091
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# Hedge Finance

> Hedge leverages Solana's speed to enable 0% interest, low collateral ratio borrowing against SOL. It features a yield generating pool that performs best in down or neutral market conditions.

[Devpost](https://devpost.com/software/hedge-ptdjgs) · hackathon [[IGNITION - A Global Solana Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[education]] [[finance_payments]]
**substrate** [[financial_record]]

**stack** anchor, nextjs, react, rust, vercel

## How they structured the write-up

- inspiration
- hedge product offering
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hedge

## Body

How to use Hedge. A yield product that does best in choppy markets Two complementary products Check us out at https://hedge.sh Inspiration The crypto ecosystem is full of stablecoin lending products with variable interest rates and high or variable maintenance collateral ratios (e.g. MakerDAO changes stability fees and another protocol called Liquity will start liquidating vaults below 150% in case of system insolvency) - meaning one must closely track their loan position. In parallel, most yield products perform best in up markets, so there is still a lot of space for products that perform best in neutral or down markets that investors could use to hedge their long positions. We saw Solana's speed as a core aspect that could help us solve both these issues at once by having lightning speed liquidations to enable low collateral ratios & give people a yield in down or neutral market conditions. Hedge product offering Hedge's initial offering consists of 2, complementary, innovative products: A 0% lending stablecoin product (initially only with SOL collateral), with a low collateral ratio option A yield pool that performs best in down or volatile market conditions Hence the name Hedge since we offer a pool that gives investors better returns in a down market. How we built it We built Hedge with multiple components: a lending vault system that tracks every user's loan amounts and locks up their collateral. Users are offered a range of maintenance collateral ratios (MCR) to give them a predictable liquidation price. The lower the MCR, the higher the one time fee. a liquidation pool that guarantees the protocol has instant access to capital to liquidate risky vaults. This is one of the core differentiators of our protocol since others, such as MakerDAO, have a lengthy auction process and cannot guarantee they have enough DAI on hand to liquidate users instantly. Since this pool is liquidating user vaults, it performs best in a down or neutral market. a stablecoin redemption function that guarantees anyone can redeem our stablecoin, the USDH , against its value in SOL. This creates an arbitrage opportunity in case someone sees USDH trading at below $1 to guarantee that USDH will have a $1 price floor. Technically, we spent some time deciding what to use and ended up with: using Anchor since it greatly improved development speed using Switchboard since was already live on mainnet and we liked its straightforward design. We're also using Chainlink in devnet that we will use in mainnet once that goes live. use Mocha for tests since we needed to ensure to cover all attack surfaces which is essential when holding user funds as collateral (e.g. ensure only vault owner can take out their SOL , have a system that is able to quickly liquidate) using React in the font-end client. Our client (hosted on Vercel) uses account listeners whenever possible to give users real-time updates to on-chain data. This means there's virtually zero lag between data changing on the Solana blockchain and what the user sees. This is something that's only possible on Solana. Challenges we ran into Challenges we ran into included: The lack of a good way to test our system at scale to simulate various kind of attacks (like users trying to open tiny vaults) or stress test for situations such as a price crash. Instead we had to design our system to be more conservative (high liquidation ratios) than we originally wanted. We'll make these tools ourselves before releasing on mainnet. The ecosystem for oracles on Solana is not completely ready. Switchboard and Pyth are both very new and have some integration issues. Chainlink is not yet live on mainnet and their current SOL / USD price feed has been stuck for the last 2 months at $141. Coding for Solana. Since Solana requires us to pass in all the accounts that will be touched prior to the transaction being called there are a few things we need to do differently than we would on Ethereum, such as pre-computing the accounts we will need info from. It also makes it a bit harder (but not impossible) to maintain ordered linked lists. Accomplishments that we're proud of Implementing variable staking. The staking formula is pretty well known at this point, but we had to deal with a staking amount that decreases over time. This involved some custom work to implement on Solana and as far as we know, there is no precedent of this being implemented on Solana yet. Ensuring our stablecoin is actually stable. Most stablecoins are badly implemented because they can temporarily lose their peg and drop in value. We were proud to have implemented an arbitrage opportunity that would allow this peg to be maintained. A clean site design. It was important to both of us that Hedge has a clean and easy-to-use interface that made it easy and clear for users to leverage their Solana position. What we learned Neither of us had written any Rust code prior to starting this project. We learned that we love Rust :) Anchor removes a lot of the effort of serialization and deserialization of account data in Rust. This allowed us to move faster and skip over the low-level Rust coding challenges as a newbie to the language. Anchor also provides a quick IDL to use in JavaScript for additional speed of development. The Solana/Anchor community is super helpful on channels like Discord. Thanks for the support everyone! What's next for Hedge We have a few areas we want to focus on once we've built the initial version of Hedge: Do the basic homework for any crypto launch: get security audit, build community and kickstart a liquidity program to launch on mainnet Build more fallbacks to ensure we can always maintain system solvency (i.e. maintain a total collateral ratio above 150%). Both in terms of diversifying oracles to ensure we always have the most accurate price and implement more systems to burn USDH should our collateral suffer (such as debt distribution). These should only be distress measures but are required if our system is to be trustworthy. Once we understand the system solvency better, introduce even more competitive collateral ratios (e.g. could we offer as low as 105%?). This combined with better USDH liquidity means that we could offer up to 20x leveraged vaults. Make it easy for other Solana apps (such as wallets or crypto dashboards) to offer 0% interest loans by giving them a revshare Introduce more collateral options such as staked SOL (loans that pay themselves back!) <div