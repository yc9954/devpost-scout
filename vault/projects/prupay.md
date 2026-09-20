---
slug: "prupay"
url: "https://devpost.com/software/prupay"
title: "PruPay"
hackathon: "Disrupt SF Hackathon 2018"
organization: "TechCrunch"
winner: true
words: 533
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/immigration_refugee"
  - "user/patient_family"
  - "user/small_business"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# PruPay

> An efficient and secure way for modern businesses to pay invoices

[Devpost](https://devpost.com/software/prupay) · hackathon [[Disrupt SF Hackathon 2018]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[health_clinical]] [[immigration_refugee]]
**user** [[patient_family]] [[small_business]]
**substrate** [[document_pdf]] [[financial_record]]

**stack** android, android-studio, firebase, google-apps-script, heroku, node.js, visa

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for prupay

## Body

Icon Inspiration "Small business isn’t for the faint of heart. It’s for the brave, the patient and the persistent. It’s for the overcomer" - Unknown Managing and tracking invoices is one of the most important aspect of running a small business. A lot of tools have been built to aid in the creation and payment tracking of invoices, however there are not a lot of modern tools help in secure payment of invoices. A lot of small businesses suffer from payment frauds, lack of cash flow and find it difficult to pay invoices on time. PruPay by leveraging VISA's Secure Commercial APIs helps small business pay invoices securely and on time thereby reducing the risks faced by a small business so that they can focus on things that actually matter What it does A small business usually receives invoices in one of the following methods Physical Invoice - PruPay allows one to directly scan an invoice and check if secure digital secure payment channel are available. We use the Visa Supplier Matching Service to allow a small business to directly pay the supplier. Email Invoice with payment information or payment link - PruPay provides mail plugins to automatically create and track an invoice on the PruPay app once an Invoice is received. We use NLP to parse the email and identify the invoice details and payment information. The provided payment information / payment link is verified for frauds and risk using the Visa risk and fraud APIs Directly in your Finance Tool - Going ahead PruPay would also be integrating with financial management tools to provide secure payment options. Once the invoice is identified and added to the PruPay platform, the small business owner can then track the invoice, protect against fraud and pay invoices using virtual payment account that are generate using Visa's B2B Virtual Account Payment APIs there by avoiding sharing of sensitive account information to multiple vendors and protecting against unnecessary headaches. How I built it PruPay app is built using the native Android SDKs for better security. The backend is hosted on Google Cloud and leverages Firebase tool set for user authentication, encrypted data storage, notifications and analytics. A Node.js API gateway is used to authenticate with Visa API network and abstracting the complexity so that the mobile app is light and better performant. It is hosted on Heroku. Google Apps Script was used to build a gmail plugin to scan for invoices. Challenges I ran into Since this project uses several technologies it was challenging to figure out a way to connect different systems and their interaction. Also understanding the Visa API network security mechanisms was challenging as this was a relatively new field Accomplishments that I'm proud of Building a complete platform with so many different technologies. What I learned A lot of things can break for reasons unknown in an integrated system and the best way to deal with this LOG everything. The trails of bread crumbs always leads to the culprit:P! What's next for PruPay Parse PDF and paper invoices to generate digital invoices Automatically detect supplier and pay through Visa direct secure channel Integrate with exisiting invoicing tools Provide financing options Make Money! <div