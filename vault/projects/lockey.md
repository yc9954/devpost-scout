---
slug: "lockey"
url: "https://devpost.com/software/lockey"
title: "Build an Encryptor/Decryptor Chatbot on Messenger using Wit"
hackathon: "2020 Facebook Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 325
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
---

# Build an Encryptor/Decryptor Chatbot on Messenger using Wit

> We are going to learn how we can build a smart chatbot that can understand and help us encrypt and decrypt messages using a secret key to help transfer encrypted messages with your friends safely.

[Devpost](https://devpost.com/software/lockey) · hackathon [[2020 Facebook Developer Circles Community Challenge]]

## Facets

**user** [[educator_student]]
**substrate** [[sensor_telemetry]]

**stack** facebook-messenger, fastapi, github, heroku, python, wit, wit.ai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next

## Body

Inspiration “If you want to learn something, read about it. If you want to understand something, write about it. If you want to master something, teach it.” This quote simply illustrates the main inspiration for this tutorial. Also what inspired me to write this tutorial is the thought of helping people learn more about the technologies used and know how to implement them. What it does This tutorial shows how to create a Facebook Messenger chatbot that uses Wit.ai to understand users. As it helps them encrypt and share their messages with other people without being afraid of revealing its content. Then they can decrypt the message again using the private key shared with them previously. How we built it We built the web application using FastAPI (a high-performance framework, easy to learn, fast to code, ready for production) for the backend. Then we added Natural Language Processing using Wit.ai to understand user intents. And we used Messenger to host our chatbot. And Fernet, a system for symmetric encryption/decryption. And finally, we integrated all of them into the web application and deployed it using ngrok Challenges we ran into One of the challenges that we ran into was that we needed a way to handle the conversation flow and have a context to determine the next steps in the flow. Accomplishments that we're proud of We're proud that we wrote our first tutorial as it wasn't an easy task because of all the research that was done to make sure that the written information was accurate and up to date. What we learned We learned how to write a proper tutorial that keeps the user interested until the end. What's next The next steps are to use more features in wit.ai, like using the speech API to understand the voice messages. Also, we want to add more features to the Messenger chatbot, like adding a share button for the encrypted message and the key <div