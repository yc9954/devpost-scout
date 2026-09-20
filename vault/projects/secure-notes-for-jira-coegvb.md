---
slug: "secure-notes-for-jira-coegvb"
url: "https://devpost.com/software/secure-notes-for-jira-coegvb"
title: "Secure Notes for Jira"
hackathon: "Codegeist 2025: Atlassian Williams Racing Edition"
organization: "Atlassian"
winner: true
words: 869
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Secure Notes for Jira

> Secure Notes: Encrypted by design, protected by the platform App provides zero-trust, burn-after-reading way to share sensitive information inside Jira, when only intended recipients can ever view it

[Devpost](https://devpost.com/software/secure-notes-for-jira-coegvb) · hackathon [[Codegeist 2025- Atlassian Williams Racing Edition]]

## Facets

**mechanism** [[privacy_tech]] [[provenance_signing]]
**domain** [[developer_tools]] [[housing_homeless]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]]

**stack** drizzle-orm, forge, forge-sql-orm, forge/event, forge/kvs, forge/realtime, forge/sql, react, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for secure notes for jira

## Body

Creating secure note Decrypting secure note Secure note decripted Secret notes history Inspiration Teams often need to share sensitive information during everyday work — temporary credentials, tokens, incident details, or any message that shouldn’t appear in comments, issue fields, or chats. Jira is the natural place where this information belongs, yet it provides no private, ephemeral channel for confidential communication. Secure Notes for Jira emerged from the idea of creating such a channel directly inside Jira — without external tools, without separate systems, and with a strict zero-trust approach where only the intended recipients can ever decrypt the content. The design is built on three principles: Zero-trust: all encryption happens in the user’s browser, and the server never holds enough data to decrypt anything. Burn-after-reading: encrypted content is permanently destroyed immediately after it’s viewed or expiration is reached. No recovery: no secret or key material are ever stored, making it cryptographically impossible to restore a note later. At the same time, organizations still require transparency and accountability. To support this, Secure Notes provides a structured audit trail available to administrators — without exposing the actual secret. ⸻ What it does Secure Notes for Jira adds an encrypted note system directly inside Jira. It enables confidential communication with automatic expiration, one-time access, and comprehensive audit logging. Secure Note Features Create encrypted notes directly in Jira issues Share with one or multiple recipients End-to-end client-side encryption (AES-GCM) One-time access with automatic self-destruction after viewing Expiration options including 1 hour, 1 day, 7 days, 10 days, or custom Audit & Compliance Dashboard A global page that provides following views: My History — all notes you created or received My Issue History — activity grouped by Jira issue My Project History — activity grouped by Jira project User History (Admin) — per-user activity across the entire site (w/o seeing actual secrets) CSV export for compliance and reporting Administrators can see: When a note was created Human-readable description (non-sensitive context string provided by the sender) Which Jira issue it belongs to Who created it Intended recipients When each recipient viewed the note Rovo agent capabilities: Provides audit trail in a natural language format according to user permissions Creates summaries about shared secure notes, their frequency, top users, etc Three-Layer Security Model Runs on Atlassian — the note lives fully inside jira site, with native isolation and governance. Strict access control — only authorized recipients can open the note. Client-side encryption — the key is generated in the browser and is never sent to Atlassian’s cloud. Together, these layers ensure confidentiality even if infrastructure or metadata is exposed. ⸻ How we built it Frontend: React + Vite (Forge Custom UI), multi-context UI (Issue Panel, Modal Dialogs, Global Page), Atlassian Design System, full theme support, client-side routing. Backend: Forge Functions with @forge/api, @forge/sql, @forge/kvs, forge-sql-orm. Shared: @forge/realtime, shared Backend-Frontend contract ORM: forge-sql-orm (custom Drizzle-based ORM). Storage: Encrypted content → @forge/kvs.setSecret Metadata (expiry, IV, salt, status, recipients) → Forge SQL Security: AES-GCM encryption performed entirely in the browser PBKDF2-based key derivation (~200,000 iterations) Key split into encryption + server-verification components No plaintext ever sent to backend(atlassian infrastructure) Multi-recipient validation via account ID matching Scheduled Forge trigger cleans expired notes every 5 minutes Audit System: A set of optimized SQL queries and indexed tables built on forge-sql-orm, with grouping by issue, project, or user. ⸻ Challenges we ran into Designing a clean UX for a security-focused app while keeping workflows fast and simple Coordinating multiple Forge contexts (Issue Panel, Modal, Global Page) with a single frontend codebase Implementing client-side crypto with zero plaintext exposure to the backend Handling multi-recipient notes with independent access tracking per user Building a large audit dashboard without compromising performance Enforcing strict one-time access semantics across Forge Functions and KVS Managing deep links (/view/:noteId) in a global page inside the Forge environment Ensuring everything stays Runs on Atlassian–compliant ⸻ Accomplishments that we’re proud of Open-source project with MIT license Created a practical development pattern for complex Forge solutions ensuring clarity, maintainability, and reliability Adopted best code quality and tooling Introduced pattern for caching and observability Forge SQL via forge-sql-orm Successfully used newly introduced @forge/realtime Successfully adopted Rovo agent Built a full end-to-end encrypted system that stores no plaintext and no keys Designed a modular security architecture built on Atlassian’s strengths Delivered an app that is both secure and practical for real-world workflows Kept the entire system Forge-native without any external services or servers ⸻ What we learned How to use @forge/realtime and shared BE-FE contract with typescript model validation How to work with Rovo How to build a multi-context Custom UI application with clean state management How to extend Forge SQL with a custom ORM and efficient indexed queries How to design user-facing encryption flows that remain simple and intuitive How to combine platform security (tenant isolation) with cryptographic security (E2E) How to structure audit trails for compliance without storing sensitive content How to add dependency injection with inversify library ⸻ What’s next for Secure Notes for Jira Larger encrypted attachments (1–2 MB) using multipart Object Storage Issue sidebar widget for fast note creation Encrypted message threads inside an issue Insights dashboards: sharing frequency, expiration patterns Marketplace listing with free and Pro editions <div