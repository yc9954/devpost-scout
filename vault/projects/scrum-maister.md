---
slug: "scrum-maister"
url: "https://devpost.com/software/scrum-maister"
title: "Scrum Maister"
hackathon: "Codegeist 2020"
organization: "Atlassian"
winner: true
words: 1131
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/web_dom"
---

# Scrum Maister

> Scrum Master + AI = intelligent helper that revolutionizes Agile development through AI-powered issue grooming, sprint analytics and retrospectives

[Devpost](https://devpost.com/software/scrum-maister) · hackathon [[Codegeist 2020]]

## Facets

**domain** [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[web_dom]]

**stack** forge, javascript, machine-learning, natural-language-processing, python

## How they structured the write-up

- update - may 2021
- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for scrum maister
- follow latest updates

## Body

UI navigation - from Jira issue view to ScrumMaister components Issue breakdown exmaple and recommendations Sprint analytics generated for the active sprint that discover potential problems AI-modelled retrospective items from the completed sprint Update - May 2021 Scrum Maister is now packed with a plenty of new features and LIVE on Atlassian Marketplace - give it a go! Inspiration As a director of engineering in product company, I spend my days building Agile development teams and departments and making them efficient. I live and breath Scrum and spend 2 years researching how to make Scrum teams successful in my MBA. My other passion is Machine Learning and the ways the AI and machine learning models can improve development practices. When working with teams, I believe in immediate feedback and tools that shift all activities closer to the team, Scrum included. The key to driving successful changes is a persistent presence of the proposed improvements in all aspects of work and levels. What I noticed in most teams that practice Agile development is smaller or larger inconsistencies around the work in Jira - each team have their own way and all them claim being Agile. However, it became evident that, compared to successful teams, failing ones had poorer practices of describing, breaking down their work, following up on it during sprints and discussing pitfalls and potential improvements in the retrospectives. In most cases, it was not about following Scrum by the book, but rather not being present in Jira as a team. To solve that, I came up with an idea of creating an AI that lives in Jira and is a part of the team and works as a super-powered Scrum Master that spots tiniest inefficiencies, slowdowns or blockers and informs the team about them right away. I invited my brother Maksym who is a published scientist and a PhD student in Machine Learning and AI program of EPFL (Switzerland) as a key expert in AI development for the project. The name for the project was easy to come up with - Scrum Master + AI = Scrum mAIster What it does Scrum Maister is a Forge add-on that actively helps teams improve their development, collaboration and SCRUM practices. It natively integrates with Jira and operates as 3 main modules at all stages of development process - before, during and after sprint activities: "Scrummarly" - it uses AI to analyze issue descriptions and then suggests text changes to improve issue breakdown to follow Agile and SCRUM practices. It also suggests a user which issue fields to fill and how to generally improve it for other users. It computes "SM breakdown score" which indicates how well is issue prepared for efficient work in SCRUM or Kanban setting. "Sprint analytics" - active discovery of potential blockers and pitfalls during active sprints across 7 different dynamic dimensions. This module performs assessment of all issues in the sprint, founds the communication, collaboration, progression problems and makes them visible in the sprint analytics dashboard. "Retrospectives" - the model collects and analyzes sprint patterns, breakdown specifics, communication and work progression and provides the baseline for team retros that includes issues that are not visible to a naked eye. Scrum Maister has a potential to become a game-changer in Agile development - its feedback is available immediately, AI text processing and modelling of potential improvements can play a significant role in improving development practices, fostering team work and enhancing not only Scrum but any development framework in any organization that uses Jira as it fits into all stages of SCRUM process as well as other less formal development methodologies (notice the blue monster icon representing Scrum Maister): How I built it I followed the Forge design spirit and utilized Azure PaaS (AppService) an FaaS (Logic apps) in the micro-service architecture pattern - where the data is sent from Forge app and Jira into the cloud-hosted solution API and model APIs. The retrospective analytics is saved into the highly-available geo-redundant Azure CosmosDB. The architecture is shown on the picture below: We used Natural Language Processing model with 2-4 grams and training set of about 2000 issues labeled according to the quality of their description. The privacy and data security is an important factor for the application, we limit the data that leaves Jira to only minimal viable (issue description, numbers of disruptions) and exclude personal or sensitive information. We also do not store the processed data and follow best practices of security for FaaS and PaaS solutions. Challenges I ran into The Forge UI toolset is slightly limited with certain functions being on the roadmap. We had to find the ways to use the existing functionality to achieve our goals. We expect to improve our design, UX and information representation practices as the platform develops. Another challenge was how to apply theory to solving practical problems - we did build the model fairly quick, but getting the training data, creating the API and returning meaningful suggestions to users turned out to be a hard but rewarding work. Accomplishments that I'm proud of When I apply Scrum Maister suggestions to real teams and their backlogs, I can see a huge amount of small improvements that, together, can significantly improve the quality of the product the team develops and the team work itself. If our tool helps at least one team to become more successful, this would me a world to me. What I learned We learned how to build and prototype quickly - the whole project was created within 4 weeks, and forge theory into practice. We are absolutely excited for the next steps in Scrum Maister roadmap and delivering even more advanced machine learning and AI models that will help teams become efficient. What's next for Scrum Maister We will spend the next weeks on improving product quality and reliability - while it works well for the key functions, some corners had to be cut short. We need to implement more robust and user-friendly error handling and cover the code with autotests. Then, the next big step would be to switch from the N-gram model for text generation to the state-of-art deep transfer learning model. We will also work on improving the checks for sprint analytics and retrospective generation. Around this time we expect our first beta customers to arrive. Then, it is all about scaling and listening to the customer feedback. We hope by November, Forge apps will be added to the Atlassian marketplace so that we get access to more customers and follow the Atlassian marketplace best practices. Also, we will work on our design, icon sets and website to make it consistent, enterprise-friendly and proprietary. Our roadmap: Follow latest updates Check out our website and tune in for the updates on functionality and availability: https://scrummaister.com/ <div