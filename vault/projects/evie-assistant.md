---
slug: "evie-assistant"
url: "https://devpost.com/software/evie-assistant"
title: "EVIE Assistant"
hackathon: "Alexa Skills Challenge: Tech for Good"
organization: "Amazon"
winner: true
words: 921
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/mental_health"
  - "domain/transportation"
  - "user/developer"
  - "user/frontline_worker"
  - "substrate/geospatial"
---

# EVIE Assistant

> A simple and engaging Alexa skill that helps you find Electric car charging stations

[Devpost](https://devpost.com/software/evie-assistant) · hackathon [[Alexa Skills Challenge- Tech for Good]]

## Facets

**domain** [[developer_tools]] [[mental_health]] [[transportation]]
**user** [[developer]] [[frontline_worker]]
**substrate** [[geospatial]]

**stack** google-maps, national-charge-register-api, open-charge-map-api, storyline

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for evie assistant

## Body

Charging stations Meet Evie Electric cars :) Inspiration I am a huge fan of green technologies, and I am keen to leave this world a better place for the next generation than it is currently. Last October I brought an Electric car, which I love not only because its better for the environment, but because it is a pleasure to drive. Most of the time I charge my car up at home, but if I ever have to go to somewhere new I get anxious about where I can charge. Many other EV users also have this anxiety. Some people who don't yet own an EV but would like one, are put off because they don't know much about the charging infrastructure. There are apps that let you search for chargers, but there was nothing on Alexa, and sometimes a simple conversation is much more convenient than using an app. I decided that if I created an Alexa skill to do this, then not only would it be useful for myself, but also for the huge community of EV drivers. It would also help those considering buying an EV to realise just how many charging points are out there! What it does In a nutshell EVIE Assistant takes a city/town name from the user and then uses that to get charging station data from a third party API. More technical explanation EVIE asks the users a few questions to confirm where they would like to search for charging points. EVIE then converts a city/town name into a longitude and latitude using the google maps api. Once the skill has the Lng/Lat it then passes that data into an Airtable api, a formula is applied to substring the Lng/Lat and then it is then passed into the Open Charge Map API (in the US & Canada) and the National Charger Register (In the UK) to return charging station information. How I built it I have built EVIE Assistant using the Storyline platform, and I have used third party API's to turn the user request into relevant data for the end user. I use Airtable to act as a staging platform to turn the API results into useful information for the user to hear, such as a count on how many chargers are returned. Challenges I ran into The first third party API that I used was great, but it experienced more downtime than what was acceptable, this impacted on the end users ability to use the skill. I changed the API that I was using to solve this. I had 30+ users from an EV community eager to beta test the skill, however in the end only 6 users where able to test it due to an issue with the Beta testing system. However I did still get some really useful feedback from that. Accomplishments that I'm proud of I am really proud of being able to provide a skill that is simple for the user to interact with, but which has some complicated stuff happening in the background, such as using multiple API calls to turn a city name into useful data for the end user. I am proud of creating a persona - EVIE for the skill, I feel that having that persona adds character and a better experience for the end user. I have networked within the EV community and have had great feedback from people who drive EV's and also from those that don't. A popular EV YouTuber here in the UK reviewed my skill which has helped get my skill exposure - https://youtu.be/J6kd03q8XBM I am also proud of how I have managed to develop EVIE assistant whilst also having a demanding day job, and a family that I like to spend lots of time with. I had to manage my time really effectively, which I somehow pulled off and I managed to take my work colleagues and family on the journey with me. What I learned Whilst developing EVIE assistant I have learned to be resilient when developing, so when issues occur to keep trying. I also learned the value of feedback from the target audience as that helped me to make the skill more useful. Finally I learned that if you are passionate about something, like I am about EV's then the satisfaction and sense of achievement you can get from developing a skill that helps others, feels amazing. I have also learned the importance of interacting with other developers and bouncing ideas off of them. Although I have developed this skill on my own, the help and inspiration that I have got from others has been invaluable. What's next for EVIE Assistant There is so much planned for EVIE Assistant. This is the first skill that I am treating as a product, which I want to keep adding to over time. Planned upgrades are mainly from user requests, such as being able to search by the charging speed or connector type, being able to define the search radius, and also looking at how i can add in the ability for users to control their cars (Turn heating and charging on/off) by utilising API's such as the Nissan EV connect service. I will also like to add cards that appear in the Alexa app which displays the information for the charging locations, I will do the same for Echo Show/Spot devices. I have now been given access to the Amazon Polly beta test, so I will be enhancing the EVIE persona with a new voice. <div