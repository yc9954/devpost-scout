---
slug: "ua-sdk-universal-account-abstraction-sdk-for-starknet"
url: "https://devpost.com/software/ua-sdk-universal-account-abstraction-sdk-for-starknet"
title: "UA²-SDK — Universal Account Abstraction SDK for Starknet"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 590
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/developer_tools"
  - "substrate/financial_record"
---

# UA²-SDK — Universal Account Abstraction SDK for Starknet

> One SDK for Starknet AA. Create scoped session keys, recover with guardians, run gas-sponsored calls via paymasters, and integrate with any wallet.

[Devpost](https://devpost.com/software/ua-sdk-universal-account-abstraction-sdk-for-starknet) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[developer_tools]]
**substrate** [[financial_record]]

**stack** cairo, starknet, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges
- what i learned
- accomplishments
- what is next

## Body

Inspiration Starknet gives everyone account abstraction by default, but the practical features that teams want are scattered across wallet UX, blog posts, and one off SDKs. I wanted a single toolkit that lets any dApp use session keys, guardian recovery, safe key rotation, and sponsored transactions without re inventing the wheel. That became UA² SDK. What it does UA² is a wallet agnostic toolkit for Starknet. It ships a modular Cairo account plus a TypeScript SDK so apps can create scoped session keys, enable m of n guardians for social recovery, rotate ownership keys safely, and use paymaster adapters for sponsored or alt token gas. The goal is to make these account abstraction features usable today by any dApp, game, or protocol. These capabilities and the overall layout are described in the repo readme and docs, including the quickstart, architecture notes, and the demo flow that shows create session, sponsored call, and revoke steps. How I built it I started by defining a minimal on chain account that composes with OpenZeppelin’s AccountComponent. I split features into modules: SessionKeys, Guardians, and KeyRotation. Off chain, I built @ua2/core for low level calls, @ua2/react for app hooks, and a small paymaster adapter layer. The repo includes a demo script that connects a wallet, creates a session with a transfer cap, performs calls through the session key without wallet popups, tries a policy violation to show a revert, then uses a sponsor to cover gas, and finally revokes the session to confirm denial. The readme and docs include quickstart commands, a Sepolia runbook, a security overview, and links to the validation and test plan. Challenges Policy design for session keys. I needed policies that are expressive enough for real apps but still simple to validate. The current model includes hard expiries, call whitelists, and per call or per value caps. The security section also highlights domain separated signatures and event coverage for every state change. Guardians and recovery flow. Balancing safety and usability required a quorum setting and a timelock so owners have time to react before a takeover completes. Sponsored transactions. Different providers use different payloads and assumptions. I wrapped this behind a small adapter so the app code does not care which paymaster is used. Tooling on an aggressive timeline. I leaned on typed SDK code, a focused test plan, and end to end scripts for both local devnet and Sepolia to keep iteration tight. The readme lists the test commands for Cairo unit tests, TypeScript unit tests, and e2e flows. What I learned Account abstraction features are powerful, but they only shine when they are easy to integrate. A small number of well named APIs beats a kitchen sink. Putting the policy model in writing early also made the demo and tests more convincing because it gave me objective checks for expected reverts and success cases. Finally, a good runbook matters. Clear steps for environment configuration and deployment made testing on Sepolia much less painful. Accomplishments A working modular UA² account with session keys, guardians, key rotation, and paymaster adapters A demo app and CLI that exercise the full lifecycle from create session to revoke, including a sponsored call path A documentation set that covers architecture, validation rules, security assumptions, runbook, and test plan, all linked from the readme ([GitHub][1]) What is next Broader paymaster coverage for common providers More policy shapes for session keys, including simple rate limits for specific methods Additional example integrations so teams can copy and adapt quickly Hardening and audits as the feature set stabilizes <div