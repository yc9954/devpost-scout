---
slug: "kintwadi-one-shared-record-for-family-caregiving"
url: "https://devpost.com/software/kintwadi-one-shared-record-for-family-caregiving"
title: "Kintwadi: One shared record for family caregiving"
hackathon: "H0: Hack the Zero Stack with Vercel v0 and AWS Databases"
organization: "Amazon"
winner: true
words: 1494
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "mechanism/structural_withholding"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/medical_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Kintwadi: One shared record for family caregiving

> One shared, permission-aware care record for families caring for an aging parent across cities and time zones: meds, vitals, tasks, and a warm AI daily digest that keeps faraway loved ones close.

[Devpost](https://devpost.com/software/kintwadi-one-shared-record-for-family-caregiving) · hackathon [[H0- Hack the Zero Stack with Vercel v0 and AWS Databases]]

## Facets

**mechanism** [[provenance_signing]] [[retrieval_grounding]] [[structural_withholding]]
**domain** [[elder_child_care]] [[health_clinical]] [[housing_homeless]] [[labor_employment]]
  <sub>weak: developer_tools</sub>
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[medical_record]] [[structured_db]] [[video_visual]]

**stack** actions, amazon-web-services, anthropic, aurora, auth.js, claude, css, drizzle, embeddings, framer, github, iam, javascript, motion

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for kintwadi: one shared record for family caregiving

## Body

Homepage Dashboard Appointment Ask Kintwadi AI with RAG Daily digest Medication People roles details Rota Tasks Report incident Timeline Onboarding care person Kintwadi in dark mode Inspiration Caring for an aging parent is one of the most universal human experiences, and one of the worst-tooled. It runs on group chats, sticky notes, and memory, usually carried by one exhausted "default" child while siblings abroad feel guilty and out of the loop. Medications get missed or doubled. No one has the full picture. And families are global now: the person who loves the patient most is often 8,000 km away. I kept coming back to the question a distant sibling asks every night: "Did Dad take his pills?" When the answer is a guess, people get hurt. Kintwadi (Kikongo for togetherness — doing it as one ) is the answer: one shared, permission-aware care record for the whole circle — the local daughter, the brother in another country, the hired aide, and the parent — each seeing the right slice of a single source of truth. What it does Kintwadi is a single, role-aware care record for a family and their helpers. Everyone sees one source of truth, scoped to who they are: Shared care record — recipient profile (conditions, allergies, blood type, directives), a documents vault with sensitivity tiers, and a one-tap emergency card for the ER. Medication safety — structured regimens and schedules, give / skip / refuse logging, PRN caps, supply countdowns and refill alerts, plus a drug-interaction / allergy check on every change. The care timeline — one chronological feed of meds, vitals, notes, photos and incidents, with comments and reactions — the screen that answers "How is Mom today?" at a glance. Coordination — shared appointments (with prep checklists and post-visit summaries), assignable/recurring tasks, a weekly rota, and a fair-share view that makes invisible labor visible and defuses family conflict. Vitals & health — BP, glucose, weight, sleep, mood and HR with trend charts and per-circle safe ranges; out-of-range readings raise urgent alerts and escalate. The smart layer (all on AWS Bedrock) — a Daily Digest that turns a day of small care logs into a warm, human update, translated into each member's own language (the aide reads it in Tagalog, the son in Dubai in English); Ask Kintwadi , a permission-aware assistant that answers natural-language questions grounded in the record with citations; and nightly care scans (refill sweep, missed-dose reconciliation, decline alerts). Roles & trust — seven distinct roles (owner, family admin, family, professional caregiver, read-only, care recipient, clinician), an immutable audit log, and a cross-tenant admin console for B2B agencies. Try it with zero sign-up: the live demo seeds a lived-in family circle (Maria in Toronto, her father Antonio in Manila, brother Paolo in Dubai, and Grace the aide) so you can click around immediately. How we built it The database is the thesis, not a default. Caregiving is inherently relational, transactional, and access-controlled — people, roles, permissions, medications, administrations, appointments, vitals, documents, audit — so I chose Amazon Aurora PostgreSQL (Serverless v2) and leaned all the way into what a relational engine guarantees and a key-value store does not. Three deliberate decisions carry the product: 1. Row-Level Security is the real security boundary — enforced in Aurora, not the UI. The app connects as a least-privilege role that is subject to RLS; every tenant query runs inside a transaction that sets the current user, and Postgres policies decide what each role may read or write. A hired aide physically cannot open a financial document; one family can never read another's record. -- Any circle member may SEE medications; only owners/admins may manage them. create policy medication_manage on medication for all using (circle_id in (select app_user_circle_ids()) and app_user_role(circle_id) in ('owner','family_admin')); // Every request runs in an RLS-scoped transaction (app.current_user_id is LOCAL). export async function withUserContext(userId, fn) { return db.transaction(async (tx) => { await tx.execute(sql`select set_config('app.current_user_id', ${userId}, true)`); return fn(tx); // all queries here obey the user's role policies }); } This is 34 tables and 74 RLS policies across 33 of them , governed by a 7-role matrix — and our CI re-proves cross-tenant isolation against a real Postgres on every push. 2. ACID medication safety. "Give a medication" must update several things at once. In Aurora it's one transaction: it logs the administration event, decrements supply, appends a timeline entry, queues a refill task at the threshold, and writes the audit row — all-or-nothing. Partial writes are clinically unacceptable, and this is exactly what a relational engine makes trivial and a key-value store cannot guarantee. 3. One database does relational and vector — and the vector search inherits the same RLS. "Ask Kintwadi" is Retrieval-Augmented Generation kept entirely inside Aurora. Documents, timeline notes and audit entries are chunked, embedded with Amazon Bedrock Titan (1024-d), and stored as vectors in a rag_chunk table via pgvector (HNSW cosine). The similarity search runs inside the same RLS-scoped transaction, so it can only ever return chunks the asker is allowed to read — sensitivity tiers and tenant isolation are enforced by the database, with no second vector-store ACL to keep in sync . Claude on Amazon Bedrock (Converse API) then writes a grounded, cited answer, and even that read is audited. The rest of the stack: Next.js 16 (App Router + Server Actions) on Vercel , Amazon S3 for documents and photos, Amazon SES/SNS for email and urgent escalation, and keyless AWS in production — each Vercel invocation exchanges its OIDC token for short-lived STS credentials, so no long-lived AWS keys live anywhere (the repo is public). Scheduled jobs run as CRON_SECRET -gated, scheduler-agnostic routes; infrastructure is defined in Terraform . UI is React 19, Tailwind v4, Radix and Recharts, internationalized with next-intl. Challenges we ran into Making RLS truly fail-closed. It's easy to say RLS; making it the last line of defense meant a least-privilege DB role with no BYPASSRLS , FORCE ROW LEVEL SECURITY , security-definer helpers for "which circles/role does this user hold," and per-feature policies for every new table — then writing an integration suite that connects as the app role and asserts circle A can never see circle B. Vector search that respects permissions. The whole point of Ask Kintwadi is that a read-only member can't surface a restricted document through AI. Tagging every chunk with a sensitivity tier and running retrieval under the same SELECT policy as the documents vault — so there's literally one permission boundary — took real schema and query design. Atomic safety across side-effects. Keeping the med-give transaction atomic and firing best-effort notifications (email/push) without letting a flaky side-effect roll back a clinically-recorded dose. Keyless AWS from Vercel. Wiring Vercel's OIDC to AWS IAM/STS so a public repo holds zero credentials, while all four AWS clients (Bedrock, S3, SES, SNS) resolve short-lived creds cleanly. A per-timezone, per-language digest — cheaply. Vercel's Hobby plan caps crons at once/day, which can't drive an hourly, per-timezone digest, so the cron routes are scheduler-agnostic and driven by GitHub Actions. Translating each digest into every member's language without N× model cost meant caching one model call per language per day. Accomplishments that we're proud of Security you can prove, not just claim. DB-enforced RBAC with 74 RLS policies, an append-only audit log, and a CI badge that continuously re-verifies cross-tenant isolation against a real pgvector Postgres. One permission boundary for relational and AI. The pgvector retrieval inherits the exact same RLS as the rest of the record — a genuinely clean architectural insight. It's shippable, not a toy. A live, seeded, zero-sign-up demo running on the same Aurora + Vercel architecture a real product would use. Tasteful AI in service of emotion and safety — the warm, per-language Daily Digest and grounded, cited Ask — not novelty. What we learned Treat the database as the last line of defense. Pushing authorization down to Aurora RLS made the whole app simpler and safer — an application bug can't leak another family's data. "One database, relational + vector" is a real simplification. Keeping embeddings in Aurora under the same policies removed an entire class of sync/ACL bugs a separate vector store would have introduced. Designing for stressed, often older users means accessibility is the UX — calm over busy, large type, one glanceable answer. Hands-on patterns for Bedrock Converse + Titan , and for keyless Vercel→AWS via OIDC/STS. What's next for Kintwadi: One shared record for family caregiving Deeper decline detection — richer vitals trends and anomaly alerts (weight loss, missed-dose streaks, reduced activity). B2B agency dashboard — a multi-family console for home-care agencies and assisted-living coordinators (the same build, a bigger market). Aurora DSQL for global families — a documented path to multi-region, strongly-consistent writes so the sibling in Dubai and the aide in Manila share one low-latency record. Real clinical integrations — replace the illustrative drug-interaction knowledge base with a licensed interactions service, plus pharmacy/EHR connections and clinician sharing. Native mobile and richer notification preferences. <div