---
slug: "automated-ramen-machine"
url: "https://devpost.com/software/automated-ramen-machine"
title: "NoodlMe | Automated Ramen Dispenser"
hackathon: "AngelHacks 2.0"
winner: true
words: 430
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/web_dom"
---

# NoodlMe | Automated Ramen Dispenser

> NoodlMe is the Keurig of ramen dispensing systems. Simply select a flavor and watch as it's dispensed and the perfect amount of hot water is injected through the lid! No more spills or pinching!

[Devpost](https://devpost.com/software/automated-ramen-machine) · hackathon [[AngelHacks 2.0]]

## Facets

  <sub>weak: deterministic_policy</sub>
**domain** [[education]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[web_dom]]

**stack** arduino, c++, cupramen, html, inventor

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for noodlme | automated ramen dispenser

## Body

The state machine Inspiration We're a group of college students who've had our fair share of bad experiences trying to grab a quick and cheap bite between classes. Cup ramen is a great choice but is prone to being messy and easy to spill while walking back to class or to a nearby table. We wondered if there was a way to add water to a cup of ramen while keeping the paper lid mostly in tact to allow for easier transportation. Que the NoodlMe! What it does The NoodlMe is an automated dispensing system designed for home and cafeterias alike. Unlike traditional ramen dispensers that require the user to peel back the lid and pour in hot water manually, our system uses a needle to puncture the paper lid and inject just the right amount of hot water. This leaves only a small hole at the top for steam venting and is much less prone to messy spills or worse, burns. How we built it The main assembly is laser cut cardboard with a wooden base. There are a total of 2 servos that are used to push the ramen cup out of the dispenser and to actuate the needle that punctures the lid. There is also a relay for operating the water pump and a button for starting the ramen making process. These are all controlled by an Arduino UNO. Challenges we ran into The cup pushing servo didn't mesh well with the cup ramen so it has to be assisted by hand on the prototype. Not having access to a working 3D printer made mounting the servos and assembly more difficult. The flex in the cardboard prevented the servo mechanism from working as planned so we had to hand assist some of the functions. We couldn't implement a water heating element due to a lack of appropriate heating element and safety concerns. Instead, water was pre-heated before being pumped into the cup ramen. Accomplishments that we're proud of The laser cut cardboard and overall build came out looking much nicer than anticipated. Provided hot water, the NoodlMe mostly works as an automated cup noodle dispenser. What we learned David: I had my first experience programming an Arduino Uno as well as creating a website. Bernard: Cardboard isn't an ideal building material. What's next for NoodlMe | Automated Ramen Dispenser Add a functional payment system through the website or a mobile app. A system that can add various toppings and seasonings to the cup ramen. A more rigid construction and redesigned actuating mechanism that is more reliable. <div