---
slug: "hubsy-the-hubspot-bot"
url: "https://devpost.com/software/hubsy-the-hubspot-bot"
title: "Hubsy (the Hubspot Bot)"
hackathon: "AWS Chatbot Challenge"
organization: "Amazon"
winner: true
words: 600
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Hubsy (the Hubspot Bot)

> Manage your HubSpot account from Slack, Facebook, and Amazon Alexa

[Devpost](https://devpost.com/software/hubsy-the-hubspot-bot) · hackathon [[AWS Chatbot Challenge]]

## Facets


**stack** amazon-alexa, amazon-cloudwatch, amazon-iam, amazon-lambda, amazon-web-services, docker, giphy, hubspot, makefile, ms-paint, node.js, terraform

## How they structured the write-up

- inspiration for hubsy
- what is hubsy ?
- the nuts and bolts
- anything clog up hubsy's gears?
- notable robotic achievements
- what did hubsy teach us?
- check out hubsy's offical site

## Body

Hubsy 1.0 Inspiration for Hubsy After hearing about the hackathon and being avid AWS fans we immediately knew we had to compete. The idea for Hubsy itself stems from the desire to incorporate a conversational AI into a real life everyday workflow. Hundreds of thousands of users pop on to HubSpot each day to click thru tasks and insights. These same people often have several different means of conversation open on their browsers as well albeit Slack, Facebook, etc (whether or not they should be). We thought it would be a cool idea to personify a SaaS product (HubSpot), throw them into these channels of communication, and talk to them just like a member of the team. Amazon Lex's natural language understanding gave us a chance to do just that; integrate, utilize, and access software as if it was our own personal assistant. What is Hubsy ? Hubsy seeks to redefine the away users traditionally manage their HubSpot account. He utilizes Lex's conversational interface to execute complex commands within the HubSpot API allowing users to unleash powerful insights, store and retrieve data, and even manage tasks directly from Facebook, Slack, or even Alexa. Maybe you are curious as to what your team is up to? - Any new deals? - How many calls were made today? - How many tasks are assigned to Andrew? Need to store some info on the fly? Let Hubsy talk you through it. - Create a contact - Take a note - Assign a task - Log a call Let Hubsy explore your pipeline! - How much money is in the negotiate stage? - What are the number of deals? Just need some quick info? - Get contact info for Brian Halligan The Nuts and Bolts Deployments Terraform was used to manage our infrastructure. Terraform automatically setup and updated Lambda, CloudWatch logs, as well as IAM profiles. Within our makefile, code was zipped and immediately pushed to the cloud. Outside of our initial setup Hubsy was built without having to even reopen the Lambda UI. Core All of our AWS Lambda functions are written using node.js. CloudWatch serves as Hubsy's memory logging of commands and API responses, crucial for development. Coding standards were enforced using ESLint to keep consistency across differing team member's. Anything Clog Up Hubsy's Gears? To bring our Hubsy concept full circle we would need to not only GET data from the HubSpot API, but also POST. While working within the API itself had it's own challenges, our biggest one actually came from Lex. After lots of research, it seemed Lex had recently done away with their concept of a slot.LITERAL rendering us in a tough spot when it came to capturing truly unique user generated content. Often times we were able to eventually teach Lex a slot type with a handful of examples, but others we were forced to come up with a work around. Utilizing sessionAttributes, and the exact inputTranscript provided, we could prepare to accept any dialogue for users who were attempting to create custom notes, tasks, etc. Notable Robotic Achievements 1) Fully dynamic commands capable of creating, retrieving, and updating data within HubSpot. 2) Our software development lifecycle. 3) Creating a dynamic bot which is deployed via both Lex and Alexa. What Did Hubsy Teach Us? Something about building bots really brings the human out in you. While AI is awesome and undeniably the future... Sometimes its really great to chat with a human. Additionally, the ins and outs of Lex and its differences from Alexa, HubSpot's API, Lambda API access. Check out Hubsy's Offical Site hubsybot.com <div