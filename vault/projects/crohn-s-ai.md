---
slug: "crohn-s-ai"
url: "https://devpost.com/software/crohn-s-ai"
title: "Crohn's AI"
hackathon: "Disrupt SF Hackathon 2018"
organization: "TechCrunch"
winner: true
words: 836
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/retail_commerce"
  - "domain/scientific_research"
  - "user/patient_family"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Crohn's AI

> FREE personalized health coaching for Crohn's disease — via SMS.

[Devpost](https://devpost.com/software/crohn-s-ai) · hackathon [[Disrupt SF Hackathon 2018]]

## Facets

**domain** [[health_clinical]] [[mental_health]] [[retail_commerce]] [[scientific_research]]
**user** [[patient_family]]
**substrate** [[sensor_telemetry]] [[video_visual]]

**stack** alexa, amazon-web-services, heroku, python, ruby, ruby-on-rails, twilio

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for crohn's ai

## Body

Crohn's AI | FREE Crohn's Health Coach Inspiration tl;dr - I believe that EVERY Chronic Illness should have its own publicly accessible personalized AI available via SMS, email ( and Alexa, Google Assistant, HomePod ) 1) Example of Personalized Medicine Crohn's is the PERFECT disease to highlight personalized medicine, with Crohn's there is very little "blanket advice". One of the first things that people ask when they are diagnosed is: What can I eat / not eat? There is almost no way to answer this question except through personal trial and error, even then its very hard to do because of our bad memories, confirmation bias etc... 2) I have Crohn's so I know this problem very well. When I was younger it was really hard to talk about my poop and being gassy or pooping blood because these things are embarrassing. As the CEO of Bayer Rx has stated many times, it is much much easier to talk to an AI than a real person sometimes. This is not just best for the patient, i have talked to Dr's who ( surprise, surprise ) don't want to look at pics of bloody poop all day - AI does task like this faster and better than we can. 4) FB Groups - I am a member of fall victim to morons, scammers, spammers and fake news all the time. In the realm of healthcare we MUST not let FB remain in this role considering their stance on FakeNews, we must have something that not only understands the patients condition and the disease but also is available 24/7 and provides the same value add that people get from posting questions for strangers on FB to answer. 5) Fake Reviews on Amazon are bad. But for people living with Chronic Illness ie: Chron's they can be deadly. I need honest reviews on supplements etc... because my health depends on it so I redeveloped reviews the way I think they should work - based on real user feedback from using the product based on a pre-defined set of expectations. What it does 1) Track Symptoms - Track symptoms and follows up to see if they are getting better or worse, then does an investigation using the data provided into what may be the catalyst. 2) ID Triggers - Because of confirmation bias and correlation vs causation it can be very hard if not impossible to ID your triggers on your own. Crohn's AI does this very well because its AI and we can optimize and re-optimize the trend detection algorithms based on real user feedback. 3) Optimize Supplements - There are a lot of people ( like me ) who after years of Rx have decided that supplements and diet are the best way to manage their Crohn's. Crohn's AI helps w/ this by running continuous adaptive clinical trials that incorporate real world feedback from other users in your cohort so person X with issue Y can benefit from persons A, B, C in their same cohort who have successfully resolved issue Y 4) Supplement / Rx and Alt therapy 411 - Getting honest feedback on supplants, prescriptions and alternative therapies can be really had because everyone has their own angle and its usually not to just help the patient. We track claims and expectations of each of the aforementioned and report / recommend based on real-world use feedback. 5) Meal Planning - Meal planning with Crohn's can be very difficult because its hard to know what you can/cant each, shop, cook, input data into feedback loop and optimize then repeat. Crohn's AI makes this easier by using the DietManager meal planner to incorporate metrics and feedback into the meal planning and grocery shopping process. 6) Flare-Up prediction and prevention - One of the hardest parts about Crohn's is dealing with Flare-Ups. Things are made worse when you don't deal w/ them immediately. Crohn's AI helps detect when you are about to have a Flare-Up and makes suggestions for things you can to do avoid it. How I built it 1) DM API - Meal Planning API 2) FitBit and Wiithings API - KPI's for patients that trigger nudges 3) Heroku - Hosting 4) Twilio - SMS 5) Einstein Vision - Image Rec AI 6) Rails / Sinatra / Ruby was main lang used for the Bot 7) Python and NLTK stuff used for ML pipeline Challenges I ran into 1) Testing, bots can be really really hard to test Accomplishments that I'm proud of 1) It works 2) Issue management is quick and easy 3) It talks to users via: Text, Emoji and Animated GIF What I learned 1) Don't build data driven bots using 3rd party platforms 2) Ruby's NLP tool kit What's next for Crohn's AI 1) Make follow-ups work better 2) Improve the NLP so conversations can go deeper 3) Integrate more 3rd party devices and API's e.g.: FitBit 4) Make food log smarter 5) Make poop log smarter ie: Detect blood progressions/regressions etc... <div