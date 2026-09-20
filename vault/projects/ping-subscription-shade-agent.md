---
slug: "ping-subscription-shade-agent"
url: "https://devpost.com/software/ping-subscription-shade-agent"
title: "Ping Subscription Shade Agent"
hackathon: "One Trillion Agents Hackathon"
organization: "NEAR Protocol"
winner: true
words: 437
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "user/patient_family"
  - "user/small_business"
  - "substrate/financial_record"
---

# Ping Subscription Shade Agent

> Secure, automated subscription payments without requiring users to pre-fund accounts or approve unlimited spending.

[Devpost](https://devpost.com/software/ping-subscription-shade-agent) · hackathon [[One Trillion Agents Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]] [[retail_commerce]]
**user** [[patient_family]] [[small_business]]
**substrate** [[financial_record]]

**stack** css, javascript, phalacloud, rust, shadeagent, typescript

## How they structured the write-up

- inspiration
- what it does
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ping subscription shade agent

## Body

Inspiration Pingpay aims to simplify merchant onboarding and enable seamless, low-cost payments across any blockchain using chain signatures and intents. This submission focuses on improving crypto subscriptions by addressing the current limitations in existing approaches. Most blockchain networks are designed primarily for one-time payments rather than recurring transactions. Unlike traditional banking systems, which offer built-in "pull payment" mechanisms such as credit card auto-debits, blockchain lacks a native solution for automated payments. In the current crypto subscription model, customers receive email reminders at the end of each subscription period, prompting them to manually renew. Alternatively, they must pre-approve and pay for a set duration upfront—an inconvenient process for managing subscriptions. For merchants, this creates uncertainty, as there is no guarantee of timely or consistent payments. Since users must manually confirm each renewal, merchants risk missed or delayed transactions. What it does The system enables secure, automated recurring payments without requiring users to pre-fund accounts or approve unlimited spending. It has a NEAR smart contract that manages: Subscription creation and management Payment processing Access key registration and verification Merchant relationships It has a Worker Agent running in a TEE on Phala Cloud that: Monitors subscriptions for due payments Securely stores private keys Signs and submits payment transactions Handles payment failures and retries A web application that allows users to: Create and manage subscriptions View payment history Pause or cancel subscriptions Challenges we ran into We had issues deploying a custom shade agent contract, in addition to redeploying the existing one. This meant for a time we were unable to cargo near build and deploy this or a fresh agent template repo, and so our custom contract code has not be deployed or is able to be used at this time. Accomplishments that we're proud of Creating automated subscriptions for NEAR transactions, which use NEAR's Function Call Access Keys and Shade Agents running in Trusted Execution Environments (TEEs). Building a frontend for an example merchant using an SDK for communcaiting directly to the TEE. What we learned The subscription/reoccurring payment framework can be reapplied to multiple different use cases such as crypto savings accounts or reoccurring payments to a friend or family member. What's next for Ping Subscription Shade Agent The integration of the subscription service into the full Pingpay platform for an upcoming launch of the projects beta launch. Allowing teams/individuals to offer subscriptions for their goods/services. Implement NEAR Chain Signatures and use NEAR Intents to allow subscriptions to be made from multiple blockchains/tokens. Use the reoccurring payments to allow for additional use cases such as crypto savings accounts or reoccurring payments to a friend or family member. <div