---
slug: "approval-request-app-for-umeed"
url: "https://devpost.com/software/approval-request-app-for-umeed"
title: "Approval Request App for UMEED"
hackathon: "DocuSign Good Code Hackathon"
organization: "Docusign"
winner: true
words: 445
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Approval Request App for UMEED

> A dynamic approval request is generated and sent for signing to the manager.

[Devpost](https://devpost.com/software/approval-request-app-for-umeed) · hackathon [[DocuSign Good Code Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]] [[supply_logistics]]
**substrate** [[document_pdf]] [[financial_record]] [[video_visual]]

**stack** bootstrap, css3, docusign, html5, php

## How they structured the write-up

- the non-profit
- inspiration
- the problem
- the solution
- how docusign comes into picture
- how we built it
- what we learned
- what's next for approval request app for umeed

## Body

Logo of the non-profit Application homepage Application homepage translated to Telegu Adding recipients Custom approval form The non-profit UMEED is a NPO that empowers women from low income communities of Hyderabad, India by providing them life skills which enable them to take control of their lives. UMEED trains them to make handicrafts out of recycled products, which are then sold, with profits divided among the women. Inspiration Last year I got the opportunity to work for UMEED through the Code for Good challenge organized by JP Morgan Chase & Co. With my team we created an inventory management system along with workforce tracking and inventory tracking (how much raw material is used etc.) After I saw what DocuSign could do, I instantly thought of the only feature I could not implement during that time, and that was approval requests. The problem The women working for the NPO needed a technology solution that would record the number of handicrafts they make each day and present this record to their manager. The manager would then approve the work and only after the approval their weekly wages would be transferred to the workers. This process is manually carried out by the managers by checking the work after physically coming to the workplace and signing a receipt for each worker. This receipt was later shown to the cashier for getting their salary deposited. The solution My solution helps two users: The workers who will get a digital platform where they can put in their details and document their weekly progress in form of text and images The managers who can monitor the weekly progress and send approval receipt in the form of an e-signed document. The workers can then simply show this document to the cashier to receive their salary. How DocuSign comes into picture The DocuSign API will be used by the women workers to input details such as their name,, the date, worker number, amount of handicrafts, images of the handicrafts prepared and this information will form their receipt for approval. This receipt will be received by the managers and after complete verification they will be signed. Only the signed approval receipt will be eligible for payment. Thus the manual procedure is digitized. How we built it I took help of the send-via-email example provided in the SDK and built my code on it. What we learned Since APIs were a new thing for me, I learnt how to send and receive requests, modify base code and a lot more! It was a great learning experience. What's next for Approval Request App for UMEED A user specific login where they can check all their signed receipts <div