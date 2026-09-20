---
slug: "kypay"
url: "https://devpost.com/software/kypay"
title: "KyPay"
hackathon: "Formula 0001: Rapyd Fintech Grand Prix"
organization: "Rapyd"
winner: true
words: 909
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/developer"
  - "substrate/structured_db"
---

# KyPay

> A universal app that comes with wallet for easy payment and receiving money and a shopping market place for buyers and sellers

[Devpost](https://devpost.com/software/kypay) · hackathon [[Formula 0001- Rapyd Fintech Grand Prix]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[retail_commerce]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** apache, firebase, mysql, php, rapyd, swift, swiftui

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for kypay

## Body

KyPay app - a universal app with eWallet and shopping market place Inspiration The inspiration comes from the number of e-Wallet and fintech apps available in my country, Malaysia and being a user of one of them. As a self-taught iOS/Android developer who have developed on and off for iOS and Android native apps over the years, but having no chance to be involved or hired in the fintech and crypto industries, making me to long for developing some fintech or finance-related apps. Furthermore, during the lockdown period of my country due to the Covid 19 in the end of last year and I've picked up a new skillset based on the Apple's new SwiftUI framework for iOS app development. And I found that how amazingly quicker to develop sleek UIs based on the SwiftUI framework while compared to the traditional UIKit, Interface Builder etc. Therefore, I was eager to take the challenge to enter the hackathon as a first timer to develop some fintech-related apps with SwiftUI framework as the main core of the user interface building for the app. What it does The app is called KyPay, which is a universal app that currently consists of e-Wallet for easy payment and receiving money for its users. And it's also a shopping market place (known as KyShop), allowing its users to be buyers and sellers to pay and collect money with ease respectively. The app was designed and built with the country and currency defaulted to Malaysia and MYR respectively, although it's not restricted to Malaysia only. How I built it I'm a solo developer for this project. The app consists of developing the mobile app - iOS version, the REST API for exchanging data with the backend - which is meant for storing the user data of the KyPay app platform. The backend REST API was built with PHP and MySQL which are the backend language and database that I'm familiar with. Building the iOS app can break down into the following components and frameworks: Google Firebase authentication for letting users to sign up or sign in the app with one-time password The Swift and SwiftUI framework for the user interface. And the coding approach is based on MVVM (Model View View Model) pattern to ensure cleaner code and better reusability of components. The Rapyd iOS mobile SDK is meant for the creation of the user's e-Wallet (Wallet SDK), the top-up of wallet (Collect Payment SDK), the sending and receiving of money (Wallet SDK for transfers, Collect Payment etc), the payment for billers (Disburse SDK) and the payment and auto-split payments for shopping/checkout (Wallet transfer & Collect Payment for online banking methods etc) Challenges I ran into The main challenge is that I faced is there is a longer than expected of getting to know the Rapyd API on how it actually works. Such as one of the blockers for a day or two was without any knowledge of how to obtain the payment method ID for a selected payment method as being unfamiliar how to get more info from the Rapyd API documentation. And having to write testing code both in PHP or Swift to find out more the supported payment/payout methods etc in my country. But fortunately, most of the technical questions or blocks that I faced were able to get the answers from the supportive Rapyd dev team on Slack. The other challenge that I faced was being too ambitious for having to include too many features for the app, leaving the app with a few unfinished features such as requesting money from users, split payments by other payment options (such as bank redirect) for sellers for shopping checkout. Accomplishments that I'm proud of The accomplishments that I'm proud of are the app is able to create wallet, send money by phone numbers to other KyPay users and the most I'm proud of is the shopping cart / check out features with the capabilities splitting payments accordingly to many sellers based on one single payment by the buyer. What I learned What I learned is how to build an e-Wallet app with the Rapyd wallet SDK, and how to send payment by phone numbers by the wallet transfer and how to make payments to wallet using the Collect SDK etc. And how to build a shopping cart/check out feature with auto split-payments for buyers buying from multiple sellers etc. And I've also learned how to write my own REST API for the KyPay backend in PHP/MySQL stack and how to write the Swift part for communicating with it etc. What's next for KyPay KyPay - as a universal app, of course I wish that it can be implemented/materialised or being able to raise fund for it and implement it in a country. And it should evolve with more features such as messaging / chat capabilities for the KyPay users. The use of AI for learning and determining the best and more convenient ways for the users shopping on the KyPay shop. A separate or integrated app known as KySeller, which is meant for the sellers to upload/manage their items and fulfil their customers' orders and better communicate with their buyers etc. And of course as a developer, I wish to continue the above-mentioned unfinished features and also build a better messaging/notification part on the message section of the app with different sub-sections for the buyers and sellers to communicate / track orders etc. <div