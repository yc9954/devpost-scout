---
slug: "nexora-the-autonomous-payroll-protocol"
url: "https://devpost.com/software/nexora-the-autonomous-payroll-protocol"
title: "Nexora - The Autonomous Payroll Protocol"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 824
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/revocation_withdrawal"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "substrate/financial_record"
---

# Nexora - The Autonomous Payroll Protocol

> Nexora is an AI-powered treasury that streams payroll per second on-chain while monitoring risk, forecasting cashflow, and automating payroll infrastructure.

[Devpost](https://devpost.com/software/nexora-the-autonomous-payroll-protocol) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[revocation_withdrawal]] [[simulation_digital_twin]]
**domain** [[finance_payments]] [[labor_employment]]
**substrate** [[financial_record]]

**stack** framer-motion, google-gemini-api, hardhat, next.js-14, node.js, rainbowkit, recharts, solidity, somnia-testnet, tailwind-css, typescript, viem, wagmi-v2

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nexora - the autonomous payroll protocol

## Body

Creating a real-time payroll stream where funds flow per second to a worker directly from the employer’s wallet. Worker dashboard showing live payment streams and instantly withdrawable earnings from active payroll flows. Nexora Treasury dashboard displaying real-time balances, active streams, AI treasury insights, and protocol statistics. AI-powered treasury analytics forecasting cashflow and visualizing payroll distribution across stream types. AI-driven risk monitoring system analyzing payroll streams and flagging potential anomalies before transactions execute. Inspiration Modern teams are global, decentralized, and operate continuously — but payroll infrastructure has not evolved to match this reality. Most payroll systems remain batch-based, opaque, and disconnected from real-time treasury visibility. Web3 organizations in particular lack native infrastructure for continuous payroll distribution, treasury intelligence, and proactive financial risk monitoring. Nexora Treasury was inspired by a simple idea: money itself should be programmable. Instead of sending salaries once a month, payroll should flow continuously — transparently, securely, and directly on-chain — while intelligent systems monitor treasury health and financial risk in real time. What it does Nexora Treasury is an AI-powered programmable payroll infrastructure built on the Somnia Testnet. It introduces continuous on-chain payroll streaming, where funds flow per second directly to employee wallets once a single transaction is confirmed. What it does Nexora Treasury is an AI-powered programmable payroll infrastructure built on the Somnia Testnet. It introduces continuous on-chain payroll streaming, where funds flow per second directly to employee wallets once a single transaction is confirmed. Key capabilities include: Per-second payroll streaming executed fully on-chain Multi-wallet group payroll with automatic equal distribution Real-time treasury dashboard showing live balances and payment flows AI-powered fraud risk analysis before stream execution Natural language payroll creation using an NLP stream parser 30-day treasury cashflow forecasting powered by AI Autonomous keeper agent maintaining protocol efficiency Reusable payroll templates generated from historical streams Unlike most hackathon projects, Nexora executes real blockchain transactions — not simulated backend logic. Once a payroll stream is created, funds begin continuously streaming to recipients in real time. This transforms payroll from a periodic payment process into programmable financial infrastructure. How we built it Nexora is built using a three-layer architecture designed for modular, production-grade infrastructure. Smart Contract Layer (Solidity + Hardhat) The on-chain layer implements Nexora’s programmable payroll engine. Core Payroll Engine Handles fund custody, streaming calculations, withdrawals, and batch updates. Template Engine Enables reusable payroll configurations and automated stream creation. Keeper Engine Maintains protocol efficiency by batching stream updates when economically profitable. The streaming mechanism calculates real-time accrued balances based on flow rate and elapsed time, enabling continuous fund distribution. Frontend Layer (Next.js 14 + Wagmi + Viem) The user interface connects directly to on-chain state. Key components include: Wallet connection via RainbowKit Live treasury dashboard with incoming/outgoing streams Real-time visualization of payment flows Fraud risk monitoring interface Analytics dashboards for runway and burn rate All UI components react directly to live blockchain data. Intelligence Layer (Google Gemini + Custom Heuristics) Nexora integrates multiple AI agents to transform payroll into an intelligent treasury system. NLP Stream Parser Converts natural language payroll instructions into structured stream parameters. Fraud Risk Analyzer Evaluates transactions using wallet history, behavioral heuristics, and Gemini contextual analysis. Treasury Optimization Agent Analyzes active payroll streams and generates financial efficiency recommendations. Cashflow Predictor Generates 30-day treasury forecasts and runway projections. Autonomous Keeper Agent Runs continuously to optimize stream updates and maintain protocol health. Together these agents enable automated treasury intelligence layered on top of on-chain finance. Challenges we ran into Designing a payroll streaming mechanism that remains gas-efficient while supporting multiple recipients required careful contract architecture. Synchronizing continuously updating on-chain payment flows with a reactive frontend interface also introduced significant complexity. Another challenge was combining deterministic financial heuristics with AI-driven contextual analysis without compromising reliability. Finally, ensuring the autonomous keeper system operates independently from the frontend required designing a robust background execution process. Accomplishments that we're proud of Fully operational per-second on-chain payroll streaming Atomic multi-wallet payroll distribution Real-time blockchain-powered treasury dashboard AI-powered fraud detection and treasury forecasting Autonomous keeper system for protocol optimization Modular architecture separating contracts, UI, and intelligence layers Most importantly, Nexora is not a UI prototype — it is functional financial infrastructure running on-chain. What we learned Building real-time financial primitives requires tight integration between smart contract logic and reactive frontend design. We also learned that AI is most powerful when combined with deterministic financial rules rather than used alone. Treasury management in decentralized organizations is not just about sending payments — it requires continuous visibility, forecasting, and risk monitoring. What's next for Nexora - The Autonomous Payroll Protocol Our vision is to evolve Nexora into the programmable treasury backbone for decentralized organizations. Planned future capabilities include: Variable-rate and milestone-based payroll streams DAO-governed payroll approval workflows Cross-chain treasury management Advanced anomaly detection using historical on-chain behavior Production-grade keeper infrastructure Stablecoin-native payroll support As teams become increasingly decentralized, financial infrastructure must evolve beyond static payments. Nexora aims to power the next generation of autonomous financial operations. <div