---
slug: "friends-reference-bureau"
url: "https://devpost.com/software/friends-reference-bureau"
title: "Friends Reference Bureau"
hackathon: "Hack to the Future 4"
organization: "Finastra"
winner: true
words: 600
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/patient_family"
  - "user/small_business"
  - "substrate/structured_db"
---

# Friends Reference Bureau

> A platform that enables peer-to-peer lending to build a credit score and later on access loans from creditors on the platform

[Devpost](https://devpost.com/software/friends-reference-bureau) · hackathon [[Hack to the Future 4]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[finance_payments]] [[retail_commerce]]
**user** [[patient_family]] [[small_business]]
**substrate** [[structured_db]]

**stack** css3, django, html5, javascript, python, sqlite

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what we learned
- what's next for friends reference bureau

## Body

Logo Login Page Home Page Loan Application Pending Loans Credit history page Financial Education Platform Inspiration Friends borrow from each other from time to time and sometimes others fail to pay back. This application aims to create credit scores based on the borrowing and payment patterns of its users. According to the 2018 digital credit survey, 35% of Kenyans (roughly six million people), most of them youth, had taken at least one digital loan of which some of them have very high interest rates (some over 300% pa). Also majority of Kenyans (82.4%) are willing to continue borrowing digital loans to invest in businesses including stocks: 62% of these borrowers go to digital lenders as their first option, then to family and friends. This application hopes to provide an easier and safer way of borrowing funds from friends and relatives. You can view an article on the Borrowing cycle among Kenyans here What it does This application provides a platform for its users to borrow and repay loans from friends and family. If a user needs a loan, he/she makes a request to a friend/family member to grant them a loan. The friend/family member receives the request and views the user's credit history on the application and based on that, they can decide whether to accept or reject the person's loan request. If a loan is approved, the loanee receives the money on their e-wallet on the platform and they can withdraw it for their use. The loanee can then start making payments(through the application) to their family or friend and pay the loan in full (with little or no interest) before the end of the payment period. How I built it This application is built using Python's Django framework for the backend and HTML5, CSS3, and JavaScript for the frontend. It is also using the Sqlite3 database (to be change to Postgres later) to store all its user data and build credit scores from the data gathered. Challenges I ran into I was hoping to build a machine learning model to help out the users to make better decisions when giving out loans to their friends/family but since this is a new application, I do not have sufficient data to build a model to that yet. Hopefully when the application is up and running, I will gather enough data to make a highly accurate prediction on whether a person will pay back a loan given previous payments habits of users with similar characteristics Accomplishments that I'm proud of I was able to come up with a flow of how persons would access the platform, access loans and make payments with minimal risk to the platform as it would only charge a facility fee and not put up the capital used to give out loans. What we learned We learnt that the people of Kenya have a high affinity to take out loans and these loans are instrumental in growing their businesses and paying day-to-day bills and expenses. It is therefor crucial to ease the loan process while also providing low interest loans so that they can be able to pay back. What's next for Friends Reference Bureau This application will start off with peer-to-peer lending and later on progress with merchant accounts where lenders will be allowed on to the platform and provide loans to deserving users based on their credit scores on the platform. The application with also have a machine learning model to predict the probability of default with will be an extra data point in helping lenders make better decisions to reduce the default rate <div