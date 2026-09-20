---
slug: "tron-energy-bot"
url: "https://devpost.com/software/tron-energy-bot"
title: "TRON ENERGY BOT"
hackathon: "TRON Grand Hackathon 2022"
organization: "TRON DAO"
winner: true
words: 1191
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# TRON ENERGY BOT

> Telegram bot that automates the process for energy rental via multisig: checking availability, calculating rental price, place an order, confirm, un/freeze and vote. Long term deals supported.

[Devpost](https://devpost.com/software/tron-energy-bot) · hackathon [[TRON Grand Hackathon 2022]]

## Facets

**domain** [[civic_government]] [[developer_tools]] [[finance_payments]] [[housing_homeless]]
**user** [[developer]]
**substrate** [[financial_record]] [[structured_db]] [[web_dom]]

**stack** blockchain, cloud, database, heroku, javascript, postgresql, python, sql, telegram, tron

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tron energy bot

## Body

Buyer checks energy availability The bot automatically defrosts when the due date comes for every order it has processed The bot automatically freezes from seller's wallet and casts votes every hour (if applicable) Some examples of validation checks (II) /start command Regular order A buyer wants to buy more energy but he has an ongoing deal - price adjustment is made in order to avoid a free renewal for the previous TRX Some examples of validation checks (I) Inspiration I am a TRON whale and I found the energy rental so useful and lucrative business. However, TokenGoodies, the principal market to do it, is usually saturated and buy orders dissappear as soon as they are placed. This implies that you have to be always refreshing the website and be the very first to click on the order to "win" it. The problem comes when you don't have the time to always be checking, or even if you set up alarms, if you have a Ledger you haven't time enough to connect and confirm the order, so at the end of the day it's very difficult to actually catch an order . Specially nowadays because they have implemented an automated selling process for those wallets with more than 1 million TRX - that leaves "smaller" users with almost zero chances of catching an order manually . What it does It is a Telegram bot that allows any energy provider, no matter its wallets size, connect his customers base to his available energy in an automated way . The energy provider grants this bot un/freezing and voting permissions over his wallet and it does everything from the very beginning until the end. It has no risk because the bot doesn't have any other permission and it works via multisig: the private key will never be shared . The buyer talks to the bot and can check how much energy is available at the moment - the bot checks on the blockhain this info. Then, the buyer can ask the bot for the price of renting at any time range he desires. Previously, the energy provider set his selling fee and the maximum period he's willing to sell (for example: from 3 to 31 days). So, the buyer can check automatically how much will be renting 300K energy for 14 days, for example. It's really good because TokenGoodies only allows the minimum period (3 days) and this bot supports long term deals . If he agrees, then he can place a buy order, typing his wallet address (where he will receive the energy), the energy amount and the number of days. He will have 10 minutes to make the transfer and send the confirmation hash to te bot, who will make several checks to confirm the transaction is OK (the wallet address is the same than he provided, the payment amount matches, the hash has not been used before for confirmation - so no double buy without actually paying is allowed, etc.). It also checks if the buyer has an ongoing deal with the seller in which the TRX are still frozen, so the previous TRX won't be "renewed for free" with the new order - it adjusts the price accordingly. When confirmation is given, the bot freezes the corresponding amount from the seller's wallet to the buyer's, and then transfer the % payment to the energy provider, and other % to the developer (~10%) for maintenance fees. Every hour, the bot also casts votes to the SR that the seller has decided if there is any vote to cast (this time frame can be modified by the energy provider), and every 5 minutes it checks if there is any "defrostable" amount based on confirmed deals with their own durations. If so, it unfreezes them. It's also remarkable that the energy provider can still freeze for himself or other separate deals without interfering the bot activity, because it will only unfreeze the orders that have been placed through it. To sum up, the bot automates the whole process and allows more flexibility regarding prices and durations . How we built it Programming language is mainly Python and JavaScript, and SQL for the databases. The bot connects to TRON blockchain through the API and checks energy price, seller's wallet balance and broadcasts every order directly to the blockchain (un/freezing, voting and making transfers to the seller and developer). Challenges we ran into First challenge was keeping the bot alive 24/7 what I solved deploying it to a (paid) cloud server. Then, I wanted the bot to support long term deals , because in TokenGoodies it's always for the minimum: 3 days, and I, as an energy seller, have made many deals for one month duration or more, so I thought it would be useful as well. So, I faced the problem that the cloud server "restarts" the bot every 24 hours, so every information it has "pending" was deleted, losing then the information about unfreezing time if it was over 3 days. Then, I solved it by attaching a database to it and making the bot alter the SQL tables with every transaction so the information won't be lost. The "ultimate challenge" was adapting it to work only with multisig and not sharing the private key . It was really challenging because the whole project was built with Python code and the current libraries don't support this kind of process, so I had to learn some JavaScript and how to include/combine it with my script. I had to rewrite many processes using JavaScript that I had previously proved they worked with Python and spend a lot of time here, but hey! it's already implemented and it works! It can be tested talking to @TRON_energy_bot in Telegram. And now some TRON community members are starting to participate, having their own energy bot for themselves! Accomplishments that we're proud of I'm very proud of having made it work through many tests, spending time researching as a non-tech woman and finally achieving it. Combining different softwares and programming languages, not to mention blockchain itself, and being able to solve every problem that came up. What we learned Reality can be (and probably is) more difficult than expected, but you can always find a solution. I've learned very much about managing versions of the code, testing before deploying, storing critical data into cloud servers so it won't be lost. I've also learned that automation makes life easier to users and making things as simple as possible for them. What's next for TRON ENERGY BOT Further steps are developing some commands for the energy provider so he can change settings by himself (current version requires them to tell me their sell rate and the SR they want to vote for at the initial configuration of the bot), and also a command so they can see their open orders and buyer wallets , so they can organize their assets checking unfreezing date for every order. I also want to expand this to bandwidth rental , not just for energy. * Many plans ahead and I'm always open to suggestions. * <div