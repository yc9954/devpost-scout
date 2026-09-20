---
slug: "flowpay-5mefh4"
url: "https://devpost.com/software/flowpay-5mefh4"
title: "Flowpay"
hackathon: "MNEE Hackathon: Programmable Money for Agents, Commerce, and Automated Finance"
organization: "MNEE, LLC"
winner: true
words: 776
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "mechanism/revocation_withdrawal"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Flowpay

> We extend the x402 protocol with payment streaming for AI agents. Agents can automatically negotiate payments when they hit a paywall; money flows like a utility meter while services are consumed.

[Devpost](https://devpost.com/software/flowpay-5mefh4) · hackathon [[MNEE Hackathon- Programmable Money for Agents- Commerce- and Automated Finance]]

## Facets

**mechanism** [[human_in_the_loop]] [[realtime_stream]] [[revocation_withdrawal]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[financial_record]] [[web_dom]]

**stack** express.js, hardhat, react, solidity, vite

## How they structured the write-up

- inspiration
- what it does
- live demo & deployments
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for flowpay
- built with

## Body

dashboard FlowPay Inspiration Ethereum gas fees are brutal. A single transaction can cost $5-50+ depending on network congestion. Now imagine an AI agent that needs to make 1,000 API calls to a paid service — that's potentially $50,000 in gas fees alone just to pay for the service. This is the N+1 payment problem: every API request requiring its own blockchain transaction. It's not just expensive — it's fundamentally broken for the age of autonomous AI agents. We looked at the x402 protocol (HTTP 402 "Payment Required") and asked: what if we could batch hundreds of payments into a single transaction? What it does FlowPay turns the payment model upside down. Instead of paying per-request, agents open a payment stream — a single on-chain transaction that authorizes continuous value transfer over time. The math is simple: Traditional : 100 API calls = 100 transactions = ~$500 in gas FlowPay : 100 API calls = 2 transactions (open + close) = ~$10 in gas That's 98% gas savings. How it works: Agent hits a paywall (HTTP 402 response) SDK automatically negotiates and opens a MNEE token stream (1 transaction) Agent makes unlimited requests against that stream (0 transactions) Stream closes when done, unused funds refund automatically (1 transaction) Key features: x402 Protocol Integration : Automatic payment negotiation when agents encounter paywalls Real-time Streaming : Money flows like a utility meter — pay only for what you consume AI-Powered Optimization : Gemini AI decides whether streaming or direct payment is more cost-effective Human Oversight : Dashboard with real-time spending visibility and emergency stop controls Automatic Refunds : Unused stream funds return to the agent when the stream closes Live Demo & Deployments 🌐 Live Dashboard : flowpay-dashboard.netlify.app 📜 Smart Contracts on Sepolia : Contract Address Etherscan FlowPayStream 0x155A00fBE3D290a8935ca4Bf5244283685Bb0035 View MockMNEE Token 0x96B1FE54Ee89811f46ecE4a347950E0D682D3896 View 💻 GitHub : github.com/ola-893/flowpay How we built it Smart Contracts (Solidity on Ethereum) FlowPayStream.sol : Core streaming logic — stream creation, real-time balance calculation, withdrawals, cancellations MockMNEE.sol : Test ERC-20 token for Sepolia deployment Deployed to Sepolia testnet, designed for Ethereum mainnet with real MNEE tokens SDK (TypeScript) FlowPaySDK : Handles x402 negotiation, token approvals, stream lifecycle GeminiPaymentBrain : AI engine that optimizes payment strategy based on expected usage SpendingMonitor : Safety limits and anomaly detection Server Middleware (Node.js/Express) x402-compliant middleware that validates payment streams on-chain before serving protected content Frontend (React/Vite) Real-time dashboard for monitoring agent activity Stream balance visualization Manual controls for stream management Architecture: Agent → API Request → 402 Response → SDK Negotiates → Open Stream (1 tx) → Unlimited Requests (0 tx) → Close Stream (1 tx) → Refund Unused Challenges we ran into Gas Optimization Pressure : Every byte of calldata costs gas on Ethereum. We obsessed over minimizing on-chain storage and computation. Real-time Balance Math : Computing claimable balances based on elapsed time required precise BigInt arithmetic — rounding errors at scale would mean lost funds. RPC Reliability : Public RPCs are flaky. We implemented fallback endpoints and graceful timeout handling. Gemini Models : We ran out of credits for the gemini-3-pro model mid-hackathon. So we pivoted to gemini-1.5-flash with fallback heuristics. Stream Header Design : The x402 headers needed to distinguish between token address and payment recipient — we carefully designed the header schema to avoid ambiguity. Accomplishments we're proud of 98% Gas Reduction : From 100 transactions to 2. The savings are real and verifiable on-chain. Working on Real Blockchain : Not mocks — actual MNEE token streams on Ethereum Sepolia. See our contracts live. Full Stack Integration : Smart contracts, SDK, middleware, and frontend all working together seamlessly. AI-Powered Decisions : Gemini analyses usage patterns to choose the optimal payment strategy. Developer-Friendly : One line of code: sdk.makeRequest(url) handles everything. What we learned HTTP 402 is underutilized : It's the perfect handshake for machine-to-machine payments. Streaming beats per-request : For high-frequency interactions, the gas savings are transformative. AI agents need guardrails : Spending limits, emergency stops, and human oversight aren't optional — they're essential. Ethereum gas is the real enemy : Building for gas efficiency changes every design decision. What's next for FlowPay Ethereum Mainnet : Deploy with real MNEE tokens ( 0x8ccedbAe4916b79da7F3F612EfB2EB93A2bFD6cF ) Multi-token Support : USDC, USDT, and other ERC-20 tokens Predictive Streaming : AI that pre-sizes streams based on historical usage Agent-to-Agent Payments : Agents paying each other directly, no human in the loop L2 Integration : Even cheaper streams on Arbitrum, Optimism, Base Built With Blockchain : Solidity, Hardhat, Ethers.js, Ethereum (Sepolia Testnet) Backend : Node.js, Express, TypeScript Frontend : React, Vite, TailwindCSS AI : Google Gemini API Tokens : MNEE (ERC-20 stablecoin) Protocol : x402 (HTTP 402 Payment Required) <div