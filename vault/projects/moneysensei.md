---
slug: "moneysensei"
url: "https://devpost.com/software/moneysensei"
title: "MoneySensei"
hackathon: "ShellHacks 2025"
organization: "init"
winner: true
words: 436
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# MoneySensei

> Smart student budgeting app that gives students from monthly financial plans to personalized tips with an AI-generated financial education section that make students stay on top of their finances.

[Devpost](https://devpost.com/software/moneysensei) · hackathon [[ShellHacks 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[finance_payments]]
**user** [[educator_student]] [[researcher]]
**substrate** [[document_pdf]] [[financial_record]] [[sensor_telemetry]] [[web_dom]]

**stack** base44, javascript, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for moneysensei

## Body

Inspiration Many college students struggle to make sense of their finances because their transaction histories live in unstructured PDFs, their income is irregular, and their financial literacy is still developing. Manually transcribing and categorizing expenses, combined with the lack of timely guidance, leads to overspending, missed savings opportunities, and elevated stress during the academic year. What it does Money Sensei converts a student’s monthly transaction PDF into clear, actionable insight. The Advanced Analytics screen provides summary metrics—total expenses as a share of income, monthly income with transaction counts, savings rate with status feedback, and a top 10 expenses for the month section—alongside a category breakdown to reveal where money goes. It operationalizes the 50/30/20 framework by comparing actual allocations to the ideal distribution for needs, wants, and savings. The financial literacy tab complements the analytics with concise, context-aware lessons—students can learn “why this matters” exactly where a behavior change is needed. Money Sensei is designed to improve financial outcomes with minimal user effort: faster time-to-budget, better visibility into spending, and measurable increases in monthly savings The modular design supports a mobile version, making the solution both portable and extensible. How we built it We built it with Base44 platform where we used AI prompting to build the app, and the code uses JavaScript for the back-end and React for the front-end. Challenges we ran into The app is not integrated with a Bank API since the Base44 platform doesn't support that to give real-time and up-to-date data for the recent transactions section. However, the platform supports PDF file uploading, so students can upload their most recent bank statement to get their financial plan personalized to their most current transactions. Accomplishments that we're proud of We're proud of being able to help students across the US that are struggling to keep up with their financials making them have peace of mind and focus more on their studies since the app has everything organized and handy for them. What we learned We learned how to use the AI prompting feature with a lot of detail on the Base44 platform to create and design our app from scratch and give it the feel that we needed. What's next for MoneySensei What's next for MoneySensei is to integrate a Bank API to give students real time and up-to-date data about their recent transactions just connecting to their bank through logging in on their respective bank's website and share their bank information with the app. That way it gives a better, improved and real time financial plan with their most up-to-date data from their recent transactions until the current date. <div