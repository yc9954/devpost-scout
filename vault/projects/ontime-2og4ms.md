---
slug: "ontime-2og4ms"
url: "https://devpost.com/software/ontime-2og4ms"
title: "onTime"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 983
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/runtime_tool_creation"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# onTime

> Because “I’ll send it later” needed a system. Split later, but onTime.

[Devpost](https://devpost.com/software/ontime-2og4ms) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[runtime_tool_creation]]
**domain** [[developer_tools]] [[finance_payments]] [[housing_homeless]]
**substrate** [[financial_record]] [[geospatial]]

**stack** arcnetwork, ens, react.js, solidity, yellownitrolite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ontime

## Body

Painless payments Inspiration Paying a shared bill upfront and chasing friends for reimbursement is one of those small but persistent social frictions that most people quietly dread. The awkward follow-up texts, the delayed Venmo requests, the unspoken resentment when someone consistently pays late — these moments quietly erode trust between friends and colleagues. Existing split-payment apps make it easy to track who owes what, but they do nothing to actually motivate timely repayment. onTime was built on a simple insight: instead of making it easier to remind people, what if you made it genuinely rewarding to pay on time? What it does onTime is a decentralized bill-splitting app that turns prompt repayment into a rewarding experience. When a group shares an expense — a dinner, a trip, a shared subscription — the person who paid upfront creates a bill on onTime and adds participants using their ENS names. From there, the app handles everything: participants receive instant, gasless payment notifications and are incentivized to settle quickly by earning ARC tokens based on how fast they pay. Pay within an hour and earn 2 ARC; within 24 hours earns 1 ARC; within seven days earns 0.5 ARC. The faster you settle, the more you earn. The result is a system where accountability is built in and awkward follow-ups become unnecessary. How we built it onTime is structured as a three-layer architecture where each layer handles a distinct responsibility, and all three work together to minimize friction for the user. The foundation is Arc Network, an EVM-compatible blockchain where we deployed two Solidity smart contracts. The first, ArcRewardToken, is an ERC-20 contract that mints reward tokens when users make qualifying payments. The second, BillSplit, manages expense creation, tracks participant shares, and computes time-based reward amounts at settlement. Because Arc is fully EVM-compatible, we were able to use standard OpenZeppelin contracts and deploy through Remix without any custom modifications. The middle layer is Yellow Network, integrated via the Nitrolite SDK. This is where the communication happens. When an expense is created, a Nitrolite session opens a WebSocket connection to a ClearNode, and all payment notifications between participants flow through off-chain state channels — completely gasless. Final settlement is the only action recorded on-chain. This reduces what would otherwise be ten or more on-chain transactions per expense down to just two: one to create the bill and one to settle it. The frontend is a React 18 application built with Vite. We used wagmi v2 hooks for UI state management and on-chain interactions, while Nitrolite required direct viem client instances. To bridge the two, we dynamically instantiate viem publicClient and walletClient objects and initialize the NitroliteClient from them, running wagmi and Nitrolite in parallel without conflict. ENS resolution provides human-readable identity throughout the interface, so users add friends by name rather than wallet address. Challenges we ran into The most significant technical challenge was reconciling wagmi and Nitrolite in the same application. wagmi v2 abstracts wallet interactions through React hooks and manages its own internal client state, while Nitrolite expects direct viem client instances to be passed in explicitly. These two models don't naturally compose. We solved this by dynamically creating viem clients that mirror the active wagmi configuration, then using those to initialize the NitroliteClient separately — effectively running both systems in parallel and letting each handle what it does best. Designing the reward logic also required careful thought. The time-based incentive needed to be fair, tamper-resistant, and simple enough that users would immediately understand the stakes. Anchoring reward tiers to block timestamps on Arc and encoding the logic directly in the BillSplit contract ensured that the rules are transparent and enforced without any off-chain dependency. Accomplishments that we're proud of Getting the Yellow Network state channel integration working end-to-end was the technical highlight of the project. The Nitrolite SDK is relatively new, and integrating it into a wagmi-based React application — where the wallet abstraction layers don't naturally align — required us to build a custom bridging approach that hadn't been documented. The fact that expense notifications now flow entirely off-chain, with only two on-chain transactions per full bill lifecycle, is a meaningful reduction in both cost and latency. We're also proud of how cleanly the three layers map onto the user experience. Arc handles trust and incentives, Yellow handles coordination, and ENS handles identity — each doing exactly one job, and none of them visible to the end user as separate systems. What we learned This project gave us hands-on experience with state channel architecture in a real product context, which is meaningfully different from understanding it conceptually. Managing session lifecycles, handling WebSocket connections to ClearNode, and ensuring graceful fallback to on-chain settlement required a level of operational thinking that went beyond smart contract development alone. We also developed a practical understanding of how to bridge competing client models in a single frontend — specifically, how wagmi's hook-based abstraction and viem's imperative client model can coexist without either interfering with the other. That pattern is likely to be useful any time a project needs to integrate an SDK that hasn't been built with wagmi compatibility in mind. What's next for onTime The most immediate priority is expanding the settlement layer to support recurring shared expenses — subscriptions, rent, utilities — where the same group splits costs on a predictable schedule. State channels are particularly well-suited for this, since an open channel between recurring participants would eliminate even the two on-chain transactions currently required per expense cycle. Longer term, we'd like to introduce a reputation layer tied to payment history, making a user's on-time record visible and portable across groups. This would add a social dimension to the incentive system beyond token rewards — making your track record something worth maintaining. We'd also like to explore letting groups pool their ARC rewards collectively, creating a shared balance that could offset future group expenses automatically. <div