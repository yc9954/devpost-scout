---
slug: "docugen-4-0"
url: "https://devpost.com/software/docugen-4-0"
title: "DocuGen 3.0"
hackathon: "monday Apps Challenge: Dream it, build it"
organization: "Monday.com"
winner: true
words: 270
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/document_pdf"
---

# DocuGen 3.0

> Create beautiful Google Docs using data from your monday.com boards.DocuGen allows the user to select Columns, Apply filters, Setup automated Triggers to generate, and auto save Google Docs.

[Devpost](https://devpost.com/software/docugen-4-0) · hackathon [[monday Apps Challenge- Dream it- build it]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[document_pdf]]

**stack** amazon-cloudfront-cdn, amazon-code-pipeline, amazon-dynamodb, amazon-lambda, amazon-web-services, angular.js, google, google-docs, google-drive-api, google-material, monday.com, monday.com-api, salesforce

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for docugen

## Body

DocuGen Settings Generate Document Integrations DocuGen Admin details Recent Documents Help Center Inspiration Cloud Concept was looking for a solution which allows the monday.com users to generate documents and templates from board data. The need for using such functionality was discussed many times during webinars and meetings. Since there was no easy to use option available Cloud Concept decided to develop a such application. What it does DocuGen allows monday.com user to create a google doc using their own template and data from monday.com How we built it We integrated Monday APIs using Monday-SDK with Google APIs to establish a coherent flow of information from Monday boards to google documents. It required an understanding of both Monday and Google APIs and how the structured data from Monday could be used to create beautiful documents on Google Docs. Monday's GraphQL API made it extremely easy to understand the data structure and simplify our query requests to ensure we're only pulling the data we require for final document generation process. Challenges we ran into Generating documents based on specific items only. Filtering out specific columns in the final document. Filtering out groups in the final document. Adding styles to the final document. Accomplishments that we're proud of One-click document generation from Monday board to Google Docs Filters and styling customizability for document generation based on Monday data What we learned Monday's new GraphQL API structure, document structure, ability to manipulate and visualize data, etc. What's next for DocuGen Extending the new functionalities for DocuGen users. Connecting DocuGen with O365 environments. Create custom template Placeholders (Formulas) Integration with Payment Gateway HelloSign e-Signature <div