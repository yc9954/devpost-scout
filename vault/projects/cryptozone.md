---
slug: "cryptozone"
url: "https://devpost.com/software/cryptozone"
title: "cryptozone"
hackathon: "Junction 2016"
winner: true
words: 340
team_size: 5
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/financial_record"
---

# cryptozone

> Improve Amazon shopping experience with Ethereum

[Devpost](https://devpost.com/software/cryptozone) · hackathon [[Junction 2016]]

## Facets

**domain** [[finance_payments]] [[retail_commerce]]
**user** [[small_business]]
**substrate** [[financial_record]]

**stack** azure, docker, ether, javascript, node.js, python, react, redis

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cryptozone

## Body

Inspiration The idea behind is to improve the cryptocurrencies ecosystem, by giving the possibility to users to spend crypto coins on many "classic e-commerce" sites. Imagine that you are a freelancer and earn your salary in Ether (or any other crypto currency) - with our service you'll be able to spend this Ether on many e-commerce sites. You no longer need conventional money to buy goods. What it does Our service translates prices on e-commerce sites from conventional currencies to cryptocurrencies, on the fly, transparently for the customers. A user can add items to the basket, just like he would normally do, and then proceed to checkout. The user will then make the payment in Ether through our plugin app. How we built it We built a dockerized micro services infrastructure, hosted on the Azure cloud. Our solution includes such components, as: Ether blockchain node, Redis, Nodejs, ngrok, and many other components. Once the user reaches the payment stage on the ecommerce site, he lands on our plugin app where a QR code is generated. Scanning the code with the Ether mobile app makes the payment. The transaction with the e-commerce site is handled by our service. Challenges we ran into It was really interesting and tough to build and run an Ether blockchain node, mainly because of the size of the block itself. We also had to orchestrate many different microservices and components to work together, which was particularly challenging to properly confiure. Accomplishments that we're proud of We actually got the prototype working. We made an amazing team and collaboration was key to productivity and success. It was an enriching experience, where we all learned new things and shared knowledge with each other What we learned We learned how to use docker, how to work with Ether, send and receive payments. As well as how to work with ES6 on Node.js and bundle ReactJS code with Webpack. What's next for cryptozone Improve the user experience and add more features, including dynamically processing payments on more ecommerce websites. <div