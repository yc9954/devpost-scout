---
slug: "solshare-cmxous"
url: "https://devpost.com/software/solshare-cmxous"
title: "Solshare"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 563
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Solshare

> Splitting bills with friends is messy—receipts get lost, people forget to pay, and tracking balances is a headache. SolShare fixes this: scan, assign, and settle instantly on Solana.

[Devpost](https://devpost.com/software/solshare-cmxous) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[financial_record]] [[structured_db]] [[video_visual]]

**stack** cohere, firebase, gcp, solana, swift, swiftui, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for solshare

## Body

Inspiration At the University of Waterloo, “Costco” has become our second home. Since we’re broke college students, we only had one membership, so everyone piled into a single trip to stock up. The problem came later. Splitting a giant receipt fairly was always a headache. At the same time, we’ve been promised seamless integration between third-party apps and banks for years, but that vision still hasn’t arrived. That pushed us to explore blockchain as a way to enable trustless, instant payments. SolShare grew out of both frustrations: the real student struggle of splitting receipts and the broader gap in payment technology. By combining receipt scanning, a smooth UI/UX, and blockchain settlement, we created a focused solution that makes cost-sharing transparent, secure, and effortless. What it does SolShare is a cost-sharing mobile app designed to make splitting bills with friends easy, transparent, and secure, using blockchain technology. Here’s what it does: Scan receipts : Users take a photo of a receipt, and the app extracts items and prices automatically. Assign items to friends : Each item can be assigned to a specific person, so everyone pays their fair share. Calculate totals and balances : The app automatically tallies what each person owes, avoiding messy calculations or forgotten IOUs. Settle payments instantly via blockchain (Solana): Payments are trustless and immediate, without relying on traditional bank integration. Real-time group tracking: Everyone in a group can see updates instantly. How we built it iOS / SwiftUI – Chosen for a smooth, native interface and portability; mobile app allows quick receipt scanning and on-the-go payments. Firebase – Enables real-time data synchronization across users, so balances and updates are instantly visible. Solana blockchain – Provides secure, trustless, and instant payments between users without relying on traditional banking integration. Cohere API – Handles receipt scanning and item parsing using a self-criticism learning process, reducing errors and automating item assignment. Challenges we ran into During development, we faced several challenges. SwiftUI introduced compiler issues and source control difficulties, which slowed progress at times. Coordinating work across multiple components, backend, UI, blockchain, and LLM integration, required careful planning and communication. On top of that, most of the team was new to blockchain, so learning Solana and implementing trustless payments added an extra layer of complexity. Despite these hurdles, we collaborated closely to overcome them and keep the project moving forward. Accomplishments that we're proud of We are proud of the Cohere API integration, as the parsing process was highly reliable, thanks to our system prompts, reliable JSON and self-correction architecture using the command-a vision and reasoning models. We're also proud of our integrations of the blockchain and databases. When planning the idea out, it felt very complex and we were concerned about the time constraints that were presented, but ultimately, we were able to handle most of our objectives in time. What we learned We learned a lot about full-stack development, prompt engineering and blockchain. But above all, one of the most important things we learned was perseverance. A lot of the database integration happened within the last two hours, and at times we felt as though this was unachievable, however with grit and determination, we were able to get all of our functionality across. What's next for Solshare We want to enhance individual profiles on the app by adding features like profile pictures and allowing users to join multiple groups. <div