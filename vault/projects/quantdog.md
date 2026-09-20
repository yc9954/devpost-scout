---
slug: "quantdog"
url: "https://devpost.com/software/quantdog"
title: "QuantDog"
hackathon: "SpurHacks"
organization: "SPUR & Konfer"
winner: true
words: 247
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
  - "domain/security_privacy"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# QuantDog

> Intelligent quantum threat detection and adaptive cryptographic routing platform that protects cryptocurrency transactions from evolving quantum computer attacks.

[Devpost](https://devpost.com/software/quantdog) · hackathon [[SpurHacks]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[agriculture_food]] [[security_privacy]]
**substrate** [[financial_record]] [[geospatial]]

**stack** fastapi, git, node.js, python, react, typescript, uv, vite, websocket

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned

## Body

Inspiration The looming quantum threat to cryptography motivated us to build a proactive solution. With quantum computers projected to break current encryption within 5-10 years, over $2.25 trillion in cryptocurrency assets face immediate risk, yet 95% of crypto exchanges and wallets remain unprotected. What it does QuantDog is an intelligent quantum threat detection platform that deploys honeypot wallets across blockchains as early warning sensors, monitors threats in real-time, and automatically switches between classical and post-quantum encryption based on threat levels to preserve speed when there is no threat expected. How we built it Frontend : React 19 with TypeScript, TailwindCSS v4, shadcn/ui components, and Three.js for 3D visualizations Backend : Python with FastAPI for high-performance APIs and async operations Real-time Communications : WebSocket connections for live threat monitoring and instant updates Cryptography : Post-quantum cryptography implementation with NIST-compliant algorithms Infrastructure : Docker containerization and Terraform for cloud deployment Network Layer : TUN/TAP interfaces for packet capture and cryptographic routing Challenges we ran into Our biggest challenges included implementing packet interception with TUN/TAP interfaces in Docker, getting post-quantum cryptography KEM working over networks, and deploying complex infrastructure with Terraform while building algorithms to distinguish normal blockchain activity from quantum attacks. What we learned Cryptographic algorithms across all sectors are in serious trouble once quantum computing reaches anticipated levels in 5+ years. We discovered the "harvest now, decrypt later" threat is already real, and there's a massive untapped market opportunity for quantum-safe solutions in the vulnerable crypto space. <div