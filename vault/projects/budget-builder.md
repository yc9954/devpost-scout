---
slug: "budget-builder"
url: "https://devpost.com/software/budget-builder"
title: "Budgetizer"
hackathon: "PennApps XII"
winner: true
words: 787
team_size: 3
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Budgetizer

> A personal budgeting tool using Plaid's transaction API

[Devpost](https://devpost.com/software/budget-builder) · hackathon [[PennApps XII]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[finance_payments]]
**substrate** [[financial_record]] [[geospatial]] [[structured_db]] [[web_dom]]

**stack** chartist, flask, mongodb, plaid, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for budgetizer

## Body

Inspiration Looking at a bank statement doesn't provide an easy way to see how your money is being spent. Yes, it shows what you purchased and how much it cost, but each item is listed chronologically. It would be usefull if you could group these items by some category when you are trying to determine how to save money. What it does It allows anyone to log in with their credit cards and bank accounts (those supported by Plaid) and get a detailed look into where their money comes from and how they've been spending it for the past few months. How we built it Budgetizer is a Python web application built on the Flask microframework which interacts with a MongoDB database and the Plaid API to make budgeting amazing. The Plaid API allows us to pull data from different bank accounts, present it in an easier-to-read format, and aggregate it with categories. Challenges we ran into In order to generate an accurate budget for the future, it's important to differentiate between one-off payments (movie tickets, a night on the town, etc.) and recurring payments (mortgage, insurance, etc.). While these are fairly easy for a human to detect based on patterns and the transaction descriptions, pattern recognition can be pretty difficult on a computer. We also decided mid-way through that we needed to save our information to a local database, so we decided to spin up a MongoDB server. While this can be done pretty quickly in a Linux environment, getting MongoDB set up on Windows is a tricky balance of pleasing the Mongo gods and reading old or outdated documentation. Accomplishments that we're proud of The UI is simple, easy to use and looks great. We used a template called Flatly , provided by Bootswatch, which is a bootstrap-based theme. It paired well with the strengths of the group and the data is handled beautifully. We were able to get MongoDB, a great NoSQL database, to function as expected on our development systems. We have used it as a team before on Ubuntu and it was easy to setup there. That said, we had not had the chance to develop with MongoDB on Windows. It was a bit of a bear to get it configured correctly, but we were happy to be able to use this technology to store our transaction data! Sorting out transactions by account to help narrow down results. Plaid's API is extremely well documented, and we realized early on that each transaction is tied to their respective accounts. Since users might want to tie a number of different cards and accounts, it felt like a no-brainer giving them the option to exclude some accounts. The implementation of this is clean and gives a lot more control to the user. The category graph on the transaction history. We've used many charting libraries in the past, and we've noticed not all of them are very responsive or accessible. This was our first time using Chartist, and it was a great experience! We were able to hook into the graphs to give an even deeper user experience by letting users have tooltips on mouseover and sorting on clicks. What we learned Plaid's API is amazing. They've really gone all out with putting plenty of great documentation and support out there. We looked into it a bit before the hacking started and it's what really sold us on doing something with it. MongoDB has a powerful aggregation framework that allows you to query the collections for the information you need, and then group, combine, and alter it to meet your needs. In our case, this was used for generating the list of transactions to look at as well as generating the expected output for the charts with all of the necessary information. What's next for Budgetizer Budgetizer is designed to be a web service. Although we opted to host it locally for our demos, the next big step would be to get it set up and hosted online. Some other future ideas for useful feature include some of the following: Integration with a stock API: This would allow a user to consider liquidating shares to help them pay for large budget items. Bonds: The user could manually enter bonds and their maturity dates to allow the system to better estimate future account balances. Location and Fraud Services: By using location data from Plaid, we could monitor transactions for the user. This would be further compounded by MongoDB's awesome geolocation tools. Deeper Analytics: This iteration of Budgetizer is just scratching the surface of what is possible with the data we can use from Plaid and the integrations with other services we can tie the website into. <div