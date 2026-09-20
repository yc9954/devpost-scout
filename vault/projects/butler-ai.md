---
slug: "butler-ai"
url: "https://devpost.com/software/butler-ai"
title: "Butler AI"
hackathon: "Amazon Alexa Skills Challenge"
organization: "Amazon"
winner: true
words: 727
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "user/developer"
  - "user/researcher"
  - "substrate/financial_record"
---

# Butler AI

> Butler AI - order food from restaurants with Alexa or Google Home, with customizations and access to full menu

[Devpost](https://devpost.com/software/butler-ai) · hackathon [[Amazon Alexa Skills Challenge]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]] [[retail_commerce]]
**user** [[developer]] [[researcher]]
**substrate** [[financial_record]]

**stack** alexa-app, amazon-alexa, express.js, google-actions-sdk, google-home, machine-learning, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what's next for butler ai

## Body

Inspiration Voice has always been an alluring method for engineers, scientists, and novelists to communicate with computers and robots. Until now it was a pipe-dream, but Amazon Alexa and Google Home showed that using modern deep neural network based machine learning can enable our computers and robots to listen and obey to their masters. While playing with these devices, I realized that they can make so many mundane tasks easier. One of them is ordering food and Alexa showed that how convenient it is to order pizza just using voice. Few of my favorite comfort foods are from local restaurants and I thought wouldn’t it be cool if I can use Alexa to order food from my local restaurants too! What it does Butler AI is a skill to order food using Amazon Alexa or Google Home from local restaurants. Butler AI lets users to order anything from the menu and also let them to customize their items. Users don't need to configure their order online or are restricted to pick from last few orders. It even allows users to build up their items, sends link to restaurant’s menu, remember their order for 30 mins so user can come back and continue from where they left off! Here’s an example of how one will order food from Austin’s Pizza restaurant using Alexa: PizzaLover: “Alexa, open Butler AI” Alexa: “Hi, which restaurant you want to order from?” PizzaLover: “From Austin’s Pizza” Alexa: “Austin’s Pizza, ok. Please say your zip code or location name for pickup.” PizzaLover: “From 78613” Alexa: “From Cedar Park, ok. What would you like to order, please say one item at a time.” PizzaLover: “I will have a large cheese pizza with pepperoni and mushrooms.” Alexa: “One 14” Large pizza with pepperoni and mushrooms is added. Anything else or you would like to checkout?” PizzaLover: “Also add jalapenos to it.” Alexa: “Added jalapenos to 14” Large pizza. Anything else or you would like to checkout?” PizzaLover: “Checkout please.” Alexa: “You order has one 14” Large pizza, please say yes to continue checkout.” PizzaLover: “Yes” Alexa: “Your order total is $16.30 and it will be ready in 30 mins. Please say yes to confirm your order.” PizzaLover: “Yes” Alexa: “Your order has been placed under PizzaLover. Thanks for ordering with Butler AI.” Butler AI is also designed to support multiple restaurants in the backend so users gets to use familiar experience across all the restaurants. Having a unified platform like Butler AI can help local restaurants to bring the modern voice assistants at minimal cost. Instead of focusing on different technologies, restaurant owners can spend their resources where it matters - satisfying customers with great food. How I built it Butler AI is built using Node.js with Alexa-App , Actions-on-Google SDK , Mongo-DB , Express.js , Nginx , boostrap , simple-oauth2 , passport.js , cheerio.js , request.js and many more node modules. Challenges I ran into There were many challenges I faced given that this was my first project in Node.js, I had to learn quite a bit about starting with Node, best practices, deploying etc. But that aside, as a personal choice, I decided to deploy Butler AI on standalone VM instead of lambda service. This decision added quite a bit of extra work to get it working and making sure that my setup is certifiable, but it has been a great learning experience. The second biggest challenge was to integrate with local restaurants. Scrapping their websites to find menu items is one thing, but its completely another thing to use these websites to place orders. Maintaining user’s order state and enabling customizations to each item was also tricky. Accomplishments that I'm proud of A skill that many people will find useful in their day to day life! This might be an overstatement but I strongly believe that Alexa and Google Home can transform people’s lives by enabling voice as a primary interface to connect with computers, robots or any services (such as restaurants). Thus, I am really proud and excited about possibilities of Butler AI on these platforms. What's next for Butler AI I am planning to add more restaurants to Butler AI so more and more people can use it. Alongside I am also looking for ways to promote voice assistants to provide better user experiences in different markets than just restaurants. <div