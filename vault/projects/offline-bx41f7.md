---
slug: "offline-bx41f7"
url: "https://devpost.com/software/offline-bx41f7"
title: "iBonus Offline Payment for retail CBDC"
hackathon: "Ripple CBDC Innovate "
organization: "Ripple"
winner: true
words: 613
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "domain/transportation"
  - "user/small_business"
  - "substrate/financial_record"
---

# iBonus Offline Payment for retail CBDC

> With the XRPL and our Offline DLT technology, payments can now be made with both smartphone and POS offline. Offline payment is one of the biggest challenges of retail CBDC.

[Devpost](https://devpost.com/software/offline-bx41f7) · hackathon [[Ripple CBDC Innovate]]

## Facets

**domain** [[finance_payments]] [[retail_commerce]] [[transportation]]
**user** [[small_business]]
**substrate** [[financial_record]]

**stack** android, java, xrpl

## How they structured the write-up

- offline inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for offline

## Body

Offline Inspiration One of the biggest challenges for retail CBDC (cashless payment) is offline payment. “To provide cash-like payment experience, the ability to handle peak traffic as well as connectivity breaks or offline” Bank of International Settlement. “To provide an “enhanced operational resilience of the payment system, designed with offline capability, that allows some payments to be made without internet”, US Federal Reserve. Our team has over 20 years of experience in offline payment systems based on smart cards. Over 100 systems, with 2 million users deployed worldwide. In 2007, we deployed an offline system for the US Army in Afghanistan & Iraq where the Internet was not available. In 2014, iBonus Limited was established to develop a smartphone version of offline payment. Smartphones are ubiquitous even in developing countries. What it does Popular mobile payments such as Venmo, Alipay, PayTM, Google Pay, and CashApp for retail payments won’t work without the Internet. Our mobile payment solution is designed to work “dual offline” where both digital wallet and POS device have no access to the Internet. How we built it In a typical online payment, the user's smartphone displays a QR code and is scanned by the POS device. It is then directed to the payment server and completes the transactions. When there is no Internet (dual offline), transactions are done thru direct communication between the user's smartphone and POS device using a QR code and BLE (Bluetooth Low Energy). Based on payment info such as Invoice ID, r-address, and $ amount, the user sends a signed XRP “Check” with a ticket of pre-registered sequence number to the POS device. The “Check” will be created on a blockchain either by the user's smartphone or POS and cashed once the Internet is available. We don’t use “direct payment” as it leaves no trace of failed transactions on the blockchain if the user does not have sufficient funds; on the other hand, “Check” can be created with no restriction, a record to be traced, and re-cashing when the funds become available. Challenges we ran into XRPL is not designed to handle offline payments as ledgers are on the blockchains. An external mechanism is needed to avoid overspending or double-spending in offline situations. Our approach is to use our award-winning “Offline DLT” technology, by having users carry their own ledger for verification offline, and two trusted systems used by the credit card payment industry to avoid the ledger from illegal modifications. IP US Patent Pending 16/681,365 China Patent Pending 201910340975.1 Accomplishments that we're proud of Awards: 2020: UK Juniper Research Gold Award - Mobile Payment 2021: HK Fintech Award: Offline DLT - CBDC 2022: HK ICT Fintech Award: Offline DLT CBDC 2022: CBDC Finalists by Hong Kong Monetary Authority Milestones of CBDC development: 2020: Integrated with Paypal wallets 2020: Sandbox of e-Yuan CBDC with HSBC Bank 2022: Entitled to participate in Rail 2 - e-HKD CBDC pilot What we learned We have been in the business of offline payment for over 20 years in smart card prepaid systems. Our solutions are mainly close-loop single merchant payment systems because the development of clearing and settlement systems is very costly and complex and require high-security standards. With XRP blockchain, it allows us to provide offline payment as well as online payment with instant settlement with minimal effort. What's Next for Offline By leveraging the security and trust of XRP blockchains, we can provide the world’s most complete, secure, and trusted mobile payment solution for retail payment online and dual offline with instant settlement as well as ISO20022 compliance. A huge opportunity as led by SWIFT, all legacy banking payment systems will be converted to ISO20022 by 2025. <div