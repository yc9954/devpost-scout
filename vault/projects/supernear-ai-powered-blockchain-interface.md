---
slug: "supernear-ai-powered-blockchain-interface"
url: "https://devpost.com/software/supernear-ai-powered-blockchain-interface"
title: "SuperNear | AI-powered Blockchain Interface"
hackathon: "[REDACTED] Hackathon"
organization: "NEAR Protocol"
winner: true
words: 309
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/labor_employment"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# SuperNear | AI-powered Blockchain Interface

> Use natural language to interact with Near Blockchain in an easy, user-friendly, expandable way.

[Devpost](https://devpost.com/software/supernear-ai-powered-blockchain-interface) · hackathon [[-REDACTED- Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[labor_employment]]
**substrate** [[financial_record]] [[structured_db]]

**stack** ai, blockchain, cloudflare, llm, near, nextjs, vector

## How they structured the write-up

- inspiration
- what it does
- how we built it
- business model
- what's near for supernear?

## Body

GIF Inspiration I didn’t have one specific inspiration—just the idea that writing transactions in natural language could be quicker and more efficient than using a command line or a complex tool. Plus, I realized it would make blockchain accessible to non-technical people who’d love the simplicity of a chat interface. What it does SuperNear is a powerful chat interface that transforms user commands into real actions on the Near Blockchain . Users simply type their instructions in natural language, and SuperNear translates these into blockchain transactions. By removing barriers, SuperNear makes decentralized finance, asset management, and smart contract interactions intuitive and accessible. It’s a frictionless solution that bridges the gap between users, AI and blockchain functionality, empowering everyone to leverage blockchain technology easily and securely. How we built it Frontend : Nextjs. API/Server : Cloudflare Workers with HonoJs. Auth : JWT provided if user sign a message + nonce using his wallet. Subscription Management : Smart Contract deployed at premium.super_near.near. Intent Recognition : Embedding Model + Vector database. Parameters Extraction : LLM (Mistral 8b). Business model SuperNear follows a freemium model: users can access it for free, with a limit of 20 messages per day. For higher usage, there’s a Pro Plan available at 5 NEAR per month, offering expanded access and features. What's Near For SuperNear? Unfortunately, I wasn’t able to complete everything I had envisioned for SuperNear during the hackathon, but the next steps are clear. I want to expand SuperNear’s capabilities, allowing it to handle more actions and enabling users to create custom actions. The goal is to refine the platform, introduce new "sparks," and give users the ability to create their own sparks—then gather feedback and evolve from there. If SuperNear gains traction, I’d also love to integrate with the innovations at app.near.ai and the Bitte.ai wallet, both of which are doing fantastic work. <div