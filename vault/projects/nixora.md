---
slug: "nixora"
url: "https://devpost.com/software/nixora"
title: "Nixora"
hackathon: "LMA EDGE Hackathon"
organization: "LMA"
winner: true
words: 1166
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "domain/security_privacy"
  - "user/government_staff"
  - "user/legal_professional"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Nixora

> Nixora brings loan markets into the digital age by transforming loan agreements into AI-powered, interoperable data with automated tracking, collaboration, and workflow integrations.

[Devpost](https://devpost.com/software/nixora) · hackathon [[LMA EDGE Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[finance_payments]] [[legal_justice]] [[security_privacy]]
**user** [[government_staff]] [[legal_professional]] [[researcher]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[geospatial]] [[structured_db]]

**stack** aiven-database, chrome, cloudinary, docker, firebase-cloud-messaging, gemini-3.0-flash, gemini-3.0-pro, google-calendar, google-cloud-console, google-document-ai, google-vertex-ai, goole-cloud-storage, java, nextjs

## How they structured the write-up

- inspiration
- the problem
- our solution
- what it does
- why this matters commercially
- how we built it
- api surface
- challenges we encountered
- accomplishments we’re proud of
- what we learned
- what’s next for nixora

## Body

Nixora — Digitising the Loan Market Inspiration The global loan market is worth trillions of dollars , yet it still runs on PDFs, emails, and manually maintained spreadsheets. Even the most sophisticated lenders and agents rely on people to read, interpret, track, and re-enter data from long legal documents. Behind every major business — from airlines to energy companies — sits a loan. And behind every loan still sits a PDF . This creates three systemic problems: Risk is hidden inside unstructured text Liquidity is slow because loans cannot be easily compared or traded Operations are expensive because every lifecycle event is manually tracked Loan documents today exist as legal prose — opaque, unsearchable, and disconnected from the systems that actually manage money, risk, and compliance. Nixora changes that. The Problem A modern commercial loan may last 5–10 years and include: Multiple lenders Variable interest rates Dozens of covenants Continuous reporting and payment obligations Yet all of this is buried inside documents that cannot be queried, analysed, or automated. So institutions are forced to rely on: Manual compliance checks Spreadsheets to track maturities Emails to coordinate between teams Legal reviews just to know what a loan requires This leads to: Missed obligations Late payments Compliance failures Hidden portfolio risk The financial system is digital, but the infrastructure behind loans is still analog . Our Solution Nixora turns loan agreements into live digital assets. By combining Google Document AI , Vertex AI , and Gemini 3.0 pro , Nixora ingests raw credit agreements and converts them into LMA-standardised, structured data . Every borrower, lender, covenant, maturity date, and obligation becomes: Searchable Comparable Trackable Actionable in real time And with Nixora’s AI-powered Loan Chat , users can now ask natural-language questions like: “What is the availability period for this loan?” “Which covenants apply to this borrower?” “When is the next interest payment due?” …and receive instant, accurate answers directly from the agreement. Instead of managing loans as files, Nixora lets institutions manage them as data — interoperable, auditable, and connected across systems. What it does Nixora is an end-to-end Digital Loan Operating System for the global loan market. Users can upload any loan agreement (PDF, Word, Excel), or capture documents directly from the web using the Nixora Chrome Extension . From there, Nixora transforms unstructured legal contracts into live, intelligent, and standardized loan data. Nixora then: Extracts and normalizes text using Google Document AI Understands and structures the contract using Vertex AI + Gemini 3.0 Flash Preview Maps everything into LMA-aligned JSON — creating a real-time, structured loan model From a single upload, Nixora powers the entire loan lifecycle: Portfolio Search & Querying Instantly search across borrowers, lenders, facilities, covenants, currencies, margins, and maturities across your entire book of loans. Loan Comparison Compare pricing, structure, repayment terms, and risk across multiple facilities and borrowers in seconds. AI Loan Chat Ask natural language questions about any agreement — Gemini returns precise, explainable answers grounded directly in the contract. Risk, Covenant & Maturity Reporting Automatically detect high-risk loans, upcoming deadlines, covenant exposure, and compliance gaps. PDF & Excel Exports Generate institution-grade reports for credit committees, auditors, and regulators. Loan Schedules & Event Tracking Automatically create payment schedules, covenant tests, and maturity timelines from the legal text. Calendar & Workflow Sync Push obligations directly into Google Calendar and Trello to ensure nothing is missed. Real-time Collaboration Invite colleagues via WhatsApp to view, edit, and work on the same loan live. Push Notifications Desktop alerts for uploads, payments, covenant breaches, and critical risk events. Chrome Extension for Live Loan Capture Capture loan documents, term sheets, and deal data directly from emails, data rooms, and web portals — sending them instantly into Nixora for structuring and tracking. Nixora turns static loan documents into living financial systems that teams can search, monitor, collaborate on, and trust. Why this matters commercially Value Proposition Nixora gives financial institutions something they have never had: A single, intelligent source of truth for every loan. From executives to analysts, everyone sees the same live data, the same risks, and the same obligations — without digging through documents. Efficiency Gains What currently takes teams of analysts, lawyers, and operations staff becomes: Automated Real-time Always accurate Nixora eliminates manual document review, spreadsheet tracking, and missed deadlines — dramatically reducing operational cost and risk. Scalability Once a loan is digitised: It can be searched Compared Queried Traded Analysed Nixora scales like software, whether managing 10 loans or 10 million. Market Impact By turning legal contracts into digital assets, Nixora unlocks: Faster loan trading Better risk pricing More transparent credit markets Easier access to capital for businesses Nixora is not just a tool — it is financial infrastructure . How we built it Nixora is a cloud-native, API-driven platform. AI & Document Intelligence Google Document AI – text extraction Google Vertex AI + Gemini-3.0-pro – clause understanding, field extraction, LMA mapping, and AI loan chat Backend Java + Spring Boot PostgreSQL (JSONB loan model) Redis for fast querying Cloudinary + Google Cloud Storage for documents Integrations Google Calendar API – obligation syncing Trello API – workflow management Firebase Cloud Messaging – push notifications Resend – transactional email Frontend React + Next.js Chrome Extension for in-workflow loan access All functionality is exposed via a fully documented OpenAPI / Swagger API . API Surface Core POST /api/loans/documents/upload PATCH /api/loans/documents/update-field/{loanId} GET /api/loans/documents/getLoan/{loanId} GET /api/loans/documents/getAllLoan DELETE /api/loans/documents/delete-loan/{loanId} Portfolio Intelligence POST /api/loans/query/search-query POST /api/loans/compare GET /api/reports/portfolio GET /api/reports/high-risk GET /api/reports/maturity AI Loan Chat POST /api/loan-chat/chat/{loanId} Exports GET /api/reports/export/*/pdf GET /api/reports/export/*/excel Scheduling & Workflow GET /api/loans/{loanId}/schedule POST /api/loan/calendar/{loanId}/sync POST /api/trello/connect POST /api/trello/push-field Collaboration POST /api/collaboration/invite POST /api/collaboration/accept Notifications POST /api/notifications/register-device Challenges We Encountered Accurate data extraction: Early attempts using regular expressions were unreliable for complex legal language. We solved this by combining Google Document AI, Vertex AI, and Gemini 3.0 Flash, which enabled us to extract and structure loan data far more accurately. LMA standardization: Identifying true LMA-standard fields was challenging, as there is no fully open public schema. We conducted deep research using LMA publications, sample agreements, and industry articles, allowing us to build a high-quality standardized model that closely reflects real-world LMA structures. Access to real loan agreements: Obtaining real-world commercial loan documents was difficult due to confidentiality. Through extensive public research and financial document repositories, we sourced realistic agreements to properly test and validate Nixora’s AI pipeline. Accomplishments we’re proud of True digital loans — not PDFs, but live data LMA-aligned structured loan models AI-powered loan chat for instant answers Calendar, Trello, and push notification integrations Real-time collaborative loan editing Institutional-grade reporting & exports What we learned Loan professionals don’t want more tools — they want their existing tools to become smarter . AI is most powerful when paired with structured data. Integrations drive adoption as much as intelligence. What’s next for Nixora Automated covenant monitoring Secondary-market trading APIs Integration with loan servicing and settlement platforms Portfolio-level risk scoring Deeper LMA data standardisation Nixora is becoming the data backbone of the modern loan market . <div