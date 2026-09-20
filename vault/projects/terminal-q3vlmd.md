---
slug: "terminal-q3vlmd"
url: "https://devpost.com/software/terminal-q3vlmd"
title: "TradeOff"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 710
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "substrate/financial_record"
---

# TradeOff

> TradeOff converts traditional investors into dedicated Polymarket users by giving them the relevant market information needed to invest with prediction markets.

[Devpost](https://devpost.com/software/terminal-q3vlmd) · hackathon [[NexHacks]]

## Facets

**mechanism** [[realtime_stream]] [[structural_withholding]]
**domain** [[developer_tools]]
**substrate** [[financial_record]]

**stack** groq, next.js, polymarket, react, shadcn, tailwind, typescript, vercel, woodwide, woodwideai, yahoo-finance

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tradeoff

## Body

Portfolio tab Hedges tab Wood Wide overview on hedge Risks tab News tab Greeks tab - upper Greeks tab - lower Inspiration I called my mom the moment I got to Pittsburgh and told her I wanted to build something for Polymarket. She had no idea what I was talking about. My mom has thousands invested in stocks but hasn't even heard of the world's largest prediction market. I realized that there are millions like her, traditional investors who aren't even aware of prediction markets as an option. We decided to build a platform to help bridge this gap. TradeOff allows traditional investors to begin trading on Polymarket without changing their techniques too much, giving them a steady introduction to the new market. What it does TradeOff allows traditional investors to connect their brokerage accounts and instantly see how to hedge their real-world risks using prediction markets. But I know my mother, and I know she doesn't trust most traditional stock advice. She needs a rigorous mathematical analysis before making a firm decision on a transaction. Luckily, Wood Wide AI allows us to mathematically analyze their portfolio vectors, detecting specific anomalies like sector over-concentration or excessive volatility. Based on these numeric hard facts, we recommend specific PolyMarket contracts to offset those risks. We pair this with real-time news and "Cost of Protection" calculators, converting complex financial hedging into a simple, data-backed strategy that anyone generally understands. How we built it We built TradeOff using Next.js 14 and shadcn/ui for a clean, terminal-inspired interface. The core intelligence is a dual-engine implementation: Groq (Llama-3) handles the semantic understanding of news and user intent, while Wood Wide AI serves as our numeric reasoning brain. We pipe portfolio datasets directly into Wood Wide’s anomaly detection models to identify risk factors that text-based LLMs simply cannot see. Integrating two different AI paradigms, textual and numeric, was key to making the system reliable. Challenges we ran into Integrating a cutting-edge numeric inference engine like Wood Wide AI came with a learning curve. LLM's are forgiving, they understand us as long as we ask valid english sentences. Numeric models demand precision. We battled through rigid data schema requirements, debugging tensor shape mismatches, and 400/422 payload errors until we perfected the "handshake" between our user's raw portfolio data and Wood Wide's training endpoints. It wasn't enough to just send data; we had to ensure the mathematical representation of "risk" was accurate. It was frustrating, but it resulted in a statistical model that is unable to fail, which is so much stronger than a typical LLM pipeline which could easily hallucinate. Accomplishments that we're proud of We’re incredibly proud of the Wood Wide Integration. We built a genuine numeric profiling system that runs in the background for every user, and it feels so much better than building a simple wrapper. Seeing that first successful anomaly detection score come back, confirming that our logic about "tech sector exposure" was mathematically sound, was a huge moment. We successfully bridged the gap between "mom's stock portfolio" and "crypto prediction markets" without overwhelming the user. What we learned We learned that the biggest barrier to adoption is trust, and trust comes from verification. Users (our collective parents) were skeptical of generic advice, but when we showed them why a hedge was suggested based on Wood Wide’s numeric risk score, the conversation changed. We also learned that numeric reasoning is the missing link in FinTech AI; LLMs are great at explaining what happened, but you need systems like Wood Wide to understand how much it matters. What's next for TradeOff We envision TradeOff becoming a fully autonomous hedging agent. The next leap is Automated Execution via AA (Account Abstraction), allowing users to deposit funds into a smart contract vault that automatically buys and sells prediction market positions as their stock portfolio shifts, maintaining a perfect "delta-neutral" hedge without manual intervention. We also want to implement Cross-Chain Collateralization, where users could pledge their actual stock assets (via tokenized securities) as collateral to mint stablecoins for betting on Polymarket, making the hedging process capital-efficient. Finally, we plan to build a "Hedge Fund Social Layer" where successful hedging strategies are tokenized and shareable, allowing retail investors to copy the risk management profiles of top-performing institutional-grade portfolios. <div