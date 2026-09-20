---
slug: "meridian-uw62z5"
url: "https://devpost.com/software/meridian-uw62z5"
title: "Meridian"
hackathon: "UiPath AgentHack"
organization: "UiPath"
winner: true
words: 1334
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/provenance_signing"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "user/government_staff"
  - "user/researcher"
  - "user/social_worker"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Meridian

> Meridian: an agentic UiPath Maestro system that automates maritime voyage compliance AI agents run document, sanctions & port checks, escalate to humans only when needed, and log every decision.

[Devpost](https://devpost.com/software/meridian-uw62z5) · hackathon [[UiPath AgentHack]]

## Facets

**mechanism** [[human_in_the_loop]] [[provenance_signing]] [[vision_ocr]]
**domain** [[finance_payments]] [[immigration_refugee]] [[labor_employment]] [[supply_logistics]]
**user** [[government_staff]] [[researcher]] [[social_worker]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[geospatial]]

**stack** apiworkflow, codedagents, documentunderstanding, javascript, lowcodeagents, maestro, roboticprocessautomation, uipath, uipathapps, uipathdatafacric

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for meridian

## Body

Intake App Maestro Implementation Approval form Inspiration Global trade moves on ships — but ships don't move until the paperwork clears compliance. Before a cargo vessel is released for a voyage, three things must be confirmed: the trade documents are internally consistent, none of the parties are on a sanctions or denied-party list, and the destination port is open. Today this is done by three different people, in three different tools, with no shared record. A document analyst reads PDFs. A compliance officer searches a watchlist. Someone emails the port agent. A voyage can sit for hours or days waiting on checks that individually take minutes — and when release is finally granted, there's no single auditable answer to the one question a regulator cares about: who approved this, and why? That gap — high stakes, real cost, still stitched together by hand — is exactly what agentic automation is for. Not replacing people, but orchestrating the whole process and pulling a human in only where judgment is genuinely required. That's Meridian. What it does Meridian turns maritime voyage release into one intelligent case on UiPath Maestro. A coordinator submits a voyage through a UiPath App — vessel and party details plus five trade documents (bill of lading, cargo manifest, certificate of origin, insurance certificate, quality certificate). That submission creates a case, and the case runs itself through four checks: Document Intake — Document Understanding extracts structured data from the five files into one packet. Document Verification — an AI agent runs five consistency checks (field matching, weight tolerance within 2%, completeness, amendment propagation, date sanity). Party Validation — a coded agent screens shipper, consignee, and vessel operator against a denied-party list. Port Readiness — an API workflow confirms the destination port is open. Every check returns one of three verdicts: PASS → continue to the next check FAIL → route straight to Rejected REVIEW → pause and route to a human reviewer , who sees exactly what was flagged and why, then decides — and the case resumes the instant they approve When everything clears, an AI Release Coordinator agent writes a plain-English closure summary and the case closes with one recorded outcome: RELEASED , RELEASED_WITH_OVERRIDE (a human approved a flagged check), or REJECTED — each with a full audit trail. Compliance that runs itself where it can, escalates to people only where judgment is needed, and produces an audit-ready record every time. How we built it The core is a UiPath Maestro case that owns the full lifecycle. Around it sit specialized components: Component Type Role Intake App UiPath App Captures voyage + document uploads; the record triggers the case DUExtraction RPA + Document Understanding Extracts five documents into one JSON packet VerificationAgent Low-code agent (Claude Sonnet) Five document-consistency checks → verdict PartyValidationAgent Coded agent (Python / LlamaIndex, Claude Haiku) Denied-party screening via token-set matching PortLookupTool API workflow Destination port status Human Review Apps UiPath Apps Human-in-the-loop approve/reject on flagged checks ReleaseCoordinatorAgent Low-code agent (Claude Sonnet) Writes the closure summary Two design decisions made the whole thing work: Flat, scalar contracts. Instead of agents returning rich nested JSON that the case has to parse, every component emits flat values — a result ( PASS / FAIL / REVIEW ), a one-sentence comment , and a score . That single choice turned every Maestro routing rule into a one-liner ( docResult == "PASS" ) with zero script tasks and zero JSON parsing in the case. A unified vocabulary. Each check has its own domain language internally — the party agent thinks in CLEAR / POSSIBLE_MATCH / CONFIRMED_MATCH , the port tool in OPEN / RESTRICTED . We mapped all of them to the same three words: PASS , FAIL , REVIEW . Because every check speaks the same language, every stage routes identically and the human-review pattern is reusable across all of them. For human-in-the-loop, we used Maestro secondary (interrupting) stages with return-to-origin exits: a REVIEW verdict diverts the case into a review stage, pauses for a human, and returns it to the exact stage it came from. Underpinning everything is one flat Data Fabric entity — every component reads from and writes back to it, so the case never holds hidden state. Challenges we ran into Routing loops. When a human approved a flagged review, the case returned to its originating stage — but the agent's verdict was still REVIEW , so the stage tried to route back into the review lane again. An infinite loop. The fix was subtle: mark the check task run-only-once , so on re-entry it doesn't re-evaluate — the human's decision, not the stale verdict, drives the case forward. A matching quirk we had to be honest about. Our party screening uses token-set matching with a stopword list that strips company suffixes ( ltd , holdings , co ). We found this collapses two genuinely different firms — "Caspian Cargo Ltd" and denied "Caspian Cargo Holdings" — to identical tokens and a perfect match. With clean demo data, nothing landed in the middle REVIEW band, so the human-review path would never fire. We computed real scores against the actual list to find inputs (an operator scoring $0.33$) that genuinely produce a borderline match — and kept the quirk documented, since over-flagging is the safe direction for compliance. Two competing routing patterns. Midway we had both destination-carrying exit rules and entry rules on target stages layered together — they collided everywhere. The conflicts vanished the moment we committed to one orchestration pattern and applied it consistently. Scope discipline. We designed an ambitious version with cost-savings math, an assumption ledger, and a document-rework loop. As the deadline closed, we cut what added risk without adding demo clarity and kept the core airtight: three checks, human review, three outcomes. Accomplishments that we're proud of A genuinely agentic case, not a linear script. Four AI/automation components make real decisions, and the case orchestrates them event-driven — stages fire on conditions, not a fixed sequence. A working human-in-the-loop loop that actually resumes. The case pauses, hands a person the exact context they need, and picks up cleanly — no lost or double-counted state. This is the hard part of case management, and it works. Three distinct, auditable outcomes — RELEASED , RELEASED_WITH_OVERRIDE , REJECTED — each with an AI-written closure summary, so every release answers "who approved this and why." A clean, reusable architecture — the flat-contract + unified-vocabulary design means every check wires in identically, and new checks or review lanes drop in without touching the case logic. Fully UiPath-native — Maestro, Apps, Document Understanding, coded and low-code Agents, Data Fabric, and RPA working as one system. What we learned Contracts matter more than cleverness. Our first design had agents returning detailed objects and a versioned ledger — elegant on paper, a nightmare to wire. Flattening every output to scalars made the system buildable and debuggable. Design the interface between components before you build the components. Event-driven orchestration is a different mental model. Maestro stages fire when their conditions become true against the entity — you reason about state , not sequence . Our worst bugs came from thinking sequentially when we should have been thinking in conditions. Human-in-the-loop is a design pattern, not a feature. The real engineering wasn't the AI checks — it was the return path: pausing, handing off with the right context, and resuming without corrupting state. What's next for Meridian Multi-review audit trail — log each human decision as its own ledger entry so multi-step approvals are fully traceable, rather than a single last-decision field. Document-rework loop — let a reviewer re-upload a corrected document and re-run extraction automatically (designed; a natural next stage). Cost & savings surfacing — quantify delay avoided and selective-recheck savings versus re-running every check. Executive sign-off gate — an optional final approval and notification for leadership before high-value releases close. Each layers on top of the working core without touching the flat contracts underneath — which was the whole point. <div