---
slug: "rapydpay"
url: "https://devpost.com/software/rapydpay"
title: "RapydPay"
hackathon: "Formula 0001: Rapyd Fintech Grand Prix"
organization: "Rapyd"
winner: true
words: 759
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# RapydPay

> Speeding fast checkout process at the swipe of a button. Generate and customize your swipe-able button and anyone with a RapydPay wallet can make a transaction at the swipe of the button.

[Devpost](https://devpost.com/software/rapydpay) · hackathon [[Formula 0001- Rapyd Fintech Grand Prix]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]] [[finance_payments]] [[retail_commerce]]
**user** [[developer]]
**substrate** [[financial_record]] [[structured_db]] [[web_dom]]

**stack** amazon-web-services, bootstrap, flask, mongodb, python, rapyd

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for rapydpay
- playing with the platform
- git repo

## Body

Main dashboard displaying the latest transactions as well as offering actions such as withdraw and deposit. Swipe button displayed on the bottom of a paywall article. A simple swipe will complete the checkout process. Simple checkout button generation page. Choose a currency and an amount and the button will be generated. The deposit page. Deposit from any card from anywhere. Inspiration Ever go on a news website and see "Pay only $1 to read the full article" or go on a blog that has a caption "Tip me $5 for a cup of coffee"? These are micro payments and they are simple online transactions providing your or the one requesting a few dollars. But did you ever try to complete the purchase of the article or to tip? You need to sign up, enter your details and payment details all over. Why shouldn't you have an online wallet that allows you with a simple swipe to complete the transaction? One wallet for all. What it does RapydPay is an online wallet that provides a smooth, fast and easy checkout process for online payments. The wallet allows you to transfer funds between other RapydPay wallet users and to complete a transaction in a matter of a second. How we built it The button is actually an iframe connected with the RapydPay platform domain. We are able to get the logged in user because of this. The iframe is designed to be integrated into any site easily without any design issues. You can create a JavaScript callback or add a webhook and close the full circle of a checkout process. The online wallet uses Rapyd Wallet API and the payment made between wallets is a wallet transfer. The deposit feature uses the Rapyd Collect API. The withdraw option uses the Rapyd Disburse API. Everything is built on Flask (Python) and rendered server side, the frontend uses Bootstrap with a mixed design of custom CSS and an opensource CSS library. The database used is MongoDB and the whole project is deployed on AWS. Challenges we ran into There were bugs discovered on the way but the Rapyd team did a great job at responding and helping with any issues that occurred. Accomplishments that we're proud of There are two main accomplishments: Since we developed in Python, we decided to create our own Rapyd wrapper. We believe the wrapper can allow other Python developers to integrate Rapyd API's easily and get access to a lot of additional useful utilities. We are considering open sourcing this part of the project after the hackathon. The platform is almost solely based on the Rapyd API's. Rapyd provided such rich API's that we managed to manage the wallets, balances and customers all using the Rapyd platform. The integration process we achieved makes it feel like RapydPay is just an extension to Rapyd. What we learned The finance world is complex, a lot to learn about it and things can sometimes take some time but that's okay. One step at a time. What's next for RapydPay Wow, so much. Here are the main features we would like add: If a user is not logged in to RapydPay but would like to make a transaction, we will display a normal credit card checkout form. The integrator of the button won't have to worry about it as they will recieve it normally. Create automated email receipts to be sent to the one making the transaction. Integrating a pin for verifying transactions. Additional support for bank account transfers, cash and other payment types for online transactions. Continue the development of the Python wrapper to allow more and more API calls and endpoints And more! Playing with the platform Notice the platform for the sake of proof of concept is all in USD. We support however other currencies in accordance with the Rapyd API's. You can login to two example accounts (or create a new one): pop@yopmail.com - An account with history and funds pop1@yopmail.com - The receiver of funds in the examples provided The password to both is 123456. I recommend using Google Chrome for the tests. For creating a tip transaction, view https://rapydpay.aviwolicki.com/examples/example2.html For creating a paywall transaction, view https://rapydpay.aviwolicki.com/examples/example1.html If you would like to create your own button, notice HTTPS is required on the host the button. You can use https://jsfiddle.net/ for copying the code there and testing. Git repo The Github repo of the code is located here in the rapyd temp Github account for privacy: https://github.com/Formula-0001-Rapyd-Fintech-Grand-Prix/rapyd-pay I have also added the testing@devpost.com user to the repo. <div