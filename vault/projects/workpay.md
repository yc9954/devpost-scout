---
slug: "workpay"
url: "https://devpost.com/software/workpay"
title: "Workpay"
hackathon: "Formula 0001: Rapyd Fintech Grand Prix"
organization: "Rapyd"
winner: true
words: 1194
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Workpay

> End-to-end digital finance management platform for companies and their employees.

[Devpost](https://devpost.com/software/workpay) · hackathon [[Formula 0001- Rapyd Fintech Grand Prix]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[retail_commerce]]
**user** [[small_business]]
**substrate** [[financial_record]] [[structured_db]] [[web_dom]]
  <sub>weak: code_repository</sub>

**stack** firebase, node.js, react-native

## How they structured the write-up

- why workpay and what is that?
- how it works?
- what’s included in workpay?
- where can i sign up?
- what’s next?

## Body

Workpay Account Management Total Rewards Statement Automatic reimbursements of company spendings Savings with Pockets Wallet and bank transactions Credit card management Cashback Deals Good to know before you start: Workpay is not a design concept, but a completely functional application that implements all features mentioned below. Make sure to see for yourself with the provided codebase. 😉 Why Workpay and what is that? Corporate finance is lagging behind digital transformation and while users are looking for a complex digital financial experience, companies fail to provide even the most basic methods digitally. At the same, targeting employers can offer access to a large pool of users in a B2B2C model, however only if the partnership improves their employee engagement, the most important HR performance indicator in 2021. Workpay combines these two opportunities into a single platform: end-to-end digital finance management for companies and their employees. In a single step, it transforms all financial tasks and transactions into a digitally mature environment while the excellent user experience of the Workpay App simply satisfies the needs of employees and improve their engagement toward their employer. There are two ways to use Workpay. Employers and HR departments get access to the Workpay Admin website, which handles all official administration, including payroll, benefits or reimbursements. At the same time employees can use the Workpay App, a digital wallet that includes their personal finance information and offers a rich set of features related to them. How it works? The Workpay ecosystem was built on top of Rapyd APIs. It utilises Rapyd Wallet, Issuing and Disburse features to provide an all-around personal finance experience. Workpay uses Firebase as its backend, augmenting the Rapyd APIs into features such as the cashback, auto-reimbursement or savings management. At the same time, Firebase Cloud Functions are listening to Rapyd webhook calls to store and mutate user-specific information into a Firebase Realtime Database. As the application has to be available only for registered employees, authentication was implemented using Firebase as well. The app itself was developed with React Native, the perfect framework for quick prototyping in projects like Workpay. This way the application is natively available on both iOS and Android. To speed up the development of Rapyd features, a custom module was built that transforms a Rapyd Postman collection into a Javascript callable SDK class. This allowed us to avoid heavily repeated code segments and resulted in much cleaner code. A simple proxy server was also created to handle the Rapyd authentication requirements. What’s included in Workpay? Account management With the Rapyd Wallet API, Workpay offers full-scale account management features. Users can manage accounts in multiple currencies, top up accounts and access detailed reports of transactions as well. The application intelligently recognises and augments transactions, and displays not only Rapyd stored information, but also related merchant, category, cashback and reimbursement data. For each account, the app offers statistics with charts and personalised insights, including the transactions related employer as well. Transfers Workpay supports two ways for transferring money. It offers wallet to wallet transfers, the default method for coworkers to handle payments between each other. As every employee own a Workpay wallet, this is incredibly powerful and has the potential to digitalise transactions that would otherwise happen with cash. When a new payment is initialised, all accessible employee wallets are available as the destination. Wallet to wallet transactions are completed instantly, and the receiver is notified about the incoming payment. Workpay also offers regular bank transactions using Rapyd Disburse. To improve the user experience, once a beneficiary’s information is typed in, it gets stored to the wallet, speeding up all future transactions. Savings management with Pockets With the help of on hold funds, Workpay provides an effective way to manage short- and long-term savings. Users can create financial goals such as a simple Summer Trip or bigger life events like a college fund or retirement. Once a Pocket is created users can add money to them anytime and also withdraw some if required. With Workpay it’s also extremely simple to build a habit of regular saving, as transferring any given amount of fund to the Pocket can happen automatically right after the monthly salary arrives at the wallet. Credit cards When new Workpay users are registered by their employer, Workpay cards are also issued by default, to incentivise them to become regular users. Workpay implements the complete credit card management process of Rapyd, including the display of cards, activation, blocking, unblocking and PIN modification. Users are also able to issue new cards for themselves with a customised look of their preference. Reimbursements A great feature related to issued cards is making it super easy to reimburse company-related spendings. When a card transaction is made, the users can mark the payment as company cost and if the HR department approves, the given amount is instantly transferred to the user’s wallet. Employers can also set up auto reimbursement for users based on merchant category codes. When a user asks for reimbursement with such MCC, the request is automatically approved without further action required. Cashbacks Discounts and deals have always been an essential part of the employee benefits packages. They are easy to understand, and in general, people are simply attracted to discounts. Workpay offers an all-around Cashback module, that encourages employers to work out exclusive deals with merchant partners. This way employers can easily set up their own cashback program, with partners who are the right match to their employees. When a card payment is fulfilled at one of these merchants, Workpay instantly initiates the cashback refund to the user’s wallet. Users can browse the available discounts in the application, see what deals are offered nearby and also follow the amount of cashback they made via Workpay. Total Rewards Employees are often not aware of the real costs to their employers. The Workpay Total Rewards Statement displays all salary, benefits and other rewards information in an easy to understand format and becomes an essential part of building employee engagement. When employers set up a rewards scheme for a user, they can also opt-in to handle all related transactions automatically. In this case, Workpay regularly transfers the given salary to the employee’s wallet and also handles the payments to external beneficiaries, such as tax administrations or insurance companies. Related to total rewards, users are also able to review all transactions initiated by their employer in one location. This helps to be up to date with the arrival of salaries and other bonus payments. Where can I sign up? We like your enthusiasm! 🙌 Workpay was developed specifically for the Rapyd Formula 0001 hackathon and now operates in beta testing. When we are satisfied with the performance of the application we make sure you are going to be among the first ones to be notified. We also created a website at http://workpay.digital to share further details. What’s next? Although Workpay is completely functional, we already see areas ready for improvement. More complex error handling, wider region support, performance improvements and in general, deeper testing for edge cases are required. At the same time, we are working on more features to offer, such as subscription management and group payments. <div