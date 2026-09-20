---
slug: "disposable-digital-wallets-pointcheckout"
url: "https://devpost.com/software/disposable-digital-wallets-pointcheckout"
title: "Disposable digital wallets - PointCheckout"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 980
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "user/developer"
  - "user/general_public"
  - "user/small_business"
  - "substrate/financial_record"
---

# Disposable digital wallets - PointCheckout

> Financial Support distribution to the unbanked and non-tech is hard, micro funds can still be sent through 'disposable' digital wallets that are blockchain secured and centrally distributed

[Devpost](https://devpost.com/software/disposable-digital-wallets-pointcheckout) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[civic_government]] [[finance_payments]] [[immigration_refugee]] [[labor_employment]] [[retail_commerce]]
**user** [[developer]] [[general_public]] [[small_business]]
**substrate** [[financial_record]]

**stack** api, blockchian, java, javascript

## How they structured the write-up

- inspiration
- the problem your project solves
- what it does
- the solution’s impact and value proposition
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- team behind it
- what's next for disposable digital wallets - pointcheckout

## Body

GIF How to withdraw funds from the ATM/teller GIF Process to register in the wallet once issued Inspiration Not everyone is tech savvy to handle digital finance, nor is there a one size fits all digital wallets that dont require both parties to have an app. There is 'disposable' everything, and why not the same with digital wallets for one time use implemented for distributing aid and financial support, requiring no app downloads or need for any tech on the receiving end. This is why we worked on this project, especially realizing the solution needs to be simple, scalable, and easy to use. The problem your project solves Distribution of public (micro)funds to citizens in the good days is very fragmented, and in times of crisis such as during the COVD pandemic the pressure on quick distribution is immense. The biggest problem is the vast difference between citizens in all dimensions be it age groups, locations, welfare situation, banked or unbanked etc, makes a common solution difficult. The need is for a scalable, simple to use solution to distribute funds that is also traceable, ye using the existing infrastructure as time is of the essence to get to as many people as quick as possible. What it does PointCheckout intends to use QR code technology to issue a digital 'disposable' wallet with credit for distribution of funds to citizens or merchants alike, sent through messages such as sms or whats app, etc. Each issued code and its details could be recorded on a blockchain ledger to prevent fraud, and the QR code could be displayed in any form, on a browser, mobile, even printed. The wallet could be used several times till amount is depleted, then it is disposed. For redemptions, the owner of the wallet has 3 options: cash withdrawal from an ATM or bank teller (possibly post office), direct purchase at a participating merchant, or transfer the wallet balance to an existing bank account if available. The distribution of the wallets takes place through a central issuing API platform based on inputs of Name, phone number, date of birth, citizen/social security number, and wallet amount. The solution’s impact and value proposition The creation of the digital wallets by an authority is done within hours instead of weeks, and hundreds of thousands of citizens can then receive it instantly reducing the current rollout times by over 80%. After claiming and authenticating, receivers can immediately spend the wallet amounts or cash it out at the local ATM/bank branch or merchant. Speed is of the essence, and we believe this achieves the main goal while remaining secure, yet at the same time grandma-friendly. How we built it PointCheckout’s disposable digital wallet was initially created to address the need to issue credit to users to speed up access to refunds from our core payments business to provide instant access to funds compared to issuing refunds through existing payment schemes. Our initial design focuses on creating a temporary wallet that can hold a fixed amount of funds and would allow debit transactions across the different channels we support. During this past weekend, we have repurposed our temporary wallets as a standalone offering allowing operators to credit funds through a centralized account and use those funds to feed value into the individual wallets of the registered wallets. We also added a layer for wallet identification and verification that is both multi-lingual and multi-channel allowing citizens to access these wallets in a secure and transparent manner via technologies such as SMS, WhatsApp, Messenger, and more. Our platform is built using a mix of technologies Amazon Webservices (Elastic Beanstalk, SQS, S3, SNS, RDS, KMS, and DynamoDB) Spring Framework Java and Hibernate PointCheckout’s infrastructure is hosted at AWS Ireland Data Center with a fail-over configured for AWS Frankfurt. We are PCI Certified (Service Provider). Challenges we ran into The issuance platform of the digital wallets has been built and tested, the major issues were finding out the different existing funding distribution systems, as many countries have varying infrastructures and varying requirements even within the same country. This is still work in progress, and we would need to validate who are he best target groups for this. This solution essentially could also work for unemployment benefit or refugee assistance, so further investigations is needed into the user base with most needs. Accomplishments that we're proud of The system to issue wallets is ready, and has been tested with approximately 50 different numbers. A simple redemption app to provide to an (agent) merchant or bank teller is also ready. The team working together though was the best achievement, they pulled this off in record time. Team behind it Our team has experience in fintechs, loyalty and also e-commerce, with the founders already working on their 4th startup. Our experience combines employers such as Rocket Internet, Meryl Lynch and BlackRock, and a team of great engineers. We are also backed by Startupbootcamp Accelerator, 500 startups and several other VCs. What's next for Disposable digital wallets - PointCheckout What is needed as next steps is to identify with the stakeholders who are the best target users who need this the most, for example places where there is already an existing welfare fund distribution process through local post offices might not be in dire need vs older population remote areas. This needs to be identified with the authorities first and a selected municipality for testing also selected assuming this project is approved. Secondly, working with the banks to find the best way to allow wallet holders to cash in, be it at the bank branch or at the ATM. Ideally we would have their involvement for scalability without the need for any integrations with their core systems. PointCheckout could complete this project including testing in under 8 weeks with the above input and have the first digital wallets distributed and tested. <div