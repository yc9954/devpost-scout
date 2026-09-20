---
slug: "1-sec-open-source-security-nq9gmk"
url: "https://devpost.com/software/1-sec-open-source-security-nq9gmk"
title: "1-SEC Open Source Security"
hackathon: "Authorized to Act: Auth0 for AI Agents"
organization: "Okta"
winner: true
words: 1047
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/revocation_withdrawal"
  - "mechanism/structural_withholding"
  - "domain/housing_homeless"
  - "domain/security_privacy"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# 1-SEC Open Source Security

> Handing off raw OAuth tokens is a security nightmare. Here's how Auth0 Token Vault and 1-SEC's AI Containment module work together to enable secure, revocable token delegation for autonomous agents.

[Devpost](https://devpost.com/software/1-sec-open-source-security-nq9gmk) · hackathon [[Authorized to Act- Auth0 for AI Agents]]

## Facets

**mechanism** [[on_device_local]] [[provenance_signing]] [[realtime_stream]] [[revocation_withdrawal]] [[structural_withholding]]
**domain** [[housing_homeless]] [[security_privacy]]
**substrate** [[geospatial]] [[structured_db]]

**stack** anthropic, gemini, go, rust, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for 1-sec open source security

## Body

Inspiration AI agents are escaping the sandbox. With sovereign AI like OpenClaw running locally on Mac Minis and browsers, users are giving agents access to their Google Calendar, GitHub, Slack — their entire digital life. But the identity layer hasn't kept up. Agents get raw API keys, long-lived tokens with broad scopes, and zero accountability for what they do with them. We built 1-SEC because we saw the OWASP Agentic AI Top 10 happening in the wild: goal hijacking, scope escalation, rogue sub-agents, memory poisoning — all exploiting the gap between "the user said yes once" and "the agent now does whatever it wants." Auth0 Token Vault was the missing piece. It gives agents delegated access without ever exposing raw credentials, and 1-SEC monitors every token exchange to catch abuse in real time. What it does 1-SEC is an open-source, all-in-one cybersecurity platform (single Go binary, zero dependencies) with 16 defense modules. Our AI Agent Containment module (Module 11) integrates Auth0 Token Vault as a sub-component to provide secure OAuth 2.0 delegation for AI agents: Token Exchange Monitoring — Tracks every RFC 8693 token exchange and detects anomalous patterns (rapid exchanges, scope escalation) Scope Escalation Detection — Alerts when a prompt-injected agent requests scopes beyond its original delegation (e.g., calendar.readonly → admin.directory.user ) Agent Authorization Tracking — Enforces that only explicitly delegated agents can use a user's connected accounts. Rogue sub-agents get blocked at the Token Vault level Goal Hijacking Defense — Detects when external content (malicious docs, prompt injection) causes an agent's goal to diverge from user intent, preventing destructive actions even if the agent holds a valid token Memory Poisoning Prevention — Blocks instruction injection into agent persistent memory that attempts to override token scope restrictions OAuth Consent Phishing Detection — Flags suspicious OAuth grants with excessive scopes (>10) for human review Cascade Revocation — When a user unlinks an account in Auth0, 1-SEC automatically revokes all agent delegations for that connection The key insight: Auth0 Token Vault and 1-SEC are complementary defense layers. Token Vault ensures agents never see raw credentials. 1-SEC ensures agents don't abuse the tokens they're given. Even if one layer is bypassed, the other holds. How we built it 1-SEC is written in Go 1.22+ with an event-driven architecture powered by embedded NATS JetStream. The Token Vault integration lives in internal/modules/tokenvault/tokenvault.go as a sub-component of the AI Containment module. Architecture: Events flow through the NATS event bus → AI Containment module → Token Vault sub-component ExchangeTracker monitors token exchange patterns and maintains per-agent scope baselines for escalation detection ConnectedAccountTracker manages the account linking lifecycle and agent authorization state DelegationChainTracker validates delegation chains with expiry, scope bounds, and cryptographic attestation REST API exposes Token Vault status ( GET /api/v1/token-vault/status ) and token exchange ( POST /api/v1/token-vault/exchange ) Auth0 Integration: Uses Auth0's federated connection access token grant type ( urn:auth0:params:oauth:grant-type:token-exchange:federated-connection-access-token ) Supports both refresh token and access token exchange flows Configuration via YAML or environment variables ( AUTH0_DOMAIN , AUTH0_CLIENT_ID , AUTH0_CLIENT_SECRET ) Token Vault is opt-in and additive — all 16 modules work without it; enabling it adds token-aware security context to AI Containment Challenges we ran into Scope baseline tracking was tricky. The first token exchange for a new agent-connection pair establishes the baseline — we can't alert on escalation until we know what's "normal." We solved this with a per-agent, per-connection scope map in ExchangeTracker.DetectScopeEscalation() that records the initial scopes and flags any subsequent request containing new ones. Cascade revocation required careful coordination. When a user unlinks an account in Auth0, we needed to automatically revoke every agent delegation for that connection without race conditions. The ConnectedAccountTracker.RecordUnlink() method atomically removes the account and all associated agent authorizations under a single mutex. Defense-in-depth without redundancy was a design challenge. We needed Token Vault monitoring and the broader AI Containment checks (goal hijacking, memory poisoning, policy enforcement) to be complementary rather than duplicative. The solution: Token Vault handles identity-layer events (exchanges, delegations, OAuth grants) while the containment module handles behavioral events (goal drift, memory writes, action patterns). They share the alert pipeline but monitor different attack surfaces. Accomplishments that we're proud of 5 OWASP Agentic AI Top 10 attack vectors detected and contained in a single demo: scope escalation (ASI02), unauthorized agent access (ASI10), goal hijacking (ASI01), consent phishing, and memory poisoning (ASI06) Zero-credential-sharing architecture — agents interact with Google, GitHub, and Slack without ever seeing a raw OAuth token, thanks to Auth0 Token Vault's RFC 8693 exchange Single binary, zero dependencies — the entire 16-module platform including Token Vault integration ships as one Go binary. No external databases, no message brokers to configure Complementary defense layers — Auth0 enforces at the identity level, 1-SEC enforces at the behavioral level. Two independent points of failure that an attacker must bypass simultaneously What we learned Auth0 Token Vault solves the credential exposure problem elegantly — the RFC 8693 token exchange pattern means agents get scoped, short-lived access tokens without ever touching refresh tokens or client secrets. But identity is necessary, not sufficient. A legitimate token in the hands of a hijacked agent is still dangerous. The combination of Token Vault (controlling what tokens are issued ) and 1-SEC (monitoring how tokens are used ) creates a defense-in-depth posture that neither could achieve alone. We also learned that the OWASP Agentic AI Top 10 threats are deeply interconnected. A memory poisoning attack (ASI06) can lead to scope escalation (ASI02), which can enable a rogue agent (ASI10). Detecting them in isolation misses the chain. 1-SEC's event-driven architecture lets us correlate across attack types in real time. What's next for 1-SEC Open Source Security Live Auth0 Token Vault exchange — Moving from monitoring mode to active token exchange proxying, where 1-SEC acts as a policy enforcement point between agents and Auth0's /oauth/token endpoint Auth0 Actions integration — Triggering Auth0 Actions from 1-SEC alerts (e.g., automatically revoking a connected account when a rogue agent is detected) Agent identity attestation — Using Auth0's client credentials to cryptographically bind agent identities to delegation chains Multi-tenant Token Vault dashboards — Per-user visibility into which agents have access to which connections, with one-click revocation Community adoption — 1-SEC is AGPLv3 open source. We want the security community to extend Token Vault monitoring with their own detection rules Blog https://1-sec.dev/blog/auth0-token-vault-secure-ai-agent-delegation <div