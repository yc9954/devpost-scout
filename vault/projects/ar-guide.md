---
slug: "ar-guide"
url: "https://devpost.com/software/ar-guide"
title: "AR Guide"
hackathon: "Amazon Raise-up Buildathon"
organization: "Amazon"
winner: true
words: 1140
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# AR Guide

> We develop an augmented reality guide(incl. payment option) so lines at the cashpoint and grouping at information sheets can be avoided. Visitors can individually explore the exhibition AR-guided

[Devpost](https://devpost.com/software/ar-guide) · hackathon [[Amazon Raise-up Buildathon]]

## Facets

**mechanism** [[sensor_fusion]]
  <sub>weak: voice_speech</sub>
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[structured_db]] [[web_dom]]

**stack** amazon-web-services, android, html, java, postgresql

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for ar guide

## Body

Your cultural companion Mobile ticket, mobile guide Technical concept Tutorial - swipe to navigate Tutorial - language change Tutorial - tap to start/stop sounds, descriptions(Text to speech) and videos always know where you are Pictures of the exhibit Picture of a beaming machine Videos can be played for every exhibit Video of a beaming machine Inspiration Because of the current Covid-19 situation and the need to not only avoid larger groups of people but also close contact with people, we thought about how we would see ourselves visiting a museum again. If you have been to a popular museum, you know how crowded they can get. The first issue is the long line at the ticket office. These lines are already super long without having 1.5 meters between people. Now imagine how the lines would look like with the new social distancing rules. Most museums will not have enough space for that and will therefore not be able to accomodate all the possible visitors. This could lead to visitors getting frustrated, leaving and a possible loss of business for the museum. The second big issue will be tours. Usually, there is one tour guide for groups of 20-25 people. What usually happens is that the guide stops at an exhibit, starts to provide information about it and the group huddles closer to be able to listen. This type of tour with large clusters of people bears a high risk for everyone and should not be continued during Covid-19. The third issue relates to points of interest like terminals, touchscreens or paper sheets with information about an exhibit. People gather around these sources of information, they get very close to be able to read it and usually stay there for a while because reading takes time. These areas are typically crowded because it is the only spot where you can get additional information about an exhibit that you like. The surface of a touchscreen is highly contagious and should be avoided during Covid-19. All of these risks need to be kept in mind if we want to open museums safely during this global pandemic. So how could I go back into a museum and feel safe? I do not want to stand in line for a ticket. I want to purchase it online. I do not want to get close to a tour guide to listen to him. I want to hear the information directly through my headphones/earphones. I do not want to wait at an information sheet until the people before me are done reading it nor do I want to feel rushed by people waiting to read an information on a terminal. I want the information directly on my phone so I can read it without stress or getting close to people. What it does When I plan on visiting a museum, I download the App on my phone. Through the App, I can buy a ticket days in advance or when I am right in front of the museum. Thus, I can avoid the first problem (the line at the ticket office) and go straight inside. As soon as I am in the building, the AR-Guide in the App shows me all the important information. It starts with a short tutorial of what I can do and how to use it properly. This tutorial is especially designed for our older folks who did not grow up with mobile phones or websites. The App is also designed for the smart glass Google Glass Enterprise 2 which can be rented for a day at the museum. With those glasses, you do not need your phone anymore and can get all the information in front of your eyes. When you enter the exhibition and look at the first exhibit, the information will be automatically on your display. This will solve the second problem (tours and grouping). You will see names, dates, author/painter/creator details as well as additional media like old pictures or videos. For instance, imagine an old, huge steam engine that is on display in the museum. You can see historical pictures of how it looked in the factory, a video of how the machine looked and sounded like while it was running as well as pictures of the assembly process at the museum. While all of this has been documented, there is usually not enough space in a classic museum to display and explain everything. In our App, there is no limit to the information that can be associated with an exhibit. All of it will be on your screen and you choose if and when you want to watch it. This will also solve the third problem (grouping at points of interest). Once you move to the next exhibit, your phone will update the information and show details of what you are currently looking at. No action will be needed and you can decide how much of the details you want to consume. With the help of bluetooth beacons and the gyroscope sensors of your phone, the App knows exactly what you are looking at and will help you out with the right information. No need for terminals with touchscreens that every visitor will touch or fact sheets next to exhibits. You have your personal guide right with you on your phone. How I built it We created an Android App, using Android Studio, Java and a PostgreSQL Database that we are hosting on AWS. To communicate we are using Azure DevOps to collect ideas, plan sprints, report bugs and host our git repository. At the museum, we mapped the area and connected exhibit and position data. Challenges I ran into Getting Amazon Pay to work on a native Android App was not as easy as we hoped. For websites, there is good documentation and it's easy, but having HTML and especially Javascript in our Java App was not as easy to handle. Accomplishments that I'm proud of During this hackathon, we presented this idea at a museum and they liked it a lot and want us to build and host it for them. When you think about problems and solutions and someone supports you and brings life to the idea, it is one of the best feelings as a developer. What I learned With the right people, ideas can become reality very fast. What's next for AR Guide We started with an Android version of our App because the smart glasses were our initial focus but we want to support iOS phones as well, so this will be the next development. We will also add the option for a museum trivia and at the end of the visit the App could offer coupons for the gift shop, show the specials, receive feedback or offer the option to make a donation if the visitor enjoyed the day. <div