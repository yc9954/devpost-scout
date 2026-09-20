---
slug: "mercury-y2zisa"
url: "https://devpost.com/software/mercury-y2zisa"
title: "Mercury"
hackathon: "Amazon Alexa Skills Challenge"
organization: "Amazon"
winner: true
words: 588
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Mercury

> Send text and email to your friends or send messages to another Alexa device.

[Devpost](https://devpost.com/software/mercury-y2zisa) · hackathon [[Amazon Alexa Skills Challenge]]

## Facets

**substrate** [[geospatial]] [[web_dom]]

**stack** amazon-alexa, amazon-dynamodb, amazon-ec2, amazon-lambda, amazon-route-53, amazon-web-services, express.js, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for mercury

## Body

Mercury login createContact mercury Mercury Inspiration Monday morning after I returned from holiday, I was struggling to get back to office on time. While I was running up and down looking for my phone, and my shoes, I thought: I wish I could send a message, now, to notify my boss quickly and let him know I will be late for the planned meeting.... at that moment Mercury was born. What it does The main command: send a {messageType} to {contactName} handles two functions in one shot. First, maps the type of message (text/SMS, email, private message, ...) then, from the received contactName , finds the relative contact in the user's contact list. The second command: write How are you , handles the body text of the message, and emits a recap for confirmation. The AMAZON.YesIntent creates the message, depending on the request and starts the delivery process. The skill requires account linking to exchange private messages and to maintain the contact list. Through the Mercury website, the user can create a contact list adding friends' name, email, phone and a "Mercury email". The Mercury email is the one provided to link the account. With the command: Who am I Mercury will remind which email was used. How I built it Hosted in the Amazon cloud, the infrastructure uses the following AWS services: Ec2, ELB, Autoscaling group, CloudWatch, SNS, DynamoDB, Lambda, Route 53. The website is built using Node.js ,the Express framework and Bootstrap with mobile-first in mind. The skill is built with Node.js as well. The website has two main areas: An OAuth service used by Alexa for authorization code grant (access token and refresh token). An admin panel, for the contact management, secured by a one-time login access (with no password). The DynamoDB schema is optimized to limit the number of queries. The deployment pipeline uses Elastic Beanstalk for the website and the Serverless framework for the Mercury skill. Challenges I ran into I had few problem with the "send" command. Since the AMAZON.PERSON slot doesn't work very well; Mercury analyses the degree of similarity between strings, based on Dice's Coefficient . To increase the accuracy, the interaction model has a custom slot type with a long list of names (thanks to my ODS project ). Another challenge was around DynamoDB, I've introduced the Amazon TTL and optimized the schema to limit the number of queries. Accomplishments that I'm proud of I am happy that Mercury works pretty well and can understand a wide range of names, the messages are fast, and the overall idea can be extended to other messaging system. What I learned I have acquired more experience around the Alexa built-in slots and how Alexa manages the utterances. I have understood that the best way is to keep it simple, but with some tweaks in the logic, everything can potentially be achieved. Furthermore, I have learned how to manage better the test process providing a preset of scripts and JSON requests. In my spare time, I will try to automate this process and share my experience. What's next for Mercury The system is very flexible and can implement other types of messages. Potentially, the skill could send letters (requesting user's address), or be linked with social networks like Facebook and Twitter to send private messages or import contact list. There is also a plan to create some Easter Eggs (i.e. send a message to Michael Jackson). The user can potentially find in his/her voicemail Christmas messages or funny jokes sent by Mercury. <div