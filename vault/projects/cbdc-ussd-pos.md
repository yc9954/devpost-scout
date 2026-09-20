---
slug: "cbdc-ussd-pos"
url: "https://devpost.com/software/cbdc-ussd-pos"
title: "Ripple Mobile"
hackathon: "Ripple CBDC Innovate "
organization: "Ripple"
winner: true
words: 477
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Ripple Mobile

> Transfer XRP from one phone to another, without internet access. An innovative solution for low-tech markets that improves the accessibility of CBDCs.

[Devpost](https://devpost.com/software/cbdc-ussd-pos) · hackathon [[Ripple CBDC Innovate]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[finance_payments]]
**substrate** [[financial_record]] [[structured_db]]

**stack** fastapi, python, ussd, xrpl

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ripplemobile

## Body

New Account Registration USSD Menu Account/Wallet Options USSD Menu SMS Notifications Inspiration Ripple Mobile was born out of a desire to bridge Africa's digital divide. We've crafted a solution that allows any African, even without internet access, to tap into the XRP network using just their mobile number. Central Bank Digital Currencies (CBDCs) herald a transformative promise of unprecedented financial inclusion. As of 2021, over 350 million individuals in Africa were unbanked, meaning the region is prime for a significant financial CBDC transformation. However, the adoption of CBDCs in Africa face a significant hurdle due to the fact that they require direct access to the internet, but only 22% of the continent is connected to the internet . But, there's hope in mobile connectivity. According to GSMA Intelligence, 44% of Africans have mobile phones , a figure projected to surpass 50% by 2025. What it does Ripple Mobile is a game-changer for accessing the Ripple network in Africa. By tapping into the power of Unstructured Supplementary Service Data (USSD) and the Global System for Mobile Communications (GSM) technology, Ripple Mobile ensures that anyone without access to the internet can interact with the Ripple network, with just their phone (smartphone or dumbphone). Here's how users interact with Ripple Mobile: One Step Registration : Once a user decides to register for a Ripple Mobile account, they choose a secure 4 digit pin and their phone number is automatically paired to an XRP wallet and secured with their pin. Sending XRP: Registered accounts can send XRP to other registered accounts knowing just the recipient's mobile number. This can be done from anywhere with a telecom tower connection. Account Insights: Users can use the USSD interface to view their account details, check their balance, and review transaction histories from anywhere and anytime. SMS Integration: SMS messages deliver timely account information and transaction notifications to keep users informed. How we built it We built our proof of concept using… xrpl-py library FastAPI framework Third party USSD/SMS integration Simulated our database operations using a local JSON file Challenges we ran into First time working with CBDC and XRPL technology, so figuring out how these technologies work was initially a challenge for us Securing a reliable, robust USSD extension and service in Ghana proved difficult, and their provided documentation were difficult to follow. Accomplishments that we're proud of Designing and implementing a solution that is uniquely suited to the African market and potentially other low-tech financially excluded markets around the world. What we learned This project helped us learn more about XRPL, CBDCs and USSD technology. What's next for RippleMobile Our vision for RippleMobile doesn't end here. We're looking towards: Developing a RippleMobile Point-of-Sale (POS) system to further streamline physical real world transactions without internet connection. Transition our proof of concept into a better product with more features to gain adoption and scale. <div