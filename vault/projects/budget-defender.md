---
slug: "budget-defender"
url: "https://devpost.com/software/budget-defender"
title: "Dime Defender"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 717
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/legal_justice"
  - "domain/retail_commerce"
  - "user/legal_professional"
---

# Dime Defender

> Chrome extension that helps you curb excessive online spending habits and cross-examine your cart ‍⚖️

[Devpost](https://devpost.com/software/budget-defender) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[cross_origin_web]] [[voice_speech]]
**domain** [[developer_tools]] [[legal_justice]] [[retail_commerce]]
**user** [[legal_professional]]

**stack** amazon-web-services, elevenlabs, javascript, plasmo, python, svelte, voiceflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dime defender

## Body

Dime Defender Key Art Dime Defender Checkout Objection Dime Defender Deliberation Dime Defender Opposition Judgee 1 Judge 2 Deliberation 2 Dime Defender Budget Adjustment Live Demo Link: https://www.youtube.com/live/I5dP9mbnx4M?si=ESRjp7SjMIVj9ACF&t=5959 Inspiration We all fall victim to impulse buying and online shopping sprees... especially in the first few weeks of university. A simple budgeting tool or promising ourselves to spend less just doesn't work anymore. Sometimes we need someone, or someone's, to physically stop us from clicking the BUY NOW button and talk us through our purchase based on our budget and previous spending. By drawing on the courtroom drama of legal battles, we infuse an element of fun and accountability into doing just this. What it does Dime Defender is a Chrome extension built to help you control your online spending to your needs. Whenever the extension detects that you are on a Shopify or Amazon checkout page, it will lock the BUY NOW button and take you to court! You'll be interrupted by two lawyers, the defence attorney explaining why you should steer away from the purchase 😒 and a prosecutor explains why there still are some benefits 😏. By giving you a detailed analysis of whether you should actually buy based on your budget and previous spendings in the month, Dime Defender allows you to make informed decisions by making you consider both sides before a purchase. The lawyers are powered by VoiceFlow using their dialog manager API as well as Chat-GPT. They have live information regarding the descriptions and prices of the items in your cart, as well as your monthly budget, which can be easily set in the extension. Instead of just saying no, we believe the detailed discussion will allow users to reflect and make genuine changes to their spending patterns while reducing impulse buys. How we built it We created the Dime Defender Chrome extension and frontend using Svelte, Plasma, and Node.js for an interactive and attractive user interface. The Chrome extension then makes calls using AWS API gateways, connecting the extension to AWS lambda serverless functions that process queries out, create outputs, and make secure and protected API calls to both VoiceFlow to source the conversational data and ElevenLabs to get our custom text-to-speech voice recordings. By using a low latency pipeline, with also AWS RDS/EC2 for storage, all our data is quickly captured back to our frontend and displayed to the user through a wonderful interface whenever they attempt to check out on any Shopify or Amazon page. Challenges we ran into Using chrome extensions poses the challenge of making calls to serverless functions effectively and making secure API calls using secret api_keys. We had to plan a system of lambda functions, API gateways, and code built into VoiceFlow to create a smooth and low latency system to allow the Chrome extension to make the correct API calls without compromising our api_keys. Additionally, making our VoiceFlow AIs arguing with each other with proper tone was very difficult. Through extensive prompt engineering and thinking, we finally reached a point with an effective and enjoyable user experience. We also faced lots of issues with debugging animation sprites and text-to-speech voiceovers, with audio overlapping and high latency API calls. However, we were able to fix all these problems and present a well-polished final product. Accomplishments that we're proud of Something that we are very proud of is our natural conversation flow within the extension as well as the different lawyers having unique personalities which are quite evident after using our extension. Having your cart cross-examined by 2 AI lawyers is something we believe to be extremely unique, and we hope that users will appreciate it. What we learned We had to create an architecture for our distributed system and learned about connection of various technologies to reap the benefits of each one while using them to cover weaknesses caused by other technologies. Also..... Don't eat the 6.8 million Scoville hot sauce if you want to code. What's next for Dime Defender The next thing we want to add to Dime Defender is the ability to work on even more e-commerce and retail sites and go beyond just Shopify and Amazon. We believe that Dime Defender can make a genuine impact helping people curb excessive online shopping tendencies and help people budget better overall. <div