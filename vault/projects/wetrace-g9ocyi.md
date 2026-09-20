---
slug: "wetrace-g9ocyi"
url: "https://devpost.com/software/wetrace-g9ocyi"
title: "WeTrace"
hackathon: "#CodeVsCovid19"
winner: true
words: 948
team_size: 8
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "domain/security_privacy"
  - "user/clinician"
  - "user/researcher"
  - "user/social_worker"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# WeTrace

> Find out if you were in contact with someone that was tested positive.

[Devpost](https://devpost.com/software/wetrace-g9ocyi) · hackathon [[-CodeVsCovid19]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[civic_government]] [[developer_tools]] [[health_clinical]] [[labor_employment]] [[legal_justice]] [[security_privacy]]
**user** [[clinician]] [[researcher]] [[social_worker]]
**substrate** [[geospatial]] [[structured_db]]

**stack** android, bluetooth, ionic, ios

## How they structured the write-up

- inspiration
- what it does
- how we built it
- prototype and links
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for wetrace

## Body

Inspiration We are a group of eight people, some from the IT field, a medical doctor, who is currently working in the field of Covid-19, an economist as well as a future social worker. We are passioned and willing to find a solution, which helps to stop spreading Covid-19. Our idea is inspired by the application built by the Singapore Government. In Singapore people are currently using the contact tracing app called TraceTogether . While we loved the idea, we disliked the lack of privacy protection. Therefore, we came up with our own idea. What it does General WeTrace uses Bluetooth LE to keep track of people you were close to. It automatically collects the ids of other users while it shares its own ID to them. When a user is tested positive, he or she can report the status change. A silent notification is broadcasted to all the users. That then can locally compare the newly reported case with their database of collected user IDs. If the reported ID is found in the database, the user that he or she might be at risk - the app will inform the user. An explanation can be found in our Video Presentation . Privacy When designing the solution, we put our focus on data privacy. Our solution has the following benefits: -A user gets a random ID assigned that he then will broadcast. The random ID will be changed every day to increase difficulty to be tracked -Contact data is only stored on the device locally, it will never be sent to a server -A backend is only needed to send a positive report to other people, this information will never be stored Infrastructure The following picture should give you an idea how our system is working: Adoption The functionality will also be provided as a SDK to be included in already popular apps to immediately increase adoption. How we built it WeTrace is being built with Ionic, Capacitor, native Android and iOS plugins for Bluetooth. Prototype and Links Web: https://wetrace.ch GitHub App: https://github.com/AndreasGassmann/contact-tracer GitHub Backend: https://github.com/lukeisontheroad/wetrace-backend EMail: hi@wetrace.ch Twitter: https://twitter.com/wetracecovid Challenges we ran into Legal concerns NPM problems Coffee supply bottlenecks Accomplishments that we're proud of The app is working pretty well. The design is simple and clean as we focused on user friendliness. What we learned Lot of stuff about Bluetooth LE What's next for WeTrace The current app covers the basic use case of tracking contacts. But as is always the case with a hackathon project, there are many things that can be improved. We have received a lot of amazing feedback and are planning to integrate as much as we can. Parameter Setting: Nobody can predict how exactly the virus spreads. New research-papers regarding the coronavirus are released daily and we learn something new every day. This is why it’s important that the different parameters in our app are adjustable. For example, how far and how long do you have to be next to someone to have the virus with a high degree of certainty? To get the best possible set of parameters, we have reached out to healthcare officials and scientists to improve them as much as possible. Neutral Status: One concern that has been raised was the fact that all people who install the app are marked as “healthy” by default. We are considering to add a new status called “unknown”. The current implementation is very simple, but error prone. As mentioned with the parameter settings above, we are working with officials to come up with the best balance here. Opt-in for data sharing with docs & researchers : People are very concerned about privacy and sharing their personal data, especially health related data. We completely agree, but it’s no secret that collecting data in a special situation like this can help tremendously. That’s why we are planning to add additional functionality that allows users to voluntarily share their data (eg. personal data, location data, health related data like symptoms, etc) with researchers, scientists or the government. But again, this will be completely optional. You don’t have to do this if you don’t want to. Self Declaration of COVID-19: We are aware of the vulnerability of the systems coming due to the self declaration. We are investigating options for a more secure way of declaring positive cases. One of them could be a collaboration with doctors or labs and using QR-Codes. Panic-Button: During these uncertain times, a lot of people get scared. The media is showing scary videos of what is happening in the world and people get afraid. Especially if an app would tell them that they have potentially been infected. This is why we are planning to add a dedicated, highly visible button that allows you to get help immediately. We are looking into different means of providing this help. One way might be to talk directly to someone on the phone. Another option would be to integrate a chatbot that can answer some of the important questions people might have. Chat-Bot: Providing additional information in every possible state helps the user to do the right thing. Currently we have a “further information”-button linked to official sources. A Chat-Bot would provide even more specific information and would help to answer all burning questions of the user. Gamification: Some people have reported that a gamification approach might help users to use the app and convince their friends to also use it. We are looking into this, but we have to be careful here because it should be a serious app and not a game. Increase adoption: Get the library implemented into already existing apps such as the official WHO Corona app. <div