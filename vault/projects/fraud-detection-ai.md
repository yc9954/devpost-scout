---
slug: "fraud-detection-ai"
url: "https://devpost.com/software/fraud-detection-ai"
title: "Fraud Detection AI -→ Version 2.4"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 819
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/immigration_refugee"
  - "domain/security_privacy"
  - "user/researcher"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
---

# Fraud Detection AI -→ Version 2.4

> A fraud detection AI that uses machine intelligence to analyze past transaction data and detect fraudulent transactions in real-time.

[Devpost](https://devpost.com/software/fraud-detection-ai) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]] [[housing_homeless]] [[immigration_refugee]] [[security_privacy]]
**user** [[researcher]]
**substrate** [[financial_record]] [[sensor_telemetry]]

**stack** isolation-forest, kaggle, machine-learning, numpy, one-class-svm, pandas, payslim, python, react, sqlalchemy, typescript

## How they structured the write-up

- fraud detection ai: version 2 update
- what we learned
- what's next

## Body

Dashboard Transactions Chart Transactions Anomalies Table Anomaly Case Management Create New Case Affected Transactions Senders Bank Main Bank API Gateway Fraud Detection AI: Version 2 Update Following up on our previous submission, we've made significant updates to Fraud AI, a real-time fraud detection system for bank accounts that watches transactions as they happen and flags suspicious activity with reasons. Version 1 Recap Version 1 video demo . The original system ran 10 checks across 5 risk categories : The 10 checks: Velocity - Is the user sending money way faster than usual? (e.g., 15 transactions in an hour) Volume Analysis - Is the amount unusually high compared to their 30-day average? Impossible Travel - Was the user just in Lagos and now suddenly in London 2 hours later? Login Integrity - Multiple failed logins before this transaction? Suspicious or mismatched device? New Device/Behavior - Is this a brand new device? Is the session length off? Structuring - Sending the same amount repeatedly to stay under reporting limits? Transaction Spikes - Sudden burst of activity on a dormant account? Cross-Border - Money going to a high-risk country or somewhere new for this user? Historical Baseline - Does this break their usual pattern? (e.g., they never spend on gambling, but now they do) Volume Thresholds - Does this single transaction drain 90% of their account balance? The 5 risk categories: Account Compromise - Login anomalies + new device + impossible travel Amount Anomaly - Volume analysis + threshold breaches AML Structuring - Structuring patterns Automation Abuse - Velocity spikes + transaction bursts Geo Anomaly - Cross-border transfers + location inconsistencies Those categories rolled up into a final verdict: BLOCKED, HELD, or APPROVED. Version 2 Updates 1. Smart Fraud Analysis Introduced a smarter ML layer that blends the base anomaly score with adaptive, user-specific thresholds and adjusts based on how complete and confident the feature data is. A large transaction from someone who regularly makes large transactions no longer gets treated the same as a large transaction from someone who never has. 2. Beneficiary Trust Score The system now tracks relationship history per recipient. Frequent, consistent transfers to the same person build trust over time, and the system applies a small, bounded risk reduction accordingly. It stays conservative for new or unfamiliar beneficiaries. 3. Risk Trend API A new endpoint, GET /api/fraud/trend/{user_id} , returns 7-day and 30-day average risk scores, flagged transaction counts, and a directional trend (up, down, stable). This shifts the system from point-in-time alarms to proactive monitoring. 4. Banking Payload Enrichment The banking backend now sends richer context to the ML layer: device signals, account age, transaction history, and beneficiary relationship metrics. Better input, better decisions. 5. Risk Trend Dashboard Card Operations teams now have a compact dashboard card showing average risk scores, flagged counts, and a directional trend indicator at a glance. 6. Overall UI Redesign Complete UI redesign and refinement across all dashboard components and modals to enhance user experience. What We Learned Static thresholds don't hold up. Version 1 treated every user the same, which meant legitimate transactions kept getting flagged simply because the amounts looked unusual on paper. We learned that the system needed to know who it was dealing with before making a call. That pushed us toward adaptive, per-user thresholds in V2. We also learned that blocking a transaction is only half the job. Fraud analysts need to understand risk over time, not just react to individual alerts. A single flagged transaction tells you something happened. A rising risk trend over 7 days tells you something is wrong with the account. That gap is what pushed us to build the Risk Trend API. The other thing that became clear was how much false positives cost trust. If the system flags your rent payment, you stop trusting the system. Beneficiary Trust Score came directly from that problem. Repeat, consistent transfers deserve different treatment than transfers to a brand new recipient. What's Next The immediate next step is production deployment. The system needs to move from a demo environment into infrastructure that can handle real transaction volumes, with proper uptime, failover, and data security standards that fintech platforms expect. From there, the plan is to pitch Fraud AI as a plug-in fraud detection layer to fintech companies and neobanks operating continentally. The fraud problem is severe in this market and most smaller platforms don't have the resources to build detection in-house. That's the gap Fraud AI fits into. On the technical side, we want the model retraining on new fraud patterns in real time rather than every 30 days. We also plan to layer in behavioral signals like typing rhythm, device orientation, and session behavior so the system can catch account takeovers before a transaction is even submitted. The goal is a fraud detection service that any fintech team can integrate through an API, without needing a dedicated data science team to run it. <div