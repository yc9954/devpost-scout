---
slug: "rapyd-g-force"
url: "https://devpost.com/software/rapyd-g-force"
title: "Rapyd G-Force"
hackathon: "Formula 0001: Rapyd Fintech Grand Prix"
organization: "Rapyd"
winner: true
words: 314
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# Rapyd G-Force

> Provide a no-code seamless Rapyd Checkout experience using Google business tools.

[Devpost](https://devpost.com/software/rapyd-g-force) · hackathon [[Formula 0001- Rapyd Fintech Grand Prix]]

## Facets

**domain** [[finance_payments]] [[retail_commerce]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** google-apps-script, html5, javascript, mysql, php

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for rapyd g-force

## Body

Rapyd G-Force No-Code payment automation for Google Workspace Three tools to help you get paid Inspiration One day Betsy asked why cant Google Forms also help businesses accept and manage payments. Ryan a payments expert talked for 30 minutes about security, PCI, and the products limitations. But then.... after a second look at open extensibility of Google applications he realized something! If we combine it with with the power of Rapyd Checkout... Why cant it...? What it does Rapyd G-Force builds on top of Google Forms and Google Sheets to provide easy to setup, no-code payment automation, creating three different experiences: Integrated Checkout Subscription Payments Automated Spreadsheet Invoicing How we built it We leveraged a combination of the Rapyd Collect API's, Google Apps Script, PHP, and a custom hosted checkout page to stitch together a seamless customer experience. Challenges we ran into Rapyd API's require fairly complex encryption that has to be recreated in Google Apps Script. The Google Sheet Invoicing concept was brand new and required a new set of tools. We learned custom sheet functions re-load each time the sheet opens, causing us to implement new caching and local document storage to avoid creating duplicate checkouts. Accomplishments that we're proud of Building users tools rather than products empowers others to take what we've built and use them in endless new and creative ways. We have written 1000's of lines of code so others don't have to. What we learned Just how many different checkout options Rapyd supports around the world. Making a short video is hard when you have so much to share. : ) What's next for Rapyd G-Force We hope to include the Rapyd capabilities in a future release of our Payable Forms Add-On, making these capabilities readily available to anyone. We hope to build upon our idea of Rapyd spreadsheet invoicing and incorporate it into future Payable products <div