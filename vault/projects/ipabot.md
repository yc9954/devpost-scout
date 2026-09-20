---
slug: "ipabot"
url: "https://devpost.com/software/ipabot"
title: "IPABOT"
hackathon: "Automation Anywhere Bot Games"
organization: "Automation Anywhere"
winner: true
words: 414
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# IPABOT

> Theme - Finance - Accounts Payable Overview: To use RPA technology along with AI & ML based OCR extraction using IQBOT & integrate with AARI to automate the end to end Invoice Process for AP Dept

[Devpost](https://devpost.com/software/ipabot) · hackathon [[Automation Anywhere Bot Games]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[finance_payments]]
  <sub>weak: labor_employment</sub>
**substrate** [[document_pdf]] [[financial_record]] [[structured_db]]

**stack** aari, access, api, database, framework, gmail, iqbot, modular, powerbi, python

## How they structured the write-up

- theme - finance - accounts payable invoice process automation using iqbot integrated with aari virtual assistant
- inspiration - invoice processing is a mundane repetitive task performed by accounts payable team across the industry. also team spends more time for providing invoice status to vendor(prod support) which is labor intensive
- what it does - automating end to end invoice process for accounts payable department. also integrate with aari for prod support to reduce the time being spent bu business
- how we built it -
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ipabot

## Body

Project Name Project Overview, Problem Statment, Solution & Technology Process Design AARI Design Benefits Detailed Process Swim Lane Diagram Database Design Development BOT Checklist Project Dashboard Learning Instance Daily Trend Dashboard Theme - Finance - Accounts Payable Invoice Process Automation using IQBOT integrated with AARI virtual assistant Inspiration - Invoice processing is a mundane repetitive task performed by Accounts Payable team across the Industry. Also team spends more time for providing Invoice status to Vendor(PROD Support) which is labor intensive What it does - Automating End to End Invoice Process for Accounts Payable Department. Also integrate with AARI for PROD support to reduce the time being spent bu Business How we built it - Created Project Workflow design Database Design Created IQBOT Learning Instance and trained Invoices with ABBYY engine Created re-usable Python code for data processing during IQBOT training(Ex: converting Date to required format) Created Modular task bot for Email attachments download, IQBOT upload & download. Merge csv file data to Access database Created AARI web form and built task bot to fetch Invoice details for Human verification Challenges we ran into Unable to create hyper link in Gmail notifications. Workaround: Created file path as text instead of hyperlink Ran into Database insertion error due to Data type mismatch which was solved after research File copy & delete intermittent errors. Workaround: Provided delay and condition to check if file size is same in source & destination folder Accomplishments that we're proud of We have come up with complete SDLC process, so it can benefit anyone seeing our Project and can implement the project with ease with all different templates provided in submission Detailed design for Project process Detailed database design Modular task for re-usability Credential vault implementation to avoid changes of critical variables Unit testing of all the modules Creation of Dashboards using Power BI Created IQBOT LI dashboard as IQBOT Control room doesn't have Drill down functionality to see the trend Creation of python re-usable functions for IQBOT data processing What we learned Usage of A360 platform as we were mostly on AA v11 for last couple of years Bot games helped us to learn different packages and connect with Dev community and learn different approaches to solve problems by increasing the efficiency IQBOT success tips What's next for IPABOT To scale up the project across different departments To process other unstructured documents and effectively utilize IQBOT capability To provide the document view directly in AARI web form for Business users <div