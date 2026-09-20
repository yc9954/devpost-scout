---
slug: "bethechange-tucfl5"
url: "https://devpost.com/software/bethechange-tucfl5"
title: "Be The Change"
hackathon: "Hack to the Future 2020"
organization: "Finastra"
winner: true
words: 613
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Be The Change

> Microdonations compounded to make a big impact.

[Devpost](https://devpost.com/software/bethechange-tucfl5) · hackathon [[Hack to the Future 2020]]

## Facets

**domain** [[finance_payments]]
**user** [[general_public]]
**substrate** [[financial_record]] [[web_dom]]

**stack** figma, finastra, gcp, react-native

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for be the change
- pitch deck

## Body

Home screen Location enabling Browse charitable causes in organization view (containing established NGOs) and community view (featuring local crowdfunding campaigns) Set your donation amount to be distributed by one lump sum or recurring over a determined period of time. Inspiration We believe the biggest barrier to donating to charities and community causes is the extensive deliberation that comes with donating one lump sum: researching where to donate, wanting to ensure you're donating wisely, and the perceived responsibility of making a one-time donation. Inspired by Bank of America's successful "Keep the Change" campaign, we adopted a similar model to drive social impact. What it does Be The Change rounds up every purchase you make on your linked bank cards to the nearest dollar, donating the difference to a charity of your choice - either an established organization, or local crowdfunding causes in your community. Since microdonations take a while to compound into substantial donations, users can choose to set their donations either by dollar amount or by time period with a total donation limit. For example: Ivy wants to put her change to good use. She logs into Be The Change, and finds a cause she'd like to support. She wants to donate up to $15 monthly to this cause, so she sets up a recurring monthly donation with an upper limit of $15. By the end of the month, Ivy will have donated either $15 or a slightly lesser amount - whichever comes first. This process removes the mental hurdle involved in donating money to charitable causes, allowing one to make an impact without feeling their wallets lighten. How I built it React Native for building a cross-platform mobile app Positionstack API for reverse geocoding GCP Functions to build a wrapper for Finastra APIs Finastra APIs used on FusionFabric Cloud: Accounts, Alerts, Bill Payments, Payments, External Transfers, Consumer, Financial Transactions, Payment Requests, Good Funds, Internal Transfers Created an Application on the Finastra Platform Added B2B and B2C API services as needed by our use case Setup OAUTH2 cycle using GCP to host a redirect URL Integrated frontend (App) functionality with backend endpoints Released under the Open Innovation License Challenges I ran into Some technical challenges we encountered while building included: Learning and navigating the entire suite of Finastra APIs and platform Abstracting Authentication for multiple access via proxy Pooling microtransactions to optimize transfer/payment charges Accomplishments that I'm proud of We're proud of creating an altruistic product that has tremendous potential at scale. We believe any big impact is the result of many little changes (pun intended), and Be The Change has the power to bring about that change where it's needed most. What I learned We learned how to collaborate with an international team across timezones on a tight schedule, and how to iterate quickly and often. We also learned Finastra provides a wide plethora of APIs and services for financial transactions, payments, transfers and account management, making it the perfect tool for a product like this. What's next for Be The Change Immediate next steps would be to conduct usability testing on Be The Change to gain insight on any user pain points and opportunities to make the user flows even more intuitive. Ideally, we'd also discuss design impact and product viability with key stakeholders. Thinking ahead, we would love to incorporate a social element to the app, where users could see and discover both organizations and crowdfunding causes based on what's trending in their network, either by location or contacts. Beyond this, we'd love to introduce suggested charities and crowdfunding campaigns for users based on their previous donation habits and what's trending in their network and location. Pitch Deck https://www.canva.com/design/DAEQ6kA0s_s/U8D25fppH9PkyToIFv5L_g/view?utm_content=DAEQ6kA0s_s&utm_campaign=designshare&utm_medium=link&utm_source=sharebutton <div