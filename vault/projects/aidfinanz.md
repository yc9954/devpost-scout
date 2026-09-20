---
slug: "aidfinanz"
url: "https://devpost.com/software/aidfinanz"
title: "AidFinanz"
hackathon: "Hack to the Future 4"
organization: "Finastra"
winner: true
words: 595
team_size: 7
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/regulation_legal_text"
---

# AidFinanz

> Aiding Financial Inclusion - AI based risk assessment model that generates credit risk rating, taking non-standard documents for the unorganized sector in India.

[Devpost](https://devpost.com/software/aidfinanz) · hackathon [[Hack to the Future 4]]

## Facets

**domain** [[education]] [[finance_payments]] [[security_privacy]]
**substrate** [[document_pdf]] [[financial_record]] [[regulation_legal_text]]

**stack** amazon-web-services, angular.js, beanstalk, figma, flask, python, random-forest, scikit-learn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aidfinanz

## Body

Introduction to AidFinanz AidFinanz Screen 1 AidFinanz Screen 3 AidFinanz Risk Meter Inspiration Unorganized sector in our country is one of the largest, most valuable and yet most ignored sector without much financial support. Due to poverty, lack of education, biases in the way they are treated, most of them stay away from banks and fall prey to money lenders who further exploit them. Most of the time they need small amounts of loans to support their enterprise or simply to help put their kids through education but with some of the reasons stated above they end up paying extremely high interest to money lenders, further pushing them down the rabbit hole. One clear way to support them is to look at their credit needs and assess personal risk on a case by case basis and help them with quick and easy access to banks, credit societies etc. This can be further enhanced by giving back discounts, rebates, creating personalized offers etc, once we track their behavior. This will give them a chance to access organized and transparent credit channels, improve their social standing through quick small value loans, create inclusivity and raise their standard of living. What it does AidFinanz is an application that performs risk assessment of individuals and creates a risk score for an applicant using an AI model. The model accepts various non standard key parameters of the applicant like school fees receipts, recommendation letters from their customers etc and will generate a risk score. Risk score will be on a scale of 1 – 10 which identifies the risk involved in providing a loan. A score of 0 to 2 indicates a higher risk in lending money. The higher the value, the risk factor decreases. The app also allows the financial institution to create custom pricing offers for the applicant as well. How we built it Sklearn Random Forest library is used to assess the applicants if they are risky or not. The binary classification machine learning model is built using Python. Loan Prediction sample data was used from datasets available on kaggle. Figma and Angular6 are used for UI. The model and API is hosted on AWS Elastic Beanstalk Challenges we ran into Unavailability of training data & hence we used synthetic data to process. Regulations will be different in different countries. The current model is proposed based on India scenario, and needs to be localized to other markets. Accomplishments that we're proud of All members of this team (except one person) are participating in a hackathon for the very first time. The team is extremely proud of taking this first step with Finastra hackathon, and for the cause #BreakTheBias. Our participation in this hackathon has inspired all of us to create more similar ideas that will help the society at large. What we learned Doing our research we learnt that the unorganized sector in our country find it extremely challenging to access banking facilities like loans, credit cards etc. and how making these available can have a huge positive impact in their lives and create more opportunities. Random forest classification for building this AI model. What's next for AidFinanz Risk score to be extended using analytical hierarchy processing. Model to be extended for other markets globally. Offer differentiated pricing. Risk score can be used in for other purposes like building the credit history. Onboard retailers to support Buy Now Pay Later options. Education and awareness. Behavioral tracking can be used to create personalized offers. Banks can give rebates and subsidies for customers to improve loyalty and retention. <div