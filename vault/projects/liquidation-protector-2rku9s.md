---
slug: "liquidation-protector-2rku9s"
url: "https://devpost.com/software/liquidation-protector-2rku9s"
title: "Liquidation Protector"
hackathon: "Evmos Momentum Hackathon led by Web3Scholarships (Deployment required for prize)"
organization: "Huobi"
winner: true
words: 1225
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/runtime_tool_creation"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# Liquidation Protector

> Liquidation Protector is a Knock-In Option protocol. If the underlying asset price hits the barrier, the option token's payoff will be automatically added as collateral to protect the liquidation.

[Devpost](https://devpost.com/software/liquidation-protector-2rku9s) · hackathon [[Evmos Momentum Hackathon led by Web3Scholarships -Deployment required for prize-]]

## Facets

**mechanism** [[runtime_tool_creation]] [[simulation_digital_twin]]
**domain** [[finance_payments]]
**substrate** [[financial_record]]

**stack** awss3/ec2, chai, docker, ethers.js, evmos, hardhat, ipfs, jest, node.js, postgresql, react, redis, solidity, thegraph

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for liquidation protector

## Body

Marketplace Sell the option Lend DAI Inspiration Building leveraged position has been common knowledge as crypto derivatives and DeFi markets grow from 2021. Highly leveraged positions caused a lot of liquidation in the recent bear market, we have witnessed many liquidation cases, and many investors suffered from their losses. A considerable amount of dollars was liquidated every day. It also led to default risk with more extensive market loss and caused a significant decline in the overall market. Nevertheless, the instrument for hedging the liquidation risk is not enough. Therefore, we firmly believe there is a greater market need for liquidation protection instruments and trading infrastructure. So we designed a market with a Knock-In option, where investors can handle the liquidation risk of their leveraged position. Not only the liquidation protector will manage individual investors, but also the systematic risk of the market. What it does Suppose the underlying asset price of Knock-In Option hits the barrier. In that case, the option token's payoff will be automatically added as collateral for the Long (Knock-In Option) Token holders to protect the liquidation of their leveraged position. Various market participants can use the Liquidation Protector. Long Knock-In Option holder (= Buy position) : Investors who want to hedge their liquidation risk. Primarily futures or collateral-based lending users. -Investors want to prepare for an event in which major market players are liquidated. Short Knock-In Option holder (= Sell position) : Investors who do not expect a particular event to occur and want to earn a premium by selling Long Option Tokens. How we built it Option Issuance First, the option issuer issues Long KI Option Token & Short KI Option Token. Then, set parameters for the options. Parameters Issuing Options: Long KI Option Token & Short KI Option Token Underlying Asset: Set the underlying asset. (e.g., ETH) Barrier Price: Specify the price level to trigger the event. Event: Set mark price and barrier price. Maturity: Date of termination of the option. Payoff: Payoff is fixed at 1 underlying asset. The payoff should be deposited at issuance. (e.g., Payoff = 1 ETH) Option Trade Options are ERC20. Buy/sell positions can be traded on OTC. Due to frequent maturities and various products, it would like to be traded in OTC (P2P) rather than AMM. If investors want to close their open positions, they can sellout options in their addresses or offset their positions by buying opposite positions. (e.g., holding the same amount of Long options and Short options with the same barrier price & maturity, the open position is zero.) The quotation in this platform shows the parameters of the KI Option, the model price, and the quote price offered by the seller. Option Termination At the maturity without the event, the option is terminated, and the deposited payoff is claimable for the Short Option holder. Option Settlement The option event is triggered if the mark price crosses the barrier price before maturity. And the deposited payoff is paid to the Long Option holder. Challenges we ran into Implementation of Option Position and Trade Options include long and short positions. Long position is paying a premium to buy the right to exercise the option, and short position is to sell the right for a premium. We adopted a method in which plus and minus tokens are issued together when an option is published. Minus tokens, meaning short position, belong to the option publisher, and plus tokens, meaning long position, are traded in the market. If the underlying asset’s price reaches the barrier price before the option expires, the plus token holders can take the payoff. If the price does not reach the barrier, the minus token holders get the collateral back. Position management using tokens also simplified options trading. Ownership of plus tokens means the right to exercise options. Accordingly, we were able to safely implement option trading in 3 days, which can be complex, through the P2P trading method. Implementation of the Bot Knock-In(KI) option Execution transactions which sent concurrently reverted since new sending transactions have the same nonce as that pending transactions. We sent transactions sequentially. Furthermore, we will have a nonce manager that specifies the nonce in each transaction and make parallel transactions. We needed to retry only failed options when options failed to execute. We created a dead letter queue for KI options that can’t be processed successfully. The bot periodically polls the queue and retries the failed options until they execute successfully. How can we define each user’s KI option balances when we trade the options? We used the Graph to display each user’s option trading from the KI option market contract events. We defined data source templates in a contract subgraph to listen to Transfer events for dynamically created KI option token contracts. Using data source templates, we handled all Transfer events of the token contracts and computed each user’s balances to display in UI. Built a indexer which does not exist yet on the Evmos ecosystem Current product requires the Graph as an on-chain data indexer, but we realized the Graph does not support Evmos while building our product on the Evmos network. Hence, we forked the Graph node to be Evmos compatible, and successfully used the node to build an on-chain indexer for our product. Accomplishments that we're proud of We strongly believe there is a greater market need for liquidation protection instruments and trading these instruments. Not only the liquidation protector will manage individual investors, but also the systematic risk of the market. The leverage position of liquidation is path-dependent. Thus, we choose the KI Option and propose the KI Option Protocol runs with minimum functions. - The model does not clear the liquidity issue, yet, the team will find a solution through further research. Fortunately, various problem-solving methods are proposed and ready to be proven in the market. When our KI Option works as liquidity protection appropriately, it can be integrated with futures and lending protocols as collateral or insurance. What we learned We figured out that the highly leveraged positions had a substantial systematic liquidation risk in the market. Also, there were not enough methods to hedge the risk in that period. So, we believed that if we could propose an appropriate protocol to the market, it would protect many other DeFi protocols, investors, and the market. At this moment, we felt we were developing something important for the Blockchain ecosystem. With the procedure of research, we discovered many financial products and infrastructure in TradFi which are not implemented in DeFi yet. So we get the idea that bringing those existing products and infrastructure to blockchain will make our ecosystem healthier. What's next for Liquidation Protector We describe possible improvements for the next step as we know the following limitations. Liquidity Usually, options markets have liquidity issues due to the various set of option products. So, we plan to develop wrapping and OTC trade for the option positions utilizing Convex-like & Seaport-like functions. Also, we will introduce Option Vault for automatic buy & sell options. Pricing Monte-Carlo Simulation requires huge computing time to calculate the model price for options. We will consider the application of established formulas (such as the Black-Scholes) through specific research on market price decision methodology. Interoperability If Knock-In Option works as protection, it can be used as collateral or insurance in CEX/DeFi using leverage. <div