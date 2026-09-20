---
slug: "cryptobot-ecytaj"
url: "https://devpost.com/software/cryptobot-ecytaj"
title: "CryptoBot"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 399
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "user/general_public"
  - "substrate/financial_record"
---

# CryptoBot

> Bring the human to humanoid - giving robots rights for a robot-powered future with our Robotic Butler

[Devpost](https://devpost.com/software/cryptobot-ecytaj) · hackathon [[Cal Hacks 12.0]]

## Facets

**domain** [[civic_government]] [[developer_tools]]
**user** [[general_public]]
**substrate** [[financial_record]]

**stack** c++, conversion, next.js, openai, postman, python, sui, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cryptobot

## Body

Inspiration Cryptobot is something we've built out of a dystopian fantasy. We envision a world with a robot in every house eventually, so we set out to build the infrastructure to make that truly happen by giving humanoid robots a REAL human touch. Our use case is a robotic butler that can eventually be put in every house, with freedom of speech, vision, transactions, and voting. What it does Cryptobot is a humanoid robot that is FULLY voice-controlled. You can ask it to move around, say hi, start cheering, etc, and it'll execute the motion and respond in a sassy manner. But more importantly, we've given it access beyond that... cryptobot can execute Crypto transactions, something that 10xes the power of robots since they can autonomously make decisions themselves and execute transactions. It also has ability to scrape and search the web and access any public API. How we built it We used Sui, Postman, and Booster K1 humanoid to power this. We take audio in from robot, stream to openai, use Postman to tool call certain functions, and Sui for sending crypto transactions and voting protocols. Challenges we ran into SSH into robot was super challenging and SDK was sparse. We wanted to implement vision but weren't able due to super sparse documentation and time crunch. That's up next tho! Accomplishments that we're proud of Getting voice to transaction to work! Also voice to movement is pretty cool. We had a lot of struggle accessing the robot mic and speaker, and used pretty niche systems like pulseaudio and alsa in order to access the proper output devices on the robot. That was definitely a challenge to debug and I think we learned quite a meta-skill there, using tech that just came out What we learned How to manage dependencies and use hi level sdk for booster robotics. We also learned about different management of depencies, using SSH for robots, Postman and Sui integration as well. What's next for CryptoBot The moon! We want a crypto bot in every house. It can be fully autonomous with ability to vote, transact, talk to people, and do household chores. And then 50 years in the future, what's even the distinction between human and robot? Shouldn't they have the right to vote? We're building that feature and functionality in from day one for a dystopian future where robots are equal citizens. <div