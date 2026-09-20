---
slug: "rapydbot"
url: "https://devpost.com/software/rapydbot"
title: "RapydBot"
hackathon: "Formula 0001: Rapyd Fintech Grand Prix"
organization: "Rapyd"
winner: true
words: 1245
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# RapydBot

> RapydBot is a Conversational User Experience designed for Telegram Messenger applications.

[Devpost](https://devpost.com/software/rapydbot) · hackathon [[Formula 0001- Rapyd Fintech Grand Prix]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[developer_tools]] [[finance_payments]] [[retail_commerce]]
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]] [[structured_db]] [[web_dom]]

**stack** grpc, mysql, node.js, rapyd, telegram, typescript

## How they structured the write-up

- summary
- inspiration
- considerations
- what it does
- how we built it (technical details)
- business details
- what's next for rapydbot (upcoming features)
- community contributions

## Body

Official Rapyd Bot Telegram username Summary @rapydbot is a Conversational User Experience designed for Telegram Messenger applications. Using the Telegram Bot API, @rapydbot implements some of the Rapyd API’s features to allow any Telegram user to create a Rapyd e-wallet, top up its balance using their card, cash payment or a bank transfer, and use that money in a variety of ways to create innovative chat economies, all within the Telegram interface. @rapydbot architecture does not limit itself to be integrated with other chat interfaces and applications such as WhatsApp. @rapydbot fits inside the category of social payments applications, such as Venmo or WeChat. Inspiration As of 2021, a variety of FinTech applications and APIs that allow developers to build robust user experiences for international payments, wallet management, mass disbursements and settlements, already exist; however, most of these applications are either a mobile/native application or a web dashboard mostly tailored for accounting managers and employees. We decided to create @rapybot inspired by Telegram Bot API's flexibility and Rapyd's extensive documentation. Building on top of Telegram (or other chat interfaces) provides us developers with these advantages: We do not have to focus our energy on building a frontend Any Telegram user can access @rapydbot just by searching for its name and create a Rapyd e-wallet with zero friction, allowing for massive user adoption of Rapyd's technology In order to use @rapydbot at its fullest, 2 or more users with a Rapyd e-wallet must exist, which makes any engaged Telegram user more likely to invite their friends When a community of users have @rapydbot set up, a variety of use-cases come up (see use-cases for more) Considerations @rapydbot does not replace a bank account (yet). However each user's Rapyd e-wallet could, in the future, become an account that may be used with other integrations such as allowing the users' access to a debit card or to have multiple e-wallets. Withdrawal of the funds is not possible without an OTP generated with the Rapyd SDK. Meaning that users may not be able to withdraw their funds directly through the Telegram interface. We see this optimistically since the @rapydbot API could evolve to be a native application with wallet-like features. @rapydbot is running on Sandbox Mode. In order to run it in Production Mode, the open-source bot owners need to pass the KYB checks. What it does To use @rapydbot’s features, a Telegram user can call these commands: /start - Responds with initial instructions to create a Rapyd e-wallet. /setcountry - Responds with a list of available countries and currencies to set the Rapyd e-wallet default currency_code and country_code. /setcurrency - Responds with a list of available currencies to set the Rapyd e-wallet default currency_code. /createwallet - Responds with a Rapyd e-wallet address and its Telegram username reference. The Rapyd e-wallet has been set to use the country_code and currency_code chosen with /setcountry and /setcurrency. /topup - Responds with an amount request to create a Rapyd checkout page URL. /balance - Responds with a balance summary of the user’s Rapyd e-wallet according to its default Currency. /transfer @username [amount] - Responds with a confirmation message to transfer an amount from the user’s Rapyd e-wallet to another Telegram user Rapyd e-wallet. If the recipient user does not have a Rapyd e-wallet yet, the command will notify the sender. /help - Responds with a list of the available commands How we built it (Technical Details) @rapydbot depends on 3 main directories: /bot, /wallet and /user. /bot is a NodeJS server written in Typescript that starts a Telegram Bot instance and listens for Rapyd webhooks. The server will send Bot replies upon a webhook POST call as well as reply to a Telegram user commands. /wallet is a NodeJS microservice written in Typescript that features its own MySQL database and a gRPC server to communicate with /bot. This microservice handles Rapyd e-wallet creation, balances, transfers and checkout pages. /user is a NodeJS microservice written in Typescript that features its own MySQL database and a gRPC server to communicate with /bot. This microservice handles Telegram users’ information such as user handles and chat ids. About the code @rapydbot’s source code is available at: https://github.com/aufacicenta/rapydbot Follow the README.md file to learn how to run an instance of your own Telegram bot. @rapydbot is licensed under the MIT License. Infrastructure The infrastructure was implemented on a cloud-native architecture on AWS using Kubernetes to enable simplified and quick administration, monitoring, automation, and scalability. The best practices and recommendations of the Well Architected Framework are followed to build a secure and efficient for the cloud. Business Details The vision behind @rapydbot’s development is to create a wide base of Telegram users with a Rapyd e-wallet. The core developers can analyse the Bot’s adoption by querying the user and wallet databases, as well as using the Rapyd’s production dashboard to know the aggregated and specific balances of the users. Once the adoption stage is complete, any Telegram user with a Rapyd e-wallet can start using a variety of features programmed into @rapydbot such as: e-commerce checkout experiences, crypto trading, lending, betting and games, to name a few. @rapydbot being open-source code can also allow other developers to deploy their own Telegram Bots and program their own experiences employing their Rapyd’s API keys. @rapydbot is programmed in such a way that allows the wallet API (topup, balance, withdraw, etc) to be used with other technologies such as Whatsapp APIs, Google’s Dialog Flow, Web and Mobile applications. Use Cases Marketplaces @rapydbot can be used inside marketplaces (Telegram groups where users post offers of any kind) and close deals by transferring money from the buyer's Rapyd e-wallet to the seller's e-wallet. Cryptocurrency Exchanges Telegram users can send money from their Rapyd e-wallet to a bot with another Rapyd e-wallet, and start an automatic fiat <> crypto exchange transaction: /exchange (TBD) Gig Economies Telegram users with a Rapyd e-wallet created with the @rapydbot open-source API, can be mass-paid by managers (or any central authority) using the Rapyd dashboard. Additionally, the @rapydbot open-source API can be integrated with a variety of services to create jobs such as a Telegram Delivery Service, where users make a request to get something delivered by sending money to an /escrow, another user can then choose to take the job and get paid by @rapydbot upon successful delivery of the goods. Remittances Sending and receiving remittances globally has never been so easy. Users who wish to send money to their relatives/acquaintances in other countries can do so in a safe and reliable way through @rapydbot and Telegram. What's next for RapydBot (upcoming features) /withdraw - Responds with an Inline Keyboard that redirects the user to a secure form to input the user’s withdrawal options, such as Bank Transfer, PayPal, etc. /createescrow [name] - Creates a Rapyd escrow that will allow Telegram users to transfer money from their Rapyd e-wallet balance to it. The given name will be an escrow identifier that users can use to send money to it. /escrow [name] - Requests the amount to transfer from the user’s Rapyd e-wallet and notifies the user upon a successful transaction. /escrowbalance [name] - Responds with a Rapyd escrow balance if it exists. Community Contributions During the development of @rapydbot we found 3 issues that were followed in these threads: Transfer Funds Between Wallets metadata not being passed to its webhook Rapyd Sandbox Bank Payment username & password? How to generate an OTP code without the mobile SDK? <div