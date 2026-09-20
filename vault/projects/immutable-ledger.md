---
slug: "immutable-ledger"
url: "https://devpost.com/software/immutable-ledger"
title: "Immutable Ledger for Jira: Verifiable Audit"
hackathon: "Codegeist 2025: Atlassian Williams Racing Edition"
organization: "Atlassian"
winner: true
words: 740
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Immutable Ledger for Jira: Verifiable Audit

> The first cryptographically verifiable, SOX-compliant audit trail for Jira. Features immutable hash-chaining, legal hold deletion tracking, and GDPR-safe erasure. Runs 100% on Atlassian Forge.

[Devpost](https://devpost.com/software/immutable-ledger) · hackathon [[Codegeist 2025- Atlassian Williams Racing Edition]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
**domain** [[finance_payments]] [[labor_employment]] [[legal_justice]]
**substrate** [[document_pdf]] [[financial_record]] [[structured_db]]

**stack** forge

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for immutable ledger for jira: verifiable audit

## Body

Inspiration While researching the needs of highly regulated industries (Finance, Healthcare, Legal), we discovered a gap in the Atlassian Marketplace. Most "audit log" apps are simply reporters—they read Jira's native history. But for an auditor or a legal representative, a report isn't enough; they need proof. We realised that native Jira history is mutable (it can be changed) and often loses context when issues are deleted. This is a nightmare for: Compliance: Which requires "immutable storage security." Legal Holds: Which require the preservation of evidence and proof of spoliation (deletion). Data Residency: Highly regulated customers cannot afford to send their sensitive logs to third-party servers. We built Immutable Ledger to replace "trust" with "verification." We wanted to give GRC teams a tool that proves that their data hasn't been tampered with, without a single byte ever leaving the Atlassian Cloud. What it does Immutable Ledger turns Jira into a secure evidence locker. It is not just a log; it is a cryptographically chained ledger. Tamper-Proof Logging: Every time an issue is changed, the app creates a "Ledger Block" containing the change data. Crucially, it calculates a SHA-256 hash of the block combined with the previous block's hash. This creates an unbreakable chain. If anyone tries to alter a past record, the entire chain breaks, and the corruption is instantly detected. Proactive Deletion Detection: Native Jira often fails to trigger events for deleted issues. Our app uses a "Proactive Reconciliation" engine that periodically scans for issues that exist in the ledger but are missing from Jira, creating an immutable record of the deletion. GDPR-Compliant Immutability: It solves the paradox of "Permanent Logs" vs. "Right to be Forgotten." We use Cryptographic Erasure. PII is stored encrypted with unique keys. To "forget" a user, we shred their specific key. The ledger remains intact and verifiable, but the personal data becomes unrecoverable gibberish. Auditor Verification: A simple "Verify" button allows an auditor to re-calculate the hash chain in real-time, proving 100% integrity. How we built it We built this as a 100% Forge-native application to qualify for the "Runs on Atlassian" badge. Storage: We used storage.set for the ledger blocks and the high-security storage.setSecret vault to protect the "Chain Head" (the latest hash) and the HMAC signing keys. This ensures that even if someone could access standard storage, they couldn't forge a valid chain signature. Encryption: We implemented Node.js native crypto modules within the Forge runtime to handle SHA-256 hashing and AES-GCM encryption for the GDPR functionality. Challenges we ran into The "Missing Delete" Event: Forge (and Jira Cloud) has historically lacked a reliable webhook for "Issue Deleted." This was a showstopper for a legal hold app. We overcame this by engineering a "Proactive Reconciliation" system, a scheduled background worker that diffs our ledger against the live API to detect and log vanishings. The Immutability Paradox: Building a compliant app means satisfying opposing laws (SOX vs. GDPR). Designing the "Key Shredding" architecture required careful planning to ensure we could destroy data readability without destroying data integrity. Forge Storage Limits: Implementing a blockchain-like structure on a Key-Value store required efficient data modelling to avoid hitting API rate limits during the verification process. Accomplishments that we're proud of Zero Data Egress: We successfully built a complex compliance tool that stores nothing off-platform. This makes the app immediately viable for banking and healthcare customers who block external data flows. Mathematical Truth: We moved beyond "trust us, we logged it" to "here is the cryptographic proof." Seeing the verification engine successfully detect a manual database tamper during testing was a huge win. Turning a Platform Gap into a Feature: Instead of giving up because of the missing "Delete" event, we built a solution that actually provides better visibility into data loss than native Jira. What we learned The Power of Forge: While constrained compared to a full external server, Forge's constraints forced us to be creative and ultimately resulted in a more secure, trustworthy product for the customer. What's next for Immutable Ledger for Jira: Verifiable Audit Rovo Agent for Auditors: We plan to build a Rovo Agent that allows an auditor to ask natural language questions like, "Show me all financial field changes approved by John Doe last quarter," and receive a verified answer. PDF Export: Generating a court-admissible, signed PDF report of the ledger directly within the browser. Expansion to Confluence: Applying the same hash-chain logic to Confluence pages for IP protection and patent documentation. <div