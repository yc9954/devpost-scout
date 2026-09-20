---
slug: "britafull"
url: "https://devpost.com/software/britafull"
title: "Britafull"
hackathon: "Hack the North 2022"
organization: "Techyon"
winner: true
words: 571
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/scientific_research"
  - "user/educator_student"
---

# Britafull

> Does your roommate forget to take out the trash? Do they never wash their dishes? Most importantly, DO THEY FORGET TO REFILL THE BRITA? Introducing Britafull, we fight your roommates for you.

[Devpost](https://devpost.com/software/britafull) · hackathon [[Hack the North 2022]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[education]] [[finance_payments]] [[housing_homeless]] [[scientific_research]]
**user** [[educator_student]]

**stack** arduino, c++, fsr, numpy, pygame, python, raspberry-pi, serial, twilio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for britafull

## Body

Britafull (logo) Britafull Anthem Britafull Britafull Product Mockup Inspiration Britafull is inspired by the ubiquitous student experience of living with people who may drive us crazy. Some roommates never wash their dishes, some don't take out the trash, but most insidious and aggravating of all... not refilling the Brita!! It's the little things that motivate you to finally get your own place. According to our highly scientific research, 80% of students face the SAME problem! What it does Britafull detects when the Brita's water levels get below a certain point using weight. The next person to grab the Brita and empties it to that point has seconds before the speaker kindly reminds them to be a good roommate and fill up that Brita. If that's not incentive enough, waiting even longer triggers a text message reminder. That's right, the whole group chat knows now. Call it petty, but here at Britafull, we get results. How we built it We used force sensing resistors to detect changes in force accounting for the presence or absence of the Brita. This information (analog) is passed to an Arduino which converts to a digital signal that is sent to our Raspberry Pi. We programmed primarily in Python and implemented functions to check when the Brita is empty based on the input data; if it is, we then trigger an alarm which prompts the user to refill. Lastly, if the Brita remains unfilled, we use Twilio to send a message to the entire roommate group chat that someone needs to get on their Brita game! Challenges we ran into As with many hardware hacks, our challenges were related to finding the right parts to use, and connecting the Raspberry Pi, Arduino, and our personal computers! Once we gathered the resistors that were compatible with the sensors to take the measurements we needed, we ran into compatibility problems that came from running Twilio's API with the rest of our backend interface. Also, we needed a Brita (generously provided by a fellow hacker)!! When working with Force-Sensing Resistors to obtain the weight of the Brita, we found that results often fluctuated as the water and sensor settled alike. To counter this, we found that gathering data across several seconds in 500ms intervals gave us a reliable set of data points, which we cleaned up with numpy for further accuracy. Accomplishments that we're proud of This was many of our first hackathons and first experiences doing a Hardware Hack! We are proud of ourselves for championing through the in-person experience and coming up with such a funny yet overwhelmingly practical product. What we learned For those of us without hardware experience, we learned how hardware-software system interfaces work! We also learned that the student housing experience is, indeed, universal. What's next for Britafull Britafull will never stop finding ways to manage your household and roommate problems for you. One way we could advance our platform is by implementing a machine learning algorithm that identifies the roommate in violation of the first roommate commandment: thou shalt refill the Brita as SOON AS IT'S EMPTY. In our pursuit of ensuring nonconfrontational hydration for all, we created a product mockup of Britafull should it ever hit the market. Featuring strong ABS plastic, inductive charging, force-sensing resistors, thin piezoelectric speakers, and ultrathin lithium batteries, we made sure that it would fit in with your daily routine and kitchen aesthetic without a hitch! <div