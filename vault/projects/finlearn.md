---
slug: "finlearn"
url: "https://devpost.com/software/finlearn"
title: "FinLearn"
hackathon: "HooHacks 2021"
organization: "HooHacks"
winner: true
words: 1074
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# FinLearn

> FinLearn progresses in a way that encourages players to complete their daily tasks and discourages them from spending their money on liabilities.

[Devpost](https://devpost.com/software/finlearn) · hackathon [[HooHacks 2021]]

## Facets

**domain** [[education]] [[finance_payments]]
**user** [[educator_student]] [[researcher]]
**substrate** [[financial_record]] [[structured_db]] [[web_dom]]

**stack** blockchain, canva, css3, flask, flutter, html5, photoshop

## How they structured the write-up

- inspiration
- what it does
- key features
- how we built it
- challenges we ran into
- what we learned
- accomplishments that we're proud of
- what's next for finlearn
- domain.com?
- google cloud?
- beginner hack
- last but not least, fincoin

## Body

FinLearn Logo Invite Page Onboarding Page Goals Page Learning Module Learning Module Quiz Page Budget Page Stocks Page Inspiration Given how important financial skills are to navigating life, it’s surprising that our schools don’t teach children about money. “Look at the mortgage crisis and how many families lost their homes — 3.9 million foreclosures. Look at the amount of money — $1.1 trillion—we owe in student loan debt. The amount — $845 billion — we owe in credit card debt. It’s pretty clear that even adults don’t know much about money. To help the next generation avoid the mistakes of their elders, and to live financially fit lives, they need to be taught the essentials about money,” says Beth Kobliner, author of the New York Times bestseller Get a Financial Life. So in this 21st century, there is a pressing need for the youth to know about money matters. Children as young as three years old can grasp financial concepts like saving and spending. And a report by researchers at the University of Cambridge commissioned by the United Kingdom’s Money Advice Service revealed that kids’ money habits are formed by age 7. What it does FinLearn gamifies teaching financing to youth. It uses its own in App blockchain-based currency called FinCoin which gets rewarded to players when they complete their daily tasks which include things like making their bed, studying, going for physical activity, etc. These tasks are configurable by the parents. The parents also decide the conversion between FinCoins and Fiat. The learning is divided into modules and levels and each module completion leads the players to earn FinCoins. The players are also presented with financial choices where choosing the correct option leads the players to earn more FinCoins and vice versa. The children can see their balance go up and down as they progress their way through the app. Along with this, there are modules that teach the youth financial terms and aspects starting from simple things like what is money and how to make money decisions to complex things like inflation and deflation. Things like banking, financing, stocks, and funds are also taught. We have also added interesting things like decreasing the value of FinCoins when teaching about inflation and then increasing the value of FinCoins during the deflation level. At the end of each module, therefore, the players will have more return indirectly. FinLearn progresses in a way that encourages players to complete their daily tasks to earn more FinCoins and discourages them from spending their money on liabilities. It instills in them important financial skills which will benefit them in adult life. In a nutshell, FinLearn transforms the whole concept of pocket money as we know it. Key Features Virtual Currency • FinCoins show patterns similar to Fiat like inflation etc. • Employ BlockChain technology • Configurable conversion factors by parents • Can be used to gain in-app advantages like virtual investing and virtual financial decisions. Encouragement of Chores Completion • The best way to earn FinCoins in the App is through completing daily chores. Gamified learning Experience • The whole user experience of the app is designed in such a way that it is easy to operate by youth as well as parents • Each financial term is explained using comprehensive visualizations and interactions • The whole process is designed like a game in which the players will crave to play more! How we built it We used tools like adobe photoshop and canvas to first prototype the app and think about the user interface as the app had a young userbase. Then we thought about the learning fundamentals we had to include in the app. Next, we coded the whole frontend of the app in Flutter and used Firebase as the database and authentication medium. We used cloud functions by Google Cloud to communicate between the backend and the frontend through the medium of requests. Challenges we ran into First of all, learning and building a cryptocurrency from scratch was a big curve. We made a prototype three times before getting the functionality we desired. We also faced the challenge of our whole video project getting corrupted mid-way. Along with this, one of our teammates experienced a power cut which made coordination difficult. What we learned We learned a lot of great things. The first one was topics that we taught in the app! Along with this, we learned the basics of blockchain as well as cloud functions which we used to connect our app to our database which was hosted at firebase. We also learned how to implement link login which we used to configure the logic between child and parent authentication. Accomplishments that we're proud of We are proud of the fact that despite frequent coordination issues and learning absolute new technologies, we were able to complete our project. Frankly speaking, we believe that not knowing finance is the biggest problem most of us face. So we are content that we were able to tackle an issue that even we face ourselves. What's next for FinLearn We acknowledge that knowledge is endless and there are countless basic things that we can and have to teach related to finance. So one of our main focuses will be configuring the teaching strategy as well as adding new modules. Along with this, we have partially implemented a virtual trading game/platform in our app. We plan to polish that as it was really fun even for us while we were testing our app. Domain.com? Our domain, which we are grateful for your team for providing us, is https://youthlearnfinance.online/ . Along with our main app, we have also built a project as well team demonstration website. Google Cloud? We have proudly hosted our crypto on the google app engine. We have also used firebase for the whole integration of our app, from the authentication to the database itself. We have also made use of cloud functions to integrate our backend and frontend. Beginner Hack This project was Jessica's and Kishan's first hackathon. They learned a lot during these 24 hrs and look forward to the wondrous world of open-source software. Last but not least, fincoin Our crypto chain can be accessed at https://moneyminder-308908.uc.r.appspot.com/chain To make a new transaction, a json request has to be send to the url https://moneyminder-308908.uc.r.appspot.com/add_transaction With the body {'sender': "sender_name", "recipient": "recepient_name", 'amount': 'xx FinCoin'} . A new block will be added every 3 transactions. <div