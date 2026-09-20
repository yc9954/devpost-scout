---
slug: "relay-n5c9re"
url: "https://devpost.com/software/relay-n5c9re"
title: "Relay - Standby access for the people who will need it"
hackathon: "H0: Hack the Zero Stack with Vercel v0 and AWS Databases"
organization: "Amazon"
winner: true
words: 1061
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/provenance_signing"
  - "mechanism/structural_withholding"
  - "domain/education"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Relay - Standby access for the people who will need it

> Relay: Standby access for the people who will need it - set up who can reach what, and Relay hands it over the moment you can't.

[Devpost](https://devpost.com/software/relay-n5c9re) · hackathon [[H0- Hack the Zero Stack with Vercel v0 and AWS Databases]]

## Facets

**mechanism** [[deterministic_policy]] [[provenance_signing]] [[structural_withholding]]
**domain** [[education]] [[elder_child_care]] [[finance_payments]] [[health_clinical]]
**user** [[general_public]] [[patient_family]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[geospatial]] [[structured_db]]

**stack** amazon-aurora-dsql, aws-kms, fast-check, next-auth, next.js, node-postgres, openai, resend, serverless, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- which aws database - and why aurora dsql
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- business model (monetizable b2c)
- what's next for relay

## Body

Logo Architecture Live in region 1 Live in Region 2 Overview Inspiration When someone is suddenly in surgery, traveling and unreachable, or gone, the people who depend on them hit a wall: they can't get into the bank, the insurance portal, the kids' school account, or the family documents - and the platforms each have their own slow, fragmented process. Existing tools are built around death, so people avoid them and never finish setup. We flipped it: Relay is about living continuity - emergencies, travel, caregiving, business continuity - with estate handoff as the final case of the same mechanism. That reframing is what makes it something people actually use. What it does Relay lets you build an encrypted vault of accounts, credentials, documents, and instructions, then assign scoped, reversible access to the right people under rules you set. When a trigger fires - a missed check-in, a manual emergency request, or a verified estate event - Relay moves through a controlled release process (notify the owner, require N-of-M trusted verifiers, observe a grace window) and only then opens a guided, prioritized access dashboard to the recipient. Emergencies are reversible: when you recover and check in, access closes automatically. Two things make it more than a vault: An importance engine turns a bulk import into focus. Import a password-manager export and dozens of accounts populate instantly; Relay ranks them by what matters in a crisis and surfaces the few that count - including the risk-graph insight that your primary email is the key that unlocks most password resets. A release that is correct under pressure. The irreversible handoff is modeled so it can never double-release, even when the owner, the verifiers, and the scheduler all act at once. Which AWS Database - and why Aurora DSQL We used Amazon Aurora DSQL, and the choice is the architecture, not a detail: Availability at an unpredictable moment. A release can happen any day - possibly during a regional disruption. Aurora DSQL's active-active, multi-region design keeps the recipient's access path live even if a region goes down. We verified this live: a write committed in us-east-1 was read strongly-consistent from us-west-2. Strong consistency for an irreversible action. Releasing a vault is one-way; a stale read of release state or recipient scope is unacceptable. Aurora DSQL's strong consistency across regional endpoints is the right guarantee. Optimistic concurrency that fits the workload. A personal continuity vault is intrinsically low-contention - one owner, rare release events - which is exactly where OCC shines, so we model the release as a conflict-checked compare-and-set. PostgreSQL compatibility with deliberate adaptation. Aurora DSQL doesn't enforce foreign keys, so we enforce referential integrity in application logic - a deliberate design choice, surfaced in our data model. How we built it Frontend: a Next.js (App Router, TypeScript) app deployed on Vercel; route handlers are the API tier. Database: Amazon Aurora DSQL, multi-region active-active, as the system of record for vault metadata, ciphertext, access rules, recipients, verifiers, the release state, and an append-only audit log. Encryption: client-side envelope encryption with AWS KMS - items are encrypted in the browser and only ciphertext plus non-secret metadata are ever uploaded. Release subsystem: a state machine (ARMED to PENDING to GRACE to RELEASED) whose every transition is a compare-and-set validated by Aurora DSQL's optimistic concurrency control; conflicting commits surface as serialization failures and retry or safely abort. Importance engine: serverless functions running heuristics plus an LLM over non-secret metadata only (category, root-credential and recurring-billing flags, dependency edges) - so the smartest part of the product never sees a secret and never breaks zero-knowledge. Triggers: an owner can raise a trigger manually, or it fires automatically on a missed check-in (a dead-man's-switch); either way it advances into the grace window where N-of-M verifier confirmations release it. Challenges we ran into Modeling an irreversible release safely under optimistic concurrency, so concurrent actors can never produce a double-release. Enforcing referential integrity without foreign keys, including orphan and cascade paths. Keeping the importance engine genuinely useful while restricting it to non-secret metadata, so it never compromises the encryption boundary. Making a single mechanism serve everything from a reversible emergency to a permanent estate handoff. Accomplishments that we're proud of A release path that is provably safe under concurrency, drivable both manually and automatically (the dead-man's-switch), and reversible on recovery. An importance engine that converts a noisy import into a short, prioritized, dependency-aware list - and a recipient experience that is a triaged plan, not a scavenger hunt. A zero-knowledge-compatible design where the database holds only ciphertext and non-secret metadata. What we learned Aurora DSQL's optimistic-concurrency model maps cleanly onto exactly-once, irreversible state transitions when you treat them as compare-and-set with retry. Designing for "no foreign keys" pushes integrity into the application in ways that are healthy for a distributed system. The hardest, most valuable problem in this space isn't storage - it is verified, reversible release. Business model (Monetizable B2C) Relay is a consumer subscription product with a clear path to scale. Who pays, and why now: the wedge is the caregiver - an adult child managing an aging parent's accounts feels acute, present pain, and the relationship expands naturally into the estate handoff later. Adjacent segments: frequent travelers, new parents, and small-business owners who need bus-factor continuity. Pricing: a free tier (a small vault + one emergency recipient) converts to a paid annual subscription for the full living vault - unlimited items, multiple recipients and verifiers, N-of-M release, and active-active availability. A one-time activation fee at the moment of need (an emergency or estate release) is easy to justify exactly when it matters most. How the B2C on-ramp compounds: direct-to-consumer is the proof and the on-ramp; the durable distribution is embedded "powered by Relay" continuity offered through institutions people already trust - banks, employer benefits, wealth managers, insurers. Same product, two revenue surfaces: consumer subscriptions + partner licensing. Why it's defensible: platform-native tools (Apple Legacy Contact, 1Password emergency kit) are single-ecosystem, all-or-nothing, and unverified. Relay's moat is the cross-platform, verified, reversible, graduated release layer - human N-of-M verification on a strongly-consistent ledger. What's next for Relay A graduated-assurance verification engine (identity verification, death/incapacity signals, notarization), productionized zero-knowledge via threshold secret-sharing, per-jurisdiction data residency on Aurora DSQL's multi-region foundation, and distribution as embedded continuity infrastructure that banks, employers, and wealth managers offer their clients - beginning with the caregiver wedge. <div