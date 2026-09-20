---
slug: "deal-flow"
url: "https://devpost.com/software/deal-flow"
title: "Deal Flow"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 499
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/general_public"
  - "user/legal_professional"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Deal Flow

> Traditional insurance is plagued by slow, manual claim verification and opaque rejection reasons. dealFlow solves this by acting as an AI Forensic Auditor.

[Devpost](https://devpost.com/software/deal-flow) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[finance_payments]] [[retail_commerce]]
**user** [[general_public]] [[legal_professional]] [[small_business]]
**substrate** [[financial_record]] [[structured_db]] [[video_visual]]

**stack** css3, html5, make.com, react, solidity

## How they structured the write-up

- inspiration
- deployed link
- 💡 inspiration
- 📸 how it works
- 🚀 key features
- ⚙️ how it works (the flow)
- 🛠️ built with
- 📦 getting started
- 🔮 what's next for dealflow
- 👥 team
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for untitled

## Body

Inspiration 🌊 DealFlow AI-Powered Autonomous Insurance Protocol Bridging the gap between on-chain liquidity and off-chain reality. DEPLOYED LINK https://deal-flows.netlify.app/ 💡 Inspiration Traditional insurance is plagued by slow, manual claim verification and opaque rejection reasons. dealFlow solves this by acting as an AI Forensic Auditor . It connects a user's real-world evidence (photos of bills/receipts) with a company's on-chain liquidity and policy rules, creating a system where valid claims are paid out instantly, and invalid ones are rejected with clear, transparent reasons. 📸 How It Works 1. The "Brain" (Automation Engine) The core of dealFlow is a Make.com scenario that orchestrates the logic between Gmail, Google Gemini AI, and our Supabase ledger. ![ https://eu1.make.com/public/shared-scenario/2CgSk0vkgBS/integration-gmail-http ] 2. The Verdict (AI Forensic Auditor) ![ insurancebot45@gmail.com ] 🚀 Key Features 🤖 AI Forensic Auditor: Uses computer vision (Google Gemini) to extract specific data from receipts (Merchant Name, Date, Total Amount) and cross-references it with the insurer's policy terms. ⚡ Automated Claim Settlement: No human intervention required. If the data matches the policy, the claim is approved instantly. 🏢 Dual-Dashboard System: Business Dashboard: Real-time financial tracking (Total Locked, Paid Out, Available Balance). Consumer Dashboard: Simple interface for users to track claim status. 📧 Zero-Friction Submission: Users don't need to learn complex dApps to file a claim; they simply reply to an email with their evidence. ⚙️ How It Works (The Flow) Business Onboarding: An Insurance Agent registers on the Business Dashboard and funds their liquidity pool. Claim Submission: A user submits a claim via the Consumer Portal or by sending an email with an attachment (photo of the bill). The "Watcher": Our Make.com engine detects the new submission. AI Analysis: Gemini AI scans the image, acting as a forensic auditor. It extracts the Bill Amount and Wallet Address and checks against the specific Company Policy stored in Supabase. The Verdict: Approved: The system updates the on-chain ledger and deducts the amount from the company's "Available Balance." Rejected: The AI drafts a specific reply explaining exactly what is missing. Notification: The user receives an instant email notification with the verdict. 🛠️ Built With Frontend: React + Vite Styling: Tailwind CSS + shadcn/ui AI Engine: Google Gemini API (Vision & Text Processing) Automation: Make.com (Orchestration) Database: Supabase (PostgreSQL & Real-time) Web3: Ethers.js (Wallet connection) 📦 Getting Started Prerequisites Node.js (v16 or higher) npm or yarn Installation Clone the repo sh git clone [https://github.com/krish2413179-prog/dealFlow.git](https://github.com/krish2413179-prog/dealFlow.git) Install NPM packages sh npm install Start the development server sh npm run dev 🔮 What's Next for dealFlow Smart Contract Integration: Moving the ledger from Supabase to a fully decentralized Smart Contract on Polygon/Ethereum. Fraud Detection 2.0: Implementing advanced metadata analysis to detect Photoshop-edited receipts. Multi-Chain Support: Allowing payouts in USDC, ETH, or MATIC. 👥 Team [Krish Sharma] - Full Stack & Automation Note to Judges: The Make.com scenario JSON is included in the /automation folder for review. What it does How we built it Challenges we ran into Accomplishments that we're proud of What we learned What's next for Untitled <div