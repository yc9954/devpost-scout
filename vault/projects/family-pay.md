---
slug: "family-pay"
url: "https://devpost.com/software/family-pay"
title: "Family Pay"
hackathon: "Hack to the Future"
organization: "Finastra"
winner: true
words: 693
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "domain/transportation"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/regulation_legal_text"
  - "substrate/web_dom"
---

# Family Pay

> Family pay increases financial inclusion of kids, by allowing them to pay on their parent's behalf, without cash or credit cards, and in a controlled, secure environment.

[Devpost](https://devpost.com/software/family-pay) · hackathon [[Hack to the Future]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[finance_payments]] [[retail_commerce]] [[transportation]]
**user** [[small_business]]
**substrate** [[financial_record]] [[regulation_legal_text]] [[web_dom]]

**stack** css3, ffdc, html5, ionic, openfoodfacts, tensorflowjs

## How they structured the write-up

- context
- what is family pay
- key benefits
- behind the scene

## Body

Context In an era of fast changing, new technologies, Open APIs, and new regulations like PSD2, we are moving towards a cashless and cardless societies . However, we still have to withdraw and give money to our kids or use our credit cards on a daily basis to pay for them. What is the problem? Kids are excluded from the financial world and restricted to pay cash or using their parents' debit/credit card. As a kid, there is also a risk of carrying cash or credit cards. Parents , on the other hand, lack of visibility and control on how their kids are spending their money. It is time-consuming as a parent to open a bank account for your kid. Merchants are still paying fees on all transactions by credit card. Banks struggle to retain customers . With Family Pay we want to build a better future for family payments leveraging on new technologies and FusionFabric.cloud APIs. What is Family Pay Family Pay is an application installed on the parents', kids' and merchants devices. Parent App After getting onboard, parents have access to their bank account balance and the transaction history of the kids. Adding a new kid is simple: the parent puts a name and a phone number, then assigns a budget on a daily/weekly/monthly basis and chooses the allowed expense categories. Payment requests within these limits are processed and approved automatically and the parent gets a notification and can view the transaction history details. Merchant App The merchant can use the Family Pay app to scan articles and generate a QR code with the amount to be payed. Kid App The kid can see how much money is available, and easily scan the vendor's QR code . A request for payment is initiated and sent to the parent device using the FusionFabric.cloud Realtime Payment Initiation API . Payment request validation & security Payment requests within the limit are automatically processed and all devices receive a confirmation message for payment success. As security is very important , we have used machine learning to train the system and detect abnormal behaviour. When an abnormal behaviour is detected, the payment transaction is pending and the parent receive a notification asking to manually accept or reject the payment . Key Benefits Kids One key goal of Family Pay is to enhance kids or teenagers' financial inclusion by allowing them to be more autonomous in their expenses. With the application, they will learn how to manage their budget and save money to fund their projects. Parents Family Pay ensures a safe and secured environment for kids payments. In that way, parents don't need to worry about cash or credit card loss of their kids and can have more control and monitoring on their expenses. It is a new way to educate on financial responsibilities. Merchants For merchants, the traffic will increase as Family Pay democratizes cashless and cardless payments and allows more people to do payments with a frictionless experience. Moreover, merchants won't pay credit card transaction charges as payments are done from account to account directly. Banks By adopting Family Pay, banks can collect and monetize data on individuals who are not customers yet, kids are potential future customers and banks can already have data on their habits. Thus, it becomes easier to offer financial services to the parent for the kids, and kids will have a complete suitable and customized experience when they will be at age of opening an account. It ensures the stickiness of families as customers of the bank. Finastra We aim to push Family Pay on Fusion Store as a real fintech would have done in its user journey. In that way, we want to inspire other fintechs to create applications with a real use-case on top of FusionFabric.cloud. It will also increase traffic on FusionFablric.cloud APIs. Finally, we plan to involve Finastra in partnerships with fintechs and charities to build a better future for family payments . Behind the scene Application implemented with: HTML/CSS/JS (UI) Ionic (UI) Node RED (API calls) Realtime Payment Initiation API from FusionFabric.cloud Open Food Facts API (Scan of food barcode) TensorFlow.js (Machine Learning) <div